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
from typing import TYPE_CHECKING

from google.showcase_v1beta1._compat import _observability, apply_channel_interceptors

from google.api_core import client_options as client_options_lib
from google.api_core import grpc_helpers
from google.api_core import operations_v1
from google.api_core import gapic_v1
import google.auth                         # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.protobuf.json_format import MessageToJson
import google.protobuf.message

import grpc  # type: ignore
import proto  # type: ignore

from google.cloud.location import locations_pb2 # type: ignore
from google.iam.v1 import iam_policy_pb2  # type: ignore
from google.iam.v1 import policy_pb2  # type: ignore
from google.longrunning import operations_pb2 # type: ignore
from google.showcase_v1beta1.types import echo as gs_echo
from .base import EchoTransport, DEFAULT_CLIENT_INFO

if TYPE_CHECKING:  # pragma: NO COVER
    # ClientInterceptor was added in google-api-core 2.36.0+; ignore attribute-defined for older api-core versions during type checking
    from google.api_core.grpc_helpers import ClientInterceptor  # type: ignore[attr-defined]

try:
    from google.api_core import client_logging  # type: ignore
    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class _LoggingClientInterceptor(grpc.UnaryUnaryClientInterceptor):  # pragma: NO COVER
    def intercept_unary_unary(self, continuation, client_call_details, request):
        logging_enabled = CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(std_logging.DEBUG)
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
                extra = {
                    "serviceName": "google.showcase.v1beta1.Echo",
                    "rpcName": str(client_call_details.method),
                    "request": grpc_request,
                    "metadata": grpc_request["metadata"],
                },
            )
        response = continuation(client_call_details, request)
        if logging_enabled:  # pragma: NO COVER
            response_metadata = response.trailing_metadata()
            # Convert gRPC metadata `<class 'grpc.aio._metadata.Metadata'>` to list of tuples
            metadata = dict([(k, str(v)) for k, v in response_metadata]) if response_metadata else None
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
                extra = {
                    "serviceName": "google.showcase.v1beta1.Echo",
                    "rpcName": client_call_details.method,
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class EchoGrpcTransport(EchoTransport):
    """gRPC backend transport for Echo.

    This service is used showcase the four main types of rpcs -
    unary, server side streaming, client side streaming, and
    bidirectional streaming. This service also exposes methods that
    explicitly implement server delay, and paginated calls. Set the
    'showcase-trailer' metadata key on any method to have the values
    echoed in the response trailers. Set the 'x-goog-request-params'
    metadata key on any method to have the values echoed in the
    response headers.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """
    _stubs: Dict[str, Callable]

    def __init__(self, *,
            host: str = 'localhost:7469',
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
            interceptors: Optional[Sequence[Union["ClientInterceptor", Callable[[grpc.Channel], grpc.Channel]]]] = None,
            client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = None,
            ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'localhost:7469').
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
            interceptors (Optional[Sequence[Union[ClientInterceptor, Callable[[grpc.Channel], grpc.Channel]]]]):
                Additional interceptors (or callables that apply interceptors) to apply to the
                gRPC channel.
            client_options (Optional[Union[google.api_core.client_options.ClientOptions, dict]]):
                Custom options for the client, containing options such as
                custom OpenTelemetry tracer providers.

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
            client_options=client_options,
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

        channel_interceptors = list(interceptors) if interceptors else []
        if (
            _observability is not None
            and (otel_interceptor := _observability.get_otel_interceptor(self._client_options)) is not None
            and otel_interceptor not in channel_interceptors
            and not any(getattr(i, "_is_otel_interceptor", None) is True for i in channel_interceptors)
        ):
            channel_interceptors.append(otel_interceptor)

        self._grpc_channel = apply_channel_interceptors(self._grpc_channel, channel_interceptors)

        self._interceptor = _LoggingClientInterceptor()
        self._logged_channel = grpc.intercept_channel(self._grpc_channel, self._interceptor)

        # Wrap messages. This must be done after self._logged_channel exists
        self._prep_wrapped_messages(client_info)

    @classmethod
    def create_channel(cls,
                       host: str = 'localhost:7469',
                       credentials: Optional[ga_credentials.Credentials] = None,
                       credentials_file: Optional[str] = None,
                       scopes: Optional[Sequence[str]] = None,
                       quota_project_id: Optional[str] = None,
                       **kwargs) -> grpc.Channel:
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
            **kwargs
        )

    @property
    def grpc_channel(self) -> grpc.Channel:
        """Return the channel designed to connect to this service.
        """
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
    def echo(self) -> Callable[
            [gs_echo.EchoRequest],
            gs_echo.EchoResponse]:
        r"""Return a callable for the echo method over gRPC.

        This method simply echoes the request. This method
        showcases unary RPCs.

        Returns:
            Callable[[~.EchoRequest],
                    ~.EchoResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'echo' not in self._stubs:
            self._stubs['echo'] = self._logged_channel.unary_unary(
                '/google.showcase.v1beta1.Echo/Echo',
                request_serializer=gs_echo.EchoRequest.serialize,
                response_deserializer=gs_echo.EchoResponse.deserialize,
            )
        return self._stubs['echo']

    @property
    def echo_error_details(self) -> Callable[
            [gs_echo.EchoErrorDetailsRequest],
            gs_echo.EchoErrorDetailsResponse]:
        r"""Return a callable for the echo error details method over gRPC.

        This method returns error details in a repeated
        "google.protobuf.Any" field. This method showcases handling
        errors thus encoded, particularly over REST transport. Note that
        GAPICs only allow the type "google.protobuf.Any" for field paths
        ending in "error.details", and, at run-time, the actual types
        for these fields must be one of the types in
        google/rpc/error_details.proto.

        Returns:
            Callable[[~.EchoErrorDetailsRequest],
                    ~.EchoErrorDetailsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'echo_error_details' not in self._stubs:
            self._stubs['echo_error_details'] = self._logged_channel.unary_unary(
                '/google.showcase.v1beta1.Echo/EchoErrorDetails',
                request_serializer=gs_echo.EchoErrorDetailsRequest.serialize,
                response_deserializer=gs_echo.EchoErrorDetailsResponse.deserialize,
            )
        return self._stubs['echo_error_details']

    @property
    def fail_echo_with_details(self) -> Callable[
            [gs_echo.FailEchoWithDetailsRequest],
            gs_echo.FailEchoWithDetailsResponse]:
        r"""Return a callable for the fail echo with details method over gRPC.

        This method always fails with a gRPC "Aborted" error status that
        contains multiple error details. These include one instance of
        each of the standard ones in error_details.proto
        (https://github.com/googleapis/googleapis/blob/master/google/rpc/error_details.proto)
        plus a custom, Showcase-defined PoetryError. The intent of this
        RPC is to verify that GAPICs can process these various error
        details and surface them to the user in an idiomatic form.

        Returns:
            Callable[[~.FailEchoWithDetailsRequest],
                    ~.FailEchoWithDetailsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'fail_echo_with_details' not in self._stubs:
            self._stubs['fail_echo_with_details'] = self._logged_channel.unary_unary(
                '/google.showcase.v1beta1.Echo/FailEchoWithDetails',
                request_serializer=gs_echo.FailEchoWithDetailsRequest.serialize,
                response_deserializer=gs_echo.FailEchoWithDetailsResponse.deserialize,
            )
        return self._stubs['fail_echo_with_details']

    @property
    def expand(self) -> Callable[
            [gs_echo.ExpandRequest],
            gs_echo.EchoResponse]:
        r"""Return a callable for the expand method over gRPC.

        This method splits the given content into words and
        will pass each word back through the stream. This method
        showcases server-side streaming RPCs.

        Returns:
            Callable[[~.ExpandRequest],
                    ~.EchoResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'expand' not in self._stubs:
            self._stubs['expand'] = self._logged_channel.unary_stream(
                '/google.showcase.v1beta1.Echo/Expand',
                request_serializer=gs_echo.ExpandRequest.serialize,
                response_deserializer=gs_echo.EchoResponse.deserialize,
            )
        return self._stubs['expand']

    @property
    def collect(self) -> Callable[
            [gs_echo.EchoRequest],
            gs_echo.EchoResponse]:
        r"""Return a callable for the collect method over gRPC.

        This method will collect the words given to it. When
        the stream is closed by the client, this method will
        return the a concatenation of the strings passed to it.
        This method showcases client-side streaming RPCs.

        Returns:
            Callable[[~.EchoRequest],
                    ~.EchoResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'collect' not in self._stubs:
            self._stubs['collect'] = self._logged_channel.stream_unary(
                '/google.showcase.v1beta1.Echo/Collect',
                request_serializer=gs_echo.EchoRequest.serialize,
                response_deserializer=gs_echo.EchoResponse.deserialize,
            )
        return self._stubs['collect']

    @property
    def chat(self) -> Callable[
            [gs_echo.EchoRequest],
            gs_echo.EchoResponse]:
        r"""Return a callable for the chat method over gRPC.

        This method, upon receiving a request on the stream,
        will pass the same content back on the stream. This
        method showcases bidirectional streaming RPCs.

        Returns:
            Callable[[~.EchoRequest],
                    ~.EchoResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'chat' not in self._stubs:
            self._stubs['chat'] = self._logged_channel.stream_stream(
                '/google.showcase.v1beta1.Echo/Chat',
                request_serializer=gs_echo.EchoRequest.serialize,
                response_deserializer=gs_echo.EchoResponse.deserialize,
            )
        return self._stubs['chat']

    @property
    def paged_expand(self) -> Callable[
            [gs_echo.PagedExpandRequest],
            gs_echo.PagedExpandResponse]:
        r"""Return a callable for the paged expand method over gRPC.

        This is similar to the Expand method but instead of
        returning a stream of expanded words, this method
        returns a paged list of expanded words.

        Returns:
            Callable[[~.PagedExpandRequest],
                    ~.PagedExpandResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'paged_expand' not in self._stubs:
            self._stubs['paged_expand'] = self._logged_channel.unary_unary(
                '/google.showcase.v1beta1.Echo/PagedExpand',
                request_serializer=gs_echo.PagedExpandRequest.serialize,
                response_deserializer=gs_echo.PagedExpandResponse.deserialize,
            )
        return self._stubs['paged_expand']

    @property
    def paged_expand_legacy(self) -> Callable[
            [gs_echo.PagedExpandLegacyRequest],
            gs_echo.PagedExpandResponse]:
        r"""Return a callable for the paged expand legacy method over gRPC.

        This is similar to the PagedExpand except that it uses
        max_results instead of page_size, as some legacy APIs still do.
        New APIs should NOT use this pattern.

        Returns:
            Callable[[~.PagedExpandLegacyRequest],
                    ~.PagedExpandResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'paged_expand_legacy' not in self._stubs:
            self._stubs['paged_expand_legacy'] = self._logged_channel.unary_unary(
                '/google.showcase.v1beta1.Echo/PagedExpandLegacy',
                request_serializer=gs_echo.PagedExpandLegacyRequest.serialize,
                response_deserializer=gs_echo.PagedExpandResponse.deserialize,
            )
        return self._stubs['paged_expand_legacy']

    @property
    def paged_expand_legacy_mapped(self) -> Callable[
            [gs_echo.PagedExpandRequest],
            gs_echo.PagedExpandLegacyMappedResponse]:
        r"""Return a callable for the paged expand legacy mapped method over gRPC.

        This method returns a map containing lists of words that appear
        in the input, keyed by their initial character. The only words
        returned are the ones included in the current page, as
        determined by page_token and page_size, which both refer to the
        word indices in the input. This paging result consisting of a
        map of lists is a pattern used by some legacy APIs. New APIs
        should NOT use this pattern.

        Returns:
            Callable[[~.PagedExpandRequest],
                    ~.PagedExpandLegacyMappedResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'paged_expand_legacy_mapped' not in self._stubs:
            self._stubs['paged_expand_legacy_mapped'] = self._logged_channel.unary_unary(
                '/google.showcase.v1beta1.Echo/PagedExpandLegacyMapped',
                request_serializer=gs_echo.PagedExpandRequest.serialize,
                response_deserializer=gs_echo.PagedExpandLegacyMappedResponse.deserialize,
            )
        return self._stubs['paged_expand_legacy_mapped']

    @property
    def wait(self) -> Callable[
            [gs_echo.WaitRequest],
            operations_pb2.Operation]:
        r"""Return a callable for the wait method over gRPC.

        This method will wait for the requested amount of
        time and then return. This method showcases how a client
        handles a request timeout.

        Returns:
            Callable[[~.WaitRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'wait' not in self._stubs:
            self._stubs['wait'] = self._logged_channel.unary_unary(
                '/google.showcase.v1beta1.Echo/Wait',
                request_serializer=gs_echo.WaitRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs['wait']

    @property
    def block(self) -> Callable[
            [gs_echo.BlockRequest],
            gs_echo.BlockResponse]:
        r"""Return a callable for the block method over gRPC.

        This method will block (wait) for the requested
        amount of time and then return the response or error.
        This method showcases how a client handles delays or
        retries.

        Returns:
            Callable[[~.BlockRequest],
                    ~.BlockResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'block' not in self._stubs:
            self._stubs['block'] = self._logged_channel.unary_unary(
                '/google.showcase.v1beta1.Echo/Block',
                request_serializer=gs_echo.BlockRequest.serialize,
                response_deserializer=gs_echo.BlockResponse.deserialize,
            )
        return self._stubs['block']

    def close(self):
        self._logged_channel.close()

    @property
    def delete_operation(
        self,
    ) -> Callable[[operations_pb2.DeleteOperationRequest], None]:
        r"""Return a callable for the delete_operation method over gRPC.
        """
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
        r"""Return a callable for the cancel_operation method over gRPC.
        """
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
        r"""Return a callable for the get_operation method over gRPC.
        """
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
    ) -> Callable[[operations_pb2.ListOperationsRequest], operations_pb2.ListOperationsResponse]:
        r"""Return a callable for the list_operations method over gRPC.
        """
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
    ) -> Callable[[locations_pb2.ListLocationsRequest], locations_pb2.ListLocationsResponse]:
        r"""Return a callable for the list locations method over gRPC.
        """
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
        r"""Return a callable for the list locations method over gRPC.
        """
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
        [iam_policy_pb2.TestIamPermissionsRequest], iam_policy_pb2.TestIamPermissionsResponse
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


__all__ = (
    'EchoGrpcTransport',
)
