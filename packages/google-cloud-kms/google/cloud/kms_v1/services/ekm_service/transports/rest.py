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
from google.cloud.location import locations_pb2  # type: ignore
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.kms_v1._compat import transcode_request
from google.cloud.kms_v1.types import ekm_service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseEkmServiceRestTransport

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


class EkmServiceRestInterceptor:
    """Interceptor for EkmService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the EkmServiceRestTransport.

    .. code-block:: python
        class MyCustomEkmServiceInterceptor(EkmServiceRestInterceptor):
            def pre_create_ekm_connection(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_ekm_connection(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_ekm_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_ekm_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_ekm_connection(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_ekm_connection(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_ekm_connections(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_ekm_connections(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_ekm_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_ekm_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_ekm_connection(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_ekm_connection(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_verify_connectivity(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_verify_connectivity(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = EkmServiceRestTransport(interceptor=MyCustomEkmServiceInterceptor())
        client = EkmServiceClient(transport=transport)


    """

    def pre_create_ekm_connection(
        self,
        request: ekm_service.CreateEkmConnectionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ekm_service.CreateEkmConnectionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_ekm_connection

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EkmService server.
        """
        return request, metadata

    def post_create_ekm_connection(
        self, response: ekm_service.EkmConnection
    ) -> ekm_service.EkmConnection:
        """Post-rpc interceptor for create_ekm_connection

        DEPRECATED. Please use the `post_create_ekm_connection_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EkmService server but before
        it is returned to user code. This `post_create_ekm_connection` interceptor runs
        before the `post_create_ekm_connection_with_metadata` interceptor.
        """
        return response

    def post_create_ekm_connection_with_metadata(
        self,
        response: ekm_service.EkmConnection,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[ekm_service.EkmConnection, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_ekm_connection

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EkmService server but before it is returned to user code.

        We recommend only using this `post_create_ekm_connection_with_metadata`
        interceptor in new development instead of the `post_create_ekm_connection` interceptor.
        When both interceptors are used, this `post_create_ekm_connection_with_metadata` interceptor runs after the
        `post_create_ekm_connection` interceptor. The (possibly modified) response returned by
        `post_create_ekm_connection` will be passed to
        `post_create_ekm_connection_with_metadata`.
        """
        return response, metadata

    def pre_get_ekm_config(
        self,
        request: ekm_service.GetEkmConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ekm_service.GetEkmConfigRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_ekm_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EkmService server.
        """
        return request, metadata

    def post_get_ekm_config(
        self, response: ekm_service.EkmConfig
    ) -> ekm_service.EkmConfig:
        """Post-rpc interceptor for get_ekm_config

        DEPRECATED. Please use the `post_get_ekm_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EkmService server but before
        it is returned to user code. This `post_get_ekm_config` interceptor runs
        before the `post_get_ekm_config_with_metadata` interceptor.
        """
        return response

    def post_get_ekm_config_with_metadata(
        self,
        response: ekm_service.EkmConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[ekm_service.EkmConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_ekm_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EkmService server but before it is returned to user code.

        We recommend only using this `post_get_ekm_config_with_metadata`
        interceptor in new development instead of the `post_get_ekm_config` interceptor.
        When both interceptors are used, this `post_get_ekm_config_with_metadata` interceptor runs after the
        `post_get_ekm_config` interceptor. The (possibly modified) response returned by
        `post_get_ekm_config` will be passed to
        `post_get_ekm_config_with_metadata`.
        """
        return response, metadata

    def pre_get_ekm_connection(
        self,
        request: ekm_service.GetEkmConnectionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ekm_service.GetEkmConnectionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_ekm_connection

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EkmService server.
        """
        return request, metadata

    def post_get_ekm_connection(
        self, response: ekm_service.EkmConnection
    ) -> ekm_service.EkmConnection:
        """Post-rpc interceptor for get_ekm_connection

        DEPRECATED. Please use the `post_get_ekm_connection_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EkmService server but before
        it is returned to user code. This `post_get_ekm_connection` interceptor runs
        before the `post_get_ekm_connection_with_metadata` interceptor.
        """
        return response

    def post_get_ekm_connection_with_metadata(
        self,
        response: ekm_service.EkmConnection,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[ekm_service.EkmConnection, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_ekm_connection

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EkmService server but before it is returned to user code.

        We recommend only using this `post_get_ekm_connection_with_metadata`
        interceptor in new development instead of the `post_get_ekm_connection` interceptor.
        When both interceptors are used, this `post_get_ekm_connection_with_metadata` interceptor runs after the
        `post_get_ekm_connection` interceptor. The (possibly modified) response returned by
        `post_get_ekm_connection` will be passed to
        `post_get_ekm_connection_with_metadata`.
        """
        return response, metadata

    def pre_list_ekm_connections(
        self,
        request: ekm_service.ListEkmConnectionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ekm_service.ListEkmConnectionsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_ekm_connections

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EkmService server.
        """
        return request, metadata

    def post_list_ekm_connections(
        self, response: ekm_service.ListEkmConnectionsResponse
    ) -> ekm_service.ListEkmConnectionsResponse:
        """Post-rpc interceptor for list_ekm_connections

        DEPRECATED. Please use the `post_list_ekm_connections_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EkmService server but before
        it is returned to user code. This `post_list_ekm_connections` interceptor runs
        before the `post_list_ekm_connections_with_metadata` interceptor.
        """
        return response

    def post_list_ekm_connections_with_metadata(
        self,
        response: ekm_service.ListEkmConnectionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ekm_service.ListEkmConnectionsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_ekm_connections

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EkmService server but before it is returned to user code.

        We recommend only using this `post_list_ekm_connections_with_metadata`
        interceptor in new development instead of the `post_list_ekm_connections` interceptor.
        When both interceptors are used, this `post_list_ekm_connections_with_metadata` interceptor runs after the
        `post_list_ekm_connections` interceptor. The (possibly modified) response returned by
        `post_list_ekm_connections` will be passed to
        `post_list_ekm_connections_with_metadata`.
        """
        return response, metadata

    def pre_update_ekm_config(
        self,
        request: ekm_service.UpdateEkmConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ekm_service.UpdateEkmConfigRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_ekm_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EkmService server.
        """
        return request, metadata

    def post_update_ekm_config(
        self, response: ekm_service.EkmConfig
    ) -> ekm_service.EkmConfig:
        """Post-rpc interceptor for update_ekm_config

        DEPRECATED. Please use the `post_update_ekm_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EkmService server but before
        it is returned to user code. This `post_update_ekm_config` interceptor runs
        before the `post_update_ekm_config_with_metadata` interceptor.
        """
        return response

    def post_update_ekm_config_with_metadata(
        self,
        response: ekm_service.EkmConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[ekm_service.EkmConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_ekm_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EkmService server but before it is returned to user code.

        We recommend only using this `post_update_ekm_config_with_metadata`
        interceptor in new development instead of the `post_update_ekm_config` interceptor.
        When both interceptors are used, this `post_update_ekm_config_with_metadata` interceptor runs after the
        `post_update_ekm_config` interceptor. The (possibly modified) response returned by
        `post_update_ekm_config` will be passed to
        `post_update_ekm_config_with_metadata`.
        """
        return response, metadata

    def pre_update_ekm_connection(
        self,
        request: ekm_service.UpdateEkmConnectionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ekm_service.UpdateEkmConnectionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_ekm_connection

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EkmService server.
        """
        return request, metadata

    def post_update_ekm_connection(
        self, response: ekm_service.EkmConnection
    ) -> ekm_service.EkmConnection:
        """Post-rpc interceptor for update_ekm_connection

        DEPRECATED. Please use the `post_update_ekm_connection_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EkmService server but before
        it is returned to user code. This `post_update_ekm_connection` interceptor runs
        before the `post_update_ekm_connection_with_metadata` interceptor.
        """
        return response

    def post_update_ekm_connection_with_metadata(
        self,
        response: ekm_service.EkmConnection,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[ekm_service.EkmConnection, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_ekm_connection

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EkmService server but before it is returned to user code.

        We recommend only using this `post_update_ekm_connection_with_metadata`
        interceptor in new development instead of the `post_update_ekm_connection` interceptor.
        When both interceptors are used, this `post_update_ekm_connection_with_metadata` interceptor runs after the
        `post_update_ekm_connection` interceptor. The (possibly modified) response returned by
        `post_update_ekm_connection` will be passed to
        `post_update_ekm_connection_with_metadata`.
        """
        return response, metadata

    def pre_verify_connectivity(
        self,
        request: ekm_service.VerifyConnectivityRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ekm_service.VerifyConnectivityRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for verify_connectivity

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EkmService server.
        """
        return request, metadata

    def post_verify_connectivity(
        self, response: ekm_service.VerifyConnectivityResponse
    ) -> ekm_service.VerifyConnectivityResponse:
        """Post-rpc interceptor for verify_connectivity

        DEPRECATED. Please use the `post_verify_connectivity_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the EkmService server but before
        it is returned to user code. This `post_verify_connectivity` interceptor runs
        before the `post_verify_connectivity_with_metadata` interceptor.
        """
        return response

    def post_verify_connectivity_with_metadata(
        self,
        response: ekm_service.VerifyConnectivityResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ekm_service.VerifyConnectivityResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for verify_connectivity

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the EkmService server but before it is returned to user code.

        We recommend only using this `post_verify_connectivity_with_metadata`
        interceptor in new development instead of the `post_verify_connectivity` interceptor.
        When both interceptors are used, this `post_verify_connectivity_with_metadata` interceptor runs after the
        `post_verify_connectivity` interceptor. The (possibly modified) response returned by
        `post_verify_connectivity` will be passed to
        `post_verify_connectivity_with_metadata`.
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
        before they are sent to the EkmService server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the EkmService server but before
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
        before they are sent to the EkmService server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the EkmService server but before
        it is returned to user code.
        """
        return response

    def pre_get_iam_policy(
        self,
        request: iam_policy_pb2.GetIamPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.GetIamPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EkmService server.
        """
        return request, metadata

    def post_get_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the EkmService server but before
        it is returned to user code.
        """
        return response

    def pre_set_iam_policy(
        self,
        request: iam_policy_pb2.SetIamPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.SetIamPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EkmService server.
        """
        return request, metadata

    def post_set_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the EkmService server but before
        it is returned to user code.
        """
        return response

    def pre_test_iam_permissions(
        self,
        request: iam_policy_pb2.TestIamPermissionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.TestIamPermissionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the EkmService server.
        """
        return request, metadata

    def post_test_iam_permissions(
        self, response: iam_policy_pb2.TestIamPermissionsResponse
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the response
        after it is returned by the EkmService server but before
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
        before they are sent to the EkmService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the EkmService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class EkmServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: EkmServiceRestInterceptor


class EkmServiceRestTransport(_BaseEkmServiceRestTransport):
    """REST backend synchronous transport for EkmService.

    Google Cloud Key Management EKM Service

    Manages external cryptographic keys and operations using those keys.
    Implements a REST model with the following objects:

    - [EkmConnection][google.cloud.kms.v1.EkmConnection]

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "cloudkms.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[EkmServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'cloudkms.googleapis.com').
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
            interceptor (Optional[EkmServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or EkmServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CreateEkmConnection(
        _BaseEkmServiceRestTransport._BaseCreateEkmConnection, EkmServiceRestStub
    ):
        def __hash__(self):
            return hash("EkmServiceRestTransport.CreateEkmConnection")

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
            request: ekm_service.CreateEkmConnectionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ekm_service.EkmConnection:
            r"""Call the create ekm connection method over HTTP.

            Args:
                request (~.ekm_service.CreateEkmConnectionRequest):
                    The request object. Request message for
                [EkmService.CreateEkmConnection][google.cloud.kms.v1.EkmService.CreateEkmConnection].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ekm_service.EkmConnection:
                    An [EkmConnection][google.cloud.kms.v1.EkmConnection]
                represents an individual EKM connection. It can be used
                for creating [CryptoKeys][google.cloud.kms.v1.CryptoKey]
                and
                [CryptoKeyVersions][google.cloud.kms.v1.CryptoKeyVersion]
                with a
                [ProtectionLevel][google.cloud.kms.v1.ProtectionLevel]
                of
                [EXTERNAL_VPC][google.cloud.kms.v1.ProtectionLevel.EXTERNAL_VPC],
                as well as performing cryptographic operations using
                keys created within the
                [EkmConnection][google.cloud.kms.v1.EkmConnection].

            """

            http_options = _BaseEkmServiceRestTransport._BaseCreateEkmConnection._get_http_options()
            request, metadata = self._interceptor.pre_create_ekm_connection(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEkmServiceRestTransport._BaseCreateEkmConnection,
                    "_BaseCreateEkmConnection__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.EkmServiceClient.CreateEkmConnection",
                    extra={
                        "serviceName": "google.cloud.kms.v1.EkmService",
                        "rpcName": "CreateEkmConnection",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EkmServiceRestTransport._CreateEkmConnection._get_response(
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
            resp = ekm_service.EkmConnection()
            pb_resp = ekm_service.EkmConnection.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_ekm_connection(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_ekm_connection_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = ekm_service.EkmConnection.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.kms_v1.EkmServiceClient.create_ekm_connection",
                    extra={
                        "serviceName": "google.cloud.kms.v1.EkmService",
                        "rpcName": "CreateEkmConnection",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetEkmConfig(
        _BaseEkmServiceRestTransport._BaseGetEkmConfig, EkmServiceRestStub
    ):
        def __hash__(self):
            return hash("EkmServiceRestTransport.GetEkmConfig")

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
            request: ekm_service.GetEkmConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ekm_service.EkmConfig:
            r"""Call the get ekm config method over HTTP.

            Args:
                request (~.ekm_service.GetEkmConfigRequest):
                    The request object. Request message for
                [EkmService.GetEkmConfig][google.cloud.kms.v1.EkmService.GetEkmConfig].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ekm_service.EkmConfig:
                    An [EkmConfig][google.cloud.kms.v1.EkmConfig] is a
                singleton resource that represents configuration
                parameters that apply to all
                [CryptoKeys][google.cloud.kms.v1.CryptoKey] and
                [CryptoKeyVersions][google.cloud.kms.v1.CryptoKeyVersion]
                with a
                [ProtectionLevel][google.cloud.kms.v1.ProtectionLevel]
                of
                [EXTERNAL_VPC][google.cloud.kms.v1.ProtectionLevel.EXTERNAL_VPC]
                in a given project and location.

            """

            http_options = (
                _BaseEkmServiceRestTransport._BaseGetEkmConfig._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_ekm_config(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEkmServiceRestTransport._BaseGetEkmConfig,
                    "_BaseGetEkmConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.EkmServiceClient.GetEkmConfig",
                    extra={
                        "serviceName": "google.cloud.kms.v1.EkmService",
                        "rpcName": "GetEkmConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EkmServiceRestTransport._GetEkmConfig._get_response(
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
            resp = ekm_service.EkmConfig()
            pb_resp = ekm_service.EkmConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_ekm_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_ekm_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = ekm_service.EkmConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.kms_v1.EkmServiceClient.get_ekm_config",
                    extra={
                        "serviceName": "google.cloud.kms.v1.EkmService",
                        "rpcName": "GetEkmConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetEkmConnection(
        _BaseEkmServiceRestTransport._BaseGetEkmConnection, EkmServiceRestStub
    ):
        def __hash__(self):
            return hash("EkmServiceRestTransport.GetEkmConnection")

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
            request: ekm_service.GetEkmConnectionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ekm_service.EkmConnection:
            r"""Call the get ekm connection method over HTTP.

            Args:
                request (~.ekm_service.GetEkmConnectionRequest):
                    The request object. Request message for
                [EkmService.GetEkmConnection][google.cloud.kms.v1.EkmService.GetEkmConnection].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ekm_service.EkmConnection:
                    An [EkmConnection][google.cloud.kms.v1.EkmConnection]
                represents an individual EKM connection. It can be used
                for creating [CryptoKeys][google.cloud.kms.v1.CryptoKey]
                and
                [CryptoKeyVersions][google.cloud.kms.v1.CryptoKeyVersion]
                with a
                [ProtectionLevel][google.cloud.kms.v1.ProtectionLevel]
                of
                [EXTERNAL_VPC][google.cloud.kms.v1.ProtectionLevel.EXTERNAL_VPC],
                as well as performing cryptographic operations using
                keys created within the
                [EkmConnection][google.cloud.kms.v1.EkmConnection].

            """

            http_options = (
                _BaseEkmServiceRestTransport._BaseGetEkmConnection._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_ekm_connection(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEkmServiceRestTransport._BaseGetEkmConnection,
                    "_BaseGetEkmConnection__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.EkmServiceClient.GetEkmConnection",
                    extra={
                        "serviceName": "google.cloud.kms.v1.EkmService",
                        "rpcName": "GetEkmConnection",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EkmServiceRestTransport._GetEkmConnection._get_response(
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
            resp = ekm_service.EkmConnection()
            pb_resp = ekm_service.EkmConnection.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_ekm_connection(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_ekm_connection_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = ekm_service.EkmConnection.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.kms_v1.EkmServiceClient.get_ekm_connection",
                    extra={
                        "serviceName": "google.cloud.kms.v1.EkmService",
                        "rpcName": "GetEkmConnection",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListEkmConnections(
        _BaseEkmServiceRestTransport._BaseListEkmConnections, EkmServiceRestStub
    ):
        def __hash__(self):
            return hash("EkmServiceRestTransport.ListEkmConnections")

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
            request: ekm_service.ListEkmConnectionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ekm_service.ListEkmConnectionsResponse:
            r"""Call the list ekm connections method over HTTP.

            Args:
                request (~.ekm_service.ListEkmConnectionsRequest):
                    The request object. Request message for
                [EkmService.ListEkmConnections][google.cloud.kms.v1.EkmService.ListEkmConnections].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ekm_service.ListEkmConnectionsResponse:
                    Response message for
                [EkmService.ListEkmConnections][google.cloud.kms.v1.EkmService.ListEkmConnections].

            """

            http_options = (
                _BaseEkmServiceRestTransport._BaseListEkmConnections._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_ekm_connections(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEkmServiceRestTransport._BaseListEkmConnections,
                    "_BaseListEkmConnections__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.EkmServiceClient.ListEkmConnections",
                    extra={
                        "serviceName": "google.cloud.kms.v1.EkmService",
                        "rpcName": "ListEkmConnections",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EkmServiceRestTransport._ListEkmConnections._get_response(
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
            resp = ekm_service.ListEkmConnectionsResponse()
            pb_resp = ekm_service.ListEkmConnectionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_ekm_connections(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_ekm_connections_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = ekm_service.ListEkmConnectionsResponse.to_json(
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
                    "Received response for google.cloud.kms_v1.EkmServiceClient.list_ekm_connections",
                    extra={
                        "serviceName": "google.cloud.kms.v1.EkmService",
                        "rpcName": "ListEkmConnections",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateEkmConfig(
        _BaseEkmServiceRestTransport._BaseUpdateEkmConfig, EkmServiceRestStub
    ):
        def __hash__(self):
            return hash("EkmServiceRestTransport.UpdateEkmConfig")

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
            request: ekm_service.UpdateEkmConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ekm_service.EkmConfig:
            r"""Call the update ekm config method over HTTP.

            Args:
                request (~.ekm_service.UpdateEkmConfigRequest):
                    The request object. Request message for
                [EkmService.UpdateEkmConfig][google.cloud.kms.v1.EkmService.UpdateEkmConfig].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ekm_service.EkmConfig:
                    An [EkmConfig][google.cloud.kms.v1.EkmConfig] is a
                singleton resource that represents configuration
                parameters that apply to all
                [CryptoKeys][google.cloud.kms.v1.CryptoKey] and
                [CryptoKeyVersions][google.cloud.kms.v1.CryptoKeyVersion]
                with a
                [ProtectionLevel][google.cloud.kms.v1.ProtectionLevel]
                of
                [EXTERNAL_VPC][google.cloud.kms.v1.ProtectionLevel.EXTERNAL_VPC]
                in a given project and location.

            """

            http_options = (
                _BaseEkmServiceRestTransport._BaseUpdateEkmConfig._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_ekm_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEkmServiceRestTransport._BaseUpdateEkmConfig,
                    "_BaseUpdateEkmConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.EkmServiceClient.UpdateEkmConfig",
                    extra={
                        "serviceName": "google.cloud.kms.v1.EkmService",
                        "rpcName": "UpdateEkmConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EkmServiceRestTransport._UpdateEkmConfig._get_response(
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
            resp = ekm_service.EkmConfig()
            pb_resp = ekm_service.EkmConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_ekm_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_ekm_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = ekm_service.EkmConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.kms_v1.EkmServiceClient.update_ekm_config",
                    extra={
                        "serviceName": "google.cloud.kms.v1.EkmService",
                        "rpcName": "UpdateEkmConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateEkmConnection(
        _BaseEkmServiceRestTransport._BaseUpdateEkmConnection, EkmServiceRestStub
    ):
        def __hash__(self):
            return hash("EkmServiceRestTransport.UpdateEkmConnection")

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
            request: ekm_service.UpdateEkmConnectionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ekm_service.EkmConnection:
            r"""Call the update ekm connection method over HTTP.

            Args:
                request (~.ekm_service.UpdateEkmConnectionRequest):
                    The request object. Request message for
                [EkmService.UpdateEkmConnection][google.cloud.kms.v1.EkmService.UpdateEkmConnection].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ekm_service.EkmConnection:
                    An [EkmConnection][google.cloud.kms.v1.EkmConnection]
                represents an individual EKM connection. It can be used
                for creating [CryptoKeys][google.cloud.kms.v1.CryptoKey]
                and
                [CryptoKeyVersions][google.cloud.kms.v1.CryptoKeyVersion]
                with a
                [ProtectionLevel][google.cloud.kms.v1.ProtectionLevel]
                of
                [EXTERNAL_VPC][google.cloud.kms.v1.ProtectionLevel.EXTERNAL_VPC],
                as well as performing cryptographic operations using
                keys created within the
                [EkmConnection][google.cloud.kms.v1.EkmConnection].

            """

            http_options = _BaseEkmServiceRestTransport._BaseUpdateEkmConnection._get_http_options()
            request, metadata = self._interceptor.pre_update_ekm_connection(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEkmServiceRestTransport._BaseUpdateEkmConnection,
                    "_BaseUpdateEkmConnection__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.EkmServiceClient.UpdateEkmConnection",
                    extra={
                        "serviceName": "google.cloud.kms.v1.EkmService",
                        "rpcName": "UpdateEkmConnection",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EkmServiceRestTransport._UpdateEkmConnection._get_response(
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
            resp = ekm_service.EkmConnection()
            pb_resp = ekm_service.EkmConnection.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_ekm_connection(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_ekm_connection_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = ekm_service.EkmConnection.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.kms_v1.EkmServiceClient.update_ekm_connection",
                    extra={
                        "serviceName": "google.cloud.kms.v1.EkmService",
                        "rpcName": "UpdateEkmConnection",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _VerifyConnectivity(
        _BaseEkmServiceRestTransport._BaseVerifyConnectivity, EkmServiceRestStub
    ):
        def __hash__(self):
            return hash("EkmServiceRestTransport.VerifyConnectivity")

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
            request: ekm_service.VerifyConnectivityRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ekm_service.VerifyConnectivityResponse:
            r"""Call the verify connectivity method over HTTP.

            Args:
                request (~.ekm_service.VerifyConnectivityRequest):
                    The request object. Request message for
                [EkmService.VerifyConnectivity][google.cloud.kms.v1.EkmService.VerifyConnectivity].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ekm_service.VerifyConnectivityResponse:
                    Response message for
                [EkmService.VerifyConnectivity][google.cloud.kms.v1.EkmService.VerifyConnectivity].

            """

            http_options = (
                _BaseEkmServiceRestTransport._BaseVerifyConnectivity._get_http_options()
            )
            request, metadata = self._interceptor.pre_verify_connectivity(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEkmServiceRestTransport._BaseVerifyConnectivity,
                    "_BaseVerifyConnectivity__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.EkmServiceClient.VerifyConnectivity",
                    extra={
                        "serviceName": "google.cloud.kms.v1.EkmService",
                        "rpcName": "VerifyConnectivity",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EkmServiceRestTransport._VerifyConnectivity._get_response(
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
            resp = ekm_service.VerifyConnectivityResponse()
            pb_resp = ekm_service.VerifyConnectivityResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_verify_connectivity(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_verify_connectivity_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = ekm_service.VerifyConnectivityResponse.to_json(
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
                    "Received response for google.cloud.kms_v1.EkmServiceClient.verify_connectivity",
                    extra={
                        "serviceName": "google.cloud.kms.v1.EkmService",
                        "rpcName": "VerifyConnectivity",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_ekm_connection(
        self,
    ) -> Callable[[ekm_service.CreateEkmConnectionRequest], ekm_service.EkmConnection]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateEkmConnection(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_ekm_config(
        self,
    ) -> Callable[[ekm_service.GetEkmConfigRequest], ekm_service.EkmConfig]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetEkmConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_ekm_connection(
        self,
    ) -> Callable[[ekm_service.GetEkmConnectionRequest], ekm_service.EkmConnection]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetEkmConnection(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_ekm_connections(
        self,
    ) -> Callable[
        [ekm_service.ListEkmConnectionsRequest], ekm_service.ListEkmConnectionsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListEkmConnections(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_ekm_config(
        self,
    ) -> Callable[[ekm_service.UpdateEkmConfigRequest], ekm_service.EkmConfig]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateEkmConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_ekm_connection(
        self,
    ) -> Callable[[ekm_service.UpdateEkmConnectionRequest], ekm_service.EkmConnection]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateEkmConnection(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def verify_connectivity(
        self,
    ) -> Callable[
        [ekm_service.VerifyConnectivityRequest], ekm_service.VerifyConnectivityResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._VerifyConnectivity(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseEkmServiceRestTransport._BaseGetLocation, EkmServiceRestStub
    ):
        def __hash__(self):
            return hash("EkmServiceRestTransport.GetLocation")

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
                _BaseEkmServiceRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEkmServiceRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.kms_v1.EkmServiceClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.kms.v1.EkmService",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EkmServiceRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.kms_v1.EkmServiceAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.kms.v1.EkmService",
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
        _BaseEkmServiceRestTransport._BaseListLocations, EkmServiceRestStub
    ):
        def __hash__(self):
            return hash("EkmServiceRestTransport.ListLocations")

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
                _BaseEkmServiceRestTransport._BaseListLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEkmServiceRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.kms_v1.EkmServiceClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.kms.v1.EkmService",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EkmServiceRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.kms_v1.EkmServiceAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.kms.v1.EkmService",
                        "rpcName": "ListLocations",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def get_iam_policy(self):
        return self._GetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    class _GetIamPolicy(
        _BaseEkmServiceRestTransport._BaseGetIamPolicy, EkmServiceRestStub
    ):
        def __hash__(self):
            return hash("EkmServiceRestTransport.GetIamPolicy")

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
            request: iam_policy_pb2.GetIamPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
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

            http_options = (
                _BaseEkmServiceRestTransport._BaseGetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEkmServiceRestTransport._BaseGetIamPolicy,
                    "_BaseGetIamPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.EkmServiceClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.kms.v1.EkmService",
                        "rpcName": "GetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EkmServiceRestTransport._GetIamPolicy._get_response(
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
            resp = policy_pb2.Policy()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_get_iam_policy(resp)
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
                    "Received response for google.cloud.kms_v1.EkmServiceAsyncClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.kms.v1.EkmService",
                        "rpcName": "GetIamPolicy",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def set_iam_policy(self):
        return self._SetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    class _SetIamPolicy(
        _BaseEkmServiceRestTransport._BaseSetIamPolicy, EkmServiceRestStub
    ):
        def __hash__(self):
            return hash("EkmServiceRestTransport.SetIamPolicy")

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
            request: iam_policy_pb2.SetIamPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
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

            http_options = (
                _BaseEkmServiceRestTransport._BaseSetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_set_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEkmServiceRestTransport._BaseSetIamPolicy,
                    "_BaseSetIamPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.EkmServiceClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.kms.v1.EkmService",
                        "rpcName": "SetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EkmServiceRestTransport._SetIamPolicy._get_response(
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

            content = response.content.decode("utf-8")
            resp = policy_pb2.Policy()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_set_iam_policy(resp)
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
                    "Received response for google.cloud.kms_v1.EkmServiceAsyncClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.kms.v1.EkmService",
                        "rpcName": "SetIamPolicy",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def test_iam_permissions(self):
        return self._TestIamPermissions(self._session, self._host, self._interceptor)  # type: ignore

    class _TestIamPermissions(
        _BaseEkmServiceRestTransport._BaseTestIamPermissions, EkmServiceRestStub
    ):
        def __hash__(self):
            return hash("EkmServiceRestTransport.TestIamPermissions")

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
            request: iam_policy_pb2.TestIamPermissionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
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

            http_options = (
                _BaseEkmServiceRestTransport._BaseTestIamPermissions._get_http_options()
            )
            request, metadata = self._interceptor.pre_test_iam_permissions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEkmServiceRestTransport._BaseTestIamPermissions,
                    "_BaseTestIamPermissions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.kms_v1.EkmServiceClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.kms.v1.EkmService",
                        "rpcName": "TestIamPermissions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EkmServiceRestTransport._TestIamPermissions._get_response(
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

            content = response.content.decode("utf-8")
            resp = iam_policy_pb2.TestIamPermissionsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_test_iam_permissions(resp)
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
                    "Received response for google.cloud.kms_v1.EkmServiceAsyncClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.kms.v1.EkmService",
                        "rpcName": "TestIamPermissions",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseEkmServiceRestTransport._BaseGetOperation, EkmServiceRestStub
    ):
        def __hash__(self):
            return hash("EkmServiceRestTransport.GetOperation")

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
                _BaseEkmServiceRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEkmServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.kms_v1.EkmServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.kms.v1.EkmService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EkmServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.kms_v1.EkmServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.kms.v1.EkmService",
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


__all__ = ("EkmServiceRestTransport",)
