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
import json
import logging as std_logging
import pickle
import warnings
from typing import Callable, Dict, Optional, Sequence, Tuple, Union

import google.auth  # type: ignore
import google.protobuf.message
import grpc  # type: ignore
import proto  # type: ignore
from google.api_core import gapic_v1, grpc_helpers, operations_v1
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf.json_format import MessageToJson

from google.cloud.network_services_v1.types import (
    agent_gateway,
    endpoint_policy,
    extensibility,
    gateway,
    grpc_route,
    http_route,
    mesh,
    route_view,
    service_binding,
    service_lb_policy,
    tcp_route,
    tls_route,
)
from google.cloud.network_services_v1.types import agent_gateway as gcn_agent_gateway
from google.cloud.network_services_v1.types import (
    endpoint_policy as gcn_endpoint_policy,
)
from google.cloud.network_services_v1.types import gateway as gcn_gateway
from google.cloud.network_services_v1.types import grpc_route as gcn_grpc_route
from google.cloud.network_services_v1.types import http_route as gcn_http_route
from google.cloud.network_services_v1.types import mesh as gcn_mesh
from google.cloud.network_services_v1.types import (
    service_binding as gcn_service_binding,
)
from google.cloud.network_services_v1.types import (
    service_lb_policy as gcn_service_lb_policy,
)
from google.cloud.network_services_v1.types import tcp_route as gcn_tcp_route
from google.cloud.network_services_v1.types import tls_route as gcn_tls_route

from .base import DEFAULT_CLIENT_INFO, NetworkServicesTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class _LoggingClientInterceptor(grpc.UnaryUnaryClientInterceptor):  # pragma: NO COVER
    def intercept_unary_unary(self, continuation, client_call_details, request):
        logging_enabled = CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        )
        if logging_enabled:  # pragma: NO COVER
            request_metadata = client_call_details.metadata
            if isinstance(request, proto.Message):
                request_payload = type(request).to_json(request)
            elif isinstance(request, google.protobuf.message.Message):
                request_payload = MessageToJson(request)
            else:
                request_payload = f"{type(request).__name__}: {pickle.dumps(request)!r}"

            request_metadata = {
                key: value.decode("utf-8") if isinstance(value, bytes) else value
                for key, value in request_metadata
            }
            grpc_request = {
                "payload": request_payload,
                "requestMethod": "grpc",
                "metadata": dict(request_metadata),
            }
            _LOGGER.debug(
                f"Sending request for {client_call_details.method}",
                extra={
                    "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                    "rpcName": str(client_call_details.method),
                    "request": grpc_request,
                    "metadata": grpc_request["metadata"],
                },
            )
        response = continuation(client_call_details, request)
        if logging_enabled:  # pragma: NO COVER
            response_metadata = response.trailing_metadata()
            # Convert gRPC metadata `<class 'grpc.aio._metadata.Metadata'>` to list of tuples
            metadata = (
                dict([(k, str(v)) for k, v in response_metadata])
                if response_metadata
                else None
            )
            result = response.result()
            if isinstance(result, proto.Message):
                response_payload = type(result).to_json(result)
            elif isinstance(result, google.protobuf.message.Message):
                response_payload = MessageToJson(result)
            else:
                response_payload = f"{type(result).__name__}: {pickle.dumps(result)!r}"
            grpc_response = {
                "payload": response_payload,
                "metadata": metadata,
                "status": "OK",
            }
            _LOGGER.debug(
                f"Received response for {client_call_details.method}.",
                extra={
                    "serviceName": "google.cloud.networkservices.v1.NetworkServices",
                    "rpcName": client_call_details.method,
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class NetworkServicesGrpcTransport(NetworkServicesTransport):
    """gRPC backend transport for NetworkServices.

    Service describing handlers for resources.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _stubs: Dict[str, Callable]

    def __init__(
        self,
        *,
        host: str = "networkservices.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        channel: Optional[Union[grpc.Channel, Callable[..., grpc.Channel]]] = None,
        api_mtls_endpoint: Optional[str] = None,
        client_cert_source: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        ssl_channel_credentials: Optional[grpc.ChannelCredentials] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'networkservices.googleapis.com').
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if a ``channel`` instance is provided.
            credentials_file (Optional[str]): Deprecated. A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if a ``channel`` instance is provided.
                This argument will be removed in the next major version of this library.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if a ``channel`` instance is provided.
            channel (Optional[Union[grpc.Channel, Callable[..., grpc.Channel]]]):
                A ``Channel`` instance through which to make calls, or a Callable
                that constructs and returns one. If set to None, ``self.create_channel``
                is used to create the channel. If a Callable is given, it will be called
                with the same arguments as used in ``self.create_channel``.
            api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                If provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or application default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                Deprecated. A callback to provide client SSL certificate bytes and
                private key bytes, both in PEM format. It is ignored if
                ``api_mtls_endpoint`` is None.
            ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
                for the grpc channel. It is ignored if a ``channel`` instance is provided.
            client_cert_source_for_mtls (Optional[Callable[[], Tuple[bytes, bytes]]]):
                A callback to provide client certificate bytes and private key bytes,
                both in PEM format. It is used to configure a mutual TLS channel. It is
                ignored if a ``channel`` instance or ``ssl_channel_credentials`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
            api_audience (Optional[str]): The intended audience for the API calls
                to the service that will be set when using certain 3rd party
                authentication flows. Audience is typically a resource identifier.
                If not set, the host value will be used as a default.

        Raises:
          google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        self._grpc_channel = None
        self._ssl_channel_credentials = ssl_channel_credentials
        self._stubs: Dict[str, Callable] = {}
        self._operations_client: Optional[operations_v1.OperationsClient] = None

        if api_mtls_endpoint:
            warnings.warn("api_mtls_endpoint is deprecated", DeprecationWarning)
        if client_cert_source:
            warnings.warn("client_cert_source is deprecated", DeprecationWarning)

        if isinstance(channel, grpc.Channel):
            # Ignore credentials if a channel was passed.
            credentials = None
            self._ignore_credentials = True
            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
            self._ssl_channel_credentials = None

        else:
            if api_mtls_endpoint:
                host = api_mtls_endpoint

                # Create SSL credentials with client_cert_source or application
                # default SSL credentials.
                if client_cert_source:
                    cert, key = client_cert_source()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )
                else:
                    self._ssl_channel_credentials = SslCredentials().ssl_credentials

            else:
                if client_cert_source_for_mtls and not ssl_channel_credentials:
                    cert, key = client_cert_source_for_mtls()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )

        # The base transport sets the host, credentials and scopes
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            api_audience=api_audience,
        )

        if not self._grpc_channel:
            # initialize with the provided callable or the default channel
            channel_init = channel or type(self).create_channel
            self._grpc_channel = channel_init(
                self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                # Set ``credentials_file`` to ``None`` here as
                # the credentials that we saved earlier should be used.
                credentials_file=None,
                scopes=self._scopes,
                ssl_credentials=self._ssl_channel_credentials,
                quota_project_id=quota_project_id,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )

        self._interceptor = _LoggingClientInterceptor()
        self._logged_channel = grpc.intercept_channel(
            self._grpc_channel, self._interceptor
        )

        # Wrap messages. This must be done after self._logged_channel exists
        self._prep_wrapped_messages(client_info)

    @classmethod
    def create_channel(
        cls,
        host: str = "networkservices.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        **kwargs,
    ) -> grpc.Channel:
        """Create and return a gRPC channel object.
        Args:
            host (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): Deprecated. A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.  This argument will be
                removed in the next major version of this library.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            grpc.Channel: A gRPC channel object.

        Raises:
            google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """

        return grpc_helpers.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            quota_project_id=quota_project_id,
            default_scopes=cls.AUTH_SCOPES,
            scopes=scopes,
            default_host=cls.DEFAULT_HOST,
            **kwargs,
        )

    @property
    def grpc_channel(self) -> grpc.Channel:
        """Return the channel designed to connect to this service."""
        return self._grpc_channel

    @property
    def operations_client(self) -> operations_v1.OperationsClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Quick check: Only create a new client if we do not already have one.
        if self._operations_client is None:
            self._operations_client = operations_v1.OperationsClient(
                self._logged_channel
            )

        # Return the client from cache.
        return self._operations_client

    @property
    def list_endpoint_policies(
        self,
    ) -> Callable[
        [endpoint_policy.ListEndpointPoliciesRequest],
        endpoint_policy.ListEndpointPoliciesResponse,
    ]:
        r"""Return a callable for the list endpoint policies method over gRPC.

        Lists EndpointPolicies in a given project and
        location.

        Returns:
            Callable[[~.ListEndpointPoliciesRequest],
                    ~.ListEndpointPoliciesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_endpoint_policies" not in self._stubs:
            self._stubs["list_endpoint_policies"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/ListEndpointPolicies",
                request_serializer=endpoint_policy.ListEndpointPoliciesRequest.serialize,
                response_deserializer=endpoint_policy.ListEndpointPoliciesResponse.deserialize,
            )
        return self._stubs["list_endpoint_policies"]

    @property
    def get_endpoint_policy(
        self,
    ) -> Callable[
        [endpoint_policy.GetEndpointPolicyRequest], endpoint_policy.EndpointPolicy
    ]:
        r"""Return a callable for the get endpoint policy method over gRPC.

        Gets details of a single EndpointPolicy.

        Returns:
            Callable[[~.GetEndpointPolicyRequest],
                    ~.EndpointPolicy]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_endpoint_policy" not in self._stubs:
            self._stubs["get_endpoint_policy"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/GetEndpointPolicy",
                request_serializer=endpoint_policy.GetEndpointPolicyRequest.serialize,
                response_deserializer=endpoint_policy.EndpointPolicy.deserialize,
            )
        return self._stubs["get_endpoint_policy"]

    @property
    def create_endpoint_policy(
        self,
    ) -> Callable[
        [gcn_endpoint_policy.CreateEndpointPolicyRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the create endpoint policy method over gRPC.

        Creates a new EndpointPolicy in a given project and
        location.

        Returns:
            Callable[[~.CreateEndpointPolicyRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_endpoint_policy" not in self._stubs:
            self._stubs["create_endpoint_policy"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/CreateEndpointPolicy",
                request_serializer=gcn_endpoint_policy.CreateEndpointPolicyRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_endpoint_policy"]

    @property
    def update_endpoint_policy(
        self,
    ) -> Callable[
        [gcn_endpoint_policy.UpdateEndpointPolicyRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the update endpoint policy method over gRPC.

        Updates the parameters of a single EndpointPolicy.

        Returns:
            Callable[[~.UpdateEndpointPolicyRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_endpoint_policy" not in self._stubs:
            self._stubs["update_endpoint_policy"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/UpdateEndpointPolicy",
                request_serializer=gcn_endpoint_policy.UpdateEndpointPolicyRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_endpoint_policy"]

    @property
    def delete_endpoint_policy(
        self,
    ) -> Callable[
        [endpoint_policy.DeleteEndpointPolicyRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the delete endpoint policy method over gRPC.

        Deletes a single EndpointPolicy.

        Returns:
            Callable[[~.DeleteEndpointPolicyRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_endpoint_policy" not in self._stubs:
            self._stubs["delete_endpoint_policy"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/DeleteEndpointPolicy",
                request_serializer=endpoint_policy.DeleteEndpointPolicyRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_endpoint_policy"]

    @property
    def list_wasm_plugin_versions(
        self,
    ) -> Callable[
        [extensibility.ListWasmPluginVersionsRequest],
        extensibility.ListWasmPluginVersionsResponse,
    ]:
        r"""Return a callable for the list wasm plugin versions method over gRPC.

        Lists ``WasmPluginVersion`` resources in a given project and
        location.

        Returns:
            Callable[[~.ListWasmPluginVersionsRequest],
                    ~.ListWasmPluginVersionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_wasm_plugin_versions" not in self._stubs:
            self._stubs["list_wasm_plugin_versions"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/ListWasmPluginVersions",
                request_serializer=extensibility.ListWasmPluginVersionsRequest.serialize,
                response_deserializer=extensibility.ListWasmPluginVersionsResponse.deserialize,
            )
        return self._stubs["list_wasm_plugin_versions"]

    @property
    def get_wasm_plugin_version(
        self,
    ) -> Callable[
        [extensibility.GetWasmPluginVersionRequest], extensibility.WasmPluginVersion
    ]:
        r"""Return a callable for the get wasm plugin version method over gRPC.

        Gets details of the specified ``WasmPluginVersion`` resource.

        Returns:
            Callable[[~.GetWasmPluginVersionRequest],
                    ~.WasmPluginVersion]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_wasm_plugin_version" not in self._stubs:
            self._stubs["get_wasm_plugin_version"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/GetWasmPluginVersion",
                request_serializer=extensibility.GetWasmPluginVersionRequest.serialize,
                response_deserializer=extensibility.WasmPluginVersion.deserialize,
            )
        return self._stubs["get_wasm_plugin_version"]

    @property
    def create_wasm_plugin_version(
        self,
    ) -> Callable[
        [extensibility.CreateWasmPluginVersionRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the create wasm plugin version method over gRPC.

        Creates a new ``WasmPluginVersion`` resource in a given project
        and location.

        Returns:
            Callable[[~.CreateWasmPluginVersionRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_wasm_plugin_version" not in self._stubs:
            self._stubs["create_wasm_plugin_version"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.networkservices.v1.NetworkServices/CreateWasmPluginVersion",
                    request_serializer=extensibility.CreateWasmPluginVersionRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["create_wasm_plugin_version"]

    @property
    def delete_wasm_plugin_version(
        self,
    ) -> Callable[
        [extensibility.DeleteWasmPluginVersionRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the delete wasm plugin version method over gRPC.

        Deletes the specified ``WasmPluginVersion`` resource.

        Returns:
            Callable[[~.DeleteWasmPluginVersionRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_wasm_plugin_version" not in self._stubs:
            self._stubs["delete_wasm_plugin_version"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.networkservices.v1.NetworkServices/DeleteWasmPluginVersion",
                    request_serializer=extensibility.DeleteWasmPluginVersionRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["delete_wasm_plugin_version"]

    @property
    def list_wasm_plugins(
        self,
    ) -> Callable[
        [extensibility.ListWasmPluginsRequest], extensibility.ListWasmPluginsResponse
    ]:
        r"""Return a callable for the list wasm plugins method over gRPC.

        Lists ``WasmPlugin`` resources in a given project and location.

        Returns:
            Callable[[~.ListWasmPluginsRequest],
                    ~.ListWasmPluginsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_wasm_plugins" not in self._stubs:
            self._stubs["list_wasm_plugins"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/ListWasmPlugins",
                request_serializer=extensibility.ListWasmPluginsRequest.serialize,
                response_deserializer=extensibility.ListWasmPluginsResponse.deserialize,
            )
        return self._stubs["list_wasm_plugins"]

    @property
    def get_wasm_plugin(
        self,
    ) -> Callable[[extensibility.GetWasmPluginRequest], extensibility.WasmPlugin]:
        r"""Return a callable for the get wasm plugin method over gRPC.

        Gets details of the specified ``WasmPlugin`` resource.

        Returns:
            Callable[[~.GetWasmPluginRequest],
                    ~.WasmPlugin]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_wasm_plugin" not in self._stubs:
            self._stubs["get_wasm_plugin"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/GetWasmPlugin",
                request_serializer=extensibility.GetWasmPluginRequest.serialize,
                response_deserializer=extensibility.WasmPlugin.deserialize,
            )
        return self._stubs["get_wasm_plugin"]

    @property
    def create_wasm_plugin(
        self,
    ) -> Callable[[extensibility.CreateWasmPluginRequest], operations_pb2.Operation]:
        r"""Return a callable for the create wasm plugin method over gRPC.

        Creates a new ``WasmPlugin`` resource in a given project and
        location.

        Returns:
            Callable[[~.CreateWasmPluginRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_wasm_plugin" not in self._stubs:
            self._stubs["create_wasm_plugin"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/CreateWasmPlugin",
                request_serializer=extensibility.CreateWasmPluginRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_wasm_plugin"]

    @property
    def update_wasm_plugin(
        self,
    ) -> Callable[[extensibility.UpdateWasmPluginRequest], operations_pb2.Operation]:
        r"""Return a callable for the update wasm plugin method over gRPC.

        Updates the parameters of the specified ``WasmPlugin`` resource.

        Returns:
            Callable[[~.UpdateWasmPluginRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_wasm_plugin" not in self._stubs:
            self._stubs["update_wasm_plugin"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/UpdateWasmPlugin",
                request_serializer=extensibility.UpdateWasmPluginRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_wasm_plugin"]

    @property
    def delete_wasm_plugin(
        self,
    ) -> Callable[[extensibility.DeleteWasmPluginRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete wasm plugin method over gRPC.

        Deletes the specified ``WasmPlugin`` resource.

        Returns:
            Callable[[~.DeleteWasmPluginRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_wasm_plugin" not in self._stubs:
            self._stubs["delete_wasm_plugin"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/DeleteWasmPlugin",
                request_serializer=extensibility.DeleteWasmPluginRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_wasm_plugin"]

    @property
    def list_gateways(
        self,
    ) -> Callable[[gateway.ListGatewaysRequest], gateway.ListGatewaysResponse]:
        r"""Return a callable for the list gateways method over gRPC.

        Lists Gateways in a given project and location.

        Returns:
            Callable[[~.ListGatewaysRequest],
                    ~.ListGatewaysResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_gateways" not in self._stubs:
            self._stubs["list_gateways"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/ListGateways",
                request_serializer=gateway.ListGatewaysRequest.serialize,
                response_deserializer=gateway.ListGatewaysResponse.deserialize,
            )
        return self._stubs["list_gateways"]

    @property
    def get_gateway(self) -> Callable[[gateway.GetGatewayRequest], gateway.Gateway]:
        r"""Return a callable for the get gateway method over gRPC.

        Gets details of a single Gateway.

        Returns:
            Callable[[~.GetGatewayRequest],
                    ~.Gateway]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_gateway" not in self._stubs:
            self._stubs["get_gateway"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/GetGateway",
                request_serializer=gateway.GetGatewayRequest.serialize,
                response_deserializer=gateway.Gateway.deserialize,
            )
        return self._stubs["get_gateway"]

    @property
    def create_gateway(
        self,
    ) -> Callable[[gcn_gateway.CreateGatewayRequest], operations_pb2.Operation]:
        r"""Return a callable for the create gateway method over gRPC.

        Creates a new Gateway in a given project and
        location.

        Returns:
            Callable[[~.CreateGatewayRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_gateway" not in self._stubs:
            self._stubs["create_gateway"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/CreateGateway",
                request_serializer=gcn_gateway.CreateGatewayRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_gateway"]

    @property
    def update_gateway(
        self,
    ) -> Callable[[gcn_gateway.UpdateGatewayRequest], operations_pb2.Operation]:
        r"""Return a callable for the update gateway method over gRPC.

        Updates the parameters of a single Gateway.

        Returns:
            Callable[[~.UpdateGatewayRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_gateway" not in self._stubs:
            self._stubs["update_gateway"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/UpdateGateway",
                request_serializer=gcn_gateway.UpdateGatewayRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_gateway"]

    @property
    def delete_gateway(
        self,
    ) -> Callable[[gateway.DeleteGatewayRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete gateway method over gRPC.

        Deletes a single Gateway.

        Returns:
            Callable[[~.DeleteGatewayRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_gateway" not in self._stubs:
            self._stubs["delete_gateway"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/DeleteGateway",
                request_serializer=gateway.DeleteGatewayRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_gateway"]

    @property
    def list_grpc_routes(
        self,
    ) -> Callable[
        [grpc_route.ListGrpcRoutesRequest], grpc_route.ListGrpcRoutesResponse
    ]:
        r"""Return a callable for the list grpc routes method over gRPC.

        Lists GrpcRoutes in a given project and location.

        Returns:
            Callable[[~.ListGrpcRoutesRequest],
                    ~.ListGrpcRoutesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_grpc_routes" not in self._stubs:
            self._stubs["list_grpc_routes"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/ListGrpcRoutes",
                request_serializer=grpc_route.ListGrpcRoutesRequest.serialize,
                response_deserializer=grpc_route.ListGrpcRoutesResponse.deserialize,
            )
        return self._stubs["list_grpc_routes"]

    @property
    def get_grpc_route(
        self,
    ) -> Callable[[grpc_route.GetGrpcRouteRequest], grpc_route.GrpcRoute]:
        r"""Return a callable for the get grpc route method over gRPC.

        Gets details of a single GrpcRoute.

        Returns:
            Callable[[~.GetGrpcRouteRequest],
                    ~.GrpcRoute]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_grpc_route" not in self._stubs:
            self._stubs["get_grpc_route"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/GetGrpcRoute",
                request_serializer=grpc_route.GetGrpcRouteRequest.serialize,
                response_deserializer=grpc_route.GrpcRoute.deserialize,
            )
        return self._stubs["get_grpc_route"]

    @property
    def create_grpc_route(
        self,
    ) -> Callable[[gcn_grpc_route.CreateGrpcRouteRequest], operations_pb2.Operation]:
        r"""Return a callable for the create grpc route method over gRPC.

        Creates a new GrpcRoute in a given project and
        location.

        Returns:
            Callable[[~.CreateGrpcRouteRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_grpc_route" not in self._stubs:
            self._stubs["create_grpc_route"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/CreateGrpcRoute",
                request_serializer=gcn_grpc_route.CreateGrpcRouteRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_grpc_route"]

    @property
    def update_grpc_route(
        self,
    ) -> Callable[[gcn_grpc_route.UpdateGrpcRouteRequest], operations_pb2.Operation]:
        r"""Return a callable for the update grpc route method over gRPC.

        Updates the parameters of a single GrpcRoute.

        Returns:
            Callable[[~.UpdateGrpcRouteRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_grpc_route" not in self._stubs:
            self._stubs["update_grpc_route"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/UpdateGrpcRoute",
                request_serializer=gcn_grpc_route.UpdateGrpcRouteRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_grpc_route"]

    @property
    def delete_grpc_route(
        self,
    ) -> Callable[[grpc_route.DeleteGrpcRouteRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete grpc route method over gRPC.

        Deletes a single GrpcRoute.

        Returns:
            Callable[[~.DeleteGrpcRouteRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_grpc_route" not in self._stubs:
            self._stubs["delete_grpc_route"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/DeleteGrpcRoute",
                request_serializer=grpc_route.DeleteGrpcRouteRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_grpc_route"]

    @property
    def list_http_routes(
        self,
    ) -> Callable[
        [http_route.ListHttpRoutesRequest], http_route.ListHttpRoutesResponse
    ]:
        r"""Return a callable for the list http routes method over gRPC.

        Lists HttpRoute in a given project and location.

        Returns:
            Callable[[~.ListHttpRoutesRequest],
                    ~.ListHttpRoutesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_http_routes" not in self._stubs:
            self._stubs["list_http_routes"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/ListHttpRoutes",
                request_serializer=http_route.ListHttpRoutesRequest.serialize,
                response_deserializer=http_route.ListHttpRoutesResponse.deserialize,
            )
        return self._stubs["list_http_routes"]

    @property
    def get_http_route(
        self,
    ) -> Callable[[http_route.GetHttpRouteRequest], http_route.HttpRoute]:
        r"""Return a callable for the get http route method over gRPC.

        Gets details of a single HttpRoute.

        Returns:
            Callable[[~.GetHttpRouteRequest],
                    ~.HttpRoute]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_http_route" not in self._stubs:
            self._stubs["get_http_route"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/GetHttpRoute",
                request_serializer=http_route.GetHttpRouteRequest.serialize,
                response_deserializer=http_route.HttpRoute.deserialize,
            )
        return self._stubs["get_http_route"]

    @property
    def create_http_route(
        self,
    ) -> Callable[[gcn_http_route.CreateHttpRouteRequest], operations_pb2.Operation]:
        r"""Return a callable for the create http route method over gRPC.

        Creates a new HttpRoute in a given project and
        location.

        Returns:
            Callable[[~.CreateHttpRouteRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_http_route" not in self._stubs:
            self._stubs["create_http_route"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/CreateHttpRoute",
                request_serializer=gcn_http_route.CreateHttpRouteRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_http_route"]

    @property
    def update_http_route(
        self,
    ) -> Callable[[gcn_http_route.UpdateHttpRouteRequest], operations_pb2.Operation]:
        r"""Return a callable for the update http route method over gRPC.

        Updates the parameters of a single HttpRoute.

        Returns:
            Callable[[~.UpdateHttpRouteRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_http_route" not in self._stubs:
            self._stubs["update_http_route"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/UpdateHttpRoute",
                request_serializer=gcn_http_route.UpdateHttpRouteRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_http_route"]

    @property
    def delete_http_route(
        self,
    ) -> Callable[[http_route.DeleteHttpRouteRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete http route method over gRPC.

        Deletes a single HttpRoute.

        Returns:
            Callable[[~.DeleteHttpRouteRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_http_route" not in self._stubs:
            self._stubs["delete_http_route"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/DeleteHttpRoute",
                request_serializer=http_route.DeleteHttpRouteRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_http_route"]

    @property
    def list_tcp_routes(
        self,
    ) -> Callable[[tcp_route.ListTcpRoutesRequest], tcp_route.ListTcpRoutesResponse]:
        r"""Return a callable for the list tcp routes method over gRPC.

        Lists TcpRoute in a given project and location.

        Returns:
            Callable[[~.ListTcpRoutesRequest],
                    ~.ListTcpRoutesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_tcp_routes" not in self._stubs:
            self._stubs["list_tcp_routes"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/ListTcpRoutes",
                request_serializer=tcp_route.ListTcpRoutesRequest.serialize,
                response_deserializer=tcp_route.ListTcpRoutesResponse.deserialize,
            )
        return self._stubs["list_tcp_routes"]

    @property
    def get_tcp_route(
        self,
    ) -> Callable[[tcp_route.GetTcpRouteRequest], tcp_route.TcpRoute]:
        r"""Return a callable for the get tcp route method over gRPC.

        Gets details of a single TcpRoute.

        Returns:
            Callable[[~.GetTcpRouteRequest],
                    ~.TcpRoute]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_tcp_route" not in self._stubs:
            self._stubs["get_tcp_route"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/GetTcpRoute",
                request_serializer=tcp_route.GetTcpRouteRequest.serialize,
                response_deserializer=tcp_route.TcpRoute.deserialize,
            )
        return self._stubs["get_tcp_route"]

    @property
    def create_tcp_route(
        self,
    ) -> Callable[[gcn_tcp_route.CreateTcpRouteRequest], operations_pb2.Operation]:
        r"""Return a callable for the create tcp route method over gRPC.

        Creates a new TcpRoute in a given project and
        location.

        Returns:
            Callable[[~.CreateTcpRouteRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_tcp_route" not in self._stubs:
            self._stubs["create_tcp_route"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/CreateTcpRoute",
                request_serializer=gcn_tcp_route.CreateTcpRouteRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_tcp_route"]

    @property
    def update_tcp_route(
        self,
    ) -> Callable[[gcn_tcp_route.UpdateTcpRouteRequest], operations_pb2.Operation]:
        r"""Return a callable for the update tcp route method over gRPC.

        Updates the parameters of a single TcpRoute.

        Returns:
            Callable[[~.UpdateTcpRouteRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_tcp_route" not in self._stubs:
            self._stubs["update_tcp_route"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/UpdateTcpRoute",
                request_serializer=gcn_tcp_route.UpdateTcpRouteRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_tcp_route"]

    @property
    def delete_tcp_route(
        self,
    ) -> Callable[[tcp_route.DeleteTcpRouteRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete tcp route method over gRPC.

        Deletes a single TcpRoute.

        Returns:
            Callable[[~.DeleteTcpRouteRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_tcp_route" not in self._stubs:
            self._stubs["delete_tcp_route"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/DeleteTcpRoute",
                request_serializer=tcp_route.DeleteTcpRouteRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_tcp_route"]

    @property
    def list_tls_routes(
        self,
    ) -> Callable[[tls_route.ListTlsRoutesRequest], tls_route.ListTlsRoutesResponse]:
        r"""Return a callable for the list tls routes method over gRPC.

        Lists TlsRoute in a given project and location.

        Returns:
            Callable[[~.ListTlsRoutesRequest],
                    ~.ListTlsRoutesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_tls_routes" not in self._stubs:
            self._stubs["list_tls_routes"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/ListTlsRoutes",
                request_serializer=tls_route.ListTlsRoutesRequest.serialize,
                response_deserializer=tls_route.ListTlsRoutesResponse.deserialize,
            )
        return self._stubs["list_tls_routes"]

    @property
    def get_tls_route(
        self,
    ) -> Callable[[tls_route.GetTlsRouteRequest], tls_route.TlsRoute]:
        r"""Return a callable for the get tls route method over gRPC.

        Gets details of a single TlsRoute.

        Returns:
            Callable[[~.GetTlsRouteRequest],
                    ~.TlsRoute]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_tls_route" not in self._stubs:
            self._stubs["get_tls_route"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/GetTlsRoute",
                request_serializer=tls_route.GetTlsRouteRequest.serialize,
                response_deserializer=tls_route.TlsRoute.deserialize,
            )
        return self._stubs["get_tls_route"]

    @property
    def create_tls_route(
        self,
    ) -> Callable[[gcn_tls_route.CreateTlsRouteRequest], operations_pb2.Operation]:
        r"""Return a callable for the create tls route method over gRPC.

        Creates a new TlsRoute in a given project and
        location.

        Returns:
            Callable[[~.CreateTlsRouteRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_tls_route" not in self._stubs:
            self._stubs["create_tls_route"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/CreateTlsRoute",
                request_serializer=gcn_tls_route.CreateTlsRouteRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_tls_route"]

    @property
    def update_tls_route(
        self,
    ) -> Callable[[gcn_tls_route.UpdateTlsRouteRequest], operations_pb2.Operation]:
        r"""Return a callable for the update tls route method over gRPC.

        Updates the parameters of a single TlsRoute.

        Returns:
            Callable[[~.UpdateTlsRouteRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_tls_route" not in self._stubs:
            self._stubs["update_tls_route"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/UpdateTlsRoute",
                request_serializer=gcn_tls_route.UpdateTlsRouteRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_tls_route"]

    @property
    def delete_tls_route(
        self,
    ) -> Callable[[tls_route.DeleteTlsRouteRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete tls route method over gRPC.

        Deletes a single TlsRoute.

        Returns:
            Callable[[~.DeleteTlsRouteRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_tls_route" not in self._stubs:
            self._stubs["delete_tls_route"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/DeleteTlsRoute",
                request_serializer=tls_route.DeleteTlsRouteRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_tls_route"]

    @property
    def list_service_bindings(
        self,
    ) -> Callable[
        [service_binding.ListServiceBindingsRequest],
        service_binding.ListServiceBindingsResponse,
    ]:
        r"""Return a callable for the list service bindings method over gRPC.

        Lists ServiceBinding in a given project and location.

        Returns:
            Callable[[~.ListServiceBindingsRequest],
                    ~.ListServiceBindingsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_service_bindings" not in self._stubs:
            self._stubs["list_service_bindings"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/ListServiceBindings",
                request_serializer=service_binding.ListServiceBindingsRequest.serialize,
                response_deserializer=service_binding.ListServiceBindingsResponse.deserialize,
            )
        return self._stubs["list_service_bindings"]

    @property
    def get_service_binding(
        self,
    ) -> Callable[
        [service_binding.GetServiceBindingRequest], service_binding.ServiceBinding
    ]:
        r"""Return a callable for the get service binding method over gRPC.

        Gets details of a single ServiceBinding.

        Returns:
            Callable[[~.GetServiceBindingRequest],
                    ~.ServiceBinding]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_service_binding" not in self._stubs:
            self._stubs["get_service_binding"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/GetServiceBinding",
                request_serializer=service_binding.GetServiceBindingRequest.serialize,
                response_deserializer=service_binding.ServiceBinding.deserialize,
            )
        return self._stubs["get_service_binding"]

    @property
    def create_service_binding(
        self,
    ) -> Callable[
        [gcn_service_binding.CreateServiceBindingRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the create service binding method over gRPC.

        Creates a new ServiceBinding in a given project and
        location.

        Returns:
            Callable[[~.CreateServiceBindingRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_service_binding" not in self._stubs:
            self._stubs["create_service_binding"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/CreateServiceBinding",
                request_serializer=gcn_service_binding.CreateServiceBindingRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_service_binding"]

    @property
    def update_service_binding(
        self,
    ) -> Callable[
        [gcn_service_binding.UpdateServiceBindingRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the update service binding method over gRPC.

        Updates the parameters of a single ServiceBinding.

        Returns:
            Callable[[~.UpdateServiceBindingRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_service_binding" not in self._stubs:
            self._stubs["update_service_binding"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/UpdateServiceBinding",
                request_serializer=gcn_service_binding.UpdateServiceBindingRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_service_binding"]

    @property
    def delete_service_binding(
        self,
    ) -> Callable[
        [service_binding.DeleteServiceBindingRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the delete service binding method over gRPC.

        Deletes a single ServiceBinding.

        Returns:
            Callable[[~.DeleteServiceBindingRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_service_binding" not in self._stubs:
            self._stubs["delete_service_binding"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/DeleteServiceBinding",
                request_serializer=service_binding.DeleteServiceBindingRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_service_binding"]

    @property
    def list_meshes(
        self,
    ) -> Callable[[mesh.ListMeshesRequest], mesh.ListMeshesResponse]:
        r"""Return a callable for the list meshes method over gRPC.

        Lists Meshes in a given project and location.

        Returns:
            Callable[[~.ListMeshesRequest],
                    ~.ListMeshesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_meshes" not in self._stubs:
            self._stubs["list_meshes"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/ListMeshes",
                request_serializer=mesh.ListMeshesRequest.serialize,
                response_deserializer=mesh.ListMeshesResponse.deserialize,
            )
        return self._stubs["list_meshes"]

    @property
    def get_mesh(self) -> Callable[[mesh.GetMeshRequest], mesh.Mesh]:
        r"""Return a callable for the get mesh method over gRPC.

        Gets details of a single Mesh.

        Returns:
            Callable[[~.GetMeshRequest],
                    ~.Mesh]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_mesh" not in self._stubs:
            self._stubs["get_mesh"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/GetMesh",
                request_serializer=mesh.GetMeshRequest.serialize,
                response_deserializer=mesh.Mesh.deserialize,
            )
        return self._stubs["get_mesh"]

    @property
    def create_mesh(
        self,
    ) -> Callable[[gcn_mesh.CreateMeshRequest], operations_pb2.Operation]:
        r"""Return a callable for the create mesh method over gRPC.

        Creates a new Mesh in a given project and location.

        Returns:
            Callable[[~.CreateMeshRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_mesh" not in self._stubs:
            self._stubs["create_mesh"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/CreateMesh",
                request_serializer=gcn_mesh.CreateMeshRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_mesh"]

    @property
    def update_mesh(
        self,
    ) -> Callable[[gcn_mesh.UpdateMeshRequest], operations_pb2.Operation]:
        r"""Return a callable for the update mesh method over gRPC.

        Updates the parameters of a single Mesh.

        Returns:
            Callable[[~.UpdateMeshRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_mesh" not in self._stubs:
            self._stubs["update_mesh"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/UpdateMesh",
                request_serializer=gcn_mesh.UpdateMeshRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_mesh"]

    @property
    def delete_mesh(
        self,
    ) -> Callable[[mesh.DeleteMeshRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete mesh method over gRPC.

        Deletes a single Mesh.

        Returns:
            Callable[[~.DeleteMeshRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_mesh" not in self._stubs:
            self._stubs["delete_mesh"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/DeleteMesh",
                request_serializer=mesh.DeleteMeshRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_mesh"]

    @property
    def list_service_lb_policies(
        self,
    ) -> Callable[
        [service_lb_policy.ListServiceLbPoliciesRequest],
        service_lb_policy.ListServiceLbPoliciesResponse,
    ]:
        r"""Return a callable for the list service lb policies method over gRPC.

        Lists ServiceLbPolicies in a given project and
        location.

        Returns:
            Callable[[~.ListServiceLbPoliciesRequest],
                    ~.ListServiceLbPoliciesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_service_lb_policies" not in self._stubs:
            self._stubs["list_service_lb_policies"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/ListServiceLbPolicies",
                request_serializer=service_lb_policy.ListServiceLbPoliciesRequest.serialize,
                response_deserializer=service_lb_policy.ListServiceLbPoliciesResponse.deserialize,
            )
        return self._stubs["list_service_lb_policies"]

    @property
    def get_service_lb_policy(
        self,
    ) -> Callable[
        [service_lb_policy.GetServiceLbPolicyRequest], service_lb_policy.ServiceLbPolicy
    ]:
        r"""Return a callable for the get service lb policy method over gRPC.

        Gets details of a single ServiceLbPolicy.

        Returns:
            Callable[[~.GetServiceLbPolicyRequest],
                    ~.ServiceLbPolicy]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_service_lb_policy" not in self._stubs:
            self._stubs["get_service_lb_policy"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/GetServiceLbPolicy",
                request_serializer=service_lb_policy.GetServiceLbPolicyRequest.serialize,
                response_deserializer=service_lb_policy.ServiceLbPolicy.deserialize,
            )
        return self._stubs["get_service_lb_policy"]

    @property
    def create_service_lb_policy(
        self,
    ) -> Callable[
        [gcn_service_lb_policy.CreateServiceLbPolicyRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the create service lb policy method over gRPC.

        Creates a new ServiceLbPolicy in a given project and
        location.

        Returns:
            Callable[[~.CreateServiceLbPolicyRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_service_lb_policy" not in self._stubs:
            self._stubs["create_service_lb_policy"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/CreateServiceLbPolicy",
                request_serializer=gcn_service_lb_policy.CreateServiceLbPolicyRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_service_lb_policy"]

    @property
    def update_service_lb_policy(
        self,
    ) -> Callable[
        [gcn_service_lb_policy.UpdateServiceLbPolicyRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the update service lb policy method over gRPC.

        Updates the parameters of a single ServiceLbPolicy.

        Returns:
            Callable[[~.UpdateServiceLbPolicyRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_service_lb_policy" not in self._stubs:
            self._stubs["update_service_lb_policy"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/UpdateServiceLbPolicy",
                request_serializer=gcn_service_lb_policy.UpdateServiceLbPolicyRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_service_lb_policy"]

    @property
    def delete_service_lb_policy(
        self,
    ) -> Callable[
        [service_lb_policy.DeleteServiceLbPolicyRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the delete service lb policy method over gRPC.

        Deletes a single ServiceLbPolicy.

        Returns:
            Callable[[~.DeleteServiceLbPolicyRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_service_lb_policy" not in self._stubs:
            self._stubs["delete_service_lb_policy"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/DeleteServiceLbPolicy",
                request_serializer=service_lb_policy.DeleteServiceLbPolicyRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_service_lb_policy"]

    @property
    def get_gateway_route_view(
        self,
    ) -> Callable[[route_view.GetGatewayRouteViewRequest], route_view.GatewayRouteView]:
        r"""Return a callable for the get gateway route view method over gRPC.

        Get a single RouteView of a Gateway.

        Returns:
            Callable[[~.GetGatewayRouteViewRequest],
                    ~.GatewayRouteView]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_gateway_route_view" not in self._stubs:
            self._stubs["get_gateway_route_view"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/GetGatewayRouteView",
                request_serializer=route_view.GetGatewayRouteViewRequest.serialize,
                response_deserializer=route_view.GatewayRouteView.deserialize,
            )
        return self._stubs["get_gateway_route_view"]

    @property
    def get_mesh_route_view(
        self,
    ) -> Callable[[route_view.GetMeshRouteViewRequest], route_view.MeshRouteView]:
        r"""Return a callable for the get mesh route view method over gRPC.

        Get a single RouteView of a Mesh.

        Returns:
            Callable[[~.GetMeshRouteViewRequest],
                    ~.MeshRouteView]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_mesh_route_view" not in self._stubs:
            self._stubs["get_mesh_route_view"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/GetMeshRouteView",
                request_serializer=route_view.GetMeshRouteViewRequest.serialize,
                response_deserializer=route_view.MeshRouteView.deserialize,
            )
        return self._stubs["get_mesh_route_view"]

    @property
    def list_gateway_route_views(
        self,
    ) -> Callable[
        [route_view.ListGatewayRouteViewsRequest],
        route_view.ListGatewayRouteViewsResponse,
    ]:
        r"""Return a callable for the list gateway route views method over gRPC.

        Lists RouteViews

        Returns:
            Callable[[~.ListGatewayRouteViewsRequest],
                    ~.ListGatewayRouteViewsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_gateway_route_views" not in self._stubs:
            self._stubs["list_gateway_route_views"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/ListGatewayRouteViews",
                request_serializer=route_view.ListGatewayRouteViewsRequest.serialize,
                response_deserializer=route_view.ListGatewayRouteViewsResponse.deserialize,
            )
        return self._stubs["list_gateway_route_views"]

    @property
    def list_mesh_route_views(
        self,
    ) -> Callable[
        [route_view.ListMeshRouteViewsRequest], route_view.ListMeshRouteViewsResponse
    ]:
        r"""Return a callable for the list mesh route views method over gRPC.

        Lists RouteViews

        Returns:
            Callable[[~.ListMeshRouteViewsRequest],
                    ~.ListMeshRouteViewsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_mesh_route_views" not in self._stubs:
            self._stubs["list_mesh_route_views"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/ListMeshRouteViews",
                request_serializer=route_view.ListMeshRouteViewsRequest.serialize,
                response_deserializer=route_view.ListMeshRouteViewsResponse.deserialize,
            )
        return self._stubs["list_mesh_route_views"]

    @property
    def list_agent_gateways(
        self,
    ) -> Callable[
        [agent_gateway.ListAgentGatewaysRequest],
        agent_gateway.ListAgentGatewaysResponse,
    ]:
        r"""Return a callable for the list agent gateways method over gRPC.

        Lists AgentGateways in a given project and location.

        Returns:
            Callable[[~.ListAgentGatewaysRequest],
                    ~.ListAgentGatewaysResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_agent_gateways" not in self._stubs:
            self._stubs["list_agent_gateways"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/ListAgentGateways",
                request_serializer=agent_gateway.ListAgentGatewaysRequest.serialize,
                response_deserializer=agent_gateway.ListAgentGatewaysResponse.deserialize,
            )
        return self._stubs["list_agent_gateways"]

    @property
    def get_agent_gateway(
        self,
    ) -> Callable[[agent_gateway.GetAgentGatewayRequest], agent_gateway.AgentGateway]:
        r"""Return a callable for the get agent gateway method over gRPC.

        Gets details of a single AgentGateway.

        Returns:
            Callable[[~.GetAgentGatewayRequest],
                    ~.AgentGateway]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_agent_gateway" not in self._stubs:
            self._stubs["get_agent_gateway"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/GetAgentGateway",
                request_serializer=agent_gateway.GetAgentGatewayRequest.serialize,
                response_deserializer=agent_gateway.AgentGateway.deserialize,
            )
        return self._stubs["get_agent_gateway"]

    @property
    def create_agent_gateway(
        self,
    ) -> Callable[
        [gcn_agent_gateway.CreateAgentGatewayRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the create agent gateway method over gRPC.

        Creates a new AgentGateway in a given project and
        location.

        Returns:
            Callable[[~.CreateAgentGatewayRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_agent_gateway" not in self._stubs:
            self._stubs["create_agent_gateway"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/CreateAgentGateway",
                request_serializer=gcn_agent_gateway.CreateAgentGatewayRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_agent_gateway"]

    @property
    def update_agent_gateway(
        self,
    ) -> Callable[
        [gcn_agent_gateway.UpdateAgentGatewayRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the update agent gateway method over gRPC.

        Updates the parameters of a single AgentGateway.

        Returns:
            Callable[[~.UpdateAgentGatewayRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_agent_gateway" not in self._stubs:
            self._stubs["update_agent_gateway"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/UpdateAgentGateway",
                request_serializer=gcn_agent_gateway.UpdateAgentGatewayRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_agent_gateway"]

    @property
    def delete_agent_gateway(
        self,
    ) -> Callable[[agent_gateway.DeleteAgentGatewayRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete agent gateway method over gRPC.

        Deletes a single AgentGateway.

        Returns:
            Callable[[~.DeleteAgentGatewayRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_agent_gateway" not in self._stubs:
            self._stubs["delete_agent_gateway"] = self._logged_channel.unary_unary(
                "/google.cloud.networkservices.v1.NetworkServices/DeleteAgentGateway",
                request_serializer=agent_gateway.DeleteAgentGatewayRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_agent_gateway"]

    def close(self):
        self._logged_channel.close()

    @property
    def delete_operation(
        self,
    ) -> Callable[[operations_pb2.DeleteOperationRequest], None]:
        r"""Return a callable for the delete_operation method over gRPC."""
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_operation" not in self._stubs:
            self._stubs["delete_operation"] = self._logged_channel.unary_unary(
                "/google.longrunning.Operations/DeleteOperation",
                request_serializer=operations_pb2.DeleteOperationRequest.SerializeToString,
                response_deserializer=None,
            )
        return self._stubs["delete_operation"]

    @property
    def cancel_operation(
        self,
    ) -> Callable[[operations_pb2.CancelOperationRequest], None]:
        r"""Return a callable for the cancel_operation method over gRPC."""
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "cancel_operation" not in self._stubs:
            self._stubs["cancel_operation"] = self._logged_channel.unary_unary(
                "/google.longrunning.Operations/CancelOperation",
                request_serializer=operations_pb2.CancelOperationRequest.SerializeToString,
                response_deserializer=None,
            )
        return self._stubs["cancel_operation"]

    @property
    def get_operation(
        self,
    ) -> Callable[[operations_pb2.GetOperationRequest], operations_pb2.Operation]:
        r"""Return a callable for the get_operation method over gRPC."""
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_operation" not in self._stubs:
            self._stubs["get_operation"] = self._logged_channel.unary_unary(
                "/google.longrunning.Operations/GetOperation",
                request_serializer=operations_pb2.GetOperationRequest.SerializeToString,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["get_operation"]

    @property
    def list_operations(
        self,
    ) -> Callable[
        [operations_pb2.ListOperationsRequest], operations_pb2.ListOperationsResponse
    ]:
        r"""Return a callable for the list_operations method over gRPC."""
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_operations" not in self._stubs:
            self._stubs["list_operations"] = self._logged_channel.unary_unary(
                "/google.longrunning.Operations/ListOperations",
                request_serializer=operations_pb2.ListOperationsRequest.SerializeToString,
                response_deserializer=operations_pb2.ListOperationsResponse.FromString,
            )
        return self._stubs["list_operations"]

    @property
    def list_locations(
        self,
    ) -> Callable[
        [locations_pb2.ListLocationsRequest], locations_pb2.ListLocationsResponse
    ]:
        r"""Return a callable for the list locations method over gRPC."""
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_locations" not in self._stubs:
            self._stubs["list_locations"] = self._logged_channel.unary_unary(
                "/google.cloud.location.Locations/ListLocations",
                request_serializer=locations_pb2.ListLocationsRequest.SerializeToString,
                response_deserializer=locations_pb2.ListLocationsResponse.FromString,
            )
        return self._stubs["list_locations"]

    @property
    def get_location(
        self,
    ) -> Callable[[locations_pb2.GetLocationRequest], locations_pb2.Location]:
        r"""Return a callable for the list locations method over gRPC."""
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_location" not in self._stubs:
            self._stubs["get_location"] = self._logged_channel.unary_unary(
                "/google.cloud.location.Locations/GetLocation",
                request_serializer=locations_pb2.GetLocationRequest.SerializeToString,
                response_deserializer=locations_pb2.Location.FromString,
            )
        return self._stubs["get_location"]

    @property
    def set_iam_policy(
        self,
    ) -> Callable[[iam_policy_pb2.SetIamPolicyRequest], policy_pb2.Policy]:
        r"""Return a callable for the set iam policy method over gRPC.
        Sets the IAM access control policy on the specified
        function. Replaces any existing policy.
        Returns:
            Callable[[~.SetIamPolicyRequest],
                    ~.Policy]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "set_iam_policy" not in self._stubs:
            self._stubs["set_iam_policy"] = self._logged_channel.unary_unary(
                "/google.iam.v1.IAMPolicy/SetIamPolicy",
                request_serializer=iam_policy_pb2.SetIamPolicyRequest.SerializeToString,
                response_deserializer=policy_pb2.Policy.FromString,
            )
        return self._stubs["set_iam_policy"]

    @property
    def get_iam_policy(
        self,
    ) -> Callable[[iam_policy_pb2.GetIamPolicyRequest], policy_pb2.Policy]:
        r"""Return a callable for the get iam policy method over gRPC.
        Gets the IAM access control policy for a function.
        Returns an empty policy if the function exists and does
        not have a policy set.
        Returns:
            Callable[[~.GetIamPolicyRequest],
                    ~.Policy]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_iam_policy" not in self._stubs:
            self._stubs["get_iam_policy"] = self._logged_channel.unary_unary(
                "/google.iam.v1.IAMPolicy/GetIamPolicy",
                request_serializer=iam_policy_pb2.GetIamPolicyRequest.SerializeToString,
                response_deserializer=policy_pb2.Policy.FromString,
            )
        return self._stubs["get_iam_policy"]

    @property
    def test_iam_permissions(
        self,
    ) -> Callable[
        [iam_policy_pb2.TestIamPermissionsRequest],
        iam_policy_pb2.TestIamPermissionsResponse,
    ]:
        r"""Return a callable for the test iam permissions method over gRPC.
        Tests the specified permissions against the IAM access control
        policy for a function. If the function does not exist, this will
        return an empty set of permissions, not a NOT_FOUND error.
        Returns:
            Callable[[~.TestIamPermissionsRequest],
                    ~.TestIamPermissionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "test_iam_permissions" not in self._stubs:
            self._stubs["test_iam_permissions"] = self._logged_channel.unary_unary(
                "/google.iam.v1.IAMPolicy/TestIamPermissions",
                request_serializer=iam_policy_pb2.TestIamPermissionsRequest.SerializeToString,
                response_deserializer=iam_policy_pb2.TestIamPermissionsResponse.FromString,
            )
        return self._stubs["test_iam_permissions"]

    @property
    def kind(self) -> str:
        return "grpc"


__all__ = ("NetworkServicesGrpcTransport",)
