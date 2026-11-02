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

from google.cloud.eventarc_v1.types import (
    channel,
    channel_connection,
    discovery,
    enrollment,
    eventarc,
    google_api_source,
    google_channel_config,
    message_bus,
    pipeline,
    trigger,
)
from google.cloud.eventarc_v1.types import (
    google_channel_config as gce_google_channel_config,
)

from .base import DEFAULT_CLIENT_INFO, EventarcTransport

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
                    "serviceName": "google.cloud.eventarc.v1.Eventarc",
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
                    "serviceName": "google.cloud.eventarc.v1.Eventarc",
                    "rpcName": client_call_details.method,
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class EventarcGrpcTransport(EventarcTransport):
    """gRPC backend transport for Eventarc.

    Eventarc allows users to subscribe to various events that are
    provided by Google Cloud services and forward them to supported
    destinations.

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
        host: str = "eventarc.googleapis.com",
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
                 The hostname to connect to (default: 'eventarc.googleapis.com').
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
        host: str = "eventarc.googleapis.com",
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
    def get_trigger(self) -> Callable[[eventarc.GetTriggerRequest], trigger.Trigger]:
        r"""Return a callable for the get trigger method over gRPC.

        Get a single trigger.

        Returns:
            Callable[[~.GetTriggerRequest],
                    ~.Trigger]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_trigger" not in self._stubs:
            self._stubs["get_trigger"] = self._logged_channel.unary_unary(
                "/google.cloud.eventarc.v1.Eventarc/GetTrigger",
                request_serializer=eventarc.GetTriggerRequest.serialize,
                response_deserializer=trigger.Trigger.deserialize,
            )
        return self._stubs["get_trigger"]

    @property
    def list_triggers(
        self,
    ) -> Callable[[eventarc.ListTriggersRequest], eventarc.ListTriggersResponse]:
        r"""Return a callable for the list triggers method over gRPC.

        List triggers.

        Returns:
            Callable[[~.ListTriggersRequest],
                    ~.ListTriggersResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_triggers" not in self._stubs:
            self._stubs["list_triggers"] = self._logged_channel.unary_unary(
                "/google.cloud.eventarc.v1.Eventarc/ListTriggers",
                request_serializer=eventarc.ListTriggersRequest.serialize,
                response_deserializer=eventarc.ListTriggersResponse.deserialize,
            )
        return self._stubs["list_triggers"]

    @property
    def create_trigger(
        self,
    ) -> Callable[[eventarc.CreateTriggerRequest], operations_pb2.Operation]:
        r"""Return a callable for the create trigger method over gRPC.

        Create a new trigger in a particular project and
        location.

        Returns:
            Callable[[~.CreateTriggerRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_trigger" not in self._stubs:
            self._stubs["create_trigger"] = self._logged_channel.unary_unary(
                "/google.cloud.eventarc.v1.Eventarc/CreateTrigger",
                request_serializer=eventarc.CreateTriggerRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_trigger"]

    @property
    def update_trigger(
        self,
    ) -> Callable[[eventarc.UpdateTriggerRequest], operations_pb2.Operation]:
        r"""Return a callable for the update trigger method over gRPC.

        Update a single trigger.

        Returns:
            Callable[[~.UpdateTriggerRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_trigger" not in self._stubs:
            self._stubs["update_trigger"] = self._logged_channel.unary_unary(
                "/google.cloud.eventarc.v1.Eventarc/UpdateTrigger",
                request_serializer=eventarc.UpdateTriggerRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_trigger"]

    @property
    def delete_trigger(
        self,
    ) -> Callable[[eventarc.DeleteTriggerRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete trigger method over gRPC.

        Delete a single trigger.

        Returns:
            Callable[[~.DeleteTriggerRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_trigger" not in self._stubs:
            self._stubs["delete_trigger"] = self._logged_channel.unary_unary(
                "/google.cloud.eventarc.v1.Eventarc/DeleteTrigger",
                request_serializer=eventarc.DeleteTriggerRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_trigger"]

    @property
    def get_channel(self) -> Callable[[eventarc.GetChannelRequest], channel.Channel]:
        r"""Return a callable for the get channel method over gRPC.

        Get a single Channel.

        Returns:
            Callable[[~.GetChannelRequest],
                    ~.Channel]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_channel" not in self._stubs:
            self._stubs["get_channel"] = self._logged_channel.unary_unary(
                "/google.cloud.eventarc.v1.Eventarc/GetChannel",
                request_serializer=eventarc.GetChannelRequest.serialize,
                response_deserializer=channel.Channel.deserialize,
            )
        return self._stubs["get_channel"]

    @property
    def list_channels(
        self,
    ) -> Callable[[eventarc.ListChannelsRequest], eventarc.ListChannelsResponse]:
        r"""Return a callable for the list channels method over gRPC.

        List channels.

        Returns:
            Callable[[~.ListChannelsRequest],
                    ~.ListChannelsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_channels" not in self._stubs:
            self._stubs["list_channels"] = self._logged_channel.unary_unary(
                "/google.cloud.eventarc.v1.Eventarc/ListChannels",
                request_serializer=eventarc.ListChannelsRequest.serialize,
                response_deserializer=eventarc.ListChannelsResponse.deserialize,
            )
        return self._stubs["list_channels"]

    @property
    def create_channel_(
        self,
    ) -> Callable[[eventarc.CreateChannelRequest], operations_pb2.Operation]:
        r"""Return a callable for the create channel method over gRPC.

        Create a new channel in a particular project and
        location.

        Returns:
            Callable[[~.CreateChannelRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_channel_" not in self._stubs:
            self._stubs["create_channel_"] = self._logged_channel.unary_unary(
                "/google.cloud.eventarc.v1.Eventarc/CreateChannel",
                request_serializer=eventarc.CreateChannelRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_channel_"]

    @property
    def update_channel(
        self,
    ) -> Callable[[eventarc.UpdateChannelRequest], operations_pb2.Operation]:
        r"""Return a callable for the update channel method over gRPC.

        Update a single channel.

        Returns:
            Callable[[~.UpdateChannelRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_channel" not in self._stubs:
            self._stubs["update_channel"] = self._logged_channel.unary_unary(
                "/google.cloud.eventarc.v1.Eventarc/UpdateChannel",
                request_serializer=eventarc.UpdateChannelRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_channel"]

    @property
    def delete_channel(
        self,
    ) -> Callable[[eventarc.DeleteChannelRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete channel method over gRPC.

        Delete a single channel.

        Returns:
            Callable[[~.DeleteChannelRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_channel" not in self._stubs:
            self._stubs["delete_channel"] = self._logged_channel.unary_unary(
                "/google.cloud.eventarc.v1.Eventarc/DeleteChannel",
                request_serializer=eventarc.DeleteChannelRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_channel"]

    @property
    def get_provider(
        self,
    ) -> Callable[[eventarc.GetProviderRequest], discovery.Provider]:
        r"""Return a callable for the get provider method over gRPC.

        Get a single Provider.

        Returns:
            Callable[[~.GetProviderRequest],
                    ~.Provider]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_provider" not in self._stubs:
            self._stubs["get_provider"] = self._logged_channel.unary_unary(
                "/google.cloud.eventarc.v1.Eventarc/GetProvider",
                request_serializer=eventarc.GetProviderRequest.serialize,
                response_deserializer=discovery.Provider.deserialize,
            )
        return self._stubs["get_provider"]

    @property
    def list_providers(
        self,
    ) -> Callable[[eventarc.ListProvidersRequest], eventarc.ListProvidersResponse]:
        r"""Return a callable for the list providers method over gRPC.

        List providers.

        Returns:
            Callable[[~.ListProvidersRequest],
                    ~.ListProvidersResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_providers" not in self._stubs:
            self._stubs["list_providers"] = self._logged_channel.unary_unary(
                "/google.cloud.eventarc.v1.Eventarc/ListProviders",
                request_serializer=eventarc.ListProvidersRequest.serialize,
                response_deserializer=eventarc.ListProvidersResponse.deserialize,
            )
        return self._stubs["list_providers"]

    @property
    def get_channel_connection(
        self,
    ) -> Callable[
        [eventarc.GetChannelConnectionRequest], channel_connection.ChannelConnection
    ]:
        r"""Return a callable for the get channel connection method over gRPC.

        Get a single ChannelConnection.

        Returns:
            Callable[[~.GetChannelConnectionRequest],
                    ~.ChannelConnection]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_channel_connection" not in self._stubs:
            self._stubs["get_channel_connection"] = self._logged_channel.unary_unary(
                "/google.cloud.eventarc.v1.Eventarc/GetChannelConnection",
                request_serializer=eventarc.GetChannelConnectionRequest.serialize,
                response_deserializer=channel_connection.ChannelConnection.deserialize,
            )
        return self._stubs["get_channel_connection"]

    @property
    def list_channel_connections(
        self,
    ) -> Callable[
        [eventarc.ListChannelConnectionsRequest],
        eventarc.ListChannelConnectionsResponse,
    ]:
        r"""Return a callable for the list channel connections method over gRPC.

        List channel connections.

        Returns:
            Callable[[~.ListChannelConnectionsRequest],
                    ~.ListChannelConnectionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_channel_connections" not in self._stubs:
            self._stubs["list_channel_connections"] = self._logged_channel.unary_unary(
                "/google.cloud.eventarc.v1.Eventarc/ListChannelConnections",
                request_serializer=eventarc.ListChannelConnectionsRequest.serialize,
                response_deserializer=eventarc.ListChannelConnectionsResponse.deserialize,
            )
        return self._stubs["list_channel_connections"]

    @property
    def create_channel_connection(
        self,
    ) -> Callable[[eventarc.CreateChannelConnectionRequest], operations_pb2.Operation]:
        r"""Return a callable for the create channel connection method over gRPC.

        Create a new ChannelConnection in a particular
        project and location.

        Returns:
            Callable[[~.CreateChannelConnectionRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_channel_connection" not in self._stubs:
            self._stubs["create_channel_connection"] = self._logged_channel.unary_unary(
                "/google.cloud.eventarc.v1.Eventarc/CreateChannelConnection",
                request_serializer=eventarc.CreateChannelConnectionRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_channel_connection"]

    @property
    def delete_channel_connection(
        self,
    ) -> Callable[[eventarc.DeleteChannelConnectionRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete channel connection method over gRPC.

        Delete a single ChannelConnection.

        Returns:
            Callable[[~.DeleteChannelConnectionRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_channel_connection" not in self._stubs:
            self._stubs["delete_channel_connection"] = self._logged_channel.unary_unary(
                "/google.cloud.eventarc.v1.Eventarc/DeleteChannelConnection",
                request_serializer=eventarc.DeleteChannelConnectionRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_channel_connection"]

    @property
    def get_google_channel_config(
        self,
    ) -> Callable[
        [eventarc.GetGoogleChannelConfigRequest],
        google_channel_config.GoogleChannelConfig,
    ]:
        r"""Return a callable for the get google channel config method over gRPC.

        Get a GoogleChannelConfig.
        The name of the GoogleChannelConfig in the response is
        ALWAYS coded with projectID.

        Returns:
            Callable[[~.GetGoogleChannelConfigRequest],
                    ~.GoogleChannelConfig]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_google_channel_config" not in self._stubs:
            self._stubs["get_google_channel_config"] = self._logged_channel.unary_unary(
                "/google.cloud.eventarc.v1.Eventarc/GetGoogleChannelConfig",
                request_serializer=eventarc.GetGoogleChannelConfigRequest.serialize,
                response_deserializer=google_channel_config.GoogleChannelConfig.deserialize,
            )
        return self._stubs["get_google_channel_config"]

    @property
    def update_google_channel_config(
        self,
    ) -> Callable[
        [eventarc.UpdateGoogleChannelConfigRequest],
        gce_google_channel_config.GoogleChannelConfig,
    ]:
        r"""Return a callable for the update google channel config method over gRPC.

        Update a single GoogleChannelConfig

        Returns:
            Callable[[~.UpdateGoogleChannelConfigRequest],
                    ~.GoogleChannelConfig]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_google_channel_config" not in self._stubs:
            self._stubs["update_google_channel_config"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.eventarc.v1.Eventarc/UpdateGoogleChannelConfig",
                    request_serializer=eventarc.UpdateGoogleChannelConfigRequest.serialize,
                    response_deserializer=gce_google_channel_config.GoogleChannelConfig.deserialize,
                )
            )
        return self._stubs["update_google_channel_config"]

    @property
    def get_message_bus(
        self,
    ) -> Callable[[eventarc.GetMessageBusRequest], message_bus.MessageBus]:
        r"""Return a callable for the get message bus method over gRPC.

        Get a single MessageBus.

        Returns:
            Callable[[~.GetMessageBusRequest],
                    ~.MessageBus]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_message_bus" not in self._stubs:
            self._stubs["get_message_bus"] = self._logged_channel.unary_unary(
                "/google.cloud.eventarc.v1.Eventarc/GetMessageBus",
                request_serializer=eventarc.GetMessageBusRequest.serialize,
                response_deserializer=message_bus.MessageBus.deserialize,
            )
        return self._stubs["get_message_bus"]

    @property
    def list_message_buses(
        self,
    ) -> Callable[
        [eventarc.ListMessageBusesRequest], eventarc.ListMessageBusesResponse
    ]:
        r"""Return a callable for the list message buses method over gRPC.

        List message buses.

        Returns:
            Callable[[~.ListMessageBusesRequest],
                    ~.ListMessageBusesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_message_buses" not in self._stubs:
            self._stubs["list_message_buses"] = self._logged_channel.unary_unary(
                "/google.cloud.eventarc.v1.Eventarc/ListMessageBuses",
                request_serializer=eventarc.ListMessageBusesRequest.serialize,
                response_deserializer=eventarc.ListMessageBusesResponse.deserialize,
            )
        return self._stubs["list_message_buses"]

    @property
    def list_message_bus_enrollments(
        self,
    ) -> Callable[
        [eventarc.ListMessageBusEnrollmentsRequest],
        eventarc.ListMessageBusEnrollmentsResponse,
    ]:
        r"""Return a callable for the list message bus enrollments method over gRPC.

        List message bus enrollments.

        Returns:
            Callable[[~.ListMessageBusEnrollmentsRequest],
                    ~.ListMessageBusEnrollmentsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_message_bus_enrollments" not in self._stubs:
            self._stubs["list_message_bus_enrollments"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.eventarc.v1.Eventarc/ListMessageBusEnrollments",
                    request_serializer=eventarc.ListMessageBusEnrollmentsRequest.serialize,
                    response_deserializer=eventarc.ListMessageBusEnrollmentsResponse.deserialize,
                )
            )
        return self._stubs["list_message_bus_enrollments"]

    @property
    def create_message_bus(
        self,
    ) -> Callable[[eventarc.CreateMessageBusRequest], operations_pb2.Operation]:
        r"""Return a callable for the create message bus method over gRPC.

        Create a new MessageBus in a particular project and
        location.

        Returns:
            Callable[[~.CreateMessageBusRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_message_bus" not in self._stubs:
            self._stubs["create_message_bus"] = self._logged_channel.unary_unary(
                "/google.cloud.eventarc.v1.Eventarc/CreateMessageBus",
                request_serializer=eventarc.CreateMessageBusRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_message_bus"]

    @property
    def update_message_bus(
        self,
    ) -> Callable[[eventarc.UpdateMessageBusRequest], operations_pb2.Operation]:
        r"""Return a callable for the update message bus method over gRPC.

        Update a single message bus.

        Returns:
            Callable[[~.UpdateMessageBusRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_message_bus" not in self._stubs:
            self._stubs["update_message_bus"] = self._logged_channel.unary_unary(
                "/google.cloud.eventarc.v1.Eventarc/UpdateMessageBus",
                request_serializer=eventarc.UpdateMessageBusRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_message_bus"]

    @property
    def delete_message_bus(
        self,
    ) -> Callable[[eventarc.DeleteMessageBusRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete message bus method over gRPC.

        Delete a single message bus.

        Returns:
            Callable[[~.DeleteMessageBusRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_message_bus" not in self._stubs:
            self._stubs["delete_message_bus"] = self._logged_channel.unary_unary(
                "/google.cloud.eventarc.v1.Eventarc/DeleteMessageBus",
                request_serializer=eventarc.DeleteMessageBusRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_message_bus"]

    @property
    def get_enrollment(
        self,
    ) -> Callable[[eventarc.GetEnrollmentRequest], enrollment.Enrollment]:
        r"""Return a callable for the get enrollment method over gRPC.

        Get a single Enrollment.

        Returns:
            Callable[[~.GetEnrollmentRequest],
                    ~.Enrollment]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_enrollment" not in self._stubs:
            self._stubs["get_enrollment"] = self._logged_channel.unary_unary(
                "/google.cloud.eventarc.v1.Eventarc/GetEnrollment",
                request_serializer=eventarc.GetEnrollmentRequest.serialize,
                response_deserializer=enrollment.Enrollment.deserialize,
            )
        return self._stubs["get_enrollment"]

    @property
    def list_enrollments(
        self,
    ) -> Callable[[eventarc.ListEnrollmentsRequest], eventarc.ListEnrollmentsResponse]:
        r"""Return a callable for the list enrollments method over gRPC.

        List Enrollments.

        Returns:
            Callable[[~.ListEnrollmentsRequest],
                    ~.ListEnrollmentsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_enrollments" not in self._stubs:
            self._stubs["list_enrollments"] = self._logged_channel.unary_unary(
                "/google.cloud.eventarc.v1.Eventarc/ListEnrollments",
                request_serializer=eventarc.ListEnrollmentsRequest.serialize,
                response_deserializer=eventarc.ListEnrollmentsResponse.deserialize,
            )
        return self._stubs["list_enrollments"]

    @property
    def create_enrollment(
        self,
    ) -> Callable[[eventarc.CreateEnrollmentRequest], operations_pb2.Operation]:
        r"""Return a callable for the create enrollment method over gRPC.

        Create a new Enrollment in a particular project and
        location.

        Returns:
            Callable[[~.CreateEnrollmentRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_enrollment" not in self._stubs:
            self._stubs["create_enrollment"] = self._logged_channel.unary_unary(
                "/google.cloud.eventarc.v1.Eventarc/CreateEnrollment",
                request_serializer=eventarc.CreateEnrollmentRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_enrollment"]

    @property
    def update_enrollment(
        self,
    ) -> Callable[[eventarc.UpdateEnrollmentRequest], operations_pb2.Operation]:
        r"""Return a callable for the update enrollment method over gRPC.

        Update a single Enrollment.

        Returns:
            Callable[[~.UpdateEnrollmentRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_enrollment" not in self._stubs:
            self._stubs["update_enrollment"] = self._logged_channel.unary_unary(
                "/google.cloud.eventarc.v1.Eventarc/UpdateEnrollment",
                request_serializer=eventarc.UpdateEnrollmentRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_enrollment"]

    @property
    def delete_enrollment(
        self,
    ) -> Callable[[eventarc.DeleteEnrollmentRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete enrollment method over gRPC.

        Delete a single Enrollment.

        Returns:
            Callable[[~.DeleteEnrollmentRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_enrollment" not in self._stubs:
            self._stubs["delete_enrollment"] = self._logged_channel.unary_unary(
                "/google.cloud.eventarc.v1.Eventarc/DeleteEnrollment",
                request_serializer=eventarc.DeleteEnrollmentRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_enrollment"]

    @property
    def get_pipeline(
        self,
    ) -> Callable[[eventarc.GetPipelineRequest], pipeline.Pipeline]:
        r"""Return a callable for the get pipeline method over gRPC.

        Get a single Pipeline.

        Returns:
            Callable[[~.GetPipelineRequest],
                    ~.Pipeline]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_pipeline" not in self._stubs:
            self._stubs["get_pipeline"] = self._logged_channel.unary_unary(
                "/google.cloud.eventarc.v1.Eventarc/GetPipeline",
                request_serializer=eventarc.GetPipelineRequest.serialize,
                response_deserializer=pipeline.Pipeline.deserialize,
            )
        return self._stubs["get_pipeline"]

    @property
    def list_pipelines(
        self,
    ) -> Callable[[eventarc.ListPipelinesRequest], eventarc.ListPipelinesResponse]:
        r"""Return a callable for the list pipelines method over gRPC.

        List pipelines.

        Returns:
            Callable[[~.ListPipelinesRequest],
                    ~.ListPipelinesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_pipelines" not in self._stubs:
            self._stubs["list_pipelines"] = self._logged_channel.unary_unary(
                "/google.cloud.eventarc.v1.Eventarc/ListPipelines",
                request_serializer=eventarc.ListPipelinesRequest.serialize,
                response_deserializer=eventarc.ListPipelinesResponse.deserialize,
            )
        return self._stubs["list_pipelines"]

    @property
    def create_pipeline(
        self,
    ) -> Callable[[eventarc.CreatePipelineRequest], operations_pb2.Operation]:
        r"""Return a callable for the create pipeline method over gRPC.

        Create a new Pipeline in a particular project and
        location.

        Returns:
            Callable[[~.CreatePipelineRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_pipeline" not in self._stubs:
            self._stubs["create_pipeline"] = self._logged_channel.unary_unary(
                "/google.cloud.eventarc.v1.Eventarc/CreatePipeline",
                request_serializer=eventarc.CreatePipelineRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_pipeline"]

    @property
    def update_pipeline(
        self,
    ) -> Callable[[eventarc.UpdatePipelineRequest], operations_pb2.Operation]:
        r"""Return a callable for the update pipeline method over gRPC.

        Update a single pipeline.

        Returns:
            Callable[[~.UpdatePipelineRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_pipeline" not in self._stubs:
            self._stubs["update_pipeline"] = self._logged_channel.unary_unary(
                "/google.cloud.eventarc.v1.Eventarc/UpdatePipeline",
                request_serializer=eventarc.UpdatePipelineRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_pipeline"]

    @property
    def delete_pipeline(
        self,
    ) -> Callable[[eventarc.DeletePipelineRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete pipeline method over gRPC.

        Delete a single pipeline.

        Returns:
            Callable[[~.DeletePipelineRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_pipeline" not in self._stubs:
            self._stubs["delete_pipeline"] = self._logged_channel.unary_unary(
                "/google.cloud.eventarc.v1.Eventarc/DeletePipeline",
                request_serializer=eventarc.DeletePipelineRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_pipeline"]

    @property
    def get_google_api_source(
        self,
    ) -> Callable[
        [eventarc.GetGoogleApiSourceRequest], google_api_source.GoogleApiSource
    ]:
        r"""Return a callable for the get google api source method over gRPC.

        Get a single GoogleApiSource.

        Returns:
            Callable[[~.GetGoogleApiSourceRequest],
                    ~.GoogleApiSource]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_google_api_source" not in self._stubs:
            self._stubs["get_google_api_source"] = self._logged_channel.unary_unary(
                "/google.cloud.eventarc.v1.Eventarc/GetGoogleApiSource",
                request_serializer=eventarc.GetGoogleApiSourceRequest.serialize,
                response_deserializer=google_api_source.GoogleApiSource.deserialize,
            )
        return self._stubs["get_google_api_source"]

    @property
    def list_google_api_sources(
        self,
    ) -> Callable[
        [eventarc.ListGoogleApiSourcesRequest], eventarc.ListGoogleApiSourcesResponse
    ]:
        r"""Return a callable for the list google api sources method over gRPC.

        List GoogleApiSources.

        Returns:
            Callable[[~.ListGoogleApiSourcesRequest],
                    ~.ListGoogleApiSourcesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_google_api_sources" not in self._stubs:
            self._stubs["list_google_api_sources"] = self._logged_channel.unary_unary(
                "/google.cloud.eventarc.v1.Eventarc/ListGoogleApiSources",
                request_serializer=eventarc.ListGoogleApiSourcesRequest.serialize,
                response_deserializer=eventarc.ListGoogleApiSourcesResponse.deserialize,
            )
        return self._stubs["list_google_api_sources"]

    @property
    def create_google_api_source(
        self,
    ) -> Callable[[eventarc.CreateGoogleApiSourceRequest], operations_pb2.Operation]:
        r"""Return a callable for the create google api source method over gRPC.

        Create a new GoogleApiSource in a particular project
        and location.

        Returns:
            Callable[[~.CreateGoogleApiSourceRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_google_api_source" not in self._stubs:
            self._stubs["create_google_api_source"] = self._logged_channel.unary_unary(
                "/google.cloud.eventarc.v1.Eventarc/CreateGoogleApiSource",
                request_serializer=eventarc.CreateGoogleApiSourceRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_google_api_source"]

    @property
    def update_google_api_source(
        self,
    ) -> Callable[[eventarc.UpdateGoogleApiSourceRequest], operations_pb2.Operation]:
        r"""Return a callable for the update google api source method over gRPC.

        Update a single GoogleApiSource.

        Returns:
            Callable[[~.UpdateGoogleApiSourceRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_google_api_source" not in self._stubs:
            self._stubs["update_google_api_source"] = self._logged_channel.unary_unary(
                "/google.cloud.eventarc.v1.Eventarc/UpdateGoogleApiSource",
                request_serializer=eventarc.UpdateGoogleApiSourceRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_google_api_source"]

    @property
    def delete_google_api_source(
        self,
    ) -> Callable[[eventarc.DeleteGoogleApiSourceRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete google api source method over gRPC.

        Delete a single GoogleApiSource.

        Returns:
            Callable[[~.DeleteGoogleApiSourceRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_google_api_source" not in self._stubs:
            self._stubs["delete_google_api_source"] = self._logged_channel.unary_unary(
                "/google.cloud.eventarc.v1.Eventarc/DeleteGoogleApiSource",
                request_serializer=eventarc.DeleteGoogleApiSourceRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_google_api_source"]

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


__all__ = ("EventarcGrpcTransport",)
