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
from google.ads.admanager_v1.types import (
    creative_wrapper_messages,
    creative_wrapper_service,
)

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseCreativeWrapperServiceRestTransport

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


class CreativeWrapperServiceRestInterceptor:
    """Interceptor for CreativeWrapperService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the CreativeWrapperServiceRestTransport.

    .. code-block:: python
        class MyCustomCreativeWrapperServiceInterceptor(CreativeWrapperServiceRestInterceptor):
            def pre_batch_activate_creative_wrappers(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_activate_creative_wrappers(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_create_creative_wrappers(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_create_creative_wrappers(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_deactivate_creative_wrappers(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_deactivate_creative_wrappers(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_update_creative_wrappers(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_update_creative_wrappers(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_creative_wrapper(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_creative_wrapper(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_creative_wrapper(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_creative_wrapper(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_creative_wrappers(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_creative_wrappers(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_creative_wrapper(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_creative_wrapper(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = CreativeWrapperServiceRestTransport(interceptor=MyCustomCreativeWrapperServiceInterceptor())
        client = CreativeWrapperServiceClient(transport=transport)


    """

    def pre_batch_activate_creative_wrappers(
        self,
        request: creative_wrapper_service.BatchActivateCreativeWrappersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        creative_wrapper_service.BatchActivateCreativeWrappersRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_activate_creative_wrappers

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CreativeWrapperService server.
        """
        return request, metadata

    def post_batch_activate_creative_wrappers(
        self, response: creative_wrapper_service.BatchActivateCreativeWrappersResponse
    ) -> creative_wrapper_service.BatchActivateCreativeWrappersResponse:
        """Post-rpc interceptor for batch_activate_creative_wrappers

        DEPRECATED. Please use the `post_batch_activate_creative_wrappers_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CreativeWrapperService server but before
        it is returned to user code. This `post_batch_activate_creative_wrappers` interceptor runs
        before the `post_batch_activate_creative_wrappers_with_metadata` interceptor.
        """
        return response

    def post_batch_activate_creative_wrappers_with_metadata(
        self,
        response: creative_wrapper_service.BatchActivateCreativeWrappersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        creative_wrapper_service.BatchActivateCreativeWrappersResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_activate_creative_wrappers

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CreativeWrapperService server but before it is returned to user code.

        We recommend only using this `post_batch_activate_creative_wrappers_with_metadata`
        interceptor in new development instead of the `post_batch_activate_creative_wrappers` interceptor.
        When both interceptors are used, this `post_batch_activate_creative_wrappers_with_metadata` interceptor runs after the
        `post_batch_activate_creative_wrappers` interceptor. The (possibly modified) response returned by
        `post_batch_activate_creative_wrappers` will be passed to
        `post_batch_activate_creative_wrappers_with_metadata`.
        """
        return response, metadata

    def pre_batch_create_creative_wrappers(
        self,
        request: creative_wrapper_service.BatchCreateCreativeWrappersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        creative_wrapper_service.BatchCreateCreativeWrappersRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_create_creative_wrappers

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CreativeWrapperService server.
        """
        return request, metadata

    def post_batch_create_creative_wrappers(
        self, response: creative_wrapper_service.BatchCreateCreativeWrappersResponse
    ) -> creative_wrapper_service.BatchCreateCreativeWrappersResponse:
        """Post-rpc interceptor for batch_create_creative_wrappers

        DEPRECATED. Please use the `post_batch_create_creative_wrappers_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CreativeWrapperService server but before
        it is returned to user code. This `post_batch_create_creative_wrappers` interceptor runs
        before the `post_batch_create_creative_wrappers_with_metadata` interceptor.
        """
        return response

    def post_batch_create_creative_wrappers_with_metadata(
        self,
        response: creative_wrapper_service.BatchCreateCreativeWrappersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        creative_wrapper_service.BatchCreateCreativeWrappersResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_create_creative_wrappers

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CreativeWrapperService server but before it is returned to user code.

        We recommend only using this `post_batch_create_creative_wrappers_with_metadata`
        interceptor in new development instead of the `post_batch_create_creative_wrappers` interceptor.
        When both interceptors are used, this `post_batch_create_creative_wrappers_with_metadata` interceptor runs after the
        `post_batch_create_creative_wrappers` interceptor. The (possibly modified) response returned by
        `post_batch_create_creative_wrappers` will be passed to
        `post_batch_create_creative_wrappers_with_metadata`.
        """
        return response, metadata

    def pre_batch_deactivate_creative_wrappers(
        self,
        request: creative_wrapper_service.BatchDeactivateCreativeWrappersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        creative_wrapper_service.BatchDeactivateCreativeWrappersRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_deactivate_creative_wrappers

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CreativeWrapperService server.
        """
        return request, metadata

    def post_batch_deactivate_creative_wrappers(
        self, response: creative_wrapper_service.BatchDeactivateCreativeWrappersResponse
    ) -> creative_wrapper_service.BatchDeactivateCreativeWrappersResponse:
        """Post-rpc interceptor for batch_deactivate_creative_wrappers

        DEPRECATED. Please use the `post_batch_deactivate_creative_wrappers_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CreativeWrapperService server but before
        it is returned to user code. This `post_batch_deactivate_creative_wrappers` interceptor runs
        before the `post_batch_deactivate_creative_wrappers_with_metadata` interceptor.
        """
        return response

    def post_batch_deactivate_creative_wrappers_with_metadata(
        self,
        response: creative_wrapper_service.BatchDeactivateCreativeWrappersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        creative_wrapper_service.BatchDeactivateCreativeWrappersResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_deactivate_creative_wrappers

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CreativeWrapperService server but before it is returned to user code.

        We recommend only using this `post_batch_deactivate_creative_wrappers_with_metadata`
        interceptor in new development instead of the `post_batch_deactivate_creative_wrappers` interceptor.
        When both interceptors are used, this `post_batch_deactivate_creative_wrappers_with_metadata` interceptor runs after the
        `post_batch_deactivate_creative_wrappers` interceptor. The (possibly modified) response returned by
        `post_batch_deactivate_creative_wrappers` will be passed to
        `post_batch_deactivate_creative_wrappers_with_metadata`.
        """
        return response, metadata

    def pre_batch_update_creative_wrappers(
        self,
        request: creative_wrapper_service.BatchUpdateCreativeWrappersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        creative_wrapper_service.BatchUpdateCreativeWrappersRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_update_creative_wrappers

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CreativeWrapperService server.
        """
        return request, metadata

    def post_batch_update_creative_wrappers(
        self, response: creative_wrapper_service.BatchUpdateCreativeWrappersResponse
    ) -> creative_wrapper_service.BatchUpdateCreativeWrappersResponse:
        """Post-rpc interceptor for batch_update_creative_wrappers

        DEPRECATED. Please use the `post_batch_update_creative_wrappers_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CreativeWrapperService server but before
        it is returned to user code. This `post_batch_update_creative_wrappers` interceptor runs
        before the `post_batch_update_creative_wrappers_with_metadata` interceptor.
        """
        return response

    def post_batch_update_creative_wrappers_with_metadata(
        self,
        response: creative_wrapper_service.BatchUpdateCreativeWrappersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        creative_wrapper_service.BatchUpdateCreativeWrappersResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_update_creative_wrappers

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CreativeWrapperService server but before it is returned to user code.

        We recommend only using this `post_batch_update_creative_wrappers_with_metadata`
        interceptor in new development instead of the `post_batch_update_creative_wrappers` interceptor.
        When both interceptors are used, this `post_batch_update_creative_wrappers_with_metadata` interceptor runs after the
        `post_batch_update_creative_wrappers` interceptor. The (possibly modified) response returned by
        `post_batch_update_creative_wrappers` will be passed to
        `post_batch_update_creative_wrappers_with_metadata`.
        """
        return response, metadata

    def pre_create_creative_wrapper(
        self,
        request: creative_wrapper_service.CreateCreativeWrapperRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        creative_wrapper_service.CreateCreativeWrapperRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_creative_wrapper

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CreativeWrapperService server.
        """
        return request, metadata

    def post_create_creative_wrapper(
        self, response: creative_wrapper_messages.CreativeWrapper
    ) -> creative_wrapper_messages.CreativeWrapper:
        """Post-rpc interceptor for create_creative_wrapper

        DEPRECATED. Please use the `post_create_creative_wrapper_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CreativeWrapperService server but before
        it is returned to user code. This `post_create_creative_wrapper` interceptor runs
        before the `post_create_creative_wrapper_with_metadata` interceptor.
        """
        return response

    def post_create_creative_wrapper_with_metadata(
        self,
        response: creative_wrapper_messages.CreativeWrapper,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        creative_wrapper_messages.CreativeWrapper,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for create_creative_wrapper

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CreativeWrapperService server but before it is returned to user code.

        We recommend only using this `post_create_creative_wrapper_with_metadata`
        interceptor in new development instead of the `post_create_creative_wrapper` interceptor.
        When both interceptors are used, this `post_create_creative_wrapper_with_metadata` interceptor runs after the
        `post_create_creative_wrapper` interceptor. The (possibly modified) response returned by
        `post_create_creative_wrapper` will be passed to
        `post_create_creative_wrapper_with_metadata`.
        """
        return response, metadata

    def pre_get_creative_wrapper(
        self,
        request: creative_wrapper_service.GetCreativeWrapperRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        creative_wrapper_service.GetCreativeWrapperRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_creative_wrapper

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CreativeWrapperService server.
        """
        return request, metadata

    def post_get_creative_wrapper(
        self, response: creative_wrapper_messages.CreativeWrapper
    ) -> creative_wrapper_messages.CreativeWrapper:
        """Post-rpc interceptor for get_creative_wrapper

        DEPRECATED. Please use the `post_get_creative_wrapper_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CreativeWrapperService server but before
        it is returned to user code. This `post_get_creative_wrapper` interceptor runs
        before the `post_get_creative_wrapper_with_metadata` interceptor.
        """
        return response

    def post_get_creative_wrapper_with_metadata(
        self,
        response: creative_wrapper_messages.CreativeWrapper,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        creative_wrapper_messages.CreativeWrapper,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_creative_wrapper

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CreativeWrapperService server but before it is returned to user code.

        We recommend only using this `post_get_creative_wrapper_with_metadata`
        interceptor in new development instead of the `post_get_creative_wrapper` interceptor.
        When both interceptors are used, this `post_get_creative_wrapper_with_metadata` interceptor runs after the
        `post_get_creative_wrapper` interceptor. The (possibly modified) response returned by
        `post_get_creative_wrapper` will be passed to
        `post_get_creative_wrapper_with_metadata`.
        """
        return response, metadata

    def pre_list_creative_wrappers(
        self,
        request: creative_wrapper_service.ListCreativeWrappersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        creative_wrapper_service.ListCreativeWrappersRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_creative_wrappers

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CreativeWrapperService server.
        """
        return request, metadata

    def post_list_creative_wrappers(
        self, response: creative_wrapper_service.ListCreativeWrappersResponse
    ) -> creative_wrapper_service.ListCreativeWrappersResponse:
        """Post-rpc interceptor for list_creative_wrappers

        DEPRECATED. Please use the `post_list_creative_wrappers_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CreativeWrapperService server but before
        it is returned to user code. This `post_list_creative_wrappers` interceptor runs
        before the `post_list_creative_wrappers_with_metadata` interceptor.
        """
        return response

    def post_list_creative_wrappers_with_metadata(
        self,
        response: creative_wrapper_service.ListCreativeWrappersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        creative_wrapper_service.ListCreativeWrappersResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_creative_wrappers

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CreativeWrapperService server but before it is returned to user code.

        We recommend only using this `post_list_creative_wrappers_with_metadata`
        interceptor in new development instead of the `post_list_creative_wrappers` interceptor.
        When both interceptors are used, this `post_list_creative_wrappers_with_metadata` interceptor runs after the
        `post_list_creative_wrappers` interceptor. The (possibly modified) response returned by
        `post_list_creative_wrappers` will be passed to
        `post_list_creative_wrappers_with_metadata`.
        """
        return response, metadata

    def pre_update_creative_wrapper(
        self,
        request: creative_wrapper_service.UpdateCreativeWrapperRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        creative_wrapper_service.UpdateCreativeWrapperRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_creative_wrapper

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CreativeWrapperService server.
        """
        return request, metadata

    def post_update_creative_wrapper(
        self, response: creative_wrapper_messages.CreativeWrapper
    ) -> creative_wrapper_messages.CreativeWrapper:
        """Post-rpc interceptor for update_creative_wrapper

        DEPRECATED. Please use the `post_update_creative_wrapper_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CreativeWrapperService server but before
        it is returned to user code. This `post_update_creative_wrapper` interceptor runs
        before the `post_update_creative_wrapper_with_metadata` interceptor.
        """
        return response

    def post_update_creative_wrapper_with_metadata(
        self,
        response: creative_wrapper_messages.CreativeWrapper,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        creative_wrapper_messages.CreativeWrapper,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for update_creative_wrapper

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CreativeWrapperService server but before it is returned to user code.

        We recommend only using this `post_update_creative_wrapper_with_metadata`
        interceptor in new development instead of the `post_update_creative_wrapper` interceptor.
        When both interceptors are used, this `post_update_creative_wrapper_with_metadata` interceptor runs after the
        `post_update_creative_wrapper` interceptor. The (possibly modified) response returned by
        `post_update_creative_wrapper` will be passed to
        `post_update_creative_wrapper_with_metadata`.
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
        before they are sent to the CreativeWrapperService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the CreativeWrapperService server but before
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
        before they are sent to the CreativeWrapperService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the CreativeWrapperService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class CreativeWrapperServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: CreativeWrapperServiceRestInterceptor


class CreativeWrapperServiceRestTransport(_BaseCreativeWrapperServiceRestTransport):
    """REST backend synchronous transport for CreativeWrapperService.

    Provides methods for handling ``CreativeWrapper`` objects.

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
        interceptor: Optional[CreativeWrapperServiceRestInterceptor] = None,
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
            interceptor (Optional[CreativeWrapperServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or CreativeWrapperServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _BatchActivateCreativeWrappers(
        _BaseCreativeWrapperServiceRestTransport._BaseBatchActivateCreativeWrappers,
        CreativeWrapperServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "CreativeWrapperServiceRestTransport.BatchActivateCreativeWrappers"
            )

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
            request: creative_wrapper_service.BatchActivateCreativeWrappersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> creative_wrapper_service.BatchActivateCreativeWrappersResponse:
            r"""Call the batch activate creative
            wrappers method over HTTP.

                Args:
                    request (~.creative_wrapper_service.BatchActivateCreativeWrappersRequest):
                        The request object. Request message to activate ``CreativeWrapper`` objects.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.creative_wrapper_service.BatchActivateCreativeWrappersResponse:
                        Response message for ``BatchActivateCreativeWrappers``
                    method.

            """

            http_options = _BaseCreativeWrapperServiceRestTransport._BaseBatchActivateCreativeWrappers._get_http_options()
            request, metadata = self._interceptor.pre_batch_activate_creative_wrappers(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCreativeWrapperServiceRestTransport._BaseBatchActivateCreativeWrappers,
                    "_BaseBatchActivateCreativeWrappers__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.CreativeWrapperServiceClient.BatchActivateCreativeWrappers",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CreativeWrapperService",
                        "rpcName": "BatchActivateCreativeWrappers",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CreativeWrapperServiceRestTransport._BatchActivateCreativeWrappers._get_response(
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
            resp = creative_wrapper_service.BatchActivateCreativeWrappersResponse()
            pb_resp = creative_wrapper_service.BatchActivateCreativeWrappersResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_activate_creative_wrappers(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_activate_creative_wrappers_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = creative_wrapper_service.BatchActivateCreativeWrappersResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.CreativeWrapperServiceClient.batch_activate_creative_wrappers",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CreativeWrapperService",
                        "rpcName": "BatchActivateCreativeWrappers",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchCreateCreativeWrappers(
        _BaseCreativeWrapperServiceRestTransport._BaseBatchCreateCreativeWrappers,
        CreativeWrapperServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "CreativeWrapperServiceRestTransport.BatchCreateCreativeWrappers"
            )

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
            request: creative_wrapper_service.BatchCreateCreativeWrappersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> creative_wrapper_service.BatchCreateCreativeWrappersResponse:
            r"""Call the batch create creative
            wrappers method over HTTP.

                Args:
                    request (~.creative_wrapper_service.BatchCreateCreativeWrappersRequest):
                        The request object. Request object for ``BatchCreateCreativeWrappers``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.creative_wrapper_service.BatchCreateCreativeWrappersResponse:
                        Response object for ``BatchCreateCreativeWrappers``
                    method.

            """

            http_options = _BaseCreativeWrapperServiceRestTransport._BaseBatchCreateCreativeWrappers._get_http_options()
            request, metadata = self._interceptor.pre_batch_create_creative_wrappers(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCreativeWrapperServiceRestTransport._BaseBatchCreateCreativeWrappers,
                    "_BaseBatchCreateCreativeWrappers__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.CreativeWrapperServiceClient.BatchCreateCreativeWrappers",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CreativeWrapperService",
                        "rpcName": "BatchCreateCreativeWrappers",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CreativeWrapperServiceRestTransport._BatchCreateCreativeWrappers._get_response(
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
            resp = creative_wrapper_service.BatchCreateCreativeWrappersResponse()
            pb_resp = creative_wrapper_service.BatchCreateCreativeWrappersResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_create_creative_wrappers(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_create_creative_wrappers_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = creative_wrapper_service.BatchCreateCreativeWrappersResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.CreativeWrapperServiceClient.batch_create_creative_wrappers",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CreativeWrapperService",
                        "rpcName": "BatchCreateCreativeWrappers",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchDeactivateCreativeWrappers(
        _BaseCreativeWrapperServiceRestTransport._BaseBatchDeactivateCreativeWrappers,
        CreativeWrapperServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "CreativeWrapperServiceRestTransport.BatchDeactivateCreativeWrappers"
            )

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
            request: creative_wrapper_service.BatchDeactivateCreativeWrappersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> creative_wrapper_service.BatchDeactivateCreativeWrappersResponse:
            r"""Call the batch deactivate creative
            wrappers method over HTTP.

                Args:
                    request (~.creative_wrapper_service.BatchDeactivateCreativeWrappersRequest):
                        The request object. Request message to deactivate ``CreativeWrapper``
                    objects.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.creative_wrapper_service.BatchDeactivateCreativeWrappersResponse:
                        Response object for ``BatchDeactivateCreativeWrappers``
                    method.

            """

            http_options = _BaseCreativeWrapperServiceRestTransport._BaseBatchDeactivateCreativeWrappers._get_http_options()
            request, metadata = (
                self._interceptor.pre_batch_deactivate_creative_wrappers(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCreativeWrapperServiceRestTransport._BaseBatchDeactivateCreativeWrappers,
                    "_BaseBatchDeactivateCreativeWrappers__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.CreativeWrapperServiceClient.BatchDeactivateCreativeWrappers",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CreativeWrapperService",
                        "rpcName": "BatchDeactivateCreativeWrappers",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CreativeWrapperServiceRestTransport._BatchDeactivateCreativeWrappers._get_response(
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
            resp = creative_wrapper_service.BatchDeactivateCreativeWrappersResponse()
            pb_resp = (
                creative_wrapper_service.BatchDeactivateCreativeWrappersResponse.pb(
                    resp
                )
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_deactivate_creative_wrappers(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_deactivate_creative_wrappers_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = creative_wrapper_service.BatchDeactivateCreativeWrappersResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.CreativeWrapperServiceClient.batch_deactivate_creative_wrappers",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CreativeWrapperService",
                        "rpcName": "BatchDeactivateCreativeWrappers",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchUpdateCreativeWrappers(
        _BaseCreativeWrapperServiceRestTransport._BaseBatchUpdateCreativeWrappers,
        CreativeWrapperServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "CreativeWrapperServiceRestTransport.BatchUpdateCreativeWrappers"
            )

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
            request: creative_wrapper_service.BatchUpdateCreativeWrappersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> creative_wrapper_service.BatchUpdateCreativeWrappersResponse:
            r"""Call the batch update creative
            wrappers method over HTTP.

                Args:
                    request (~.creative_wrapper_service.BatchUpdateCreativeWrappersRequest):
                        The request object. Request object for ``BatchUpdateCreativeWrappers``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.creative_wrapper_service.BatchUpdateCreativeWrappersResponse:
                        Response object for ``BatchUpdateCreativeWrappers``
                    method.

            """

            http_options = _BaseCreativeWrapperServiceRestTransport._BaseBatchUpdateCreativeWrappers._get_http_options()
            request, metadata = self._interceptor.pre_batch_update_creative_wrappers(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCreativeWrapperServiceRestTransport._BaseBatchUpdateCreativeWrappers,
                    "_BaseBatchUpdateCreativeWrappers__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.CreativeWrapperServiceClient.BatchUpdateCreativeWrappers",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CreativeWrapperService",
                        "rpcName": "BatchUpdateCreativeWrappers",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CreativeWrapperServiceRestTransport._BatchUpdateCreativeWrappers._get_response(
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
            resp = creative_wrapper_service.BatchUpdateCreativeWrappersResponse()
            pb_resp = creative_wrapper_service.BatchUpdateCreativeWrappersResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_update_creative_wrappers(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_update_creative_wrappers_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = creative_wrapper_service.BatchUpdateCreativeWrappersResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.CreativeWrapperServiceClient.batch_update_creative_wrappers",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CreativeWrapperService",
                        "rpcName": "BatchUpdateCreativeWrappers",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateCreativeWrapper(
        _BaseCreativeWrapperServiceRestTransport._BaseCreateCreativeWrapper,
        CreativeWrapperServiceRestStub,
    ):
        def __hash__(self):
            return hash("CreativeWrapperServiceRestTransport.CreateCreativeWrapper")

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
            request: creative_wrapper_service.CreateCreativeWrapperRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> creative_wrapper_messages.CreativeWrapper:
            r"""Call the create creative wrapper method over HTTP.

            Args:
                request (~.creative_wrapper_service.CreateCreativeWrapperRequest):
                    The request object. Request object for ``CreateCreativeWrapper`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.creative_wrapper_messages.CreativeWrapper:
                    A ``CreativeWrapper`` allows the wrapping of HTML
                snippets to be served along with Creative objects.

                ``CreativeWrapper`` must be associated with a
                [LabelType.CREATIVE_WRAPPER][google.ads.admanager.v1.LabelTypeEnum.LabelType.CREATIVE_WRAPPER]
                label and applied to ad units by
                [AdUnit.appliedLabels][google.ads.admanager.v1.AdUnit.applied_labels].

            """

            http_options = _BaseCreativeWrapperServiceRestTransport._BaseCreateCreativeWrapper._get_http_options()
            request, metadata = self._interceptor.pre_create_creative_wrapper(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCreativeWrapperServiceRestTransport._BaseCreateCreativeWrapper,
                    "_BaseCreateCreativeWrapper__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.CreativeWrapperServiceClient.CreateCreativeWrapper",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CreativeWrapperService",
                        "rpcName": "CreateCreativeWrapper",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CreativeWrapperServiceRestTransport._CreateCreativeWrapper._get_response(
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
            resp = creative_wrapper_messages.CreativeWrapper()
            pb_resp = creative_wrapper_messages.CreativeWrapper.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_creative_wrapper(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_creative_wrapper_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        creative_wrapper_messages.CreativeWrapper.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.CreativeWrapperServiceClient.create_creative_wrapper",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CreativeWrapperService",
                        "rpcName": "CreateCreativeWrapper",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetCreativeWrapper(
        _BaseCreativeWrapperServiceRestTransport._BaseGetCreativeWrapper,
        CreativeWrapperServiceRestStub,
    ):
        def __hash__(self):
            return hash("CreativeWrapperServiceRestTransport.GetCreativeWrapper")

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
            request: creative_wrapper_service.GetCreativeWrapperRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> creative_wrapper_messages.CreativeWrapper:
            r"""Call the get creative wrapper method over HTTP.

            Args:
                request (~.creative_wrapper_service.GetCreativeWrapperRequest):
                    The request object. Request object for ``GetCreativeWrapper`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.creative_wrapper_messages.CreativeWrapper:
                    A ``CreativeWrapper`` allows the wrapping of HTML
                snippets to be served along with Creative objects.

                ``CreativeWrapper`` must be associated with a
                [LabelType.CREATIVE_WRAPPER][google.ads.admanager.v1.LabelTypeEnum.LabelType.CREATIVE_WRAPPER]
                label and applied to ad units by
                [AdUnit.appliedLabels][google.ads.admanager.v1.AdUnit.applied_labels].

            """

            http_options = _BaseCreativeWrapperServiceRestTransport._BaseGetCreativeWrapper._get_http_options()
            request, metadata = self._interceptor.pre_get_creative_wrapper(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCreativeWrapperServiceRestTransport._BaseGetCreativeWrapper,
                    "_BaseGetCreativeWrapper__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.CreativeWrapperServiceClient.GetCreativeWrapper",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CreativeWrapperService",
                        "rpcName": "GetCreativeWrapper",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CreativeWrapperServiceRestTransport._GetCreativeWrapper._get_response(
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
            resp = creative_wrapper_messages.CreativeWrapper()
            pb_resp = creative_wrapper_messages.CreativeWrapper.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_creative_wrapper(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_creative_wrapper_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        creative_wrapper_messages.CreativeWrapper.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.CreativeWrapperServiceClient.get_creative_wrapper",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CreativeWrapperService",
                        "rpcName": "GetCreativeWrapper",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListCreativeWrappers(
        _BaseCreativeWrapperServiceRestTransport._BaseListCreativeWrappers,
        CreativeWrapperServiceRestStub,
    ):
        def __hash__(self):
            return hash("CreativeWrapperServiceRestTransport.ListCreativeWrappers")

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
            request: creative_wrapper_service.ListCreativeWrappersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> creative_wrapper_service.ListCreativeWrappersResponse:
            r"""Call the list creative wrappers method over HTTP.

            Args:
                request (~.creative_wrapper_service.ListCreativeWrappersRequest):
                    The request object. Request object for ``ListCreativeWrappers`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.creative_wrapper_service.ListCreativeWrappersResponse:
                    Response object for ``ListCreativeWrappersRequest``
                containing matching ``CreativeWrapper`` objects.

            """

            http_options = _BaseCreativeWrapperServiceRestTransport._BaseListCreativeWrappers._get_http_options()
            request, metadata = self._interceptor.pre_list_creative_wrappers(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCreativeWrapperServiceRestTransport._BaseListCreativeWrappers,
                    "_BaseListCreativeWrappers__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.CreativeWrapperServiceClient.ListCreativeWrappers",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CreativeWrapperService",
                        "rpcName": "ListCreativeWrappers",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CreativeWrapperServiceRestTransport._ListCreativeWrappers._get_response(
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
            resp = creative_wrapper_service.ListCreativeWrappersResponse()
            pb_resp = creative_wrapper_service.ListCreativeWrappersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_creative_wrappers(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_creative_wrappers_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        creative_wrapper_service.ListCreativeWrappersResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.CreativeWrapperServiceClient.list_creative_wrappers",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CreativeWrapperService",
                        "rpcName": "ListCreativeWrappers",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateCreativeWrapper(
        _BaseCreativeWrapperServiceRestTransport._BaseUpdateCreativeWrapper,
        CreativeWrapperServiceRestStub,
    ):
        def __hash__(self):
            return hash("CreativeWrapperServiceRestTransport.UpdateCreativeWrapper")

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
            request: creative_wrapper_service.UpdateCreativeWrapperRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> creative_wrapper_messages.CreativeWrapper:
            r"""Call the update creative wrapper method over HTTP.

            Args:
                request (~.creative_wrapper_service.UpdateCreativeWrapperRequest):
                    The request object. Request object for ``UpdateCreativeWrapper`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.creative_wrapper_messages.CreativeWrapper:
                    A ``CreativeWrapper`` allows the wrapping of HTML
                snippets to be served along with Creative objects.

                ``CreativeWrapper`` must be associated with a
                [LabelType.CREATIVE_WRAPPER][google.ads.admanager.v1.LabelTypeEnum.LabelType.CREATIVE_WRAPPER]
                label and applied to ad units by
                [AdUnit.appliedLabels][google.ads.admanager.v1.AdUnit.applied_labels].

            """

            http_options = _BaseCreativeWrapperServiceRestTransport._BaseUpdateCreativeWrapper._get_http_options()
            request, metadata = self._interceptor.pre_update_creative_wrapper(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCreativeWrapperServiceRestTransport._BaseUpdateCreativeWrapper,
                    "_BaseUpdateCreativeWrapper__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.CreativeWrapperServiceClient.UpdateCreativeWrapper",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CreativeWrapperService",
                        "rpcName": "UpdateCreativeWrapper",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CreativeWrapperServiceRestTransport._UpdateCreativeWrapper._get_response(
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
            resp = creative_wrapper_messages.CreativeWrapper()
            pb_resp = creative_wrapper_messages.CreativeWrapper.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_creative_wrapper(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_creative_wrapper_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        creative_wrapper_messages.CreativeWrapper.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.CreativeWrapperServiceClient.update_creative_wrapper",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CreativeWrapperService",
                        "rpcName": "UpdateCreativeWrapper",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_activate_creative_wrappers(
        self,
    ) -> Callable[
        [creative_wrapper_service.BatchActivateCreativeWrappersRequest],
        creative_wrapper_service.BatchActivateCreativeWrappersResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchActivateCreativeWrappers(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_create_creative_wrappers(
        self,
    ) -> Callable[
        [creative_wrapper_service.BatchCreateCreativeWrappersRequest],
        creative_wrapper_service.BatchCreateCreativeWrappersResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchCreateCreativeWrappers(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_deactivate_creative_wrappers(
        self,
    ) -> Callable[
        [creative_wrapper_service.BatchDeactivateCreativeWrappersRequest],
        creative_wrapper_service.BatchDeactivateCreativeWrappersResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchDeactivateCreativeWrappers(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_update_creative_wrappers(
        self,
    ) -> Callable[
        [creative_wrapper_service.BatchUpdateCreativeWrappersRequest],
        creative_wrapper_service.BatchUpdateCreativeWrappersResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchUpdateCreativeWrappers(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_creative_wrapper(
        self,
    ) -> Callable[
        [creative_wrapper_service.CreateCreativeWrapperRequest],
        creative_wrapper_messages.CreativeWrapper,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateCreativeWrapper(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_creative_wrapper(
        self,
    ) -> Callable[
        [creative_wrapper_service.GetCreativeWrapperRequest],
        creative_wrapper_messages.CreativeWrapper,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetCreativeWrapper(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_creative_wrappers(
        self,
    ) -> Callable[
        [creative_wrapper_service.ListCreativeWrappersRequest],
        creative_wrapper_service.ListCreativeWrappersResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListCreativeWrappers(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_creative_wrapper(
        self,
    ) -> Callable[
        [creative_wrapper_service.UpdateCreativeWrapperRequest],
        creative_wrapper_messages.CreativeWrapper,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateCreativeWrapper(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseCreativeWrapperServiceRestTransport._BaseCancelOperation,
        CreativeWrapperServiceRestStub,
    ):
        def __hash__(self):
            return hash("CreativeWrapperServiceRestTransport.CancelOperation")

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

            http_options = _BaseCreativeWrapperServiceRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCreativeWrapperServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.ads.admanager_v1.CreativeWrapperServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CreativeWrapperService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CreativeWrapperServiceRestTransport._CancelOperation._get_response(
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

            return self._interceptor.post_cancel_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseCreativeWrapperServiceRestTransport._BaseGetOperation,
        CreativeWrapperServiceRestStub,
    ):
        def __hash__(self):
            return hash("CreativeWrapperServiceRestTransport.GetOperation")

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

            http_options = _BaseCreativeWrapperServiceRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCreativeWrapperServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.ads.admanager_v1.CreativeWrapperServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CreativeWrapperService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CreativeWrapperServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.ads.admanager_v1.CreativeWrapperServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.CreativeWrapperService",
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


__all__ = ("CreativeWrapperServiceRestTransport",)
