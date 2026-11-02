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
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
import google.protobuf.message
import grpc  # type: ignore
import proto  # type: ignore
from google.api_core import gapic_v1, grpc_helpers, operations_v1
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf.json_format import MessageToJson

from google.cloud.video.live_stream_v1.types import resources, service

from .base import DEFAULT_CLIENT_INFO, LivestreamServiceTransport

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
                    "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
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
                    "serviceName": "google.cloud.video.livestream.v1.LivestreamService",
                    "rpcName": client_call_details.method,
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class LivestreamServiceGrpcTransport(LivestreamServiceTransport):
    """gRPC backend transport for LivestreamService.

    Using Live Stream API, you can generate live streams in the
    various renditions and streaming formats. The streaming format
    include HTTP Live Streaming (HLS) and Dynamic Adaptive Streaming
    over HTTP (DASH). You can send a source stream in the various
    ways, including Real-Time Messaging Protocol (RTMP) and Secure
    Reliable Transport (SRT).

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
        host: str = "livestream.googleapis.com",
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
                 The hostname to connect to (default: 'livestream.googleapis.com').
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
        host: str = "livestream.googleapis.com",
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
    def create_channel_(
        self,
    ) -> Callable[[service.CreateChannelRequest], operations_pb2.Operation]:
        r"""Return a callable for the create channel method over gRPC.

        Creates a channel with the provided unique ID in the
        specified region.

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
                "/google.cloud.video.livestream.v1.LivestreamService/CreateChannel",
                request_serializer=service.CreateChannelRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_channel_"]

    @property
    def list_channels(
        self,
    ) -> Callable[[service.ListChannelsRequest], service.ListChannelsResponse]:
        r"""Return a callable for the list channels method over gRPC.

        Returns a list of all channels in the specified
        region.

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
                "/google.cloud.video.livestream.v1.LivestreamService/ListChannels",
                request_serializer=service.ListChannelsRequest.serialize,
                response_deserializer=service.ListChannelsResponse.deserialize,
            )
        return self._stubs["list_channels"]

    @property
    def get_channel(self) -> Callable[[service.GetChannelRequest], resources.Channel]:
        r"""Return a callable for the get channel method over gRPC.

        Returns the specified channel.

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
                "/google.cloud.video.livestream.v1.LivestreamService/GetChannel",
                request_serializer=service.GetChannelRequest.serialize,
                response_deserializer=resources.Channel.deserialize,
            )
        return self._stubs["get_channel"]

    @property
    def delete_channel(
        self,
    ) -> Callable[[service.DeleteChannelRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete channel method over gRPC.

        Deletes the specified channel.

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
                "/google.cloud.video.livestream.v1.LivestreamService/DeleteChannel",
                request_serializer=service.DeleteChannelRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_channel"]

    @property
    def update_channel(
        self,
    ) -> Callable[[service.UpdateChannelRequest], operations_pb2.Operation]:
        r"""Return a callable for the update channel method over gRPC.

        Updates the specified channel.

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
                "/google.cloud.video.livestream.v1.LivestreamService/UpdateChannel",
                request_serializer=service.UpdateChannelRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_channel"]

    @property
    def start_channel(
        self,
    ) -> Callable[[service.StartChannelRequest], operations_pb2.Operation]:
        r"""Return a callable for the start channel method over gRPC.

        Starts the specified channel. Part of the video
        pipeline will be created only when the StartChannel
        request is received by the server.

        Returns:
            Callable[[~.StartChannelRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "start_channel" not in self._stubs:
            self._stubs["start_channel"] = self._logged_channel.unary_unary(
                "/google.cloud.video.livestream.v1.LivestreamService/StartChannel",
                request_serializer=service.StartChannelRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["start_channel"]

    @property
    def stop_channel(
        self,
    ) -> Callable[[service.StopChannelRequest], operations_pb2.Operation]:
        r"""Return a callable for the stop channel method over gRPC.

        Stops the specified channel. Part of the video
        pipeline will be released when the StopChannel request
        is received by the server.

        Returns:
            Callable[[~.StopChannelRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "stop_channel" not in self._stubs:
            self._stubs["stop_channel"] = self._logged_channel.unary_unary(
                "/google.cloud.video.livestream.v1.LivestreamService/StopChannel",
                request_serializer=service.StopChannelRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["stop_channel"]

    @property
    def start_distribution(
        self,
    ) -> Callable[[service.StartDistributionRequest], operations_pb2.Operation]:
        r"""Return a callable for the start distribution method over gRPC.

        Starts distribution which delivers outputs to the
        destination indicated by the Distribution configuration.

        Returns:
            Callable[[~.StartDistributionRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "start_distribution" not in self._stubs:
            self._stubs["start_distribution"] = self._logged_channel.unary_unary(
                "/google.cloud.video.livestream.v1.LivestreamService/StartDistribution",
                request_serializer=service.StartDistributionRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["start_distribution"]

    @property
    def stop_distribution(
        self,
    ) -> Callable[[service.StopDistributionRequest], operations_pb2.Operation]:
        r"""Return a callable for the stop distribution method over gRPC.

        Stops the specified distribution.

        Returns:
            Callable[[~.StopDistributionRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "stop_distribution" not in self._stubs:
            self._stubs["stop_distribution"] = self._logged_channel.unary_unary(
                "/google.cloud.video.livestream.v1.LivestreamService/StopDistribution",
                request_serializer=service.StopDistributionRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["stop_distribution"]

    @property
    def create_input(
        self,
    ) -> Callable[[service.CreateInputRequest], operations_pb2.Operation]:
        r"""Return a callable for the create input method over gRPC.

        Creates an input with the provided unique ID in the
        specified region.

        Returns:
            Callable[[~.CreateInputRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_input" not in self._stubs:
            self._stubs["create_input"] = self._logged_channel.unary_unary(
                "/google.cloud.video.livestream.v1.LivestreamService/CreateInput",
                request_serializer=service.CreateInputRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_input"]

    @property
    def list_inputs(
        self,
    ) -> Callable[[service.ListInputsRequest], service.ListInputsResponse]:
        r"""Return a callable for the list inputs method over gRPC.

        Returns a list of all inputs in the specified region.

        Returns:
            Callable[[~.ListInputsRequest],
                    ~.ListInputsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_inputs" not in self._stubs:
            self._stubs["list_inputs"] = self._logged_channel.unary_unary(
                "/google.cloud.video.livestream.v1.LivestreamService/ListInputs",
                request_serializer=service.ListInputsRequest.serialize,
                response_deserializer=service.ListInputsResponse.deserialize,
            )
        return self._stubs["list_inputs"]

    @property
    def get_input(self) -> Callable[[service.GetInputRequest], resources.Input]:
        r"""Return a callable for the get input method over gRPC.

        Returns the specified input.

        Returns:
            Callable[[~.GetInputRequest],
                    ~.Input]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_input" not in self._stubs:
            self._stubs["get_input"] = self._logged_channel.unary_unary(
                "/google.cloud.video.livestream.v1.LivestreamService/GetInput",
                request_serializer=service.GetInputRequest.serialize,
                response_deserializer=resources.Input.deserialize,
            )
        return self._stubs["get_input"]

    @property
    def delete_input(
        self,
    ) -> Callable[[service.DeleteInputRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete input method over gRPC.

        Deletes the specified input.

        Returns:
            Callable[[~.DeleteInputRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_input" not in self._stubs:
            self._stubs["delete_input"] = self._logged_channel.unary_unary(
                "/google.cloud.video.livestream.v1.LivestreamService/DeleteInput",
                request_serializer=service.DeleteInputRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_input"]

    @property
    def update_input(
        self,
    ) -> Callable[[service.UpdateInputRequest], operations_pb2.Operation]:
        r"""Return a callable for the update input method over gRPC.

        Updates the specified input.

        Returns:
            Callable[[~.UpdateInputRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_input" not in self._stubs:
            self._stubs["update_input"] = self._logged_channel.unary_unary(
                "/google.cloud.video.livestream.v1.LivestreamService/UpdateInput",
                request_serializer=service.UpdateInputRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_input"]

    @property
    def preview_input(
        self,
    ) -> Callable[[service.PreviewInputRequest], service.PreviewInputResponse]:
        r"""Return a callable for the preview input method over gRPC.

        Preview the streaming content of the specified input.

        Returns:
            Callable[[~.PreviewInputRequest],
                    ~.PreviewInputResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "preview_input" not in self._stubs:
            self._stubs["preview_input"] = self._logged_channel.unary_unary(
                "/google.cloud.video.livestream.v1.LivestreamService/PreviewInput",
                request_serializer=service.PreviewInputRequest.serialize,
                response_deserializer=service.PreviewInputResponse.deserialize,
            )
        return self._stubs["preview_input"]

    @property
    def create_event(self) -> Callable[[service.CreateEventRequest], resources.Event]:
        r"""Return a callable for the create event method over gRPC.

        Creates an event with the provided unique ID in the
        specified channel.

        Returns:
            Callable[[~.CreateEventRequest],
                    ~.Event]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_event" not in self._stubs:
            self._stubs["create_event"] = self._logged_channel.unary_unary(
                "/google.cloud.video.livestream.v1.LivestreamService/CreateEvent",
                request_serializer=service.CreateEventRequest.serialize,
                response_deserializer=resources.Event.deserialize,
            )
        return self._stubs["create_event"]

    @property
    def list_events(
        self,
    ) -> Callable[[service.ListEventsRequest], service.ListEventsResponse]:
        r"""Return a callable for the list events method over gRPC.

        Returns a list of all events in the specified
        channel.

        Returns:
            Callable[[~.ListEventsRequest],
                    ~.ListEventsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_events" not in self._stubs:
            self._stubs["list_events"] = self._logged_channel.unary_unary(
                "/google.cloud.video.livestream.v1.LivestreamService/ListEvents",
                request_serializer=service.ListEventsRequest.serialize,
                response_deserializer=service.ListEventsResponse.deserialize,
            )
        return self._stubs["list_events"]

    @property
    def get_event(self) -> Callable[[service.GetEventRequest], resources.Event]:
        r"""Return a callable for the get event method over gRPC.

        Returns the specified event.

        Returns:
            Callable[[~.GetEventRequest],
                    ~.Event]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_event" not in self._stubs:
            self._stubs["get_event"] = self._logged_channel.unary_unary(
                "/google.cloud.video.livestream.v1.LivestreamService/GetEvent",
                request_serializer=service.GetEventRequest.serialize,
                response_deserializer=resources.Event.deserialize,
            )
        return self._stubs["get_event"]

    @property
    def delete_event(self) -> Callable[[service.DeleteEventRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete event method over gRPC.

        Deletes the specified event.

        Returns:
            Callable[[~.DeleteEventRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_event" not in self._stubs:
            self._stubs["delete_event"] = self._logged_channel.unary_unary(
                "/google.cloud.video.livestream.v1.LivestreamService/DeleteEvent",
                request_serializer=service.DeleteEventRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_event"]

    @property
    def list_clips(
        self,
    ) -> Callable[[service.ListClipsRequest], service.ListClipsResponse]:
        r"""Return a callable for the list clips method over gRPC.

        Returns a list of all clips in the specified channel.

        Returns:
            Callable[[~.ListClipsRequest],
                    ~.ListClipsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_clips" not in self._stubs:
            self._stubs["list_clips"] = self._logged_channel.unary_unary(
                "/google.cloud.video.livestream.v1.LivestreamService/ListClips",
                request_serializer=service.ListClipsRequest.serialize,
                response_deserializer=service.ListClipsResponse.deserialize,
            )
        return self._stubs["list_clips"]

    @property
    def get_clip(self) -> Callable[[service.GetClipRequest], resources.Clip]:
        r"""Return a callable for the get clip method over gRPC.

        Returns the specified clip.

        Returns:
            Callable[[~.GetClipRequest],
                    ~.Clip]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_clip" not in self._stubs:
            self._stubs["get_clip"] = self._logged_channel.unary_unary(
                "/google.cloud.video.livestream.v1.LivestreamService/GetClip",
                request_serializer=service.GetClipRequest.serialize,
                response_deserializer=resources.Clip.deserialize,
            )
        return self._stubs["get_clip"]

    @property
    def create_clip(
        self,
    ) -> Callable[[service.CreateClipRequest], operations_pb2.Operation]:
        r"""Return a callable for the create clip method over gRPC.

        Creates a clip with the provided clip ID in the
        specified channel.

        Returns:
            Callable[[~.CreateClipRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_clip" not in self._stubs:
            self._stubs["create_clip"] = self._logged_channel.unary_unary(
                "/google.cloud.video.livestream.v1.LivestreamService/CreateClip",
                request_serializer=service.CreateClipRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_clip"]

    @property
    def delete_clip(
        self,
    ) -> Callable[[service.DeleteClipRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete clip method over gRPC.

        Deletes the specified clip job resource. This method
        only deletes the clip job and does not delete the VOD
        clip stored in Cloud Storage.

        Returns:
            Callable[[~.DeleteClipRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_clip" not in self._stubs:
            self._stubs["delete_clip"] = self._logged_channel.unary_unary(
                "/google.cloud.video.livestream.v1.LivestreamService/DeleteClip",
                request_serializer=service.DeleteClipRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_clip"]

    @property
    def create_dvr_session(
        self,
    ) -> Callable[[service.CreateDvrSessionRequest], operations_pb2.Operation]:
        r"""Return a callable for the create dvr session method over gRPC.

        Creates a DVR session with the provided unique ID in
        the specified channel.

        Returns:
            Callable[[~.CreateDvrSessionRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_dvr_session" not in self._stubs:
            self._stubs["create_dvr_session"] = self._logged_channel.unary_unary(
                "/google.cloud.video.livestream.v1.LivestreamService/CreateDvrSession",
                request_serializer=service.CreateDvrSessionRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_dvr_session"]

    @property
    def list_dvr_sessions(
        self,
    ) -> Callable[[service.ListDvrSessionsRequest], service.ListDvrSessionsResponse]:
        r"""Return a callable for the list dvr sessions method over gRPC.

        Returns a list of all DVR sessions in the specified
        channel.

        Returns:
            Callable[[~.ListDvrSessionsRequest],
                    ~.ListDvrSessionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_dvr_sessions" not in self._stubs:
            self._stubs["list_dvr_sessions"] = self._logged_channel.unary_unary(
                "/google.cloud.video.livestream.v1.LivestreamService/ListDvrSessions",
                request_serializer=service.ListDvrSessionsRequest.serialize,
                response_deserializer=service.ListDvrSessionsResponse.deserialize,
            )
        return self._stubs["list_dvr_sessions"]

    @property
    def get_dvr_session(
        self,
    ) -> Callable[[service.GetDvrSessionRequest], resources.DvrSession]:
        r"""Return a callable for the get dvr session method over gRPC.

        Returns the specified DVR session.

        Returns:
            Callable[[~.GetDvrSessionRequest],
                    ~.DvrSession]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_dvr_session" not in self._stubs:
            self._stubs["get_dvr_session"] = self._logged_channel.unary_unary(
                "/google.cloud.video.livestream.v1.LivestreamService/GetDvrSession",
                request_serializer=service.GetDvrSessionRequest.serialize,
                response_deserializer=resources.DvrSession.deserialize,
            )
        return self._stubs["get_dvr_session"]

    @property
    def delete_dvr_session(
        self,
    ) -> Callable[[service.DeleteDvrSessionRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete dvr session method over gRPC.

        Deletes the specified DVR session.

        Returns:
            Callable[[~.DeleteDvrSessionRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_dvr_session" not in self._stubs:
            self._stubs["delete_dvr_session"] = self._logged_channel.unary_unary(
                "/google.cloud.video.livestream.v1.LivestreamService/DeleteDvrSession",
                request_serializer=service.DeleteDvrSessionRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_dvr_session"]

    @property
    def update_dvr_session(
        self,
    ) -> Callable[[service.UpdateDvrSessionRequest], operations_pb2.Operation]:
        r"""Return a callable for the update dvr session method over gRPC.

        Updates the specified DVR session.

        Returns:
            Callable[[~.UpdateDvrSessionRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_dvr_session" not in self._stubs:
            self._stubs["update_dvr_session"] = self._logged_channel.unary_unary(
                "/google.cloud.video.livestream.v1.LivestreamService/UpdateDvrSession",
                request_serializer=service.UpdateDvrSessionRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_dvr_session"]

    @property
    def create_asset(
        self,
    ) -> Callable[[service.CreateAssetRequest], operations_pb2.Operation]:
        r"""Return a callable for the create asset method over gRPC.

        Creates a Asset with the provided unique ID in the
        specified region.

        Returns:
            Callable[[~.CreateAssetRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_asset" not in self._stubs:
            self._stubs["create_asset"] = self._logged_channel.unary_unary(
                "/google.cloud.video.livestream.v1.LivestreamService/CreateAsset",
                request_serializer=service.CreateAssetRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_asset"]

    @property
    def delete_asset(
        self,
    ) -> Callable[[service.DeleteAssetRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete asset method over gRPC.

        Deletes the specified asset if it is not used.

        Returns:
            Callable[[~.DeleteAssetRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_asset" not in self._stubs:
            self._stubs["delete_asset"] = self._logged_channel.unary_unary(
                "/google.cloud.video.livestream.v1.LivestreamService/DeleteAsset",
                request_serializer=service.DeleteAssetRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_asset"]

    @property
    def get_asset(self) -> Callable[[service.GetAssetRequest], resources.Asset]:
        r"""Return a callable for the get asset method over gRPC.

        Returns the specified asset.

        Returns:
            Callable[[~.GetAssetRequest],
                    ~.Asset]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_asset" not in self._stubs:
            self._stubs["get_asset"] = self._logged_channel.unary_unary(
                "/google.cloud.video.livestream.v1.LivestreamService/GetAsset",
                request_serializer=service.GetAssetRequest.serialize,
                response_deserializer=resources.Asset.deserialize,
            )
        return self._stubs["get_asset"]

    @property
    def list_assets(
        self,
    ) -> Callable[[service.ListAssetsRequest], service.ListAssetsResponse]:
        r"""Return a callable for the list assets method over gRPC.

        Returns a list of all assets in the specified region.

        Returns:
            Callable[[~.ListAssetsRequest],
                    ~.ListAssetsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_assets" not in self._stubs:
            self._stubs["list_assets"] = self._logged_channel.unary_unary(
                "/google.cloud.video.livestream.v1.LivestreamService/ListAssets",
                request_serializer=service.ListAssetsRequest.serialize,
                response_deserializer=service.ListAssetsResponse.deserialize,
            )
        return self._stubs["list_assets"]

    @property
    def get_pool(self) -> Callable[[service.GetPoolRequest], resources.Pool]:
        r"""Return a callable for the get pool method over gRPC.

        Returns the specified pool.

        Returns:
            Callable[[~.GetPoolRequest],
                    ~.Pool]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_pool" not in self._stubs:
            self._stubs["get_pool"] = self._logged_channel.unary_unary(
                "/google.cloud.video.livestream.v1.LivestreamService/GetPool",
                request_serializer=service.GetPoolRequest.serialize,
                response_deserializer=resources.Pool.deserialize,
            )
        return self._stubs["get_pool"]

    @property
    def update_pool(
        self,
    ) -> Callable[[service.UpdatePoolRequest], operations_pb2.Operation]:
        r"""Return a callable for the update pool method over gRPC.

        Updates the specified pool.

        Returns:
            Callable[[~.UpdatePoolRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_pool" not in self._stubs:
            self._stubs["update_pool"] = self._logged_channel.unary_unary(
                "/google.cloud.video.livestream.v1.LivestreamService/UpdatePool",
                request_serializer=service.UpdatePoolRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_pool"]

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
    def kind(self) -> str:
        return "grpc"


__all__ = ("LivestreamServiceGrpcTransport",)
