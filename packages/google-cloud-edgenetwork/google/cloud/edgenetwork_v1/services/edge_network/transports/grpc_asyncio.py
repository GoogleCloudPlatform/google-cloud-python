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
import inspect
import json
import logging as std_logging
import pickle
import warnings
from typing import Awaitable, Callable, Dict, Optional, Sequence, Tuple, Union

import google.protobuf.message
import grpc  # type: ignore
import proto  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, grpc_helpers_async, operations_v1
from google.api_core import retry_async as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf.json_format import MessageToJson
from grpc.experimental import aio  # type: ignore

from google.cloud.edgenetwork_v1.types import resources, service

from .base import DEFAULT_CLIENT_INFO, EdgeNetworkTransport
from .grpc import EdgeNetworkGrpcTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class _LoggingClientAIOInterceptor(
    grpc.aio.UnaryUnaryClientInterceptor
):  # pragma: NO COVER
    async def intercept_unary_unary(self, continuation, client_call_details, request):
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
                    "serviceName": "google.cloud.edgenetwork.v1.EdgeNetwork",
                    "rpcName": str(client_call_details.method),
                    "request": grpc_request,
                    "metadata": grpc_request["metadata"],
                },
            )
        response = await continuation(client_call_details, request)
        if logging_enabled:  # pragma: NO COVER
            response_metadata = await response.trailing_metadata()
            # Convert gRPC metadata `<class 'grpc.aio._metadata.Metadata'>` to list of tuples
            metadata = (
                dict([(k, str(v)) for k, v in response_metadata])
                if response_metadata
                else None
            )
            result = await response
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
                f"Received response to rpc {client_call_details.method}.",
                extra={
                    "serviceName": "google.cloud.edgenetwork.v1.EdgeNetwork",
                    "rpcName": str(client_call_details.method),
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class EdgeNetworkGrpcAsyncIOTransport(EdgeNetworkTransport):
    """gRPC AsyncIO backend transport for EdgeNetwork.

    EdgeNetwork API provides managed, highly available cloud
    dynamic network configuration service to the GEC customer to
    enable edge application and network function solutions. This
    allows the customers to easily define and configure the network
    setup and property to meet the workload requirement.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _grpc_channel: aio.Channel
    _stubs: Dict[str, Callable] = {}

    @classmethod
    def create_channel(
        cls,
        host: str = "edgenetwork.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        **kwargs,
    ) -> aio.Channel:
        """Create and return a gRPC AsyncIO channel object.
        Args:
            host (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): Deprecated. A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`. This argument will be
                removed in the next major version of this library.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            aio.Channel: A gRPC AsyncIO channel object.
        """

        return grpc_helpers_async.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            quota_project_id=quota_project_id,
            default_scopes=cls.AUTH_SCOPES,
            scopes=scopes,
            default_host=cls.DEFAULT_HOST,
            **kwargs,
        )

    def __init__(
        self,
        *,
        host: str = "edgenetwork.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        channel: Optional[Union[aio.Channel, Callable[..., aio.Channel]]] = None,
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
                 The hostname to connect to (default: 'edgenetwork.googleapis.com').
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
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            channel (Optional[Union[aio.Channel, Callable[..., aio.Channel]]]):
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
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        self._grpc_channel = None
        self._ssl_channel_credentials = ssl_channel_credentials
        self._stubs: Dict[str, Callable] = {}
        self._operations_client: Optional[operations_v1.OperationsAsyncClient] = None

        if api_mtls_endpoint:
            warnings.warn("api_mtls_endpoint is deprecated", DeprecationWarning)
        if client_cert_source:
            warnings.warn("client_cert_source is deprecated", DeprecationWarning)

        if isinstance(channel, aio.Channel):
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

        self._interceptor = _LoggingClientAIOInterceptor()
        self._grpc_channel._unary_unary_interceptors.append(self._interceptor)
        self._logged_channel = self._grpc_channel
        self._wrap_with_kind = (
            "kind" in inspect.signature(gapic_v1.method_async.wrap_method).parameters
        )
        # Wrap messages. This must be done after self._logged_channel exists
        self._prep_wrapped_messages(client_info)

    @property
    def grpc_channel(self) -> aio.Channel:
        """Create the channel designed to connect to this service.

        This property caches on the instance; repeated calls return
        the same channel.
        """
        # Return the channel from cache.
        return self._grpc_channel

    @property
    def operations_client(self) -> operations_v1.OperationsAsyncClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Quick check: Only create a new client if we do not already have one.
        if self._operations_client is None:
            self._operations_client = operations_v1.OperationsAsyncClient(
                self._logged_channel
            )

        # Return the client from cache.
        return self._operations_client

    @property
    def initialize_zone(
        self,
    ) -> Callable[
        [service.InitializeZoneRequest], Awaitable[service.InitializeZoneResponse]
    ]:
        r"""Return a callable for the initialize zone method over gRPC.

        InitializeZone will initialize resources for a zone
        in a project.

        Returns:
            Callable[[~.InitializeZoneRequest],
                    Awaitable[~.InitializeZoneResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "initialize_zone" not in self._stubs:
            self._stubs["initialize_zone"] = self._logged_channel.unary_unary(
                "/google.cloud.edgenetwork.v1.EdgeNetwork/InitializeZone",
                request_serializer=service.InitializeZoneRequest.serialize,
                response_deserializer=service.InitializeZoneResponse.deserialize,
            )
        return self._stubs["initialize_zone"]

    @property
    def list_zones(
        self,
    ) -> Callable[[service.ListZonesRequest], Awaitable[service.ListZonesResponse]]:
        r"""Return a callable for the list zones method over gRPC.

        Deprecated: not implemented.
        Lists Zones in a given project and location.

        Returns:
            Callable[[~.ListZonesRequest],
                    Awaitable[~.ListZonesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_zones" not in self._stubs:
            self._stubs["list_zones"] = self._logged_channel.unary_unary(
                "/google.cloud.edgenetwork.v1.EdgeNetwork/ListZones",
                request_serializer=service.ListZonesRequest.serialize,
                response_deserializer=service.ListZonesResponse.deserialize,
            )
        return self._stubs["list_zones"]

    @property
    def get_zone(self) -> Callable[[service.GetZoneRequest], Awaitable[resources.Zone]]:
        r"""Return a callable for the get zone method over gRPC.

        Deprecated: not implemented.
        Gets details of a single Zone.

        Returns:
            Callable[[~.GetZoneRequest],
                    Awaitable[~.Zone]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_zone" not in self._stubs:
            self._stubs["get_zone"] = self._logged_channel.unary_unary(
                "/google.cloud.edgenetwork.v1.EdgeNetwork/GetZone",
                request_serializer=service.GetZoneRequest.serialize,
                response_deserializer=resources.Zone.deserialize,
            )
        return self._stubs["get_zone"]

    @property
    def list_networks(
        self,
    ) -> Callable[
        [service.ListNetworksRequest], Awaitable[service.ListNetworksResponse]
    ]:
        r"""Return a callable for the list networks method over gRPC.

        Lists Networks in a given project and location.

        Returns:
            Callable[[~.ListNetworksRequest],
                    Awaitable[~.ListNetworksResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_networks" not in self._stubs:
            self._stubs["list_networks"] = self._logged_channel.unary_unary(
                "/google.cloud.edgenetwork.v1.EdgeNetwork/ListNetworks",
                request_serializer=service.ListNetworksRequest.serialize,
                response_deserializer=service.ListNetworksResponse.deserialize,
            )
        return self._stubs["list_networks"]

    @property
    def get_network(
        self,
    ) -> Callable[[service.GetNetworkRequest], Awaitable[resources.Network]]:
        r"""Return a callable for the get network method over gRPC.

        Gets details of a single Network.

        Returns:
            Callable[[~.GetNetworkRequest],
                    Awaitable[~.Network]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_network" not in self._stubs:
            self._stubs["get_network"] = self._logged_channel.unary_unary(
                "/google.cloud.edgenetwork.v1.EdgeNetwork/GetNetwork",
                request_serializer=service.GetNetworkRequest.serialize,
                response_deserializer=resources.Network.deserialize,
            )
        return self._stubs["get_network"]

    @property
    def diagnose_network(
        self,
    ) -> Callable[
        [service.DiagnoseNetworkRequest], Awaitable[service.DiagnoseNetworkResponse]
    ]:
        r"""Return a callable for the diagnose network method over gRPC.

        Get the diagnostics of a single network resource.

        Returns:
            Callable[[~.DiagnoseNetworkRequest],
                    Awaitable[~.DiagnoseNetworkResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "diagnose_network" not in self._stubs:
            self._stubs["diagnose_network"] = self._logged_channel.unary_unary(
                "/google.cloud.edgenetwork.v1.EdgeNetwork/DiagnoseNetwork",
                request_serializer=service.DiagnoseNetworkRequest.serialize,
                response_deserializer=service.DiagnoseNetworkResponse.deserialize,
            )
        return self._stubs["diagnose_network"]

    @property
    def create_network(
        self,
    ) -> Callable[[service.CreateNetworkRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the create network method over gRPC.

        Creates a new Network in a given project and
        location.

        Returns:
            Callable[[~.CreateNetworkRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_network" not in self._stubs:
            self._stubs["create_network"] = self._logged_channel.unary_unary(
                "/google.cloud.edgenetwork.v1.EdgeNetwork/CreateNetwork",
                request_serializer=service.CreateNetworkRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_network"]

    @property
    def delete_network(
        self,
    ) -> Callable[[service.DeleteNetworkRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the delete network method over gRPC.

        Deletes a single Network.

        Returns:
            Callable[[~.DeleteNetworkRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_network" not in self._stubs:
            self._stubs["delete_network"] = self._logged_channel.unary_unary(
                "/google.cloud.edgenetwork.v1.EdgeNetwork/DeleteNetwork",
                request_serializer=service.DeleteNetworkRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_network"]

    @property
    def list_subnets(
        self,
    ) -> Callable[[service.ListSubnetsRequest], Awaitable[service.ListSubnetsResponse]]:
        r"""Return a callable for the list subnets method over gRPC.

        Lists Subnets in a given project and location.

        Returns:
            Callable[[~.ListSubnetsRequest],
                    Awaitable[~.ListSubnetsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_subnets" not in self._stubs:
            self._stubs["list_subnets"] = self._logged_channel.unary_unary(
                "/google.cloud.edgenetwork.v1.EdgeNetwork/ListSubnets",
                request_serializer=service.ListSubnetsRequest.serialize,
                response_deserializer=service.ListSubnetsResponse.deserialize,
            )
        return self._stubs["list_subnets"]

    @property
    def get_subnet(
        self,
    ) -> Callable[[service.GetSubnetRequest], Awaitable[resources.Subnet]]:
        r"""Return a callable for the get subnet method over gRPC.

        Gets details of a single Subnet.

        Returns:
            Callable[[~.GetSubnetRequest],
                    Awaitable[~.Subnet]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_subnet" not in self._stubs:
            self._stubs["get_subnet"] = self._logged_channel.unary_unary(
                "/google.cloud.edgenetwork.v1.EdgeNetwork/GetSubnet",
                request_serializer=service.GetSubnetRequest.serialize,
                response_deserializer=resources.Subnet.deserialize,
            )
        return self._stubs["get_subnet"]

    @property
    def create_subnet(
        self,
    ) -> Callable[[service.CreateSubnetRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the create subnet method over gRPC.

        Creates a new Subnet in a given project and location.

        Returns:
            Callable[[~.CreateSubnetRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_subnet" not in self._stubs:
            self._stubs["create_subnet"] = self._logged_channel.unary_unary(
                "/google.cloud.edgenetwork.v1.EdgeNetwork/CreateSubnet",
                request_serializer=service.CreateSubnetRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_subnet"]

    @property
    def update_subnet(
        self,
    ) -> Callable[[service.UpdateSubnetRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the update subnet method over gRPC.

        Updates the parameters of a single Subnet.

        Returns:
            Callable[[~.UpdateSubnetRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_subnet" not in self._stubs:
            self._stubs["update_subnet"] = self._logged_channel.unary_unary(
                "/google.cloud.edgenetwork.v1.EdgeNetwork/UpdateSubnet",
                request_serializer=service.UpdateSubnetRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_subnet"]

    @property
    def delete_subnet(
        self,
    ) -> Callable[[service.DeleteSubnetRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the delete subnet method over gRPC.

        Deletes a single Subnet.

        Returns:
            Callable[[~.DeleteSubnetRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_subnet" not in self._stubs:
            self._stubs["delete_subnet"] = self._logged_channel.unary_unary(
                "/google.cloud.edgenetwork.v1.EdgeNetwork/DeleteSubnet",
                request_serializer=service.DeleteSubnetRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_subnet"]

    @property
    def list_interconnects(
        self,
    ) -> Callable[
        [service.ListInterconnectsRequest], Awaitable[service.ListInterconnectsResponse]
    ]:
        r"""Return a callable for the list interconnects method over gRPC.

        Lists Interconnects in a given project and location.

        Returns:
            Callable[[~.ListInterconnectsRequest],
                    Awaitable[~.ListInterconnectsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_interconnects" not in self._stubs:
            self._stubs["list_interconnects"] = self._logged_channel.unary_unary(
                "/google.cloud.edgenetwork.v1.EdgeNetwork/ListInterconnects",
                request_serializer=service.ListInterconnectsRequest.serialize,
                response_deserializer=service.ListInterconnectsResponse.deserialize,
            )
        return self._stubs["list_interconnects"]

    @property
    def get_interconnect(
        self,
    ) -> Callable[[service.GetInterconnectRequest], Awaitable[resources.Interconnect]]:
        r"""Return a callable for the get interconnect method over gRPC.

        Gets details of a single Interconnect.

        Returns:
            Callable[[~.GetInterconnectRequest],
                    Awaitable[~.Interconnect]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_interconnect" not in self._stubs:
            self._stubs["get_interconnect"] = self._logged_channel.unary_unary(
                "/google.cloud.edgenetwork.v1.EdgeNetwork/GetInterconnect",
                request_serializer=service.GetInterconnectRequest.serialize,
                response_deserializer=resources.Interconnect.deserialize,
            )
        return self._stubs["get_interconnect"]

    @property
    def diagnose_interconnect(
        self,
    ) -> Callable[
        [service.DiagnoseInterconnectRequest],
        Awaitable[service.DiagnoseInterconnectResponse],
    ]:
        r"""Return a callable for the diagnose interconnect method over gRPC.

        Get the diagnostics of a single interconnect
        resource.

        Returns:
            Callable[[~.DiagnoseInterconnectRequest],
                    Awaitable[~.DiagnoseInterconnectResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "diagnose_interconnect" not in self._stubs:
            self._stubs["diagnose_interconnect"] = self._logged_channel.unary_unary(
                "/google.cloud.edgenetwork.v1.EdgeNetwork/DiagnoseInterconnect",
                request_serializer=service.DiagnoseInterconnectRequest.serialize,
                response_deserializer=service.DiagnoseInterconnectResponse.deserialize,
            )
        return self._stubs["diagnose_interconnect"]

    @property
    def list_interconnect_attachments(
        self,
    ) -> Callable[
        [service.ListInterconnectAttachmentsRequest],
        Awaitable[service.ListInterconnectAttachmentsResponse],
    ]:
        r"""Return a callable for the list interconnect attachments method over gRPC.

        Lists InterconnectAttachments in a given project and
        location.

        Returns:
            Callable[[~.ListInterconnectAttachmentsRequest],
                    Awaitable[~.ListInterconnectAttachmentsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_interconnect_attachments" not in self._stubs:
            self._stubs["list_interconnect_attachments"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.edgenetwork.v1.EdgeNetwork/ListInterconnectAttachments",
                    request_serializer=service.ListInterconnectAttachmentsRequest.serialize,
                    response_deserializer=service.ListInterconnectAttachmentsResponse.deserialize,
                )
            )
        return self._stubs["list_interconnect_attachments"]

    @property
    def get_interconnect_attachment(
        self,
    ) -> Callable[
        [service.GetInterconnectAttachmentRequest],
        Awaitable[resources.InterconnectAttachment],
    ]:
        r"""Return a callable for the get interconnect attachment method over gRPC.

        Gets details of a single InterconnectAttachment.

        Returns:
            Callable[[~.GetInterconnectAttachmentRequest],
                    Awaitable[~.InterconnectAttachment]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_interconnect_attachment" not in self._stubs:
            self._stubs["get_interconnect_attachment"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.edgenetwork.v1.EdgeNetwork/GetInterconnectAttachment",
                    request_serializer=service.GetInterconnectAttachmentRequest.serialize,
                    response_deserializer=resources.InterconnectAttachment.deserialize,
                )
            )
        return self._stubs["get_interconnect_attachment"]

    @property
    def create_interconnect_attachment(
        self,
    ) -> Callable[
        [service.CreateInterconnectAttachmentRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the create interconnect attachment method over gRPC.

        Creates a new InterconnectAttachment in a given
        project and location.

        Returns:
            Callable[[~.CreateInterconnectAttachmentRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_interconnect_attachment" not in self._stubs:
            self._stubs["create_interconnect_attachment"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.edgenetwork.v1.EdgeNetwork/CreateInterconnectAttachment",
                    request_serializer=service.CreateInterconnectAttachmentRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["create_interconnect_attachment"]

    @property
    def delete_interconnect_attachment(
        self,
    ) -> Callable[
        [service.DeleteInterconnectAttachmentRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the delete interconnect attachment method over gRPC.

        Deletes a single InterconnectAttachment.

        Returns:
            Callable[[~.DeleteInterconnectAttachmentRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_interconnect_attachment" not in self._stubs:
            self._stubs["delete_interconnect_attachment"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.edgenetwork.v1.EdgeNetwork/DeleteInterconnectAttachment",
                    request_serializer=service.DeleteInterconnectAttachmentRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["delete_interconnect_attachment"]

    @property
    def list_routers(
        self,
    ) -> Callable[[service.ListRoutersRequest], Awaitable[service.ListRoutersResponse]]:
        r"""Return a callable for the list routers method over gRPC.

        Lists Routers in a given project and location.

        Returns:
            Callable[[~.ListRoutersRequest],
                    Awaitable[~.ListRoutersResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_routers" not in self._stubs:
            self._stubs["list_routers"] = self._logged_channel.unary_unary(
                "/google.cloud.edgenetwork.v1.EdgeNetwork/ListRouters",
                request_serializer=service.ListRoutersRequest.serialize,
                response_deserializer=service.ListRoutersResponse.deserialize,
            )
        return self._stubs["list_routers"]

    @property
    def get_router(
        self,
    ) -> Callable[[service.GetRouterRequest], Awaitable[resources.Router]]:
        r"""Return a callable for the get router method over gRPC.

        Gets details of a single Router.

        Returns:
            Callable[[~.GetRouterRequest],
                    Awaitable[~.Router]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_router" not in self._stubs:
            self._stubs["get_router"] = self._logged_channel.unary_unary(
                "/google.cloud.edgenetwork.v1.EdgeNetwork/GetRouter",
                request_serializer=service.GetRouterRequest.serialize,
                response_deserializer=resources.Router.deserialize,
            )
        return self._stubs["get_router"]

    @property
    def diagnose_router(
        self,
    ) -> Callable[
        [service.DiagnoseRouterRequest], Awaitable[service.DiagnoseRouterResponse]
    ]:
        r"""Return a callable for the diagnose router method over gRPC.

        Get the diagnostics of a single router resource.

        Returns:
            Callable[[~.DiagnoseRouterRequest],
                    Awaitable[~.DiagnoseRouterResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "diagnose_router" not in self._stubs:
            self._stubs["diagnose_router"] = self._logged_channel.unary_unary(
                "/google.cloud.edgenetwork.v1.EdgeNetwork/DiagnoseRouter",
                request_serializer=service.DiagnoseRouterRequest.serialize,
                response_deserializer=service.DiagnoseRouterResponse.deserialize,
            )
        return self._stubs["diagnose_router"]

    @property
    def create_router(
        self,
    ) -> Callable[[service.CreateRouterRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the create router method over gRPC.

        Creates a new Router in a given project and location.

        Returns:
            Callable[[~.CreateRouterRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_router" not in self._stubs:
            self._stubs["create_router"] = self._logged_channel.unary_unary(
                "/google.cloud.edgenetwork.v1.EdgeNetwork/CreateRouter",
                request_serializer=service.CreateRouterRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_router"]

    @property
    def update_router(
        self,
    ) -> Callable[[service.UpdateRouterRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the update router method over gRPC.

        Updates the parameters of a single Router.

        Returns:
            Callable[[~.UpdateRouterRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_router" not in self._stubs:
            self._stubs["update_router"] = self._logged_channel.unary_unary(
                "/google.cloud.edgenetwork.v1.EdgeNetwork/UpdateRouter",
                request_serializer=service.UpdateRouterRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_router"]

    @property
    def delete_router(
        self,
    ) -> Callable[[service.DeleteRouterRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the delete router method over gRPC.

        Deletes a single Router.

        Returns:
            Callable[[~.DeleteRouterRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_router" not in self._stubs:
            self._stubs["delete_router"] = self._logged_channel.unary_unary(
                "/google.cloud.edgenetwork.v1.EdgeNetwork/DeleteRouter",
                request_serializer=service.DeleteRouterRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_router"]

    def _prep_wrapped_messages(self, client_info):
        """Precompute the wrapped methods, overriding the base class method to use async wrappers."""
        self._wrapped_methods = {
            self.initialize_zone: self._wrap_method(
                self.initialize_zone,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_zones: self._wrap_method(
                self.list_zones,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_zone: self._wrap_method(
                self.get_zone,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_networks: self._wrap_method(
                self.list_networks,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_network: self._wrap_method(
                self.get_network,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.diagnose_network: self._wrap_method(
                self.diagnose_network,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_network: self._wrap_method(
                self.create_network,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_network: self._wrap_method(
                self.delete_network,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_subnets: self._wrap_method(
                self.list_subnets,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_subnet: self._wrap_method(
                self.get_subnet,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_subnet: self._wrap_method(
                self.create_subnet,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_subnet: self._wrap_method(
                self.update_subnet,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_subnet: self._wrap_method(
                self.delete_subnet,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_interconnects: self._wrap_method(
                self.list_interconnects,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_interconnect: self._wrap_method(
                self.get_interconnect,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.diagnose_interconnect: self._wrap_method(
                self.diagnose_interconnect,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_interconnect_attachments: self._wrap_method(
                self.list_interconnect_attachments,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_interconnect_attachment: self._wrap_method(
                self.get_interconnect_attachment,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_interconnect_attachment: self._wrap_method(
                self.create_interconnect_attachment,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_interconnect_attachment: self._wrap_method(
                self.delete_interconnect_attachment,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_routers: self._wrap_method(
                self.list_routers,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_router: self._wrap_method(
                self.get_router,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.diagnose_router: self._wrap_method(
                self.diagnose_router,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_router: self._wrap_method(
                self.create_router,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_router: self._wrap_method(
                self.update_router,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_router: self._wrap_method(
                self.delete_router,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_location: self._wrap_method(
                self.get_location,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_locations: self._wrap_method(
                self.list_locations,
                default_timeout=None,
                client_info=client_info,
            ),
            self.cancel_operation: self._wrap_method(
                self.cancel_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_operation: self._wrap_method(
                self.delete_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_operation: self._wrap_method(
                self.get_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_operations: self._wrap_method(
                self.list_operations,
                default_timeout=None,
                client_info=client_info,
            ),
        }

    def _wrap_method(self, func, *args, **kwargs):
        if self._wrap_with_kind:  # pragma: NO COVER
            kwargs["kind"] = self.kind
        return gapic_v1.method_async.wrap_method(func, *args, **kwargs)

    def close(self):
        return self._logged_channel.close()

    @property
    def kind(self) -> str:
        return "grpc_asyncio"

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


__all__ = ("EdgeNetworkGrpcAsyncIOTransport",)
