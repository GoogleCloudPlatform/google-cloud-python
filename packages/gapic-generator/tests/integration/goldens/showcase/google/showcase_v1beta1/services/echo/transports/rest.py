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
import logging
import json  # type: ignore

from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.api_core import client_options as client_options_lib
from google.api_core import exceptions as core_exceptions
from google.api_core import retry as retries
from google.api_core import rest_helpers
from google.api_core import rest_streaming
from google.api_core import gapic_v1
from google.showcase_v1beta1._compat import transcode_request, trace_http_request
import google.protobuf

from google.protobuf import json_format
from google.api_core import operations_v1
from google.iam.v1 import iam_policy_pb2  # type: ignore
from google.iam.v1 import policy_pb2  # type: ignore
from google.cloud.location import locations_pb2 # type: ignore

from requests import __version__ as requests_version
import dataclasses
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union
import warnings


from google.showcase_v1beta1.types import echo as gs_echo
from google.longrunning import operations_pb2  # type: ignore


from .rest_base import _BaseEchoRestTransport
from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO

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


class EchoRestInterceptor:
    """Interceptor for Echo.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the EchoRestTransport.

    .. code-block:: python
        class MyCustomEchoInterceptor(EchoRestInterceptor):
            def pre_block(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_block(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_echo(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_echo(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_echo_error_details(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_echo_error_details(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_expand(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_expand(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_fail_echo_with_details(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fail_echo_with_details(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_paged_expand(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_paged_expand(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_paged_expand_legacy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_paged_expand_legacy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_paged_expand_legacy_mapped(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_paged_expand_legacy_mapped(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_wait(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_wait(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = EchoRestTransport(interceptor=MyCustomEchoInterceptor())
        client = EchoClient(transport=transport)


    """
    def pre_block(self, request: gs_echo.BlockRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[gs_echo.BlockRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for block

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Echo server.
        """
        return request, metadata

    def post_block(self, response: gs_echo.BlockResponse) -> gs_echo.BlockResponse:
        """Post-rpc interceptor for block

        DEPRECATED. Please use the `post_block_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Echo server but before
        it is returned to user code. This `post_block` interceptor runs
        before the `post_block_with_metadata` interceptor.
        """
        return response

    def post_block_with_metadata(self, response: gs_echo.BlockResponse, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[gs_echo.BlockResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for block

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Echo server but before it is returned to user code.

        We recommend only using this `post_block_with_metadata`
        interceptor in new development instead of the `post_block` interceptor.
        When both interceptors are used, this `post_block_with_metadata` interceptor runs after the
        `post_block` interceptor. The (possibly modified) response returned by
        `post_block` will be passed to
        `post_block_with_metadata`.
        """
        return response, metadata

    def pre_echo(self, request: gs_echo.EchoRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[gs_echo.EchoRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for echo

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Echo server.
        """
        return request, metadata

    def post_echo(self, response: gs_echo.EchoResponse) -> gs_echo.EchoResponse:
        """Post-rpc interceptor for echo

        DEPRECATED. Please use the `post_echo_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Echo server but before
        it is returned to user code. This `post_echo` interceptor runs
        before the `post_echo_with_metadata` interceptor.
        """
        return response

    def post_echo_with_metadata(self, response: gs_echo.EchoResponse, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[gs_echo.EchoResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for echo

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Echo server but before it is returned to user code.

        We recommend only using this `post_echo_with_metadata`
        interceptor in new development instead of the `post_echo` interceptor.
        When both interceptors are used, this `post_echo_with_metadata` interceptor runs after the
        `post_echo` interceptor. The (possibly modified) response returned by
        `post_echo` will be passed to
        `post_echo_with_metadata`.
        """
        return response, metadata

    def pre_echo_error_details(self, request: gs_echo.EchoErrorDetailsRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[gs_echo.EchoErrorDetailsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for echo_error_details

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Echo server.
        """
        return request, metadata

    def post_echo_error_details(self, response: gs_echo.EchoErrorDetailsResponse) -> gs_echo.EchoErrorDetailsResponse:
        """Post-rpc interceptor for echo_error_details

        DEPRECATED. Please use the `post_echo_error_details_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Echo server but before
        it is returned to user code. This `post_echo_error_details` interceptor runs
        before the `post_echo_error_details_with_metadata` interceptor.
        """
        return response

    def post_echo_error_details_with_metadata(self, response: gs_echo.EchoErrorDetailsResponse, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[gs_echo.EchoErrorDetailsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for echo_error_details

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Echo server but before it is returned to user code.

        We recommend only using this `post_echo_error_details_with_metadata`
        interceptor in new development instead of the `post_echo_error_details` interceptor.
        When both interceptors are used, this `post_echo_error_details_with_metadata` interceptor runs after the
        `post_echo_error_details` interceptor. The (possibly modified) response returned by
        `post_echo_error_details` will be passed to
        `post_echo_error_details_with_metadata`.
        """
        return response, metadata

    def pre_expand(self, request: gs_echo.ExpandRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[gs_echo.ExpandRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for expand

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Echo server.
        """
        return request, metadata

    def post_expand(self, response: rest_streaming.ResponseIterator) -> rest_streaming.ResponseIterator:
        """Post-rpc interceptor for expand

        DEPRECATED. Please use the `post_expand_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Echo server but before
        it is returned to user code. This `post_expand` interceptor runs
        before the `post_expand_with_metadata` interceptor.
        """
        return response

    def post_expand_with_metadata(self, response: rest_streaming.ResponseIterator, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[rest_streaming.ResponseIterator, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for expand

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Echo server but before it is returned to user code.

        We recommend only using this `post_expand_with_metadata`
        interceptor in new development instead of the `post_expand` interceptor.
        When both interceptors are used, this `post_expand_with_metadata` interceptor runs after the
        `post_expand` interceptor. The (possibly modified) response returned by
        `post_expand` will be passed to
        `post_expand_with_metadata`.
        """
        return response, metadata

    def pre_fail_echo_with_details(self, request: gs_echo.FailEchoWithDetailsRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[gs_echo.FailEchoWithDetailsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for fail_echo_with_details

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Echo server.
        """
        return request, metadata

    def post_fail_echo_with_details(self, response: gs_echo.FailEchoWithDetailsResponse) -> gs_echo.FailEchoWithDetailsResponse:
        """Post-rpc interceptor for fail_echo_with_details

        DEPRECATED. Please use the `post_fail_echo_with_details_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Echo server but before
        it is returned to user code. This `post_fail_echo_with_details` interceptor runs
        before the `post_fail_echo_with_details_with_metadata` interceptor.
        """
        return response

    def post_fail_echo_with_details_with_metadata(self, response: gs_echo.FailEchoWithDetailsResponse, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[gs_echo.FailEchoWithDetailsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for fail_echo_with_details

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Echo server but before it is returned to user code.

        We recommend only using this `post_fail_echo_with_details_with_metadata`
        interceptor in new development instead of the `post_fail_echo_with_details` interceptor.
        When both interceptors are used, this `post_fail_echo_with_details_with_metadata` interceptor runs after the
        `post_fail_echo_with_details` interceptor. The (possibly modified) response returned by
        `post_fail_echo_with_details` will be passed to
        `post_fail_echo_with_details_with_metadata`.
        """
        return response, metadata

    def pre_paged_expand(self, request: gs_echo.PagedExpandRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[gs_echo.PagedExpandRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for paged_expand

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Echo server.
        """
        return request, metadata

    def post_paged_expand(self, response: gs_echo.PagedExpandResponse) -> gs_echo.PagedExpandResponse:
        """Post-rpc interceptor for paged_expand

        DEPRECATED. Please use the `post_paged_expand_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Echo server but before
        it is returned to user code. This `post_paged_expand` interceptor runs
        before the `post_paged_expand_with_metadata` interceptor.
        """
        return response

    def post_paged_expand_with_metadata(self, response: gs_echo.PagedExpandResponse, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[gs_echo.PagedExpandResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for paged_expand

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Echo server but before it is returned to user code.

        We recommend only using this `post_paged_expand_with_metadata`
        interceptor in new development instead of the `post_paged_expand` interceptor.
        When both interceptors are used, this `post_paged_expand_with_metadata` interceptor runs after the
        `post_paged_expand` interceptor. The (possibly modified) response returned by
        `post_paged_expand` will be passed to
        `post_paged_expand_with_metadata`.
        """
        return response, metadata

    def pre_paged_expand_legacy(self, request: gs_echo.PagedExpandLegacyRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[gs_echo.PagedExpandLegacyRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for paged_expand_legacy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Echo server.
        """
        return request, metadata

    def post_paged_expand_legacy(self, response: gs_echo.PagedExpandResponse) -> gs_echo.PagedExpandResponse:
        """Post-rpc interceptor for paged_expand_legacy

        DEPRECATED. Please use the `post_paged_expand_legacy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Echo server but before
        it is returned to user code. This `post_paged_expand_legacy` interceptor runs
        before the `post_paged_expand_legacy_with_metadata` interceptor.
        """
        return response

    def post_paged_expand_legacy_with_metadata(self, response: gs_echo.PagedExpandResponse, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[gs_echo.PagedExpandResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for paged_expand_legacy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Echo server but before it is returned to user code.

        We recommend only using this `post_paged_expand_legacy_with_metadata`
        interceptor in new development instead of the `post_paged_expand_legacy` interceptor.
        When both interceptors are used, this `post_paged_expand_legacy_with_metadata` interceptor runs after the
        `post_paged_expand_legacy` interceptor. The (possibly modified) response returned by
        `post_paged_expand_legacy` will be passed to
        `post_paged_expand_legacy_with_metadata`.
        """
        return response, metadata

    def pre_paged_expand_legacy_mapped(self, request: gs_echo.PagedExpandRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[gs_echo.PagedExpandRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for paged_expand_legacy_mapped

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Echo server.
        """
        return request, metadata

    def post_paged_expand_legacy_mapped(self, response: gs_echo.PagedExpandLegacyMappedResponse) -> gs_echo.PagedExpandLegacyMappedResponse:
        """Post-rpc interceptor for paged_expand_legacy_mapped

        DEPRECATED. Please use the `post_paged_expand_legacy_mapped_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Echo server but before
        it is returned to user code. This `post_paged_expand_legacy_mapped` interceptor runs
        before the `post_paged_expand_legacy_mapped_with_metadata` interceptor.
        """
        return response

    def post_paged_expand_legacy_mapped_with_metadata(self, response: gs_echo.PagedExpandLegacyMappedResponse, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[gs_echo.PagedExpandLegacyMappedResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for paged_expand_legacy_mapped

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Echo server but before it is returned to user code.

        We recommend only using this `post_paged_expand_legacy_mapped_with_metadata`
        interceptor in new development instead of the `post_paged_expand_legacy_mapped` interceptor.
        When both interceptors are used, this `post_paged_expand_legacy_mapped_with_metadata` interceptor runs after the
        `post_paged_expand_legacy_mapped` interceptor. The (possibly modified) response returned by
        `post_paged_expand_legacy_mapped` will be passed to
        `post_paged_expand_legacy_mapped_with_metadata`.
        """
        return response, metadata

    def pre_wait(self, request: gs_echo.WaitRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[gs_echo.WaitRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for wait

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Echo server.
        """
        return request, metadata

    def post_wait(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for wait

        DEPRECATED. Please use the `post_wait_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Echo server but before
        it is returned to user code. This `post_wait` interceptor runs
        before the `post_wait_with_metadata` interceptor.
        """
        return response

    def post_wait_with_metadata(self, response: operations_pb2.Operation, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for wait

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Echo server but before it is returned to user code.

        We recommend only using this `post_wait_with_metadata`
        interceptor in new development instead of the `post_wait` interceptor.
        When both interceptors are used, this `post_wait_with_metadata` interceptor runs after the
        `post_wait` interceptor. The (possibly modified) response returned by
        `post_wait` will be passed to
        `post_wait_with_metadata`.
        """
        return response, metadata

    def pre_list_locations(
        self, request: locations_pb2.ListLocationsRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[locations_pb2.ListLocationsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_locations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Echo server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the Echo server but before
        it is returned to user code.
        """
        return response

    def pre_get_location(
        self, request: locations_pb2.GetLocationRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[locations_pb2.GetLocationRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_location

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Echo server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the Echo server but before
        it is returned to user code.
        """
        return response

    def pre_set_iam_policy(
        self, request: iam_policy_pb2.SetIamPolicyRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[iam_policy_pb2.SetIamPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Echo server.
        """
        return request, metadata

    def post_set_iam_policy(
        self, response: policy_pb2.Policy
    ) -> policy_pb2.Policy:
        """Post-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the Echo server but before
        it is returned to user code.
        """
        return response

    def pre_get_iam_policy(
        self, request: iam_policy_pb2.GetIamPolicyRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[iam_policy_pb2.GetIamPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Echo server.
        """
        return request, metadata

    def post_get_iam_policy(
        self, response: policy_pb2.Policy
    ) -> policy_pb2.Policy:
        """Post-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the Echo server but before
        it is returned to user code.
        """
        return response

    def pre_test_iam_permissions(
        self, request: iam_policy_pb2.TestIamPermissionsRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[iam_policy_pb2.TestIamPermissionsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Echo server.
        """
        return request, metadata

    def post_test_iam_permissions(
        self, response: iam_policy_pb2.TestIamPermissionsResponse
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the response
        after it is returned by the Echo server but before
        it is returned to user code.
        """
        return response

    def pre_list_operations(
        self, request: operations_pb2.ListOperationsRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[operations_pb2.ListOperationsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_operations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Echo server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the Echo server but before
        it is returned to user code.
        """
        return response

    def pre_get_operation(
        self, request: operations_pb2.GetOperationRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[operations_pb2.GetOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Echo server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the Echo server but before
        it is returned to user code.
        """
        return response

    def pre_delete_operation(
        self, request: operations_pb2.DeleteOperationRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[operations_pb2.DeleteOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Echo server.
        """
        return request, metadata

    def post_delete_operation(
        self, response: None
    ) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the Echo server but before
        it is returned to user code.
        """
        return response

    def pre_cancel_operation(
        self, request: operations_pb2.CancelOperationRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[operations_pb2.CancelOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Echo server.
        """
        return request, metadata

    def post_cancel_operation(
        self, response: None
    ) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the Echo server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class EchoRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: EchoRestInterceptor
    _client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = None


class EchoRestTransport(_BaseEchoRestTransport):
    """REST backend synchronous transport for Echo.

    This service is used showcase the four main types of rpcs -
    unary, server side streaming, client side streaming, and
    bidirectional streaming. This service also exposes methods that
    explicitly implement server delay, and paginated calls. Set the
    'showcase-trailer' metadata key on any method to have the values
    echoed in the response trailers. Set the 'x-goog-request-params'
    metadata key on any method to have the values echoed in the
    response headers.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(self, *,
            host: str = 'localhost:7469',
            credentials: Optional[ga_credentials.Credentials] = None,
            credentials_file: Optional[str] = None,
            scopes: Optional[Sequence[str]] = None,
            client_cert_source_for_mtls: Optional[Callable[[
                ], Tuple[bytes, bytes]]] = None,
            quota_project_id: Optional[str] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            always_use_jwt_access: Optional[bool] = False,
            url_scheme: str = 'https',
            interceptor: Optional[EchoRestInterceptor] = None,
            api_audience: Optional[str] = None,
            client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = None,
            **kwargs,
            ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'localhost:7469').
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
            interceptor (Optional[EchoRestInterceptor]): Interceptor used
                to manipulate requests, request metadata, and responses.
            api_audience (Optional[str]): The intended audience for the API calls
                to the service that will be set when using certain 3rd party
                authentication flows. Audience is typically a resource identifier.
                If not set, the host value will be used as a default.
            client_options (Optional[Union[google.api_core.client_options.ClientOptions, dict]]):
                Custom options for the client, containing options such as
                custom OpenTelemetry tracer providers.
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
            client_options=client_options,
            **kwargs,
        )
        self._session = AuthorizedSession(
            self._credentials, default_host=self.DEFAULT_HOST)
        self._operations_client: Optional[operations_v1.AbstractOperationsClient] = None
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or EchoRestInterceptor()
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
                'google.longrunning.Operations.ListOperations': [
                    {
                        'method': 'get',
                        'uri': '/v1beta1/operations',
                    },
                ],
                'google.longrunning.Operations.GetOperation': [
                    {
                        'method': 'get',
                        'uri': '/v1beta1/{name=operations/**}',
                    },
                ],
                'google.longrunning.Operations.DeleteOperation': [
                    {
                        'method': 'delete',
                        'uri': '/v1beta1/{name=operations/**}',
                    },
                ],
                'google.longrunning.Operations.CancelOperation': [
                    {
                        'method': 'post',
                        'uri': '/v1beta1/{name=operations/**}:cancel',
                    },
                ],
            }

            rest_transport = operations_v1.OperationsRestTransport(
                    host=self._host,
                    # use the credentials which are saved
                    credentials=self._credentials,
                    scopes=self._scopes,
                    http_options=http_options,
                    path_prefix="v1beta1")

            self._operations_client = operations_v1.AbstractOperationsClient(transport=rest_transport)

        # Return the client from cache.
        return self._operations_client

    class _Block(_BaseEchoRestTransport._BaseBlock, EchoRestStub):
        def __hash__(self):
            return hash("EchoRestTransport.Block")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                    )
                trace_ctx.record_response(response)
                return response

        def __call__(self,
                request: gs_echo.BlockRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
                ) -> gs_echo.BlockResponse:
            r"""Call the block method over HTTP.

            Args:
                request (~.gs_echo.BlockRequest):
                    The request object. The request for Block method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gs_echo.BlockResponse:
                    The response for Block method.
            """

            http_options = _BaseEchoRestTransport._BaseBlock._get_http_options()
            request, metadata = self._interceptor.pre_block(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEchoRestTransport._BaseBlock,
                    "_BaseBlock__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.showcase_v1beta1.EchoClient.Block",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Echo",
                        "rpcName": "Block",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EchoRestTransport._Block._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = gs_echo.BlockResponse()
            pb_resp = gs_echo.BlockResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_block(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_block_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = gs_echo.BlockResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                "payload": response_payload,
                "headers":  dict(response.headers),
                "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.showcase_v1beta1.EchoClient.block",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Echo",
                        "rpcName": "Block",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Chat(_BaseEchoRestTransport._BaseChat, EchoRestStub):
        def __hash__(self):
            return hash("EchoRestTransport.Chat")

        def __call__(self,
                request: gs_echo.EchoRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
                ) -> rest_streaming.ResponseIterator:
            raise NotImplementedError(
                "Method Chat is not available over REST transport"
            )
    class _Collect(_BaseEchoRestTransport._BaseCollect, EchoRestStub):
        def __hash__(self):
            return hash("EchoRestTransport.Collect")

        def __call__(self,
                request: gs_echo.EchoRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
                ) -> gs_echo.EchoResponse:
            raise NotImplementedError(
                "Method Collect is not available over REST transport"
            )
    class _Echo(_BaseEchoRestTransport._BaseEcho, EchoRestStub):
        def __hash__(self):
            return hash("EchoRestTransport.Echo")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                    )
                trace_ctx.record_response(response)
                return response

        def __call__(self,
                request: gs_echo.EchoRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
                ) -> gs_echo.EchoResponse:
            r"""Call the echo method over HTTP.

            Args:
                request (~.gs_echo.EchoRequest):
                    The request object. The request message used for the
                Echo, Collect and Chat methods. If
                content or opt are set in this message
                then the request will succeed. If status
                is set in this message then the status
                will be returned as an error.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gs_echo.EchoResponse:
                    The response message for the Echo
                methods.

            """

            http_options = _BaseEchoRestTransport._BaseEcho._get_http_options()
            request, metadata = self._interceptor.pre_echo(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEchoRestTransport._BaseEcho,
                    "_BaseEcho__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.showcase_v1beta1.EchoClient.Echo",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Echo",
                        "rpcName": "Echo",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EchoRestTransport._Echo._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = gs_echo.EchoResponse()
            pb_resp = gs_echo.EchoResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_echo(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_echo_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = gs_echo.EchoResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                "payload": response_payload,
                "headers":  dict(response.headers),
                "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.showcase_v1beta1.EchoClient.echo",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Echo",
                        "rpcName": "Echo",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _EchoErrorDetails(_BaseEchoRestTransport._BaseEchoErrorDetails, EchoRestStub):
        def __hash__(self):
            return hash("EchoRestTransport.EchoErrorDetails")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                    )
                trace_ctx.record_response(response)
                return response

        def __call__(self,
                request: gs_echo.EchoErrorDetailsRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
                ) -> gs_echo.EchoErrorDetailsResponse:
            r"""Call the echo error details method over HTTP.

            Args:
                request (~.gs_echo.EchoErrorDetailsRequest):
                    The request object. The request message used for the
                EchoErrorDetails method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gs_echo.EchoErrorDetailsResponse:
                    The response message used for the
                EchoErrorDetails method.

            """

            http_options = _BaseEchoRestTransport._BaseEchoErrorDetails._get_http_options()
            request, metadata = self._interceptor.pre_echo_error_details(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEchoRestTransport._BaseEchoErrorDetails,
                    "_BaseEchoErrorDetails__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.showcase_v1beta1.EchoClient.EchoErrorDetails",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Echo",
                        "rpcName": "EchoErrorDetails",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EchoRestTransport._EchoErrorDetails._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = gs_echo.EchoErrorDetailsResponse()
            pb_resp = gs_echo.EchoErrorDetailsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_echo_error_details(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_echo_error_details_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = gs_echo.EchoErrorDetailsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                "payload": response_payload,
                "headers":  dict(response.headers),
                "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.showcase_v1beta1.EchoClient.echo_error_details",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Echo",
                        "rpcName": "EchoErrorDetails",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Expand(_BaseEchoRestTransport._BaseExpand, EchoRestStub):
        def __hash__(self):
            return hash("EchoRestTransport.Expand")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                    stream=True,
                    )
                trace_ctx.record_response(response)
                return response

        def __call__(self,
                request: gs_echo.ExpandRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
                ) -> rest_streaming.ResponseIterator:
            r"""Call the expand method over HTTP.

            Args:
                request (~.gs_echo.ExpandRequest):
                    The request object. The request message for the Expand
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gs_echo.EchoResponse:
                    The response message for the Echo
                methods.

            """

            http_options = _BaseEchoRestTransport._BaseExpand._get_http_options()
            request, metadata = self._interceptor.pre_expand(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEchoRestTransport._BaseExpand,
                    "_BaseExpand__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.showcase_v1beta1.EchoClient.Expand",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Echo",
                        "rpcName": "Expand",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EchoRestTransport._Expand._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = rest_streaming.ResponseIterator(response, gs_echo.EchoResponse)
            resp = self._interceptor.post_expand(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_expand_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                http_response = {
                "headers":  dict(response.headers),
                "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.showcase_v1beta1.EchoClient.expand",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Echo",
                        "rpcName": "Expand",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _FailEchoWithDetails(_BaseEchoRestTransport._BaseFailEchoWithDetails, EchoRestStub):
        def __hash__(self):
            return hash("EchoRestTransport.FailEchoWithDetails")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                    )
                trace_ctx.record_response(response)
                return response

        def __call__(self,
                request: gs_echo.FailEchoWithDetailsRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
                ) -> gs_echo.FailEchoWithDetailsResponse:
            r"""Call the fail echo with details method over HTTP.

            Args:
                request (~.gs_echo.FailEchoWithDetailsRequest):
                    The request object. The request message used for the
                FailEchoWithDetails method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gs_echo.FailEchoWithDetailsResponse:
                    The response message declared (but
                never used) for the FailEchoWithDetails
                method.

            """

            http_options = _BaseEchoRestTransport._BaseFailEchoWithDetails._get_http_options()
            request, metadata = self._interceptor.pre_fail_echo_with_details(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEchoRestTransport._BaseFailEchoWithDetails,
                    "_BaseFailEchoWithDetails__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.showcase_v1beta1.EchoClient.FailEchoWithDetails",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Echo",
                        "rpcName": "FailEchoWithDetails",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EchoRestTransport._FailEchoWithDetails._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = gs_echo.FailEchoWithDetailsResponse()
            pb_resp = gs_echo.FailEchoWithDetailsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_fail_echo_with_details(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_fail_echo_with_details_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = gs_echo.FailEchoWithDetailsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                "payload": response_payload,
                "headers":  dict(response.headers),
                "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.showcase_v1beta1.EchoClient.fail_echo_with_details",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Echo",
                        "rpcName": "FailEchoWithDetails",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _PagedExpand(_BaseEchoRestTransport._BasePagedExpand, EchoRestStub):
        def __hash__(self):
            return hash("EchoRestTransport.PagedExpand")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                    )
                trace_ctx.record_response(response)
                return response

        def __call__(self,
                request: gs_echo.PagedExpandRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
                ) -> gs_echo.PagedExpandResponse:
            r"""Call the paged expand method over HTTP.

            Args:
                request (~.gs_echo.PagedExpandRequest):
                    The request object. The request for the PagedExpand
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gs_echo.PagedExpandResponse:
                    The response for the PagedExpand
                method.

            """

            http_options = _BaseEchoRestTransport._BasePagedExpand._get_http_options()
            request, metadata = self._interceptor.pre_paged_expand(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEchoRestTransport._BasePagedExpand,
                    "_BasePagedExpand__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.showcase_v1beta1.EchoClient.PagedExpand",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Echo",
                        "rpcName": "PagedExpand",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EchoRestTransport._PagedExpand._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = gs_echo.PagedExpandResponse()
            pb_resp = gs_echo.PagedExpandResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_paged_expand(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_paged_expand_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = gs_echo.PagedExpandResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                "payload": response_payload,
                "headers":  dict(response.headers),
                "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.showcase_v1beta1.EchoClient.paged_expand",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Echo",
                        "rpcName": "PagedExpand",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _PagedExpandLegacy(_BaseEchoRestTransport._BasePagedExpandLegacy, EchoRestStub):
        def __hash__(self):
            return hash("EchoRestTransport.PagedExpandLegacy")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                    )
                trace_ctx.record_response(response)
                return response

        def __call__(self,
                request: gs_echo.PagedExpandLegacyRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
                ) -> gs_echo.PagedExpandResponse:
            r"""Call the paged expand legacy method over HTTP.

            Args:
                request (~.gs_echo.PagedExpandLegacyRequest):
                    The request object. The request for the PagedExpandLegacy
                method.  This is a pattern used by some
                legacy APIs. New APIs should NOT use
                this pattern, but rather something like
                PagedExpandRequest which conforms to
                aip.dev/158.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gs_echo.PagedExpandResponse:
                    The response for the PagedExpand
                method.

            """

            http_options = _BaseEchoRestTransport._BasePagedExpandLegacy._get_http_options()
            request, metadata = self._interceptor.pre_paged_expand_legacy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEchoRestTransport._BasePagedExpandLegacy,
                    "_BasePagedExpandLegacy__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.showcase_v1beta1.EchoClient.PagedExpandLegacy",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Echo",
                        "rpcName": "PagedExpandLegacy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EchoRestTransport._PagedExpandLegacy._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = gs_echo.PagedExpandResponse()
            pb_resp = gs_echo.PagedExpandResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_paged_expand_legacy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_paged_expand_legacy_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = gs_echo.PagedExpandResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                "payload": response_payload,
                "headers":  dict(response.headers),
                "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.showcase_v1beta1.EchoClient.paged_expand_legacy",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Echo",
                        "rpcName": "PagedExpandLegacy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _PagedExpandLegacyMapped(_BaseEchoRestTransport._BasePagedExpandLegacyMapped, EchoRestStub):
        def __hash__(self):
            return hash("EchoRestTransport.PagedExpandLegacyMapped")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                    )
                trace_ctx.record_response(response)
                return response

        def __call__(self,
                request: gs_echo.PagedExpandRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
                ) -> gs_echo.PagedExpandLegacyMappedResponse:
            r"""Call the paged expand legacy
        mapped method over HTTP.

            Args:
                request (~.gs_echo.PagedExpandRequest):
                    The request object. The request for the PagedExpand
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gs_echo.PagedExpandLegacyMappedResponse:

            """

            http_options = _BaseEchoRestTransport._BasePagedExpandLegacyMapped._get_http_options()
            request, metadata = self._interceptor.pre_paged_expand_legacy_mapped(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEchoRestTransport._BasePagedExpandLegacyMapped,
                    "_BasePagedExpandLegacyMapped__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.showcase_v1beta1.EchoClient.PagedExpandLegacyMapped",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Echo",
                        "rpcName": "PagedExpandLegacyMapped",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EchoRestTransport._PagedExpandLegacyMapped._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = gs_echo.PagedExpandLegacyMappedResponse()
            pb_resp = gs_echo.PagedExpandLegacyMappedResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_paged_expand_legacy_mapped(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_paged_expand_legacy_mapped_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = gs_echo.PagedExpandLegacyMappedResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                "payload": response_payload,
                "headers":  dict(response.headers),
                "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.showcase_v1beta1.EchoClient.paged_expand_legacy_mapped",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Echo",
                        "rpcName": "PagedExpandLegacyMapped",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Wait(_BaseEchoRestTransport._BaseWait, EchoRestStub):
        def __hash__(self):
            return hash("EchoRestTransport.Wait")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                    )
                trace_ctx.record_response(response)
                return response

        def __call__(self,
                request: gs_echo.WaitRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: Optional[float]=None,
                metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
                ) -> operations_pb2.Operation:
            r"""Call the wait method over HTTP.

            Args:
                request (~.gs_echo.WaitRequest):
                    The request object. The request for Wait method.
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

            http_options = _BaseEchoRestTransport._BaseWait._get_http_options()
            request, metadata = self._interceptor.pre_wait(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEchoRestTransport._BaseWait,
                    "_BaseWait__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.showcase_v1beta1.EchoClient.Wait",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Echo",
                        "rpcName": "Wait",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EchoRestTransport._Wait._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_wait(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_wait_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                "payload": response_payload,
                "headers":  dict(response.headers),
                "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.showcase_v1beta1.EchoClient.wait",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Echo",
                        "rpcName": "Wait",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def block(self) -> Callable[
            [gs_echo.BlockRequest],
            gs_echo.BlockResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Block(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    @property
    def chat(self) -> Callable[
            [gs_echo.EchoRequest],
            gs_echo.EchoResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Chat(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    @property
    def collect(self) -> Callable[
            [gs_echo.EchoRequest],
            gs_echo.EchoResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Collect(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    @property
    def echo(self) -> Callable[
            [gs_echo.EchoRequest],
            gs_echo.EchoResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Echo(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    @property
    def echo_error_details(self) -> Callable[
            [gs_echo.EchoErrorDetailsRequest],
            gs_echo.EchoErrorDetailsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._EchoErrorDetails(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    @property
    def expand(self) -> Callable[
            [gs_echo.ExpandRequest],
            gs_echo.EchoResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Expand(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    @property
    def fail_echo_with_details(self) -> Callable[
            [gs_echo.FailEchoWithDetailsRequest],
            gs_echo.FailEchoWithDetailsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FailEchoWithDetails(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    @property
    def paged_expand(self) -> Callable[
            [gs_echo.PagedExpandRequest],
            gs_echo.PagedExpandResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._PagedExpand(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    @property
    def paged_expand_legacy(self) -> Callable[
            [gs_echo.PagedExpandLegacyRequest],
            gs_echo.PagedExpandResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._PagedExpandLegacy(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    @property
    def paged_expand_legacy_mapped(self) -> Callable[
            [gs_echo.PagedExpandRequest],
            gs_echo.PagedExpandLegacyMappedResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._PagedExpandLegacyMapped(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    @property
    def wait(self) -> Callable[
            [gs_echo.WaitRequest],
            operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Wait(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    @property
    def list_locations(self):
        return self._ListLocations(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    class _ListLocations(_BaseEchoRestTransport._BaseListLocations, EchoRestStub):
        def __hash__(self):
            return hash("EchoRestTransport.ListLocations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    )
                trace_ctx.record_response(response)
                return response

        def __call__(self,
            request: locations_pb2.ListLocationsRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: Optional[float]=None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
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

            http_options = _BaseEchoRestTransport._BaseListLocations._get_http_options()
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEchoRestTransport._BaseListLocations,
                    "_BaseListLocations__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.showcase_v1beta1.EchoClient.ListLocations",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Echo",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EchoRestTransport._ListLocations._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = locations_pb2.ListLocationsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_list_locations(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers":  dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.showcase_v1beta1.EchoAsyncClient.ListLocations",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Echo",
                        "rpcName": "ListLocations",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    class _GetLocation(_BaseEchoRestTransport._BaseGetLocation, EchoRestStub):
        def __hash__(self):
            return hash("EchoRestTransport.GetLocation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    )
                trace_ctx.record_response(response)
                return response

        def __call__(self,
            request: locations_pb2.GetLocationRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: Optional[float]=None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
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

            http_options = _BaseEchoRestTransport._BaseGetLocation._get_http_options()
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEchoRestTransport._BaseGetLocation,
                    "_BaseGetLocation__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.showcase_v1beta1.EchoClient.GetLocation",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Echo",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EchoRestTransport._GetLocation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = locations_pb2.Location()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_get_location(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers":  dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.showcase_v1beta1.EchoAsyncClient.GetLocation",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Echo",
                        "rpcName": "GetLocation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def set_iam_policy(self):
        return self._SetIamPolicy(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    class _SetIamPolicy(_BaseEchoRestTransport._BaseSetIamPolicy, EchoRestStub):
        def __hash__(self):
            return hash("EchoRestTransport.SetIamPolicy")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                    )
                trace_ctx.record_response(response)
                return response

        def __call__(self,
            request: iam_policy_pb2.SetIamPolicyRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: Optional[float]=None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
            ) -> policy_pb2.Policy:

            r"""Call the set iam policy method over HTTP.

            Args:
                request (iam_policy_pb2.SetIamPolicyRequest):
                    The request object for SetIamPolicy method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                policy_pb2.Policy: Response from SetIamPolicy method.
            """

            http_options = _BaseEchoRestTransport._BaseSetIamPolicy._get_http_options()
            request, metadata = self._interceptor.pre_set_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEchoRestTransport._BaseSetIamPolicy,
                    "_BaseSetIamPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.showcase_v1beta1.EchoClient.SetIamPolicy",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Echo",
                        "rpcName": "SetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EchoRestTransport._SetIamPolicy._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = policy_pb2.Policy()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_set_iam_policy(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers":  dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.showcase_v1beta1.EchoAsyncClient.SetIamPolicy",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Echo",
                        "rpcName": "SetIamPolicy",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def get_iam_policy(self):
        return self._GetIamPolicy(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    class _GetIamPolicy(_BaseEchoRestTransport._BaseGetIamPolicy, EchoRestStub):
        def __hash__(self):
            return hash("EchoRestTransport.GetIamPolicy")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    )
                trace_ctx.record_response(response)
                return response

        def __call__(self,
            request: iam_policy_pb2.GetIamPolicyRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: Optional[float]=None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
            ) -> policy_pb2.Policy:

            r"""Call the get iam policy method over HTTP.

            Args:
                request (iam_policy_pb2.GetIamPolicyRequest):
                    The request object for GetIamPolicy method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                policy_pb2.Policy: Response from GetIamPolicy method.
            """

            http_options = _BaseEchoRestTransport._BaseGetIamPolicy._get_http_options()
            request, metadata = self._interceptor.pre_get_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEchoRestTransport._BaseGetIamPolicy,
                    "_BaseGetIamPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.showcase_v1beta1.EchoClient.GetIamPolicy",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Echo",
                        "rpcName": "GetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EchoRestTransport._GetIamPolicy._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = policy_pb2.Policy()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_get_iam_policy(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers":  dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.showcase_v1beta1.EchoAsyncClient.GetIamPolicy",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Echo",
                        "rpcName": "GetIamPolicy",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def test_iam_permissions(self):
        return self._TestIamPermissions(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    class _TestIamPermissions(_BaseEchoRestTransport._BaseTestIamPermissions, EchoRestStub):
        def __hash__(self):
            return hash("EchoRestTransport.TestIamPermissions")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                    )
                trace_ctx.record_response(response)
                return response

        def __call__(self,
            request: iam_policy_pb2.TestIamPermissionsRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: Optional[float]=None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
            ) -> iam_policy_pb2.TestIamPermissionsResponse:

            r"""Call the test iam permissions method over HTTP.

            Args:
                request (iam_policy_pb2.TestIamPermissionsRequest):
                    The request object for TestIamPermissions method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                iam_policy_pb2.TestIamPermissionsResponse: Response from TestIamPermissions method.
            """

            http_options = _BaseEchoRestTransport._BaseTestIamPermissions._get_http_options()
            request, metadata = self._interceptor.pre_test_iam_permissions(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEchoRestTransport._BaseTestIamPermissions,
                    "_BaseTestIamPermissions__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.showcase_v1beta1.EchoClient.TestIamPermissions",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Echo",
                        "rpcName": "TestIamPermissions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EchoRestTransport._TestIamPermissions._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = iam_policy_pb2.TestIamPermissionsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_test_iam_permissions(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers":  dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.showcase_v1beta1.EchoAsyncClient.TestIamPermissions",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Echo",
                        "rpcName": "TestIamPermissions",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def list_operations(self):
        return self._ListOperations(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    class _ListOperations(_BaseEchoRestTransport._BaseListOperations, EchoRestStub):
        def __hash__(self):
            return hash("EchoRestTransport.ListOperations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    )
                trace_ctx.record_response(response)
                return response

        def __call__(self,
            request: operations_pb2.ListOperationsRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: Optional[float]=None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
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

            http_options = _BaseEchoRestTransport._BaseListOperations._get_http_options()
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEchoRestTransport._BaseListOperations,
                    "_BaseListOperations__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.showcase_v1beta1.EchoClient.ListOperations",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Echo",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EchoRestTransport._ListOperations._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = operations_pb2.ListOperationsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_list_operations(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers":  dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.showcase_v1beta1.EchoAsyncClient.ListOperations",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Echo",
                        "rpcName": "ListOperations",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    class _GetOperation(_BaseEchoRestTransport._BaseGetOperation, EchoRestStub):
        def __hash__(self):
            return hash("EchoRestTransport.GetOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    )
                trace_ctx.record_response(response)
                return response

        def __call__(self,
            request: operations_pb2.GetOperationRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: Optional[float]=None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
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

            http_options = _BaseEchoRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEchoRestTransport._BaseGetOperation,
                    "_BaseGetOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.showcase_v1beta1.EchoClient.GetOperation",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Echo",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EchoRestTransport._GetOperation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = operations_pb2.Operation()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_get_operation(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers":  dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.showcase_v1beta1.EchoAsyncClient.GetOperation",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Echo",
                        "rpcName": "GetOperation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def delete_operation(self):
        return self._DeleteOperation(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    class _DeleteOperation(_BaseEchoRestTransport._BaseDeleteOperation, EchoRestStub):
        def __hash__(self):
            return hash("EchoRestTransport.DeleteOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    )
                trace_ctx.record_response(response)
                return response

        def __call__(self,
            request: operations_pb2.DeleteOperationRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: Optional[float]=None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
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

            http_options = _BaseEchoRestTransport._BaseDeleteOperation._get_http_options()
            request, metadata = self._interceptor.pre_delete_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEchoRestTransport._BaseDeleteOperation,
                    "_BaseDeleteOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.showcase_v1beta1.EchoClient.DeleteOperation",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Echo",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EchoRestTransport._DeleteOperation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            return self._interceptor.post_delete_operation(None)

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    class _CancelOperation(_BaseEchoRestTransport._BaseCancelOperation, EchoRestStub):
        def __hash__(self):
            return hash("EchoRestTransport.CancelOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    )
                trace_ctx.record_response(response)
                return response

        def __call__(self,
            request: operations_pb2.CancelOperationRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: Optional[float]=None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
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

            http_options = _BaseEchoRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEchoRestTransport._BaseCancelOperation,
                    "_BaseCancelOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.showcase_v1beta1.EchoClient.CancelOperation",
                    extra = {
                        "serviceName": "google.showcase.v1beta1.Echo",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EchoRestTransport._CancelOperation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            return self._interceptor.post_cancel_operation(None)

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__=(
    'EchoRestTransport',
)
