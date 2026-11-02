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

from google.cloud.vmmigration_v1.types import vmmigration

from .base import DEFAULT_CLIENT_INFO, VmMigrationTransport

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
                    "serviceName": "google.cloud.vmmigration.v1.VmMigration",
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
                    "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                    "rpcName": client_call_details.method,
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class VmMigrationGrpcTransport(VmMigrationTransport):
    """gRPC backend transport for VmMigration.

    VM Migration Service

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
        host: str = "vmmigration.googleapis.com",
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
                 The hostname to connect to (default: 'vmmigration.googleapis.com').
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
        host: str = "vmmigration.googleapis.com",
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
    def list_sources(
        self,
    ) -> Callable[[vmmigration.ListSourcesRequest], vmmigration.ListSourcesResponse]:
        r"""Return a callable for the list sources method over gRPC.

        Lists Sources in a given project and location.

        Returns:
            Callable[[~.ListSourcesRequest],
                    ~.ListSourcesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_sources" not in self._stubs:
            self._stubs["list_sources"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/ListSources",
                request_serializer=vmmigration.ListSourcesRequest.serialize,
                response_deserializer=vmmigration.ListSourcesResponse.deserialize,
            )
        return self._stubs["list_sources"]

    @property
    def get_source(
        self,
    ) -> Callable[[vmmigration.GetSourceRequest], vmmigration.Source]:
        r"""Return a callable for the get source method over gRPC.

        Gets details of a single Source.

        Returns:
            Callable[[~.GetSourceRequest],
                    ~.Source]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_source" not in self._stubs:
            self._stubs["get_source"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/GetSource",
                request_serializer=vmmigration.GetSourceRequest.serialize,
                response_deserializer=vmmigration.Source.deserialize,
            )
        return self._stubs["get_source"]

    @property
    def create_source(
        self,
    ) -> Callable[[vmmigration.CreateSourceRequest], operations_pb2.Operation]:
        r"""Return a callable for the create source method over gRPC.

        Creates a new Source in a given project and location.

        Returns:
            Callable[[~.CreateSourceRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_source" not in self._stubs:
            self._stubs["create_source"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/CreateSource",
                request_serializer=vmmigration.CreateSourceRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_source"]

    @property
    def update_source(
        self,
    ) -> Callable[[vmmigration.UpdateSourceRequest], operations_pb2.Operation]:
        r"""Return a callable for the update source method over gRPC.

        Updates the parameters of a single Source.

        Returns:
            Callable[[~.UpdateSourceRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_source" not in self._stubs:
            self._stubs["update_source"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/UpdateSource",
                request_serializer=vmmigration.UpdateSourceRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_source"]

    @property
    def delete_source(
        self,
    ) -> Callable[[vmmigration.DeleteSourceRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete source method over gRPC.

        Deletes a single Source.

        Returns:
            Callable[[~.DeleteSourceRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_source" not in self._stubs:
            self._stubs["delete_source"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/DeleteSource",
                request_serializer=vmmigration.DeleteSourceRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_source"]

    @property
    def fetch_inventory(
        self,
    ) -> Callable[
        [vmmigration.FetchInventoryRequest], vmmigration.FetchInventoryResponse
    ]:
        r"""Return a callable for the fetch inventory method over gRPC.

        List remote source's inventory of VMs.
        The remote source is the onprem vCenter (remote in the
        sense it's not in Compute Engine). The inventory
        describes the list of existing VMs in that source. Note
        that this operation lists the VMs on the remote source,
        as opposed to listing the MigratingVms resources in the
        vmmigration service.

        Returns:
            Callable[[~.FetchInventoryRequest],
                    ~.FetchInventoryResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "fetch_inventory" not in self._stubs:
            self._stubs["fetch_inventory"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/FetchInventory",
                request_serializer=vmmigration.FetchInventoryRequest.serialize,
                response_deserializer=vmmigration.FetchInventoryResponse.deserialize,
            )
        return self._stubs["fetch_inventory"]

    @property
    def fetch_storage_inventory(
        self,
    ) -> Callable[
        [vmmigration.FetchStorageInventoryRequest],
        vmmigration.FetchStorageInventoryResponse,
    ]:
        r"""Return a callable for the fetch storage inventory method over gRPC.

        List remote source's inventory of storage resources.
        The remote source is another cloud vendor (e.g. AWS,
        Azure). The inventory describes the list of existing
        storage resources in that source. Note that this
        operation lists the resources on the remote source, as
        opposed to listing the MigratingVms resources in the
        vmmigration service.

        Returns:
            Callable[[~.FetchStorageInventoryRequest],
                    ~.FetchStorageInventoryResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "fetch_storage_inventory" not in self._stubs:
            self._stubs["fetch_storage_inventory"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/FetchStorageInventory",
                request_serializer=vmmigration.FetchStorageInventoryRequest.serialize,
                response_deserializer=vmmigration.FetchStorageInventoryResponse.deserialize,
            )
        return self._stubs["fetch_storage_inventory"]

    @property
    def list_utilization_reports(
        self,
    ) -> Callable[
        [vmmigration.ListUtilizationReportsRequest],
        vmmigration.ListUtilizationReportsResponse,
    ]:
        r"""Return a callable for the list utilization reports method over gRPC.

        Lists Utilization Reports of the given Source.

        Returns:
            Callable[[~.ListUtilizationReportsRequest],
                    ~.ListUtilizationReportsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_utilization_reports" not in self._stubs:
            self._stubs["list_utilization_reports"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/ListUtilizationReports",
                request_serializer=vmmigration.ListUtilizationReportsRequest.serialize,
                response_deserializer=vmmigration.ListUtilizationReportsResponse.deserialize,
            )
        return self._stubs["list_utilization_reports"]

    @property
    def get_utilization_report(
        self,
    ) -> Callable[
        [vmmigration.GetUtilizationReportRequest], vmmigration.UtilizationReport
    ]:
        r"""Return a callable for the get utilization report method over gRPC.

        Gets a single Utilization Report.

        Returns:
            Callable[[~.GetUtilizationReportRequest],
                    ~.UtilizationReport]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_utilization_report" not in self._stubs:
            self._stubs["get_utilization_report"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/GetUtilizationReport",
                request_serializer=vmmigration.GetUtilizationReportRequest.serialize,
                response_deserializer=vmmigration.UtilizationReport.deserialize,
            )
        return self._stubs["get_utilization_report"]

    @property
    def create_utilization_report(
        self,
    ) -> Callable[
        [vmmigration.CreateUtilizationReportRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the create utilization report method over gRPC.

        Creates a new UtilizationReport.

        Returns:
            Callable[[~.CreateUtilizationReportRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_utilization_report" not in self._stubs:
            self._stubs["create_utilization_report"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/CreateUtilizationReport",
                request_serializer=vmmigration.CreateUtilizationReportRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_utilization_report"]

    @property
    def delete_utilization_report(
        self,
    ) -> Callable[
        [vmmigration.DeleteUtilizationReportRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the delete utilization report method over gRPC.

        Deletes a single Utilization Report.

        Returns:
            Callable[[~.DeleteUtilizationReportRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_utilization_report" not in self._stubs:
            self._stubs["delete_utilization_report"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/DeleteUtilizationReport",
                request_serializer=vmmigration.DeleteUtilizationReportRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_utilization_report"]

    @property
    def list_datacenter_connectors(
        self,
    ) -> Callable[
        [vmmigration.ListDatacenterConnectorsRequest],
        vmmigration.ListDatacenterConnectorsResponse,
    ]:
        r"""Return a callable for the list datacenter connectors method over gRPC.

        Lists DatacenterConnectors in a given Source.

        Returns:
            Callable[[~.ListDatacenterConnectorsRequest],
                    ~.ListDatacenterConnectorsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_datacenter_connectors" not in self._stubs:
            self._stubs["list_datacenter_connectors"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.vmmigration.v1.VmMigration/ListDatacenterConnectors",
                    request_serializer=vmmigration.ListDatacenterConnectorsRequest.serialize,
                    response_deserializer=vmmigration.ListDatacenterConnectorsResponse.deserialize,
                )
            )
        return self._stubs["list_datacenter_connectors"]

    @property
    def get_datacenter_connector(
        self,
    ) -> Callable[
        [vmmigration.GetDatacenterConnectorRequest], vmmigration.DatacenterConnector
    ]:
        r"""Return a callable for the get datacenter connector method over gRPC.

        Gets details of a single DatacenterConnector.

        Returns:
            Callable[[~.GetDatacenterConnectorRequest],
                    ~.DatacenterConnector]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_datacenter_connector" not in self._stubs:
            self._stubs["get_datacenter_connector"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/GetDatacenterConnector",
                request_serializer=vmmigration.GetDatacenterConnectorRequest.serialize,
                response_deserializer=vmmigration.DatacenterConnector.deserialize,
            )
        return self._stubs["get_datacenter_connector"]

    @property
    def create_datacenter_connector(
        self,
    ) -> Callable[
        [vmmigration.CreateDatacenterConnectorRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the create datacenter connector method over gRPC.

        Creates a new DatacenterConnector in a given Source.

        Returns:
            Callable[[~.CreateDatacenterConnectorRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_datacenter_connector" not in self._stubs:
            self._stubs["create_datacenter_connector"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.vmmigration.v1.VmMigration/CreateDatacenterConnector",
                    request_serializer=vmmigration.CreateDatacenterConnectorRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["create_datacenter_connector"]

    @property
    def delete_datacenter_connector(
        self,
    ) -> Callable[
        [vmmigration.DeleteDatacenterConnectorRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the delete datacenter connector method over gRPC.

        Deletes a single DatacenterConnector.

        Returns:
            Callable[[~.DeleteDatacenterConnectorRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_datacenter_connector" not in self._stubs:
            self._stubs["delete_datacenter_connector"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.vmmigration.v1.VmMigration/DeleteDatacenterConnector",
                    request_serializer=vmmigration.DeleteDatacenterConnectorRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["delete_datacenter_connector"]

    @property
    def upgrade_appliance(
        self,
    ) -> Callable[[vmmigration.UpgradeApplianceRequest], operations_pb2.Operation]:
        r"""Return a callable for the upgrade appliance method over gRPC.

        Upgrades the appliance relate to this
        DatacenterConnector to the in-place updateable version.

        Returns:
            Callable[[~.UpgradeApplianceRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "upgrade_appliance" not in self._stubs:
            self._stubs["upgrade_appliance"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/UpgradeAppliance",
                request_serializer=vmmigration.UpgradeApplianceRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["upgrade_appliance"]

    @property
    def create_migrating_vm(
        self,
    ) -> Callable[[vmmigration.CreateMigratingVmRequest], operations_pb2.Operation]:
        r"""Return a callable for the create migrating vm method over gRPC.

        Creates a new MigratingVm in a given Source.

        Returns:
            Callable[[~.CreateMigratingVmRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_migrating_vm" not in self._stubs:
            self._stubs["create_migrating_vm"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/CreateMigratingVm",
                request_serializer=vmmigration.CreateMigratingVmRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_migrating_vm"]

    @property
    def list_migrating_vms(
        self,
    ) -> Callable[
        [vmmigration.ListMigratingVmsRequest], vmmigration.ListMigratingVmsResponse
    ]:
        r"""Return a callable for the list migrating vms method over gRPC.

        Lists MigratingVms in a given Source.

        Returns:
            Callable[[~.ListMigratingVmsRequest],
                    ~.ListMigratingVmsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_migrating_vms" not in self._stubs:
            self._stubs["list_migrating_vms"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/ListMigratingVms",
                request_serializer=vmmigration.ListMigratingVmsRequest.serialize,
                response_deserializer=vmmigration.ListMigratingVmsResponse.deserialize,
            )
        return self._stubs["list_migrating_vms"]

    @property
    def get_migrating_vm(
        self,
    ) -> Callable[[vmmigration.GetMigratingVmRequest], vmmigration.MigratingVm]:
        r"""Return a callable for the get migrating vm method over gRPC.

        Gets details of a single MigratingVm.

        Returns:
            Callable[[~.GetMigratingVmRequest],
                    ~.MigratingVm]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_migrating_vm" not in self._stubs:
            self._stubs["get_migrating_vm"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/GetMigratingVm",
                request_serializer=vmmigration.GetMigratingVmRequest.serialize,
                response_deserializer=vmmigration.MigratingVm.deserialize,
            )
        return self._stubs["get_migrating_vm"]

    @property
    def update_migrating_vm(
        self,
    ) -> Callable[[vmmigration.UpdateMigratingVmRequest], operations_pb2.Operation]:
        r"""Return a callable for the update migrating vm method over gRPC.

        Updates the parameters of a single MigratingVm.

        Returns:
            Callable[[~.UpdateMigratingVmRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_migrating_vm" not in self._stubs:
            self._stubs["update_migrating_vm"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/UpdateMigratingVm",
                request_serializer=vmmigration.UpdateMigratingVmRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_migrating_vm"]

    @property
    def delete_migrating_vm(
        self,
    ) -> Callable[[vmmigration.DeleteMigratingVmRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete migrating vm method over gRPC.

        Deletes a single MigratingVm.

        Returns:
            Callable[[~.DeleteMigratingVmRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_migrating_vm" not in self._stubs:
            self._stubs["delete_migrating_vm"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/DeleteMigratingVm",
                request_serializer=vmmigration.DeleteMigratingVmRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_migrating_vm"]

    @property
    def start_migration(
        self,
    ) -> Callable[[vmmigration.StartMigrationRequest], operations_pb2.Operation]:
        r"""Return a callable for the start migration method over gRPC.

        Starts migration for a VM. Starts the process of
        uploading data and creating snapshots, in replication
        cycles scheduled by the policy.

        Returns:
            Callable[[~.StartMigrationRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "start_migration" not in self._stubs:
            self._stubs["start_migration"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/StartMigration",
                request_serializer=vmmigration.StartMigrationRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["start_migration"]

    @property
    def resume_migration(
        self,
    ) -> Callable[[vmmigration.ResumeMigrationRequest], operations_pb2.Operation]:
        r"""Return a callable for the resume migration method over gRPC.

        Resumes a migration for a VM. When called on a paused
        migration, will start the process of uploading data and
        creating snapshots; when called on a completed cut-over
        migration, will update the migration to active state and
        start the process of uploading data and creating
        snapshots.

        Returns:
            Callable[[~.ResumeMigrationRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "resume_migration" not in self._stubs:
            self._stubs["resume_migration"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/ResumeMigration",
                request_serializer=vmmigration.ResumeMigrationRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["resume_migration"]

    @property
    def pause_migration(
        self,
    ) -> Callable[[vmmigration.PauseMigrationRequest], operations_pb2.Operation]:
        r"""Return a callable for the pause migration method over gRPC.

        Pauses a migration for a VM. If cycle tasks are
        running they will be cancelled, preserving source task
        data. Further replication cycles will not be triggered
        while the VM is paused.

        Returns:
            Callable[[~.PauseMigrationRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "pause_migration" not in self._stubs:
            self._stubs["pause_migration"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/PauseMigration",
                request_serializer=vmmigration.PauseMigrationRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["pause_migration"]

    @property
    def finalize_migration(
        self,
    ) -> Callable[[vmmigration.FinalizeMigrationRequest], operations_pb2.Operation]:
        r"""Return a callable for the finalize migration method over gRPC.

        Marks a migration as completed, deleting migration
        resources that are no longer being used. Only applicable
        after cutover is done.

        Returns:
            Callable[[~.FinalizeMigrationRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "finalize_migration" not in self._stubs:
            self._stubs["finalize_migration"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/FinalizeMigration",
                request_serializer=vmmigration.FinalizeMigrationRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["finalize_migration"]

    @property
    def extend_migration(
        self,
    ) -> Callable[[vmmigration.ExtendMigrationRequest], operations_pb2.Operation]:
        r"""Return a callable for the extend migration method over gRPC.

        Extend the migrating VM time to live.

        Returns:
            Callable[[~.ExtendMigrationRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "extend_migration" not in self._stubs:
            self._stubs["extend_migration"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/ExtendMigration",
                request_serializer=vmmigration.ExtendMigrationRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["extend_migration"]

    @property
    def create_clone_job(
        self,
    ) -> Callable[[vmmigration.CreateCloneJobRequest], operations_pb2.Operation]:
        r"""Return a callable for the create clone job method over gRPC.

        Initiates a Clone of a specific migrating VM.

        Returns:
            Callable[[~.CreateCloneJobRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_clone_job" not in self._stubs:
            self._stubs["create_clone_job"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/CreateCloneJob",
                request_serializer=vmmigration.CreateCloneJobRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_clone_job"]

    @property
    def cancel_clone_job(
        self,
    ) -> Callable[[vmmigration.CancelCloneJobRequest], operations_pb2.Operation]:
        r"""Return a callable for the cancel clone job method over gRPC.

        Initiates the cancellation of a running clone job.

        Returns:
            Callable[[~.CancelCloneJobRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "cancel_clone_job" not in self._stubs:
            self._stubs["cancel_clone_job"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/CancelCloneJob",
                request_serializer=vmmigration.CancelCloneJobRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["cancel_clone_job"]

    @property
    def list_clone_jobs(
        self,
    ) -> Callable[
        [vmmigration.ListCloneJobsRequest], vmmigration.ListCloneJobsResponse
    ]:
        r"""Return a callable for the list clone jobs method over gRPC.

        Lists the CloneJobs of a migrating VM. Only 25 most
        recent CloneJobs are listed.

        Returns:
            Callable[[~.ListCloneJobsRequest],
                    ~.ListCloneJobsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_clone_jobs" not in self._stubs:
            self._stubs["list_clone_jobs"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/ListCloneJobs",
                request_serializer=vmmigration.ListCloneJobsRequest.serialize,
                response_deserializer=vmmigration.ListCloneJobsResponse.deserialize,
            )
        return self._stubs["list_clone_jobs"]

    @property
    def get_clone_job(
        self,
    ) -> Callable[[vmmigration.GetCloneJobRequest], vmmigration.CloneJob]:
        r"""Return a callable for the get clone job method over gRPC.

        Gets details of a single CloneJob.

        Returns:
            Callable[[~.GetCloneJobRequest],
                    ~.CloneJob]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_clone_job" not in self._stubs:
            self._stubs["get_clone_job"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/GetCloneJob",
                request_serializer=vmmigration.GetCloneJobRequest.serialize,
                response_deserializer=vmmigration.CloneJob.deserialize,
            )
        return self._stubs["get_clone_job"]

    @property
    def create_cutover_job(
        self,
    ) -> Callable[[vmmigration.CreateCutoverJobRequest], operations_pb2.Operation]:
        r"""Return a callable for the create cutover job method over gRPC.

        Initiates a Cutover of a specific migrating VM.
        The returned LRO is completed when the cutover job
        resource is created and the job is initiated.

        Returns:
            Callable[[~.CreateCutoverJobRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_cutover_job" not in self._stubs:
            self._stubs["create_cutover_job"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/CreateCutoverJob",
                request_serializer=vmmigration.CreateCutoverJobRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_cutover_job"]

    @property
    def cancel_cutover_job(
        self,
    ) -> Callable[[vmmigration.CancelCutoverJobRequest], operations_pb2.Operation]:
        r"""Return a callable for the cancel cutover job method over gRPC.

        Initiates the cancellation of a running cutover job.

        Returns:
            Callable[[~.CancelCutoverJobRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "cancel_cutover_job" not in self._stubs:
            self._stubs["cancel_cutover_job"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/CancelCutoverJob",
                request_serializer=vmmigration.CancelCutoverJobRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["cancel_cutover_job"]

    @property
    def list_cutover_jobs(
        self,
    ) -> Callable[
        [vmmigration.ListCutoverJobsRequest], vmmigration.ListCutoverJobsResponse
    ]:
        r"""Return a callable for the list cutover jobs method over gRPC.

        Lists the CutoverJobs of a migrating VM. Only 25 most
        recent CutoverJobs are listed.

        Returns:
            Callable[[~.ListCutoverJobsRequest],
                    ~.ListCutoverJobsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_cutover_jobs" not in self._stubs:
            self._stubs["list_cutover_jobs"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/ListCutoverJobs",
                request_serializer=vmmigration.ListCutoverJobsRequest.serialize,
                response_deserializer=vmmigration.ListCutoverJobsResponse.deserialize,
            )
        return self._stubs["list_cutover_jobs"]

    @property
    def get_cutover_job(
        self,
    ) -> Callable[[vmmigration.GetCutoverJobRequest], vmmigration.CutoverJob]:
        r"""Return a callable for the get cutover job method over gRPC.

        Gets details of a single CutoverJob.

        Returns:
            Callable[[~.GetCutoverJobRequest],
                    ~.CutoverJob]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_cutover_job" not in self._stubs:
            self._stubs["get_cutover_job"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/GetCutoverJob",
                request_serializer=vmmigration.GetCutoverJobRequest.serialize,
                response_deserializer=vmmigration.CutoverJob.deserialize,
            )
        return self._stubs["get_cutover_job"]

    @property
    def list_groups(
        self,
    ) -> Callable[[vmmigration.ListGroupsRequest], vmmigration.ListGroupsResponse]:
        r"""Return a callable for the list groups method over gRPC.

        Lists Groups in a given project and location.

        Returns:
            Callable[[~.ListGroupsRequest],
                    ~.ListGroupsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_groups" not in self._stubs:
            self._stubs["list_groups"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/ListGroups",
                request_serializer=vmmigration.ListGroupsRequest.serialize,
                response_deserializer=vmmigration.ListGroupsResponse.deserialize,
            )
        return self._stubs["list_groups"]

    @property
    def get_group(self) -> Callable[[vmmigration.GetGroupRequest], vmmigration.Group]:
        r"""Return a callable for the get group method over gRPC.

        Gets details of a single Group.

        Returns:
            Callable[[~.GetGroupRequest],
                    ~.Group]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_group" not in self._stubs:
            self._stubs["get_group"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/GetGroup",
                request_serializer=vmmigration.GetGroupRequest.serialize,
                response_deserializer=vmmigration.Group.deserialize,
            )
        return self._stubs["get_group"]

    @property
    def create_group(
        self,
    ) -> Callable[[vmmigration.CreateGroupRequest], operations_pb2.Operation]:
        r"""Return a callable for the create group method over gRPC.

        Creates a new Group in a given project and location.

        Returns:
            Callable[[~.CreateGroupRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_group" not in self._stubs:
            self._stubs["create_group"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/CreateGroup",
                request_serializer=vmmigration.CreateGroupRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_group"]

    @property
    def update_group(
        self,
    ) -> Callable[[vmmigration.UpdateGroupRequest], operations_pb2.Operation]:
        r"""Return a callable for the update group method over gRPC.

        Updates the parameters of a single Group.

        Returns:
            Callable[[~.UpdateGroupRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_group" not in self._stubs:
            self._stubs["update_group"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/UpdateGroup",
                request_serializer=vmmigration.UpdateGroupRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_group"]

    @property
    def delete_group(
        self,
    ) -> Callable[[vmmigration.DeleteGroupRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete group method over gRPC.

        Deletes a single Group.

        Returns:
            Callable[[~.DeleteGroupRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_group" not in self._stubs:
            self._stubs["delete_group"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/DeleteGroup",
                request_serializer=vmmigration.DeleteGroupRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_group"]

    @property
    def add_group_migration(
        self,
    ) -> Callable[[vmmigration.AddGroupMigrationRequest], operations_pb2.Operation]:
        r"""Return a callable for the add group migration method over gRPC.

        Adds a MigratingVm to a Group.

        Returns:
            Callable[[~.AddGroupMigrationRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "add_group_migration" not in self._stubs:
            self._stubs["add_group_migration"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/AddGroupMigration",
                request_serializer=vmmigration.AddGroupMigrationRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["add_group_migration"]

    @property
    def remove_group_migration(
        self,
    ) -> Callable[[vmmigration.RemoveGroupMigrationRequest], operations_pb2.Operation]:
        r"""Return a callable for the remove group migration method over gRPC.

        Removes a MigratingVm from a Group.

        Returns:
            Callable[[~.RemoveGroupMigrationRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "remove_group_migration" not in self._stubs:
            self._stubs["remove_group_migration"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/RemoveGroupMigration",
                request_serializer=vmmigration.RemoveGroupMigrationRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["remove_group_migration"]

    @property
    def list_target_projects(
        self,
    ) -> Callable[
        [vmmigration.ListTargetProjectsRequest], vmmigration.ListTargetProjectsResponse
    ]:
        r"""Return a callable for the list target projects method over gRPC.

        Lists TargetProjects in a given project.

        NOTE: TargetProject is a global resource; hence the only
        supported value for location is ``global``.

        Returns:
            Callable[[~.ListTargetProjectsRequest],
                    ~.ListTargetProjectsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_target_projects" not in self._stubs:
            self._stubs["list_target_projects"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/ListTargetProjects",
                request_serializer=vmmigration.ListTargetProjectsRequest.serialize,
                response_deserializer=vmmigration.ListTargetProjectsResponse.deserialize,
            )
        return self._stubs["list_target_projects"]

    @property
    def get_target_project(
        self,
    ) -> Callable[[vmmigration.GetTargetProjectRequest], vmmigration.TargetProject]:
        r"""Return a callable for the get target project method over gRPC.

        Gets details of a single TargetProject.

        NOTE: TargetProject is a global resource; hence the only
        supported value for location is ``global``.

        Returns:
            Callable[[~.GetTargetProjectRequest],
                    ~.TargetProject]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_target_project" not in self._stubs:
            self._stubs["get_target_project"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/GetTargetProject",
                request_serializer=vmmigration.GetTargetProjectRequest.serialize,
                response_deserializer=vmmigration.TargetProject.deserialize,
            )
        return self._stubs["get_target_project"]

    @property
    def create_target_project(
        self,
    ) -> Callable[[vmmigration.CreateTargetProjectRequest], operations_pb2.Operation]:
        r"""Return a callable for the create target project method over gRPC.

        Creates a new TargetProject in a given project.

        NOTE: TargetProject is a global resource; hence the only
        supported value for location is ``global``.

        Returns:
            Callable[[~.CreateTargetProjectRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_target_project" not in self._stubs:
            self._stubs["create_target_project"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/CreateTargetProject",
                request_serializer=vmmigration.CreateTargetProjectRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_target_project"]

    @property
    def update_target_project(
        self,
    ) -> Callable[[vmmigration.UpdateTargetProjectRequest], operations_pb2.Operation]:
        r"""Return a callable for the update target project method over gRPC.

        Updates the parameters of a single TargetProject.

        NOTE: TargetProject is a global resource; hence the only
        supported value for location is ``global``.

        Returns:
            Callable[[~.UpdateTargetProjectRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_target_project" not in self._stubs:
            self._stubs["update_target_project"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/UpdateTargetProject",
                request_serializer=vmmigration.UpdateTargetProjectRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_target_project"]

    @property
    def delete_target_project(
        self,
    ) -> Callable[[vmmigration.DeleteTargetProjectRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete target project method over gRPC.

        Deletes a single TargetProject.

        NOTE: TargetProject is a global resource; hence the only
        supported value for location is ``global``.

        Returns:
            Callable[[~.DeleteTargetProjectRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_target_project" not in self._stubs:
            self._stubs["delete_target_project"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/DeleteTargetProject",
                request_serializer=vmmigration.DeleteTargetProjectRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_target_project"]

    @property
    def list_replication_cycles(
        self,
    ) -> Callable[
        [vmmigration.ListReplicationCyclesRequest],
        vmmigration.ListReplicationCyclesResponse,
    ]:
        r"""Return a callable for the list replication cycles method over gRPC.

        Lists ReplicationCycles in a given MigratingVM.

        Returns:
            Callable[[~.ListReplicationCyclesRequest],
                    ~.ListReplicationCyclesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_replication_cycles" not in self._stubs:
            self._stubs["list_replication_cycles"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/ListReplicationCycles",
                request_serializer=vmmigration.ListReplicationCyclesRequest.serialize,
                response_deserializer=vmmigration.ListReplicationCyclesResponse.deserialize,
            )
        return self._stubs["list_replication_cycles"]

    @property
    def get_replication_cycle(
        self,
    ) -> Callable[
        [vmmigration.GetReplicationCycleRequest], vmmigration.ReplicationCycle
    ]:
        r"""Return a callable for the get replication cycle method over gRPC.

        Gets details of a single ReplicationCycle.

        Returns:
            Callable[[~.GetReplicationCycleRequest],
                    ~.ReplicationCycle]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_replication_cycle" not in self._stubs:
            self._stubs["get_replication_cycle"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/GetReplicationCycle",
                request_serializer=vmmigration.GetReplicationCycleRequest.serialize,
                response_deserializer=vmmigration.ReplicationCycle.deserialize,
            )
        return self._stubs["get_replication_cycle"]

    @property
    def list_image_imports(
        self,
    ) -> Callable[
        [vmmigration.ListImageImportsRequest], vmmigration.ListImageImportsResponse
    ]:
        r"""Return a callable for the list image imports method over gRPC.

        Lists ImageImports in a given project.

        Returns:
            Callable[[~.ListImageImportsRequest],
                    ~.ListImageImportsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_image_imports" not in self._stubs:
            self._stubs["list_image_imports"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/ListImageImports",
                request_serializer=vmmigration.ListImageImportsRequest.serialize,
                response_deserializer=vmmigration.ListImageImportsResponse.deserialize,
            )
        return self._stubs["list_image_imports"]

    @property
    def get_image_import(
        self,
    ) -> Callable[[vmmigration.GetImageImportRequest], vmmigration.ImageImport]:
        r"""Return a callable for the get image import method over gRPC.

        Gets details of a single ImageImport.

        Returns:
            Callable[[~.GetImageImportRequest],
                    ~.ImageImport]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_image_import" not in self._stubs:
            self._stubs["get_image_import"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/GetImageImport",
                request_serializer=vmmigration.GetImageImportRequest.serialize,
                response_deserializer=vmmigration.ImageImport.deserialize,
            )
        return self._stubs["get_image_import"]

    @property
    def create_image_import(
        self,
    ) -> Callable[[vmmigration.CreateImageImportRequest], operations_pb2.Operation]:
        r"""Return a callable for the create image import method over gRPC.

        Creates a new ImageImport in a given project.

        Returns:
            Callable[[~.CreateImageImportRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_image_import" not in self._stubs:
            self._stubs["create_image_import"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/CreateImageImport",
                request_serializer=vmmigration.CreateImageImportRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_image_import"]

    @property
    def delete_image_import(
        self,
    ) -> Callable[[vmmigration.DeleteImageImportRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete image import method over gRPC.

        Deletes a single ImageImport.

        Returns:
            Callable[[~.DeleteImageImportRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_image_import" not in self._stubs:
            self._stubs["delete_image_import"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/DeleteImageImport",
                request_serializer=vmmigration.DeleteImageImportRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_image_import"]

    @property
    def list_image_import_jobs(
        self,
    ) -> Callable[
        [vmmigration.ListImageImportJobsRequest],
        vmmigration.ListImageImportJobsResponse,
    ]:
        r"""Return a callable for the list image import jobs method over gRPC.

        Lists ImageImportJobs in a given project.

        Returns:
            Callable[[~.ListImageImportJobsRequest],
                    ~.ListImageImportJobsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_image_import_jobs" not in self._stubs:
            self._stubs["list_image_import_jobs"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/ListImageImportJobs",
                request_serializer=vmmigration.ListImageImportJobsRequest.serialize,
                response_deserializer=vmmigration.ListImageImportJobsResponse.deserialize,
            )
        return self._stubs["list_image_import_jobs"]

    @property
    def get_image_import_job(
        self,
    ) -> Callable[[vmmigration.GetImageImportJobRequest], vmmigration.ImageImportJob]:
        r"""Return a callable for the get image import job method over gRPC.

        Gets details of a single ImageImportJob.

        Returns:
            Callable[[~.GetImageImportJobRequest],
                    ~.ImageImportJob]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_image_import_job" not in self._stubs:
            self._stubs["get_image_import_job"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/GetImageImportJob",
                request_serializer=vmmigration.GetImageImportJobRequest.serialize,
                response_deserializer=vmmigration.ImageImportJob.deserialize,
            )
        return self._stubs["get_image_import_job"]

    @property
    def cancel_image_import_job(
        self,
    ) -> Callable[[vmmigration.CancelImageImportJobRequest], operations_pb2.Operation]:
        r"""Return a callable for the cancel image import job method over gRPC.

        Initiates the cancellation of a running
        ImageImportJob.

        Returns:
            Callable[[~.CancelImageImportJobRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "cancel_image_import_job" not in self._stubs:
            self._stubs["cancel_image_import_job"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/CancelImageImportJob",
                request_serializer=vmmigration.CancelImageImportJobRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["cancel_image_import_job"]

    @property
    def create_disk_migration_job(
        self,
    ) -> Callable[
        [vmmigration.CreateDiskMigrationJobRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the create disk migration job method over gRPC.

        Creates a new disk migration job in a given Source.

        Returns:
            Callable[[~.CreateDiskMigrationJobRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_disk_migration_job" not in self._stubs:
            self._stubs["create_disk_migration_job"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/CreateDiskMigrationJob",
                request_serializer=vmmigration.CreateDiskMigrationJobRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_disk_migration_job"]

    @property
    def list_disk_migration_jobs(
        self,
    ) -> Callable[
        [vmmigration.ListDiskMigrationJobsRequest],
        vmmigration.ListDiskMigrationJobsResponse,
    ]:
        r"""Return a callable for the list disk migration jobs method over gRPC.

        Lists DiskMigrationJobs in a given Source.

        Returns:
            Callable[[~.ListDiskMigrationJobsRequest],
                    ~.ListDiskMigrationJobsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_disk_migration_jobs" not in self._stubs:
            self._stubs["list_disk_migration_jobs"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/ListDiskMigrationJobs",
                request_serializer=vmmigration.ListDiskMigrationJobsRequest.serialize,
                response_deserializer=vmmigration.ListDiskMigrationJobsResponse.deserialize,
            )
        return self._stubs["list_disk_migration_jobs"]

    @property
    def get_disk_migration_job(
        self,
    ) -> Callable[
        [vmmigration.GetDiskMigrationJobRequest], vmmigration.DiskMigrationJob
    ]:
        r"""Return a callable for the get disk migration job method over gRPC.

        Gets details of a single DiskMigrationJob.

        Returns:
            Callable[[~.GetDiskMigrationJobRequest],
                    ~.DiskMigrationJob]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_disk_migration_job" not in self._stubs:
            self._stubs["get_disk_migration_job"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/GetDiskMigrationJob",
                request_serializer=vmmigration.GetDiskMigrationJobRequest.serialize,
                response_deserializer=vmmigration.DiskMigrationJob.deserialize,
            )
        return self._stubs["get_disk_migration_job"]

    @property
    def update_disk_migration_job(
        self,
    ) -> Callable[
        [vmmigration.UpdateDiskMigrationJobRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the update disk migration job method over gRPC.

        Updates the parameters of a single DiskMigrationJob.

        Returns:
            Callable[[~.UpdateDiskMigrationJobRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_disk_migration_job" not in self._stubs:
            self._stubs["update_disk_migration_job"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/UpdateDiskMigrationJob",
                request_serializer=vmmigration.UpdateDiskMigrationJobRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_disk_migration_job"]

    @property
    def delete_disk_migration_job(
        self,
    ) -> Callable[
        [vmmigration.DeleteDiskMigrationJobRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the delete disk migration job method over gRPC.

        Deletes a single DiskMigrationJob.

        Returns:
            Callable[[~.DeleteDiskMigrationJobRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_disk_migration_job" not in self._stubs:
            self._stubs["delete_disk_migration_job"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/DeleteDiskMigrationJob",
                request_serializer=vmmigration.DeleteDiskMigrationJobRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_disk_migration_job"]

    @property
    def run_disk_migration_job(
        self,
    ) -> Callable[[vmmigration.RunDiskMigrationJobRequest], operations_pb2.Operation]:
        r"""Return a callable for the run disk migration job method over gRPC.

        Runs the disk migration job.

        Returns:
            Callable[[~.RunDiskMigrationJobRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "run_disk_migration_job" not in self._stubs:
            self._stubs["run_disk_migration_job"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/RunDiskMigrationJob",
                request_serializer=vmmigration.RunDiskMigrationJobRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["run_disk_migration_job"]

    @property
    def cancel_disk_migration_job(
        self,
    ) -> Callable[
        [vmmigration.CancelDiskMigrationJobRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the cancel disk migration job method over gRPC.

        Cancels the disk migration job.

        Returns:
            Callable[[~.CancelDiskMigrationJobRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "cancel_disk_migration_job" not in self._stubs:
            self._stubs["cancel_disk_migration_job"] = self._logged_channel.unary_unary(
                "/google.cloud.vmmigration.v1.VmMigration/CancelDiskMigrationJob",
                request_serializer=vmmigration.CancelDiskMigrationJobRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["cancel_disk_migration_job"]

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


__all__ = ("VmMigrationGrpcTransport",)
