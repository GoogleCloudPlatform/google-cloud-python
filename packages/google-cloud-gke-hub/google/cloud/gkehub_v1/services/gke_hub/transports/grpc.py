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
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf.json_format import MessageToJson

from google.cloud.gkehub_v1.types import feature, fleet, membership, service

from .base import DEFAULT_CLIENT_INFO, GkeHubTransport

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
                    "serviceName": "google.cloud.gkehub.v1.GkeHub",
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
                    "serviceName": "google.cloud.gkehub.v1.GkeHub",
                    "rpcName": client_call_details.method,
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class GkeHubGrpcTransport(GkeHubTransport):
    """gRPC backend transport for GkeHub.

    The GKE Hub service handles the registration of many Kubernetes
    clusters to Google Cloud, and the management of multi-cluster
    features over those clusters.

    The GKE Hub service operates on the following resources:

    - [Membership][google.cloud.gkehub.v1.Membership]
    - [Feature][google.cloud.gkehub.v1.Feature]

    GKE Hub is currently available in the global region and all regions
    in https://cloud.google.com/compute/docs/regions-zones. Feature is
    only available in global region while membership is global region
    and all the regions.

    **Membership management may be non-trivial:** it is recommended to
    use one of the Google-provided client libraries or tools where
    possible when working with Membership resources.

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
        host: str = "gkehub.googleapis.com",
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
                 The hostname to connect to (default: 'gkehub.googleapis.com').
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
        host: str = "gkehub.googleapis.com",
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
    def list_memberships(
        self,
    ) -> Callable[[service.ListMembershipsRequest], service.ListMembershipsResponse]:
        r"""Return a callable for the list memberships method over gRPC.

        Lists Memberships in a given project and location.

        Returns:
            Callable[[~.ListMembershipsRequest],
                    ~.ListMembershipsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_memberships" not in self._stubs:
            self._stubs["list_memberships"] = self._logged_channel.unary_unary(
                "/google.cloud.gkehub.v1.GkeHub/ListMemberships",
                request_serializer=service.ListMembershipsRequest.serialize,
                response_deserializer=service.ListMembershipsResponse.deserialize,
            )
        return self._stubs["list_memberships"]

    @property
    def list_bound_memberships(
        self,
    ) -> Callable[
        [service.ListBoundMembershipsRequest], service.ListBoundMembershipsResponse
    ]:
        r"""Return a callable for the list bound memberships method over gRPC.

        Lists Memberships bound to a Scope. The response
        includes relevant Memberships from all regions.

        Returns:
            Callable[[~.ListBoundMembershipsRequest],
                    ~.ListBoundMembershipsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_bound_memberships" not in self._stubs:
            self._stubs["list_bound_memberships"] = self._logged_channel.unary_unary(
                "/google.cloud.gkehub.v1.GkeHub/ListBoundMemberships",
                request_serializer=service.ListBoundMembershipsRequest.serialize,
                response_deserializer=service.ListBoundMembershipsResponse.deserialize,
            )
        return self._stubs["list_bound_memberships"]

    @property
    def list_features(
        self,
    ) -> Callable[[service.ListFeaturesRequest], service.ListFeaturesResponse]:
        r"""Return a callable for the list features method over gRPC.

        Lists Features in a given project and location.

        Returns:
            Callable[[~.ListFeaturesRequest],
                    ~.ListFeaturesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_features" not in self._stubs:
            self._stubs["list_features"] = self._logged_channel.unary_unary(
                "/google.cloud.gkehub.v1.GkeHub/ListFeatures",
                request_serializer=service.ListFeaturesRequest.serialize,
                response_deserializer=service.ListFeaturesResponse.deserialize,
            )
        return self._stubs["list_features"]

    @property
    def get_membership(
        self,
    ) -> Callable[[service.GetMembershipRequest], membership.Membership]:
        r"""Return a callable for the get membership method over gRPC.

        Gets the details of a Membership.

        Returns:
            Callable[[~.GetMembershipRequest],
                    ~.Membership]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_membership" not in self._stubs:
            self._stubs["get_membership"] = self._logged_channel.unary_unary(
                "/google.cloud.gkehub.v1.GkeHub/GetMembership",
                request_serializer=service.GetMembershipRequest.serialize,
                response_deserializer=membership.Membership.deserialize,
            )
        return self._stubs["get_membership"]

    @property
    def get_feature(self) -> Callable[[service.GetFeatureRequest], feature.Feature]:
        r"""Return a callable for the get feature method over gRPC.

        Gets details of a single Feature.

        Returns:
            Callable[[~.GetFeatureRequest],
                    ~.Feature]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_feature" not in self._stubs:
            self._stubs["get_feature"] = self._logged_channel.unary_unary(
                "/google.cloud.gkehub.v1.GkeHub/GetFeature",
                request_serializer=service.GetFeatureRequest.serialize,
                response_deserializer=feature.Feature.deserialize,
            )
        return self._stubs["get_feature"]

    @property
    def create_membership(
        self,
    ) -> Callable[[service.CreateMembershipRequest], operations_pb2.Operation]:
        r"""Return a callable for the create membership method over gRPC.

        Creates a new Membership.

        **This is currently only supported for GKE clusters on Google
        Cloud**. To register other clusters, follow the instructions at
        https://cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster.

        Returns:
            Callable[[~.CreateMembershipRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_membership" not in self._stubs:
            self._stubs["create_membership"] = self._logged_channel.unary_unary(
                "/google.cloud.gkehub.v1.GkeHub/CreateMembership",
                request_serializer=service.CreateMembershipRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_membership"]

    @property
    def create_feature(
        self,
    ) -> Callable[[service.CreateFeatureRequest], operations_pb2.Operation]:
        r"""Return a callable for the create feature method over gRPC.

        Adds a new Feature.

        Returns:
            Callable[[~.CreateFeatureRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_feature" not in self._stubs:
            self._stubs["create_feature"] = self._logged_channel.unary_unary(
                "/google.cloud.gkehub.v1.GkeHub/CreateFeature",
                request_serializer=service.CreateFeatureRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_feature"]

    @property
    def delete_membership(
        self,
    ) -> Callable[[service.DeleteMembershipRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete membership method over gRPC.

        Removes a Membership.

        **This is currently only supported for GKE clusters on Google
        Cloud**. To unregister other clusters, follow the instructions
        at
        https://cloud.google.com/anthos/multicluster-management/connect/unregistering-a-cluster.

        Returns:
            Callable[[~.DeleteMembershipRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_membership" not in self._stubs:
            self._stubs["delete_membership"] = self._logged_channel.unary_unary(
                "/google.cloud.gkehub.v1.GkeHub/DeleteMembership",
                request_serializer=service.DeleteMembershipRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_membership"]

    @property
    def delete_feature(
        self,
    ) -> Callable[[service.DeleteFeatureRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete feature method over gRPC.

        Removes a Feature.

        Returns:
            Callable[[~.DeleteFeatureRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_feature" not in self._stubs:
            self._stubs["delete_feature"] = self._logged_channel.unary_unary(
                "/google.cloud.gkehub.v1.GkeHub/DeleteFeature",
                request_serializer=service.DeleteFeatureRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_feature"]

    @property
    def update_membership(
        self,
    ) -> Callable[[service.UpdateMembershipRequest], operations_pb2.Operation]:
        r"""Return a callable for the update membership method over gRPC.

        Updates an existing Membership.

        Returns:
            Callable[[~.UpdateMembershipRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_membership" not in self._stubs:
            self._stubs["update_membership"] = self._logged_channel.unary_unary(
                "/google.cloud.gkehub.v1.GkeHub/UpdateMembership",
                request_serializer=service.UpdateMembershipRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_membership"]

    @property
    def update_feature(
        self,
    ) -> Callable[[service.UpdateFeatureRequest], operations_pb2.Operation]:
        r"""Return a callable for the update feature method over gRPC.

        Updates an existing Feature.

        Returns:
            Callable[[~.UpdateFeatureRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_feature" not in self._stubs:
            self._stubs["update_feature"] = self._logged_channel.unary_unary(
                "/google.cloud.gkehub.v1.GkeHub/UpdateFeature",
                request_serializer=service.UpdateFeatureRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_feature"]

    @property
    def generate_connect_manifest(
        self,
    ) -> Callable[
        [service.GenerateConnectManifestRequest],
        service.GenerateConnectManifestResponse,
    ]:
        r"""Return a callable for the generate connect manifest method over gRPC.

        Generates the manifest for deployment of the GKE connect agent.

        **This method is used internally by Google-provided libraries.**
        Most clients should not need to call this method directly.

        Returns:
            Callable[[~.GenerateConnectManifestRequest],
                    ~.GenerateConnectManifestResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "generate_connect_manifest" not in self._stubs:
            self._stubs["generate_connect_manifest"] = self._logged_channel.unary_unary(
                "/google.cloud.gkehub.v1.GkeHub/GenerateConnectManifest",
                request_serializer=service.GenerateConnectManifestRequest.serialize,
                response_deserializer=service.GenerateConnectManifestResponse.deserialize,
            )
        return self._stubs["generate_connect_manifest"]

    @property
    def create_fleet(
        self,
    ) -> Callable[[service.CreateFleetRequest], operations_pb2.Operation]:
        r"""Return a callable for the create fleet method over gRPC.

        Creates a fleet.

        Returns:
            Callable[[~.CreateFleetRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_fleet" not in self._stubs:
            self._stubs["create_fleet"] = self._logged_channel.unary_unary(
                "/google.cloud.gkehub.v1.GkeHub/CreateFleet",
                request_serializer=service.CreateFleetRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_fleet"]

    @property
    def get_fleet(self) -> Callable[[service.GetFleetRequest], fleet.Fleet]:
        r"""Return a callable for the get fleet method over gRPC.

        Returns the details of a fleet.

        Returns:
            Callable[[~.GetFleetRequest],
                    ~.Fleet]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_fleet" not in self._stubs:
            self._stubs["get_fleet"] = self._logged_channel.unary_unary(
                "/google.cloud.gkehub.v1.GkeHub/GetFleet",
                request_serializer=service.GetFleetRequest.serialize,
                response_deserializer=fleet.Fleet.deserialize,
            )
        return self._stubs["get_fleet"]

    @property
    def update_fleet(
        self,
    ) -> Callable[[service.UpdateFleetRequest], operations_pb2.Operation]:
        r"""Return a callable for the update fleet method over gRPC.

        Updates a fleet.

        Returns:
            Callable[[~.UpdateFleetRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_fleet" not in self._stubs:
            self._stubs["update_fleet"] = self._logged_channel.unary_unary(
                "/google.cloud.gkehub.v1.GkeHub/UpdateFleet",
                request_serializer=service.UpdateFleetRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_fleet"]

    @property
    def delete_fleet(
        self,
    ) -> Callable[[service.DeleteFleetRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete fleet method over gRPC.

        Removes a Fleet. There must be no memberships
        remaining in the Fleet.

        Returns:
            Callable[[~.DeleteFleetRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_fleet" not in self._stubs:
            self._stubs["delete_fleet"] = self._logged_channel.unary_unary(
                "/google.cloud.gkehub.v1.GkeHub/DeleteFleet",
                request_serializer=service.DeleteFleetRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_fleet"]

    @property
    def list_fleets(
        self,
    ) -> Callable[[service.ListFleetsRequest], service.ListFleetsResponse]:
        r"""Return a callable for the list fleets method over gRPC.

        Returns all fleets within an organization or a
        project that the caller has access to.

        Returns:
            Callable[[~.ListFleetsRequest],
                    ~.ListFleetsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_fleets" not in self._stubs:
            self._stubs["list_fleets"] = self._logged_channel.unary_unary(
                "/google.cloud.gkehub.v1.GkeHub/ListFleets",
                request_serializer=service.ListFleetsRequest.serialize,
                response_deserializer=service.ListFleetsResponse.deserialize,
            )
        return self._stubs["list_fleets"]

    @property
    def get_scope_namespace(
        self,
    ) -> Callable[[service.GetScopeNamespaceRequest], fleet.Namespace]:
        r"""Return a callable for the get scope namespace method over gRPC.

        Returns the details of a fleet namespace.

        Returns:
            Callable[[~.GetScopeNamespaceRequest],
                    ~.Namespace]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_scope_namespace" not in self._stubs:
            self._stubs["get_scope_namespace"] = self._logged_channel.unary_unary(
                "/google.cloud.gkehub.v1.GkeHub/GetScopeNamespace",
                request_serializer=service.GetScopeNamespaceRequest.serialize,
                response_deserializer=fleet.Namespace.deserialize,
            )
        return self._stubs["get_scope_namespace"]

    @property
    def create_scope_namespace(
        self,
    ) -> Callable[[service.CreateScopeNamespaceRequest], operations_pb2.Operation]:
        r"""Return a callable for the create scope namespace method over gRPC.

        Creates a fleet namespace.

        Returns:
            Callable[[~.CreateScopeNamespaceRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_scope_namespace" not in self._stubs:
            self._stubs["create_scope_namespace"] = self._logged_channel.unary_unary(
                "/google.cloud.gkehub.v1.GkeHub/CreateScopeNamespace",
                request_serializer=service.CreateScopeNamespaceRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_scope_namespace"]

    @property
    def update_scope_namespace(
        self,
    ) -> Callable[[service.UpdateScopeNamespaceRequest], operations_pb2.Operation]:
        r"""Return a callable for the update scope namespace method over gRPC.

        Updates a fleet namespace.

        Returns:
            Callable[[~.UpdateScopeNamespaceRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_scope_namespace" not in self._stubs:
            self._stubs["update_scope_namespace"] = self._logged_channel.unary_unary(
                "/google.cloud.gkehub.v1.GkeHub/UpdateScopeNamespace",
                request_serializer=service.UpdateScopeNamespaceRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_scope_namespace"]

    @property
    def delete_scope_namespace(
        self,
    ) -> Callable[[service.DeleteScopeNamespaceRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete scope namespace method over gRPC.

        Deletes a fleet namespace.

        Returns:
            Callable[[~.DeleteScopeNamespaceRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_scope_namespace" not in self._stubs:
            self._stubs["delete_scope_namespace"] = self._logged_channel.unary_unary(
                "/google.cloud.gkehub.v1.GkeHub/DeleteScopeNamespace",
                request_serializer=service.DeleteScopeNamespaceRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_scope_namespace"]

    @property
    def list_scope_namespaces(
        self,
    ) -> Callable[
        [service.ListScopeNamespacesRequest], service.ListScopeNamespacesResponse
    ]:
        r"""Return a callable for the list scope namespaces method over gRPC.

        Lists fleet namespaces.

        Returns:
            Callable[[~.ListScopeNamespacesRequest],
                    ~.ListScopeNamespacesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_scope_namespaces" not in self._stubs:
            self._stubs["list_scope_namespaces"] = self._logged_channel.unary_unary(
                "/google.cloud.gkehub.v1.GkeHub/ListScopeNamespaces",
                request_serializer=service.ListScopeNamespacesRequest.serialize,
                response_deserializer=service.ListScopeNamespacesResponse.deserialize,
            )
        return self._stubs["list_scope_namespaces"]

    @property
    def get_scope_rbac_role_binding(
        self,
    ) -> Callable[[service.GetScopeRBACRoleBindingRequest], fleet.RBACRoleBinding]:
        r"""Return a callable for the get scope rbac role binding method over gRPC.

        Returns the details of a Scope RBACRoleBinding.

        Returns:
            Callable[[~.GetScopeRBACRoleBindingRequest],
                    ~.RBACRoleBinding]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_scope_rbac_role_binding" not in self._stubs:
            self._stubs["get_scope_rbac_role_binding"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.gkehub.v1.GkeHub/GetScopeRBACRoleBinding",
                    request_serializer=service.GetScopeRBACRoleBindingRequest.serialize,
                    response_deserializer=fleet.RBACRoleBinding.deserialize,
                )
            )
        return self._stubs["get_scope_rbac_role_binding"]

    @property
    def create_scope_rbac_role_binding(
        self,
    ) -> Callable[
        [service.CreateScopeRBACRoleBindingRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the create scope rbac role binding method over gRPC.

        Creates a Scope RBACRoleBinding.

        Returns:
            Callable[[~.CreateScopeRBACRoleBindingRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_scope_rbac_role_binding" not in self._stubs:
            self._stubs["create_scope_rbac_role_binding"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.gkehub.v1.GkeHub/CreateScopeRBACRoleBinding",
                    request_serializer=service.CreateScopeRBACRoleBindingRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["create_scope_rbac_role_binding"]

    @property
    def update_scope_rbac_role_binding(
        self,
    ) -> Callable[
        [service.UpdateScopeRBACRoleBindingRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the update scope rbac role binding method over gRPC.

        Updates a Scope RBACRoleBinding.

        Returns:
            Callable[[~.UpdateScopeRBACRoleBindingRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_scope_rbac_role_binding" not in self._stubs:
            self._stubs["update_scope_rbac_role_binding"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.gkehub.v1.GkeHub/UpdateScopeRBACRoleBinding",
                    request_serializer=service.UpdateScopeRBACRoleBindingRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["update_scope_rbac_role_binding"]

    @property
    def delete_scope_rbac_role_binding(
        self,
    ) -> Callable[
        [service.DeleteScopeRBACRoleBindingRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the delete scope rbac role binding method over gRPC.

        Deletes a Scope RBACRoleBinding.

        Returns:
            Callable[[~.DeleteScopeRBACRoleBindingRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_scope_rbac_role_binding" not in self._stubs:
            self._stubs["delete_scope_rbac_role_binding"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.gkehub.v1.GkeHub/DeleteScopeRBACRoleBinding",
                    request_serializer=service.DeleteScopeRBACRoleBindingRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["delete_scope_rbac_role_binding"]

    @property
    def list_scope_rbac_role_bindings(
        self,
    ) -> Callable[
        [service.ListScopeRBACRoleBindingsRequest],
        service.ListScopeRBACRoleBindingsResponse,
    ]:
        r"""Return a callable for the list scope rbac role bindings method over gRPC.

        Lists all Scope RBACRoleBindings.

        Returns:
            Callable[[~.ListScopeRBACRoleBindingsRequest],
                    ~.ListScopeRBACRoleBindingsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_scope_rbac_role_bindings" not in self._stubs:
            self._stubs["list_scope_rbac_role_bindings"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.gkehub.v1.GkeHub/ListScopeRBACRoleBindings",
                    request_serializer=service.ListScopeRBACRoleBindingsRequest.serialize,
                    response_deserializer=service.ListScopeRBACRoleBindingsResponse.deserialize,
                )
            )
        return self._stubs["list_scope_rbac_role_bindings"]

    @property
    def get_scope(self) -> Callable[[service.GetScopeRequest], fleet.Scope]:
        r"""Return a callable for the get scope method over gRPC.

        Returns the details of a Scope.

        Returns:
            Callable[[~.GetScopeRequest],
                    ~.Scope]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_scope" not in self._stubs:
            self._stubs["get_scope"] = self._logged_channel.unary_unary(
                "/google.cloud.gkehub.v1.GkeHub/GetScope",
                request_serializer=service.GetScopeRequest.serialize,
                response_deserializer=fleet.Scope.deserialize,
            )
        return self._stubs["get_scope"]

    @property
    def create_scope(
        self,
    ) -> Callable[[service.CreateScopeRequest], operations_pb2.Operation]:
        r"""Return a callable for the create scope method over gRPC.

        Creates a Scope.

        Returns:
            Callable[[~.CreateScopeRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_scope" not in self._stubs:
            self._stubs["create_scope"] = self._logged_channel.unary_unary(
                "/google.cloud.gkehub.v1.GkeHub/CreateScope",
                request_serializer=service.CreateScopeRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_scope"]

    @property
    def update_scope(
        self,
    ) -> Callable[[service.UpdateScopeRequest], operations_pb2.Operation]:
        r"""Return a callable for the update scope method over gRPC.

        Updates a scopes.

        Returns:
            Callable[[~.UpdateScopeRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_scope" not in self._stubs:
            self._stubs["update_scope"] = self._logged_channel.unary_unary(
                "/google.cloud.gkehub.v1.GkeHub/UpdateScope",
                request_serializer=service.UpdateScopeRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_scope"]

    @property
    def delete_scope(
        self,
    ) -> Callable[[service.DeleteScopeRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete scope method over gRPC.

        Deletes a Scope.

        Returns:
            Callable[[~.DeleteScopeRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_scope" not in self._stubs:
            self._stubs["delete_scope"] = self._logged_channel.unary_unary(
                "/google.cloud.gkehub.v1.GkeHub/DeleteScope",
                request_serializer=service.DeleteScopeRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_scope"]

    @property
    def list_scopes(
        self,
    ) -> Callable[[service.ListScopesRequest], service.ListScopesResponse]:
        r"""Return a callable for the list scopes method over gRPC.

        Lists Scopes.

        Returns:
            Callable[[~.ListScopesRequest],
                    ~.ListScopesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_scopes" not in self._stubs:
            self._stubs["list_scopes"] = self._logged_channel.unary_unary(
                "/google.cloud.gkehub.v1.GkeHub/ListScopes",
                request_serializer=service.ListScopesRequest.serialize,
                response_deserializer=service.ListScopesResponse.deserialize,
            )
        return self._stubs["list_scopes"]

    @property
    def list_permitted_scopes(
        self,
    ) -> Callable[
        [service.ListPermittedScopesRequest], service.ListPermittedScopesResponse
    ]:
        r"""Return a callable for the list permitted scopes method over gRPC.

        Lists permitted Scopes.

        Returns:
            Callable[[~.ListPermittedScopesRequest],
                    ~.ListPermittedScopesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_permitted_scopes" not in self._stubs:
            self._stubs["list_permitted_scopes"] = self._logged_channel.unary_unary(
                "/google.cloud.gkehub.v1.GkeHub/ListPermittedScopes",
                request_serializer=service.ListPermittedScopesRequest.serialize,
                response_deserializer=service.ListPermittedScopesResponse.deserialize,
            )
        return self._stubs["list_permitted_scopes"]

    @property
    def get_membership_binding(
        self,
    ) -> Callable[[service.GetMembershipBindingRequest], fleet.MembershipBinding]:
        r"""Return a callable for the get membership binding method over gRPC.

        Returns the details of a MembershipBinding.

        Returns:
            Callable[[~.GetMembershipBindingRequest],
                    ~.MembershipBinding]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_membership_binding" not in self._stubs:
            self._stubs["get_membership_binding"] = self._logged_channel.unary_unary(
                "/google.cloud.gkehub.v1.GkeHub/GetMembershipBinding",
                request_serializer=service.GetMembershipBindingRequest.serialize,
                response_deserializer=fleet.MembershipBinding.deserialize,
            )
        return self._stubs["get_membership_binding"]

    @property
    def create_membership_binding(
        self,
    ) -> Callable[[service.CreateMembershipBindingRequest], operations_pb2.Operation]:
        r"""Return a callable for the create membership binding method over gRPC.

        Creates a MembershipBinding.

        Returns:
            Callable[[~.CreateMembershipBindingRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_membership_binding" not in self._stubs:
            self._stubs["create_membership_binding"] = self._logged_channel.unary_unary(
                "/google.cloud.gkehub.v1.GkeHub/CreateMembershipBinding",
                request_serializer=service.CreateMembershipBindingRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_membership_binding"]

    @property
    def update_membership_binding(
        self,
    ) -> Callable[[service.UpdateMembershipBindingRequest], operations_pb2.Operation]:
        r"""Return a callable for the update membership binding method over gRPC.

        Updates a MembershipBinding.

        Returns:
            Callable[[~.UpdateMembershipBindingRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_membership_binding" not in self._stubs:
            self._stubs["update_membership_binding"] = self._logged_channel.unary_unary(
                "/google.cloud.gkehub.v1.GkeHub/UpdateMembershipBinding",
                request_serializer=service.UpdateMembershipBindingRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_membership_binding"]

    @property
    def delete_membership_binding(
        self,
    ) -> Callable[[service.DeleteMembershipBindingRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete membership binding method over gRPC.

        Deletes a MembershipBinding.

        Returns:
            Callable[[~.DeleteMembershipBindingRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_membership_binding" not in self._stubs:
            self._stubs["delete_membership_binding"] = self._logged_channel.unary_unary(
                "/google.cloud.gkehub.v1.GkeHub/DeleteMembershipBinding",
                request_serializer=service.DeleteMembershipBindingRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_membership_binding"]

    @property
    def list_membership_bindings(
        self,
    ) -> Callable[
        [service.ListMembershipBindingsRequest], service.ListMembershipBindingsResponse
    ]:
        r"""Return a callable for the list membership bindings method over gRPC.

        Lists MembershipBindings.

        Returns:
            Callable[[~.ListMembershipBindingsRequest],
                    ~.ListMembershipBindingsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_membership_bindings" not in self._stubs:
            self._stubs["list_membership_bindings"] = self._logged_channel.unary_unary(
                "/google.cloud.gkehub.v1.GkeHub/ListMembershipBindings",
                request_serializer=service.ListMembershipBindingsRequest.serialize,
                response_deserializer=service.ListMembershipBindingsResponse.deserialize,
            )
        return self._stubs["list_membership_bindings"]

    @property
    def get_membership_rbac_role_binding(
        self,
    ) -> Callable[[service.GetMembershipRBACRoleBindingRequest], fleet.RBACRoleBinding]:
        r"""Return a callable for the get membership rbac role
        binding method over gRPC.

        Returns the details of a Membership RBACRoleBinding.

        Returns:
            Callable[[~.GetMembershipRBACRoleBindingRequest],
                    ~.RBACRoleBinding]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_membership_rbac_role_binding" not in self._stubs:
            self._stubs["get_membership_rbac_role_binding"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.gkehub.v1.GkeHub/GetMembershipRBACRoleBinding",
                    request_serializer=service.GetMembershipRBACRoleBindingRequest.serialize,
                    response_deserializer=fleet.RBACRoleBinding.deserialize,
                )
            )
        return self._stubs["get_membership_rbac_role_binding"]

    @property
    def create_membership_rbac_role_binding(
        self,
    ) -> Callable[
        [service.CreateMembershipRBACRoleBindingRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the create membership rbac role
        binding method over gRPC.

        Creates a Membership RBACRoleBinding.

        Returns:
            Callable[[~.CreateMembershipRBACRoleBindingRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_membership_rbac_role_binding" not in self._stubs:
            self._stubs["create_membership_rbac_role_binding"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.gkehub.v1.GkeHub/CreateMembershipRBACRoleBinding",
                    request_serializer=service.CreateMembershipRBACRoleBindingRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["create_membership_rbac_role_binding"]

    @property
    def update_membership_rbac_role_binding(
        self,
    ) -> Callable[
        [service.UpdateMembershipRBACRoleBindingRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the update membership rbac role
        binding method over gRPC.

        Updates a Membership RBACRoleBinding.

        Returns:
            Callable[[~.UpdateMembershipRBACRoleBindingRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_membership_rbac_role_binding" not in self._stubs:
            self._stubs["update_membership_rbac_role_binding"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.gkehub.v1.GkeHub/UpdateMembershipRBACRoleBinding",
                    request_serializer=service.UpdateMembershipRBACRoleBindingRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["update_membership_rbac_role_binding"]

    @property
    def delete_membership_rbac_role_binding(
        self,
    ) -> Callable[
        [service.DeleteMembershipRBACRoleBindingRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the delete membership rbac role
        binding method over gRPC.

        Deletes a Membership RBACRoleBinding.

        Returns:
            Callable[[~.DeleteMembershipRBACRoleBindingRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_membership_rbac_role_binding" not in self._stubs:
            self._stubs["delete_membership_rbac_role_binding"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.gkehub.v1.GkeHub/DeleteMembershipRBACRoleBinding",
                    request_serializer=service.DeleteMembershipRBACRoleBindingRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["delete_membership_rbac_role_binding"]

    @property
    def list_membership_rbac_role_bindings(
        self,
    ) -> Callable[
        [service.ListMembershipRBACRoleBindingsRequest],
        service.ListMembershipRBACRoleBindingsResponse,
    ]:
        r"""Return a callable for the list membership rbac role
        bindings method over gRPC.

        Lists all Membership RBACRoleBindings.

        Returns:
            Callable[[~.ListMembershipRBACRoleBindingsRequest],
                    ~.ListMembershipRBACRoleBindingsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_membership_rbac_role_bindings" not in self._stubs:
            self._stubs["list_membership_rbac_role_bindings"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.gkehub.v1.GkeHub/ListMembershipRBACRoleBindings",
                    request_serializer=service.ListMembershipRBACRoleBindingsRequest.serialize,
                    response_deserializer=service.ListMembershipRBACRoleBindingsResponse.deserialize,
                )
            )
        return self._stubs["list_membership_rbac_role_bindings"]

    @property
    def generate_membership_rbac_role_binding_yaml(
        self,
    ) -> Callable[
        [service.GenerateMembershipRBACRoleBindingYAMLRequest],
        service.GenerateMembershipRBACRoleBindingYAMLResponse,
    ]:
        r"""Return a callable for the generate membership rbac role
        binding yaml method over gRPC.

        Generates a YAML of the  RBAC policies for the
        specified RoleBinding and its associated impersonation
        resources.

        Returns:
            Callable[[~.GenerateMembershipRBACRoleBindingYAMLRequest],
                    ~.GenerateMembershipRBACRoleBindingYAMLResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "generate_membership_rbac_role_binding_yaml" not in self._stubs:
            self._stubs["generate_membership_rbac_role_binding_yaml"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.gkehub.v1.GkeHub/GenerateMembershipRBACRoleBindingYAML",
                    request_serializer=service.GenerateMembershipRBACRoleBindingYAMLRequest.serialize,
                    response_deserializer=service.GenerateMembershipRBACRoleBindingYAMLResponse.deserialize,
                )
            )
        return self._stubs["generate_membership_rbac_role_binding_yaml"]

    def close(self):
        self._logged_channel.close()

    @property
    def kind(self) -> str:
        return "grpc"


__all__ = ("GkeHubGrpcTransport",)
