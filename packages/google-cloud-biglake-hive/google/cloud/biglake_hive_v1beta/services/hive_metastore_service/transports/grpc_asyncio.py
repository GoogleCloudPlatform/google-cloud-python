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

import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
import google.protobuf.message
import grpc  # type: ignore
import proto  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, grpc_helpers_async
from google.api_core import retry_async as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.protobuf.json_format import MessageToJson
from grpc.experimental import aio  # type: ignore

from google.cloud.biglake_hive_v1beta.types import hive_metastore

from .base import DEFAULT_CLIENT_INFO, HiveMetastoreServiceTransport
from .grpc import HiveMetastoreServiceGrpcTransport

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
                    "serviceName": "google.cloud.biglake.hive.v1beta.HiveMetastoreService",
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
                    "serviceName": "google.cloud.biglake.hive.v1beta.HiveMetastoreService",
                    "rpcName": str(client_call_details.method),
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class HiveMetastoreServiceGrpcAsyncIOTransport(HiveMetastoreServiceTransport):
    """gRPC AsyncIO backend transport for HiveMetastoreService.

    Hive Metastore Service is a biglake service that allows users to
    manage their external Hive catalogs. Full API compatibility with OSS
    Hive Metastore APIs is not supported. The methods match the Hive
    Metastore API spec mostly except for a few exceptions. These include
    listing resources with pattern, environment context which are
    combined in a single List API, return of ListResponse object instead
    of a list of resources, transactions, locks, etc.

    The BigLake Hive Metastore API defines the following resources:

    - A collection of Google Cloud projects: ``/projects/*``
    - Each project has a collection of catalogs: ``/catalogs/*``
    - Each catalog has a collection of databases: ``/databases/*``
    - Each database has a collection of tables: ``/tables/*``

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
        host: str = "biglake.googleapis.com",
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
        host: str = "biglake.googleapis.com",
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
                 The hostname to connect to (default: 'biglake.googleapis.com').
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
    def create_hive_catalog(
        self,
    ) -> Callable[
        [hive_metastore.CreateHiveCatalogRequest], Awaitable[hive_metastore.HiveCatalog]
    ]:
        r"""Return a callable for the create hive catalog method over gRPC.

        Creates a new hive catalog.

        Returns:
            Callable[[~.CreateHiveCatalogRequest],
                    Awaitable[~.HiveCatalog]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_hive_catalog" not in self._stubs:
            self._stubs["create_hive_catalog"] = self._logged_channel.unary_unary(
                "/google.cloud.biglake.hive.v1beta.HiveMetastoreService/CreateHiveCatalog",
                request_serializer=hive_metastore.CreateHiveCatalogRequest.serialize,
                response_deserializer=hive_metastore.HiveCatalog.deserialize,
            )
        return self._stubs["create_hive_catalog"]

    @property
    def get_hive_catalog(
        self,
    ) -> Callable[
        [hive_metastore.GetHiveCatalogRequest], Awaitable[hive_metastore.HiveCatalog]
    ]:
        r"""Return a callable for the get hive catalog method over gRPC.

        Gets the catalog specified by the resource name.

        Returns:
            Callable[[~.GetHiveCatalogRequest],
                    Awaitable[~.HiveCatalog]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_hive_catalog" not in self._stubs:
            self._stubs["get_hive_catalog"] = self._logged_channel.unary_unary(
                "/google.cloud.biglake.hive.v1beta.HiveMetastoreService/GetHiveCatalog",
                request_serializer=hive_metastore.GetHiveCatalogRequest.serialize,
                response_deserializer=hive_metastore.HiveCatalog.deserialize,
            )
        return self._stubs["get_hive_catalog"]

    @property
    def list_hive_catalogs(
        self,
    ) -> Callable[
        [hive_metastore.ListHiveCatalogsRequest],
        Awaitable[hive_metastore.ListHiveCatalogsResponse],
    ]:
        r"""Return a callable for the list hive catalogs method over gRPC.

        List all catalogs in a specified project.

        Returns:
            Callable[[~.ListHiveCatalogsRequest],
                    Awaitable[~.ListHiveCatalogsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_hive_catalogs" not in self._stubs:
            self._stubs["list_hive_catalogs"] = self._logged_channel.unary_unary(
                "/google.cloud.biglake.hive.v1beta.HiveMetastoreService/ListHiveCatalogs",
                request_serializer=hive_metastore.ListHiveCatalogsRequest.serialize,
                response_deserializer=hive_metastore.ListHiveCatalogsResponse.deserialize,
            )
        return self._stubs["list_hive_catalogs"]

    @property
    def update_hive_catalog(
        self,
    ) -> Callable[
        [hive_metastore.UpdateHiveCatalogRequest], Awaitable[hive_metastore.HiveCatalog]
    ]:
        r"""Return a callable for the update hive catalog method over gRPC.

        Updates an existing catalog.

        Returns:
            Callable[[~.UpdateHiveCatalogRequest],
                    Awaitable[~.HiveCatalog]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_hive_catalog" not in self._stubs:
            self._stubs["update_hive_catalog"] = self._logged_channel.unary_unary(
                "/google.cloud.biglake.hive.v1beta.HiveMetastoreService/UpdateHiveCatalog",
                request_serializer=hive_metastore.UpdateHiveCatalogRequest.serialize,
                response_deserializer=hive_metastore.HiveCatalog.deserialize,
            )
        return self._stubs["update_hive_catalog"]

    @property
    def delete_hive_catalog(
        self,
    ) -> Callable[
        [hive_metastore.DeleteHiveCatalogRequest], Awaitable[empty_pb2.Empty]
    ]:
        r"""Return a callable for the delete hive catalog method over gRPC.

        Deletes an existing catalog specified by the catalog
        ID. Delete will fail if the catalog is not empty.

        Returns:
            Callable[[~.DeleteHiveCatalogRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_hive_catalog" not in self._stubs:
            self._stubs["delete_hive_catalog"] = self._logged_channel.unary_unary(
                "/google.cloud.biglake.hive.v1beta.HiveMetastoreService/DeleteHiveCatalog",
                request_serializer=hive_metastore.DeleteHiveCatalogRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_hive_catalog"]

    @property
    def create_hive_database(
        self,
    ) -> Callable[
        [hive_metastore.CreateHiveDatabaseRequest],
        Awaitable[hive_metastore.HiveDatabase],
    ]:
        r"""Return a callable for the create hive database method over gRPC.

        Creates a new database.

        Returns:
            Callable[[~.CreateHiveDatabaseRequest],
                    Awaitable[~.HiveDatabase]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_hive_database" not in self._stubs:
            self._stubs["create_hive_database"] = self._logged_channel.unary_unary(
                "/google.cloud.biglake.hive.v1beta.HiveMetastoreService/CreateHiveDatabase",
                request_serializer=hive_metastore.CreateHiveDatabaseRequest.serialize,
                response_deserializer=hive_metastore.HiveDatabase.deserialize,
            )
        return self._stubs["create_hive_database"]

    @property
    def get_hive_database(
        self,
    ) -> Callable[
        [hive_metastore.GetHiveDatabaseRequest], Awaitable[hive_metastore.HiveDatabase]
    ]:
        r"""Return a callable for the get hive database method over gRPC.

        Gets the database specified by the resource name.

        Returns:
            Callable[[~.GetHiveDatabaseRequest],
                    Awaitable[~.HiveDatabase]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_hive_database" not in self._stubs:
            self._stubs["get_hive_database"] = self._logged_channel.unary_unary(
                "/google.cloud.biglake.hive.v1beta.HiveMetastoreService/GetHiveDatabase",
                request_serializer=hive_metastore.GetHiveDatabaseRequest.serialize,
                response_deserializer=hive_metastore.HiveDatabase.deserialize,
            )
        return self._stubs["get_hive_database"]

    @property
    def list_hive_databases(
        self,
    ) -> Callable[
        [hive_metastore.ListHiveDatabasesRequest],
        Awaitable[hive_metastore.ListHiveDatabasesResponse],
    ]:
        r"""Return a callable for the list hive databases method over gRPC.

        List all databases in a specified catalog.

        Returns:
            Callable[[~.ListHiveDatabasesRequest],
                    Awaitable[~.ListHiveDatabasesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_hive_databases" not in self._stubs:
            self._stubs["list_hive_databases"] = self._logged_channel.unary_unary(
                "/google.cloud.biglake.hive.v1beta.HiveMetastoreService/ListHiveDatabases",
                request_serializer=hive_metastore.ListHiveDatabasesRequest.serialize,
                response_deserializer=hive_metastore.ListHiveDatabasesResponse.deserialize,
            )
        return self._stubs["list_hive_databases"]

    @property
    def update_hive_database(
        self,
    ) -> Callable[
        [hive_metastore.UpdateHiveDatabaseRequest],
        Awaitable[hive_metastore.HiveDatabase],
    ]:
        r"""Return a callable for the update hive database method over gRPC.

        Updates an existing database specified by the
        database name.

        Returns:
            Callable[[~.UpdateHiveDatabaseRequest],
                    Awaitable[~.HiveDatabase]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_hive_database" not in self._stubs:
            self._stubs["update_hive_database"] = self._logged_channel.unary_unary(
                "/google.cloud.biglake.hive.v1beta.HiveMetastoreService/UpdateHiveDatabase",
                request_serializer=hive_metastore.UpdateHiveDatabaseRequest.serialize,
                response_deserializer=hive_metastore.HiveDatabase.deserialize,
            )
        return self._stubs["update_hive_database"]

    @property
    def delete_hive_database(
        self,
    ) -> Callable[
        [hive_metastore.DeleteHiveDatabaseRequest], Awaitable[empty_pb2.Empty]
    ]:
        r"""Return a callable for the delete hive database method over gRPC.

        Deletes an existing database specified by the
        database name.

        Returns:
            Callable[[~.DeleteHiveDatabaseRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_hive_database" not in self._stubs:
            self._stubs["delete_hive_database"] = self._logged_channel.unary_unary(
                "/google.cloud.biglake.hive.v1beta.HiveMetastoreService/DeleteHiveDatabase",
                request_serializer=hive_metastore.DeleteHiveDatabaseRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_hive_database"]

    @property
    def create_hive_table(
        self,
    ) -> Callable[
        [hive_metastore.CreateHiveTableRequest], Awaitable[hive_metastore.HiveTable]
    ]:
        r"""Return a callable for the create hive table method over gRPC.

        Creates a new hive table.

        Returns:
            Callable[[~.CreateHiveTableRequest],
                    Awaitable[~.HiveTable]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_hive_table" not in self._stubs:
            self._stubs["create_hive_table"] = self._logged_channel.unary_unary(
                "/google.cloud.biglake.hive.v1beta.HiveMetastoreService/CreateHiveTable",
                request_serializer=hive_metastore.CreateHiveTableRequest.serialize,
                response_deserializer=hive_metastore.HiveTable.deserialize,
            )
        return self._stubs["create_hive_table"]

    @property
    def get_hive_table(
        self,
    ) -> Callable[
        [hive_metastore.GetHiveTableRequest], Awaitable[hive_metastore.HiveTable]
    ]:
        r"""Return a callable for the get hive table method over gRPC.

        Gets the table specified by the resource name.

        Returns:
            Callable[[~.GetHiveTableRequest],
                    Awaitable[~.HiveTable]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_hive_table" not in self._stubs:
            self._stubs["get_hive_table"] = self._logged_channel.unary_unary(
                "/google.cloud.biglake.hive.v1beta.HiveMetastoreService/GetHiveTable",
                request_serializer=hive_metastore.GetHiveTableRequest.serialize,
                response_deserializer=hive_metastore.HiveTable.deserialize,
            )
        return self._stubs["get_hive_table"]

    @property
    def list_hive_tables(
        self,
    ) -> Callable[
        [hive_metastore.ListHiveTablesRequest],
        Awaitable[hive_metastore.ListHiveTablesResponse],
    ]:
        r"""Return a callable for the list hive tables method over gRPC.

        List all hive tables in a specified project under the
        hive catalog and database.

        Returns:
            Callable[[~.ListHiveTablesRequest],
                    Awaitable[~.ListHiveTablesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_hive_tables" not in self._stubs:
            self._stubs["list_hive_tables"] = self._logged_channel.unary_unary(
                "/google.cloud.biglake.hive.v1beta.HiveMetastoreService/ListHiveTables",
                request_serializer=hive_metastore.ListHiveTablesRequest.serialize,
                response_deserializer=hive_metastore.ListHiveTablesResponse.deserialize,
            )
        return self._stubs["list_hive_tables"]

    @property
    def update_hive_table(
        self,
    ) -> Callable[
        [hive_metastore.UpdateHiveTableRequest], Awaitable[hive_metastore.HiveTable]
    ]:
        r"""Return a callable for the update hive table method over gRPC.

        Updates an existing table specified by the table
        name.

        Returns:
            Callable[[~.UpdateHiveTableRequest],
                    Awaitable[~.HiveTable]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_hive_table" not in self._stubs:
            self._stubs["update_hive_table"] = self._logged_channel.unary_unary(
                "/google.cloud.biglake.hive.v1beta.HiveMetastoreService/UpdateHiveTable",
                request_serializer=hive_metastore.UpdateHiveTableRequest.serialize,
                response_deserializer=hive_metastore.HiveTable.deserialize,
            )
        return self._stubs["update_hive_table"]

    @property
    def delete_hive_table(
        self,
    ) -> Callable[[hive_metastore.DeleteHiveTableRequest], Awaitable[empty_pb2.Empty]]:
        r"""Return a callable for the delete hive table method over gRPC.

        Deletes an existing table specified by the table
        name.

        Returns:
            Callable[[~.DeleteHiveTableRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_hive_table" not in self._stubs:
            self._stubs["delete_hive_table"] = self._logged_channel.unary_unary(
                "/google.cloud.biglake.hive.v1beta.HiveMetastoreService/DeleteHiveTable",
                request_serializer=hive_metastore.DeleteHiveTableRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_hive_table"]

    @property
    def batch_create_partitions(
        self,
    ) -> Callable[
        [hive_metastore.BatchCreatePartitionsRequest],
        Awaitable[hive_metastore.BatchCreatePartitionsResponse],
    ]:
        r"""Return a callable for the batch create partitions method over gRPC.

        Adds partitions to a table.

        Returns:
            Callable[[~.BatchCreatePartitionsRequest],
                    Awaitable[~.BatchCreatePartitionsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "batch_create_partitions" not in self._stubs:
            self._stubs["batch_create_partitions"] = self._logged_channel.unary_unary(
                "/google.cloud.biglake.hive.v1beta.HiveMetastoreService/BatchCreatePartitions",
                request_serializer=hive_metastore.BatchCreatePartitionsRequest.serialize,
                response_deserializer=hive_metastore.BatchCreatePartitionsResponse.deserialize,
            )
        return self._stubs["batch_create_partitions"]

    @property
    def batch_delete_partitions(
        self,
    ) -> Callable[
        [hive_metastore.BatchDeletePartitionsRequest], Awaitable[empty_pb2.Empty]
    ]:
        r"""Return a callable for the batch delete partitions method over gRPC.

        Deletes partitions from a table.

        Returns:
            Callable[[~.BatchDeletePartitionsRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "batch_delete_partitions" not in self._stubs:
            self._stubs["batch_delete_partitions"] = self._logged_channel.unary_unary(
                "/google.cloud.biglake.hive.v1beta.HiveMetastoreService/BatchDeletePartitions",
                request_serializer=hive_metastore.BatchDeletePartitionsRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["batch_delete_partitions"]

    @property
    def batch_update_partitions(
        self,
    ) -> Callable[
        [hive_metastore.BatchUpdatePartitionsRequest],
        Awaitable[hive_metastore.BatchUpdatePartitionsResponse],
    ]:
        r"""Return a callable for the batch update partitions method over gRPC.

        Updates partitions in a table.

        Returns:
            Callable[[~.BatchUpdatePartitionsRequest],
                    Awaitable[~.BatchUpdatePartitionsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "batch_update_partitions" not in self._stubs:
            self._stubs["batch_update_partitions"] = self._logged_channel.unary_unary(
                "/google.cloud.biglake.hive.v1beta.HiveMetastoreService/BatchUpdatePartitions",
                request_serializer=hive_metastore.BatchUpdatePartitionsRequest.serialize,
                response_deserializer=hive_metastore.BatchUpdatePartitionsResponse.deserialize,
            )
        return self._stubs["batch_update_partitions"]

    @property
    def list_partitions(
        self,
    ) -> Callable[
        [hive_metastore.ListPartitionsRequest],
        Awaitable[hive_metastore.ListPartitionsResponse],
    ]:
        r"""Return a callable for the list partitions method over gRPC.

        Streams list of partitions from a table.

        Returns:
            Callable[[~.ListPartitionsRequest],
                    Awaitable[~.ListPartitionsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_partitions" not in self._stubs:
            self._stubs["list_partitions"] = self._logged_channel.unary_stream(
                "/google.cloud.biglake.hive.v1beta.HiveMetastoreService/ListPartitions",
                request_serializer=hive_metastore.ListPartitionsRequest.serialize,
                response_deserializer=hive_metastore.ListPartitionsResponse.deserialize,
            )
        return self._stubs["list_partitions"]

    @property
    def failover_hive_catalog(
        self,
    ) -> Callable[
        [hive_metastore.FailoverHiveCatalogRequest],
        Awaitable[hive_metastore.FailoverHiveCatalogResponse],
    ]:
        r"""Return a callable for the failover hive catalog method over gRPC.

        Failover the catalog to a new primary replica region.

        Returns:
            Callable[[~.FailoverHiveCatalogRequest],
                    Awaitable[~.FailoverHiveCatalogResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "failover_hive_catalog" not in self._stubs:
            self._stubs["failover_hive_catalog"] = self._logged_channel.unary_unary(
                "/google.cloud.biglake.hive.v1beta.HiveMetastoreService/FailoverHiveCatalog",
                request_serializer=hive_metastore.FailoverHiveCatalogRequest.serialize,
                response_deserializer=hive_metastore.FailoverHiveCatalogResponse.deserialize,
            )
        return self._stubs["failover_hive_catalog"]

    def _prep_wrapped_messages(self, client_info):
        """Precompute the wrapped methods, overriding the base class method to use async wrappers."""
        self._wrapped_methods = {
            self.create_hive_catalog: self._wrap_method(
                self.create_hive_catalog,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_hive_catalog: self._wrap_method(
                self.get_hive_catalog,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_hive_catalogs: self._wrap_method(
                self.list_hive_catalogs,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_hive_catalog: self._wrap_method(
                self.update_hive_catalog,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_hive_catalog: self._wrap_method(
                self.delete_hive_catalog,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_hive_database: self._wrap_method(
                self.create_hive_database,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_hive_database: self._wrap_method(
                self.get_hive_database,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_hive_databases: self._wrap_method(
                self.list_hive_databases,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_hive_database: self._wrap_method(
                self.update_hive_database,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_hive_database: self._wrap_method(
                self.delete_hive_database,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_hive_table: self._wrap_method(
                self.create_hive_table,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_hive_table: self._wrap_method(
                self.get_hive_table,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_hive_tables: self._wrap_method(
                self.list_hive_tables,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_hive_table: self._wrap_method(
                self.update_hive_table,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_hive_table: self._wrap_method(
                self.delete_hive_table,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_create_partitions: self._wrap_method(
                self.batch_create_partitions,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_delete_partitions: self._wrap_method(
                self.batch_delete_partitions,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_update_partitions: self._wrap_method(
                self.batch_update_partitions,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_partitions: self._wrap_method(
                self.list_partitions,
                default_timeout=None,
                client_info=client_info,
            ),
            self.failover_hive_catalog: self._wrap_method(
                self.failover_hive_catalog,
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


__all__ = ("HiveMetastoreServiceGrpcAsyncIOTransport",)
