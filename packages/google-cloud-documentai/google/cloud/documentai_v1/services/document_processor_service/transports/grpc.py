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
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf.json_format import MessageToJson

from google.cloud.documentai_v1.types import (
    document_processor_service,
    evaluation,
    processor,
    processor_type,
)
from google.cloud.documentai_v1.types import processor as gcd_processor

from .base import DEFAULT_CLIENT_INFO, DocumentProcessorServiceTransport

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
                    "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
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
                    "serviceName": "google.cloud.documentai.v1.DocumentProcessorService",
                    "rpcName": client_call_details.method,
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class DocumentProcessorServiceGrpcTransport(DocumentProcessorServiceTransport):
    """gRPC backend transport for DocumentProcessorService.

    Service to call Document AI to process documents according to
    the processor's definition. Processors are built using
    state-of-the-art Google AI such as natural language, computer
    vision, and translation to extract structured information from
    unstructured or semi-structured documents.

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
        host: str = "documentai.googleapis.com",
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
                 The hostname to connect to (default: 'documentai.googleapis.com').
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
        host: str = "documentai.googleapis.com",
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
    def process_document(
        self,
    ) -> Callable[
        [document_processor_service.ProcessRequest],
        document_processor_service.ProcessResponse,
    ]:
        r"""Return a callable for the process document method over gRPC.

        Processes a single document.

        Returns:
            Callable[[~.ProcessRequest],
                    ~.ProcessResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "process_document" not in self._stubs:
            self._stubs["process_document"] = self._logged_channel.unary_unary(
                "/google.cloud.documentai.v1.DocumentProcessorService/ProcessDocument",
                request_serializer=document_processor_service.ProcessRequest.serialize,
                response_deserializer=document_processor_service.ProcessResponse.deserialize,
            )
        return self._stubs["process_document"]

    @property
    def batch_process_documents(
        self,
    ) -> Callable[
        [document_processor_service.BatchProcessRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the batch process documents method over gRPC.

        LRO endpoint to batch process many documents. The output is
        written to Cloud Storage as JSON in the [Document] format.

        Returns:
            Callable[[~.BatchProcessRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "batch_process_documents" not in self._stubs:
            self._stubs["batch_process_documents"] = self._logged_channel.unary_unary(
                "/google.cloud.documentai.v1.DocumentProcessorService/BatchProcessDocuments",
                request_serializer=document_processor_service.BatchProcessRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["batch_process_documents"]

    @property
    def fetch_processor_types(
        self,
    ) -> Callable[
        [document_processor_service.FetchProcessorTypesRequest],
        document_processor_service.FetchProcessorTypesResponse,
    ]:
        r"""Return a callable for the fetch processor types method over gRPC.

        Fetches processor types. Note that we don't use
        [ListProcessorTypes][google.cloud.documentai.v1.DocumentProcessorService.ListProcessorTypes]
        here, because it isn't paginated.

        Returns:
            Callable[[~.FetchProcessorTypesRequest],
                    ~.FetchProcessorTypesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "fetch_processor_types" not in self._stubs:
            self._stubs["fetch_processor_types"] = self._logged_channel.unary_unary(
                "/google.cloud.documentai.v1.DocumentProcessorService/FetchProcessorTypes",
                request_serializer=document_processor_service.FetchProcessorTypesRequest.serialize,
                response_deserializer=document_processor_service.FetchProcessorTypesResponse.deserialize,
            )
        return self._stubs["fetch_processor_types"]

    @property
    def list_processor_types(
        self,
    ) -> Callable[
        [document_processor_service.ListProcessorTypesRequest],
        document_processor_service.ListProcessorTypesResponse,
    ]:
        r"""Return a callable for the list processor types method over gRPC.

        Lists the processor types that exist.

        Returns:
            Callable[[~.ListProcessorTypesRequest],
                    ~.ListProcessorTypesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_processor_types" not in self._stubs:
            self._stubs["list_processor_types"] = self._logged_channel.unary_unary(
                "/google.cloud.documentai.v1.DocumentProcessorService/ListProcessorTypes",
                request_serializer=document_processor_service.ListProcessorTypesRequest.serialize,
                response_deserializer=document_processor_service.ListProcessorTypesResponse.deserialize,
            )
        return self._stubs["list_processor_types"]

    @property
    def get_processor_type(
        self,
    ) -> Callable[
        [document_processor_service.GetProcessorTypeRequest],
        processor_type.ProcessorType,
    ]:
        r"""Return a callable for the get processor type method over gRPC.

        Gets a processor type detail.

        Returns:
            Callable[[~.GetProcessorTypeRequest],
                    ~.ProcessorType]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_processor_type" not in self._stubs:
            self._stubs["get_processor_type"] = self._logged_channel.unary_unary(
                "/google.cloud.documentai.v1.DocumentProcessorService/GetProcessorType",
                request_serializer=document_processor_service.GetProcessorTypeRequest.serialize,
                response_deserializer=processor_type.ProcessorType.deserialize,
            )
        return self._stubs["get_processor_type"]

    @property
    def list_processors(
        self,
    ) -> Callable[
        [document_processor_service.ListProcessorsRequest],
        document_processor_service.ListProcessorsResponse,
    ]:
        r"""Return a callable for the list processors method over gRPC.

        Lists all processors which belong to this project.

        Returns:
            Callable[[~.ListProcessorsRequest],
                    ~.ListProcessorsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_processors" not in self._stubs:
            self._stubs["list_processors"] = self._logged_channel.unary_unary(
                "/google.cloud.documentai.v1.DocumentProcessorService/ListProcessors",
                request_serializer=document_processor_service.ListProcessorsRequest.serialize,
                response_deserializer=document_processor_service.ListProcessorsResponse.deserialize,
            )
        return self._stubs["list_processors"]

    @property
    def get_processor(
        self,
    ) -> Callable[
        [document_processor_service.GetProcessorRequest], processor.Processor
    ]:
        r"""Return a callable for the get processor method over gRPC.

        Gets a processor detail.

        Returns:
            Callable[[~.GetProcessorRequest],
                    ~.Processor]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_processor" not in self._stubs:
            self._stubs["get_processor"] = self._logged_channel.unary_unary(
                "/google.cloud.documentai.v1.DocumentProcessorService/GetProcessor",
                request_serializer=document_processor_service.GetProcessorRequest.serialize,
                response_deserializer=processor.Processor.deserialize,
            )
        return self._stubs["get_processor"]

    @property
    def train_processor_version(
        self,
    ) -> Callable[
        [document_processor_service.TrainProcessorVersionRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the train processor version method over gRPC.

        Trains a new processor version. Operation metadata is returned
        as
        [TrainProcessorVersionMetadata][google.cloud.documentai.v1.TrainProcessorVersionMetadata].

        Returns:
            Callable[[~.TrainProcessorVersionRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "train_processor_version" not in self._stubs:
            self._stubs["train_processor_version"] = self._logged_channel.unary_unary(
                "/google.cloud.documentai.v1.DocumentProcessorService/TrainProcessorVersion",
                request_serializer=document_processor_service.TrainProcessorVersionRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["train_processor_version"]

    @property
    def get_processor_version(
        self,
    ) -> Callable[
        [document_processor_service.GetProcessorVersionRequest],
        processor.ProcessorVersion,
    ]:
        r"""Return a callable for the get processor version method over gRPC.

        Gets a processor version detail.

        Returns:
            Callable[[~.GetProcessorVersionRequest],
                    ~.ProcessorVersion]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_processor_version" not in self._stubs:
            self._stubs["get_processor_version"] = self._logged_channel.unary_unary(
                "/google.cloud.documentai.v1.DocumentProcessorService/GetProcessorVersion",
                request_serializer=document_processor_service.GetProcessorVersionRequest.serialize,
                response_deserializer=processor.ProcessorVersion.deserialize,
            )
        return self._stubs["get_processor_version"]

    @property
    def list_processor_versions(
        self,
    ) -> Callable[
        [document_processor_service.ListProcessorVersionsRequest],
        document_processor_service.ListProcessorVersionsResponse,
    ]:
        r"""Return a callable for the list processor versions method over gRPC.

        Lists all versions of a processor.

        Returns:
            Callable[[~.ListProcessorVersionsRequest],
                    ~.ListProcessorVersionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_processor_versions" not in self._stubs:
            self._stubs["list_processor_versions"] = self._logged_channel.unary_unary(
                "/google.cloud.documentai.v1.DocumentProcessorService/ListProcessorVersions",
                request_serializer=document_processor_service.ListProcessorVersionsRequest.serialize,
                response_deserializer=document_processor_service.ListProcessorVersionsResponse.deserialize,
            )
        return self._stubs["list_processor_versions"]

    @property
    def delete_processor_version(
        self,
    ) -> Callable[
        [document_processor_service.DeleteProcessorVersionRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the delete processor version method over gRPC.

        Deletes the processor version, all artifacts under
        the processor version will be deleted.

        Returns:
            Callable[[~.DeleteProcessorVersionRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_processor_version" not in self._stubs:
            self._stubs["delete_processor_version"] = self._logged_channel.unary_unary(
                "/google.cloud.documentai.v1.DocumentProcessorService/DeleteProcessorVersion",
                request_serializer=document_processor_service.DeleteProcessorVersionRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_processor_version"]

    @property
    def deploy_processor_version(
        self,
    ) -> Callable[
        [document_processor_service.DeployProcessorVersionRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the deploy processor version method over gRPC.

        Deploys the processor version.

        Returns:
            Callable[[~.DeployProcessorVersionRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "deploy_processor_version" not in self._stubs:
            self._stubs["deploy_processor_version"] = self._logged_channel.unary_unary(
                "/google.cloud.documentai.v1.DocumentProcessorService/DeployProcessorVersion",
                request_serializer=document_processor_service.DeployProcessorVersionRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["deploy_processor_version"]

    @property
    def undeploy_processor_version(
        self,
    ) -> Callable[
        [document_processor_service.UndeployProcessorVersionRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the undeploy processor version method over gRPC.

        Undeploys the processor version.

        Returns:
            Callable[[~.UndeployProcessorVersionRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "undeploy_processor_version" not in self._stubs:
            self._stubs["undeploy_processor_version"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.documentai.v1.DocumentProcessorService/UndeployProcessorVersion",
                    request_serializer=document_processor_service.UndeployProcessorVersionRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["undeploy_processor_version"]

    @property
    def create_processor(
        self,
    ) -> Callable[
        [document_processor_service.CreateProcessorRequest], gcd_processor.Processor
    ]:
        r"""Return a callable for the create processor method over gRPC.

        Creates a processor from the
        [ProcessorType][google.cloud.documentai.v1.ProcessorType]
        provided. The processor will be at ``ENABLED`` state by default
        after its creation. Note that this method requires the
        ``documentai.processors.create`` permission on the project,
        which is highly privileged. A user or service account with this
        permission can create new processors that can interact with any
        gcs bucket in your project.

        Returns:
            Callable[[~.CreateProcessorRequest],
                    ~.Processor]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_processor" not in self._stubs:
            self._stubs["create_processor"] = self._logged_channel.unary_unary(
                "/google.cloud.documentai.v1.DocumentProcessorService/CreateProcessor",
                request_serializer=document_processor_service.CreateProcessorRequest.serialize,
                response_deserializer=gcd_processor.Processor.deserialize,
            )
        return self._stubs["create_processor"]

    @property
    def delete_processor(
        self,
    ) -> Callable[
        [document_processor_service.DeleteProcessorRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the delete processor method over gRPC.

        Deletes the processor, unloads all deployed model
        artifacts if it was enabled and then deletes all
        artifacts associated with this processor.

        Returns:
            Callable[[~.DeleteProcessorRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_processor" not in self._stubs:
            self._stubs["delete_processor"] = self._logged_channel.unary_unary(
                "/google.cloud.documentai.v1.DocumentProcessorService/DeleteProcessor",
                request_serializer=document_processor_service.DeleteProcessorRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_processor"]

    @property
    def enable_processor(
        self,
    ) -> Callable[
        [document_processor_service.EnableProcessorRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the enable processor method over gRPC.

        Enables a processor

        Returns:
            Callable[[~.EnableProcessorRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "enable_processor" not in self._stubs:
            self._stubs["enable_processor"] = self._logged_channel.unary_unary(
                "/google.cloud.documentai.v1.DocumentProcessorService/EnableProcessor",
                request_serializer=document_processor_service.EnableProcessorRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["enable_processor"]

    @property
    def disable_processor(
        self,
    ) -> Callable[
        [document_processor_service.DisableProcessorRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the disable processor method over gRPC.

        Disables a processor

        Returns:
            Callable[[~.DisableProcessorRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "disable_processor" not in self._stubs:
            self._stubs["disable_processor"] = self._logged_channel.unary_unary(
                "/google.cloud.documentai.v1.DocumentProcessorService/DisableProcessor",
                request_serializer=document_processor_service.DisableProcessorRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["disable_processor"]

    @property
    def set_default_processor_version(
        self,
    ) -> Callable[
        [document_processor_service.SetDefaultProcessorVersionRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the set default processor version method over gRPC.

        Set the default (active) version of a
        [Processor][google.cloud.documentai.v1.Processor] that will be
        used in
        [ProcessDocument][google.cloud.documentai.v1.DocumentProcessorService.ProcessDocument]
        and
        [BatchProcessDocuments][google.cloud.documentai.v1.DocumentProcessorService.BatchProcessDocuments].

        Returns:
            Callable[[~.SetDefaultProcessorVersionRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "set_default_processor_version" not in self._stubs:
            self._stubs["set_default_processor_version"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.documentai.v1.DocumentProcessorService/SetDefaultProcessorVersion",
                    request_serializer=document_processor_service.SetDefaultProcessorVersionRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["set_default_processor_version"]

    @property
    def review_document(
        self,
    ) -> Callable[
        [document_processor_service.ReviewDocumentRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the review document method over gRPC.

        Send a document for Human Review. The input document
        should be processed by the specified processor.

        Returns:
            Callable[[~.ReviewDocumentRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "review_document" not in self._stubs:
            self._stubs["review_document"] = self._logged_channel.unary_unary(
                "/google.cloud.documentai.v1.DocumentProcessorService/ReviewDocument",
                request_serializer=document_processor_service.ReviewDocumentRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["review_document"]

    @property
    def evaluate_processor_version(
        self,
    ) -> Callable[
        [document_processor_service.EvaluateProcessorVersionRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the evaluate processor version method over gRPC.

        Evaluates a ProcessorVersion against annotated
        documents, producing an Evaluation.

        Returns:
            Callable[[~.EvaluateProcessorVersionRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "evaluate_processor_version" not in self._stubs:
            self._stubs["evaluate_processor_version"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.documentai.v1.DocumentProcessorService/EvaluateProcessorVersion",
                    request_serializer=document_processor_service.EvaluateProcessorVersionRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["evaluate_processor_version"]

    @property
    def get_evaluation(
        self,
    ) -> Callable[
        [document_processor_service.GetEvaluationRequest], evaluation.Evaluation
    ]:
        r"""Return a callable for the get evaluation method over gRPC.

        Retrieves a specific evaluation.

        Returns:
            Callable[[~.GetEvaluationRequest],
                    ~.Evaluation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_evaluation" not in self._stubs:
            self._stubs["get_evaluation"] = self._logged_channel.unary_unary(
                "/google.cloud.documentai.v1.DocumentProcessorService/GetEvaluation",
                request_serializer=document_processor_service.GetEvaluationRequest.serialize,
                response_deserializer=evaluation.Evaluation.deserialize,
            )
        return self._stubs["get_evaluation"]

    @property
    def list_evaluations(
        self,
    ) -> Callable[
        [document_processor_service.ListEvaluationsRequest],
        document_processor_service.ListEvaluationsResponse,
    ]:
        r"""Return a callable for the list evaluations method over gRPC.

        Retrieves a set of evaluations for a given processor
        version.

        Returns:
            Callable[[~.ListEvaluationsRequest],
                    ~.ListEvaluationsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_evaluations" not in self._stubs:
            self._stubs["list_evaluations"] = self._logged_channel.unary_unary(
                "/google.cloud.documentai.v1.DocumentProcessorService/ListEvaluations",
                request_serializer=document_processor_service.ListEvaluationsRequest.serialize,
                response_deserializer=document_processor_service.ListEvaluationsResponse.deserialize,
            )
        return self._stubs["list_evaluations"]

    def close(self):
        self._logged_channel.close()

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


__all__ = ("DocumentProcessorServiceGrpcTransport",)
