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
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf.json_format import MessageToJson
from grpc.experimental import aio  # type: ignore

from google.cloud.networkconnectivity_v1.types import hub
from google.cloud.networkconnectivity_v1.types import hub as gcn_hub

from .base import DEFAULT_CLIENT_INFO, HubServiceTransport
from .grpc import HubServiceGrpcTransport

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
                    "serviceName": "google.cloud.networkconnectivity.v1.HubService",
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
                    "serviceName": "google.cloud.networkconnectivity.v1.HubService",
                    "rpcName": str(client_call_details.method),
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class HubServiceGrpcAsyncIOTransport(HubServiceTransport):
    """gRPC AsyncIO backend transport for HubService.

    Network Connectivity Center is a hub-and-spoke abstraction
    for network connectivity management in Google Cloud. It reduces
    operational complexity through a simple, centralized
    connectivity management model.

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
        host: str = "networkconnectivity.googleapis.com",
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
        host: str = "networkconnectivity.googleapis.com",
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
                 The hostname to connect to (default: 'networkconnectivity.googleapis.com').
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
    def list_hubs(
        self,
    ) -> Callable[[hub.ListHubsRequest], Awaitable[hub.ListHubsResponse]]:
        r"""Return a callable for the list hubs method over gRPC.

        Lists the Network Connectivity Center hubs associated
        with a given project.

        Returns:
            Callable[[~.ListHubsRequest],
                    Awaitable[~.ListHubsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_hubs" not in self._stubs:
            self._stubs["list_hubs"] = self._logged_channel.unary_unary(
                "/google.cloud.networkconnectivity.v1.HubService/ListHubs",
                request_serializer=hub.ListHubsRequest.serialize,
                response_deserializer=hub.ListHubsResponse.deserialize,
            )
        return self._stubs["list_hubs"]

    @property
    def get_hub(self) -> Callable[[hub.GetHubRequest], Awaitable[hub.Hub]]:
        r"""Return a callable for the get hub method over gRPC.

        Gets details about a Network Connectivity Center hub.

        Returns:
            Callable[[~.GetHubRequest],
                    Awaitable[~.Hub]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_hub" not in self._stubs:
            self._stubs["get_hub"] = self._logged_channel.unary_unary(
                "/google.cloud.networkconnectivity.v1.HubService/GetHub",
                request_serializer=hub.GetHubRequest.serialize,
                response_deserializer=hub.Hub.deserialize,
            )
        return self._stubs["get_hub"]

    @property
    def create_hub(
        self,
    ) -> Callable[[gcn_hub.CreateHubRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the create hub method over gRPC.

        Creates a new Network Connectivity Center hub in the
        specified project.

        Returns:
            Callable[[~.CreateHubRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_hub" not in self._stubs:
            self._stubs["create_hub"] = self._logged_channel.unary_unary(
                "/google.cloud.networkconnectivity.v1.HubService/CreateHub",
                request_serializer=gcn_hub.CreateHubRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_hub"]

    @property
    def update_hub(
        self,
    ) -> Callable[[gcn_hub.UpdateHubRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the update hub method over gRPC.

        Updates the description and/or labels of a Network
        Connectivity Center hub.

        Returns:
            Callable[[~.UpdateHubRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_hub" not in self._stubs:
            self._stubs["update_hub"] = self._logged_channel.unary_unary(
                "/google.cloud.networkconnectivity.v1.HubService/UpdateHub",
                request_serializer=gcn_hub.UpdateHubRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_hub"]

    @property
    def delete_hub(
        self,
    ) -> Callable[[hub.DeleteHubRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the delete hub method over gRPC.

        Deletes a Network Connectivity Center hub.

        Returns:
            Callable[[~.DeleteHubRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_hub" not in self._stubs:
            self._stubs["delete_hub"] = self._logged_channel.unary_unary(
                "/google.cloud.networkconnectivity.v1.HubService/DeleteHub",
                request_serializer=hub.DeleteHubRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_hub"]

    @property
    def list_hub_spokes(
        self,
    ) -> Callable[[hub.ListHubSpokesRequest], Awaitable[hub.ListHubSpokesResponse]]:
        r"""Return a callable for the list hub spokes method over gRPC.

        Lists the Network Connectivity Center spokes
        associated with a specified hub and location. The list
        includes both spokes that are attached to the hub and
        spokes that have been proposed but not yet accepted.

        Returns:
            Callable[[~.ListHubSpokesRequest],
                    Awaitable[~.ListHubSpokesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_hub_spokes" not in self._stubs:
            self._stubs["list_hub_spokes"] = self._logged_channel.unary_unary(
                "/google.cloud.networkconnectivity.v1.HubService/ListHubSpokes",
                request_serializer=hub.ListHubSpokesRequest.serialize,
                response_deserializer=hub.ListHubSpokesResponse.deserialize,
            )
        return self._stubs["list_hub_spokes"]

    @property
    def query_hub_status(
        self,
    ) -> Callable[[hub.QueryHubStatusRequest], Awaitable[hub.QueryHubStatusResponse]]:
        r"""Return a callable for the query hub status method over gRPC.

        Query the Private Service Connect propagation status
        of a Network Connectivity Center hub.

        Returns:
            Callable[[~.QueryHubStatusRequest],
                    Awaitable[~.QueryHubStatusResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "query_hub_status" not in self._stubs:
            self._stubs["query_hub_status"] = self._logged_channel.unary_unary(
                "/google.cloud.networkconnectivity.v1.HubService/QueryHubStatus",
                request_serializer=hub.QueryHubStatusRequest.serialize,
                response_deserializer=hub.QueryHubStatusResponse.deserialize,
            )
        return self._stubs["query_hub_status"]

    @property
    def list_spokes(
        self,
    ) -> Callable[[hub.ListSpokesRequest], Awaitable[hub.ListSpokesResponse]]:
        r"""Return a callable for the list spokes method over gRPC.

        Lists the Network Connectivity Center spokes in a
        specified project and location.

        Returns:
            Callable[[~.ListSpokesRequest],
                    Awaitable[~.ListSpokesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_spokes" not in self._stubs:
            self._stubs["list_spokes"] = self._logged_channel.unary_unary(
                "/google.cloud.networkconnectivity.v1.HubService/ListSpokes",
                request_serializer=hub.ListSpokesRequest.serialize,
                response_deserializer=hub.ListSpokesResponse.deserialize,
            )
        return self._stubs["list_spokes"]

    @property
    def get_spoke(self) -> Callable[[hub.GetSpokeRequest], Awaitable[hub.Spoke]]:
        r"""Return a callable for the get spoke method over gRPC.

        Gets details about a Network Connectivity Center
        spoke.

        Returns:
            Callable[[~.GetSpokeRequest],
                    Awaitable[~.Spoke]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_spoke" not in self._stubs:
            self._stubs["get_spoke"] = self._logged_channel.unary_unary(
                "/google.cloud.networkconnectivity.v1.HubService/GetSpoke",
                request_serializer=hub.GetSpokeRequest.serialize,
                response_deserializer=hub.Spoke.deserialize,
            )
        return self._stubs["get_spoke"]

    @property
    def create_spoke(
        self,
    ) -> Callable[[hub.CreateSpokeRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the create spoke method over gRPC.

        Creates a Network Connectivity Center spoke.

        Returns:
            Callable[[~.CreateSpokeRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_spoke" not in self._stubs:
            self._stubs["create_spoke"] = self._logged_channel.unary_unary(
                "/google.cloud.networkconnectivity.v1.HubService/CreateSpoke",
                request_serializer=hub.CreateSpokeRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_spoke"]

    @property
    def update_spoke(
        self,
    ) -> Callable[[hub.UpdateSpokeRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the update spoke method over gRPC.

        Updates the parameters of a Network Connectivity
        Center spoke.

        Returns:
            Callable[[~.UpdateSpokeRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_spoke" not in self._stubs:
            self._stubs["update_spoke"] = self._logged_channel.unary_unary(
                "/google.cloud.networkconnectivity.v1.HubService/UpdateSpoke",
                request_serializer=hub.UpdateSpokeRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_spoke"]

    @property
    def reject_hub_spoke(
        self,
    ) -> Callable[[hub.RejectHubSpokeRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the reject hub spoke method over gRPC.

        Rejects a Network Connectivity Center spoke from being attached
        to a hub. If the spoke was previously in the ``ACTIVE`` state,
        it transitions to the ``INACTIVE`` state and is no longer able
        to connect to other spokes that are attached to the hub.

        Returns:
            Callable[[~.RejectHubSpokeRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "reject_hub_spoke" not in self._stubs:
            self._stubs["reject_hub_spoke"] = self._logged_channel.unary_unary(
                "/google.cloud.networkconnectivity.v1.HubService/RejectHubSpoke",
                request_serializer=hub.RejectHubSpokeRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["reject_hub_spoke"]

    @property
    def accept_hub_spoke(
        self,
    ) -> Callable[[hub.AcceptHubSpokeRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the accept hub spoke method over gRPC.

        Accepts a proposal to attach a Network Connectivity
        Center spoke to a hub.

        Returns:
            Callable[[~.AcceptHubSpokeRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "accept_hub_spoke" not in self._stubs:
            self._stubs["accept_hub_spoke"] = self._logged_channel.unary_unary(
                "/google.cloud.networkconnectivity.v1.HubService/AcceptHubSpoke",
                request_serializer=hub.AcceptHubSpokeRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["accept_hub_spoke"]

    @property
    def accept_spoke_update(
        self,
    ) -> Callable[[hub.AcceptSpokeUpdateRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the accept spoke update method over gRPC.

        Accepts a proposal to update a Network Connectivity
        Center spoke in a hub.

        Returns:
            Callable[[~.AcceptSpokeUpdateRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "accept_spoke_update" not in self._stubs:
            self._stubs["accept_spoke_update"] = self._logged_channel.unary_unary(
                "/google.cloud.networkconnectivity.v1.HubService/AcceptSpokeUpdate",
                request_serializer=hub.AcceptSpokeUpdateRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["accept_spoke_update"]

    @property
    def reject_spoke_update(
        self,
    ) -> Callable[[hub.RejectSpokeUpdateRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the reject spoke update method over gRPC.

        Rejects a proposal to update a Network Connectivity
        Center spoke in a hub.

        Returns:
            Callable[[~.RejectSpokeUpdateRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "reject_spoke_update" not in self._stubs:
            self._stubs["reject_spoke_update"] = self._logged_channel.unary_unary(
                "/google.cloud.networkconnectivity.v1.HubService/RejectSpokeUpdate",
                request_serializer=hub.RejectSpokeUpdateRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["reject_spoke_update"]

    @property
    def delete_spoke(
        self,
    ) -> Callable[[hub.DeleteSpokeRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the delete spoke method over gRPC.

        Deletes a Network Connectivity Center spoke.

        Returns:
            Callable[[~.DeleteSpokeRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_spoke" not in self._stubs:
            self._stubs["delete_spoke"] = self._logged_channel.unary_unary(
                "/google.cloud.networkconnectivity.v1.HubService/DeleteSpoke",
                request_serializer=hub.DeleteSpokeRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_spoke"]

    @property
    def get_route_table(
        self,
    ) -> Callable[[hub.GetRouteTableRequest], Awaitable[hub.RouteTable]]:
        r"""Return a callable for the get route table method over gRPC.

        Gets details about a Network Connectivity Center
        route table.

        Returns:
            Callable[[~.GetRouteTableRequest],
                    Awaitable[~.RouteTable]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_route_table" not in self._stubs:
            self._stubs["get_route_table"] = self._logged_channel.unary_unary(
                "/google.cloud.networkconnectivity.v1.HubService/GetRouteTable",
                request_serializer=hub.GetRouteTableRequest.serialize,
                response_deserializer=hub.RouteTable.deserialize,
            )
        return self._stubs["get_route_table"]

    @property
    def get_route(self) -> Callable[[hub.GetRouteRequest], Awaitable[hub.Route]]:
        r"""Return a callable for the get route method over gRPC.

        Gets details about the specified route.

        Returns:
            Callable[[~.GetRouteRequest],
                    Awaitable[~.Route]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_route" not in self._stubs:
            self._stubs["get_route"] = self._logged_channel.unary_unary(
                "/google.cloud.networkconnectivity.v1.HubService/GetRoute",
                request_serializer=hub.GetRouteRequest.serialize,
                response_deserializer=hub.Route.deserialize,
            )
        return self._stubs["get_route"]

    @property
    def list_routes(
        self,
    ) -> Callable[[hub.ListRoutesRequest], Awaitable[hub.ListRoutesResponse]]:
        r"""Return a callable for the list routes method over gRPC.

        Lists routes in a given route table.

        Returns:
            Callable[[~.ListRoutesRequest],
                    Awaitable[~.ListRoutesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_routes" not in self._stubs:
            self._stubs["list_routes"] = self._logged_channel.unary_unary(
                "/google.cloud.networkconnectivity.v1.HubService/ListRoutes",
                request_serializer=hub.ListRoutesRequest.serialize,
                response_deserializer=hub.ListRoutesResponse.deserialize,
            )
        return self._stubs["list_routes"]

    @property
    def list_route_tables(
        self,
    ) -> Callable[[hub.ListRouteTablesRequest], Awaitable[hub.ListRouteTablesResponse]]:
        r"""Return a callable for the list route tables method over gRPC.

        Lists route tables in a given hub.

        Returns:
            Callable[[~.ListRouteTablesRequest],
                    Awaitable[~.ListRouteTablesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_route_tables" not in self._stubs:
            self._stubs["list_route_tables"] = self._logged_channel.unary_unary(
                "/google.cloud.networkconnectivity.v1.HubService/ListRouteTables",
                request_serializer=hub.ListRouteTablesRequest.serialize,
                response_deserializer=hub.ListRouteTablesResponse.deserialize,
            )
        return self._stubs["list_route_tables"]

    @property
    def get_group(self) -> Callable[[hub.GetGroupRequest], Awaitable[hub.Group]]:
        r"""Return a callable for the get group method over gRPC.

        Gets details about a Network Connectivity Center
        group.

        Returns:
            Callable[[~.GetGroupRequest],
                    Awaitable[~.Group]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_group" not in self._stubs:
            self._stubs["get_group"] = self._logged_channel.unary_unary(
                "/google.cloud.networkconnectivity.v1.HubService/GetGroup",
                request_serializer=hub.GetGroupRequest.serialize,
                response_deserializer=hub.Group.deserialize,
            )
        return self._stubs["get_group"]

    @property
    def list_groups(
        self,
    ) -> Callable[[hub.ListGroupsRequest], Awaitable[hub.ListGroupsResponse]]:
        r"""Return a callable for the list groups method over gRPC.

        Lists groups in a given hub.

        Returns:
            Callable[[~.ListGroupsRequest],
                    Awaitable[~.ListGroupsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_groups" not in self._stubs:
            self._stubs["list_groups"] = self._logged_channel.unary_unary(
                "/google.cloud.networkconnectivity.v1.HubService/ListGroups",
                request_serializer=hub.ListGroupsRequest.serialize,
                response_deserializer=hub.ListGroupsResponse.deserialize,
            )
        return self._stubs["list_groups"]

    @property
    def update_group(
        self,
    ) -> Callable[[hub.UpdateGroupRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the update group method over gRPC.

        Updates the parameters of a Network Connectivity
        Center group.

        Returns:
            Callable[[~.UpdateGroupRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_group" not in self._stubs:
            self._stubs["update_group"] = self._logged_channel.unary_unary(
                "/google.cloud.networkconnectivity.v1.HubService/UpdateGroup",
                request_serializer=hub.UpdateGroupRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_group"]

    def _prep_wrapped_messages(self, client_info):
        """Precompute the wrapped methods, overriding the base class method to use async wrappers."""
        self._wrapped_methods = {
            self.list_hubs: self._wrap_method(
                self.list_hubs,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_hub: self._wrap_method(
                self.get_hub,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_hub: self._wrap_method(
                self.create_hub,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_hub: self._wrap_method(
                self.update_hub,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_hub: self._wrap_method(
                self.delete_hub,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_hub_spokes: self._wrap_method(
                self.list_hub_spokes,
                default_timeout=None,
                client_info=client_info,
            ),
            self.query_hub_status: self._wrap_method(
                self.query_hub_status,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_spokes: self._wrap_method(
                self.list_spokes,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_spoke: self._wrap_method(
                self.get_spoke,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_spoke: self._wrap_method(
                self.create_spoke,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_spoke: self._wrap_method(
                self.update_spoke,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.reject_hub_spoke: self._wrap_method(
                self.reject_hub_spoke,
                default_timeout=None,
                client_info=client_info,
            ),
            self.accept_hub_spoke: self._wrap_method(
                self.accept_hub_spoke,
                default_timeout=None,
                client_info=client_info,
            ),
            self.accept_spoke_update: self._wrap_method(
                self.accept_spoke_update,
                default_timeout=None,
                client_info=client_info,
            ),
            self.reject_spoke_update: self._wrap_method(
                self.reject_spoke_update,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_spoke: self._wrap_method(
                self.delete_spoke,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_route_table: self._wrap_method(
                self.get_route_table,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_route: self._wrap_method(
                self.get_route,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_routes: self._wrap_method(
                self.list_routes,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_route_tables: self._wrap_method(
                self.list_route_tables,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_group: self._wrap_method(
                self.get_group,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_groups: self._wrap_method(
                self.list_groups,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_group: self._wrap_method(
                self.update_group,
                default_timeout=None,
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
            self.get_iam_policy: self._wrap_method(
                self.get_iam_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.set_iam_policy: self._wrap_method(
                self.set_iam_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.test_iam_permissions: self._wrap_method(
                self.test_iam_permissions,
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


__all__ = ("HubServiceGrpcAsyncIOTransport",)
