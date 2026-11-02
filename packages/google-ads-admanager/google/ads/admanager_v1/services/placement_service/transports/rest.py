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
from google.ads.admanager_v1.types import placement_messages, placement_service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BasePlacementServiceRestTransport

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


class PlacementServiceRestInterceptor:
    """Interceptor for PlacementService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the PlacementServiceRestTransport.

    .. code-block:: python
        class MyCustomPlacementServiceInterceptor(PlacementServiceRestInterceptor):
            def pre_batch_activate_placements(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_activate_placements(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_archive_placements(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_archive_placements(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_create_placements(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_create_placements(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_deactivate_placements(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_deactivate_placements(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_update_placements(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_update_placements(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_placement(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_placement(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_placement(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_placement(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_placements(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_placements(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_placement(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_placement(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = PlacementServiceRestTransport(interceptor=MyCustomPlacementServiceInterceptor())
        client = PlacementServiceClient(transport=transport)


    """

    def pre_batch_activate_placements(
        self,
        request: placement_service.BatchActivatePlacementsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        placement_service.BatchActivatePlacementsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_activate_placements

        Override in a subclass to manipulate the request or metadata
        before they are sent to the PlacementService server.
        """
        return request, metadata

    def post_batch_activate_placements(
        self, response: placement_service.BatchActivatePlacementsResponse
    ) -> placement_service.BatchActivatePlacementsResponse:
        """Post-rpc interceptor for batch_activate_placements

        DEPRECATED. Please use the `post_batch_activate_placements_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the PlacementService server but before
        it is returned to user code. This `post_batch_activate_placements` interceptor runs
        before the `post_batch_activate_placements_with_metadata` interceptor.
        """
        return response

    def post_batch_activate_placements_with_metadata(
        self,
        response: placement_service.BatchActivatePlacementsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        placement_service.BatchActivatePlacementsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_activate_placements

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the PlacementService server but before it is returned to user code.

        We recommend only using this `post_batch_activate_placements_with_metadata`
        interceptor in new development instead of the `post_batch_activate_placements` interceptor.
        When both interceptors are used, this `post_batch_activate_placements_with_metadata` interceptor runs after the
        `post_batch_activate_placements` interceptor. The (possibly modified) response returned by
        `post_batch_activate_placements` will be passed to
        `post_batch_activate_placements_with_metadata`.
        """
        return response, metadata

    def pre_batch_archive_placements(
        self,
        request: placement_service.BatchArchivePlacementsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        placement_service.BatchArchivePlacementsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_archive_placements

        Override in a subclass to manipulate the request or metadata
        before they are sent to the PlacementService server.
        """
        return request, metadata

    def post_batch_archive_placements(
        self, response: placement_service.BatchArchivePlacementsResponse
    ) -> placement_service.BatchArchivePlacementsResponse:
        """Post-rpc interceptor for batch_archive_placements

        DEPRECATED. Please use the `post_batch_archive_placements_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the PlacementService server but before
        it is returned to user code. This `post_batch_archive_placements` interceptor runs
        before the `post_batch_archive_placements_with_metadata` interceptor.
        """
        return response

    def post_batch_archive_placements_with_metadata(
        self,
        response: placement_service.BatchArchivePlacementsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        placement_service.BatchArchivePlacementsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_archive_placements

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the PlacementService server but before it is returned to user code.

        We recommend only using this `post_batch_archive_placements_with_metadata`
        interceptor in new development instead of the `post_batch_archive_placements` interceptor.
        When both interceptors are used, this `post_batch_archive_placements_with_metadata` interceptor runs after the
        `post_batch_archive_placements` interceptor. The (possibly modified) response returned by
        `post_batch_archive_placements` will be passed to
        `post_batch_archive_placements_with_metadata`.
        """
        return response, metadata

    def pre_batch_create_placements(
        self,
        request: placement_service.BatchCreatePlacementsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        placement_service.BatchCreatePlacementsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_create_placements

        Override in a subclass to manipulate the request or metadata
        before they are sent to the PlacementService server.
        """
        return request, metadata

    def post_batch_create_placements(
        self, response: placement_service.BatchCreatePlacementsResponse
    ) -> placement_service.BatchCreatePlacementsResponse:
        """Post-rpc interceptor for batch_create_placements

        DEPRECATED. Please use the `post_batch_create_placements_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the PlacementService server but before
        it is returned to user code. This `post_batch_create_placements` interceptor runs
        before the `post_batch_create_placements_with_metadata` interceptor.
        """
        return response

    def post_batch_create_placements_with_metadata(
        self,
        response: placement_service.BatchCreatePlacementsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        placement_service.BatchCreatePlacementsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_create_placements

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the PlacementService server but before it is returned to user code.

        We recommend only using this `post_batch_create_placements_with_metadata`
        interceptor in new development instead of the `post_batch_create_placements` interceptor.
        When both interceptors are used, this `post_batch_create_placements_with_metadata` interceptor runs after the
        `post_batch_create_placements` interceptor. The (possibly modified) response returned by
        `post_batch_create_placements` will be passed to
        `post_batch_create_placements_with_metadata`.
        """
        return response, metadata

    def pre_batch_deactivate_placements(
        self,
        request: placement_service.BatchDeactivatePlacementsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        placement_service.BatchDeactivatePlacementsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_deactivate_placements

        Override in a subclass to manipulate the request or metadata
        before they are sent to the PlacementService server.
        """
        return request, metadata

    def post_batch_deactivate_placements(
        self, response: placement_service.BatchDeactivatePlacementsResponse
    ) -> placement_service.BatchDeactivatePlacementsResponse:
        """Post-rpc interceptor for batch_deactivate_placements

        DEPRECATED. Please use the `post_batch_deactivate_placements_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the PlacementService server but before
        it is returned to user code. This `post_batch_deactivate_placements` interceptor runs
        before the `post_batch_deactivate_placements_with_metadata` interceptor.
        """
        return response

    def post_batch_deactivate_placements_with_metadata(
        self,
        response: placement_service.BatchDeactivatePlacementsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        placement_service.BatchDeactivatePlacementsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_deactivate_placements

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the PlacementService server but before it is returned to user code.

        We recommend only using this `post_batch_deactivate_placements_with_metadata`
        interceptor in new development instead of the `post_batch_deactivate_placements` interceptor.
        When both interceptors are used, this `post_batch_deactivate_placements_with_metadata` interceptor runs after the
        `post_batch_deactivate_placements` interceptor. The (possibly modified) response returned by
        `post_batch_deactivate_placements` will be passed to
        `post_batch_deactivate_placements_with_metadata`.
        """
        return response, metadata

    def pre_batch_update_placements(
        self,
        request: placement_service.BatchUpdatePlacementsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        placement_service.BatchUpdatePlacementsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_update_placements

        Override in a subclass to manipulate the request or metadata
        before they are sent to the PlacementService server.
        """
        return request, metadata

    def post_batch_update_placements(
        self, response: placement_service.BatchUpdatePlacementsResponse
    ) -> placement_service.BatchUpdatePlacementsResponse:
        """Post-rpc interceptor for batch_update_placements

        DEPRECATED. Please use the `post_batch_update_placements_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the PlacementService server but before
        it is returned to user code. This `post_batch_update_placements` interceptor runs
        before the `post_batch_update_placements_with_metadata` interceptor.
        """
        return response

    def post_batch_update_placements_with_metadata(
        self,
        response: placement_service.BatchUpdatePlacementsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        placement_service.BatchUpdatePlacementsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_update_placements

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the PlacementService server but before it is returned to user code.

        We recommend only using this `post_batch_update_placements_with_metadata`
        interceptor in new development instead of the `post_batch_update_placements` interceptor.
        When both interceptors are used, this `post_batch_update_placements_with_metadata` interceptor runs after the
        `post_batch_update_placements` interceptor. The (possibly modified) response returned by
        `post_batch_update_placements` will be passed to
        `post_batch_update_placements_with_metadata`.
        """
        return response, metadata

    def pre_create_placement(
        self,
        request: placement_service.CreatePlacementRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        placement_service.CreatePlacementRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_placement

        Override in a subclass to manipulate the request or metadata
        before they are sent to the PlacementService server.
        """
        return request, metadata

    def post_create_placement(
        self, response: placement_messages.Placement
    ) -> placement_messages.Placement:
        """Post-rpc interceptor for create_placement

        DEPRECATED. Please use the `post_create_placement_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the PlacementService server but before
        it is returned to user code. This `post_create_placement` interceptor runs
        before the `post_create_placement_with_metadata` interceptor.
        """
        return response

    def post_create_placement_with_metadata(
        self,
        response: placement_messages.Placement,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[placement_messages.Placement, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_placement

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the PlacementService server but before it is returned to user code.

        We recommend only using this `post_create_placement_with_metadata`
        interceptor in new development instead of the `post_create_placement` interceptor.
        When both interceptors are used, this `post_create_placement_with_metadata` interceptor runs after the
        `post_create_placement` interceptor. The (possibly modified) response returned by
        `post_create_placement` will be passed to
        `post_create_placement_with_metadata`.
        """
        return response, metadata

    def pre_get_placement(
        self,
        request: placement_service.GetPlacementRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        placement_service.GetPlacementRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_placement

        Override in a subclass to manipulate the request or metadata
        before they are sent to the PlacementService server.
        """
        return request, metadata

    def post_get_placement(
        self, response: placement_messages.Placement
    ) -> placement_messages.Placement:
        """Post-rpc interceptor for get_placement

        DEPRECATED. Please use the `post_get_placement_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the PlacementService server but before
        it is returned to user code. This `post_get_placement` interceptor runs
        before the `post_get_placement_with_metadata` interceptor.
        """
        return response

    def post_get_placement_with_metadata(
        self,
        response: placement_messages.Placement,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[placement_messages.Placement, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_placement

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the PlacementService server but before it is returned to user code.

        We recommend only using this `post_get_placement_with_metadata`
        interceptor in new development instead of the `post_get_placement` interceptor.
        When both interceptors are used, this `post_get_placement_with_metadata` interceptor runs after the
        `post_get_placement` interceptor. The (possibly modified) response returned by
        `post_get_placement` will be passed to
        `post_get_placement_with_metadata`.
        """
        return response, metadata

    def pre_list_placements(
        self,
        request: placement_service.ListPlacementsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        placement_service.ListPlacementsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_placements

        Override in a subclass to manipulate the request or metadata
        before they are sent to the PlacementService server.
        """
        return request, metadata

    def post_list_placements(
        self, response: placement_service.ListPlacementsResponse
    ) -> placement_service.ListPlacementsResponse:
        """Post-rpc interceptor for list_placements

        DEPRECATED. Please use the `post_list_placements_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the PlacementService server but before
        it is returned to user code. This `post_list_placements` interceptor runs
        before the `post_list_placements_with_metadata` interceptor.
        """
        return response

    def post_list_placements_with_metadata(
        self,
        response: placement_service.ListPlacementsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        placement_service.ListPlacementsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_placements

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the PlacementService server but before it is returned to user code.

        We recommend only using this `post_list_placements_with_metadata`
        interceptor in new development instead of the `post_list_placements` interceptor.
        When both interceptors are used, this `post_list_placements_with_metadata` interceptor runs after the
        `post_list_placements` interceptor. The (possibly modified) response returned by
        `post_list_placements` will be passed to
        `post_list_placements_with_metadata`.
        """
        return response, metadata

    def pre_update_placement(
        self,
        request: placement_service.UpdatePlacementRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        placement_service.UpdatePlacementRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_placement

        Override in a subclass to manipulate the request or metadata
        before they are sent to the PlacementService server.
        """
        return request, metadata

    def post_update_placement(
        self, response: placement_messages.Placement
    ) -> placement_messages.Placement:
        """Post-rpc interceptor for update_placement

        DEPRECATED. Please use the `post_update_placement_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the PlacementService server but before
        it is returned to user code. This `post_update_placement` interceptor runs
        before the `post_update_placement_with_metadata` interceptor.
        """
        return response

    def post_update_placement_with_metadata(
        self,
        response: placement_messages.Placement,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[placement_messages.Placement, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_placement

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the PlacementService server but before it is returned to user code.

        We recommend only using this `post_update_placement_with_metadata`
        interceptor in new development instead of the `post_update_placement` interceptor.
        When both interceptors are used, this `post_update_placement_with_metadata` interceptor runs after the
        `post_update_placement` interceptor. The (possibly modified) response returned by
        `post_update_placement` will be passed to
        `post_update_placement_with_metadata`.
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
        before they are sent to the PlacementService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the PlacementService server but before
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
        before they are sent to the PlacementService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the PlacementService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class PlacementServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: PlacementServiceRestInterceptor


class PlacementServiceRestTransport(_BasePlacementServiceRestTransport):
    """REST backend synchronous transport for PlacementService.

    Provides methods for handling ``Placement`` objects.

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
        interceptor: Optional[PlacementServiceRestInterceptor] = None,
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
            interceptor (Optional[PlacementServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or PlacementServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _BatchActivatePlacements(
        _BasePlacementServiceRestTransport._BaseBatchActivatePlacements,
        PlacementServiceRestStub,
    ):
        def __hash__(self):
            return hash("PlacementServiceRestTransport.BatchActivatePlacements")

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
            request: placement_service.BatchActivatePlacementsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> placement_service.BatchActivatePlacementsResponse:
            r"""Call the batch activate placements method over HTTP.

            Args:
                request (~.placement_service.BatchActivatePlacementsRequest):
                    The request object. Request message for ``BatchActivatePlacements`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.placement_service.BatchActivatePlacementsResponse:
                    Response object for ``BatchActivatePlacements`` method.
            """

            http_options = _BasePlacementServiceRestTransport._BaseBatchActivatePlacements._get_http_options()
            request, metadata = self._interceptor.pre_batch_activate_placements(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePlacementServiceRestTransport._BaseBatchActivatePlacements,
                    "_BaseBatchActivatePlacements__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.PlacementServiceClient.BatchActivatePlacements",
                    extra={
                        "serviceName": "google.ads.admanager.v1.PlacementService",
                        "rpcName": "BatchActivatePlacements",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                PlacementServiceRestTransport._BatchActivatePlacements._get_response(
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
            resp = placement_service.BatchActivatePlacementsResponse()
            pb_resp = placement_service.BatchActivatePlacementsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_activate_placements(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_activate_placements_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        placement_service.BatchActivatePlacementsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.PlacementServiceClient.batch_activate_placements",
                    extra={
                        "serviceName": "google.ads.admanager.v1.PlacementService",
                        "rpcName": "BatchActivatePlacements",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchArchivePlacements(
        _BasePlacementServiceRestTransport._BaseBatchArchivePlacements,
        PlacementServiceRestStub,
    ):
        def __hash__(self):
            return hash("PlacementServiceRestTransport.BatchArchivePlacements")

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
            request: placement_service.BatchArchivePlacementsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> placement_service.BatchArchivePlacementsResponse:
            r"""Call the batch archive placements method over HTTP.

            Args:
                request (~.placement_service.BatchArchivePlacementsRequest):
                    The request object. Request message for ``BatchArchivePlacements`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.placement_service.BatchArchivePlacementsResponse:
                    Response object for ``BatchArchivePlacements`` method.
            """

            http_options = _BasePlacementServiceRestTransport._BaseBatchArchivePlacements._get_http_options()
            request, metadata = self._interceptor.pre_batch_archive_placements(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePlacementServiceRestTransport._BaseBatchArchivePlacements,
                    "_BaseBatchArchivePlacements__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.PlacementServiceClient.BatchArchivePlacements",
                    extra={
                        "serviceName": "google.ads.admanager.v1.PlacementService",
                        "rpcName": "BatchArchivePlacements",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                PlacementServiceRestTransport._BatchArchivePlacements._get_response(
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
            resp = placement_service.BatchArchivePlacementsResponse()
            pb_resp = placement_service.BatchArchivePlacementsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_archive_placements(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_archive_placements_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        placement_service.BatchArchivePlacementsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.PlacementServiceClient.batch_archive_placements",
                    extra={
                        "serviceName": "google.ads.admanager.v1.PlacementService",
                        "rpcName": "BatchArchivePlacements",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchCreatePlacements(
        _BasePlacementServiceRestTransport._BaseBatchCreatePlacements,
        PlacementServiceRestStub,
    ):
        def __hash__(self):
            return hash("PlacementServiceRestTransport.BatchCreatePlacements")

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
            request: placement_service.BatchCreatePlacementsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> placement_service.BatchCreatePlacementsResponse:
            r"""Call the batch create placements method over HTTP.

            Args:
                request (~.placement_service.BatchCreatePlacementsRequest):
                    The request object. Request object for ``BatchCreatePlacements`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.placement_service.BatchCreatePlacementsResponse:
                    Response object for ``BatchCreatePlacements`` method.
            """

            http_options = _BasePlacementServiceRestTransport._BaseBatchCreatePlacements._get_http_options()
            request, metadata = self._interceptor.pre_batch_create_placements(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePlacementServiceRestTransport._BaseBatchCreatePlacements,
                    "_BaseBatchCreatePlacements__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.PlacementServiceClient.BatchCreatePlacements",
                    extra={
                        "serviceName": "google.ads.admanager.v1.PlacementService",
                        "rpcName": "BatchCreatePlacements",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                PlacementServiceRestTransport._BatchCreatePlacements._get_response(
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
            resp = placement_service.BatchCreatePlacementsResponse()
            pb_resp = placement_service.BatchCreatePlacementsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_create_placements(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_create_placements_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        placement_service.BatchCreatePlacementsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.PlacementServiceClient.batch_create_placements",
                    extra={
                        "serviceName": "google.ads.admanager.v1.PlacementService",
                        "rpcName": "BatchCreatePlacements",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchDeactivatePlacements(
        _BasePlacementServiceRestTransport._BaseBatchDeactivatePlacements,
        PlacementServiceRestStub,
    ):
        def __hash__(self):
            return hash("PlacementServiceRestTransport.BatchDeactivatePlacements")

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
            request: placement_service.BatchDeactivatePlacementsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> placement_service.BatchDeactivatePlacementsResponse:
            r"""Call the batch deactivate
            placements method over HTTP.

                Args:
                    request (~.placement_service.BatchDeactivatePlacementsRequest):
                        The request object. Request message for ``BatchDeactivatePlacements``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.placement_service.BatchDeactivatePlacementsResponse:
                        Response object for ``BatchDeactivatePlacements``
                    method.

            """

            http_options = _BasePlacementServiceRestTransport._BaseBatchDeactivatePlacements._get_http_options()
            request, metadata = self._interceptor.pre_batch_deactivate_placements(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePlacementServiceRestTransport._BaseBatchDeactivatePlacements,
                    "_BaseBatchDeactivatePlacements__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.PlacementServiceClient.BatchDeactivatePlacements",
                    extra={
                        "serviceName": "google.ads.admanager.v1.PlacementService",
                        "rpcName": "BatchDeactivatePlacements",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                PlacementServiceRestTransport._BatchDeactivatePlacements._get_response(
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
            resp = placement_service.BatchDeactivatePlacementsResponse()
            pb_resp = placement_service.BatchDeactivatePlacementsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_deactivate_placements(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_deactivate_placements_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        placement_service.BatchDeactivatePlacementsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.PlacementServiceClient.batch_deactivate_placements",
                    extra={
                        "serviceName": "google.ads.admanager.v1.PlacementService",
                        "rpcName": "BatchDeactivatePlacements",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchUpdatePlacements(
        _BasePlacementServiceRestTransport._BaseBatchUpdatePlacements,
        PlacementServiceRestStub,
    ):
        def __hash__(self):
            return hash("PlacementServiceRestTransport.BatchUpdatePlacements")

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
            request: placement_service.BatchUpdatePlacementsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> placement_service.BatchUpdatePlacementsResponse:
            r"""Call the batch update placements method over HTTP.

            Args:
                request (~.placement_service.BatchUpdatePlacementsRequest):
                    The request object. Request object for ``BatchUpdatePlacements`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.placement_service.BatchUpdatePlacementsResponse:
                    Response object for ``BatchUpdatePlacements`` method.
            """

            http_options = _BasePlacementServiceRestTransport._BaseBatchUpdatePlacements._get_http_options()
            request, metadata = self._interceptor.pre_batch_update_placements(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePlacementServiceRestTransport._BaseBatchUpdatePlacements,
                    "_BaseBatchUpdatePlacements__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.PlacementServiceClient.BatchUpdatePlacements",
                    extra={
                        "serviceName": "google.ads.admanager.v1.PlacementService",
                        "rpcName": "BatchUpdatePlacements",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                PlacementServiceRestTransport._BatchUpdatePlacements._get_response(
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
            resp = placement_service.BatchUpdatePlacementsResponse()
            pb_resp = placement_service.BatchUpdatePlacementsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_update_placements(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_update_placements_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        placement_service.BatchUpdatePlacementsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.PlacementServiceClient.batch_update_placements",
                    extra={
                        "serviceName": "google.ads.admanager.v1.PlacementService",
                        "rpcName": "BatchUpdatePlacements",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreatePlacement(
        _BasePlacementServiceRestTransport._BaseCreatePlacement,
        PlacementServiceRestStub,
    ):
        def __hash__(self):
            return hash("PlacementServiceRestTransport.CreatePlacement")

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
            request: placement_service.CreatePlacementRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> placement_messages.Placement:
            r"""Call the create placement method over HTTP.

            Args:
                request (~.placement_service.CreatePlacementRequest):
                    The request object. Request object for ``CreatePlacement`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.placement_messages.Placement:
                    The ``Placement`` resource.
            """

            http_options = _BasePlacementServiceRestTransport._BaseCreatePlacement._get_http_options()
            request, metadata = self._interceptor.pre_create_placement(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePlacementServiceRestTransport._BaseCreatePlacement,
                    "_BaseCreatePlacement__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.PlacementServiceClient.CreatePlacement",
                    extra={
                        "serviceName": "google.ads.admanager.v1.PlacementService",
                        "rpcName": "CreatePlacement",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PlacementServiceRestTransport._CreatePlacement._get_response(
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
            resp = placement_messages.Placement()
            pb_resp = placement_messages.Placement.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_placement(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_placement_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = placement_messages.Placement.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.PlacementServiceClient.create_placement",
                    extra={
                        "serviceName": "google.ads.admanager.v1.PlacementService",
                        "rpcName": "CreatePlacement",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetPlacement(
        _BasePlacementServiceRestTransport._BaseGetPlacement, PlacementServiceRestStub
    ):
        def __hash__(self):
            return hash("PlacementServiceRestTransport.GetPlacement")

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
            request: placement_service.GetPlacementRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> placement_messages.Placement:
            r"""Call the get placement method over HTTP.

            Args:
                request (~.placement_service.GetPlacementRequest):
                    The request object. Request object for ``GetPlacement`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.placement_messages.Placement:
                    The ``Placement`` resource.
            """

            http_options = (
                _BasePlacementServiceRestTransport._BaseGetPlacement._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_placement(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePlacementServiceRestTransport._BaseGetPlacement,
                    "_BaseGetPlacement__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.PlacementServiceClient.GetPlacement",
                    extra={
                        "serviceName": "google.ads.admanager.v1.PlacementService",
                        "rpcName": "GetPlacement",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PlacementServiceRestTransport._GetPlacement._get_response(
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
            resp = placement_messages.Placement()
            pb_resp = placement_messages.Placement.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_placement(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_placement_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = placement_messages.Placement.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.PlacementServiceClient.get_placement",
                    extra={
                        "serviceName": "google.ads.admanager.v1.PlacementService",
                        "rpcName": "GetPlacement",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListPlacements(
        _BasePlacementServiceRestTransport._BaseListPlacements, PlacementServiceRestStub
    ):
        def __hash__(self):
            return hash("PlacementServiceRestTransport.ListPlacements")

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
            request: placement_service.ListPlacementsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> placement_service.ListPlacementsResponse:
            r"""Call the list placements method over HTTP.

            Args:
                request (~.placement_service.ListPlacementsRequest):
                    The request object. Request object for ``ListPlacements`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.placement_service.ListPlacementsResponse:
                    Response object for ``ListPlacementsRequest`` containing
                matching ``Placement`` objects.

            """

            http_options = _BasePlacementServiceRestTransport._BaseListPlacements._get_http_options()
            request, metadata = self._interceptor.pre_list_placements(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePlacementServiceRestTransport._BaseListPlacements,
                    "_BaseListPlacements__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.PlacementServiceClient.ListPlacements",
                    extra={
                        "serviceName": "google.ads.admanager.v1.PlacementService",
                        "rpcName": "ListPlacements",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PlacementServiceRestTransport._ListPlacements._get_response(
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
            resp = placement_service.ListPlacementsResponse()
            pb_resp = placement_service.ListPlacementsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_placements(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_placements_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = placement_service.ListPlacementsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.PlacementServiceClient.list_placements",
                    extra={
                        "serviceName": "google.ads.admanager.v1.PlacementService",
                        "rpcName": "ListPlacements",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdatePlacement(
        _BasePlacementServiceRestTransport._BaseUpdatePlacement,
        PlacementServiceRestStub,
    ):
        def __hash__(self):
            return hash("PlacementServiceRestTransport.UpdatePlacement")

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
            request: placement_service.UpdatePlacementRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> placement_messages.Placement:
            r"""Call the update placement method over HTTP.

            Args:
                request (~.placement_service.UpdatePlacementRequest):
                    The request object. Request object for ``UpdatePlacement`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.placement_messages.Placement:
                    The ``Placement`` resource.
            """

            http_options = _BasePlacementServiceRestTransport._BaseUpdatePlacement._get_http_options()
            request, metadata = self._interceptor.pre_update_placement(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePlacementServiceRestTransport._BaseUpdatePlacement,
                    "_BaseUpdatePlacement__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.PlacementServiceClient.UpdatePlacement",
                    extra={
                        "serviceName": "google.ads.admanager.v1.PlacementService",
                        "rpcName": "UpdatePlacement",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PlacementServiceRestTransport._UpdatePlacement._get_response(
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
            resp = placement_messages.Placement()
            pb_resp = placement_messages.Placement.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_placement(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_placement_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = placement_messages.Placement.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.PlacementServiceClient.update_placement",
                    extra={
                        "serviceName": "google.ads.admanager.v1.PlacementService",
                        "rpcName": "UpdatePlacement",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_activate_placements(
        self,
    ) -> Callable[
        [placement_service.BatchActivatePlacementsRequest],
        placement_service.BatchActivatePlacementsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchActivatePlacements(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_archive_placements(
        self,
    ) -> Callable[
        [placement_service.BatchArchivePlacementsRequest],
        placement_service.BatchArchivePlacementsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchArchivePlacements(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_create_placements(
        self,
    ) -> Callable[
        [placement_service.BatchCreatePlacementsRequest],
        placement_service.BatchCreatePlacementsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchCreatePlacements(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_deactivate_placements(
        self,
    ) -> Callable[
        [placement_service.BatchDeactivatePlacementsRequest],
        placement_service.BatchDeactivatePlacementsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchDeactivatePlacements(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_update_placements(
        self,
    ) -> Callable[
        [placement_service.BatchUpdatePlacementsRequest],
        placement_service.BatchUpdatePlacementsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchUpdatePlacements(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_placement(
        self,
    ) -> Callable[
        [placement_service.CreatePlacementRequest], placement_messages.Placement
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreatePlacement(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_placement(
        self,
    ) -> Callable[
        [placement_service.GetPlacementRequest], placement_messages.Placement
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetPlacement(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_placements(
        self,
    ) -> Callable[
        [placement_service.ListPlacementsRequest],
        placement_service.ListPlacementsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListPlacements(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_placement(
        self,
    ) -> Callable[
        [placement_service.UpdatePlacementRequest], placement_messages.Placement
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdatePlacement(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BasePlacementServiceRestTransport._BaseCancelOperation,
        PlacementServiceRestStub,
    ):
        def __hash__(self):
            return hash("PlacementServiceRestTransport.CancelOperation")

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

            http_options = _BasePlacementServiceRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePlacementServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.ads.admanager_v1.PlacementServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.PlacementService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PlacementServiceRestTransport._CancelOperation._get_response(
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
        _BasePlacementServiceRestTransport._BaseGetOperation, PlacementServiceRestStub
    ):
        def __hash__(self):
            return hash("PlacementServiceRestTransport.GetOperation")

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
                _BasePlacementServiceRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePlacementServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.ads.admanager_v1.PlacementServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.PlacementService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PlacementServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.ads.admanager_v1.PlacementServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.PlacementService",
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


__all__ = ("PlacementServiceRestTransport",)
