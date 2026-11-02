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

from google.cloud.managedkafka_v1.types import managed_kafka, resources

from .base import DEFAULT_CLIENT_INFO, ManagedKafkaTransport

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
                    "serviceName": "google.cloud.managedkafka.v1.ManagedKafka",
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
                    "serviceName": "google.cloud.managedkafka.v1.ManagedKafka",
                    "rpcName": client_call_details.method,
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class ManagedKafkaGrpcTransport(ManagedKafkaTransport):
    """gRPC backend transport for ManagedKafka.

    The service that a client application uses to manage Apache
    Kafka clusters, topics and consumer groups.

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
        host: str = "managedkafka.googleapis.com",
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
        host: str = "managedkafka.googleapis.com",
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
    def list_clusters(
        self,
    ) -> Callable[
        [managed_kafka.ListClustersRequest], managed_kafka.ListClustersResponse
    ]:
        r"""Return a callable for the list clusters method over gRPC.

        Lists the clusters in a given project and location.

        Returns:
            Callable[[~.ListClustersRequest],
                    ~.ListClustersResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_clusters" not in self._stubs:
            self._stubs["list_clusters"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.v1.ManagedKafka/ListClusters",
                request_serializer=managed_kafka.ListClustersRequest.serialize,
                response_deserializer=managed_kafka.ListClustersResponse.deserialize,
            )
        return self._stubs["list_clusters"]

    @property
    def get_cluster(
        self,
    ) -> Callable[[managed_kafka.GetClusterRequest], resources.Cluster]:
        r"""Return a callable for the get cluster method over gRPC.

        Returns the properties of a single cluster.

        Returns:
            Callable[[~.GetClusterRequest],
                    ~.Cluster]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_cluster" not in self._stubs:
            self._stubs["get_cluster"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.v1.ManagedKafka/GetCluster",
                request_serializer=managed_kafka.GetClusterRequest.serialize,
                response_deserializer=resources.Cluster.deserialize,
            )
        return self._stubs["get_cluster"]

    @property
    def create_cluster(
        self,
    ) -> Callable[[managed_kafka.CreateClusterRequest], operations_pb2.Operation]:
        r"""Return a callable for the create cluster method over gRPC.

        Creates a new cluster in a given project and
        location.

        Returns:
            Callable[[~.CreateClusterRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_cluster" not in self._stubs:
            self._stubs["create_cluster"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.v1.ManagedKafka/CreateCluster",
                request_serializer=managed_kafka.CreateClusterRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_cluster"]

    @property
    def update_cluster(
        self,
    ) -> Callable[[managed_kafka.UpdateClusterRequest], operations_pb2.Operation]:
        r"""Return a callable for the update cluster method over gRPC.

        Updates the properties of a single cluster.

        Returns:
            Callable[[~.UpdateClusterRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_cluster" not in self._stubs:
            self._stubs["update_cluster"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.v1.ManagedKafka/UpdateCluster",
                request_serializer=managed_kafka.UpdateClusterRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_cluster"]

    @property
    def delete_cluster(
        self,
    ) -> Callable[[managed_kafka.DeleteClusterRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete cluster method over gRPC.

        Deletes a single cluster.

        Returns:
            Callable[[~.DeleteClusterRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_cluster" not in self._stubs:
            self._stubs["delete_cluster"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.v1.ManagedKafka/DeleteCluster",
                request_serializer=managed_kafka.DeleteClusterRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_cluster"]

    @property
    def list_topics(
        self,
    ) -> Callable[[managed_kafka.ListTopicsRequest], managed_kafka.ListTopicsResponse]:
        r"""Return a callable for the list topics method over gRPC.

        Lists the topics in a given cluster.

        Returns:
            Callable[[~.ListTopicsRequest],
                    ~.ListTopicsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_topics" not in self._stubs:
            self._stubs["list_topics"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.v1.ManagedKafka/ListTopics",
                request_serializer=managed_kafka.ListTopicsRequest.serialize,
                response_deserializer=managed_kafka.ListTopicsResponse.deserialize,
            )
        return self._stubs["list_topics"]

    @property
    def get_topic(self) -> Callable[[managed_kafka.GetTopicRequest], resources.Topic]:
        r"""Return a callable for the get topic method over gRPC.

        Returns the properties of a single topic.

        Returns:
            Callable[[~.GetTopicRequest],
                    ~.Topic]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_topic" not in self._stubs:
            self._stubs["get_topic"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.v1.ManagedKafka/GetTopic",
                request_serializer=managed_kafka.GetTopicRequest.serialize,
                response_deserializer=resources.Topic.deserialize,
            )
        return self._stubs["get_topic"]

    @property
    def create_topic(
        self,
    ) -> Callable[[managed_kafka.CreateTopicRequest], resources.Topic]:
        r"""Return a callable for the create topic method over gRPC.

        Creates a new topic in a given project and location.

        Returns:
            Callable[[~.CreateTopicRequest],
                    ~.Topic]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_topic" not in self._stubs:
            self._stubs["create_topic"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.v1.ManagedKafka/CreateTopic",
                request_serializer=managed_kafka.CreateTopicRequest.serialize,
                response_deserializer=resources.Topic.deserialize,
            )
        return self._stubs["create_topic"]

    @property
    def update_topic(
        self,
    ) -> Callable[[managed_kafka.UpdateTopicRequest], resources.Topic]:
        r"""Return a callable for the update topic method over gRPC.

        Updates the properties of a single topic.

        Returns:
            Callable[[~.UpdateTopicRequest],
                    ~.Topic]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_topic" not in self._stubs:
            self._stubs["update_topic"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.v1.ManagedKafka/UpdateTopic",
                request_serializer=managed_kafka.UpdateTopicRequest.serialize,
                response_deserializer=resources.Topic.deserialize,
            )
        return self._stubs["update_topic"]

    @property
    def delete_topic(
        self,
    ) -> Callable[[managed_kafka.DeleteTopicRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete topic method over gRPC.

        Deletes a single topic.

        Returns:
            Callable[[~.DeleteTopicRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_topic" not in self._stubs:
            self._stubs["delete_topic"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.v1.ManagedKafka/DeleteTopic",
                request_serializer=managed_kafka.DeleteTopicRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_topic"]

    @property
    def list_consumer_groups(
        self,
    ) -> Callable[
        [managed_kafka.ListConsumerGroupsRequest],
        managed_kafka.ListConsumerGroupsResponse,
    ]:
        r"""Return a callable for the list consumer groups method over gRPC.

        Lists the consumer groups in a given cluster.

        Returns:
            Callable[[~.ListConsumerGroupsRequest],
                    ~.ListConsumerGroupsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_consumer_groups" not in self._stubs:
            self._stubs["list_consumer_groups"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.v1.ManagedKafka/ListConsumerGroups",
                request_serializer=managed_kafka.ListConsumerGroupsRequest.serialize,
                response_deserializer=managed_kafka.ListConsumerGroupsResponse.deserialize,
            )
        return self._stubs["list_consumer_groups"]

    @property
    def get_consumer_group(
        self,
    ) -> Callable[[managed_kafka.GetConsumerGroupRequest], resources.ConsumerGroup]:
        r"""Return a callable for the get consumer group method over gRPC.

        Returns the properties of a single consumer group.

        Returns:
            Callable[[~.GetConsumerGroupRequest],
                    ~.ConsumerGroup]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_consumer_group" not in self._stubs:
            self._stubs["get_consumer_group"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.v1.ManagedKafka/GetConsumerGroup",
                request_serializer=managed_kafka.GetConsumerGroupRequest.serialize,
                response_deserializer=resources.ConsumerGroup.deserialize,
            )
        return self._stubs["get_consumer_group"]

    @property
    def update_consumer_group(
        self,
    ) -> Callable[[managed_kafka.UpdateConsumerGroupRequest], resources.ConsumerGroup]:
        r"""Return a callable for the update consumer group method over gRPC.

        Updates the properties of a single consumer group.

        Returns:
            Callable[[~.UpdateConsumerGroupRequest],
                    ~.ConsumerGroup]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_consumer_group" not in self._stubs:
            self._stubs["update_consumer_group"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.v1.ManagedKafka/UpdateConsumerGroup",
                request_serializer=managed_kafka.UpdateConsumerGroupRequest.serialize,
                response_deserializer=resources.ConsumerGroup.deserialize,
            )
        return self._stubs["update_consumer_group"]

    @property
    def delete_consumer_group(
        self,
    ) -> Callable[[managed_kafka.DeleteConsumerGroupRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete consumer group method over gRPC.

        Deletes a single consumer group.

        Returns:
            Callable[[~.DeleteConsumerGroupRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_consumer_group" not in self._stubs:
            self._stubs["delete_consumer_group"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.v1.ManagedKafka/DeleteConsumerGroup",
                request_serializer=managed_kafka.DeleteConsumerGroupRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_consumer_group"]

    @property
    def list_acls(
        self,
    ) -> Callable[[managed_kafka.ListAclsRequest], managed_kafka.ListAclsResponse]:
        r"""Return a callable for the list acls method over gRPC.

        Lists the acls in a given cluster.

        Returns:
            Callable[[~.ListAclsRequest],
                    ~.ListAclsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_acls" not in self._stubs:
            self._stubs["list_acls"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.v1.ManagedKafka/ListAcls",
                request_serializer=managed_kafka.ListAclsRequest.serialize,
                response_deserializer=managed_kafka.ListAclsResponse.deserialize,
            )
        return self._stubs["list_acls"]

    @property
    def get_acl(self) -> Callable[[managed_kafka.GetAclRequest], resources.Acl]:
        r"""Return a callable for the get acl method over gRPC.

        Returns the properties of a single acl.

        Returns:
            Callable[[~.GetAclRequest],
                    ~.Acl]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_acl" not in self._stubs:
            self._stubs["get_acl"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.v1.ManagedKafka/GetAcl",
                request_serializer=managed_kafka.GetAclRequest.serialize,
                response_deserializer=resources.Acl.deserialize,
            )
        return self._stubs["get_acl"]

    @property
    def create_acl(self) -> Callable[[managed_kafka.CreateAclRequest], resources.Acl]:
        r"""Return a callable for the create acl method over gRPC.

        Creates a new acl in the given project, location, and
        cluster.

        Returns:
            Callable[[~.CreateAclRequest],
                    ~.Acl]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_acl" not in self._stubs:
            self._stubs["create_acl"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.v1.ManagedKafka/CreateAcl",
                request_serializer=managed_kafka.CreateAclRequest.serialize,
                response_deserializer=resources.Acl.deserialize,
            )
        return self._stubs["create_acl"]

    @property
    def update_acl(self) -> Callable[[managed_kafka.UpdateAclRequest], resources.Acl]:
        r"""Return a callable for the update acl method over gRPC.

        Updates the properties of a single acl.

        Returns:
            Callable[[~.UpdateAclRequest],
                    ~.Acl]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_acl" not in self._stubs:
            self._stubs["update_acl"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.v1.ManagedKafka/UpdateAcl",
                request_serializer=managed_kafka.UpdateAclRequest.serialize,
                response_deserializer=resources.Acl.deserialize,
            )
        return self._stubs["update_acl"]

    @property
    def delete_acl(self) -> Callable[[managed_kafka.DeleteAclRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete acl method over gRPC.

        Deletes an acl.

        Returns:
            Callable[[~.DeleteAclRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_acl" not in self._stubs:
            self._stubs["delete_acl"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.v1.ManagedKafka/DeleteAcl",
                request_serializer=managed_kafka.DeleteAclRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_acl"]

    @property
    def add_acl_entry(
        self,
    ) -> Callable[
        [managed_kafka.AddAclEntryRequest], managed_kafka.AddAclEntryResponse
    ]:
        r"""Return a callable for the add acl entry method over gRPC.

        Incremental update: Adds an acl entry to an acl.
        Creates the acl if it does not exist yet.

        Returns:
            Callable[[~.AddAclEntryRequest],
                    ~.AddAclEntryResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "add_acl_entry" not in self._stubs:
            self._stubs["add_acl_entry"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.v1.ManagedKafka/AddAclEntry",
                request_serializer=managed_kafka.AddAclEntryRequest.serialize,
                response_deserializer=managed_kafka.AddAclEntryResponse.deserialize,
            )
        return self._stubs["add_acl_entry"]

    @property
    def remove_acl_entry(
        self,
    ) -> Callable[
        [managed_kafka.RemoveAclEntryRequest], managed_kafka.RemoveAclEntryResponse
    ]:
        r"""Return a callable for the remove acl entry method over gRPC.

        Incremental update: Removes an acl entry from an acl.
        Deletes the acl if its acl entries become empty (i.e. if
        the removed entry was the last one in the acl).

        Returns:
            Callable[[~.RemoveAclEntryRequest],
                    ~.RemoveAclEntryResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "remove_acl_entry" not in self._stubs:
            self._stubs["remove_acl_entry"] = self._logged_channel.unary_unary(
                "/google.cloud.managedkafka.v1.ManagedKafka/RemoveAclEntry",
                request_serializer=managed_kafka.RemoveAclEntryRequest.serialize,
                response_deserializer=managed_kafka.RemoveAclEntryResponse.deserialize,
            )
        return self._stubs["remove_acl_entry"]

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


__all__ = ("ManagedKafkaGrpcTransport",)
