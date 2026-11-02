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
from google.api_core import gapic_v1, grpc_helpers_async, operations_v1
from google.api_core import retry_async as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf.json_format import MessageToJson
from grpc.experimental import aio  # type: ignore

from google.cloud.gke_multicloud_v1.types import attached_resources, attached_service

from .base import DEFAULT_CLIENT_INFO, AttachedClustersTransport
from .grpc import AttachedClustersGrpcTransport

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
                    "serviceName": "google.cloud.gkemulticloud.v1.AttachedClusters",
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
                    "serviceName": "google.cloud.gkemulticloud.v1.AttachedClusters",
                    "rpcName": str(client_call_details.method),
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class AttachedClustersGrpcAsyncIOTransport(AttachedClustersTransport):
    """gRPC AsyncIO backend transport for AttachedClusters.

    The AttachedClusters API provides a single centrally managed
    service to register and manage Anthos attached clusters that run
    on customer's owned infrastructure.

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
        host: str = "gkemulticloud.googleapis.com",
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
        host: str = "gkemulticloud.googleapis.com",
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
                 The hostname to connect to (default: 'gkemulticloud.googleapis.com').
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
        self._operations_client: Optional[operations_v1.OperationsAsyncClient] = None

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
    def operations_client(self) -> operations_v1.OperationsAsyncClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Quick check: Only create a new client if we do not already have one.
        if self._operations_client is None:
            self._operations_client = operations_v1.OperationsAsyncClient(
                self._logged_channel
            )

        # Return the client from cache.
        return self._operations_client

    @property
    def create_attached_cluster(
        self,
    ) -> Callable[
        [attached_service.CreateAttachedClusterRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the create attached cluster method over gRPC.

        Creates a new
        [AttachedCluster][google.cloud.gkemulticloud.v1.AttachedCluster]
        resource on a given Google Cloud Platform project and region.

        If successful, the response contains a newly created
        [Operation][google.longrunning.Operation] resource that can be
        described to track the status of the operation.

        Returns:
            Callable[[~.CreateAttachedClusterRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_attached_cluster" not in self._stubs:
            self._stubs["create_attached_cluster"] = self._logged_channel.unary_unary(
                "/google.cloud.gkemulticloud.v1.AttachedClusters/CreateAttachedCluster",
                request_serializer=attached_service.CreateAttachedClusterRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_attached_cluster"]

    @property
    def update_attached_cluster(
        self,
    ) -> Callable[
        [attached_service.UpdateAttachedClusterRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the update attached cluster method over gRPC.

        Updates an
        [AttachedCluster][google.cloud.gkemulticloud.v1.AttachedCluster].

        Returns:
            Callable[[~.UpdateAttachedClusterRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_attached_cluster" not in self._stubs:
            self._stubs["update_attached_cluster"] = self._logged_channel.unary_unary(
                "/google.cloud.gkemulticloud.v1.AttachedClusters/UpdateAttachedCluster",
                request_serializer=attached_service.UpdateAttachedClusterRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_attached_cluster"]

    @property
    def import_attached_cluster(
        self,
    ) -> Callable[
        [attached_service.ImportAttachedClusterRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the import attached cluster method over gRPC.

        Imports creates a new
        [AttachedCluster][google.cloud.gkemulticloud.v1.AttachedCluster]
        resource by importing an existing Fleet Membership resource.

        Attached Clusters created before the introduction of the Anthos
        Multi-Cloud API can be imported through this method.

        If successful, the response contains a newly created
        [Operation][google.longrunning.Operation] resource that can be
        described to track the status of the operation.

        Returns:
            Callable[[~.ImportAttachedClusterRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "import_attached_cluster" not in self._stubs:
            self._stubs["import_attached_cluster"] = self._logged_channel.unary_unary(
                "/google.cloud.gkemulticloud.v1.AttachedClusters/ImportAttachedCluster",
                request_serializer=attached_service.ImportAttachedClusterRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["import_attached_cluster"]

    @property
    def get_attached_cluster(
        self,
    ) -> Callable[
        [attached_service.GetAttachedClusterRequest],
        Awaitable[attached_resources.AttachedCluster],
    ]:
        r"""Return a callable for the get attached cluster method over gRPC.

        Describes a specific
        [AttachedCluster][google.cloud.gkemulticloud.v1.AttachedCluster]
        resource.

        Returns:
            Callable[[~.GetAttachedClusterRequest],
                    Awaitable[~.AttachedCluster]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_attached_cluster" not in self._stubs:
            self._stubs["get_attached_cluster"] = self._logged_channel.unary_unary(
                "/google.cloud.gkemulticloud.v1.AttachedClusters/GetAttachedCluster",
                request_serializer=attached_service.GetAttachedClusterRequest.serialize,
                response_deserializer=attached_resources.AttachedCluster.deserialize,
            )
        return self._stubs["get_attached_cluster"]

    @property
    def list_attached_clusters(
        self,
    ) -> Callable[
        [attached_service.ListAttachedClustersRequest],
        Awaitable[attached_service.ListAttachedClustersResponse],
    ]:
        r"""Return a callable for the list attached clusters method over gRPC.

        Lists all
        [AttachedCluster][google.cloud.gkemulticloud.v1.AttachedCluster]
        resources on a given Google Cloud project and region.

        Returns:
            Callable[[~.ListAttachedClustersRequest],
                    Awaitable[~.ListAttachedClustersResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_attached_clusters" not in self._stubs:
            self._stubs["list_attached_clusters"] = self._logged_channel.unary_unary(
                "/google.cloud.gkemulticloud.v1.AttachedClusters/ListAttachedClusters",
                request_serializer=attached_service.ListAttachedClustersRequest.serialize,
                response_deserializer=attached_service.ListAttachedClustersResponse.deserialize,
            )
        return self._stubs["list_attached_clusters"]

    @property
    def delete_attached_cluster(
        self,
    ) -> Callable[
        [attached_service.DeleteAttachedClusterRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the delete attached cluster method over gRPC.

        Deletes a specific
        [AttachedCluster][google.cloud.gkemulticloud.v1.AttachedCluster]
        resource.

        If successful, the response contains a newly created
        [Operation][google.longrunning.Operation] resource that can be
        described to track the status of the operation.

        Returns:
            Callable[[~.DeleteAttachedClusterRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_attached_cluster" not in self._stubs:
            self._stubs["delete_attached_cluster"] = self._logged_channel.unary_unary(
                "/google.cloud.gkemulticloud.v1.AttachedClusters/DeleteAttachedCluster",
                request_serializer=attached_service.DeleteAttachedClusterRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_attached_cluster"]

    @property
    def get_attached_server_config(
        self,
    ) -> Callable[
        [attached_service.GetAttachedServerConfigRequest],
        Awaitable[attached_resources.AttachedServerConfig],
    ]:
        r"""Return a callable for the get attached server config method over gRPC.

        Returns information, such as supported Kubernetes
        versions, on a given Google Cloud location.

        Returns:
            Callable[[~.GetAttachedServerConfigRequest],
                    Awaitable[~.AttachedServerConfig]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_attached_server_config" not in self._stubs:
            self._stubs["get_attached_server_config"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.gkemulticloud.v1.AttachedClusters/GetAttachedServerConfig",
                    request_serializer=attached_service.GetAttachedServerConfigRequest.serialize,
                    response_deserializer=attached_resources.AttachedServerConfig.deserialize,
                )
            )
        return self._stubs["get_attached_server_config"]

    @property
    def generate_attached_cluster_install_manifest(
        self,
    ) -> Callable[
        [attached_service.GenerateAttachedClusterInstallManifestRequest],
        Awaitable[attached_service.GenerateAttachedClusterInstallManifestResponse],
    ]:
        r"""Return a callable for the generate attached cluster
        install manifest method over gRPC.

        Generates the install manifest to be installed on the
        target cluster.

        Returns:
            Callable[[~.GenerateAttachedClusterInstallManifestRequest],
                    Awaitable[~.GenerateAttachedClusterInstallManifestResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "generate_attached_cluster_install_manifest" not in self._stubs:
            self._stubs["generate_attached_cluster_install_manifest"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.gkemulticloud.v1.AttachedClusters/GenerateAttachedClusterInstallManifest",
                    request_serializer=attached_service.GenerateAttachedClusterInstallManifestRequest.serialize,
                    response_deserializer=attached_service.GenerateAttachedClusterInstallManifestResponse.deserialize,
                )
            )
        return self._stubs["generate_attached_cluster_install_manifest"]

    @property
    def generate_attached_cluster_agent_token(
        self,
    ) -> Callable[
        [attached_service.GenerateAttachedClusterAgentTokenRequest],
        Awaitable[attached_service.GenerateAttachedClusterAgentTokenResponse],
    ]:
        r"""Return a callable for the generate attached cluster
        agent token method over gRPC.

        Generates an access token for a cluster agent.

        Returns:
            Callable[[~.GenerateAttachedClusterAgentTokenRequest],
                    Awaitable[~.GenerateAttachedClusterAgentTokenResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "generate_attached_cluster_agent_token" not in self._stubs:
            self._stubs["generate_attached_cluster_agent_token"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.gkemulticloud.v1.AttachedClusters/GenerateAttachedClusterAgentToken",
                    request_serializer=attached_service.GenerateAttachedClusterAgentTokenRequest.serialize,
                    response_deserializer=attached_service.GenerateAttachedClusterAgentTokenResponse.deserialize,
                )
            )
        return self._stubs["generate_attached_cluster_agent_token"]

    def _prep_wrapped_messages(self, client_info):
        """Precompute the wrapped methods, overriding the base class method to use async wrappers."""
        self._wrapped_methods = {
            self.create_attached_cluster: self._wrap_method(
                self.create_attached_cluster,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_attached_cluster: self._wrap_method(
                self.update_attached_cluster,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.import_attached_cluster: self._wrap_method(
                self.import_attached_cluster,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_attached_cluster: self._wrap_method(
                self.get_attached_cluster,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_attached_clusters: self._wrap_method(
                self.list_attached_clusters,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_attached_cluster: self._wrap_method(
                self.delete_attached_cluster,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_attached_server_config: self._wrap_method(
                self.get_attached_server_config,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.generate_attached_cluster_install_manifest: self._wrap_method(
                self.generate_attached_cluster_install_manifest,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.generate_attached_cluster_agent_token: self._wrap_method(
                self.generate_attached_cluster_agent_token,
                default_retry=retries.AsyncRetry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
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


__all__ = ("AttachedClustersGrpcAsyncIOTransport",)
