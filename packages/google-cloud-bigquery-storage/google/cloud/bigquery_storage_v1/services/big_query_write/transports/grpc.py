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
from google.api_core import gapic_v1, grpc_helpers
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.protobuf.json_format import MessageToJson

from google.cloud.bigquery_storage_v1.types import storage, stream

from .base import DEFAULT_CLIENT_INFO, BigQueryWriteTransport

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
                    "serviceName": "google.cloud.bigquery.storage.v1.BigQueryWrite",
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
                    "serviceName": "google.cloud.bigquery.storage.v1.BigQueryWrite",
                    "rpcName": client_call_details.method,
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class BigQueryWriteGrpcTransport(BigQueryWriteTransport):
    """gRPC backend transport for BigQueryWrite.

    BigQuery Write API.

    The Write API can be used to write data to BigQuery.

    For supplementary information about the Write API, see:

    https://cloud.google.com/bigquery/docs/write-api

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
        host: str = "bigquerystorage.googleapis.com",
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
                 The hostname to connect to (default: 'bigquerystorage.googleapis.com').
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
        host: str = "bigquerystorage.googleapis.com",
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
    def create_write_stream(
        self,
    ) -> Callable[[storage.CreateWriteStreamRequest], stream.WriteStream]:
        r"""Return a callable for the create write stream method over gRPC.

        Creates a write stream to the given table. Additionally, every
        table has a special stream named '\_default' to which data can
        be written. This stream doesn't need to be created using
        CreateWriteStream. It is a stream that can be used
        simultaneously by any number of clients. Data written to this
        stream is considered committed as soon as an acknowledgement is
        received.

        Returns:
            Callable[[~.CreateWriteStreamRequest],
                    ~.WriteStream]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_write_stream" not in self._stubs:
            self._stubs["create_write_stream"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.storage.v1.BigQueryWrite/CreateWriteStream",
                request_serializer=storage.CreateWriteStreamRequest.serialize,
                response_deserializer=stream.WriteStream.deserialize,
            )
        return self._stubs["create_write_stream"]

    @property
    def append_rows(
        self,
    ) -> Callable[[storage.AppendRowsRequest], storage.AppendRowsResponse]:
        r"""Return a callable for the append rows method over gRPC.

        Appends data to the given stream.

        If ``offset`` is specified, the ``offset`` is checked against
        the end of stream. The server returns ``OUT_OF_RANGE`` in
        ``AppendRowsResponse`` if an attempt is made to append to an
        offset beyond the current end of the stream or
        ``ALREADY_EXISTS`` if user provides an ``offset`` that has
        already been written to. User can retry with adjusted offset
        within the same RPC connection. If ``offset`` is not specified,
        append happens at the end of the stream.

        The response contains an optional offset at which the append
        happened. No offset information will be returned for appends to
        a default stream.

        Responses are received in the same order in which requests are
        sent. There will be one response for each successful inserted
        request. Responses may optionally embed error information if the
        originating AppendRequest was not successfully processed.

        The specifics of when successfully appended data is made visible
        to the table are governed by the type of stream:

        - For COMMITTED streams (which includes the default stream),
          data is visible immediately upon successful append.

        - For BUFFERED streams, data is made visible via a subsequent
          ``FlushRows`` rpc which advances a cursor to a newer offset in
          the stream.

        - For PENDING streams, data is not made visible until the stream
          itself is finalized (via the ``FinalizeWriteStream`` rpc), and
          the stream is explicitly committed via the
          ``BatchCommitWriteStreams`` rpc.

        Returns:
            Callable[[~.AppendRowsRequest],
                    ~.AppendRowsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "append_rows" not in self._stubs:
            self._stubs["append_rows"] = self._logged_channel.stream_stream(
                "/google.cloud.bigquery.storage.v1.BigQueryWrite/AppendRows",
                request_serializer=storage.AppendRowsRequest.serialize,
                response_deserializer=storage.AppendRowsResponse.deserialize,
            )
        return self._stubs["append_rows"]

    @property
    def get_write_stream(
        self,
    ) -> Callable[[storage.GetWriteStreamRequest], stream.WriteStream]:
        r"""Return a callable for the get write stream method over gRPC.

        Gets information about a write stream.

        Returns:
            Callable[[~.GetWriteStreamRequest],
                    ~.WriteStream]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_write_stream" not in self._stubs:
            self._stubs["get_write_stream"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.storage.v1.BigQueryWrite/GetWriteStream",
                request_serializer=storage.GetWriteStreamRequest.serialize,
                response_deserializer=stream.WriteStream.deserialize,
            )
        return self._stubs["get_write_stream"]

    @property
    def finalize_write_stream(
        self,
    ) -> Callable[
        [storage.FinalizeWriteStreamRequest], storage.FinalizeWriteStreamResponse
    ]:
        r"""Return a callable for the finalize write stream method over gRPC.

        Finalize a write stream so that no new data can be appended to
        the stream. Finalize is not supported on the '\_default' stream.

        Returns:
            Callable[[~.FinalizeWriteStreamRequest],
                    ~.FinalizeWriteStreamResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "finalize_write_stream" not in self._stubs:
            self._stubs["finalize_write_stream"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.storage.v1.BigQueryWrite/FinalizeWriteStream",
                request_serializer=storage.FinalizeWriteStreamRequest.serialize,
                response_deserializer=storage.FinalizeWriteStreamResponse.deserialize,
            )
        return self._stubs["finalize_write_stream"]

    @property
    def batch_commit_write_streams(
        self,
    ) -> Callable[
        [storage.BatchCommitWriteStreamsRequest],
        storage.BatchCommitWriteStreamsResponse,
    ]:
        r"""Return a callable for the batch commit write streams method over gRPC.

        Atomically commits a group of ``PENDING`` streams that belong to
        the same ``parent`` table.

        Streams must be finalized before commit and cannot be committed
        multiple times. Once a stream is committed, data in the stream
        becomes available for read operations.

        Returns:
            Callable[[~.BatchCommitWriteStreamsRequest],
                    ~.BatchCommitWriteStreamsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "batch_commit_write_streams" not in self._stubs:
            self._stubs["batch_commit_write_streams"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.bigquery.storage.v1.BigQueryWrite/BatchCommitWriteStreams",
                    request_serializer=storage.BatchCommitWriteStreamsRequest.serialize,
                    response_deserializer=storage.BatchCommitWriteStreamsResponse.deserialize,
                )
            )
        return self._stubs["batch_commit_write_streams"]

    @property
    def flush_rows(
        self,
    ) -> Callable[[storage.FlushRowsRequest], storage.FlushRowsResponse]:
        r"""Return a callable for the flush rows method over gRPC.

        Flushes rows to a BUFFERED stream.

        If users are appending rows to BUFFERED stream, flush operation
        is required in order for the rows to become available for
        reading. A Flush operation flushes up to any previously flushed
        offset in a BUFFERED stream, to the offset specified in the
        request.

        Flush is not supported on the \_default stream, since it is not
        BUFFERED.

        Returns:
            Callable[[~.FlushRowsRequest],
                    ~.FlushRowsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "flush_rows" not in self._stubs:
            self._stubs["flush_rows"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.storage.v1.BigQueryWrite/FlushRows",
                request_serializer=storage.FlushRowsRequest.serialize,
                response_deserializer=storage.FlushRowsResponse.deserialize,
            )
        return self._stubs["flush_rows"]

    def close(self):
        self._logged_channel.close()

    @property
    def kind(self) -> str:
        return "grpc"


__all__ = ("BigQueryWriteGrpcTransport",)
