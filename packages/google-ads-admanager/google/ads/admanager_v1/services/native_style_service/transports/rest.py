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
from google.api_core import gapic_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.ads.admanager_v1._compat import transcode_request
from google.ads.admanager_v1.types import native_style_messages, native_style_service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseNativeStyleServiceRestTransport

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


class NativeStyleServiceRestInterceptor:
    """Interceptor for NativeStyleService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the NativeStyleServiceRestTransport.

    .. code-block:: python
        class MyCustomNativeStyleServiceInterceptor(NativeStyleServiceRestInterceptor):
            def pre_batch_activate_native_styles(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_activate_native_styles(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_archive_native_styles(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_archive_native_styles(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_create_native_styles(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_create_native_styles(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_deactivate_native_styles(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_deactivate_native_styles(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_update_native_styles(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_update_native_styles(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_native_style(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_native_style(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_native_style(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_native_style(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_native_styles(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_native_styles(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_native_style(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_native_style(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = NativeStyleServiceRestTransport(interceptor=MyCustomNativeStyleServiceInterceptor())
        client = NativeStyleServiceClient(transport=transport)


    """

    def pre_batch_activate_native_styles(
        self,
        request: native_style_service.BatchActivateNativeStylesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        native_style_service.BatchActivateNativeStylesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_activate_native_styles

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NativeStyleService server.
        """
        return request, metadata

    def post_batch_activate_native_styles(
        self, response: native_style_service.BatchActivateNativeStylesResponse
    ) -> native_style_service.BatchActivateNativeStylesResponse:
        """Post-rpc interceptor for batch_activate_native_styles

        DEPRECATED. Please use the `post_batch_activate_native_styles_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NativeStyleService server but before
        it is returned to user code. This `post_batch_activate_native_styles` interceptor runs
        before the `post_batch_activate_native_styles_with_metadata` interceptor.
        """
        return response

    def post_batch_activate_native_styles_with_metadata(
        self,
        response: native_style_service.BatchActivateNativeStylesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        native_style_service.BatchActivateNativeStylesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_activate_native_styles

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NativeStyleService server but before it is returned to user code.

        We recommend only using this `post_batch_activate_native_styles_with_metadata`
        interceptor in new development instead of the `post_batch_activate_native_styles` interceptor.
        When both interceptors are used, this `post_batch_activate_native_styles_with_metadata` interceptor runs after the
        `post_batch_activate_native_styles` interceptor. The (possibly modified) response returned by
        `post_batch_activate_native_styles` will be passed to
        `post_batch_activate_native_styles_with_metadata`.
        """
        return response, metadata

    def pre_batch_archive_native_styles(
        self,
        request: native_style_service.BatchArchiveNativeStylesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        native_style_service.BatchArchiveNativeStylesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_archive_native_styles

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NativeStyleService server.
        """
        return request, metadata

    def post_batch_archive_native_styles(
        self, response: native_style_service.BatchArchiveNativeStylesResponse
    ) -> native_style_service.BatchArchiveNativeStylesResponse:
        """Post-rpc interceptor for batch_archive_native_styles

        DEPRECATED. Please use the `post_batch_archive_native_styles_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NativeStyleService server but before
        it is returned to user code. This `post_batch_archive_native_styles` interceptor runs
        before the `post_batch_archive_native_styles_with_metadata` interceptor.
        """
        return response

    def post_batch_archive_native_styles_with_metadata(
        self,
        response: native_style_service.BatchArchiveNativeStylesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        native_style_service.BatchArchiveNativeStylesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_archive_native_styles

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NativeStyleService server but before it is returned to user code.

        We recommend only using this `post_batch_archive_native_styles_with_metadata`
        interceptor in new development instead of the `post_batch_archive_native_styles` interceptor.
        When both interceptors are used, this `post_batch_archive_native_styles_with_metadata` interceptor runs after the
        `post_batch_archive_native_styles` interceptor. The (possibly modified) response returned by
        `post_batch_archive_native_styles` will be passed to
        `post_batch_archive_native_styles_with_metadata`.
        """
        return response, metadata

    def pre_batch_create_native_styles(
        self,
        request: native_style_service.BatchCreateNativeStylesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        native_style_service.BatchCreateNativeStylesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_create_native_styles

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NativeStyleService server.
        """
        return request, metadata

    def post_batch_create_native_styles(
        self, response: native_style_service.BatchCreateNativeStylesResponse
    ) -> native_style_service.BatchCreateNativeStylesResponse:
        """Post-rpc interceptor for batch_create_native_styles

        DEPRECATED. Please use the `post_batch_create_native_styles_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NativeStyleService server but before
        it is returned to user code. This `post_batch_create_native_styles` interceptor runs
        before the `post_batch_create_native_styles_with_metadata` interceptor.
        """
        return response

    def post_batch_create_native_styles_with_metadata(
        self,
        response: native_style_service.BatchCreateNativeStylesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        native_style_service.BatchCreateNativeStylesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_create_native_styles

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NativeStyleService server but before it is returned to user code.

        We recommend only using this `post_batch_create_native_styles_with_metadata`
        interceptor in new development instead of the `post_batch_create_native_styles` interceptor.
        When both interceptors are used, this `post_batch_create_native_styles_with_metadata` interceptor runs after the
        `post_batch_create_native_styles` interceptor. The (possibly modified) response returned by
        `post_batch_create_native_styles` will be passed to
        `post_batch_create_native_styles_with_metadata`.
        """
        return response, metadata

    def pre_batch_deactivate_native_styles(
        self,
        request: native_style_service.BatchDeactivateNativeStylesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        native_style_service.BatchDeactivateNativeStylesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_deactivate_native_styles

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NativeStyleService server.
        """
        return request, metadata

    def post_batch_deactivate_native_styles(
        self, response: native_style_service.BatchDeactivateNativeStylesResponse
    ) -> native_style_service.BatchDeactivateNativeStylesResponse:
        """Post-rpc interceptor for batch_deactivate_native_styles

        DEPRECATED. Please use the `post_batch_deactivate_native_styles_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NativeStyleService server but before
        it is returned to user code. This `post_batch_deactivate_native_styles` interceptor runs
        before the `post_batch_deactivate_native_styles_with_metadata` interceptor.
        """
        return response

    def post_batch_deactivate_native_styles_with_metadata(
        self,
        response: native_style_service.BatchDeactivateNativeStylesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        native_style_service.BatchDeactivateNativeStylesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_deactivate_native_styles

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NativeStyleService server but before it is returned to user code.

        We recommend only using this `post_batch_deactivate_native_styles_with_metadata`
        interceptor in new development instead of the `post_batch_deactivate_native_styles` interceptor.
        When both interceptors are used, this `post_batch_deactivate_native_styles_with_metadata` interceptor runs after the
        `post_batch_deactivate_native_styles` interceptor. The (possibly modified) response returned by
        `post_batch_deactivate_native_styles` will be passed to
        `post_batch_deactivate_native_styles_with_metadata`.
        """
        return response, metadata

    def pre_batch_update_native_styles(
        self,
        request: native_style_service.BatchUpdateNativeStylesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        native_style_service.BatchUpdateNativeStylesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_update_native_styles

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NativeStyleService server.
        """
        return request, metadata

    def post_batch_update_native_styles(
        self, response: native_style_service.BatchUpdateNativeStylesResponse
    ) -> native_style_service.BatchUpdateNativeStylesResponse:
        """Post-rpc interceptor for batch_update_native_styles

        DEPRECATED. Please use the `post_batch_update_native_styles_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NativeStyleService server but before
        it is returned to user code. This `post_batch_update_native_styles` interceptor runs
        before the `post_batch_update_native_styles_with_metadata` interceptor.
        """
        return response

    def post_batch_update_native_styles_with_metadata(
        self,
        response: native_style_service.BatchUpdateNativeStylesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        native_style_service.BatchUpdateNativeStylesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_update_native_styles

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NativeStyleService server but before it is returned to user code.

        We recommend only using this `post_batch_update_native_styles_with_metadata`
        interceptor in new development instead of the `post_batch_update_native_styles` interceptor.
        When both interceptors are used, this `post_batch_update_native_styles_with_metadata` interceptor runs after the
        `post_batch_update_native_styles` interceptor. The (possibly modified) response returned by
        `post_batch_update_native_styles` will be passed to
        `post_batch_update_native_styles_with_metadata`.
        """
        return response, metadata

    def pre_create_native_style(
        self,
        request: native_style_service.CreateNativeStyleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        native_style_service.CreateNativeStyleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_native_style

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NativeStyleService server.
        """
        return request, metadata

    def post_create_native_style(
        self, response: native_style_messages.NativeStyle
    ) -> native_style_messages.NativeStyle:
        """Post-rpc interceptor for create_native_style

        DEPRECATED. Please use the `post_create_native_style_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NativeStyleService server but before
        it is returned to user code. This `post_create_native_style` interceptor runs
        before the `post_create_native_style_with_metadata` interceptor.
        """
        return response

    def post_create_native_style_with_metadata(
        self,
        response: native_style_messages.NativeStyle,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        native_style_messages.NativeStyle, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for create_native_style

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NativeStyleService server but before it is returned to user code.

        We recommend only using this `post_create_native_style_with_metadata`
        interceptor in new development instead of the `post_create_native_style` interceptor.
        When both interceptors are used, this `post_create_native_style_with_metadata` interceptor runs after the
        `post_create_native_style` interceptor. The (possibly modified) response returned by
        `post_create_native_style` will be passed to
        `post_create_native_style_with_metadata`.
        """
        return response, metadata

    def pre_get_native_style(
        self,
        request: native_style_service.GetNativeStyleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        native_style_service.GetNativeStyleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_native_style

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NativeStyleService server.
        """
        return request, metadata

    def post_get_native_style(
        self, response: native_style_messages.NativeStyle
    ) -> native_style_messages.NativeStyle:
        """Post-rpc interceptor for get_native_style

        DEPRECATED. Please use the `post_get_native_style_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NativeStyleService server but before
        it is returned to user code. This `post_get_native_style` interceptor runs
        before the `post_get_native_style_with_metadata` interceptor.
        """
        return response

    def post_get_native_style_with_metadata(
        self,
        response: native_style_messages.NativeStyle,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        native_style_messages.NativeStyle, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_native_style

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NativeStyleService server but before it is returned to user code.

        We recommend only using this `post_get_native_style_with_metadata`
        interceptor in new development instead of the `post_get_native_style` interceptor.
        When both interceptors are used, this `post_get_native_style_with_metadata` interceptor runs after the
        `post_get_native_style` interceptor. The (possibly modified) response returned by
        `post_get_native_style` will be passed to
        `post_get_native_style_with_metadata`.
        """
        return response, metadata

    def pre_list_native_styles(
        self,
        request: native_style_service.ListNativeStylesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        native_style_service.ListNativeStylesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_native_styles

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NativeStyleService server.
        """
        return request, metadata

    def post_list_native_styles(
        self, response: native_style_service.ListNativeStylesResponse
    ) -> native_style_service.ListNativeStylesResponse:
        """Post-rpc interceptor for list_native_styles

        DEPRECATED. Please use the `post_list_native_styles_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NativeStyleService server but before
        it is returned to user code. This `post_list_native_styles` interceptor runs
        before the `post_list_native_styles_with_metadata` interceptor.
        """
        return response

    def post_list_native_styles_with_metadata(
        self,
        response: native_style_service.ListNativeStylesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        native_style_service.ListNativeStylesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_native_styles

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NativeStyleService server but before it is returned to user code.

        We recommend only using this `post_list_native_styles_with_metadata`
        interceptor in new development instead of the `post_list_native_styles` interceptor.
        When both interceptors are used, this `post_list_native_styles_with_metadata` interceptor runs after the
        `post_list_native_styles` interceptor. The (possibly modified) response returned by
        `post_list_native_styles` will be passed to
        `post_list_native_styles_with_metadata`.
        """
        return response, metadata

    def pre_update_native_style(
        self,
        request: native_style_service.UpdateNativeStyleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        native_style_service.UpdateNativeStyleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_native_style

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NativeStyleService server.
        """
        return request, metadata

    def post_update_native_style(
        self, response: native_style_messages.NativeStyle
    ) -> native_style_messages.NativeStyle:
        """Post-rpc interceptor for update_native_style

        DEPRECATED. Please use the `post_update_native_style_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NativeStyleService server but before
        it is returned to user code. This `post_update_native_style` interceptor runs
        before the `post_update_native_style_with_metadata` interceptor.
        """
        return response

    def post_update_native_style_with_metadata(
        self,
        response: native_style_messages.NativeStyle,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        native_style_messages.NativeStyle, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for update_native_style

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NativeStyleService server but before it is returned to user code.

        We recommend only using this `post_update_native_style_with_metadata`
        interceptor in new development instead of the `post_update_native_style` interceptor.
        When both interceptors are used, this `post_update_native_style_with_metadata` interceptor runs after the
        `post_update_native_style` interceptor. The (possibly modified) response returned by
        `post_update_native_style` will be passed to
        `post_update_native_style_with_metadata`.
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
        before they are sent to the NativeStyleService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the NativeStyleService server but before
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
        before they are sent to the NativeStyleService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the NativeStyleService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class NativeStyleServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: NativeStyleServiceRestInterceptor


class NativeStyleServiceRestTransport(_BaseNativeStyleServiceRestTransport):
    """REST backend synchronous transport for NativeStyleService.

    Provides methods for handling ``NativeStyle`` objects.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "admanager.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[NativeStyleServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'admanager.googleapis.com').
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
            interceptor (Optional[NativeStyleServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or NativeStyleServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _BatchActivateNativeStyles(
        _BaseNativeStyleServiceRestTransport._BaseBatchActivateNativeStyles,
        NativeStyleServiceRestStub,
    ):
        def __hash__(self):
            return hash("NativeStyleServiceRestTransport.BatchActivateNativeStyles")

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
            request: native_style_service.BatchActivateNativeStylesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> native_style_service.BatchActivateNativeStylesResponse:
            r"""Call the batch activate native
            styles method over HTTP.

                Args:
                    request (~.native_style_service.BatchActivateNativeStylesRequest):
                        The request object. Request object for ``BatchActivateNativeStyles`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.native_style_service.BatchActivateNativeStylesResponse:
                        Response object for ``BatchActivateNativeStyles``
                    method.

            """

            http_options = _BaseNativeStyleServiceRestTransport._BaseBatchActivateNativeStyles._get_http_options()
            request, metadata = self._interceptor.pre_batch_activate_native_styles(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNativeStyleServiceRestTransport._BaseBatchActivateNativeStyles,
                    "_BaseBatchActivateNativeStyles__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.NativeStyleServiceClient.BatchActivateNativeStyles",
                    extra={
                        "serviceName": "google.ads.admanager.v1.NativeStyleService",
                        "rpcName": "BatchActivateNativeStyles",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NativeStyleServiceRestTransport._BatchActivateNativeStyles._get_response(
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
            resp = native_style_service.BatchActivateNativeStylesResponse()
            pb_resp = native_style_service.BatchActivateNativeStylesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_activate_native_styles(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_activate_native_styles_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        native_style_service.BatchActivateNativeStylesResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.NativeStyleServiceClient.batch_activate_native_styles",
                    extra={
                        "serviceName": "google.ads.admanager.v1.NativeStyleService",
                        "rpcName": "BatchActivateNativeStyles",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchArchiveNativeStyles(
        _BaseNativeStyleServiceRestTransport._BaseBatchArchiveNativeStyles,
        NativeStyleServiceRestStub,
    ):
        def __hash__(self):
            return hash("NativeStyleServiceRestTransport.BatchArchiveNativeStyles")

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
            request: native_style_service.BatchArchiveNativeStylesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> native_style_service.BatchArchiveNativeStylesResponse:
            r"""Call the batch archive native
            styles method over HTTP.

                Args:
                    request (~.native_style_service.BatchArchiveNativeStylesRequest):
                        The request object. Request object for ``BatchArchiveNativeStyles`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.native_style_service.BatchArchiveNativeStylesResponse:
                        Response object for ``BatchArchiveNativeStyles`` method.
            """

            http_options = _BaseNativeStyleServiceRestTransport._BaseBatchArchiveNativeStyles._get_http_options()
            request, metadata = self._interceptor.pre_batch_archive_native_styles(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNativeStyleServiceRestTransport._BaseBatchArchiveNativeStyles,
                    "_BaseBatchArchiveNativeStyles__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.NativeStyleServiceClient.BatchArchiveNativeStyles",
                    extra={
                        "serviceName": "google.ads.admanager.v1.NativeStyleService",
                        "rpcName": "BatchArchiveNativeStyles",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                NativeStyleServiceRestTransport._BatchArchiveNativeStyles._get_response(
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
            resp = native_style_service.BatchArchiveNativeStylesResponse()
            pb_resp = native_style_service.BatchArchiveNativeStylesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_archive_native_styles(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_archive_native_styles_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        native_style_service.BatchArchiveNativeStylesResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.NativeStyleServiceClient.batch_archive_native_styles",
                    extra={
                        "serviceName": "google.ads.admanager.v1.NativeStyleService",
                        "rpcName": "BatchArchiveNativeStyles",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchCreateNativeStyles(
        _BaseNativeStyleServiceRestTransport._BaseBatchCreateNativeStyles,
        NativeStyleServiceRestStub,
    ):
        def __hash__(self):
            return hash("NativeStyleServiceRestTransport.BatchCreateNativeStyles")

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
            request: native_style_service.BatchCreateNativeStylesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> native_style_service.BatchCreateNativeStylesResponse:
            r"""Call the batch create native
            styles method over HTTP.

                Args:
                    request (~.native_style_service.BatchCreateNativeStylesRequest):
                        The request object. Request object for ``BatchCreateNativeStyles`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.native_style_service.BatchCreateNativeStylesResponse:
                        Response object for ``BatchCreateNativeStyles`` method.
            """

            http_options = _BaseNativeStyleServiceRestTransport._BaseBatchCreateNativeStyles._get_http_options()
            request, metadata = self._interceptor.pre_batch_create_native_styles(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNativeStyleServiceRestTransport._BaseBatchCreateNativeStyles,
                    "_BaseBatchCreateNativeStyles__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.NativeStyleServiceClient.BatchCreateNativeStyles",
                    extra={
                        "serviceName": "google.ads.admanager.v1.NativeStyleService",
                        "rpcName": "BatchCreateNativeStyles",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                NativeStyleServiceRestTransport._BatchCreateNativeStyles._get_response(
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
            resp = native_style_service.BatchCreateNativeStylesResponse()
            pb_resp = native_style_service.BatchCreateNativeStylesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_create_native_styles(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_create_native_styles_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        native_style_service.BatchCreateNativeStylesResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.NativeStyleServiceClient.batch_create_native_styles",
                    extra={
                        "serviceName": "google.ads.admanager.v1.NativeStyleService",
                        "rpcName": "BatchCreateNativeStyles",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchDeactivateNativeStyles(
        _BaseNativeStyleServiceRestTransport._BaseBatchDeactivateNativeStyles,
        NativeStyleServiceRestStub,
    ):
        def __hash__(self):
            return hash("NativeStyleServiceRestTransport.BatchDeactivateNativeStyles")

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
            request: native_style_service.BatchDeactivateNativeStylesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> native_style_service.BatchDeactivateNativeStylesResponse:
            r"""Call the batch deactivate native
            styles method over HTTP.

                Args:
                    request (~.native_style_service.BatchDeactivateNativeStylesRequest):
                        The request object. Request object for ``BatchDeactivateNativeStyles``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.native_style_service.BatchDeactivateNativeStylesResponse:
                        Response object for ``BatchDeactivateNativeStyles``
                    method.

            """

            http_options = _BaseNativeStyleServiceRestTransport._BaseBatchDeactivateNativeStyles._get_http_options()
            request, metadata = self._interceptor.pre_batch_deactivate_native_styles(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNativeStyleServiceRestTransport._BaseBatchDeactivateNativeStyles,
                    "_BaseBatchDeactivateNativeStyles__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.NativeStyleServiceClient.BatchDeactivateNativeStyles",
                    extra={
                        "serviceName": "google.ads.admanager.v1.NativeStyleService",
                        "rpcName": "BatchDeactivateNativeStyles",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NativeStyleServiceRestTransport._BatchDeactivateNativeStyles._get_response(
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
            resp = native_style_service.BatchDeactivateNativeStylesResponse()
            pb_resp = native_style_service.BatchDeactivateNativeStylesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_deactivate_native_styles(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_deactivate_native_styles_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = native_style_service.BatchDeactivateNativeStylesResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.NativeStyleServiceClient.batch_deactivate_native_styles",
                    extra={
                        "serviceName": "google.ads.admanager.v1.NativeStyleService",
                        "rpcName": "BatchDeactivateNativeStyles",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchUpdateNativeStyles(
        _BaseNativeStyleServiceRestTransport._BaseBatchUpdateNativeStyles,
        NativeStyleServiceRestStub,
    ):
        def __hash__(self):
            return hash("NativeStyleServiceRestTransport.BatchUpdateNativeStyles")

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
            request: native_style_service.BatchUpdateNativeStylesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> native_style_service.BatchUpdateNativeStylesResponse:
            r"""Call the batch update native
            styles method over HTTP.

                Args:
                    request (~.native_style_service.BatchUpdateNativeStylesRequest):
                        The request object. Request object for ``BatchUpdateNativeStyles`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.native_style_service.BatchUpdateNativeStylesResponse:
                        Response object for ``BatchUpdateNativeStyles`` method.
            """

            http_options = _BaseNativeStyleServiceRestTransport._BaseBatchUpdateNativeStyles._get_http_options()
            request, metadata = self._interceptor.pre_batch_update_native_styles(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNativeStyleServiceRestTransport._BaseBatchUpdateNativeStyles,
                    "_BaseBatchUpdateNativeStyles__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.NativeStyleServiceClient.BatchUpdateNativeStyles",
                    extra={
                        "serviceName": "google.ads.admanager.v1.NativeStyleService",
                        "rpcName": "BatchUpdateNativeStyles",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                NativeStyleServiceRestTransport._BatchUpdateNativeStyles._get_response(
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
            resp = native_style_service.BatchUpdateNativeStylesResponse()
            pb_resp = native_style_service.BatchUpdateNativeStylesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_update_native_styles(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_update_native_styles_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        native_style_service.BatchUpdateNativeStylesResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.NativeStyleServiceClient.batch_update_native_styles",
                    extra={
                        "serviceName": "google.ads.admanager.v1.NativeStyleService",
                        "rpcName": "BatchUpdateNativeStyles",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateNativeStyle(
        _BaseNativeStyleServiceRestTransport._BaseCreateNativeStyle,
        NativeStyleServiceRestStub,
    ):
        def __hash__(self):
            return hash("NativeStyleServiceRestTransport.CreateNativeStyle")

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
            request: native_style_service.CreateNativeStyleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> native_style_messages.NativeStyle:
            r"""Call the create native style method over HTTP.

            Args:
                request (~.native_style_service.CreateNativeStyleRequest):
                    The request object. Request object for ``CreateNativeStyle`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.native_style_messages.NativeStyle:
                    Used to define the look and feel of
                native ads, for both web and apps.
                Native styles determine how native
                creatives look for a segment of
                inventory.

            """

            http_options = _BaseNativeStyleServiceRestTransport._BaseCreateNativeStyle._get_http_options()
            request, metadata = self._interceptor.pre_create_native_style(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNativeStyleServiceRestTransport._BaseCreateNativeStyle,
                    "_BaseCreateNativeStyle__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.NativeStyleServiceClient.CreateNativeStyle",
                    extra={
                        "serviceName": "google.ads.admanager.v1.NativeStyleService",
                        "rpcName": "CreateNativeStyle",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NativeStyleServiceRestTransport._CreateNativeStyle._get_response(
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
            resp = native_style_messages.NativeStyle()
            pb_resp = native_style_messages.NativeStyle.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_native_style(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_native_style_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = native_style_messages.NativeStyle.to_json(
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
                    "Received response for google.ads.admanager_v1.NativeStyleServiceClient.create_native_style",
                    extra={
                        "serviceName": "google.ads.admanager.v1.NativeStyleService",
                        "rpcName": "CreateNativeStyle",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetNativeStyle(
        _BaseNativeStyleServiceRestTransport._BaseGetNativeStyle,
        NativeStyleServiceRestStub,
    ):
        def __hash__(self):
            return hash("NativeStyleServiceRestTransport.GetNativeStyle")

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
            request: native_style_service.GetNativeStyleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> native_style_messages.NativeStyle:
            r"""Call the get native style method over HTTP.

            Args:
                request (~.native_style_service.GetNativeStyleRequest):
                    The request object. Request object for ``GetNativeStyle`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.native_style_messages.NativeStyle:
                    Used to define the look and feel of
                native ads, for both web and apps.
                Native styles determine how native
                creatives look for a segment of
                inventory.

            """

            http_options = _BaseNativeStyleServiceRestTransport._BaseGetNativeStyle._get_http_options()
            request, metadata = self._interceptor.pre_get_native_style(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNativeStyleServiceRestTransport._BaseGetNativeStyle,
                    "_BaseGetNativeStyle__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.NativeStyleServiceClient.GetNativeStyle",
                    extra={
                        "serviceName": "google.ads.admanager.v1.NativeStyleService",
                        "rpcName": "GetNativeStyle",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NativeStyleServiceRestTransport._GetNativeStyle._get_response(
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
            resp = native_style_messages.NativeStyle()
            pb_resp = native_style_messages.NativeStyle.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_native_style(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_native_style_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = native_style_messages.NativeStyle.to_json(
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
                    "Received response for google.ads.admanager_v1.NativeStyleServiceClient.get_native_style",
                    extra={
                        "serviceName": "google.ads.admanager.v1.NativeStyleService",
                        "rpcName": "GetNativeStyle",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListNativeStyles(
        _BaseNativeStyleServiceRestTransport._BaseListNativeStyles,
        NativeStyleServiceRestStub,
    ):
        def __hash__(self):
            return hash("NativeStyleServiceRestTransport.ListNativeStyles")

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
            request: native_style_service.ListNativeStylesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> native_style_service.ListNativeStylesResponse:
            r"""Call the list native styles method over HTTP.

            Args:
                request (~.native_style_service.ListNativeStylesRequest):
                    The request object. Request object for ``ListNativeStyles`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.native_style_service.ListNativeStylesResponse:
                    Response object for ``ListNativeStylesRequest``
                containing matching ``NativeStyle`` objects.

            """

            http_options = _BaseNativeStyleServiceRestTransport._BaseListNativeStyles._get_http_options()
            request, metadata = self._interceptor.pre_list_native_styles(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNativeStyleServiceRestTransport._BaseListNativeStyles,
                    "_BaseListNativeStyles__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.NativeStyleServiceClient.ListNativeStyles",
                    extra={
                        "serviceName": "google.ads.admanager.v1.NativeStyleService",
                        "rpcName": "ListNativeStyles",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NativeStyleServiceRestTransport._ListNativeStyles._get_response(
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
            resp = native_style_service.ListNativeStylesResponse()
            pb_resp = native_style_service.ListNativeStylesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_native_styles(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_native_styles_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        native_style_service.ListNativeStylesResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.NativeStyleServiceClient.list_native_styles",
                    extra={
                        "serviceName": "google.ads.admanager.v1.NativeStyleService",
                        "rpcName": "ListNativeStyles",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateNativeStyle(
        _BaseNativeStyleServiceRestTransport._BaseUpdateNativeStyle,
        NativeStyleServiceRestStub,
    ):
        def __hash__(self):
            return hash("NativeStyleServiceRestTransport.UpdateNativeStyle")

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
            request: native_style_service.UpdateNativeStyleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> native_style_messages.NativeStyle:
            r"""Call the update native style method over HTTP.

            Args:
                request (~.native_style_service.UpdateNativeStyleRequest):
                    The request object. Request object for ``UpdateNativeStyle`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.native_style_messages.NativeStyle:
                    Used to define the look and feel of
                native ads, for both web and apps.
                Native styles determine how native
                creatives look for a segment of
                inventory.

            """

            http_options = _BaseNativeStyleServiceRestTransport._BaseUpdateNativeStyle._get_http_options()
            request, metadata = self._interceptor.pre_update_native_style(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNativeStyleServiceRestTransport._BaseUpdateNativeStyle,
                    "_BaseUpdateNativeStyle__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.NativeStyleServiceClient.UpdateNativeStyle",
                    extra={
                        "serviceName": "google.ads.admanager.v1.NativeStyleService",
                        "rpcName": "UpdateNativeStyle",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NativeStyleServiceRestTransport._UpdateNativeStyle._get_response(
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
            resp = native_style_messages.NativeStyle()
            pb_resp = native_style_messages.NativeStyle.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_native_style(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_native_style_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = native_style_messages.NativeStyle.to_json(
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
                    "Received response for google.ads.admanager_v1.NativeStyleServiceClient.update_native_style",
                    extra={
                        "serviceName": "google.ads.admanager.v1.NativeStyleService",
                        "rpcName": "UpdateNativeStyle",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_activate_native_styles(
        self,
    ) -> Callable[
        [native_style_service.BatchActivateNativeStylesRequest],
        native_style_service.BatchActivateNativeStylesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchActivateNativeStyles(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_archive_native_styles(
        self,
    ) -> Callable[
        [native_style_service.BatchArchiveNativeStylesRequest],
        native_style_service.BatchArchiveNativeStylesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchArchiveNativeStyles(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_create_native_styles(
        self,
    ) -> Callable[
        [native_style_service.BatchCreateNativeStylesRequest],
        native_style_service.BatchCreateNativeStylesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchCreateNativeStyles(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_deactivate_native_styles(
        self,
    ) -> Callable[
        [native_style_service.BatchDeactivateNativeStylesRequest],
        native_style_service.BatchDeactivateNativeStylesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchDeactivateNativeStyles(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_update_native_styles(
        self,
    ) -> Callable[
        [native_style_service.BatchUpdateNativeStylesRequest],
        native_style_service.BatchUpdateNativeStylesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchUpdateNativeStyles(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_native_style(
        self,
    ) -> Callable[
        [native_style_service.CreateNativeStyleRequest],
        native_style_messages.NativeStyle,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateNativeStyle(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_native_style(
        self,
    ) -> Callable[
        [native_style_service.GetNativeStyleRequest], native_style_messages.NativeStyle
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetNativeStyle(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_native_styles(
        self,
    ) -> Callable[
        [native_style_service.ListNativeStylesRequest],
        native_style_service.ListNativeStylesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListNativeStyles(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_native_style(
        self,
    ) -> Callable[
        [native_style_service.UpdateNativeStyleRequest],
        native_style_messages.NativeStyle,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateNativeStyle(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseNativeStyleServiceRestTransport._BaseCancelOperation,
        NativeStyleServiceRestStub,
    ):
        def __hash__(self):
            return hash("NativeStyleServiceRestTransport.CancelOperation")

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

            http_options = _BaseNativeStyleServiceRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNativeStyleServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.ads.admanager_v1.NativeStyleServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.NativeStyleService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NativeStyleServiceRestTransport._CancelOperation._get_response(
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
        _BaseNativeStyleServiceRestTransport._BaseGetOperation,
        NativeStyleServiceRestStub,
    ):
        def __hash__(self):
            return hash("NativeStyleServiceRestTransport.GetOperation")

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

            http_options = _BaseNativeStyleServiceRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNativeStyleServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.ads.admanager_v1.NativeStyleServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.NativeStyleService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NativeStyleServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.ads.admanager_v1.NativeStyleServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.NativeStyleService",
                        "rpcName": "GetOperation",
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


__all__ = ("NativeStyleServiceRestTransport",)
