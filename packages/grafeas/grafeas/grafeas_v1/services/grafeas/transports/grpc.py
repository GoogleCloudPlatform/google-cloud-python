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
from google.api_core import gapic_v1, grpc_helpers
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.protobuf.json_format import MessageToJson

from grafeas.grafeas_v1.types import grafeas

from .base import DEFAULT_CLIENT_INFO, GrafeasTransport

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
                    "serviceName": "grafeas.v1.Grafeas",
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
                    "serviceName": "grafeas.v1.Grafeas",
                    "rpcName": client_call_details.method,
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class GrafeasGrpcTransport(GrafeasTransport):
    """gRPC backend transport for Grafeas.

    `Grafeas <https://grafeas.io>`__ API.

    Retrieves analysis results of Cloud components such as Docker
    container images.

    Analysis results are stored as a series of occurrences. An
    ``Occurrence`` contains information about a specific analysis
    instance on a resource. An occurrence refers to a ``Note``. A note
    contains details describing the analysis and is generally stored in
    a separate project, called a ``Provider``. Multiple occurrences can
    refer to the same note.

    For example, an SSL vulnerability could affect multiple images. In
    this case, there would be one note for the vulnerability and an
    occurrence for each image with the vulnerability referring to that
    note.

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
        host: str = "",
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
                 The hostname to connect to (default: '').
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
        host: str = "",
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
    def get_occurrence(
        self,
    ) -> Callable[[grafeas.GetOccurrenceRequest], grafeas.Occurrence]:
        r"""Return a callable for the get occurrence method over gRPC.

        Gets the specified occurrence.

        Returns:
            Callable[[~.GetOccurrenceRequest],
                    ~.Occurrence]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_occurrence" not in self._stubs:
            self._stubs["get_occurrence"] = self._logged_channel.unary_unary(
                "/grafeas.v1.Grafeas/GetOccurrence",
                request_serializer=grafeas.GetOccurrenceRequest.serialize,
                response_deserializer=grafeas.Occurrence.deserialize,
            )
        return self._stubs["get_occurrence"]

    @property
    def list_occurrences(
        self,
    ) -> Callable[[grafeas.ListOccurrencesRequest], grafeas.ListOccurrencesResponse]:
        r"""Return a callable for the list occurrences method over gRPC.

        Lists occurrences for the specified project.

        Returns:
            Callable[[~.ListOccurrencesRequest],
                    ~.ListOccurrencesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_occurrences" not in self._stubs:
            self._stubs["list_occurrences"] = self._logged_channel.unary_unary(
                "/grafeas.v1.Grafeas/ListOccurrences",
                request_serializer=grafeas.ListOccurrencesRequest.serialize,
                response_deserializer=grafeas.ListOccurrencesResponse.deserialize,
            )
        return self._stubs["list_occurrences"]

    @property
    def delete_occurrence(
        self,
    ) -> Callable[[grafeas.DeleteOccurrenceRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete occurrence method over gRPC.

        Deletes the specified occurrence. For example, use
        this method to delete an occurrence when the occurrence
        is no longer applicable for the given resource.

        Returns:
            Callable[[~.DeleteOccurrenceRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_occurrence" not in self._stubs:
            self._stubs["delete_occurrence"] = self._logged_channel.unary_unary(
                "/grafeas.v1.Grafeas/DeleteOccurrence",
                request_serializer=grafeas.DeleteOccurrenceRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_occurrence"]

    @property
    def create_occurrence(
        self,
    ) -> Callable[[grafeas.CreateOccurrenceRequest], grafeas.Occurrence]:
        r"""Return a callable for the create occurrence method over gRPC.

        Creates a new occurrence.

        Returns:
            Callable[[~.CreateOccurrenceRequest],
                    ~.Occurrence]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_occurrence" not in self._stubs:
            self._stubs["create_occurrence"] = self._logged_channel.unary_unary(
                "/grafeas.v1.Grafeas/CreateOccurrence",
                request_serializer=grafeas.CreateOccurrenceRequest.serialize,
                response_deserializer=grafeas.Occurrence.deserialize,
            )
        return self._stubs["create_occurrence"]

    @property
    def batch_create_occurrences(
        self,
    ) -> Callable[
        [grafeas.BatchCreateOccurrencesRequest], grafeas.BatchCreateOccurrencesResponse
    ]:
        r"""Return a callable for the batch create occurrences method over gRPC.

        Creates new occurrences in batch.

        Returns:
            Callable[[~.BatchCreateOccurrencesRequest],
                    ~.BatchCreateOccurrencesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "batch_create_occurrences" not in self._stubs:
            self._stubs["batch_create_occurrences"] = self._logged_channel.unary_unary(
                "/grafeas.v1.Grafeas/BatchCreateOccurrences",
                request_serializer=grafeas.BatchCreateOccurrencesRequest.serialize,
                response_deserializer=grafeas.BatchCreateOccurrencesResponse.deserialize,
            )
        return self._stubs["batch_create_occurrences"]

    @property
    def update_occurrence(
        self,
    ) -> Callable[[grafeas.UpdateOccurrenceRequest], grafeas.Occurrence]:
        r"""Return a callable for the update occurrence method over gRPC.

        Updates the specified occurrence.

        Returns:
            Callable[[~.UpdateOccurrenceRequest],
                    ~.Occurrence]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_occurrence" not in self._stubs:
            self._stubs["update_occurrence"] = self._logged_channel.unary_unary(
                "/grafeas.v1.Grafeas/UpdateOccurrence",
                request_serializer=grafeas.UpdateOccurrenceRequest.serialize,
                response_deserializer=grafeas.Occurrence.deserialize,
            )
        return self._stubs["update_occurrence"]

    @property
    def get_occurrence_note(
        self,
    ) -> Callable[[grafeas.GetOccurrenceNoteRequest], grafeas.Note]:
        r"""Return a callable for the get occurrence note method over gRPC.

        Gets the note attached to the specified occurrence.
        Consumer projects can use this method to get a note that
        belongs to a provider project.

        Returns:
            Callable[[~.GetOccurrenceNoteRequest],
                    ~.Note]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_occurrence_note" not in self._stubs:
            self._stubs["get_occurrence_note"] = self._logged_channel.unary_unary(
                "/grafeas.v1.Grafeas/GetOccurrenceNote",
                request_serializer=grafeas.GetOccurrenceNoteRequest.serialize,
                response_deserializer=grafeas.Note.deserialize,
            )
        return self._stubs["get_occurrence_note"]

    @property
    def get_note(self) -> Callable[[grafeas.GetNoteRequest], grafeas.Note]:
        r"""Return a callable for the get note method over gRPC.

        Gets the specified note.

        Returns:
            Callable[[~.GetNoteRequest],
                    ~.Note]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_note" not in self._stubs:
            self._stubs["get_note"] = self._logged_channel.unary_unary(
                "/grafeas.v1.Grafeas/GetNote",
                request_serializer=grafeas.GetNoteRequest.serialize,
                response_deserializer=grafeas.Note.deserialize,
            )
        return self._stubs["get_note"]

    @property
    def list_notes(
        self,
    ) -> Callable[[grafeas.ListNotesRequest], grafeas.ListNotesResponse]:
        r"""Return a callable for the list notes method over gRPC.

        Lists notes for the specified project.

        Returns:
            Callable[[~.ListNotesRequest],
                    ~.ListNotesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_notes" not in self._stubs:
            self._stubs["list_notes"] = self._logged_channel.unary_unary(
                "/grafeas.v1.Grafeas/ListNotes",
                request_serializer=grafeas.ListNotesRequest.serialize,
                response_deserializer=grafeas.ListNotesResponse.deserialize,
            )
        return self._stubs["list_notes"]

    @property
    def delete_note(self) -> Callable[[grafeas.DeleteNoteRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete note method over gRPC.

        Deletes the specified note.

        Returns:
            Callable[[~.DeleteNoteRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_note" not in self._stubs:
            self._stubs["delete_note"] = self._logged_channel.unary_unary(
                "/grafeas.v1.Grafeas/DeleteNote",
                request_serializer=grafeas.DeleteNoteRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_note"]

    @property
    def create_note(self) -> Callable[[grafeas.CreateNoteRequest], grafeas.Note]:
        r"""Return a callable for the create note method over gRPC.

        Creates a new note.

        Returns:
            Callable[[~.CreateNoteRequest],
                    ~.Note]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_note" not in self._stubs:
            self._stubs["create_note"] = self._logged_channel.unary_unary(
                "/grafeas.v1.Grafeas/CreateNote",
                request_serializer=grafeas.CreateNoteRequest.serialize,
                response_deserializer=grafeas.Note.deserialize,
            )
        return self._stubs["create_note"]

    @property
    def batch_create_notes(
        self,
    ) -> Callable[[grafeas.BatchCreateNotesRequest], grafeas.BatchCreateNotesResponse]:
        r"""Return a callable for the batch create notes method over gRPC.

        Creates new notes in batch.

        Returns:
            Callable[[~.BatchCreateNotesRequest],
                    ~.BatchCreateNotesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "batch_create_notes" not in self._stubs:
            self._stubs["batch_create_notes"] = self._logged_channel.unary_unary(
                "/grafeas.v1.Grafeas/BatchCreateNotes",
                request_serializer=grafeas.BatchCreateNotesRequest.serialize,
                response_deserializer=grafeas.BatchCreateNotesResponse.deserialize,
            )
        return self._stubs["batch_create_notes"]

    @property
    def update_note(self) -> Callable[[grafeas.UpdateNoteRequest], grafeas.Note]:
        r"""Return a callable for the update note method over gRPC.

        Updates the specified note.

        Returns:
            Callable[[~.UpdateNoteRequest],
                    ~.Note]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_note" not in self._stubs:
            self._stubs["update_note"] = self._logged_channel.unary_unary(
                "/grafeas.v1.Grafeas/UpdateNote",
                request_serializer=grafeas.UpdateNoteRequest.serialize,
                response_deserializer=grafeas.Note.deserialize,
            )
        return self._stubs["update_note"]

    @property
    def list_note_occurrences(
        self,
    ) -> Callable[
        [grafeas.ListNoteOccurrencesRequest], grafeas.ListNoteOccurrencesResponse
    ]:
        r"""Return a callable for the list note occurrences method over gRPC.

        Lists occurrences referencing the specified note.
        Provider projects can use this method to get all
        occurrences across consumer projects referencing the
        specified note.

        Returns:
            Callable[[~.ListNoteOccurrencesRequest],
                    ~.ListNoteOccurrencesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_note_occurrences" not in self._stubs:
            self._stubs["list_note_occurrences"] = self._logged_channel.unary_unary(
                "/grafeas.v1.Grafeas/ListNoteOccurrences",
                request_serializer=grafeas.ListNoteOccurrencesRequest.serialize,
                response_deserializer=grafeas.ListNoteOccurrencesResponse.deserialize,
            )
        return self._stubs["list_note_occurrences"]

    def close(self):
        self._logged_channel.close()

    @property
    def kind(self) -> str:
        return "grpc"


__all__ = ("GrafeasGrpcTransport",)
