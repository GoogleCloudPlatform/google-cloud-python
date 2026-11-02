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

from google.cloud.telcoautomation_v1.types import telcoautomation

from .base import DEFAULT_CLIENT_INFO, TelcoAutomationTransport

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
                    "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
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
                    "serviceName": "google.cloud.telcoautomation.v1.TelcoAutomation",
                    "rpcName": client_call_details.method,
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class TelcoAutomationGrpcTransport(TelcoAutomationTransport):
    """gRPC backend transport for TelcoAutomation.

    TelcoAutomation Service manages the control plane cluster
    a.k.a. Orchestration Cluster (GKE cluster with config
    controller) of TNA. It also exposes blueprint APIs which manages
    the lifecycle of blueprints that control the infrastructure
    setup (e.g GDCE clusters) and deployment of network functions.

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
        host: str = "telcoautomation.googleapis.com",
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
                 The hostname to connect to (default: 'telcoautomation.googleapis.com').
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
        host: str = "telcoautomation.googleapis.com",
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
    def list_orchestration_clusters(
        self,
    ) -> Callable[
        [telcoautomation.ListOrchestrationClustersRequest],
        telcoautomation.ListOrchestrationClustersResponse,
    ]:
        r"""Return a callable for the list orchestration clusters method over gRPC.

        Lists OrchestrationClusters in a given project and
        location.

        Returns:
            Callable[[~.ListOrchestrationClustersRequest],
                    ~.ListOrchestrationClustersResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_orchestration_clusters" not in self._stubs:
            self._stubs["list_orchestration_clusters"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.telcoautomation.v1.TelcoAutomation/ListOrchestrationClusters",
                    request_serializer=telcoautomation.ListOrchestrationClustersRequest.serialize,
                    response_deserializer=telcoautomation.ListOrchestrationClustersResponse.deserialize,
                )
            )
        return self._stubs["list_orchestration_clusters"]

    @property
    def get_orchestration_cluster(
        self,
    ) -> Callable[
        [telcoautomation.GetOrchestrationClusterRequest],
        telcoautomation.OrchestrationCluster,
    ]:
        r"""Return a callable for the get orchestration cluster method over gRPC.

        Gets details of a single OrchestrationCluster.

        Returns:
            Callable[[~.GetOrchestrationClusterRequest],
                    ~.OrchestrationCluster]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_orchestration_cluster" not in self._stubs:
            self._stubs["get_orchestration_cluster"] = self._logged_channel.unary_unary(
                "/google.cloud.telcoautomation.v1.TelcoAutomation/GetOrchestrationCluster",
                request_serializer=telcoautomation.GetOrchestrationClusterRequest.serialize,
                response_deserializer=telcoautomation.OrchestrationCluster.deserialize,
            )
        return self._stubs["get_orchestration_cluster"]

    @property
    def create_orchestration_cluster(
        self,
    ) -> Callable[
        [telcoautomation.CreateOrchestrationClusterRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the create orchestration cluster method over gRPC.

        Creates a new OrchestrationCluster in a given project
        and location.

        Returns:
            Callable[[~.CreateOrchestrationClusterRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_orchestration_cluster" not in self._stubs:
            self._stubs["create_orchestration_cluster"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.telcoautomation.v1.TelcoAutomation/CreateOrchestrationCluster",
                    request_serializer=telcoautomation.CreateOrchestrationClusterRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["create_orchestration_cluster"]

    @property
    def delete_orchestration_cluster(
        self,
    ) -> Callable[
        [telcoautomation.DeleteOrchestrationClusterRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the delete orchestration cluster method over gRPC.

        Deletes a single OrchestrationCluster.

        Returns:
            Callable[[~.DeleteOrchestrationClusterRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_orchestration_cluster" not in self._stubs:
            self._stubs["delete_orchestration_cluster"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.telcoautomation.v1.TelcoAutomation/DeleteOrchestrationCluster",
                    request_serializer=telcoautomation.DeleteOrchestrationClusterRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["delete_orchestration_cluster"]

    @property
    def list_edge_slms(
        self,
    ) -> Callable[
        [telcoautomation.ListEdgeSlmsRequest], telcoautomation.ListEdgeSlmsResponse
    ]:
        r"""Return a callable for the list edge slms method over gRPC.

        Lists EdgeSlms in a given project and location.

        Returns:
            Callable[[~.ListEdgeSlmsRequest],
                    ~.ListEdgeSlmsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_edge_slms" not in self._stubs:
            self._stubs["list_edge_slms"] = self._logged_channel.unary_unary(
                "/google.cloud.telcoautomation.v1.TelcoAutomation/ListEdgeSlms",
                request_serializer=telcoautomation.ListEdgeSlmsRequest.serialize,
                response_deserializer=telcoautomation.ListEdgeSlmsResponse.deserialize,
            )
        return self._stubs["list_edge_slms"]

    @property
    def get_edge_slm(
        self,
    ) -> Callable[[telcoautomation.GetEdgeSlmRequest], telcoautomation.EdgeSlm]:
        r"""Return a callable for the get edge slm method over gRPC.

        Gets details of a single EdgeSlm.

        Returns:
            Callable[[~.GetEdgeSlmRequest],
                    ~.EdgeSlm]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_edge_slm" not in self._stubs:
            self._stubs["get_edge_slm"] = self._logged_channel.unary_unary(
                "/google.cloud.telcoautomation.v1.TelcoAutomation/GetEdgeSlm",
                request_serializer=telcoautomation.GetEdgeSlmRequest.serialize,
                response_deserializer=telcoautomation.EdgeSlm.deserialize,
            )
        return self._stubs["get_edge_slm"]

    @property
    def create_edge_slm(
        self,
    ) -> Callable[[telcoautomation.CreateEdgeSlmRequest], operations_pb2.Operation]:
        r"""Return a callable for the create edge slm method over gRPC.

        Creates a new EdgeSlm in a given project and
        location.

        Returns:
            Callable[[~.CreateEdgeSlmRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_edge_slm" not in self._stubs:
            self._stubs["create_edge_slm"] = self._logged_channel.unary_unary(
                "/google.cloud.telcoautomation.v1.TelcoAutomation/CreateEdgeSlm",
                request_serializer=telcoautomation.CreateEdgeSlmRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_edge_slm"]

    @property
    def delete_edge_slm(
        self,
    ) -> Callable[[telcoautomation.DeleteEdgeSlmRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete edge slm method over gRPC.

        Deletes a single EdgeSlm.

        Returns:
            Callable[[~.DeleteEdgeSlmRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_edge_slm" not in self._stubs:
            self._stubs["delete_edge_slm"] = self._logged_channel.unary_unary(
                "/google.cloud.telcoautomation.v1.TelcoAutomation/DeleteEdgeSlm",
                request_serializer=telcoautomation.DeleteEdgeSlmRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_edge_slm"]

    @property
    def create_blueprint(
        self,
    ) -> Callable[[telcoautomation.CreateBlueprintRequest], telcoautomation.Blueprint]:
        r"""Return a callable for the create blueprint method over gRPC.

        Creates a blueprint.

        Returns:
            Callable[[~.CreateBlueprintRequest],
                    ~.Blueprint]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_blueprint" not in self._stubs:
            self._stubs["create_blueprint"] = self._logged_channel.unary_unary(
                "/google.cloud.telcoautomation.v1.TelcoAutomation/CreateBlueprint",
                request_serializer=telcoautomation.CreateBlueprintRequest.serialize,
                response_deserializer=telcoautomation.Blueprint.deserialize,
            )
        return self._stubs["create_blueprint"]

    @property
    def update_blueprint(
        self,
    ) -> Callable[[telcoautomation.UpdateBlueprintRequest], telcoautomation.Blueprint]:
        r"""Return a callable for the update blueprint method over gRPC.

        Updates a blueprint.

        Returns:
            Callable[[~.UpdateBlueprintRequest],
                    ~.Blueprint]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_blueprint" not in self._stubs:
            self._stubs["update_blueprint"] = self._logged_channel.unary_unary(
                "/google.cloud.telcoautomation.v1.TelcoAutomation/UpdateBlueprint",
                request_serializer=telcoautomation.UpdateBlueprintRequest.serialize,
                response_deserializer=telcoautomation.Blueprint.deserialize,
            )
        return self._stubs["update_blueprint"]

    @property
    def get_blueprint(
        self,
    ) -> Callable[[telcoautomation.GetBlueprintRequest], telcoautomation.Blueprint]:
        r"""Return a callable for the get blueprint method over gRPC.

        Returns the requested blueprint.

        Returns:
            Callable[[~.GetBlueprintRequest],
                    ~.Blueprint]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_blueprint" not in self._stubs:
            self._stubs["get_blueprint"] = self._logged_channel.unary_unary(
                "/google.cloud.telcoautomation.v1.TelcoAutomation/GetBlueprint",
                request_serializer=telcoautomation.GetBlueprintRequest.serialize,
                response_deserializer=telcoautomation.Blueprint.deserialize,
            )
        return self._stubs["get_blueprint"]

    @property
    def delete_blueprint(
        self,
    ) -> Callable[[telcoautomation.DeleteBlueprintRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete blueprint method over gRPC.

        Deletes a blueprint and all its revisions.

        Returns:
            Callable[[~.DeleteBlueprintRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_blueprint" not in self._stubs:
            self._stubs["delete_blueprint"] = self._logged_channel.unary_unary(
                "/google.cloud.telcoautomation.v1.TelcoAutomation/DeleteBlueprint",
                request_serializer=telcoautomation.DeleteBlueprintRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_blueprint"]

    @property
    def list_blueprints(
        self,
    ) -> Callable[
        [telcoautomation.ListBlueprintsRequest], telcoautomation.ListBlueprintsResponse
    ]:
        r"""Return a callable for the list blueprints method over gRPC.

        List all blueprints.

        Returns:
            Callable[[~.ListBlueprintsRequest],
                    ~.ListBlueprintsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_blueprints" not in self._stubs:
            self._stubs["list_blueprints"] = self._logged_channel.unary_unary(
                "/google.cloud.telcoautomation.v1.TelcoAutomation/ListBlueprints",
                request_serializer=telcoautomation.ListBlueprintsRequest.serialize,
                response_deserializer=telcoautomation.ListBlueprintsResponse.deserialize,
            )
        return self._stubs["list_blueprints"]

    @property
    def approve_blueprint(
        self,
    ) -> Callable[[telcoautomation.ApproveBlueprintRequest], telcoautomation.Blueprint]:
        r"""Return a callable for the approve blueprint method over gRPC.

        Approves a blueprint and commits a new revision.

        Returns:
            Callable[[~.ApproveBlueprintRequest],
                    ~.Blueprint]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "approve_blueprint" not in self._stubs:
            self._stubs["approve_blueprint"] = self._logged_channel.unary_unary(
                "/google.cloud.telcoautomation.v1.TelcoAutomation/ApproveBlueprint",
                request_serializer=telcoautomation.ApproveBlueprintRequest.serialize,
                response_deserializer=telcoautomation.Blueprint.deserialize,
            )
        return self._stubs["approve_blueprint"]

    @property
    def propose_blueprint(
        self,
    ) -> Callable[[telcoautomation.ProposeBlueprintRequest], telcoautomation.Blueprint]:
        r"""Return a callable for the propose blueprint method over gRPC.

        Proposes a blueprint for approval of changes.

        Returns:
            Callable[[~.ProposeBlueprintRequest],
                    ~.Blueprint]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "propose_blueprint" not in self._stubs:
            self._stubs["propose_blueprint"] = self._logged_channel.unary_unary(
                "/google.cloud.telcoautomation.v1.TelcoAutomation/ProposeBlueprint",
                request_serializer=telcoautomation.ProposeBlueprintRequest.serialize,
                response_deserializer=telcoautomation.Blueprint.deserialize,
            )
        return self._stubs["propose_blueprint"]

    @property
    def reject_blueprint(
        self,
    ) -> Callable[[telcoautomation.RejectBlueprintRequest], telcoautomation.Blueprint]:
        r"""Return a callable for the reject blueprint method over gRPC.

        Rejects a blueprint revision proposal and flips it
        back to Draft state.

        Returns:
            Callable[[~.RejectBlueprintRequest],
                    ~.Blueprint]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "reject_blueprint" not in self._stubs:
            self._stubs["reject_blueprint"] = self._logged_channel.unary_unary(
                "/google.cloud.telcoautomation.v1.TelcoAutomation/RejectBlueprint",
                request_serializer=telcoautomation.RejectBlueprintRequest.serialize,
                response_deserializer=telcoautomation.Blueprint.deserialize,
            )
        return self._stubs["reject_blueprint"]

    @property
    def list_blueprint_revisions(
        self,
    ) -> Callable[
        [telcoautomation.ListBlueprintRevisionsRequest],
        telcoautomation.ListBlueprintRevisionsResponse,
    ]:
        r"""Return a callable for the list blueprint revisions method over gRPC.

        List blueprint revisions of a given blueprint.

        Returns:
            Callable[[~.ListBlueprintRevisionsRequest],
                    ~.ListBlueprintRevisionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_blueprint_revisions" not in self._stubs:
            self._stubs["list_blueprint_revisions"] = self._logged_channel.unary_unary(
                "/google.cloud.telcoautomation.v1.TelcoAutomation/ListBlueprintRevisions",
                request_serializer=telcoautomation.ListBlueprintRevisionsRequest.serialize,
                response_deserializer=telcoautomation.ListBlueprintRevisionsResponse.deserialize,
            )
        return self._stubs["list_blueprint_revisions"]

    @property
    def search_blueprint_revisions(
        self,
    ) -> Callable[
        [telcoautomation.SearchBlueprintRevisionsRequest],
        telcoautomation.SearchBlueprintRevisionsResponse,
    ]:
        r"""Return a callable for the search blueprint revisions method over gRPC.

        Searches across blueprint revisions.

        Returns:
            Callable[[~.SearchBlueprintRevisionsRequest],
                    ~.SearchBlueprintRevisionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "search_blueprint_revisions" not in self._stubs:
            self._stubs["search_blueprint_revisions"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.telcoautomation.v1.TelcoAutomation/SearchBlueprintRevisions",
                    request_serializer=telcoautomation.SearchBlueprintRevisionsRequest.serialize,
                    response_deserializer=telcoautomation.SearchBlueprintRevisionsResponse.deserialize,
                )
            )
        return self._stubs["search_blueprint_revisions"]

    @property
    def search_deployment_revisions(
        self,
    ) -> Callable[
        [telcoautomation.SearchDeploymentRevisionsRequest],
        telcoautomation.SearchDeploymentRevisionsResponse,
    ]:
        r"""Return a callable for the search deployment revisions method over gRPC.

        Searches across deployment revisions.

        Returns:
            Callable[[~.SearchDeploymentRevisionsRequest],
                    ~.SearchDeploymentRevisionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "search_deployment_revisions" not in self._stubs:
            self._stubs["search_deployment_revisions"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.telcoautomation.v1.TelcoAutomation/SearchDeploymentRevisions",
                    request_serializer=telcoautomation.SearchDeploymentRevisionsRequest.serialize,
                    response_deserializer=telcoautomation.SearchDeploymentRevisionsResponse.deserialize,
                )
            )
        return self._stubs["search_deployment_revisions"]

    @property
    def discard_blueprint_changes(
        self,
    ) -> Callable[
        [telcoautomation.DiscardBlueprintChangesRequest],
        telcoautomation.DiscardBlueprintChangesResponse,
    ]:
        r"""Return a callable for the discard blueprint changes method over gRPC.

        Discards the changes in a blueprint and reverts the
        blueprint to the last approved blueprint revision. No
        changes take place if a blueprint does not have
        revisions.

        Returns:
            Callable[[~.DiscardBlueprintChangesRequest],
                    ~.DiscardBlueprintChangesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "discard_blueprint_changes" not in self._stubs:
            self._stubs["discard_blueprint_changes"] = self._logged_channel.unary_unary(
                "/google.cloud.telcoautomation.v1.TelcoAutomation/DiscardBlueprintChanges",
                request_serializer=telcoautomation.DiscardBlueprintChangesRequest.serialize,
                response_deserializer=telcoautomation.DiscardBlueprintChangesResponse.deserialize,
            )
        return self._stubs["discard_blueprint_changes"]

    @property
    def list_public_blueprints(
        self,
    ) -> Callable[
        [telcoautomation.ListPublicBlueprintsRequest],
        telcoautomation.ListPublicBlueprintsResponse,
    ]:
        r"""Return a callable for the list public blueprints method over gRPC.

        Lists the blueprints in TNA's public catalog. Default
        page size = 20, Max Page Size = 100.

        Returns:
            Callable[[~.ListPublicBlueprintsRequest],
                    ~.ListPublicBlueprintsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_public_blueprints" not in self._stubs:
            self._stubs["list_public_blueprints"] = self._logged_channel.unary_unary(
                "/google.cloud.telcoautomation.v1.TelcoAutomation/ListPublicBlueprints",
                request_serializer=telcoautomation.ListPublicBlueprintsRequest.serialize,
                response_deserializer=telcoautomation.ListPublicBlueprintsResponse.deserialize,
            )
        return self._stubs["list_public_blueprints"]

    @property
    def get_public_blueprint(
        self,
    ) -> Callable[
        [telcoautomation.GetPublicBlueprintRequest], telcoautomation.PublicBlueprint
    ]:
        r"""Return a callable for the get public blueprint method over gRPC.

        Returns the requested public blueprint.

        Returns:
            Callable[[~.GetPublicBlueprintRequest],
                    ~.PublicBlueprint]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_public_blueprint" not in self._stubs:
            self._stubs["get_public_blueprint"] = self._logged_channel.unary_unary(
                "/google.cloud.telcoautomation.v1.TelcoAutomation/GetPublicBlueprint",
                request_serializer=telcoautomation.GetPublicBlueprintRequest.serialize,
                response_deserializer=telcoautomation.PublicBlueprint.deserialize,
            )
        return self._stubs["get_public_blueprint"]

    @property
    def create_deployment(
        self,
    ) -> Callable[
        [telcoautomation.CreateDeploymentRequest], telcoautomation.Deployment
    ]:
        r"""Return a callable for the create deployment method over gRPC.

        Creates a deployment.

        Returns:
            Callable[[~.CreateDeploymentRequest],
                    ~.Deployment]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_deployment" not in self._stubs:
            self._stubs["create_deployment"] = self._logged_channel.unary_unary(
                "/google.cloud.telcoautomation.v1.TelcoAutomation/CreateDeployment",
                request_serializer=telcoautomation.CreateDeploymentRequest.serialize,
                response_deserializer=telcoautomation.Deployment.deserialize,
            )
        return self._stubs["create_deployment"]

    @property
    def update_deployment(
        self,
    ) -> Callable[
        [telcoautomation.UpdateDeploymentRequest], telcoautomation.Deployment
    ]:
        r"""Return a callable for the update deployment method over gRPC.

        Updates a deployment.

        Returns:
            Callable[[~.UpdateDeploymentRequest],
                    ~.Deployment]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_deployment" not in self._stubs:
            self._stubs["update_deployment"] = self._logged_channel.unary_unary(
                "/google.cloud.telcoautomation.v1.TelcoAutomation/UpdateDeployment",
                request_serializer=telcoautomation.UpdateDeploymentRequest.serialize,
                response_deserializer=telcoautomation.Deployment.deserialize,
            )
        return self._stubs["update_deployment"]

    @property
    def get_deployment(
        self,
    ) -> Callable[[telcoautomation.GetDeploymentRequest], telcoautomation.Deployment]:
        r"""Return a callable for the get deployment method over gRPC.

        Returns the requested deployment.

        Returns:
            Callable[[~.GetDeploymentRequest],
                    ~.Deployment]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_deployment" not in self._stubs:
            self._stubs["get_deployment"] = self._logged_channel.unary_unary(
                "/google.cloud.telcoautomation.v1.TelcoAutomation/GetDeployment",
                request_serializer=telcoautomation.GetDeploymentRequest.serialize,
                response_deserializer=telcoautomation.Deployment.deserialize,
            )
        return self._stubs["get_deployment"]

    @property
    def remove_deployment(
        self,
    ) -> Callable[[telcoautomation.RemoveDeploymentRequest], empty_pb2.Empty]:
        r"""Return a callable for the remove deployment method over gRPC.

        Removes the deployment by marking it as DELETING.
        Post which deployment and it's revisions gets deleted.

        Returns:
            Callable[[~.RemoveDeploymentRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "remove_deployment" not in self._stubs:
            self._stubs["remove_deployment"] = self._logged_channel.unary_unary(
                "/google.cloud.telcoautomation.v1.TelcoAutomation/RemoveDeployment",
                request_serializer=telcoautomation.RemoveDeploymentRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["remove_deployment"]

    @property
    def list_deployments(
        self,
    ) -> Callable[
        [telcoautomation.ListDeploymentsRequest],
        telcoautomation.ListDeploymentsResponse,
    ]:
        r"""Return a callable for the list deployments method over gRPC.

        List all deployments.

        Returns:
            Callable[[~.ListDeploymentsRequest],
                    ~.ListDeploymentsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_deployments" not in self._stubs:
            self._stubs["list_deployments"] = self._logged_channel.unary_unary(
                "/google.cloud.telcoautomation.v1.TelcoAutomation/ListDeployments",
                request_serializer=telcoautomation.ListDeploymentsRequest.serialize,
                response_deserializer=telcoautomation.ListDeploymentsResponse.deserialize,
            )
        return self._stubs["list_deployments"]

    @property
    def list_deployment_revisions(
        self,
    ) -> Callable[
        [telcoautomation.ListDeploymentRevisionsRequest],
        telcoautomation.ListDeploymentRevisionsResponse,
    ]:
        r"""Return a callable for the list deployment revisions method over gRPC.

        List deployment revisions of a given deployment.

        Returns:
            Callable[[~.ListDeploymentRevisionsRequest],
                    ~.ListDeploymentRevisionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_deployment_revisions" not in self._stubs:
            self._stubs["list_deployment_revisions"] = self._logged_channel.unary_unary(
                "/google.cloud.telcoautomation.v1.TelcoAutomation/ListDeploymentRevisions",
                request_serializer=telcoautomation.ListDeploymentRevisionsRequest.serialize,
                response_deserializer=telcoautomation.ListDeploymentRevisionsResponse.deserialize,
            )
        return self._stubs["list_deployment_revisions"]

    @property
    def discard_deployment_changes(
        self,
    ) -> Callable[
        [telcoautomation.DiscardDeploymentChangesRequest],
        telcoautomation.DiscardDeploymentChangesResponse,
    ]:
        r"""Return a callable for the discard deployment changes method over gRPC.

        Discards the changes in a deployment and reverts the
        deployment to the last approved deployment revision. No
        changes take place if a deployment does not have
        revisions.

        Returns:
            Callable[[~.DiscardDeploymentChangesRequest],
                    ~.DiscardDeploymentChangesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "discard_deployment_changes" not in self._stubs:
            self._stubs["discard_deployment_changes"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.telcoautomation.v1.TelcoAutomation/DiscardDeploymentChanges",
                    request_serializer=telcoautomation.DiscardDeploymentChangesRequest.serialize,
                    response_deserializer=telcoautomation.DiscardDeploymentChangesResponse.deserialize,
                )
            )
        return self._stubs["discard_deployment_changes"]

    @property
    def apply_deployment(
        self,
    ) -> Callable[[telcoautomation.ApplyDeploymentRequest], telcoautomation.Deployment]:
        r"""Return a callable for the apply deployment method over gRPC.

        Applies the deployment's YAML files to the parent
        orchestration cluster.

        Returns:
            Callable[[~.ApplyDeploymentRequest],
                    ~.Deployment]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "apply_deployment" not in self._stubs:
            self._stubs["apply_deployment"] = self._logged_channel.unary_unary(
                "/google.cloud.telcoautomation.v1.TelcoAutomation/ApplyDeployment",
                request_serializer=telcoautomation.ApplyDeploymentRequest.serialize,
                response_deserializer=telcoautomation.Deployment.deserialize,
            )
        return self._stubs["apply_deployment"]

    @property
    def compute_deployment_status(
        self,
    ) -> Callable[
        [telcoautomation.ComputeDeploymentStatusRequest],
        telcoautomation.ComputeDeploymentStatusResponse,
    ]:
        r"""Return a callable for the compute deployment status method over gRPC.

        Returns the requested deployment status.

        Returns:
            Callable[[~.ComputeDeploymentStatusRequest],
                    ~.ComputeDeploymentStatusResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "compute_deployment_status" not in self._stubs:
            self._stubs["compute_deployment_status"] = self._logged_channel.unary_unary(
                "/google.cloud.telcoautomation.v1.TelcoAutomation/ComputeDeploymentStatus",
                request_serializer=telcoautomation.ComputeDeploymentStatusRequest.serialize,
                response_deserializer=telcoautomation.ComputeDeploymentStatusResponse.deserialize,
            )
        return self._stubs["compute_deployment_status"]

    @property
    def rollback_deployment(
        self,
    ) -> Callable[
        [telcoautomation.RollbackDeploymentRequest], telcoautomation.Deployment
    ]:
        r"""Return a callable for the rollback deployment method over gRPC.

        Rollback the active deployment to the given past
        approved deployment revision.

        Returns:
            Callable[[~.RollbackDeploymentRequest],
                    ~.Deployment]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "rollback_deployment" not in self._stubs:
            self._stubs["rollback_deployment"] = self._logged_channel.unary_unary(
                "/google.cloud.telcoautomation.v1.TelcoAutomation/RollbackDeployment",
                request_serializer=telcoautomation.RollbackDeploymentRequest.serialize,
                response_deserializer=telcoautomation.Deployment.deserialize,
            )
        return self._stubs["rollback_deployment"]

    @property
    def get_hydrated_deployment(
        self,
    ) -> Callable[
        [telcoautomation.GetHydratedDeploymentRequest],
        telcoautomation.HydratedDeployment,
    ]:
        r"""Return a callable for the get hydrated deployment method over gRPC.

        Returns the requested hydrated deployment.

        Returns:
            Callable[[~.GetHydratedDeploymentRequest],
                    ~.HydratedDeployment]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_hydrated_deployment" not in self._stubs:
            self._stubs["get_hydrated_deployment"] = self._logged_channel.unary_unary(
                "/google.cloud.telcoautomation.v1.TelcoAutomation/GetHydratedDeployment",
                request_serializer=telcoautomation.GetHydratedDeploymentRequest.serialize,
                response_deserializer=telcoautomation.HydratedDeployment.deserialize,
            )
        return self._stubs["get_hydrated_deployment"]

    @property
    def list_hydrated_deployments(
        self,
    ) -> Callable[
        [telcoautomation.ListHydratedDeploymentsRequest],
        telcoautomation.ListHydratedDeploymentsResponse,
    ]:
        r"""Return a callable for the list hydrated deployments method over gRPC.

        List all hydrated deployments present under a
        deployment.

        Returns:
            Callable[[~.ListHydratedDeploymentsRequest],
                    ~.ListHydratedDeploymentsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_hydrated_deployments" not in self._stubs:
            self._stubs["list_hydrated_deployments"] = self._logged_channel.unary_unary(
                "/google.cloud.telcoautomation.v1.TelcoAutomation/ListHydratedDeployments",
                request_serializer=telcoautomation.ListHydratedDeploymentsRequest.serialize,
                response_deserializer=telcoautomation.ListHydratedDeploymentsResponse.deserialize,
            )
        return self._stubs["list_hydrated_deployments"]

    @property
    def update_hydrated_deployment(
        self,
    ) -> Callable[
        [telcoautomation.UpdateHydratedDeploymentRequest],
        telcoautomation.HydratedDeployment,
    ]:
        r"""Return a callable for the update hydrated deployment method over gRPC.

        Updates a hydrated deployment.

        Returns:
            Callable[[~.UpdateHydratedDeploymentRequest],
                    ~.HydratedDeployment]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_hydrated_deployment" not in self._stubs:
            self._stubs["update_hydrated_deployment"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.telcoautomation.v1.TelcoAutomation/UpdateHydratedDeployment",
                    request_serializer=telcoautomation.UpdateHydratedDeploymentRequest.serialize,
                    response_deserializer=telcoautomation.HydratedDeployment.deserialize,
                )
            )
        return self._stubs["update_hydrated_deployment"]

    @property
    def apply_hydrated_deployment(
        self,
    ) -> Callable[
        [telcoautomation.ApplyHydratedDeploymentRequest],
        telcoautomation.HydratedDeployment,
    ]:
        r"""Return a callable for the apply hydrated deployment method over gRPC.

        Applies a hydrated deployment to a workload cluster.

        Returns:
            Callable[[~.ApplyHydratedDeploymentRequest],
                    ~.HydratedDeployment]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "apply_hydrated_deployment" not in self._stubs:
            self._stubs["apply_hydrated_deployment"] = self._logged_channel.unary_unary(
                "/google.cloud.telcoautomation.v1.TelcoAutomation/ApplyHydratedDeployment",
                request_serializer=telcoautomation.ApplyHydratedDeploymentRequest.serialize,
                response_deserializer=telcoautomation.HydratedDeployment.deserialize,
            )
        return self._stubs["apply_hydrated_deployment"]

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


__all__ = ("TelcoAutomationGrpcTransport",)
