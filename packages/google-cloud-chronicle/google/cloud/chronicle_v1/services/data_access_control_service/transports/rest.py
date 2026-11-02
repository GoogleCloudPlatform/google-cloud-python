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
from google.cloud.chronicle_v1.types import data_access_control

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseDataAccessControlServiceRestTransport

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


class DataAccessControlServiceRestInterceptor:
    """Interceptor for DataAccessControlService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the DataAccessControlServiceRestTransport.

    .. code-block:: python
        class MyCustomDataAccessControlServiceInterceptor(DataAccessControlServiceRestInterceptor):
            def pre_create_data_access_label(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_data_access_label(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_data_access_scope(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_data_access_scope(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_data_access_label(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_data_access_scope(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_data_access_label(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_data_access_label(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_data_access_scope(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_data_access_scope(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_data_access_labels(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_data_access_labels(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_data_access_scopes(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_data_access_scopes(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_data_access_label(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_data_access_label(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_data_access_scope(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_data_access_scope(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = DataAccessControlServiceRestTransport(interceptor=MyCustomDataAccessControlServiceInterceptor())
        client = DataAccessControlServiceClient(transport=transport)


    """

    def pre_create_data_access_label(
        self,
        request: data_access_control.CreateDataAccessLabelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_access_control.CreateDataAccessLabelRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_data_access_label

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataAccessControlService server.
        """
        return request, metadata

    def post_create_data_access_label(
        self, response: data_access_control.DataAccessLabel
    ) -> data_access_control.DataAccessLabel:
        """Post-rpc interceptor for create_data_access_label

        DEPRECATED. Please use the `post_create_data_access_label_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataAccessControlService server but before
        it is returned to user code. This `post_create_data_access_label` interceptor runs
        before the `post_create_data_access_label_with_metadata` interceptor.
        """
        return response

    def post_create_data_access_label_with_metadata(
        self,
        response: data_access_control.DataAccessLabel,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_access_control.DataAccessLabel, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for create_data_access_label

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataAccessControlService server but before it is returned to user code.

        We recommend only using this `post_create_data_access_label_with_metadata`
        interceptor in new development instead of the `post_create_data_access_label` interceptor.
        When both interceptors are used, this `post_create_data_access_label_with_metadata` interceptor runs after the
        `post_create_data_access_label` interceptor. The (possibly modified) response returned by
        `post_create_data_access_label` will be passed to
        `post_create_data_access_label_with_metadata`.
        """
        return response, metadata

    def pre_create_data_access_scope(
        self,
        request: data_access_control.CreateDataAccessScopeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_access_control.CreateDataAccessScopeRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_data_access_scope

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataAccessControlService server.
        """
        return request, metadata

    def post_create_data_access_scope(
        self, response: data_access_control.DataAccessScope
    ) -> data_access_control.DataAccessScope:
        """Post-rpc interceptor for create_data_access_scope

        DEPRECATED. Please use the `post_create_data_access_scope_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataAccessControlService server but before
        it is returned to user code. This `post_create_data_access_scope` interceptor runs
        before the `post_create_data_access_scope_with_metadata` interceptor.
        """
        return response

    def post_create_data_access_scope_with_metadata(
        self,
        response: data_access_control.DataAccessScope,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_access_control.DataAccessScope, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for create_data_access_scope

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataAccessControlService server but before it is returned to user code.

        We recommend only using this `post_create_data_access_scope_with_metadata`
        interceptor in new development instead of the `post_create_data_access_scope` interceptor.
        When both interceptors are used, this `post_create_data_access_scope_with_metadata` interceptor runs after the
        `post_create_data_access_scope` interceptor. The (possibly modified) response returned by
        `post_create_data_access_scope` will be passed to
        `post_create_data_access_scope_with_metadata`.
        """
        return response, metadata

    def pre_delete_data_access_label(
        self,
        request: data_access_control.DeleteDataAccessLabelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_access_control.DeleteDataAccessLabelRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_data_access_label

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataAccessControlService server.
        """
        return request, metadata

    def pre_delete_data_access_scope(
        self,
        request: data_access_control.DeleteDataAccessScopeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_access_control.DeleteDataAccessScopeRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_data_access_scope

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataAccessControlService server.
        """
        return request, metadata

    def pre_get_data_access_label(
        self,
        request: data_access_control.GetDataAccessLabelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_access_control.GetDataAccessLabelRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_data_access_label

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataAccessControlService server.
        """
        return request, metadata

    def post_get_data_access_label(
        self, response: data_access_control.DataAccessLabel
    ) -> data_access_control.DataAccessLabel:
        """Post-rpc interceptor for get_data_access_label

        DEPRECATED. Please use the `post_get_data_access_label_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataAccessControlService server but before
        it is returned to user code. This `post_get_data_access_label` interceptor runs
        before the `post_get_data_access_label_with_metadata` interceptor.
        """
        return response

    def post_get_data_access_label_with_metadata(
        self,
        response: data_access_control.DataAccessLabel,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_access_control.DataAccessLabel, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_data_access_label

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataAccessControlService server but before it is returned to user code.

        We recommend only using this `post_get_data_access_label_with_metadata`
        interceptor in new development instead of the `post_get_data_access_label` interceptor.
        When both interceptors are used, this `post_get_data_access_label_with_metadata` interceptor runs after the
        `post_get_data_access_label` interceptor. The (possibly modified) response returned by
        `post_get_data_access_label` will be passed to
        `post_get_data_access_label_with_metadata`.
        """
        return response, metadata

    def pre_get_data_access_scope(
        self,
        request: data_access_control.GetDataAccessScopeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_access_control.GetDataAccessScopeRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_data_access_scope

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataAccessControlService server.
        """
        return request, metadata

    def post_get_data_access_scope(
        self, response: data_access_control.DataAccessScope
    ) -> data_access_control.DataAccessScope:
        """Post-rpc interceptor for get_data_access_scope

        DEPRECATED. Please use the `post_get_data_access_scope_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataAccessControlService server but before
        it is returned to user code. This `post_get_data_access_scope` interceptor runs
        before the `post_get_data_access_scope_with_metadata` interceptor.
        """
        return response

    def post_get_data_access_scope_with_metadata(
        self,
        response: data_access_control.DataAccessScope,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_access_control.DataAccessScope, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_data_access_scope

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataAccessControlService server but before it is returned to user code.

        We recommend only using this `post_get_data_access_scope_with_metadata`
        interceptor in new development instead of the `post_get_data_access_scope` interceptor.
        When both interceptors are used, this `post_get_data_access_scope_with_metadata` interceptor runs after the
        `post_get_data_access_scope` interceptor. The (possibly modified) response returned by
        `post_get_data_access_scope` will be passed to
        `post_get_data_access_scope_with_metadata`.
        """
        return response, metadata

    def pre_list_data_access_labels(
        self,
        request: data_access_control.ListDataAccessLabelsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_access_control.ListDataAccessLabelsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_data_access_labels

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataAccessControlService server.
        """
        return request, metadata

    def post_list_data_access_labels(
        self, response: data_access_control.ListDataAccessLabelsResponse
    ) -> data_access_control.ListDataAccessLabelsResponse:
        """Post-rpc interceptor for list_data_access_labels

        DEPRECATED. Please use the `post_list_data_access_labels_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataAccessControlService server but before
        it is returned to user code. This `post_list_data_access_labels` interceptor runs
        before the `post_list_data_access_labels_with_metadata` interceptor.
        """
        return response

    def post_list_data_access_labels_with_metadata(
        self,
        response: data_access_control.ListDataAccessLabelsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_access_control.ListDataAccessLabelsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_data_access_labels

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataAccessControlService server but before it is returned to user code.

        We recommend only using this `post_list_data_access_labels_with_metadata`
        interceptor in new development instead of the `post_list_data_access_labels` interceptor.
        When both interceptors are used, this `post_list_data_access_labels_with_metadata` interceptor runs after the
        `post_list_data_access_labels` interceptor. The (possibly modified) response returned by
        `post_list_data_access_labels` will be passed to
        `post_list_data_access_labels_with_metadata`.
        """
        return response, metadata

    def pre_list_data_access_scopes(
        self,
        request: data_access_control.ListDataAccessScopesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_access_control.ListDataAccessScopesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_data_access_scopes

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataAccessControlService server.
        """
        return request, metadata

    def post_list_data_access_scopes(
        self, response: data_access_control.ListDataAccessScopesResponse
    ) -> data_access_control.ListDataAccessScopesResponse:
        """Post-rpc interceptor for list_data_access_scopes

        DEPRECATED. Please use the `post_list_data_access_scopes_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataAccessControlService server but before
        it is returned to user code. This `post_list_data_access_scopes` interceptor runs
        before the `post_list_data_access_scopes_with_metadata` interceptor.
        """
        return response

    def post_list_data_access_scopes_with_metadata(
        self,
        response: data_access_control.ListDataAccessScopesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_access_control.ListDataAccessScopesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_data_access_scopes

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataAccessControlService server but before it is returned to user code.

        We recommend only using this `post_list_data_access_scopes_with_metadata`
        interceptor in new development instead of the `post_list_data_access_scopes` interceptor.
        When both interceptors are used, this `post_list_data_access_scopes_with_metadata` interceptor runs after the
        `post_list_data_access_scopes` interceptor. The (possibly modified) response returned by
        `post_list_data_access_scopes` will be passed to
        `post_list_data_access_scopes_with_metadata`.
        """
        return response, metadata

    def pre_update_data_access_label(
        self,
        request: data_access_control.UpdateDataAccessLabelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_access_control.UpdateDataAccessLabelRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_data_access_label

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataAccessControlService server.
        """
        return request, metadata

    def post_update_data_access_label(
        self, response: data_access_control.DataAccessLabel
    ) -> data_access_control.DataAccessLabel:
        """Post-rpc interceptor for update_data_access_label

        DEPRECATED. Please use the `post_update_data_access_label_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataAccessControlService server but before
        it is returned to user code. This `post_update_data_access_label` interceptor runs
        before the `post_update_data_access_label_with_metadata` interceptor.
        """
        return response

    def post_update_data_access_label_with_metadata(
        self,
        response: data_access_control.DataAccessLabel,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_access_control.DataAccessLabel, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for update_data_access_label

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataAccessControlService server but before it is returned to user code.

        We recommend only using this `post_update_data_access_label_with_metadata`
        interceptor in new development instead of the `post_update_data_access_label` interceptor.
        When both interceptors are used, this `post_update_data_access_label_with_metadata` interceptor runs after the
        `post_update_data_access_label` interceptor. The (possibly modified) response returned by
        `post_update_data_access_label` will be passed to
        `post_update_data_access_label_with_metadata`.
        """
        return response, metadata

    def pre_update_data_access_scope(
        self,
        request: data_access_control.UpdateDataAccessScopeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_access_control.UpdateDataAccessScopeRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_data_access_scope

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataAccessControlService server.
        """
        return request, metadata

    def post_update_data_access_scope(
        self, response: data_access_control.DataAccessScope
    ) -> data_access_control.DataAccessScope:
        """Post-rpc interceptor for update_data_access_scope

        DEPRECATED. Please use the `post_update_data_access_scope_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataAccessControlService server but before
        it is returned to user code. This `post_update_data_access_scope` interceptor runs
        before the `post_update_data_access_scope_with_metadata` interceptor.
        """
        return response

    def post_update_data_access_scope_with_metadata(
        self,
        response: data_access_control.DataAccessScope,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_access_control.DataAccessScope, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for update_data_access_scope

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataAccessControlService server but before it is returned to user code.

        We recommend only using this `post_update_data_access_scope_with_metadata`
        interceptor in new development instead of the `post_update_data_access_scope` interceptor.
        When both interceptors are used, this `post_update_data_access_scope_with_metadata` interceptor runs after the
        `post_update_data_access_scope` interceptor. The (possibly modified) response returned by
        `post_update_data_access_scope` will be passed to
        `post_update_data_access_scope_with_metadata`.
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
        before they are sent to the DataAccessControlService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the DataAccessControlService server but before
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
        before they are sent to the DataAccessControlService server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the DataAccessControlService server but before
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
        before they are sent to the DataAccessControlService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the DataAccessControlService server but before
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
        before they are sent to the DataAccessControlService server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the DataAccessControlService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class DataAccessControlServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: DataAccessControlServiceRestInterceptor


class DataAccessControlServiceRestTransport(_BaseDataAccessControlServiceRestTransport):
    """REST backend synchronous transport for DataAccessControlService.

    DataAccessControlService exposes resources and endpoints
    related to data access control.

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
        interceptor: Optional[DataAccessControlServiceRestInterceptor] = None,
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
            interceptor (Optional[DataAccessControlServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or DataAccessControlServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CreateDataAccessLabel(
        _BaseDataAccessControlServiceRestTransport._BaseCreateDataAccessLabel,
        DataAccessControlServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataAccessControlServiceRestTransport.CreateDataAccessLabel")

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
            request: data_access_control.CreateDataAccessLabelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> data_access_control.DataAccessLabel:
            r"""Call the create data access label method over HTTP.

            Args:
                request (~.data_access_control.CreateDataAccessLabelRequest):
                    The request object. Request message for
                CreateDataAccessLabel.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.data_access_control.DataAccessLabel:
                    A DataAccessLabel is a label on
                events to define user access to data.

            """

            http_options = _BaseDataAccessControlServiceRestTransport._BaseCreateDataAccessLabel._get_http_options()
            request, metadata = self._interceptor.pre_create_data_access_label(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataAccessControlServiceRestTransport._BaseCreateDataAccessLabel,
                    "_BaseCreateDataAccessLabel__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.DataAccessControlServiceClient.CreateDataAccessLabel",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataAccessControlService",
                        "rpcName": "CreateDataAccessLabel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataAccessControlServiceRestTransport._CreateDataAccessLabel._get_response(
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
            resp = data_access_control.DataAccessLabel()
            pb_resp = data_access_control.DataAccessLabel.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_data_access_label(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_data_access_label_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = data_access_control.DataAccessLabel.to_json(
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
                    "Received response for google.cloud.chronicle_v1.DataAccessControlServiceClient.create_data_access_label",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataAccessControlService",
                        "rpcName": "CreateDataAccessLabel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateDataAccessScope(
        _BaseDataAccessControlServiceRestTransport._BaseCreateDataAccessScope,
        DataAccessControlServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataAccessControlServiceRestTransport.CreateDataAccessScope")

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
            request: data_access_control.CreateDataAccessScopeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> data_access_control.DataAccessScope:
            r"""Call the create data access scope method over HTTP.

            Args:
                request (~.data_access_control.CreateDataAccessScopeRequest):
                    The request object. Request message for
                CreateDataAccessScope.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.data_access_control.DataAccessScope:
                    A DataAccessScope is a boolean
                expression of data access labels used to
                restrict access to data for users.

            """

            http_options = _BaseDataAccessControlServiceRestTransport._BaseCreateDataAccessScope._get_http_options()
            request, metadata = self._interceptor.pre_create_data_access_scope(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataAccessControlServiceRestTransport._BaseCreateDataAccessScope,
                    "_BaseCreateDataAccessScope__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.DataAccessControlServiceClient.CreateDataAccessScope",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataAccessControlService",
                        "rpcName": "CreateDataAccessScope",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataAccessControlServiceRestTransport._CreateDataAccessScope._get_response(
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
            resp = data_access_control.DataAccessScope()
            pb_resp = data_access_control.DataAccessScope.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_data_access_scope(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_data_access_scope_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = data_access_control.DataAccessScope.to_json(
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
                    "Received response for google.cloud.chronicle_v1.DataAccessControlServiceClient.create_data_access_scope",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataAccessControlService",
                        "rpcName": "CreateDataAccessScope",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteDataAccessLabel(
        _BaseDataAccessControlServiceRestTransport._BaseDeleteDataAccessLabel,
        DataAccessControlServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataAccessControlServiceRestTransport.DeleteDataAccessLabel")

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
            request: data_access_control.DeleteDataAccessLabelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete data access label method over HTTP.

            Args:
                request (~.data_access_control.DeleteDataAccessLabelRequest):
                    The request object. Request message to delete a data
                access label.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseDataAccessControlServiceRestTransport._BaseDeleteDataAccessLabel._get_http_options()
            request, metadata = self._interceptor.pre_delete_data_access_label(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataAccessControlServiceRestTransport._BaseDeleteDataAccessLabel,
                    "_BaseDeleteDataAccessLabel__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.DataAccessControlServiceClient.DeleteDataAccessLabel",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataAccessControlService",
                        "rpcName": "DeleteDataAccessLabel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataAccessControlServiceRestTransport._DeleteDataAccessLabel._get_response(
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

    class _DeleteDataAccessScope(
        _BaseDataAccessControlServiceRestTransport._BaseDeleteDataAccessScope,
        DataAccessControlServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataAccessControlServiceRestTransport.DeleteDataAccessScope")

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
            request: data_access_control.DeleteDataAccessScopeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete data access scope method over HTTP.

            Args:
                request (~.data_access_control.DeleteDataAccessScopeRequest):
                    The request object. Request message to delete a data
                access scope.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseDataAccessControlServiceRestTransport._BaseDeleteDataAccessScope._get_http_options()
            request, metadata = self._interceptor.pre_delete_data_access_scope(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataAccessControlServiceRestTransport._BaseDeleteDataAccessScope,
                    "_BaseDeleteDataAccessScope__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.DataAccessControlServiceClient.DeleteDataAccessScope",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataAccessControlService",
                        "rpcName": "DeleteDataAccessScope",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataAccessControlServiceRestTransport._DeleteDataAccessScope._get_response(
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

    class _GetDataAccessLabel(
        _BaseDataAccessControlServiceRestTransport._BaseGetDataAccessLabel,
        DataAccessControlServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataAccessControlServiceRestTransport.GetDataAccessLabel")

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
            request: data_access_control.GetDataAccessLabelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> data_access_control.DataAccessLabel:
            r"""Call the get data access label method over HTTP.

            Args:
                request (~.data_access_control.GetDataAccessLabelRequest):
                    The request object. Request message to retrieve a data
                access label.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.data_access_control.DataAccessLabel:
                    A DataAccessLabel is a label on
                events to define user access to data.

            """

            http_options = _BaseDataAccessControlServiceRestTransport._BaseGetDataAccessLabel._get_http_options()
            request, metadata = self._interceptor.pre_get_data_access_label(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataAccessControlServiceRestTransport._BaseGetDataAccessLabel,
                    "_BaseGetDataAccessLabel__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.DataAccessControlServiceClient.GetDataAccessLabel",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataAccessControlService",
                        "rpcName": "GetDataAccessLabel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataAccessControlServiceRestTransport._GetDataAccessLabel._get_response(
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
            resp = data_access_control.DataAccessLabel()
            pb_resp = data_access_control.DataAccessLabel.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_data_access_label(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_data_access_label_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = data_access_control.DataAccessLabel.to_json(
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
                    "Received response for google.cloud.chronicle_v1.DataAccessControlServiceClient.get_data_access_label",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataAccessControlService",
                        "rpcName": "GetDataAccessLabel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDataAccessScope(
        _BaseDataAccessControlServiceRestTransport._BaseGetDataAccessScope,
        DataAccessControlServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataAccessControlServiceRestTransport.GetDataAccessScope")

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
            request: data_access_control.GetDataAccessScopeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> data_access_control.DataAccessScope:
            r"""Call the get data access scope method over HTTP.

            Args:
                request (~.data_access_control.GetDataAccessScopeRequest):
                    The request object. Request message to retrieve a data
                access scope.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.data_access_control.DataAccessScope:
                    A DataAccessScope is a boolean
                expression of data access labels used to
                restrict access to data for users.

            """

            http_options = _BaseDataAccessControlServiceRestTransport._BaseGetDataAccessScope._get_http_options()
            request, metadata = self._interceptor.pre_get_data_access_scope(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataAccessControlServiceRestTransport._BaseGetDataAccessScope,
                    "_BaseGetDataAccessScope__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.DataAccessControlServiceClient.GetDataAccessScope",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataAccessControlService",
                        "rpcName": "GetDataAccessScope",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataAccessControlServiceRestTransport._GetDataAccessScope._get_response(
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
            resp = data_access_control.DataAccessScope()
            pb_resp = data_access_control.DataAccessScope.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_data_access_scope(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_data_access_scope_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = data_access_control.DataAccessScope.to_json(
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
                    "Received response for google.cloud.chronicle_v1.DataAccessControlServiceClient.get_data_access_scope",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataAccessControlService",
                        "rpcName": "GetDataAccessScope",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListDataAccessLabels(
        _BaseDataAccessControlServiceRestTransport._BaseListDataAccessLabels,
        DataAccessControlServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataAccessControlServiceRestTransport.ListDataAccessLabels")

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
            request: data_access_control.ListDataAccessLabelsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> data_access_control.ListDataAccessLabelsResponse:
            r"""Call the list data access labels method over HTTP.

            Args:
                request (~.data_access_control.ListDataAccessLabelsRequest):
                    The request object. Request message for
                ListDataAccessLabels.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.data_access_control.ListDataAccessLabelsResponse:
                    Response message for
                ListDataAccessLabels.

            """

            http_options = _BaseDataAccessControlServiceRestTransport._BaseListDataAccessLabels._get_http_options()
            request, metadata = self._interceptor.pre_list_data_access_labels(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataAccessControlServiceRestTransport._BaseListDataAccessLabels,
                    "_BaseListDataAccessLabels__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.DataAccessControlServiceClient.ListDataAccessLabels",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataAccessControlService",
                        "rpcName": "ListDataAccessLabels",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataAccessControlServiceRestTransport._ListDataAccessLabels._get_response(
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
            resp = data_access_control.ListDataAccessLabelsResponse()
            pb_resp = data_access_control.ListDataAccessLabelsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_data_access_labels(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_data_access_labels_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        data_access_control.ListDataAccessLabelsResponse.to_json(
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
                    "Received response for google.cloud.chronicle_v1.DataAccessControlServiceClient.list_data_access_labels",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataAccessControlService",
                        "rpcName": "ListDataAccessLabels",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListDataAccessScopes(
        _BaseDataAccessControlServiceRestTransport._BaseListDataAccessScopes,
        DataAccessControlServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataAccessControlServiceRestTransport.ListDataAccessScopes")

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
            request: data_access_control.ListDataAccessScopesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> data_access_control.ListDataAccessScopesResponse:
            r"""Call the list data access scopes method over HTTP.

            Args:
                request (~.data_access_control.ListDataAccessScopesRequest):
                    The request object. Request message for
                ListDataAccessScopes.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.data_access_control.ListDataAccessScopesResponse:
                    Response message for
                ListDataAccessScopes.

            """

            http_options = _BaseDataAccessControlServiceRestTransport._BaseListDataAccessScopes._get_http_options()
            request, metadata = self._interceptor.pre_list_data_access_scopes(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataAccessControlServiceRestTransport._BaseListDataAccessScopes,
                    "_BaseListDataAccessScopes__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.DataAccessControlServiceClient.ListDataAccessScopes",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataAccessControlService",
                        "rpcName": "ListDataAccessScopes",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataAccessControlServiceRestTransport._ListDataAccessScopes._get_response(
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
            resp = data_access_control.ListDataAccessScopesResponse()
            pb_resp = data_access_control.ListDataAccessScopesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_data_access_scopes(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_data_access_scopes_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        data_access_control.ListDataAccessScopesResponse.to_json(
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
                    "Received response for google.cloud.chronicle_v1.DataAccessControlServiceClient.list_data_access_scopes",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataAccessControlService",
                        "rpcName": "ListDataAccessScopes",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateDataAccessLabel(
        _BaseDataAccessControlServiceRestTransport._BaseUpdateDataAccessLabel,
        DataAccessControlServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataAccessControlServiceRestTransport.UpdateDataAccessLabel")

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
            request: data_access_control.UpdateDataAccessLabelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> data_access_control.DataAccessLabel:
            r"""Call the update data access label method over HTTP.

            Args:
                request (~.data_access_control.UpdateDataAccessLabelRequest):
                    The request object. Request message for
                UpdateDataAccessLabel method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.data_access_control.DataAccessLabel:
                    A DataAccessLabel is a label on
                events to define user access to data.

            """

            http_options = _BaseDataAccessControlServiceRestTransport._BaseUpdateDataAccessLabel._get_http_options()
            request, metadata = self._interceptor.pre_update_data_access_label(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataAccessControlServiceRestTransport._BaseUpdateDataAccessLabel,
                    "_BaseUpdateDataAccessLabel__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.DataAccessControlServiceClient.UpdateDataAccessLabel",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataAccessControlService",
                        "rpcName": "UpdateDataAccessLabel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataAccessControlServiceRestTransport._UpdateDataAccessLabel._get_response(
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
            resp = data_access_control.DataAccessLabel()
            pb_resp = data_access_control.DataAccessLabel.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_data_access_label(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_data_access_label_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = data_access_control.DataAccessLabel.to_json(
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
                    "Received response for google.cloud.chronicle_v1.DataAccessControlServiceClient.update_data_access_label",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataAccessControlService",
                        "rpcName": "UpdateDataAccessLabel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateDataAccessScope(
        _BaseDataAccessControlServiceRestTransport._BaseUpdateDataAccessScope,
        DataAccessControlServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataAccessControlServiceRestTransport.UpdateDataAccessScope")

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
            request: data_access_control.UpdateDataAccessScopeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> data_access_control.DataAccessScope:
            r"""Call the update data access scope method over HTTP.

            Args:
                request (~.data_access_control.UpdateDataAccessScopeRequest):
                    The request object. Request message for
                UpdateDataAccessScope method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.data_access_control.DataAccessScope:
                    A DataAccessScope is a boolean
                expression of data access labels used to
                restrict access to data for users.

            """

            http_options = _BaseDataAccessControlServiceRestTransport._BaseUpdateDataAccessScope._get_http_options()
            request, metadata = self._interceptor.pre_update_data_access_scope(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataAccessControlServiceRestTransport._BaseUpdateDataAccessScope,
                    "_BaseUpdateDataAccessScope__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.DataAccessControlServiceClient.UpdateDataAccessScope",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataAccessControlService",
                        "rpcName": "UpdateDataAccessScope",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataAccessControlServiceRestTransport._UpdateDataAccessScope._get_response(
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
            resp = data_access_control.DataAccessScope()
            pb_resp = data_access_control.DataAccessScope.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_data_access_scope(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_data_access_scope_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = data_access_control.DataAccessScope.to_json(
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
                    "Received response for google.cloud.chronicle_v1.DataAccessControlServiceClient.update_data_access_scope",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataAccessControlService",
                        "rpcName": "UpdateDataAccessScope",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_data_access_label(
        self,
    ) -> Callable[
        [data_access_control.CreateDataAccessLabelRequest],
        data_access_control.DataAccessLabel,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateDataAccessLabel(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_data_access_scope(
        self,
    ) -> Callable[
        [data_access_control.CreateDataAccessScopeRequest],
        data_access_control.DataAccessScope,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateDataAccessScope(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_data_access_label(
        self,
    ) -> Callable[[data_access_control.DeleteDataAccessLabelRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteDataAccessLabel(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_data_access_scope(
        self,
    ) -> Callable[[data_access_control.DeleteDataAccessScopeRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteDataAccessScope(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_data_access_label(
        self,
    ) -> Callable[
        [data_access_control.GetDataAccessLabelRequest],
        data_access_control.DataAccessLabel,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDataAccessLabel(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_data_access_scope(
        self,
    ) -> Callable[
        [data_access_control.GetDataAccessScopeRequest],
        data_access_control.DataAccessScope,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDataAccessScope(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_data_access_labels(
        self,
    ) -> Callable[
        [data_access_control.ListDataAccessLabelsRequest],
        data_access_control.ListDataAccessLabelsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDataAccessLabels(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_data_access_scopes(
        self,
    ) -> Callable[
        [data_access_control.ListDataAccessScopesRequest],
        data_access_control.ListDataAccessScopesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDataAccessScopes(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_data_access_label(
        self,
    ) -> Callable[
        [data_access_control.UpdateDataAccessLabelRequest],
        data_access_control.DataAccessLabel,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateDataAccessLabel(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_data_access_scope(
        self,
    ) -> Callable[
        [data_access_control.UpdateDataAccessScopeRequest],
        data_access_control.DataAccessScope,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateDataAccessScope(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseDataAccessControlServiceRestTransport._BaseCancelOperation,
        DataAccessControlServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataAccessControlServiceRestTransport.CancelOperation")

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

            http_options = _BaseDataAccessControlServiceRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataAccessControlServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.chronicle_v1.DataAccessControlServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataAccessControlService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataAccessControlServiceRestTransport._CancelOperation._get_response(
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
        _BaseDataAccessControlServiceRestTransport._BaseDeleteOperation,
        DataAccessControlServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataAccessControlServiceRestTransport.DeleteOperation")

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

            http_options = _BaseDataAccessControlServiceRestTransport._BaseDeleteOperation._get_http_options()
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataAccessControlServiceRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.chronicle_v1.DataAccessControlServiceClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataAccessControlService",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataAccessControlServiceRestTransport._DeleteOperation._get_response(
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
        _BaseDataAccessControlServiceRestTransport._BaseGetOperation,
        DataAccessControlServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataAccessControlServiceRestTransport.GetOperation")

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

            http_options = _BaseDataAccessControlServiceRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataAccessControlServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.chronicle_v1.DataAccessControlServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataAccessControlService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataAccessControlServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.chronicle_v1.DataAccessControlServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataAccessControlService",
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
        _BaseDataAccessControlServiceRestTransport._BaseListOperations,
        DataAccessControlServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataAccessControlServiceRestTransport.ListOperations")

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

            http_options = _BaseDataAccessControlServiceRestTransport._BaseListOperations._get_http_options()
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataAccessControlServiceRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.chronicle_v1.DataAccessControlServiceClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataAccessControlService",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataAccessControlServiceRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.chronicle_v1.DataAccessControlServiceAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataAccessControlService",
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


__all__ = ("DataAccessControlServiceRestTransport",)
