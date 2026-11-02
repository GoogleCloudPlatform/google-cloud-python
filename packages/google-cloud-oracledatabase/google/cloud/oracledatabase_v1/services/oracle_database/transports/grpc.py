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

from google.cloud.oracledatabase_v1.types import (
    autonomous_database,
    database,
    database_character_set,
    db_system,
    db_system_initial_storage_size,
    db_version,
    exadata_infra,
    exadb_vm_cluster,
    exascale_db_storage_vault,
    goldengate_connection,
    goldengate_connection_assignment,
    goldengate_connection_type,
    goldengate_deployment,
    goldengate_deployment_environment,
    goldengate_deployment_type,
    goldengate_deployment_version,
    minor_version,
    odb_dns_zone,
    odb_network,
    odb_subnet,
    oracledatabase,
    pluggable_database,
    vm_cluster,
)
from google.cloud.oracledatabase_v1.types import db_system as gco_db_system
from google.cloud.oracledatabase_v1.types import (
    exascale_db_storage_vault as gco_exascale_db_storage_vault,
)
from google.cloud.oracledatabase_v1.types import (
    goldengate_connection as gco_goldengate_connection,
)
from google.cloud.oracledatabase_v1.types import (
    goldengate_connection_assignment as gco_goldengate_connection_assignment,
)
from google.cloud.oracledatabase_v1.types import (
    goldengate_deployment as gco_goldengate_deployment,
)
from google.cloud.oracledatabase_v1.types import odb_dns_zone as gco_odb_dns_zone
from google.cloud.oracledatabase_v1.types import odb_network as gco_odb_network
from google.cloud.oracledatabase_v1.types import odb_subnet as gco_odb_subnet

from .base import DEFAULT_CLIENT_INFO, OracleDatabaseTransport

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
                    "serviceName": "google.cloud.oracledatabase.v1.OracleDatabase",
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
                    "serviceName": "google.cloud.oracledatabase.v1.OracleDatabase",
                    "rpcName": client_call_details.method,
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class OracleDatabaseGrpcTransport(OracleDatabaseTransport):
    """gRPC backend transport for OracleDatabase.

    Service describing handlers for resources

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
        host: str = "oracledatabase.googleapis.com",
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
                 The hostname to connect to (default: 'oracledatabase.googleapis.com').
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
        host: str = "oracledatabase.googleapis.com",
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
    def list_cloud_exadata_infrastructures(
        self,
    ) -> Callable[
        [oracledatabase.ListCloudExadataInfrastructuresRequest],
        oracledatabase.ListCloudExadataInfrastructuresResponse,
    ]:
        r"""Return a callable for the list cloud exadata
        infrastructures method over gRPC.

        Lists Exadata Infrastructures in a given project and
        location.

        Returns:
            Callable[[~.ListCloudExadataInfrastructuresRequest],
                    ~.ListCloudExadataInfrastructuresResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_cloud_exadata_infrastructures" not in self._stubs:
            self._stubs["list_cloud_exadata_infrastructures"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.oracledatabase.v1.OracleDatabase/ListCloudExadataInfrastructures",
                    request_serializer=oracledatabase.ListCloudExadataInfrastructuresRequest.serialize,
                    response_deserializer=oracledatabase.ListCloudExadataInfrastructuresResponse.deserialize,
                )
            )
        return self._stubs["list_cloud_exadata_infrastructures"]

    @property
    def get_cloud_exadata_infrastructure(
        self,
    ) -> Callable[
        [oracledatabase.GetCloudExadataInfrastructureRequest],
        exadata_infra.CloudExadataInfrastructure,
    ]:
        r"""Return a callable for the get cloud exadata
        infrastructure method over gRPC.

        Gets details of a single Exadata Infrastructure.

        Returns:
            Callable[[~.GetCloudExadataInfrastructureRequest],
                    ~.CloudExadataInfrastructure]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_cloud_exadata_infrastructure" not in self._stubs:
            self._stubs["get_cloud_exadata_infrastructure"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.oracledatabase.v1.OracleDatabase/GetCloudExadataInfrastructure",
                    request_serializer=oracledatabase.GetCloudExadataInfrastructureRequest.serialize,
                    response_deserializer=exadata_infra.CloudExadataInfrastructure.deserialize,
                )
            )
        return self._stubs["get_cloud_exadata_infrastructure"]

    @property
    def create_cloud_exadata_infrastructure(
        self,
    ) -> Callable[
        [oracledatabase.CreateCloudExadataInfrastructureRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the create cloud exadata
        infrastructure method over gRPC.

        Creates a new Exadata Infrastructure in a given
        project and location.

        Returns:
            Callable[[~.CreateCloudExadataInfrastructureRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_cloud_exadata_infrastructure" not in self._stubs:
            self._stubs["create_cloud_exadata_infrastructure"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.oracledatabase.v1.OracleDatabase/CreateCloudExadataInfrastructure",
                    request_serializer=oracledatabase.CreateCloudExadataInfrastructureRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["create_cloud_exadata_infrastructure"]

    @property
    def delete_cloud_exadata_infrastructure(
        self,
    ) -> Callable[
        [oracledatabase.DeleteCloudExadataInfrastructureRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the delete cloud exadata
        infrastructure method over gRPC.

        Deletes a single Exadata Infrastructure.

        Returns:
            Callable[[~.DeleteCloudExadataInfrastructureRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_cloud_exadata_infrastructure" not in self._stubs:
            self._stubs["delete_cloud_exadata_infrastructure"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.oracledatabase.v1.OracleDatabase/DeleteCloudExadataInfrastructure",
                    request_serializer=oracledatabase.DeleteCloudExadataInfrastructureRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["delete_cloud_exadata_infrastructure"]

    @property
    def configure_exascale_cloud_exadata_infrastructure(
        self,
    ) -> Callable[
        [exadata_infra.ConfigureExascaleCloudExadataInfrastructureRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the configure exascale cloud
        exadata infrastructure method over gRPC.

        Configures Exascale for a single Exadata
        Infrastructure.

        Returns:
            Callable[[~.ConfigureExascaleCloudExadataInfrastructureRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "configure_exascale_cloud_exadata_infrastructure" not in self._stubs:
            self._stubs["configure_exascale_cloud_exadata_infrastructure"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.oracledatabase.v1.OracleDatabase/ConfigureExascaleCloudExadataInfrastructure",
                    request_serializer=exadata_infra.ConfigureExascaleCloudExadataInfrastructureRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["configure_exascale_cloud_exadata_infrastructure"]

    @property
    def list_cloud_vm_clusters(
        self,
    ) -> Callable[
        [oracledatabase.ListCloudVmClustersRequest],
        oracledatabase.ListCloudVmClustersResponse,
    ]:
        r"""Return a callable for the list cloud vm clusters method over gRPC.

        Lists the VM Clusters in a given project and
        location.

        Returns:
            Callable[[~.ListCloudVmClustersRequest],
                    ~.ListCloudVmClustersResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_cloud_vm_clusters" not in self._stubs:
            self._stubs["list_cloud_vm_clusters"] = self._logged_channel.unary_unary(
                "/google.cloud.oracledatabase.v1.OracleDatabase/ListCloudVmClusters",
                request_serializer=oracledatabase.ListCloudVmClustersRequest.serialize,
                response_deserializer=oracledatabase.ListCloudVmClustersResponse.deserialize,
            )
        return self._stubs["list_cloud_vm_clusters"]

    @property
    def get_cloud_vm_cluster(
        self,
    ) -> Callable[[oracledatabase.GetCloudVmClusterRequest], vm_cluster.CloudVmCluster]:
        r"""Return a callable for the get cloud vm cluster method over gRPC.

        Gets details of a single VM Cluster.

        Returns:
            Callable[[~.GetCloudVmClusterRequest],
                    ~.CloudVmCluster]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_cloud_vm_cluster" not in self._stubs:
            self._stubs["get_cloud_vm_cluster"] = self._logged_channel.unary_unary(
                "/google.cloud.oracledatabase.v1.OracleDatabase/GetCloudVmCluster",
                request_serializer=oracledatabase.GetCloudVmClusterRequest.serialize,
                response_deserializer=vm_cluster.CloudVmCluster.deserialize,
            )
        return self._stubs["get_cloud_vm_cluster"]

    @property
    def create_cloud_vm_cluster(
        self,
    ) -> Callable[
        [oracledatabase.CreateCloudVmClusterRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the create cloud vm cluster method over gRPC.

        Creates a new VM Cluster in a given project and
        location.

        Returns:
            Callable[[~.CreateCloudVmClusterRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_cloud_vm_cluster" not in self._stubs:
            self._stubs["create_cloud_vm_cluster"] = self._logged_channel.unary_unary(
                "/google.cloud.oracledatabase.v1.OracleDatabase/CreateCloudVmCluster",
                request_serializer=oracledatabase.CreateCloudVmClusterRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_cloud_vm_cluster"]

    @property
    def delete_cloud_vm_cluster(
        self,
    ) -> Callable[
        [oracledatabase.DeleteCloudVmClusterRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the delete cloud vm cluster method over gRPC.

        Deletes a single VM Cluster.

        Returns:
            Callable[[~.DeleteCloudVmClusterRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_cloud_vm_cluster" not in self._stubs:
            self._stubs["delete_cloud_vm_cluster"] = self._logged_channel.unary_unary(
                "/google.cloud.oracledatabase.v1.OracleDatabase/DeleteCloudVmCluster",
                request_serializer=oracledatabase.DeleteCloudVmClusterRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_cloud_vm_cluster"]

    @property
    def list_entitlements(
        self,
    ) -> Callable[
        [oracledatabase.ListEntitlementsRequest],
        oracledatabase.ListEntitlementsResponse,
    ]:
        r"""Return a callable for the list entitlements method over gRPC.

        Lists the entitlements in a given project.

        Returns:
            Callable[[~.ListEntitlementsRequest],
                    ~.ListEntitlementsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_entitlements" not in self._stubs:
            self._stubs["list_entitlements"] = self._logged_channel.unary_unary(
                "/google.cloud.oracledatabase.v1.OracleDatabase/ListEntitlements",
                request_serializer=oracledatabase.ListEntitlementsRequest.serialize,
                response_deserializer=oracledatabase.ListEntitlementsResponse.deserialize,
            )
        return self._stubs["list_entitlements"]

    @property
    def list_db_servers(
        self,
    ) -> Callable[
        [oracledatabase.ListDbServersRequest], oracledatabase.ListDbServersResponse
    ]:
        r"""Return a callable for the list db servers method over gRPC.

        Lists the database servers of an Exadata
        Infrastructure instance.

        Returns:
            Callable[[~.ListDbServersRequest],
                    ~.ListDbServersResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_db_servers" not in self._stubs:
            self._stubs["list_db_servers"] = self._logged_channel.unary_unary(
                "/google.cloud.oracledatabase.v1.OracleDatabase/ListDbServers",
                request_serializer=oracledatabase.ListDbServersRequest.serialize,
                response_deserializer=oracledatabase.ListDbServersResponse.deserialize,
            )
        return self._stubs["list_db_servers"]

    @property
    def list_db_nodes(
        self,
    ) -> Callable[
        [oracledatabase.ListDbNodesRequest], oracledatabase.ListDbNodesResponse
    ]:
        r"""Return a callable for the list db nodes method over gRPC.

        Lists the database nodes of a VM Cluster.

        Returns:
            Callable[[~.ListDbNodesRequest],
                    ~.ListDbNodesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_db_nodes" not in self._stubs:
            self._stubs["list_db_nodes"] = self._logged_channel.unary_unary(
                "/google.cloud.oracledatabase.v1.OracleDatabase/ListDbNodes",
                request_serializer=oracledatabase.ListDbNodesRequest.serialize,
                response_deserializer=oracledatabase.ListDbNodesResponse.deserialize,
            )
        return self._stubs["list_db_nodes"]

    @property
    def list_gi_versions(
        self,
    ) -> Callable[
        [oracledatabase.ListGiVersionsRequest], oracledatabase.ListGiVersionsResponse
    ]:
        r"""Return a callable for the list gi versions method over gRPC.

        Lists all the valid Oracle Grid Infrastructure (GI)
        versions for the given project and location.

        Returns:
            Callable[[~.ListGiVersionsRequest],
                    ~.ListGiVersionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_gi_versions" not in self._stubs:
            self._stubs["list_gi_versions"] = self._logged_channel.unary_unary(
                "/google.cloud.oracledatabase.v1.OracleDatabase/ListGiVersions",
                request_serializer=oracledatabase.ListGiVersionsRequest.serialize,
                response_deserializer=oracledatabase.ListGiVersionsResponse.deserialize,
            )
        return self._stubs["list_gi_versions"]

    @property
    def list_minor_versions(
        self,
    ) -> Callable[
        [minor_version.ListMinorVersionsRequest],
        minor_version.ListMinorVersionsResponse,
    ]:
        r"""Return a callable for the list minor versions method over gRPC.

        Lists all the valid minor versions for the given
        project, location, gi version and shape family.

        Returns:
            Callable[[~.ListMinorVersionsRequest],
                    ~.ListMinorVersionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_minor_versions" not in self._stubs:
            self._stubs["list_minor_versions"] = self._logged_channel.unary_unary(
                "/google.cloud.oracledatabase.v1.OracleDatabase/ListMinorVersions",
                request_serializer=minor_version.ListMinorVersionsRequest.serialize,
                response_deserializer=minor_version.ListMinorVersionsResponse.deserialize,
            )
        return self._stubs["list_minor_versions"]

    @property
    def list_db_system_shapes(
        self,
    ) -> Callable[
        [oracledatabase.ListDbSystemShapesRequest],
        oracledatabase.ListDbSystemShapesResponse,
    ]:
        r"""Return a callable for the list db system shapes method over gRPC.

        Lists the database system shapes available for the
        project and location.

        Returns:
            Callable[[~.ListDbSystemShapesRequest],
                    ~.ListDbSystemShapesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_db_system_shapes" not in self._stubs:
            self._stubs["list_db_system_shapes"] = self._logged_channel.unary_unary(
                "/google.cloud.oracledatabase.v1.OracleDatabase/ListDbSystemShapes",
                request_serializer=oracledatabase.ListDbSystemShapesRequest.serialize,
                response_deserializer=oracledatabase.ListDbSystemShapesResponse.deserialize,
            )
        return self._stubs["list_db_system_shapes"]

    @property
    def list_autonomous_databases(
        self,
    ) -> Callable[
        [oracledatabase.ListAutonomousDatabasesRequest],
        oracledatabase.ListAutonomousDatabasesResponse,
    ]:
        r"""Return a callable for the list autonomous databases method over gRPC.

        Lists the Autonomous Databases in a given project and
        location.

        Returns:
            Callable[[~.ListAutonomousDatabasesRequest],
                    ~.ListAutonomousDatabasesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_autonomous_databases" not in self._stubs:
            self._stubs["list_autonomous_databases"] = self._logged_channel.unary_unary(
                "/google.cloud.oracledatabase.v1.OracleDatabase/ListAutonomousDatabases",
                request_serializer=oracledatabase.ListAutonomousDatabasesRequest.serialize,
                response_deserializer=oracledatabase.ListAutonomousDatabasesResponse.deserialize,
            )
        return self._stubs["list_autonomous_databases"]

    @property
    def get_autonomous_database(
        self,
    ) -> Callable[
        [oracledatabase.GetAutonomousDatabaseRequest],
        autonomous_database.AutonomousDatabase,
    ]:
        r"""Return a callable for the get autonomous database method over gRPC.

        Gets the details of a single Autonomous Database.

        Returns:
            Callable[[~.GetAutonomousDatabaseRequest],
                    ~.AutonomousDatabase]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_autonomous_database" not in self._stubs:
            self._stubs["get_autonomous_database"] = self._logged_channel.unary_unary(
                "/google.cloud.oracledatabase.v1.OracleDatabase/GetAutonomousDatabase",
                request_serializer=oracledatabase.GetAutonomousDatabaseRequest.serialize,
                response_deserializer=autonomous_database.AutonomousDatabase.deserialize,
            )
        return self._stubs["get_autonomous_database"]

    @property
    def create_autonomous_database(
        self,
    ) -> Callable[
        [oracledatabase.CreateAutonomousDatabaseRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the create autonomous database method over gRPC.

        Creates a new Autonomous Database in a given project
        and location.

        Returns:
            Callable[[~.CreateAutonomousDatabaseRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_autonomous_database" not in self._stubs:
            self._stubs["create_autonomous_database"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.oracledatabase.v1.OracleDatabase/CreateAutonomousDatabase",
                    request_serializer=oracledatabase.CreateAutonomousDatabaseRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["create_autonomous_database"]

    @property
    def update_autonomous_database(
        self,
    ) -> Callable[
        [oracledatabase.UpdateAutonomousDatabaseRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the update autonomous database method over gRPC.

        Updates the parameters of a single Autonomous
        Database.

        Returns:
            Callable[[~.UpdateAutonomousDatabaseRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_autonomous_database" not in self._stubs:
            self._stubs["update_autonomous_database"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.oracledatabase.v1.OracleDatabase/UpdateAutonomousDatabase",
                    request_serializer=oracledatabase.UpdateAutonomousDatabaseRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["update_autonomous_database"]

    @property
    def delete_autonomous_database(
        self,
    ) -> Callable[
        [oracledatabase.DeleteAutonomousDatabaseRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the delete autonomous database method over gRPC.

        Deletes a single Autonomous Database.

        Returns:
            Callable[[~.DeleteAutonomousDatabaseRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_autonomous_database" not in self._stubs:
            self._stubs["delete_autonomous_database"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.oracledatabase.v1.OracleDatabase/DeleteAutonomousDatabase",
                    request_serializer=oracledatabase.DeleteAutonomousDatabaseRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["delete_autonomous_database"]

    @property
    def restore_autonomous_database(
        self,
    ) -> Callable[
        [oracledatabase.RestoreAutonomousDatabaseRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the restore autonomous database method over gRPC.

        Restores a single Autonomous Database.

        Returns:
            Callable[[~.RestoreAutonomousDatabaseRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "restore_autonomous_database" not in self._stubs:
            self._stubs["restore_autonomous_database"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.oracledatabase.v1.OracleDatabase/RestoreAutonomousDatabase",
                    request_serializer=oracledatabase.RestoreAutonomousDatabaseRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["restore_autonomous_database"]

    @property
    def generate_autonomous_database_wallet(
        self,
    ) -> Callable[
        [oracledatabase.GenerateAutonomousDatabaseWalletRequest],
        oracledatabase.GenerateAutonomousDatabaseWalletResponse,
    ]:
        r"""Return a callable for the generate autonomous database
        wallet method over gRPC.

        Generates a wallet for an Autonomous Database.

        Returns:
            Callable[[~.GenerateAutonomousDatabaseWalletRequest],
                    ~.GenerateAutonomousDatabaseWalletResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "generate_autonomous_database_wallet" not in self._stubs:
            self._stubs["generate_autonomous_database_wallet"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.oracledatabase.v1.OracleDatabase/GenerateAutonomousDatabaseWallet",
                    request_serializer=oracledatabase.GenerateAutonomousDatabaseWalletRequest.serialize,
                    response_deserializer=oracledatabase.GenerateAutonomousDatabaseWalletResponse.deserialize,
                )
            )
        return self._stubs["generate_autonomous_database_wallet"]

    @property
    def list_autonomous_db_versions(
        self,
    ) -> Callable[
        [oracledatabase.ListAutonomousDbVersionsRequest],
        oracledatabase.ListAutonomousDbVersionsResponse,
    ]:
        r"""Return a callable for the list autonomous db versions method over gRPC.

        Lists all the available Autonomous Database versions
        for a project and location.

        Returns:
            Callable[[~.ListAutonomousDbVersionsRequest],
                    ~.ListAutonomousDbVersionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_autonomous_db_versions" not in self._stubs:
            self._stubs["list_autonomous_db_versions"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.oracledatabase.v1.OracleDatabase/ListAutonomousDbVersions",
                    request_serializer=oracledatabase.ListAutonomousDbVersionsRequest.serialize,
                    response_deserializer=oracledatabase.ListAutonomousDbVersionsResponse.deserialize,
                )
            )
        return self._stubs["list_autonomous_db_versions"]

    @property
    def list_autonomous_database_character_sets(
        self,
    ) -> Callable[
        [oracledatabase.ListAutonomousDatabaseCharacterSetsRequest],
        oracledatabase.ListAutonomousDatabaseCharacterSetsResponse,
    ]:
        r"""Return a callable for the list autonomous database
        character sets method over gRPC.

        Lists Autonomous Database Character Sets in a given
        project and location.

        Returns:
            Callable[[~.ListAutonomousDatabaseCharacterSetsRequest],
                    ~.ListAutonomousDatabaseCharacterSetsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_autonomous_database_character_sets" not in self._stubs:
            self._stubs["list_autonomous_database_character_sets"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.oracledatabase.v1.OracleDatabase/ListAutonomousDatabaseCharacterSets",
                    request_serializer=oracledatabase.ListAutonomousDatabaseCharacterSetsRequest.serialize,
                    response_deserializer=oracledatabase.ListAutonomousDatabaseCharacterSetsResponse.deserialize,
                )
            )
        return self._stubs["list_autonomous_database_character_sets"]

    @property
    def list_autonomous_database_backups(
        self,
    ) -> Callable[
        [oracledatabase.ListAutonomousDatabaseBackupsRequest],
        oracledatabase.ListAutonomousDatabaseBackupsResponse,
    ]:
        r"""Return a callable for the list autonomous database
        backups method over gRPC.

        Lists the long-term and automatic backups of an
        Autonomous Database.

        Returns:
            Callable[[~.ListAutonomousDatabaseBackupsRequest],
                    ~.ListAutonomousDatabaseBackupsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_autonomous_database_backups" not in self._stubs:
            self._stubs["list_autonomous_database_backups"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.oracledatabase.v1.OracleDatabase/ListAutonomousDatabaseBackups",
                    request_serializer=oracledatabase.ListAutonomousDatabaseBackupsRequest.serialize,
                    response_deserializer=oracledatabase.ListAutonomousDatabaseBackupsResponse.deserialize,
                )
            )
        return self._stubs["list_autonomous_database_backups"]

    @property
    def stop_autonomous_database(
        self,
    ) -> Callable[
        [oracledatabase.StopAutonomousDatabaseRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the stop autonomous database method over gRPC.

        Stops an Autonomous Database.

        Returns:
            Callable[[~.StopAutonomousDatabaseRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "stop_autonomous_database" not in self._stubs:
            self._stubs["stop_autonomous_database"] = self._logged_channel.unary_unary(
                "/google.cloud.oracledatabase.v1.OracleDatabase/StopAutonomousDatabase",
                request_serializer=oracledatabase.StopAutonomousDatabaseRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["stop_autonomous_database"]

    @property
    def start_autonomous_database(
        self,
    ) -> Callable[
        [oracledatabase.StartAutonomousDatabaseRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the start autonomous database method over gRPC.

        Starts an Autonomous Database.

        Returns:
            Callable[[~.StartAutonomousDatabaseRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "start_autonomous_database" not in self._stubs:
            self._stubs["start_autonomous_database"] = self._logged_channel.unary_unary(
                "/google.cloud.oracledatabase.v1.OracleDatabase/StartAutonomousDatabase",
                request_serializer=oracledatabase.StartAutonomousDatabaseRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["start_autonomous_database"]

    @property
    def restart_autonomous_database(
        self,
    ) -> Callable[
        [oracledatabase.RestartAutonomousDatabaseRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the restart autonomous database method over gRPC.

        Restarts an Autonomous Database.

        Returns:
            Callable[[~.RestartAutonomousDatabaseRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "restart_autonomous_database" not in self._stubs:
            self._stubs["restart_autonomous_database"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.oracledatabase.v1.OracleDatabase/RestartAutonomousDatabase",
                    request_serializer=oracledatabase.RestartAutonomousDatabaseRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["restart_autonomous_database"]

    @property
    def switchover_autonomous_database(
        self,
    ) -> Callable[
        [oracledatabase.SwitchoverAutonomousDatabaseRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the switchover autonomous database method over gRPC.

        Initiates a switchover of specified autonomous
        database to the associated peer database.

        Returns:
            Callable[[~.SwitchoverAutonomousDatabaseRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "switchover_autonomous_database" not in self._stubs:
            self._stubs["switchover_autonomous_database"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.oracledatabase.v1.OracleDatabase/SwitchoverAutonomousDatabase",
                    request_serializer=oracledatabase.SwitchoverAutonomousDatabaseRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["switchover_autonomous_database"]

    @property
    def failover_autonomous_database(
        self,
    ) -> Callable[
        [oracledatabase.FailoverAutonomousDatabaseRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the failover autonomous database method over gRPC.

        Initiates a failover to target autonomous database
        from the associated primary database.

        Returns:
            Callable[[~.FailoverAutonomousDatabaseRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "failover_autonomous_database" not in self._stubs:
            self._stubs["failover_autonomous_database"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.oracledatabase.v1.OracleDatabase/FailoverAutonomousDatabase",
                    request_serializer=oracledatabase.FailoverAutonomousDatabaseRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["failover_autonomous_database"]

    @property
    def refresh_autonomous_database(
        self,
    ) -> Callable[
        [oracledatabase.RefreshAutonomousDatabaseRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the refresh autonomous database method over gRPC.

        Refreshes the refreshable clone of an Autonomous
        Database.

        Returns:
            Callable[[~.RefreshAutonomousDatabaseRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "refresh_autonomous_database" not in self._stubs:
            self._stubs["refresh_autonomous_database"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.oracledatabase.v1.OracleDatabase/RefreshAutonomousDatabase",
                    request_serializer=oracledatabase.RefreshAutonomousDatabaseRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["refresh_autonomous_database"]

    @property
    def get_autonomous_database_refreshable_clones(
        self,
    ) -> Callable[
        [oracledatabase.GetAutonomousDatabaseRefreshableClonesRequest],
        oracledatabase.AutonomousDatabaseRefreshableClones,
    ]:
        r"""Return a callable for the get autonomous database
        refreshable clones method over gRPC.

        Gets the refreshable clones for a given Autonomous
        Database.

        Returns:
            Callable[[~.GetAutonomousDatabaseRefreshableClonesRequest],
                    ~.AutonomousDatabaseRefreshableClones]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_autonomous_database_refreshable_clones" not in self._stubs:
            self._stubs["get_autonomous_database_refreshable_clones"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.oracledatabase.v1.OracleDatabase/GetAutonomousDatabaseRefreshableClones",
                    request_serializer=oracledatabase.GetAutonomousDatabaseRefreshableClonesRequest.serialize,
                    response_deserializer=oracledatabase.AutonomousDatabaseRefreshableClones.deserialize,
                )
            )
        return self._stubs["get_autonomous_database_refreshable_clones"]

    @property
    def list_odb_networks(
        self,
    ) -> Callable[
        [odb_network.ListOdbNetworksRequest], odb_network.ListOdbNetworksResponse
    ]:
        r"""Return a callable for the list odb networks method over gRPC.

        Lists the ODB Networks in a given project and
        location.

        Returns:
            Callable[[~.ListOdbNetworksRequest],
                    ~.ListOdbNetworksResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_odb_networks" not in self._stubs:
            self._stubs["list_odb_networks"] = self._logged_channel.unary_unary(
                "/google.cloud.oracledatabase.v1.OracleDatabase/ListOdbNetworks",
                request_serializer=odb_network.ListOdbNetworksRequest.serialize,
                response_deserializer=odb_network.ListOdbNetworksResponse.deserialize,
            )
        return self._stubs["list_odb_networks"]

    @property
    def get_odb_network(
        self,
    ) -> Callable[[odb_network.GetOdbNetworkRequest], odb_network.OdbNetwork]:
        r"""Return a callable for the get odb network method over gRPC.

        Gets details of a single ODB Network.

        Returns:
            Callable[[~.GetOdbNetworkRequest],
                    ~.OdbNetwork]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_odb_network" not in self._stubs:
            self._stubs["get_odb_network"] = self._logged_channel.unary_unary(
                "/google.cloud.oracledatabase.v1.OracleDatabase/GetOdbNetwork",
                request_serializer=odb_network.GetOdbNetworkRequest.serialize,
                response_deserializer=odb_network.OdbNetwork.deserialize,
            )
        return self._stubs["get_odb_network"]

    @property
    def create_odb_network(
        self,
    ) -> Callable[[gco_odb_network.CreateOdbNetworkRequest], operations_pb2.Operation]:
        r"""Return a callable for the create odb network method over gRPC.

        Creates a new ODB Network in a given project and
        location.

        Returns:
            Callable[[~.CreateOdbNetworkRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_odb_network" not in self._stubs:
            self._stubs["create_odb_network"] = self._logged_channel.unary_unary(
                "/google.cloud.oracledatabase.v1.OracleDatabase/CreateOdbNetwork",
                request_serializer=gco_odb_network.CreateOdbNetworkRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_odb_network"]

    @property
    def delete_odb_network(
        self,
    ) -> Callable[[odb_network.DeleteOdbNetworkRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete odb network method over gRPC.

        Deletes a single ODB Network.

        Returns:
            Callable[[~.DeleteOdbNetworkRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_odb_network" not in self._stubs:
            self._stubs["delete_odb_network"] = self._logged_channel.unary_unary(
                "/google.cloud.oracledatabase.v1.OracleDatabase/DeleteOdbNetwork",
                request_serializer=odb_network.DeleteOdbNetworkRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_odb_network"]

    @property
    def list_odb_subnets(
        self,
    ) -> Callable[
        [odb_subnet.ListOdbSubnetsRequest], odb_subnet.ListOdbSubnetsResponse
    ]:
        r"""Return a callable for the list odb subnets method over gRPC.

        Lists all the ODB Subnets in a given ODB Network.

        Returns:
            Callable[[~.ListOdbSubnetsRequest],
                    ~.ListOdbSubnetsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_odb_subnets" not in self._stubs:
            self._stubs["list_odb_subnets"] = self._logged_channel.unary_unary(
                "/google.cloud.oracledatabase.v1.OracleDatabase/ListOdbSubnets",
                request_serializer=odb_subnet.ListOdbSubnetsRequest.serialize,
                response_deserializer=odb_subnet.ListOdbSubnetsResponse.deserialize,
            )
        return self._stubs["list_odb_subnets"]

    @property
    def get_odb_subnet(
        self,
    ) -> Callable[[odb_subnet.GetOdbSubnetRequest], odb_subnet.OdbSubnet]:
        r"""Return a callable for the get odb subnet method over gRPC.

        Gets details of a single ODB Subnet.

        Returns:
            Callable[[~.GetOdbSubnetRequest],
                    ~.OdbSubnet]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_odb_subnet" not in self._stubs:
            self._stubs["get_odb_subnet"] = self._logged_channel.unary_unary(
                "/google.cloud.oracledatabase.v1.OracleDatabase/GetOdbSubnet",
                request_serializer=odb_subnet.GetOdbSubnetRequest.serialize,
                response_deserializer=odb_subnet.OdbSubnet.deserialize,
            )
        return self._stubs["get_odb_subnet"]

    @property
    def create_odb_subnet(
        self,
    ) -> Callable[[gco_odb_subnet.CreateOdbSubnetRequest], operations_pb2.Operation]:
        r"""Return a callable for the create odb subnet method over gRPC.

        Creates a new ODB Subnet in a given ODB Network.

        Returns:
            Callable[[~.CreateOdbSubnetRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_odb_subnet" not in self._stubs:
            self._stubs["create_odb_subnet"] = self._logged_channel.unary_unary(
                "/google.cloud.oracledatabase.v1.OracleDatabase/CreateOdbSubnet",
                request_serializer=gco_odb_subnet.CreateOdbSubnetRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_odb_subnet"]

    @property
    def delete_odb_subnet(
        self,
    ) -> Callable[[odb_subnet.DeleteOdbSubnetRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete odb subnet method over gRPC.

        Deletes a single ODB Subnet.

        Returns:
            Callable[[~.DeleteOdbSubnetRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_odb_subnet" not in self._stubs:
            self._stubs["delete_odb_subnet"] = self._logged_channel.unary_unary(
                "/google.cloud.oracledatabase.v1.OracleDatabase/DeleteOdbSubnet",
                request_serializer=odb_subnet.DeleteOdbSubnetRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_odb_subnet"]

    @property
    def list_odb_dns_zones(
        self,
    ) -> Callable[
        [odb_dns_zone.ListOdbDnsZonesRequest], odb_dns_zone.ListOdbDnsZonesResponse
    ]:
        r"""Return a callable for the list odb dns zones method over gRPC.

        Lists all the ODB DNS Zones in a given ODB Network.

        Returns:
            Callable[[~.ListOdbDnsZonesRequest],
                    ~.ListOdbDnsZonesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_odb_dns_zones" not in self._stubs:
            self._stubs["list_odb_dns_zones"] = self._logged_channel.unary_unary(
                "/google.cloud.oracledatabase.v1.OracleDatabase/ListOdbDnsZones",
                request_serializer=odb_dns_zone.ListOdbDnsZonesRequest.serialize,
                response_deserializer=odb_dns_zone.ListOdbDnsZonesResponse.deserialize,
            )
        return self._stubs["list_odb_dns_zones"]

    @property
    def get_odb_dns_zone(
        self,
    ) -> Callable[[odb_dns_zone.GetOdbDnsZoneRequest], odb_dns_zone.OdbDnsZone]:
        r"""Return a callable for the get odb dns zone method over gRPC.

        Gets details of a single ODB DNS Zone.

        Returns:
            Callable[[~.GetOdbDnsZoneRequest],
                    ~.OdbDnsZone]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_odb_dns_zone" not in self._stubs:
            self._stubs["get_odb_dns_zone"] = self._logged_channel.unary_unary(
                "/google.cloud.oracledatabase.v1.OracleDatabase/GetOdbDnsZone",
                request_serializer=odb_dns_zone.GetOdbDnsZoneRequest.serialize,
                response_deserializer=odb_dns_zone.OdbDnsZone.deserialize,
            )
        return self._stubs["get_odb_dns_zone"]

    @property
    def create_odb_dns_zone(
        self,
    ) -> Callable[[gco_odb_dns_zone.CreateOdbDnsZoneRequest], operations_pb2.Operation]:
        r"""Return a callable for the create odb dns zone method over gRPC.

        Creates a new ODB DNS Zone in a given ODB Network.

        Returns:
            Callable[[~.CreateOdbDnsZoneRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_odb_dns_zone" not in self._stubs:
            self._stubs["create_odb_dns_zone"] = self._logged_channel.unary_unary(
                "/google.cloud.oracledatabase.v1.OracleDatabase/CreateOdbDnsZone",
                request_serializer=gco_odb_dns_zone.CreateOdbDnsZoneRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_odb_dns_zone"]

    @property
    def delete_odb_dns_zone(
        self,
    ) -> Callable[[odb_dns_zone.DeleteOdbDnsZoneRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete odb dns zone method over gRPC.

        Deletes a single ODB DNS Zone.

        Returns:
            Callable[[~.DeleteOdbDnsZoneRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_odb_dns_zone" not in self._stubs:
            self._stubs["delete_odb_dns_zone"] = self._logged_channel.unary_unary(
                "/google.cloud.oracledatabase.v1.OracleDatabase/DeleteOdbDnsZone",
                request_serializer=odb_dns_zone.DeleteOdbDnsZoneRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_odb_dns_zone"]

    @property
    def list_exadb_vm_clusters(
        self,
    ) -> Callable[
        [oracledatabase.ListExadbVmClustersRequest],
        oracledatabase.ListExadbVmClustersResponse,
    ]:
        r"""Return a callable for the list exadb vm clusters method over gRPC.

        Lists all the Exadb (Exascale) VM Clusters for the
        given project and location.

        Returns:
            Callable[[~.ListExadbVmClustersRequest],
                    ~.ListExadbVmClustersResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_exadb_vm_clusters" not in self._stubs:
            self._stubs["list_exadb_vm_clusters"] = self._logged_channel.unary_unary(
                "/google.cloud.oracledatabase.v1.OracleDatabase/ListExadbVmClusters",
                request_serializer=oracledatabase.ListExadbVmClustersRequest.serialize,
                response_deserializer=oracledatabase.ListExadbVmClustersResponse.deserialize,
            )
        return self._stubs["list_exadb_vm_clusters"]

    @property
    def get_exadb_vm_cluster(
        self,
    ) -> Callable[
        [oracledatabase.GetExadbVmClusterRequest], exadb_vm_cluster.ExadbVmCluster
    ]:
        r"""Return a callable for the get exadb vm cluster method over gRPC.

        Gets details of a single Exadb (Exascale) VM Cluster.

        Returns:
            Callable[[~.GetExadbVmClusterRequest],
                    ~.ExadbVmCluster]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_exadb_vm_cluster" not in self._stubs:
            self._stubs["get_exadb_vm_cluster"] = self._logged_channel.unary_unary(
                "/google.cloud.oracledatabase.v1.OracleDatabase/GetExadbVmCluster",
                request_serializer=oracledatabase.GetExadbVmClusterRequest.serialize,
                response_deserializer=exadb_vm_cluster.ExadbVmCluster.deserialize,
            )
        return self._stubs["get_exadb_vm_cluster"]

    @property
    def create_exadb_vm_cluster(
        self,
    ) -> Callable[
        [oracledatabase.CreateExadbVmClusterRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the create exadb vm cluster method over gRPC.

        Creates a new Exadb (Exascale) VM Cluster resource.

        Returns:
            Callable[[~.CreateExadbVmClusterRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_exadb_vm_cluster" not in self._stubs:
            self._stubs["create_exadb_vm_cluster"] = self._logged_channel.unary_unary(
                "/google.cloud.oracledatabase.v1.OracleDatabase/CreateExadbVmCluster",
                request_serializer=oracledatabase.CreateExadbVmClusterRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_exadb_vm_cluster"]

    @property
    def delete_exadb_vm_cluster(
        self,
    ) -> Callable[
        [oracledatabase.DeleteExadbVmClusterRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the delete exadb vm cluster method over gRPC.

        Deletes a single Exadb (Exascale) VM Cluster.

        Returns:
            Callable[[~.DeleteExadbVmClusterRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_exadb_vm_cluster" not in self._stubs:
            self._stubs["delete_exadb_vm_cluster"] = self._logged_channel.unary_unary(
                "/google.cloud.oracledatabase.v1.OracleDatabase/DeleteExadbVmCluster",
                request_serializer=oracledatabase.DeleteExadbVmClusterRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_exadb_vm_cluster"]

    @property
    def update_exadb_vm_cluster(
        self,
    ) -> Callable[
        [oracledatabase.UpdateExadbVmClusterRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the update exadb vm cluster method over gRPC.

        Updates a single Exadb (Exascale) VM Cluster. To add
        virtual machines to existing exadb vm cluster, only pass
        the node count.

        Returns:
            Callable[[~.UpdateExadbVmClusterRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_exadb_vm_cluster" not in self._stubs:
            self._stubs["update_exadb_vm_cluster"] = self._logged_channel.unary_unary(
                "/google.cloud.oracledatabase.v1.OracleDatabase/UpdateExadbVmCluster",
                request_serializer=oracledatabase.UpdateExadbVmClusterRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_exadb_vm_cluster"]

    @property
    def remove_virtual_machine_exadb_vm_cluster(
        self,
    ) -> Callable[
        [oracledatabase.RemoveVirtualMachineExadbVmClusterRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the remove virtual machine exadb
        vm cluster method over gRPC.

        Removes virtual machines from an existing exadb vm
        cluster.

        Returns:
            Callable[[~.RemoveVirtualMachineExadbVmClusterRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "remove_virtual_machine_exadb_vm_cluster" not in self._stubs:
            self._stubs["remove_virtual_machine_exadb_vm_cluster"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.oracledatabase.v1.OracleDatabase/RemoveVirtualMachineExadbVmCluster",
                    request_serializer=oracledatabase.RemoveVirtualMachineExadbVmClusterRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["remove_virtual_machine_exadb_vm_cluster"]

    @property
    def list_exascale_db_storage_vaults(
        self,
    ) -> Callable[
        [exascale_db_storage_vault.ListExascaleDbStorageVaultsRequest],
        exascale_db_storage_vault.ListExascaleDbStorageVaultsResponse,
    ]:
        r"""Return a callable for the list exascale db storage
        vaults method over gRPC.

        Lists all the ExascaleDB Storage Vaults for the given
        project and location.

        Returns:
            Callable[[~.ListExascaleDbStorageVaultsRequest],
                    ~.ListExascaleDbStorageVaultsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_exascale_db_storage_vaults" not in self._stubs:
            self._stubs["list_exascale_db_storage_vaults"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.oracledatabase.v1.OracleDatabase/ListExascaleDbStorageVaults",
                    request_serializer=exascale_db_storage_vault.ListExascaleDbStorageVaultsRequest.serialize,
                    response_deserializer=exascale_db_storage_vault.ListExascaleDbStorageVaultsResponse.deserialize,
                )
            )
        return self._stubs["list_exascale_db_storage_vaults"]

    @property
    def get_exascale_db_storage_vault(
        self,
    ) -> Callable[
        [exascale_db_storage_vault.GetExascaleDbStorageVaultRequest],
        exascale_db_storage_vault.ExascaleDbStorageVault,
    ]:
        r"""Return a callable for the get exascale db storage vault method over gRPC.

        Gets details of a single ExascaleDB Storage Vault.

        Returns:
            Callable[[~.GetExascaleDbStorageVaultRequest],
                    ~.ExascaleDbStorageVault]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_exascale_db_storage_vault" not in self._stubs:
            self._stubs["get_exascale_db_storage_vault"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.oracledatabase.v1.OracleDatabase/GetExascaleDbStorageVault",
                    request_serializer=exascale_db_storage_vault.GetExascaleDbStorageVaultRequest.serialize,
                    response_deserializer=exascale_db_storage_vault.ExascaleDbStorageVault.deserialize,
                )
            )
        return self._stubs["get_exascale_db_storage_vault"]

    @property
    def create_exascale_db_storage_vault(
        self,
    ) -> Callable[
        [gco_exascale_db_storage_vault.CreateExascaleDbStorageVaultRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the create exascale db storage
        vault method over gRPC.

        Creates a new ExascaleDB Storage Vault resource.

        Returns:
            Callable[[~.CreateExascaleDbStorageVaultRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_exascale_db_storage_vault" not in self._stubs:
            self._stubs["create_exascale_db_storage_vault"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.oracledatabase.v1.OracleDatabase/CreateExascaleDbStorageVault",
                    request_serializer=gco_exascale_db_storage_vault.CreateExascaleDbStorageVaultRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["create_exascale_db_storage_vault"]

    @property
    def delete_exascale_db_storage_vault(
        self,
    ) -> Callable[
        [exascale_db_storage_vault.DeleteExascaleDbStorageVaultRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the delete exascale db storage
        vault method over gRPC.

        Deletes a single ExascaleDB Storage Vault.

        Returns:
            Callable[[~.DeleteExascaleDbStorageVaultRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_exascale_db_storage_vault" not in self._stubs:
            self._stubs["delete_exascale_db_storage_vault"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.oracledatabase.v1.OracleDatabase/DeleteExascaleDbStorageVault",
                    request_serializer=exascale_db_storage_vault.DeleteExascaleDbStorageVaultRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["delete_exascale_db_storage_vault"]

    @property
    def list_db_system_initial_storage_sizes(
        self,
    ) -> Callable[
        [db_system_initial_storage_size.ListDbSystemInitialStorageSizesRequest],
        db_system_initial_storage_size.ListDbSystemInitialStorageSizesResponse,
    ]:
        r"""Return a callable for the list db system initial storage
        sizes method over gRPC.

        Lists all the DbSystemInitialStorageSizes for the
        given project and location.

        Returns:
            Callable[[~.ListDbSystemInitialStorageSizesRequest],
                    ~.ListDbSystemInitialStorageSizesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_db_system_initial_storage_sizes" not in self._stubs:
            self._stubs["list_db_system_initial_storage_sizes"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.oracledatabase.v1.OracleDatabase/ListDbSystemInitialStorageSizes",
                    request_serializer=db_system_initial_storage_size.ListDbSystemInitialStorageSizesRequest.serialize,
                    response_deserializer=db_system_initial_storage_size.ListDbSystemInitialStorageSizesResponse.deserialize,
                )
            )
        return self._stubs["list_db_system_initial_storage_sizes"]

    @property
    def list_databases(
        self,
    ) -> Callable[[database.ListDatabasesRequest], database.ListDatabasesResponse]:
        r"""Return a callable for the list databases method over gRPC.

        Lists all the Databases for the given project,
        location and DbSystem.

        Returns:
            Callable[[~.ListDatabasesRequest],
                    ~.ListDatabasesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_databases" not in self._stubs:
            self._stubs["list_databases"] = self._logged_channel.unary_unary(
                "/google.cloud.oracledatabase.v1.OracleDatabase/ListDatabases",
                request_serializer=database.ListDatabasesRequest.serialize,
                response_deserializer=database.ListDatabasesResponse.deserialize,
            )
        return self._stubs["list_databases"]

    @property
    def get_database(
        self,
    ) -> Callable[[database.GetDatabaseRequest], database.Database]:
        r"""Return a callable for the get database method over gRPC.

        Gets details of a single Database.

        Returns:
            Callable[[~.GetDatabaseRequest],
                    ~.Database]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_database" not in self._stubs:
            self._stubs["get_database"] = self._logged_channel.unary_unary(
                "/google.cloud.oracledatabase.v1.OracleDatabase/GetDatabase",
                request_serializer=database.GetDatabaseRequest.serialize,
                response_deserializer=database.Database.deserialize,
            )
        return self._stubs["get_database"]

    @property
    def list_pluggable_databases(
        self,
    ) -> Callable[
        [pluggable_database.ListPluggableDatabasesRequest],
        pluggable_database.ListPluggableDatabasesResponse,
    ]:
        r"""Return a callable for the list pluggable databases method over gRPC.

        Lists all the PluggableDatabases for the given
        project, location and Container Database.

        Returns:
            Callable[[~.ListPluggableDatabasesRequest],
                    ~.ListPluggableDatabasesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_pluggable_databases" not in self._stubs:
            self._stubs["list_pluggable_databases"] = self._logged_channel.unary_unary(
                "/google.cloud.oracledatabase.v1.OracleDatabase/ListPluggableDatabases",
                request_serializer=pluggable_database.ListPluggableDatabasesRequest.serialize,
                response_deserializer=pluggable_database.ListPluggableDatabasesResponse.deserialize,
            )
        return self._stubs["list_pluggable_databases"]

    @property
    def get_pluggable_database(
        self,
    ) -> Callable[
        [pluggable_database.GetPluggableDatabaseRequest],
        pluggable_database.PluggableDatabase,
    ]:
        r"""Return a callable for the get pluggable database method over gRPC.

        Gets details of a single PluggableDatabase.

        Returns:
            Callable[[~.GetPluggableDatabaseRequest],
                    ~.PluggableDatabase]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_pluggable_database" not in self._stubs:
            self._stubs["get_pluggable_database"] = self._logged_channel.unary_unary(
                "/google.cloud.oracledatabase.v1.OracleDatabase/GetPluggableDatabase",
                request_serializer=pluggable_database.GetPluggableDatabaseRequest.serialize,
                response_deserializer=pluggable_database.PluggableDatabase.deserialize,
            )
        return self._stubs["get_pluggable_database"]

    @property
    def list_db_systems(
        self,
    ) -> Callable[[db_system.ListDbSystemsRequest], db_system.ListDbSystemsResponse]:
        r"""Return a callable for the list db systems method over gRPC.

        Lists all the DbSystems for the given project and
        location.

        Returns:
            Callable[[~.ListDbSystemsRequest],
                    ~.ListDbSystemsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_db_systems" not in self._stubs:
            self._stubs["list_db_systems"] = self._logged_channel.unary_unary(
                "/google.cloud.oracledatabase.v1.OracleDatabase/ListDbSystems",
                request_serializer=db_system.ListDbSystemsRequest.serialize,
                response_deserializer=db_system.ListDbSystemsResponse.deserialize,
            )
        return self._stubs["list_db_systems"]

    @property
    def get_db_system(
        self,
    ) -> Callable[[db_system.GetDbSystemRequest], db_system.DbSystem]:
        r"""Return a callable for the get db system method over gRPC.

        Gets details of a single DbSystem.

        Returns:
            Callable[[~.GetDbSystemRequest],
                    ~.DbSystem]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_db_system" not in self._stubs:
            self._stubs["get_db_system"] = self._logged_channel.unary_unary(
                "/google.cloud.oracledatabase.v1.OracleDatabase/GetDbSystem",
                request_serializer=db_system.GetDbSystemRequest.serialize,
                response_deserializer=db_system.DbSystem.deserialize,
            )
        return self._stubs["get_db_system"]

    @property
    def create_db_system(
        self,
    ) -> Callable[[gco_db_system.CreateDbSystemRequest], operations_pb2.Operation]:
        r"""Return a callable for the create db system method over gRPC.

        Creates a new DbSystem in a given project and
        location.

        Returns:
            Callable[[~.CreateDbSystemRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_db_system" not in self._stubs:
            self._stubs["create_db_system"] = self._logged_channel.unary_unary(
                "/google.cloud.oracledatabase.v1.OracleDatabase/CreateDbSystem",
                request_serializer=gco_db_system.CreateDbSystemRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_db_system"]

    @property
    def delete_db_system(
        self,
    ) -> Callable[[db_system.DeleteDbSystemRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete db system method over gRPC.

        Deletes a single DbSystem.

        Returns:
            Callable[[~.DeleteDbSystemRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_db_system" not in self._stubs:
            self._stubs["delete_db_system"] = self._logged_channel.unary_unary(
                "/google.cloud.oracledatabase.v1.OracleDatabase/DeleteDbSystem",
                request_serializer=db_system.DeleteDbSystemRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_db_system"]

    @property
    def list_goldengate_deployments(
        self,
    ) -> Callable[
        [goldengate_deployment.ListGoldengateDeploymentsRequest],
        goldengate_deployment.ListGoldengateDeploymentsResponse,
    ]:
        r"""Return a callable for the list goldengate deployments method over gRPC.

        Lists all the GoldengateDeployments for the given
        project and location.

        Returns:
            Callable[[~.ListGoldengateDeploymentsRequest],
                    ~.ListGoldengateDeploymentsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_goldengate_deployments" not in self._stubs:
            self._stubs["list_goldengate_deployments"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.oracledatabase.v1.OracleDatabase/ListGoldengateDeployments",
                    request_serializer=goldengate_deployment.ListGoldengateDeploymentsRequest.serialize,
                    response_deserializer=goldengate_deployment.ListGoldengateDeploymentsResponse.deserialize,
                )
            )
        return self._stubs["list_goldengate_deployments"]

    @property
    def get_goldengate_deployment(
        self,
    ) -> Callable[
        [goldengate_deployment.GetGoldengateDeploymentRequest],
        goldengate_deployment.GoldengateDeployment,
    ]:
        r"""Return a callable for the get goldengate deployment method over gRPC.

        Gets details of a single GoldengateDeployment.

        Returns:
            Callable[[~.GetGoldengateDeploymentRequest],
                    ~.GoldengateDeployment]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_goldengate_deployment" not in self._stubs:
            self._stubs["get_goldengate_deployment"] = self._logged_channel.unary_unary(
                "/google.cloud.oracledatabase.v1.OracleDatabase/GetGoldengateDeployment",
                request_serializer=goldengate_deployment.GetGoldengateDeploymentRequest.serialize,
                response_deserializer=goldengate_deployment.GoldengateDeployment.deserialize,
            )
        return self._stubs["get_goldengate_deployment"]

    @property
    def create_goldengate_deployment(
        self,
    ) -> Callable[
        [gco_goldengate_deployment.CreateGoldengateDeploymentRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the create goldengate deployment method over gRPC.

        Creates a new GoldengateDeployment in a given project
        and location.

        Returns:
            Callable[[~.CreateGoldengateDeploymentRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_goldengate_deployment" not in self._stubs:
            self._stubs["create_goldengate_deployment"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.oracledatabase.v1.OracleDatabase/CreateGoldengateDeployment",
                    request_serializer=gco_goldengate_deployment.CreateGoldengateDeploymentRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["create_goldengate_deployment"]

    @property
    def delete_goldengate_deployment(
        self,
    ) -> Callable[
        [goldengate_deployment.DeleteGoldengateDeploymentRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the delete goldengate deployment method over gRPC.

        Deletes a single GoldengateDeployment.

        Returns:
            Callable[[~.DeleteGoldengateDeploymentRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_goldengate_deployment" not in self._stubs:
            self._stubs["delete_goldengate_deployment"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.oracledatabase.v1.OracleDatabase/DeleteGoldengateDeployment",
                    request_serializer=goldengate_deployment.DeleteGoldengateDeploymentRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["delete_goldengate_deployment"]

    @property
    def stop_goldengate_deployment(
        self,
    ) -> Callable[
        [goldengate_deployment.StopGoldengateDeploymentRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the stop goldengate deployment method over gRPC.

        Stops a single GoldengateDeployment.

        Returns:
            Callable[[~.StopGoldengateDeploymentRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "stop_goldengate_deployment" not in self._stubs:
            self._stubs["stop_goldengate_deployment"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.oracledatabase.v1.OracleDatabase/StopGoldengateDeployment",
                    request_serializer=goldengate_deployment.StopGoldengateDeploymentRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["stop_goldengate_deployment"]

    @property
    def start_goldengate_deployment(
        self,
    ) -> Callable[
        [goldengate_deployment.StartGoldengateDeploymentRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the start goldengate deployment method over gRPC.

        Starts a single GoldengateDeployment.

        Returns:
            Callable[[~.StartGoldengateDeploymentRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "start_goldengate_deployment" not in self._stubs:
            self._stubs["start_goldengate_deployment"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.oracledatabase.v1.OracleDatabase/StartGoldengateDeployment",
                    request_serializer=goldengate_deployment.StartGoldengateDeploymentRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["start_goldengate_deployment"]

    @property
    def list_goldengate_connections(
        self,
    ) -> Callable[
        [goldengate_connection.ListGoldengateConnectionsRequest],
        goldengate_connection.ListGoldengateConnectionsResponse,
    ]:
        r"""Return a callable for the list goldengate connections method over gRPC.

        Lists all the GoldengateConnections for the given
        project and location.

        Returns:
            Callable[[~.ListGoldengateConnectionsRequest],
                    ~.ListGoldengateConnectionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_goldengate_connections" not in self._stubs:
            self._stubs["list_goldengate_connections"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.oracledatabase.v1.OracleDatabase/ListGoldengateConnections",
                    request_serializer=goldengate_connection.ListGoldengateConnectionsRequest.serialize,
                    response_deserializer=goldengate_connection.ListGoldengateConnectionsResponse.deserialize,
                )
            )
        return self._stubs["list_goldengate_connections"]

    @property
    def get_goldengate_connection(
        self,
    ) -> Callable[
        [goldengate_connection.GetGoldengateConnectionRequest],
        goldengate_connection.GoldengateConnection,
    ]:
        r"""Return a callable for the get goldengate connection method over gRPC.

        Gets details of a single GoldengateConnection.

        Returns:
            Callable[[~.GetGoldengateConnectionRequest],
                    ~.GoldengateConnection]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_goldengate_connection" not in self._stubs:
            self._stubs["get_goldengate_connection"] = self._logged_channel.unary_unary(
                "/google.cloud.oracledatabase.v1.OracleDatabase/GetGoldengateConnection",
                request_serializer=goldengate_connection.GetGoldengateConnectionRequest.serialize,
                response_deserializer=goldengate_connection.GoldengateConnection.deserialize,
            )
        return self._stubs["get_goldengate_connection"]

    @property
    def create_goldengate_connection(
        self,
    ) -> Callable[
        [gco_goldengate_connection.CreateGoldengateConnectionRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the create goldengate connection method over gRPC.

        Creates a new GoldengateConnection in a given project
        and location.

        Returns:
            Callable[[~.CreateGoldengateConnectionRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_goldengate_connection" not in self._stubs:
            self._stubs["create_goldengate_connection"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.oracledatabase.v1.OracleDatabase/CreateGoldengateConnection",
                    request_serializer=gco_goldengate_connection.CreateGoldengateConnectionRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["create_goldengate_connection"]

    @property
    def delete_goldengate_connection(
        self,
    ) -> Callable[
        [goldengate_connection.DeleteGoldengateConnectionRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the delete goldengate connection method over gRPC.

        Deletes a single GoldengateConnection.

        Returns:
            Callable[[~.DeleteGoldengateConnectionRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_goldengate_connection" not in self._stubs:
            self._stubs["delete_goldengate_connection"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.oracledatabase.v1.OracleDatabase/DeleteGoldengateConnection",
                    request_serializer=goldengate_connection.DeleteGoldengateConnectionRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["delete_goldengate_connection"]

    @property
    def list_goldengate_deployment_versions(
        self,
    ) -> Callable[
        [goldengate_deployment_version.ListGoldengateDeploymentVersionsRequest],
        goldengate_deployment_version.ListGoldengateDeploymentVersionsResponse,
    ]:
        r"""Return a callable for the list goldengate deployment
        versions method over gRPC.

        Lists GoldengateDeploymentVersions in a given project
        and location.

        Returns:
            Callable[[~.ListGoldengateDeploymentVersionsRequest],
                    ~.ListGoldengateDeploymentVersionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_goldengate_deployment_versions" not in self._stubs:
            self._stubs["list_goldengate_deployment_versions"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.oracledatabase.v1.OracleDatabase/ListGoldengateDeploymentVersions",
                    request_serializer=goldengate_deployment_version.ListGoldengateDeploymentVersionsRequest.serialize,
                    response_deserializer=goldengate_deployment_version.ListGoldengateDeploymentVersionsResponse.deserialize,
                )
            )
        return self._stubs["list_goldengate_deployment_versions"]

    @property
    def list_goldengate_deployment_types(
        self,
    ) -> Callable[
        [goldengate_deployment_type.ListGoldengateDeploymentTypesRequest],
        goldengate_deployment_type.ListGoldengateDeploymentTypesResponse,
    ]:
        r"""Return a callable for the list goldengate deployment
        types method over gRPC.

        Lists GoldenGateDeploymentTypes in a given project
        and location.

        Returns:
            Callable[[~.ListGoldengateDeploymentTypesRequest],
                    ~.ListGoldengateDeploymentTypesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_goldengate_deployment_types" not in self._stubs:
            self._stubs["list_goldengate_deployment_types"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.oracledatabase.v1.OracleDatabase/ListGoldengateDeploymentTypes",
                    request_serializer=goldengate_deployment_type.ListGoldengateDeploymentTypesRequest.serialize,
                    response_deserializer=goldengate_deployment_type.ListGoldengateDeploymentTypesResponse.deserialize,
                )
            )
        return self._stubs["list_goldengate_deployment_types"]

    @property
    def list_goldengate_deployment_environments(
        self,
    ) -> Callable[
        [goldengate_deployment_environment.ListGoldengateDeploymentEnvironmentsRequest],
        goldengate_deployment_environment.ListGoldengateDeploymentEnvironmentsResponse,
    ]:
        r"""Return a callable for the list goldengate deployment
        environments method over gRPC.

        Lists GoldengateDeploymentEnvironments in a given
        project and location.

        Returns:
            Callable[[~.ListGoldengateDeploymentEnvironmentsRequest],
                    ~.ListGoldengateDeploymentEnvironmentsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_goldengate_deployment_environments" not in self._stubs:
            self._stubs["list_goldengate_deployment_environments"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.oracledatabase.v1.OracleDatabase/ListGoldengateDeploymentEnvironments",
                    request_serializer=goldengate_deployment_environment.ListGoldengateDeploymentEnvironmentsRequest.serialize,
                    response_deserializer=goldengate_deployment_environment.ListGoldengateDeploymentEnvironmentsResponse.deserialize,
                )
            )
        return self._stubs["list_goldengate_deployment_environments"]

    @property
    def list_goldengate_connection_types(
        self,
    ) -> Callable[
        [goldengate_connection_type.ListGoldengateConnectionTypesRequest],
        goldengate_connection_type.ListGoldengateConnectionTypesResponse,
    ]:
        r"""Return a callable for the list goldengate connection
        types method over gRPC.

        Lists GoldengateConnectionTypes in a given project
        and location.

        Returns:
            Callable[[~.ListGoldengateConnectionTypesRequest],
                    ~.ListGoldengateConnectionTypesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_goldengate_connection_types" not in self._stubs:
            self._stubs["list_goldengate_connection_types"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.oracledatabase.v1.OracleDatabase/ListGoldengateConnectionTypes",
                    request_serializer=goldengate_connection_type.ListGoldengateConnectionTypesRequest.serialize,
                    response_deserializer=goldengate_connection_type.ListGoldengateConnectionTypesResponse.deserialize,
                )
            )
        return self._stubs["list_goldengate_connection_types"]

    @property
    def list_db_versions(
        self,
    ) -> Callable[
        [db_version.ListDbVersionsRequest], db_version.ListDbVersionsResponse
    ]:
        r"""Return a callable for the list db versions method over gRPC.

        List DbVersions for the given project and location.

        Returns:
            Callable[[~.ListDbVersionsRequest],
                    ~.ListDbVersionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_db_versions" not in self._stubs:
            self._stubs["list_db_versions"] = self._logged_channel.unary_unary(
                "/google.cloud.oracledatabase.v1.OracleDatabase/ListDbVersions",
                request_serializer=db_version.ListDbVersionsRequest.serialize,
                response_deserializer=db_version.ListDbVersionsResponse.deserialize,
            )
        return self._stubs["list_db_versions"]

    @property
    def list_database_character_sets(
        self,
    ) -> Callable[
        [database_character_set.ListDatabaseCharacterSetsRequest],
        database_character_set.ListDatabaseCharacterSetsResponse,
    ]:
        r"""Return a callable for the list database character sets method over gRPC.

        List DatabaseCharacterSets for the given project and
        location.

        Returns:
            Callable[[~.ListDatabaseCharacterSetsRequest],
                    ~.ListDatabaseCharacterSetsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_database_character_sets" not in self._stubs:
            self._stubs["list_database_character_sets"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.oracledatabase.v1.OracleDatabase/ListDatabaseCharacterSets",
                    request_serializer=database_character_set.ListDatabaseCharacterSetsRequest.serialize,
                    response_deserializer=database_character_set.ListDatabaseCharacterSetsResponse.deserialize,
                )
            )
        return self._stubs["list_database_character_sets"]

    @property
    def list_goldengate_connection_assignments(
        self,
    ) -> Callable[
        [goldengate_connection_assignment.ListGoldengateConnectionAssignmentsRequest],
        goldengate_connection_assignment.ListGoldengateConnectionAssignmentsResponse,
    ]:
        r"""Return a callable for the list goldengate connection
        assignments method over gRPC.

        Lists GoldengateConnectionAssignments in a given
        project and location.

        Returns:
            Callable[[~.ListGoldengateConnectionAssignmentsRequest],
                    ~.ListGoldengateConnectionAssignmentsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_goldengate_connection_assignments" not in self._stubs:
            self._stubs["list_goldengate_connection_assignments"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.oracledatabase.v1.OracleDatabase/ListGoldengateConnectionAssignments",
                    request_serializer=goldengate_connection_assignment.ListGoldengateConnectionAssignmentsRequest.serialize,
                    response_deserializer=goldengate_connection_assignment.ListGoldengateConnectionAssignmentsResponse.deserialize,
                )
            )
        return self._stubs["list_goldengate_connection_assignments"]

    @property
    def get_goldengate_connection_assignment(
        self,
    ) -> Callable[
        [goldengate_connection_assignment.GetGoldengateConnectionAssignmentRequest],
        goldengate_connection_assignment.GoldengateConnectionAssignment,
    ]:
        r"""Return a callable for the get goldengate connection
        assignment method over gRPC.

        Gets details of a single
        GoldengateConnectionAssignment.

        Returns:
            Callable[[~.GetGoldengateConnectionAssignmentRequest],
                    ~.GoldengateConnectionAssignment]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_goldengate_connection_assignment" not in self._stubs:
            self._stubs["get_goldengate_connection_assignment"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.oracledatabase.v1.OracleDatabase/GetGoldengateConnectionAssignment",
                    request_serializer=goldengate_connection_assignment.GetGoldengateConnectionAssignmentRequest.serialize,
                    response_deserializer=goldengate_connection_assignment.GoldengateConnectionAssignment.deserialize,
                )
            )
        return self._stubs["get_goldengate_connection_assignment"]

    @property
    def create_goldengate_connection_assignment(
        self,
    ) -> Callable[
        [
            gco_goldengate_connection_assignment.CreateGoldengateConnectionAssignmentRequest
        ],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the create goldengate connection
        assignment method over gRPC.

        Creates a new GoldengateConnectionAssignment in a
        given project and location.

        Returns:
            Callable[[~.CreateGoldengateConnectionAssignmentRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_goldengate_connection_assignment" not in self._stubs:
            self._stubs["create_goldengate_connection_assignment"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.oracledatabase.v1.OracleDatabase/CreateGoldengateConnectionAssignment",
                    request_serializer=gco_goldengate_connection_assignment.CreateGoldengateConnectionAssignmentRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["create_goldengate_connection_assignment"]

    @property
    def delete_goldengate_connection_assignment(
        self,
    ) -> Callable[
        [goldengate_connection_assignment.DeleteGoldengateConnectionAssignmentRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the delete goldengate connection
        assignment method over gRPC.

        Deletes a single GoldengateConnectionAssignment.

        Returns:
            Callable[[~.DeleteGoldengateConnectionAssignmentRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_goldengate_connection_assignment" not in self._stubs:
            self._stubs["delete_goldengate_connection_assignment"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.oracledatabase.v1.OracleDatabase/DeleteGoldengateConnectionAssignment",
                    request_serializer=goldengate_connection_assignment.DeleteGoldengateConnectionAssignmentRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["delete_goldengate_connection_assignment"]

    @property
    def test_goldengate_connection_assignment(
        self,
    ) -> Callable[
        [goldengate_connection_assignment.TestGoldengateConnectionAssignmentRequest],
        goldengate_connection_assignment.TestGoldengateConnectionAssignmentResponse,
    ]:
        r"""Return a callable for the test goldengate connection
        assignment method over gRPC.

        Tests a single GoldengateConnectionAssignment.

        Returns:
            Callable[[~.TestGoldengateConnectionAssignmentRequest],
                    ~.TestGoldengateConnectionAssignmentResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "test_goldengate_connection_assignment" not in self._stubs:
            self._stubs["test_goldengate_connection_assignment"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.oracledatabase.v1.OracleDatabase/TestGoldengateConnectionAssignment",
                    request_serializer=goldengate_connection_assignment.TestGoldengateConnectionAssignmentRequest.serialize,
                    response_deserializer=goldengate_connection_assignment.TestGoldengateConnectionAssignmentResponse.deserialize,
                )
            )
        return self._stubs["test_goldengate_connection_assignment"]

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


__all__ = ("OracleDatabaseGrpcTransport",)
