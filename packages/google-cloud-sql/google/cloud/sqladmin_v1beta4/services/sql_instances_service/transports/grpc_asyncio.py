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
from google.api_core import gapic_v1, grpc_helpers_async
from google.api_core import retry_async as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf.json_format import MessageToJson
from grpc.experimental import aio  # type: ignore

from google.cloud.sqladmin_v1beta4.types import cloud_sql, cloud_sql_resources

from .base import DEFAULT_CLIENT_INFO, SqlInstancesServiceTransport
from .grpc import SqlInstancesServiceGrpcTransport

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
                    "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
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
                    "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                    "rpcName": str(client_call_details.method),
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class SqlInstancesServiceGrpcAsyncIOTransport(SqlInstancesServiceTransport):
    """gRPC AsyncIO backend transport for SqlInstancesService.

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
        host: str = "sqladmin.googleapis.com",
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
        host: str = "sqladmin.googleapis.com",
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
                 The hostname to connect to (default: 'sqladmin.googleapis.com').
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
    def add_server_ca(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesAddServerCaRequest],
        Awaitable[cloud_sql_resources.Operation],
    ]:
        r"""Return a callable for the add server ca method over gRPC.

        Add a new trusted Certificate Authority (CA) version
        for the specified instance. Required to prepare for a
        certificate rotation. If a CA version was previously
        added but never used in a certificate rotation, this
        operation replaces that version. There cannot be more
        than one CA version waiting to be rotated in. For
        instances that have enabled Certificate Authority
        Service (CAS) based server CA, use AddServerCertificate
        to add a new server certificate.

        Returns:
            Callable[[~.SqlInstancesAddServerCaRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "add_server_ca" not in self._stubs:
            self._stubs["add_server_ca"] = self._logged_channel.unary_unary(
                "/google.cloud.sql.v1beta4.SqlInstancesService/AddServerCa",
                request_serializer=cloud_sql.SqlInstancesAddServerCaRequest.serialize,
                response_deserializer=cloud_sql_resources.Operation.deserialize,
            )
        return self._stubs["add_server_ca"]

    @property
    def add_server_certificate(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesAddServerCertificateRequest],
        Awaitable[cloud_sql_resources.Operation],
    ]:
        r"""Return a callable for the add server certificate method over gRPC.

        Add a new trusted server certificate version for the
        specified instance using Certificate Authority Service
        (CAS) server CA. Required to prepare for a certificate
        rotation. If a server certificate version was previously
        added but never used in a certificate rotation, this
        operation replaces that version. There cannot be more
        than one certificate version waiting to be rotated in.
        For instances not using CAS server CA, use AddServerCa
        instead.

        Returns:
            Callable[[~.SqlInstancesAddServerCertificateRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "add_server_certificate" not in self._stubs:
            self._stubs["add_server_certificate"] = self._logged_channel.unary_unary(
                "/google.cloud.sql.v1beta4.SqlInstancesService/AddServerCertificate",
                request_serializer=cloud_sql.SqlInstancesAddServerCertificateRequest.serialize,
                response_deserializer=cloud_sql_resources.Operation.deserialize,
            )
        return self._stubs["add_server_certificate"]

    @property
    def add_entra_id_certificate(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesAddEntraIdCertificateRequest],
        Awaitable[cloud_sql_resources.Operation],
    ]:
        r"""Return a callable for the add entra id certificate method over gRPC.

        Adds a new Entra ID certificate for the specified
        instance. If an Entra ID certificate was previously
        added but never used in a certificate rotation, this
        operation replaces that version.

        Returns:
            Callable[[~.SqlInstancesAddEntraIdCertificateRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "add_entra_id_certificate" not in self._stubs:
            self._stubs["add_entra_id_certificate"] = self._logged_channel.unary_unary(
                "/google.cloud.sql.v1beta4.SqlInstancesService/AddEntraIdCertificate",
                request_serializer=cloud_sql.SqlInstancesAddEntraIdCertificateRequest.serialize,
                response_deserializer=cloud_sql_resources.Operation.deserialize,
            )
        return self._stubs["add_entra_id_certificate"]

    @property
    def clone(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesCloneRequest], Awaitable[cloud_sql_resources.Operation]
    ]:
        r"""Return a callable for the clone method over gRPC.

        Creates a Cloud SQL instance as a clone of the source
        instance. Using this operation might cause your instance
        to restart.

        Returns:
            Callable[[~.SqlInstancesCloneRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "clone" not in self._stubs:
            self._stubs["clone"] = self._logged_channel.unary_unary(
                "/google.cloud.sql.v1beta4.SqlInstancesService/Clone",
                request_serializer=cloud_sql.SqlInstancesCloneRequest.serialize,
                response_deserializer=cloud_sql_resources.Operation.deserialize,
            )
        return self._stubs["clone"]

    @property
    def delete(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesDeleteRequest], Awaitable[cloud_sql_resources.Operation]
    ]:
        r"""Return a callable for the delete method over gRPC.

        Deletes a Cloud SQL instance.

        Returns:
            Callable[[~.SqlInstancesDeleteRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete" not in self._stubs:
            self._stubs["delete"] = self._logged_channel.unary_unary(
                "/google.cloud.sql.v1beta4.SqlInstancesService/Delete",
                request_serializer=cloud_sql.SqlInstancesDeleteRequest.serialize,
                response_deserializer=cloud_sql_resources.Operation.deserialize,
            )
        return self._stubs["delete"]

    @property
    def demote_master(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesDemoteMasterRequest],
        Awaitable[cloud_sql_resources.Operation],
    ]:
        r"""Return a callable for the demote master method over gRPC.

        Demotes the stand-alone instance to be a Cloud SQL
        read replica for an external database server.

        Returns:
            Callable[[~.SqlInstancesDemoteMasterRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "demote_master" not in self._stubs:
            self._stubs["demote_master"] = self._logged_channel.unary_unary(
                "/google.cloud.sql.v1beta4.SqlInstancesService/DemoteMaster",
                request_serializer=cloud_sql.SqlInstancesDemoteMasterRequest.serialize,
                response_deserializer=cloud_sql_resources.Operation.deserialize,
            )
        return self._stubs["demote_master"]

    @property
    def demote(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesDemoteRequest], Awaitable[cloud_sql_resources.Operation]
    ]:
        r"""Return a callable for the demote method over gRPC.

        Demotes an existing standalone instance to be a Cloud
        SQL read replica for an external database server.

        Returns:
            Callable[[~.SqlInstancesDemoteRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "demote" not in self._stubs:
            self._stubs["demote"] = self._logged_channel.unary_unary(
                "/google.cloud.sql.v1beta4.SqlInstancesService/Demote",
                request_serializer=cloud_sql.SqlInstancesDemoteRequest.serialize,
                response_deserializer=cloud_sql_resources.Operation.deserialize,
            )
        return self._stubs["demote"]

    @property
    def export(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesExportRequest], Awaitable[cloud_sql_resources.Operation]
    ]:
        r"""Return a callable for the export method over gRPC.

        Exports data from a Cloud SQL instance to a Cloud
        Storage bucket as a SQL dump or CSV file.

        Returns:
            Callable[[~.SqlInstancesExportRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "export" not in self._stubs:
            self._stubs["export"] = self._logged_channel.unary_unary(
                "/google.cloud.sql.v1beta4.SqlInstancesService/Export",
                request_serializer=cloud_sql.SqlInstancesExportRequest.serialize,
                response_deserializer=cloud_sql_resources.Operation.deserialize,
            )
        return self._stubs["export"]

    @property
    def failover(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesFailoverRequest],
        Awaitable[cloud_sql_resources.Operation],
    ]:
        r"""Return a callable for the failover method over gRPC.

        Initiates a manual failover of a high availability (HA) primary
        instance to a standby instance, which becomes the primary
        instance. Users are then rerouted to the new primary. For more
        information, see the `Overview of high
        availability <https://cloud.google.com/sql/docs/mysql/high-availability>`__
        page in the Cloud SQL documentation. If using Legacy HA (MySQL
        only), this causes the instance to failover to its failover
        replica instance.

        Returns:
            Callable[[~.SqlInstancesFailoverRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "failover" not in self._stubs:
            self._stubs["failover"] = self._logged_channel.unary_unary(
                "/google.cloud.sql.v1beta4.SqlInstancesService/Failover",
                request_serializer=cloud_sql.SqlInstancesFailoverRequest.serialize,
                response_deserializer=cloud_sql_resources.Operation.deserialize,
            )
        return self._stubs["failover"]

    @property
    def reencrypt(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesReencryptRequest],
        Awaitable[cloud_sql_resources.Operation],
    ]:
        r"""Return a callable for the reencrypt method over gRPC.

        Reencrypt CMEK instance with latest key version.

        Returns:
            Callable[[~.SqlInstancesReencryptRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "reencrypt" not in self._stubs:
            self._stubs["reencrypt"] = self._logged_channel.unary_unary(
                "/google.cloud.sql.v1beta4.SqlInstancesService/Reencrypt",
                request_serializer=cloud_sql.SqlInstancesReencryptRequest.serialize,
                response_deserializer=cloud_sql_resources.Operation.deserialize,
            )
        return self._stubs["reencrypt"]

    @property
    def get(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesGetRequest],
        Awaitable[cloud_sql_resources.DatabaseInstance],
    ]:
        r"""Return a callable for the get method over gRPC.

        Retrieves a resource containing information about a
        Cloud SQL instance.

        Returns:
            Callable[[~.SqlInstancesGetRequest],
                    Awaitable[~.DatabaseInstance]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get" not in self._stubs:
            self._stubs["get"] = self._logged_channel.unary_unary(
                "/google.cloud.sql.v1beta4.SqlInstancesService/Get",
                request_serializer=cloud_sql.SqlInstancesGetRequest.serialize,
                response_deserializer=cloud_sql_resources.DatabaseInstance.deserialize,
            )
        return self._stubs["get"]

    @property
    def import_(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesImportRequest], Awaitable[cloud_sql_resources.Operation]
    ]:
        r"""Return a callable for the import method over gRPC.

        Imports data into a Cloud SQL instance from a SQL
        dump  or CSV file in Cloud Storage.

        Returns:
            Callable[[~.SqlInstancesImportRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "import_" not in self._stubs:
            self._stubs["import_"] = self._logged_channel.unary_unary(
                "/google.cloud.sql.v1beta4.SqlInstancesService/Import",
                request_serializer=cloud_sql.SqlInstancesImportRequest.serialize,
                response_deserializer=cloud_sql_resources.Operation.deserialize,
            )
        return self._stubs["import_"]

    @property
    def insert(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesInsertRequest], Awaitable[cloud_sql_resources.Operation]
    ]:
        r"""Return a callable for the insert method over gRPC.

        Creates a new Cloud SQL instance.

        Returns:
            Callable[[~.SqlInstancesInsertRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "insert" not in self._stubs:
            self._stubs["insert"] = self._logged_channel.unary_unary(
                "/google.cloud.sql.v1beta4.SqlInstancesService/Insert",
                request_serializer=cloud_sql.SqlInstancesInsertRequest.serialize,
                response_deserializer=cloud_sql_resources.Operation.deserialize,
            )
        return self._stubs["insert"]

    @property
    def list(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesListRequest],
        Awaitable[cloud_sql_resources.InstancesListResponse],
    ]:
        r"""Return a callable for the list method over gRPC.

        Lists instances under a given project.

        Returns:
            Callable[[~.SqlInstancesListRequest],
                    Awaitable[~.InstancesListResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list" not in self._stubs:
            self._stubs["list"] = self._logged_channel.unary_unary(
                "/google.cloud.sql.v1beta4.SqlInstancesService/List",
                request_serializer=cloud_sql.SqlInstancesListRequest.serialize,
                response_deserializer=cloud_sql_resources.InstancesListResponse.deserialize,
            )
        return self._stubs["list"]

    @property
    def list_server_cas(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesListServerCasRequest],
        Awaitable[cloud_sql_resources.InstancesListServerCasResponse],
    ]:
        r"""Return a callable for the list server cas method over gRPC.

        Lists all of the trusted Certificate Authorities
        (CAs) for the specified instance. There can be up to
        three CAs listed: the CA that was used to sign the
        certificate that is currently in use, a CA that has been
        added but not yet used to sign a certificate, and a CA
        used to sign a certificate that has previously rotated
        out.

        Returns:
            Callable[[~.SqlInstancesListServerCasRequest],
                    Awaitable[~.InstancesListServerCasResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_server_cas" not in self._stubs:
            self._stubs["list_server_cas"] = self._logged_channel.unary_unary(
                "/google.cloud.sql.v1beta4.SqlInstancesService/ListServerCas",
                request_serializer=cloud_sql.SqlInstancesListServerCasRequest.serialize,
                response_deserializer=cloud_sql_resources.InstancesListServerCasResponse.deserialize,
            )
        return self._stubs["list_server_cas"]

    @property
    def list_server_certificates(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesListServerCertificatesRequest],
        Awaitable[cloud_sql_resources.InstancesListServerCertificatesResponse],
    ]:
        r"""Return a callable for the list server certificates method over gRPC.

        Lists all versions of server certificates and
        certificate authorities (CAs) for the specified
        instance. There can be up to three sets of certs listed:

        the certificate that is currently in use, a future that
        has been added but not yet used to sign a certificate,
        and a certificate that has been rotated out. For
        instances not using Certificate Authority Service (CAS)
        server CA, use ListServerCas instead.

        Returns:
            Callable[[~.SqlInstancesListServerCertificatesRequest],
                    Awaitable[~.InstancesListServerCertificatesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_server_certificates" not in self._stubs:
            self._stubs["list_server_certificates"] = self._logged_channel.unary_unary(
                "/google.cloud.sql.v1beta4.SqlInstancesService/ListServerCertificates",
                request_serializer=cloud_sql.SqlInstancesListServerCertificatesRequest.serialize,
                response_deserializer=cloud_sql_resources.InstancesListServerCertificatesResponse.deserialize,
            )
        return self._stubs["list_server_certificates"]

    @property
    def list_entra_id_certificates(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesListEntraIdCertificatesRequest],
        Awaitable[cloud_sql_resources.InstancesListEntraIdCertificatesResponse],
    ]:
        r"""Return a callable for the list entra id certificates method over gRPC.

        Lists all versions of EntraID certificates for the
        specified instance. There can be up to three sets of
        certificates listed: the certificate that is currently
        in use, a future that has been added but not yet used to
        sign a certificate, and a certificate that has been
        rotated out.

        Returns:
            Callable[[~.SqlInstancesListEntraIdCertificatesRequest],
                    Awaitable[~.InstancesListEntraIdCertificatesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_entra_id_certificates" not in self._stubs:
            self._stubs["list_entra_id_certificates"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.sql.v1beta4.SqlInstancesService/ListEntraIdCertificates",
                    request_serializer=cloud_sql.SqlInstancesListEntraIdCertificatesRequest.serialize,
                    response_deserializer=cloud_sql_resources.InstancesListEntraIdCertificatesResponse.deserialize,
                )
            )
        return self._stubs["list_entra_id_certificates"]

    @property
    def patch(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesPatchRequest], Awaitable[cloud_sql_resources.Operation]
    ]:
        r"""Return a callable for the patch method over gRPC.

        Partially updates settings of a Cloud SQL instance by
        merging the request with the current configuration. This
        method supports patch semantics.

        Returns:
            Callable[[~.SqlInstancesPatchRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "patch" not in self._stubs:
            self._stubs["patch"] = self._logged_channel.unary_unary(
                "/google.cloud.sql.v1beta4.SqlInstancesService/Patch",
                request_serializer=cloud_sql.SqlInstancesPatchRequest.serialize,
                response_deserializer=cloud_sql_resources.Operation.deserialize,
            )
        return self._stubs["patch"]

    @property
    def promote_replica(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesPromoteReplicaRequest],
        Awaitable[cloud_sql_resources.Operation],
    ]:
        r"""Return a callable for the promote replica method over gRPC.

        Promotes the read replica instance to be an
        independent Cloud SQL primary instance.
        Using this operation might cause your instance to
        restart.

        Returns:
            Callable[[~.SqlInstancesPromoteReplicaRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "promote_replica" not in self._stubs:
            self._stubs["promote_replica"] = self._logged_channel.unary_unary(
                "/google.cloud.sql.v1beta4.SqlInstancesService/PromoteReplica",
                request_serializer=cloud_sql.SqlInstancesPromoteReplicaRequest.serialize,
                response_deserializer=cloud_sql_resources.Operation.deserialize,
            )
        return self._stubs["promote_replica"]

    @property
    def switchover(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesSwitchoverRequest],
        Awaitable[cloud_sql_resources.Operation],
    ]:
        r"""Return a callable for the switchover method over gRPC.

        Switches over from the primary instance to the DR
        replica instance.

        Returns:
            Callable[[~.SqlInstancesSwitchoverRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "switchover" not in self._stubs:
            self._stubs["switchover"] = self._logged_channel.unary_unary(
                "/google.cloud.sql.v1beta4.SqlInstancesService/Switchover",
                request_serializer=cloud_sql.SqlInstancesSwitchoverRequest.serialize,
                response_deserializer=cloud_sql_resources.Operation.deserialize,
            )
        return self._stubs["switchover"]

    @property
    def reset_ssl_config(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesResetSslConfigRequest],
        Awaitable[cloud_sql_resources.Operation],
    ]:
        r"""Return a callable for the reset ssl config method over gRPC.

        Deletes all client certificates and generates a new
        server SSL certificate for the instance.

        Returns:
            Callable[[~.SqlInstancesResetSslConfigRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "reset_ssl_config" not in self._stubs:
            self._stubs["reset_ssl_config"] = self._logged_channel.unary_unary(
                "/google.cloud.sql.v1beta4.SqlInstancesService/ResetSslConfig",
                request_serializer=cloud_sql.SqlInstancesResetSslConfigRequest.serialize,
                response_deserializer=cloud_sql_resources.Operation.deserialize,
            )
        return self._stubs["reset_ssl_config"]

    @property
    def restart(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesRestartRequest], Awaitable[cloud_sql_resources.Operation]
    ]:
        r"""Return a callable for the restart method over gRPC.

        Restarts a Cloud SQL instance.

        Returns:
            Callable[[~.SqlInstancesRestartRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "restart" not in self._stubs:
            self._stubs["restart"] = self._logged_channel.unary_unary(
                "/google.cloud.sql.v1beta4.SqlInstancesService/Restart",
                request_serializer=cloud_sql.SqlInstancesRestartRequest.serialize,
                response_deserializer=cloud_sql_resources.Operation.deserialize,
            )
        return self._stubs["restart"]

    @property
    def restore_backup(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesRestoreBackupRequest],
        Awaitable[cloud_sql_resources.Operation],
    ]:
        r"""Return a callable for the restore backup method over gRPC.

        Restores a backup of a Cloud SQL instance. Using this
        operation might cause your instance to restart.

        Returns:
            Callable[[~.SqlInstancesRestoreBackupRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "restore_backup" not in self._stubs:
            self._stubs["restore_backup"] = self._logged_channel.unary_unary(
                "/google.cloud.sql.v1beta4.SqlInstancesService/RestoreBackup",
                request_serializer=cloud_sql.SqlInstancesRestoreBackupRequest.serialize,
                response_deserializer=cloud_sql_resources.Operation.deserialize,
            )
        return self._stubs["restore_backup"]

    @property
    def rotate_server_ca(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesRotateServerCaRequest],
        Awaitable[cloud_sql_resources.Operation],
    ]:
        r"""Return a callable for the rotate server ca method over gRPC.

        Rotates the server certificate to one signed by the
        Certificate Authority (CA) version previously added with
        the addServerCA method. For instances that have enabled
        Certificate Authority Service (CAS) based server CA, use
        RotateServerCertificate to rotate the server
        certificate.

        Returns:
            Callable[[~.SqlInstancesRotateServerCaRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "rotate_server_ca" not in self._stubs:
            self._stubs["rotate_server_ca"] = self._logged_channel.unary_unary(
                "/google.cloud.sql.v1beta4.SqlInstancesService/RotateServerCa",
                request_serializer=cloud_sql.SqlInstancesRotateServerCaRequest.serialize,
                response_deserializer=cloud_sql_resources.Operation.deserialize,
            )
        return self._stubs["rotate_server_ca"]

    @property
    def rotate_server_certificate(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesRotateServerCertificateRequest],
        Awaitable[cloud_sql_resources.Operation],
    ]:
        r"""Return a callable for the rotate server certificate method over gRPC.

        Rotates the server certificate version to one
        previously added with the addServerCertificate method.
        For instances not using Certificate Authority Service
        (CAS) server CA, use RotateServerCa instead.

        Returns:
            Callable[[~.SqlInstancesRotateServerCertificateRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "rotate_server_certificate" not in self._stubs:
            self._stubs["rotate_server_certificate"] = self._logged_channel.unary_unary(
                "/google.cloud.sql.v1beta4.SqlInstancesService/RotateServerCertificate",
                request_serializer=cloud_sql.SqlInstancesRotateServerCertificateRequest.serialize,
                response_deserializer=cloud_sql_resources.Operation.deserialize,
            )
        return self._stubs["rotate_server_certificate"]

    @property
    def rotate_entra_id_certificate(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesRotateEntraIdCertificateRequest],
        Awaitable[cloud_sql_resources.Operation],
    ]:
        r"""Return a callable for the rotate entra id certificate method over gRPC.

        Rotates the Entra Id certificate version to one
        previously added with the addEntraIdCertificate method.

        Returns:
            Callable[[~.SqlInstancesRotateEntraIdCertificateRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "rotate_entra_id_certificate" not in self._stubs:
            self._stubs["rotate_entra_id_certificate"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.sql.v1beta4.SqlInstancesService/RotateEntraIdCertificate",
                    request_serializer=cloud_sql.SqlInstancesRotateEntraIdCertificateRequest.serialize,
                    response_deserializer=cloud_sql_resources.Operation.deserialize,
                )
            )
        return self._stubs["rotate_entra_id_certificate"]

    @property
    def start_replica(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesStartReplicaRequest],
        Awaitable[cloud_sql_resources.Operation],
    ]:
        r"""Return a callable for the start replica method over gRPC.

        Starts the replication in the read replica instance.

        Returns:
            Callable[[~.SqlInstancesStartReplicaRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "start_replica" not in self._stubs:
            self._stubs["start_replica"] = self._logged_channel.unary_unary(
                "/google.cloud.sql.v1beta4.SqlInstancesService/StartReplica",
                request_serializer=cloud_sql.SqlInstancesStartReplicaRequest.serialize,
                response_deserializer=cloud_sql_resources.Operation.deserialize,
            )
        return self._stubs["start_replica"]

    @property
    def stop_replica(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesStopReplicaRequest],
        Awaitable[cloud_sql_resources.Operation],
    ]:
        r"""Return a callable for the stop replica method over gRPC.

        Stops the replication in the read replica instance.

        Returns:
            Callable[[~.SqlInstancesStopReplicaRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "stop_replica" not in self._stubs:
            self._stubs["stop_replica"] = self._logged_channel.unary_unary(
                "/google.cloud.sql.v1beta4.SqlInstancesService/StopReplica",
                request_serializer=cloud_sql.SqlInstancesStopReplicaRequest.serialize,
                response_deserializer=cloud_sql_resources.Operation.deserialize,
            )
        return self._stubs["stop_replica"]

    @property
    def truncate_log(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesTruncateLogRequest],
        Awaitable[cloud_sql_resources.Operation],
    ]:
        r"""Return a callable for the truncate log method over gRPC.

        Truncate MySQL general and slow query log tables
        MySQL only.

        Returns:
            Callable[[~.SqlInstancesTruncateLogRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "truncate_log" not in self._stubs:
            self._stubs["truncate_log"] = self._logged_channel.unary_unary(
                "/google.cloud.sql.v1beta4.SqlInstancesService/TruncateLog",
                request_serializer=cloud_sql.SqlInstancesTruncateLogRequest.serialize,
                response_deserializer=cloud_sql_resources.Operation.deserialize,
            )
        return self._stubs["truncate_log"]

    @property
    def update(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesUpdateRequest], Awaitable[cloud_sql_resources.Operation]
    ]:
        r"""Return a callable for the update method over gRPC.

        Updates settings of a Cloud SQL instance. Using this
        operation might cause your instance to restart.

        Returns:
            Callable[[~.SqlInstancesUpdateRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update" not in self._stubs:
            self._stubs["update"] = self._logged_channel.unary_unary(
                "/google.cloud.sql.v1beta4.SqlInstancesService/Update",
                request_serializer=cloud_sql.SqlInstancesUpdateRequest.serialize,
                response_deserializer=cloud_sql_resources.Operation.deserialize,
            )
        return self._stubs["update"]

    @property
    def create_ephemeral(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesCreateEphemeralCertRequest],
        Awaitable[cloud_sql_resources.SslCert],
    ]:
        r"""Return a callable for the create ephemeral method over gRPC.

        Generates a short-lived X509 certificate containing
        the provided public key and signed by a private key
        specific to the target instance. Users may use the
        certificate to authenticate as themselves when
        connecting to the database.

        Returns:
            Callable[[~.SqlInstancesCreateEphemeralCertRequest],
                    Awaitable[~.SslCert]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_ephemeral" not in self._stubs:
            self._stubs["create_ephemeral"] = self._logged_channel.unary_unary(
                "/google.cloud.sql.v1beta4.SqlInstancesService/CreateEphemeral",
                request_serializer=cloud_sql.SqlInstancesCreateEphemeralCertRequest.serialize,
                response_deserializer=cloud_sql_resources.SslCert.deserialize,
            )
        return self._stubs["create_ephemeral"]

    @property
    def reschedule_maintenance(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesRescheduleMaintenanceRequest],
        Awaitable[cloud_sql_resources.Operation],
    ]:
        r"""Return a callable for the reschedule maintenance method over gRPC.

        Reschedules the maintenance on the given instance.

        Returns:
            Callable[[~.SqlInstancesRescheduleMaintenanceRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "reschedule_maintenance" not in self._stubs:
            self._stubs["reschedule_maintenance"] = self._logged_channel.unary_unary(
                "/google.cloud.sql.v1beta4.SqlInstancesService/RescheduleMaintenance",
                request_serializer=cloud_sql.SqlInstancesRescheduleMaintenanceRequest.serialize,
                response_deserializer=cloud_sql_resources.Operation.deserialize,
            )
        return self._stubs["reschedule_maintenance"]

    @property
    def verify_external_sync_settings(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesVerifyExternalSyncSettingsRequest],
        Awaitable[cloud_sql_resources.SqlInstancesVerifyExternalSyncSettingsResponse],
    ]:
        r"""Return a callable for the verify external sync settings method over gRPC.

        Verify External primary instance external sync
        settings.

        Returns:
            Callable[[~.SqlInstancesVerifyExternalSyncSettingsRequest],
                    Awaitable[~.SqlInstancesVerifyExternalSyncSettingsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "verify_external_sync_settings" not in self._stubs:
            self._stubs["verify_external_sync_settings"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.sql.v1beta4.SqlInstancesService/VerifyExternalSyncSettings",
                    request_serializer=cloud_sql.SqlInstancesVerifyExternalSyncSettingsRequest.serialize,
                    response_deserializer=cloud_sql_resources.SqlInstancesVerifyExternalSyncSettingsResponse.deserialize,
                )
            )
        return self._stubs["verify_external_sync_settings"]

    @property
    def start_external_sync(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesStartExternalSyncRequest],
        Awaitable[cloud_sql_resources.Operation],
    ]:
        r"""Return a callable for the start external sync method over gRPC.

        Start External primary instance migration.

        Returns:
            Callable[[~.SqlInstancesStartExternalSyncRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "start_external_sync" not in self._stubs:
            self._stubs["start_external_sync"] = self._logged_channel.unary_unary(
                "/google.cloud.sql.v1beta4.SqlInstancesService/StartExternalSync",
                request_serializer=cloud_sql.SqlInstancesStartExternalSyncRequest.serialize,
                response_deserializer=cloud_sql_resources.Operation.deserialize,
            )
        return self._stubs["start_external_sync"]

    @property
    def perform_disk_shrink(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesPerformDiskShrinkRequest],
        Awaitable[cloud_sql_resources.Operation],
    ]:
        r"""Return a callable for the perform disk shrink method over gRPC.

        Perform Disk Shrink on primary instance.

        Returns:
            Callable[[~.SqlInstancesPerformDiskShrinkRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "perform_disk_shrink" not in self._stubs:
            self._stubs["perform_disk_shrink"] = self._logged_channel.unary_unary(
                "/google.cloud.sql.v1beta4.SqlInstancesService/PerformDiskShrink",
                request_serializer=cloud_sql.SqlInstancesPerformDiskShrinkRequest.serialize,
                response_deserializer=cloud_sql_resources.Operation.deserialize,
            )
        return self._stubs["perform_disk_shrink"]

    @property
    def get_disk_shrink_config(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesGetDiskShrinkConfigRequest],
        Awaitable[cloud_sql_resources.SqlInstancesGetDiskShrinkConfigResponse],
    ]:
        r"""Return a callable for the get disk shrink config method over gRPC.

        Get Disk Shrink Config for a given instance.

        Returns:
            Callable[[~.SqlInstancesGetDiskShrinkConfigRequest],
                    Awaitable[~.SqlInstancesGetDiskShrinkConfigResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_disk_shrink_config" not in self._stubs:
            self._stubs["get_disk_shrink_config"] = self._logged_channel.unary_unary(
                "/google.cloud.sql.v1beta4.SqlInstancesService/GetDiskShrinkConfig",
                request_serializer=cloud_sql.SqlInstancesGetDiskShrinkConfigRequest.serialize,
                response_deserializer=cloud_sql_resources.SqlInstancesGetDiskShrinkConfigResponse.deserialize,
            )
        return self._stubs["get_disk_shrink_config"]

    @property
    def reset_replica_size(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesResetReplicaSizeRequest],
        Awaitable[cloud_sql_resources.Operation],
    ]:
        r"""Return a callable for the reset replica size method over gRPC.

        Reset Replica Size to primary instance disk size.

        Returns:
            Callable[[~.SqlInstancesResetReplicaSizeRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "reset_replica_size" not in self._stubs:
            self._stubs["reset_replica_size"] = self._logged_channel.unary_unary(
                "/google.cloud.sql.v1beta4.SqlInstancesService/ResetReplicaSize",
                request_serializer=cloud_sql.SqlInstancesResetReplicaSizeRequest.serialize,
                response_deserializer=cloud_sql_resources.Operation.deserialize,
            )
        return self._stubs["reset_replica_size"]

    @property
    def get_latest_recovery_time(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesGetLatestRecoveryTimeRequest],
        Awaitable[cloud_sql.SqlInstancesGetLatestRecoveryTimeResponse],
    ]:
        r"""Return a callable for the get latest recovery time method over gRPC.

        Get Latest Recovery Time for a given instance.

        Returns:
            Callable[[~.SqlInstancesGetLatestRecoveryTimeRequest],
                    Awaitable[~.SqlInstancesGetLatestRecoveryTimeResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_latest_recovery_time" not in self._stubs:
            self._stubs["get_latest_recovery_time"] = self._logged_channel.unary_unary(
                "/google.cloud.sql.v1beta4.SqlInstancesService/GetLatestRecoveryTime",
                request_serializer=cloud_sql.SqlInstancesGetLatestRecoveryTimeRequest.serialize,
                response_deserializer=cloud_sql.SqlInstancesGetLatestRecoveryTimeResponse.deserialize,
            )
        return self._stubs["get_latest_recovery_time"]

    @property
    def execute_sql(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesExecuteSqlRequest],
        Awaitable[cloud_sql.SqlInstancesExecuteSqlResponse],
    ]:
        r"""Return a callable for the execute sql method over gRPC.

        Execute SQL statements.

        Returns:
            Callable[[~.SqlInstancesExecuteSqlRequest],
                    Awaitable[~.SqlInstancesExecuteSqlResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "execute_sql" not in self._stubs:
            self._stubs["execute_sql"] = self._logged_channel.unary_unary(
                "/google.cloud.sql.v1beta4.SqlInstancesService/ExecuteSql",
                request_serializer=cloud_sql.SqlInstancesExecuteSqlRequest.serialize,
                response_deserializer=cloud_sql.SqlInstancesExecuteSqlResponse.deserialize,
            )
        return self._stubs["execute_sql"]

    @property
    def acquire_ssrs_lease(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesAcquireSsrsLeaseRequest],
        Awaitable[cloud_sql.SqlInstancesAcquireSsrsLeaseResponse],
    ]:
        r"""Return a callable for the acquire ssrs lease method over gRPC.

        Acquire a lease for the setup of SQL Server Reporting
        Services (SSRS).

        Returns:
            Callable[[~.SqlInstancesAcquireSsrsLeaseRequest],
                    Awaitable[~.SqlInstancesAcquireSsrsLeaseResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "acquire_ssrs_lease" not in self._stubs:
            self._stubs["acquire_ssrs_lease"] = self._logged_channel.unary_unary(
                "/google.cloud.sql.v1beta4.SqlInstancesService/AcquireSsrsLease",
                request_serializer=cloud_sql.SqlInstancesAcquireSsrsLeaseRequest.serialize,
                response_deserializer=cloud_sql.SqlInstancesAcquireSsrsLeaseResponse.deserialize,
            )
        return self._stubs["acquire_ssrs_lease"]

    @property
    def release_ssrs_lease(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesReleaseSsrsLeaseRequest],
        Awaitable[cloud_sql.SqlInstancesReleaseSsrsLeaseResponse],
    ]:
        r"""Return a callable for the release ssrs lease method over gRPC.

        Release a lease for the setup of SQL Server Reporting
        Services (SSRS).

        Returns:
            Callable[[~.SqlInstancesReleaseSsrsLeaseRequest],
                    Awaitable[~.SqlInstancesReleaseSsrsLeaseResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "release_ssrs_lease" not in self._stubs:
            self._stubs["release_ssrs_lease"] = self._logged_channel.unary_unary(
                "/google.cloud.sql.v1beta4.SqlInstancesService/ReleaseSsrsLease",
                request_serializer=cloud_sql.SqlInstancesReleaseSsrsLeaseRequest.serialize,
                response_deserializer=cloud_sql.SqlInstancesReleaseSsrsLeaseResponse.deserialize,
            )
        return self._stubs["release_ssrs_lease"]

    @property
    def pre_check_major_version_upgrade(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesPreCheckMajorVersionUpgradeRequest],
        Awaitable[cloud_sql_resources.Operation],
    ]:
        r"""Return a callable for the pre check major version
        upgrade method over gRPC.

        Execute MVU Pre-checks

        Returns:
            Callable[[~.SqlInstancesPreCheckMajorVersionUpgradeRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "pre_check_major_version_upgrade" not in self._stubs:
            self._stubs["pre_check_major_version_upgrade"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.sql.v1beta4.SqlInstancesService/PreCheckMajorVersionUpgrade",
                    request_serializer=cloud_sql.SqlInstancesPreCheckMajorVersionUpgradeRequest.serialize,
                    response_deserializer=cloud_sql_resources.Operation.deserialize,
                )
            )
        return self._stubs["pre_check_major_version_upgrade"]

    @property
    def point_in_time_restore(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesPointInTimeRestoreRequest],
        Awaitable[cloud_sql_resources.Operation],
    ]:
        r"""Return a callable for the point in time restore method over gRPC.

        Point in time restore for an instance managed by
        Google Cloud Backup and Disaster Recovery.

        Returns:
            Callable[[~.SqlInstancesPointInTimeRestoreRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "point_in_time_restore" not in self._stubs:
            self._stubs["point_in_time_restore"] = self._logged_channel.unary_unary(
                "/google.cloud.sql.v1beta4.SqlInstancesService/PointInTimeRestore",
                request_serializer=cloud_sql.SqlInstancesPointInTimeRestoreRequest.serialize,
                response_deserializer=cloud_sql_resources.Operation.deserialize,
            )
        return self._stubs["point_in_time_restore"]

    def _prep_wrapped_messages(self, client_info):
        """Precompute the wrapped methods, overriding the base class method to use async wrappers."""
        self._wrapped_methods = {
            self.add_server_ca: self._wrap_method(
                self.add_server_ca,
                default_timeout=None,
                client_info=client_info,
            ),
            self.add_server_certificate: self._wrap_method(
                self.add_server_certificate,
                default_timeout=None,
                client_info=client_info,
            ),
            self.add_entra_id_certificate: self._wrap_method(
                self.add_entra_id_certificate,
                default_timeout=None,
                client_info=client_info,
            ),
            self.clone: self._wrap_method(
                self.clone,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete: self._wrap_method(
                self.delete,
                default_timeout=None,
                client_info=client_info,
            ),
            self.demote_master: self._wrap_method(
                self.demote_master,
                default_timeout=None,
                client_info=client_info,
            ),
            self.demote: self._wrap_method(
                self.demote,
                default_timeout=None,
                client_info=client_info,
            ),
            self.export: self._wrap_method(
                self.export,
                default_timeout=None,
                client_info=client_info,
            ),
            self.failover: self._wrap_method(
                self.failover,
                default_timeout=None,
                client_info=client_info,
            ),
            self.reencrypt: self._wrap_method(
                self.reencrypt,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get: self._wrap_method(
                self.get,
                default_timeout=None,
                client_info=client_info,
            ),
            self.import_: self._wrap_method(
                self.import_,
                default_timeout=None,
                client_info=client_info,
            ),
            self.insert: self._wrap_method(
                self.insert,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list: self._wrap_method(
                self.list,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_server_cas: self._wrap_method(
                self.list_server_cas,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_server_certificates: self._wrap_method(
                self.list_server_certificates,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_entra_id_certificates: self._wrap_method(
                self.list_entra_id_certificates,
                default_timeout=None,
                client_info=client_info,
            ),
            self.patch: self._wrap_method(
                self.patch,
                default_timeout=None,
                client_info=client_info,
            ),
            self.promote_replica: self._wrap_method(
                self.promote_replica,
                default_timeout=None,
                client_info=client_info,
            ),
            self.switchover: self._wrap_method(
                self.switchover,
                default_timeout=None,
                client_info=client_info,
            ),
            self.reset_ssl_config: self._wrap_method(
                self.reset_ssl_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.restart: self._wrap_method(
                self.restart,
                default_timeout=None,
                client_info=client_info,
            ),
            self.restore_backup: self._wrap_method(
                self.restore_backup,
                default_timeout=None,
                client_info=client_info,
            ),
            self.rotate_server_ca: self._wrap_method(
                self.rotate_server_ca,
                default_timeout=None,
                client_info=client_info,
            ),
            self.rotate_server_certificate: self._wrap_method(
                self.rotate_server_certificate,
                default_timeout=None,
                client_info=client_info,
            ),
            self.rotate_entra_id_certificate: self._wrap_method(
                self.rotate_entra_id_certificate,
                default_timeout=None,
                client_info=client_info,
            ),
            self.start_replica: self._wrap_method(
                self.start_replica,
                default_timeout=None,
                client_info=client_info,
            ),
            self.stop_replica: self._wrap_method(
                self.stop_replica,
                default_timeout=None,
                client_info=client_info,
            ),
            self.truncate_log: self._wrap_method(
                self.truncate_log,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update: self._wrap_method(
                self.update,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_ephemeral: self._wrap_method(
                self.create_ephemeral,
                default_timeout=None,
                client_info=client_info,
            ),
            self.reschedule_maintenance: self._wrap_method(
                self.reschedule_maintenance,
                default_timeout=None,
                client_info=client_info,
            ),
            self.verify_external_sync_settings: self._wrap_method(
                self.verify_external_sync_settings,
                default_timeout=None,
                client_info=client_info,
            ),
            self.start_external_sync: self._wrap_method(
                self.start_external_sync,
                default_timeout=None,
                client_info=client_info,
            ),
            self.perform_disk_shrink: self._wrap_method(
                self.perform_disk_shrink,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_disk_shrink_config: self._wrap_method(
                self.get_disk_shrink_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.reset_replica_size: self._wrap_method(
                self.reset_replica_size,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_latest_recovery_time: self._wrap_method(
                self.get_latest_recovery_time,
                default_timeout=None,
                client_info=client_info,
            ),
            self.execute_sql: self._wrap_method(
                self.execute_sql,
                default_timeout=None,
                client_info=client_info,
            ),
            self.acquire_ssrs_lease: self._wrap_method(
                self.acquire_ssrs_lease,
                default_timeout=None,
                client_info=client_info,
            ),
            self.release_ssrs_lease: self._wrap_method(
                self.release_ssrs_lease,
                default_timeout=None,
                client_info=client_info,
            ),
            self.pre_check_major_version_upgrade: self._wrap_method(
                self.pre_check_major_version_upgrade,
                default_timeout=None,
                client_info=client_info,
            ),
            self.point_in_time_restore: self._wrap_method(
                self.point_in_time_restore,
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


__all__ = ("SqlInstancesServiceGrpcAsyncIOTransport",)
