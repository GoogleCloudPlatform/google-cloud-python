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

import google.api.httpbody_pb2 as httpbody_pb2  # type: ignore
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
import google.protobuf.message
import grpc  # type: ignore
import proto  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, grpc_helpers_async
from google.api_core import retry_async as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf.json_format import MessageToJson
from grpc.experimental import aio  # type: ignore

from google.cloud.managedkafka_schemaregistry_v1.types import (
    schema_registry,
    schema_registry_resources,
)
from google.cloud.managedkafka_schemaregistry_v1.types import (
    schema_registry as gcms_schema_registry,
)

from .base import DEFAULT_CLIENT_INFO, ManagedSchemaRegistryTransport
from .grpc import ManagedSchemaRegistryGrpcTransport

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
                    "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
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
                    "serviceName": "google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry",
                    "rpcName": str(client_call_details.method),
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class ManagedSchemaRegistryGrpcAsyncIOTransport(ManagedSchemaRegistryTransport):
    """gRPC AsyncIO backend transport for ManagedSchemaRegistry.

    SchemaRegistry is a service that allows users to manage schemas for
    their Kafka clusters. It provides APIs to register, list, and delete
    schemas, as well as to get the schema for a given schema id or a
    given version id under a subject, to update the global or
    subject-specific compatibility mode, and to check the compatibility
    of a schema against a subject or a version. The main resource
    hierarchy is as follows:

    - SchemaRegistry
    - SchemaRegistry/Context
    - SchemaRegistry/Context/Schema
    - SchemaRegistry/Context/Subject
    - SchemaRegistry/Context/Subject/Version
    - SchemaRegistry/Config
    - SchemaRegistry/Mode

    **SchemaRegistry** is the root resource to represent a schema
    registry instance. A customer can have multiple schema registry
    instances in a project.

    **Context** is a context resource that represents a group of
    schemas, subjects and versions. A schema registry instance can have
    multiple contexts and always has a 'default' context. Contexts are
    independent of each other. Context is optional and if not specified,
    it falls back to the 'default' context.

    **Schema** is a schema resource that represents a unique schema in a
    context of a schema registry instance. Each schema has a unique
    schema id, and can be referenced by a version of a subject.

    **Subject** refers to the name under which the schema is registered.
    A typical subject is the Kafka topic name. A schema registry
    instance can have multiple subjects.

    **Version** represents a version of a subject. A subject can have
    multiple versions. Creation of new version of a subject is guarded
    by the compatibility mode configured globally or for the subject
    specifically.

    **Config** represents a config at global level cross all registry
    instances or at subject level. Currently, only compatibility is
    supported in config.

    **Mode** represents the mode of a schema registry or a specific
    subject. Three modes are supported:

    - READONLY: The schema registry is in read-only mode, no write
      operations allowed..
    - READWRITE: The schema registry is in read-write mode, which allows
      limited write operations on the schema.
    - IMPORT: The schema registry is in import mode, which allows more
      editing operations on the schema for data importing purposes.

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
        host: str = "managedkafka.googleapis.com",
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
        host: str = "managedkafka.googleapis.com",
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
                 The hostname to connect to (default: 'managedkafka.googleapis.com').
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
    def get_schema_registry(
        self,
    ) -> Callable[
        [schema_registry.GetSchemaRegistryRequest],
        Awaitable[schema_registry_resources.SchemaRegistry],
    ]:
        r"""Return a callable for the get schema registry method over gRPC.

        Get the schema registry instance.

        Returns:
            Callable[[~.GetSchemaRegistryRequest],
                    Awaitable[~.SchemaRegistry]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_schema_registry" not in self._stubs:
            self._stubs["get_schema_registry"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry/GetSchemaRegistry",
                request_serializer=schema_registry.GetSchemaRegistryRequest.serialize,
                response_deserializer=schema_registry_resources.SchemaRegistry.deserialize,
            )
        return self._stubs["get_schema_registry"]

    @property
    def list_schema_registries(
        self,
    ) -> Callable[
        [schema_registry.ListSchemaRegistriesRequest],
        Awaitable[schema_registry.ListSchemaRegistriesResponse],
    ]:
        r"""Return a callable for the list schema registries method over gRPC.

        List schema registries.

        Returns:
            Callable[[~.ListSchemaRegistriesRequest],
                    Awaitable[~.ListSchemaRegistriesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_schema_registries" not in self._stubs:
            self._stubs["list_schema_registries"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry/ListSchemaRegistries",
                request_serializer=schema_registry.ListSchemaRegistriesRequest.serialize,
                response_deserializer=schema_registry.ListSchemaRegistriesResponse.deserialize,
            )
        return self._stubs["list_schema_registries"]

    @property
    def create_schema_registry(
        self,
    ) -> Callable[
        [gcms_schema_registry.CreateSchemaRegistryRequest],
        Awaitable[schema_registry_resources.SchemaRegistry],
    ]:
        r"""Return a callable for the create schema registry method over gRPC.

        Create a schema registry instance.

        Returns:
            Callable[[~.CreateSchemaRegistryRequest],
                    Awaitable[~.SchemaRegistry]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_schema_registry" not in self._stubs:
            self._stubs["create_schema_registry"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry/CreateSchemaRegistry",
                request_serializer=gcms_schema_registry.CreateSchemaRegistryRequest.serialize,
                response_deserializer=schema_registry_resources.SchemaRegistry.deserialize,
            )
        return self._stubs["create_schema_registry"]

    @property
    def delete_schema_registry(
        self,
    ) -> Callable[
        [schema_registry.DeleteSchemaRegistryRequest], Awaitable[empty_pb2.Empty]
    ]:
        r"""Return a callable for the delete schema registry method over gRPC.

        Delete a schema registry instance.

        Returns:
            Callable[[~.DeleteSchemaRegistryRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_schema_registry" not in self._stubs:
            self._stubs["delete_schema_registry"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry/DeleteSchemaRegistry",
                request_serializer=schema_registry.DeleteSchemaRegistryRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_schema_registry"]

    @property
    def get_context(
        self,
    ) -> Callable[
        [schema_registry.GetContextRequest],
        Awaitable[schema_registry_resources.Context],
    ]:
        r"""Return a callable for the get context method over gRPC.

        Get the context.

        Returns:
            Callable[[~.GetContextRequest],
                    Awaitable[~.Context]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_context" not in self._stubs:
            self._stubs["get_context"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry/GetContext",
                request_serializer=schema_registry.GetContextRequest.serialize,
                response_deserializer=schema_registry_resources.Context.deserialize,
            )
        return self._stubs["get_context"]

    @property
    def list_contexts(
        self,
    ) -> Callable[
        [schema_registry.ListContextsRequest], Awaitable[httpbody_pb2.HttpBody]
    ]:
        r"""Return a callable for the list contexts method over gRPC.

        List contexts for a schema registry.

        Returns:
            Callable[[~.ListContextsRequest],
                    Awaitable[~.HttpBody]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_contexts" not in self._stubs:
            self._stubs["list_contexts"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry/ListContexts",
                request_serializer=schema_registry.ListContextsRequest.serialize,
                response_deserializer=httpbody_pb2.HttpBody.FromString,
            )
        return self._stubs["list_contexts"]

    @property
    def get_schema(
        self,
    ) -> Callable[
        [schema_registry.GetSchemaRequest], Awaitable[schema_registry_resources.Schema]
    ]:
        r"""Return a callable for the get schema method over gRPC.

        Get the schema for the given schema id.

        Returns:
            Callable[[~.GetSchemaRequest],
                    Awaitable[~.Schema]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_schema" not in self._stubs:
            self._stubs["get_schema"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry/GetSchema",
                request_serializer=schema_registry.GetSchemaRequest.serialize,
                response_deserializer=schema_registry_resources.Schema.deserialize,
            )
        return self._stubs["get_schema"]

    @property
    def get_raw_schema(
        self,
    ) -> Callable[[schema_registry.GetSchemaRequest], Awaitable[httpbody_pb2.HttpBody]]:
        r"""Return a callable for the get raw schema method over gRPC.

        Get the schema string for the given schema id.
        The response will be the schema string.

        Returns:
            Callable[[~.GetSchemaRequest],
                    Awaitable[~.HttpBody]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_raw_schema" not in self._stubs:
            self._stubs["get_raw_schema"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry/GetRawSchema",
                request_serializer=schema_registry.GetSchemaRequest.serialize,
                response_deserializer=httpbody_pb2.HttpBody.FromString,
            )
        return self._stubs["get_raw_schema"]

    @property
    def list_schema_versions(
        self,
    ) -> Callable[
        [schema_registry.ListSchemaVersionsRequest], Awaitable[httpbody_pb2.HttpBody]
    ]:
        r"""Return a callable for the list schema versions method over gRPC.

        List the schema versions for the given schema id. The response
        will be an array of subject-version pairs as:
        [{"subject":"subject1", "version":1}, {"subject":"subject2",
        "version":2}].

        Returns:
            Callable[[~.ListSchemaVersionsRequest],
                    Awaitable[~.HttpBody]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_schema_versions" not in self._stubs:
            self._stubs["list_schema_versions"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry/ListSchemaVersions",
                request_serializer=schema_registry.ListSchemaVersionsRequest.serialize,
                response_deserializer=httpbody_pb2.HttpBody.FromString,
            )
        return self._stubs["list_schema_versions"]

    @property
    def list_schema_types(
        self,
    ) -> Callable[
        [schema_registry.ListSchemaTypesRequest], Awaitable[httpbody_pb2.HttpBody]
    ]:
        r"""Return a callable for the list schema types method over gRPC.

        List the supported schema types.
        The response will be an array of schema types.

        Returns:
            Callable[[~.ListSchemaTypesRequest],
                    Awaitable[~.HttpBody]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_schema_types" not in self._stubs:
            self._stubs["list_schema_types"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry/ListSchemaTypes",
                request_serializer=schema_registry.ListSchemaTypesRequest.serialize,
                response_deserializer=httpbody_pb2.HttpBody.FromString,
            )
        return self._stubs["list_schema_types"]

    @property
    def list_subjects(
        self,
    ) -> Callable[
        [schema_registry.ListSubjectsRequest], Awaitable[httpbody_pb2.HttpBody]
    ]:
        r"""Return a callable for the list subjects method over gRPC.

        List subjects in the schema registry.
        The response will be an array of subject names.

        Returns:
            Callable[[~.ListSubjectsRequest],
                    Awaitable[~.HttpBody]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_subjects" not in self._stubs:
            self._stubs["list_subjects"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry/ListSubjects",
                request_serializer=schema_registry.ListSubjectsRequest.serialize,
                response_deserializer=httpbody_pb2.HttpBody.FromString,
            )
        return self._stubs["list_subjects"]

    @property
    def list_subjects_by_schema_id(
        self,
    ) -> Callable[
        [schema_registry.ListSubjectsBySchemaIdRequest],
        Awaitable[httpbody_pb2.HttpBody],
    ]:
        r"""Return a callable for the list subjects by schema id method over gRPC.

        List subjects which reference a particular schema id.
        The response will be an array of subject names.

        Returns:
            Callable[[~.ListSubjectsBySchemaIdRequest],
                    Awaitable[~.HttpBody]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_subjects_by_schema_id" not in self._stubs:
            self._stubs["list_subjects_by_schema_id"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry/ListSubjectsBySchemaId",
                    request_serializer=schema_registry.ListSubjectsBySchemaIdRequest.serialize,
                    response_deserializer=httpbody_pb2.HttpBody.FromString,
                )
            )
        return self._stubs["list_subjects_by_schema_id"]

    @property
    def delete_subject(
        self,
    ) -> Callable[
        [schema_registry.DeleteSubjectRequest], Awaitable[httpbody_pb2.HttpBody]
    ]:
        r"""Return a callable for the delete subject method over gRPC.

        Delete a subject.
        The response will be an array of versions of the deleted
        subject.

        Returns:
            Callable[[~.DeleteSubjectRequest],
                    Awaitable[~.HttpBody]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_subject" not in self._stubs:
            self._stubs["delete_subject"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry/DeleteSubject",
                request_serializer=schema_registry.DeleteSubjectRequest.serialize,
                response_deserializer=httpbody_pb2.HttpBody.FromString,
            )
        return self._stubs["delete_subject"]

    @property
    def lookup_version(
        self,
    ) -> Callable[
        [schema_registry.LookupVersionRequest],
        Awaitable[schema_registry_resources.SchemaVersion],
    ]:
        r"""Return a callable for the lookup version method over gRPC.

        Lookup a schema under the specified subject.

        Returns:
            Callable[[~.LookupVersionRequest],
                    Awaitable[~.SchemaVersion]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "lookup_version" not in self._stubs:
            self._stubs["lookup_version"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry/LookupVersion",
                request_serializer=schema_registry.LookupVersionRequest.serialize,
                response_deserializer=schema_registry_resources.SchemaVersion.deserialize,
            )
        return self._stubs["lookup_version"]

    @property
    def get_version(
        self,
    ) -> Callable[
        [schema_registry.GetVersionRequest],
        Awaitable[schema_registry_resources.SchemaVersion],
    ]:
        r"""Return a callable for the get version method over gRPC.

        Get a versioned schema (schema with subject/version)
        of a subject.

        Returns:
            Callable[[~.GetVersionRequest],
                    Awaitable[~.SchemaVersion]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_version" not in self._stubs:
            self._stubs["get_version"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry/GetVersion",
                request_serializer=schema_registry.GetVersionRequest.serialize,
                response_deserializer=schema_registry_resources.SchemaVersion.deserialize,
            )
        return self._stubs["get_version"]

    @property
    def get_raw_schema_version(
        self,
    ) -> Callable[
        [schema_registry.GetVersionRequest], Awaitable[httpbody_pb2.HttpBody]
    ]:
        r"""Return a callable for the get raw schema version method over gRPC.

        Get the schema string only for a version of a
        subject. The response will be the schema string.

        Returns:
            Callable[[~.GetVersionRequest],
                    Awaitable[~.HttpBody]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_raw_schema_version" not in self._stubs:
            self._stubs["get_raw_schema_version"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry/GetRawSchemaVersion",
                request_serializer=schema_registry.GetVersionRequest.serialize,
                response_deserializer=httpbody_pb2.HttpBody.FromString,
            )
        return self._stubs["get_raw_schema_version"]

    @property
    def list_versions(
        self,
    ) -> Callable[
        [schema_registry.ListVersionsRequest], Awaitable[httpbody_pb2.HttpBody]
    ]:
        r"""Return a callable for the list versions method over gRPC.

        Get all versions of a subject.
        The response will be an array of versions of the
        subject.

        Returns:
            Callable[[~.ListVersionsRequest],
                    Awaitable[~.HttpBody]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_versions" not in self._stubs:
            self._stubs["list_versions"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry/ListVersions",
                request_serializer=schema_registry.ListVersionsRequest.serialize,
                response_deserializer=httpbody_pb2.HttpBody.FromString,
            )
        return self._stubs["list_versions"]

    @property
    def create_version(
        self,
    ) -> Callable[
        [schema_registry.CreateVersionRequest],
        Awaitable[schema_registry.CreateVersionResponse],
    ]:
        r"""Return a callable for the create version method over gRPC.

        Register a new version under a given subject with the
        given schema.

        Returns:
            Callable[[~.CreateVersionRequest],
                    Awaitable[~.CreateVersionResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_version" not in self._stubs:
            self._stubs["create_version"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry/CreateVersion",
                request_serializer=schema_registry.CreateVersionRequest.serialize,
                response_deserializer=schema_registry.CreateVersionResponse.deserialize,
            )
        return self._stubs["create_version"]

    @property
    def delete_version(
        self,
    ) -> Callable[
        [schema_registry.DeleteVersionRequest], Awaitable[httpbody_pb2.HttpBody]
    ]:
        r"""Return a callable for the delete version method over gRPC.

        Delete a version of a subject.
        The response will be the deleted version id.

        Returns:
            Callable[[~.DeleteVersionRequest],
                    Awaitable[~.HttpBody]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_version" not in self._stubs:
            self._stubs["delete_version"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry/DeleteVersion",
                request_serializer=schema_registry.DeleteVersionRequest.serialize,
                response_deserializer=httpbody_pb2.HttpBody.FromString,
            )
        return self._stubs["delete_version"]

    @property
    def list_referenced_schemas(
        self,
    ) -> Callable[
        [schema_registry.ListReferencedSchemasRequest], Awaitable[httpbody_pb2.HttpBody]
    ]:
        r"""Return a callable for the list referenced schemas method over gRPC.

        Get a list of IDs of schemas that reference the
        schema with the given subject and version.

        Returns:
            Callable[[~.ListReferencedSchemasRequest],
                    Awaitable[~.HttpBody]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_referenced_schemas" not in self._stubs:
            self._stubs["list_referenced_schemas"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry/ListReferencedSchemas",
                request_serializer=schema_registry.ListReferencedSchemasRequest.serialize,
                response_deserializer=httpbody_pb2.HttpBody.FromString,
            )
        return self._stubs["list_referenced_schemas"]

    @property
    def check_compatibility(
        self,
    ) -> Callable[
        [schema_registry.CheckCompatibilityRequest],
        Awaitable[schema_registry.CheckCompatibilityResponse],
    ]:
        r"""Return a callable for the check compatibility method over gRPC.

        Check compatibility of a schema with all versions or
        a specific version of a subject.

        Returns:
            Callable[[~.CheckCompatibilityRequest],
                    Awaitable[~.CheckCompatibilityResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "check_compatibility" not in self._stubs:
            self._stubs["check_compatibility"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry/CheckCompatibility",
                request_serializer=schema_registry.CheckCompatibilityRequest.serialize,
                response_deserializer=schema_registry.CheckCompatibilityResponse.deserialize,
            )
        return self._stubs["check_compatibility"]

    @property
    def get_schema_config(
        self,
    ) -> Callable[
        [schema_registry.GetSchemaConfigRequest],
        Awaitable[schema_registry_resources.SchemaConfig],
    ]:
        r"""Return a callable for the get schema config method over gRPC.

        Get schema config at global level or for a subject.

        Returns:
            Callable[[~.GetSchemaConfigRequest],
                    Awaitable[~.SchemaConfig]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_schema_config" not in self._stubs:
            self._stubs["get_schema_config"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry/GetSchemaConfig",
                request_serializer=schema_registry.GetSchemaConfigRequest.serialize,
                response_deserializer=schema_registry_resources.SchemaConfig.deserialize,
            )
        return self._stubs["get_schema_config"]

    @property
    def update_schema_config(
        self,
    ) -> Callable[
        [schema_registry.UpdateSchemaConfigRequest],
        Awaitable[schema_registry_resources.SchemaConfig],
    ]:
        r"""Return a callable for the update schema config method over gRPC.

        Update config at global level or for a subject.
        Creates a SchemaSubject-level SchemaConfig if it does
        not exist.

        Returns:
            Callable[[~.UpdateSchemaConfigRequest],
                    Awaitable[~.SchemaConfig]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_schema_config" not in self._stubs:
            self._stubs["update_schema_config"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry/UpdateSchemaConfig",
                request_serializer=schema_registry.UpdateSchemaConfigRequest.serialize,
                response_deserializer=schema_registry_resources.SchemaConfig.deserialize,
            )
        return self._stubs["update_schema_config"]

    @property
    def delete_schema_config(
        self,
    ) -> Callable[
        [schema_registry.DeleteSchemaConfigRequest],
        Awaitable[schema_registry_resources.SchemaConfig],
    ]:
        r"""Return a callable for the delete schema config method over gRPC.

        Delete schema config for a subject.

        Returns:
            Callable[[~.DeleteSchemaConfigRequest],
                    Awaitable[~.SchemaConfig]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_schema_config" not in self._stubs:
            self._stubs["delete_schema_config"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry/DeleteSchemaConfig",
                request_serializer=schema_registry.DeleteSchemaConfigRequest.serialize,
                response_deserializer=schema_registry_resources.SchemaConfig.deserialize,
            )
        return self._stubs["delete_schema_config"]

    @property
    def get_schema_mode(
        self,
    ) -> Callable[
        [schema_registry.GetSchemaModeRequest],
        Awaitable[schema_registry_resources.SchemaMode],
    ]:
        r"""Return a callable for the get schema mode method over gRPC.

        Get mode at global level or for a subject.

        Returns:
            Callable[[~.GetSchemaModeRequest],
                    Awaitable[~.SchemaMode]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_schema_mode" not in self._stubs:
            self._stubs["get_schema_mode"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry/GetSchemaMode",
                request_serializer=schema_registry.GetSchemaModeRequest.serialize,
                response_deserializer=schema_registry_resources.SchemaMode.deserialize,
            )
        return self._stubs["get_schema_mode"]

    @property
    def update_schema_mode(
        self,
    ) -> Callable[
        [schema_registry.UpdateSchemaModeRequest],
        Awaitable[schema_registry_resources.SchemaMode],
    ]:
        r"""Return a callable for the update schema mode method over gRPC.

        Update mode at global level or for a subject.

        Returns:
            Callable[[~.UpdateSchemaModeRequest],
                    Awaitable[~.SchemaMode]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_schema_mode" not in self._stubs:
            self._stubs["update_schema_mode"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry/UpdateSchemaMode",
                request_serializer=schema_registry.UpdateSchemaModeRequest.serialize,
                response_deserializer=schema_registry_resources.SchemaMode.deserialize,
            )
        return self._stubs["update_schema_mode"]

    @property
    def delete_schema_mode(
        self,
    ) -> Callable[
        [schema_registry.DeleteSchemaModeRequest],
        Awaitable[schema_registry_resources.SchemaMode],
    ]:
        r"""Return a callable for the delete schema mode method over gRPC.

        Delete schema mode for a subject.

        Returns:
            Callable[[~.DeleteSchemaModeRequest],
                    Awaitable[~.SchemaMode]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_schema_mode" not in self._stubs:
            self._stubs["delete_schema_mode"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.schemaregistry.v1.ManagedSchemaRegistry/DeleteSchemaMode",
                request_serializer=schema_registry.DeleteSchemaModeRequest.serialize,
                response_deserializer=schema_registry_resources.SchemaMode.deserialize,
            )
        return self._stubs["delete_schema_mode"]

    def _prep_wrapped_messages(self, client_info):
        """Precompute the wrapped methods, overriding the base class method to use async wrappers."""
        self._wrapped_methods = {
            self.get_schema_registry: self._wrap_method(
                self.get_schema_registry,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_schema_registries: self._wrap_method(
                self.list_schema_registries,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_schema_registry: self._wrap_method(
                self.create_schema_registry,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_schema_registry: self._wrap_method(
                self.delete_schema_registry,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_context: self._wrap_method(
                self.get_context,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_contexts: self._wrap_method(
                self.list_contexts,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_schema: self._wrap_method(
                self.get_schema,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_raw_schema: self._wrap_method(
                self.get_raw_schema,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_schema_versions: self._wrap_method(
                self.list_schema_versions,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_schema_types: self._wrap_method(
                self.list_schema_types,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_subjects: self._wrap_method(
                self.list_subjects,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_subjects_by_schema_id: self._wrap_method(
                self.list_subjects_by_schema_id,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_subject: self._wrap_method(
                self.delete_subject,
                default_timeout=None,
                client_info=client_info,
            ),
            self.lookup_version: self._wrap_method(
                self.lookup_version,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_version: self._wrap_method(
                self.get_version,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_raw_schema_version: self._wrap_method(
                self.get_raw_schema_version,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_versions: self._wrap_method(
                self.list_versions,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_version: self._wrap_method(
                self.create_version,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_version: self._wrap_method(
                self.delete_version,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_referenced_schemas: self._wrap_method(
                self.list_referenced_schemas,
                default_timeout=None,
                client_info=client_info,
            ),
            self.check_compatibility: self._wrap_method(
                self.check_compatibility,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_schema_config: self._wrap_method(
                self.get_schema_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_schema_config: self._wrap_method(
                self.update_schema_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_schema_config: self._wrap_method(
                self.delete_schema_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_schema_mode: self._wrap_method(
                self.get_schema_mode,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_schema_mode: self._wrap_method(
                self.update_schema_mode,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_schema_mode: self._wrap_method(
                self.delete_schema_mode,
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


__all__ = ("ManagedSchemaRegistryGrpcAsyncIOTransport",)
