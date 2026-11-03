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
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf.json_format import MessageToJson
from grpc.experimental import aio  # type: ignore

from google.cloud.redis_cluster_v1beta1.types import cloud_redis_cluster

from .base import DEFAULT_CLIENT_INFO, CloudRedisClusterTransport
from .grpc import CloudRedisClusterGrpcTransport

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
                    "serviceName": "google.cloud.redis.cluster.v1beta1.CloudRedisCluster",
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
                    "serviceName": "google.cloud.redis.cluster.v1beta1.CloudRedisCluster",
                    "rpcName": str(client_call_details.method),
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class CloudRedisClusterGrpcAsyncIOTransport(CloudRedisClusterTransport):
    """gRPC AsyncIO backend transport for CloudRedisCluster.

    Configures and manages Cloud Memorystore for Redis clusters

    Google Cloud Memorystore for Redis Cluster

    The ``redis.googleapis.com`` service implements the Google Cloud
    Memorystore for Redis API and defines the following resource model
    for managing Redis clusters:

    - The service works with a collection of cloud projects, named:
      ``/projects/*``
    - Each project has a collection of available locations, named:
      ``/locations/*``
    - Each location has a collection of Redis clusters, named:
      ``/clusters/*``
    - As such, Redis clusters are resources of the form:
      ``/projects/{project_id}/locations/{location_id}/clusters/{instance_id}``

    Note that location_id must be a GCP ``region``; for example:

    - ``projects/redpepper-1290/locations/us-central1/clusters/my-redis``

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
        host: str = "redis.googleapis.com",
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
        host: str = "redis.googleapis.com",
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
                 The hostname to connect to (default: 'redis.googleapis.com').
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
    def list_clusters(
        self,
    ) -> Callable[
        [cloud_redis_cluster.ListClustersRequest],
        Awaitable[cloud_redis_cluster.ListClustersResponse],
    ]:
        r"""Return a callable for the list clusters method over gRPC.

        Lists all Redis clusters owned by a project in either the
        specified location (region) or all locations.

        The location should have the following format:

        - ``projects/{project_id}/locations/{location_id}``

        If ``location_id`` is specified as ``-`` (wildcard), then all
        regions available to the project are queried, and the results
        are aggregated.

        Returns:
            Callable[[~.ListClustersRequest],
                    Awaitable[~.ListClustersResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_clusters" not in self._stubs:
            self._stubs["list_clusters"] = self._logged_channel.unary_unary(
                "/google.cloud.redis.cluster.v1beta1.CloudRedisCluster/ListClusters",
                request_serializer=cloud_redis_cluster.ListClustersRequest.serialize,
                response_deserializer=cloud_redis_cluster.ListClustersResponse.deserialize,
            )
        return self._stubs["list_clusters"]

    @property
    def list_acl_policies(
        self,
    ) -> Callable[
        [cloud_redis_cluster.ListAclPoliciesRequest],
        Awaitable[cloud_redis_cluster.ListAclPoliciesResponse],
    ]:
        r"""Return a callable for the list acl policies method over gRPC.

        Lists all ACL policies owned by a project in either the
        specified location (region) or all locations.

        The location should have the following format:

        - ``projects/{project_id}/locations/{location_id}``

        If ``location_id`` is specified as ``-`` (wildcard), then all
        regions available to the project are queried, and the results
        are aggregated.

        Returns:
            Callable[[~.ListAclPoliciesRequest],
                    Awaitable[~.ListAclPoliciesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_acl_policies" not in self._stubs:
            self._stubs["list_acl_policies"] = self._logged_channel.unary_unary(
                "/google.cloud.redis.cluster.v1beta1.CloudRedisCluster/ListAclPolicies",
                request_serializer=cloud_redis_cluster.ListAclPoliciesRequest.serialize,
                response_deserializer=cloud_redis_cluster.ListAclPoliciesResponse.deserialize,
            )
        return self._stubs["list_acl_policies"]

    @property
    def get_cluster(
        self,
    ) -> Callable[
        [cloud_redis_cluster.GetClusterRequest], Awaitable[cloud_redis_cluster.Cluster]
    ]:
        r"""Return a callable for the get cluster method over gRPC.

        Gets the details of a specific Redis cluster.

        Returns:
            Callable[[~.GetClusterRequest],
                    Awaitable[~.Cluster]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_cluster" not in self._stubs:
            self._stubs["get_cluster"] = self._logged_channel.unary_unary(
                "/google.cloud.redis.cluster.v1beta1.CloudRedisCluster/GetCluster",
                request_serializer=cloud_redis_cluster.GetClusterRequest.serialize,
                response_deserializer=cloud_redis_cluster.Cluster.deserialize,
            )
        return self._stubs["get_cluster"]

    @property
    def get_acl_policy(
        self,
    ) -> Callable[
        [cloud_redis_cluster.GetAclPolicyRequest],
        Awaitable[cloud_redis_cluster.AclPolicy],
    ]:
        r"""Return a callable for the get acl policy method over gRPC.

        Gets the details of a specific Redis Cluster ACL
        policy.

        Returns:
            Callable[[~.GetAclPolicyRequest],
                    Awaitable[~.AclPolicy]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_acl_policy" not in self._stubs:
            self._stubs["get_acl_policy"] = self._logged_channel.unary_unary(
                "/google.cloud.redis.cluster.v1beta1.CloudRedisCluster/GetAclPolicy",
                request_serializer=cloud_redis_cluster.GetAclPolicyRequest.serialize,
                response_deserializer=cloud_redis_cluster.AclPolicy.deserialize,
            )
        return self._stubs["get_acl_policy"]

    @property
    def update_cluster(
        self,
    ) -> Callable[
        [cloud_redis_cluster.UpdateClusterRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update cluster method over gRPC.

        Updates the metadata and configuration of a specific
        Redis cluster.
        Completed longrunning.Operation will contain the new
        cluster object in the response field. The returned
        operation is automatically deleted after a few hours, so
        there is no need to call DeleteOperation.

        Returns:
            Callable[[~.UpdateClusterRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_cluster" not in self._stubs:
            self._stubs["update_cluster"] = self._logged_channel.unary_unary(
                "/google.cloud.redis.cluster.v1beta1.CloudRedisCluster/UpdateCluster",
                request_serializer=cloud_redis_cluster.UpdateClusterRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_cluster"]

    @property
    def update_acl_policy(
        self,
    ) -> Callable[
        [cloud_redis_cluster.UpdateAclPolicyRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the update acl policy method over gRPC.

        Updates the ACL policy.

        The operation applies the updated ACL policy to all of
        the linked clusters. If Memorystore can apply the policy
        to all clusters, then the operation returns a SUCCESS
        status. If Memorystore can't apply the policy to all
        clusters, then to ensure eventual consistency,
        Memorystore uses reconciliation to apply the policy to
        the failed clusters.

        Completed longrunning.Operation will contain the new ACL
        policy object in the response field.

        Returns:
            Callable[[~.UpdateAclPolicyRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_acl_policy" not in self._stubs:
            self._stubs["update_acl_policy"] = self._logged_channel.unary_unary(
                "/google.cloud.redis.cluster.v1beta1.CloudRedisCluster/UpdateAclPolicy",
                request_serializer=cloud_redis_cluster.UpdateAclPolicyRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_acl_policy"]

    @property
    def delete_cluster(
        self,
    ) -> Callable[
        [cloud_redis_cluster.DeleteClusterRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the delete cluster method over gRPC.

        Deletes a specific Redis cluster. Cluster stops
        serving and data is deleted.

        Returns:
            Callable[[~.DeleteClusterRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_cluster" not in self._stubs:
            self._stubs["delete_cluster"] = self._logged_channel.unary_unary(
                "/google.cloud.redis.cluster.v1beta1.CloudRedisCluster/DeleteCluster",
                request_serializer=cloud_redis_cluster.DeleteClusterRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_cluster"]

    @property
    def delete_acl_policy(
        self,
    ) -> Callable[
        [cloud_redis_cluster.DeleteAclPolicyRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the delete acl policy method over gRPC.

        Deletes a specific ACL policy. This action will
        delete the ACL policy and all the rules associated with
        it. An ACL policy cannot be deleted if it is attached to
        a cluster.

        Returns:
            Callable[[~.DeleteAclPolicyRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_acl_policy" not in self._stubs:
            self._stubs["delete_acl_policy"] = self._logged_channel.unary_unary(
                "/google.cloud.redis.cluster.v1beta1.CloudRedisCluster/DeleteAclPolicy",
                request_serializer=cloud_redis_cluster.DeleteAclPolicyRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_acl_policy"]

    @property
    def get_acl_policy_revision(
        self,
    ) -> Callable[
        [cloud_redis_cluster.GetAclPolicyRevisionRequest],
        Awaitable[cloud_redis_cluster.AclPolicyRevision],
    ]:
        r"""Return a callable for the get acl policy revision method over gRPC.

        Gets details of a specific ACL policy revision.

        Returns:
            Callable[[~.GetAclPolicyRevisionRequest],
                    Awaitable[~.AclPolicyRevision]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_acl_policy_revision" not in self._stubs:
            self._stubs["get_acl_policy_revision"] = self._logged_channel.unary_unary(
                "/google.cloud.redis.cluster.v1beta1.CloudRedisCluster/GetAclPolicyRevision",
                request_serializer=cloud_redis_cluster.GetAclPolicyRevisionRequest.serialize,
                response_deserializer=cloud_redis_cluster.AclPolicyRevision.deserialize,
            )
        return self._stubs["get_acl_policy_revision"]

    @property
    def list_acl_policy_revisions(
        self,
    ) -> Callable[
        [cloud_redis_cluster.ListAclPolicyRevisionsRequest],
        Awaitable[cloud_redis_cluster.ListAclPolicyRevisionsResponse],
    ]:
        r"""Return a callable for the list acl policy revisions method over gRPC.

        Lists all ACL policy revisions in a given ACL policy.

        Returns:
            Callable[[~.ListAclPolicyRevisionsRequest],
                    Awaitable[~.ListAclPolicyRevisionsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_acl_policy_revisions" not in self._stubs:
            self._stubs["list_acl_policy_revisions"] = self._logged_channel.unary_unary(
                "/google.cloud.redis.cluster.v1beta1.CloudRedisCluster/ListAclPolicyRevisions",
                request_serializer=cloud_redis_cluster.ListAclPolicyRevisionsRequest.serialize,
                response_deserializer=cloud_redis_cluster.ListAclPolicyRevisionsResponse.deserialize,
            )
        return self._stubs["list_acl_policy_revisions"]

    @property
    def create_cluster(
        self,
    ) -> Callable[
        [cloud_redis_cluster.CreateClusterRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create cluster method over gRPC.

        Creates a Redis cluster based on the specified
        properties. The creation is executed asynchronously and
        callers may check the returned operation to track its
        progress. Once the operation is completed the Redis
        cluster will be fully functional. The completed
        longrunning.Operation will contain the new cluster
        object in the response field.

        The returned operation is automatically deleted after a
        few hours, so there is no need to call DeleteOperation.

        Returns:
            Callable[[~.CreateClusterRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_cluster" not in self._stubs:
            self._stubs["create_cluster"] = self._logged_channel.unary_unary(
                "/google.cloud.redis.cluster.v1beta1.CloudRedisCluster/CreateCluster",
                request_serializer=cloud_redis_cluster.CreateClusterRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_cluster"]

    @property
    def create_acl_policy(
        self,
    ) -> Callable[
        [cloud_redis_cluster.CreateAclPolicyRequest],
        Awaitable[cloud_redis_cluster.AclPolicy],
    ]:
        r"""Return a callable for the create acl policy method over gRPC.

        Creates an ACL policy.
        The creation is executed synchronously and the policy is
        available for use immediately after the RPC returns.

        Returns:
            Callable[[~.CreateAclPolicyRequest],
                    Awaitable[~.AclPolicy]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_acl_policy" not in self._stubs:
            self._stubs["create_acl_policy"] = self._logged_channel.unary_unary(
                "/google.cloud.redis.cluster.v1beta1.CloudRedisCluster/CreateAclPolicy",
                request_serializer=cloud_redis_cluster.CreateAclPolicyRequest.serialize,
                response_deserializer=cloud_redis_cluster.AclPolicy.deserialize,
            )
        return self._stubs["create_acl_policy"]

    @property
    def get_cluster_certificate_authority(
        self,
    ) -> Callable[
        [cloud_redis_cluster.GetClusterCertificateAuthorityRequest],
        Awaitable[cloud_redis_cluster.CertificateAuthority],
    ]:
        r"""Return a callable for the get cluster certificate
        authority method over gRPC.

        Gets the details of certificate authority information
        for Redis cluster.

        Returns:
            Callable[[~.GetClusterCertificateAuthorityRequest],
                    Awaitable[~.CertificateAuthority]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_cluster_certificate_authority" not in self._stubs:
            self._stubs["get_cluster_certificate_authority"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.redis.cluster.v1beta1.CloudRedisCluster/GetClusterCertificateAuthority",
                    request_serializer=cloud_redis_cluster.GetClusterCertificateAuthorityRequest.serialize,
                    response_deserializer=cloud_redis_cluster.CertificateAuthority.deserialize,
                )
            )
        return self._stubs["get_cluster_certificate_authority"]

    @property
    def get_shared_regional_certificate_authority(
        self,
    ) -> Callable[
        [cloud_redis_cluster.GetSharedRegionalCertificateAuthorityRequest],
        Awaitable[cloud_redis_cluster.SharedRegionalCertificateAuthority],
    ]:
        r"""Return a callable for the get shared regional
        certificate authority method over gRPC.

        Gets the details of regional certificate authority
        information for Redis cluster.

        Returns:
            Callable[[~.GetSharedRegionalCertificateAuthorityRequest],
                    Awaitable[~.SharedRegionalCertificateAuthority]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_shared_regional_certificate_authority" not in self._stubs:
            self._stubs["get_shared_regional_certificate_authority"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.redis.cluster.v1beta1.CloudRedisCluster/GetSharedRegionalCertificateAuthority",
                    request_serializer=cloud_redis_cluster.GetSharedRegionalCertificateAuthorityRequest.serialize,
                    response_deserializer=cloud_redis_cluster.SharedRegionalCertificateAuthority.deserialize,
                )
            )
        return self._stubs["get_shared_regional_certificate_authority"]

    @property
    def reschedule_cluster_maintenance(
        self,
    ) -> Callable[
        [cloud_redis_cluster.RescheduleClusterMaintenanceRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the reschedule cluster maintenance method over gRPC.

        Reschedules upcoming maintenance event.

        Returns:
            Callable[[~.RescheduleClusterMaintenanceRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "reschedule_cluster_maintenance" not in self._stubs:
            self._stubs["reschedule_cluster_maintenance"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.redis.cluster.v1beta1.CloudRedisCluster/RescheduleClusterMaintenance",
                    request_serializer=cloud_redis_cluster.RescheduleClusterMaintenanceRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["reschedule_cluster_maintenance"]

    @property
    def list_backup_collections(
        self,
    ) -> Callable[
        [cloud_redis_cluster.ListBackupCollectionsRequest],
        Awaitable[cloud_redis_cluster.ListBackupCollectionsResponse],
    ]:
        r"""Return a callable for the list backup collections method over gRPC.

        Lists all backup collections owned by a consumer project in
        either the specified location (region) or all locations.

        If ``location_id`` is specified as ``-`` (wildcard), then all
        regions available to the project are queried, and the results
        are aggregated.

        Returns:
            Callable[[~.ListBackupCollectionsRequest],
                    Awaitable[~.ListBackupCollectionsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_backup_collections" not in self._stubs:
            self._stubs["list_backup_collections"] = self._logged_channel.unary_unary(
                "/google.cloud.redis.cluster.v1beta1.CloudRedisCluster/ListBackupCollections",
                request_serializer=cloud_redis_cluster.ListBackupCollectionsRequest.serialize,
                response_deserializer=cloud_redis_cluster.ListBackupCollectionsResponse.deserialize,
            )
        return self._stubs["list_backup_collections"]

    @property
    def get_backup_collection(
        self,
    ) -> Callable[
        [cloud_redis_cluster.GetBackupCollectionRequest],
        Awaitable[cloud_redis_cluster.BackupCollection],
    ]:
        r"""Return a callable for the get backup collection method over gRPC.

        Get a backup collection.

        Returns:
            Callable[[~.GetBackupCollectionRequest],
                    Awaitable[~.BackupCollection]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_backup_collection" not in self._stubs:
            self._stubs["get_backup_collection"] = self._logged_channel.unary_unary(
                "/google.cloud.redis.cluster.v1beta1.CloudRedisCluster/GetBackupCollection",
                request_serializer=cloud_redis_cluster.GetBackupCollectionRequest.serialize,
                response_deserializer=cloud_redis_cluster.BackupCollection.deserialize,
            )
        return self._stubs["get_backup_collection"]

    @property
    def list_backups(
        self,
    ) -> Callable[
        [cloud_redis_cluster.ListBackupsRequest],
        Awaitable[cloud_redis_cluster.ListBackupsResponse],
    ]:
        r"""Return a callable for the list backups method over gRPC.

        Lists all backups owned by a backup collection.

        Returns:
            Callable[[~.ListBackupsRequest],
                    Awaitable[~.ListBackupsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_backups" not in self._stubs:
            self._stubs["list_backups"] = self._logged_channel.unary_unary(
                "/google.cloud.redis.cluster.v1beta1.CloudRedisCluster/ListBackups",
                request_serializer=cloud_redis_cluster.ListBackupsRequest.serialize,
                response_deserializer=cloud_redis_cluster.ListBackupsResponse.deserialize,
            )
        return self._stubs["list_backups"]

    @property
    def get_backup(
        self,
    ) -> Callable[
        [cloud_redis_cluster.GetBackupRequest], Awaitable[cloud_redis_cluster.Backup]
    ]:
        r"""Return a callable for the get backup method over gRPC.

        Gets the details of a specific backup.

        Returns:
            Callable[[~.GetBackupRequest],
                    Awaitable[~.Backup]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_backup" not in self._stubs:
            self._stubs["get_backup"] = self._logged_channel.unary_unary(
                "/google.cloud.redis.cluster.v1beta1.CloudRedisCluster/GetBackup",
                request_serializer=cloud_redis_cluster.GetBackupRequest.serialize,
                response_deserializer=cloud_redis_cluster.Backup.deserialize,
            )
        return self._stubs["get_backup"]

    @property
    def delete_backup(
        self,
    ) -> Callable[
        [cloud_redis_cluster.DeleteBackupRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the delete backup method over gRPC.

        Deletes a specific backup.

        Returns:
            Callable[[~.DeleteBackupRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_backup" not in self._stubs:
            self._stubs["delete_backup"] = self._logged_channel.unary_unary(
                "/google.cloud.redis.cluster.v1beta1.CloudRedisCluster/DeleteBackup",
                request_serializer=cloud_redis_cluster.DeleteBackupRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_backup"]

    @property
    def export_backup(
        self,
    ) -> Callable[
        [cloud_redis_cluster.ExportBackupRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the export backup method over gRPC.

        Exports a specific backup to a customer target Cloud
        Storage URI.

        Returns:
            Callable[[~.ExportBackupRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "export_backup" not in self._stubs:
            self._stubs["export_backup"] = self._logged_channel.unary_unary(
                "/google.cloud.redis.cluster.v1beta1.CloudRedisCluster/ExportBackup",
                request_serializer=cloud_redis_cluster.ExportBackupRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["export_backup"]

    @property
    def backup_cluster(
        self,
    ) -> Callable[
        [cloud_redis_cluster.BackupClusterRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the backup cluster method over gRPC.

        Backup Redis Cluster.
        If this is the first time a backup is being created, a
        backup collection will be created at the backend, and
        this backup belongs to this collection. Both collection
        and backup will have a resource name. Backup will be
        executed for each shard. A replica (primary if nonHA)
        will be selected to perform the execution. Backup call
        will be rejected if there is an ongoing backup or update
        operation. Be aware that during preview, if the
        cluster's internal software version is too old, critical
        update will be performed before actual backup. Once the
        internal software version is updated to the minimum
        version required by the backup feature, subsequent
        backups will not require critical update. After preview,
        there will be no critical update needed for backup.

        Returns:
            Callable[[~.BackupClusterRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "backup_cluster" not in self._stubs:
            self._stubs["backup_cluster"] = self._logged_channel.unary_unary(
                "/google.cloud.redis.cluster.v1beta1.CloudRedisCluster/BackupCluster",
                request_serializer=cloud_redis_cluster.BackupClusterRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["backup_cluster"]

    @property
    def list_token_auth_users(
        self,
    ) -> Callable[
        [cloud_redis_cluster.ListTokenAuthUsersRequest],
        Awaitable[cloud_redis_cluster.ListTokenAuthUsersResponse],
    ]:
        r"""Return a callable for the list token auth users method over gRPC.

        Lists all the token auth users for a token based auth
        enabled cluster.

        Returns:
            Callable[[~.ListTokenAuthUsersRequest],
                    Awaitable[~.ListTokenAuthUsersResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_token_auth_users" not in self._stubs:
            self._stubs["list_token_auth_users"] = self._logged_channel.unary_unary(
                "/google.cloud.redis.cluster.v1beta1.CloudRedisCluster/ListTokenAuthUsers",
                request_serializer=cloud_redis_cluster.ListTokenAuthUsersRequest.serialize,
                response_deserializer=cloud_redis_cluster.ListTokenAuthUsersResponse.deserialize,
            )
        return self._stubs["list_token_auth_users"]

    @property
    def get_token_auth_user(
        self,
    ) -> Callable[
        [cloud_redis_cluster.GetTokenAuthUserRequest],
        Awaitable[cloud_redis_cluster.TokenAuthUser],
    ]:
        r"""Return a callable for the get token auth user method over gRPC.

        Gets a specific token auth user for a basic auth
        enabled cluster.

        Returns:
            Callable[[~.GetTokenAuthUserRequest],
                    Awaitable[~.TokenAuthUser]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_token_auth_user" not in self._stubs:
            self._stubs["get_token_auth_user"] = self._logged_channel.unary_unary(
                "/google.cloud.redis.cluster.v1beta1.CloudRedisCluster/GetTokenAuthUser",
                request_serializer=cloud_redis_cluster.GetTokenAuthUserRequest.serialize,
                response_deserializer=cloud_redis_cluster.TokenAuthUser.deserialize,
            )
        return self._stubs["get_token_auth_user"]

    @property
    def list_auth_tokens(
        self,
    ) -> Callable[
        [cloud_redis_cluster.ListAuthTokensRequest],
        Awaitable[cloud_redis_cluster.ListAuthTokensResponse],
    ]:
        r"""Return a callable for the list auth tokens method over gRPC.

        Lists all the auth tokens for a specific token auth
        user.

        Returns:
            Callable[[~.ListAuthTokensRequest],
                    Awaitable[~.ListAuthTokensResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_auth_tokens" not in self._stubs:
            self._stubs["list_auth_tokens"] = self._logged_channel.unary_unary(
                "/google.cloud.redis.cluster.v1beta1.CloudRedisCluster/ListAuthTokens",
                request_serializer=cloud_redis_cluster.ListAuthTokensRequest.serialize,
                response_deserializer=cloud_redis_cluster.ListAuthTokensResponse.deserialize,
            )
        return self._stubs["list_auth_tokens"]

    @property
    def get_auth_token(
        self,
    ) -> Callable[
        [cloud_redis_cluster.GetAuthTokenRequest],
        Awaitable[cloud_redis_cluster.AuthToken],
    ]:
        r"""Return a callable for the get auth token method over gRPC.

        Gets a specific auth token for a specific token auth
        user.

        Returns:
            Callable[[~.GetAuthTokenRequest],
                    Awaitable[~.AuthToken]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_auth_token" not in self._stubs:
            self._stubs["get_auth_token"] = self._logged_channel.unary_unary(
                "/google.cloud.redis.cluster.v1beta1.CloudRedisCluster/GetAuthToken",
                request_serializer=cloud_redis_cluster.GetAuthTokenRequest.serialize,
                response_deserializer=cloud_redis_cluster.AuthToken.deserialize,
            )
        return self._stubs["get_auth_token"]

    @property
    def add_token_auth_user(
        self,
    ) -> Callable[
        [cloud_redis_cluster.AddTokenAuthUserRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the add token auth user method over gRPC.

        Adds a token auth user for a token based auth enabled
        cluster.

        Returns:
            Callable[[~.AddTokenAuthUserRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "add_token_auth_user" not in self._stubs:
            self._stubs["add_token_auth_user"] = self._logged_channel.unary_unary(
                "/google.cloud.redis.cluster.v1beta1.CloudRedisCluster/AddTokenAuthUser",
                request_serializer=cloud_redis_cluster.AddTokenAuthUserRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["add_token_auth_user"]

    @property
    def delete_token_auth_user(
        self,
    ) -> Callable[
        [cloud_redis_cluster.DeleteTokenAuthUserRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the delete token auth user method over gRPC.

        Deletes a token auth user for a token based auth
        enabled cluster.

        Returns:
            Callable[[~.DeleteTokenAuthUserRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_token_auth_user" not in self._stubs:
            self._stubs["delete_token_auth_user"] = self._logged_channel.unary_unary(
                "/google.cloud.redis.cluster.v1beta1.CloudRedisCluster/DeleteTokenAuthUser",
                request_serializer=cloud_redis_cluster.DeleteTokenAuthUserRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_token_auth_user"]

    @property
    def add_auth_token(
        self,
    ) -> Callable[
        [cloud_redis_cluster.AddAuthTokenRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the add auth token method over gRPC.

        Adds a auth token for a user of a token based auth
        enabled cluster.

        Returns:
            Callable[[~.AddAuthTokenRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "add_auth_token" not in self._stubs:
            self._stubs["add_auth_token"] = self._logged_channel.unary_unary(
                "/google.cloud.redis.cluster.v1beta1.CloudRedisCluster/AddAuthToken",
                request_serializer=cloud_redis_cluster.AddAuthTokenRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["add_auth_token"]

    @property
    def delete_auth_token(
        self,
    ) -> Callable[
        [cloud_redis_cluster.DeleteAuthTokenRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the delete auth token method over gRPC.

        Removes a auth token for a user of a token based auth
        enabled instance.

        Returns:
            Callable[[~.DeleteAuthTokenRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_auth_token" not in self._stubs:
            self._stubs["delete_auth_token"] = self._logged_channel.unary_unary(
                "/google.cloud.redis.cluster.v1beta1.CloudRedisCluster/DeleteAuthToken",
                request_serializer=cloud_redis_cluster.DeleteAuthTokenRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_auth_token"]

    def _prep_wrapped_messages(self, client_info):
        """Precompute the wrapped methods, overriding the base class method to use async wrappers."""
        self._wrapped_methods = {
            self.list_clusters: self._wrap_method(
                self.list_clusters,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.list_acl_policies: self._wrap_method(
                self.list_acl_policies,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.get_cluster: self._wrap_method(
                self.get_cluster,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.get_acl_policy: self._wrap_method(
                self.get_acl_policy,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.update_cluster: self._wrap_method(
                self.update_cluster,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.update_acl_policy: self._wrap_method(
                self.update_acl_policy,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.delete_cluster: self._wrap_method(
                self.delete_cluster,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.delete_acl_policy: self._wrap_method(
                self.delete_acl_policy,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.get_acl_policy_revision: self._wrap_method(
                self.get_acl_policy_revision,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_acl_policy_revisions: self._wrap_method(
                self.list_acl_policy_revisions,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_cluster: self._wrap_method(
                self.create_cluster,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.create_acl_policy: self._wrap_method(
                self.create_acl_policy,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.get_cluster_certificate_authority: self._wrap_method(
                self.get_cluster_certificate_authority,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.get_shared_regional_certificate_authority: self._wrap_method(
                self.get_shared_regional_certificate_authority,
                default_timeout=None,
                client_info=client_info,
            ),
            self.reschedule_cluster_maintenance: self._wrap_method(
                self.reschedule_cluster_maintenance,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.list_backup_collections: self._wrap_method(
                self.list_backup_collections,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.get_backup_collection: self._wrap_method(
                self.get_backup_collection,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.list_backups: self._wrap_method(
                self.list_backups,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.get_backup: self._wrap_method(
                self.get_backup,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.delete_backup: self._wrap_method(
                self.delete_backup,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.export_backup: self._wrap_method(
                self.export_backup,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.backup_cluster: self._wrap_method(
                self.backup_cluster,
                default_timeout=600.0,
                client_info=client_info,
            ),
            self.list_token_auth_users: self._wrap_method(
                self.list_token_auth_users,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_token_auth_user: self._wrap_method(
                self.get_token_auth_user,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_auth_tokens: self._wrap_method(
                self.list_auth_tokens,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_auth_token: self._wrap_method(
                self.get_auth_token,
                default_timeout=None,
                client_info=client_info,
            ),
            self.add_token_auth_user: self._wrap_method(
                self.add_token_auth_user,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_token_auth_user: self._wrap_method(
                self.delete_token_auth_user,
                default_timeout=None,
                client_info=client_info,
            ),
            self.add_auth_token: self._wrap_method(
                self.add_auth_token,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_auth_token: self._wrap_method(
                self.delete_auth_token,
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


__all__ = ("CloudRedisClusterGrpcAsyncIOTransport",)
