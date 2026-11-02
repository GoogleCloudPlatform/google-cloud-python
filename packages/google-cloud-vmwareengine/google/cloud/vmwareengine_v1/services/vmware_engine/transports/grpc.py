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
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf.json_format import MessageToJson

from google.cloud.vmwareengine_v1.types import vmwareengine, vmwareengine_resources

from .base import DEFAULT_CLIENT_INFO, VmwareEngineTransport

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
                    "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
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
                    "serviceName": "google.cloud.vmwareengine.v1.VmwareEngine",
                    "rpcName": client_call_details.method,
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class VmwareEngineGrpcTransport(VmwareEngineTransport):
    """gRPC backend transport for VmwareEngine.

    VMwareEngine manages VMware's private clusters in the Cloud.

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
        host: str = "vmwareengine.googleapis.com",
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
                 The hostname to connect to (default: 'vmwareengine.googleapis.com').
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
        host: str = "vmwareengine.googleapis.com",
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
    def list_private_clouds(
        self,
    ) -> Callable[
        [vmwareengine.ListPrivateCloudsRequest], vmwareengine.ListPrivateCloudsResponse
    ]:
        r"""Return a callable for the list private clouds method over gRPC.

        Lists ``PrivateCloud`` resources in a given project and
        location.

        Returns:
            Callable[[~.ListPrivateCloudsRequest],
                    ~.ListPrivateCloudsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_private_clouds" not in self._stubs:
            self._stubs["list_private_clouds"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/ListPrivateClouds",
                request_serializer=vmwareengine.ListPrivateCloudsRequest.serialize,
                response_deserializer=vmwareengine.ListPrivateCloudsResponse.deserialize,
            )
        return self._stubs["list_private_clouds"]

    @property
    def get_private_cloud(
        self,
    ) -> Callable[
        [vmwareengine.GetPrivateCloudRequest], vmwareengine_resources.PrivateCloud
    ]:
        r"""Return a callable for the get private cloud method over gRPC.

        Retrieves a ``PrivateCloud`` resource by its resource name.

        Returns:
            Callable[[~.GetPrivateCloudRequest],
                    ~.PrivateCloud]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_private_cloud" not in self._stubs:
            self._stubs["get_private_cloud"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/GetPrivateCloud",
                request_serializer=vmwareengine.GetPrivateCloudRequest.serialize,
                response_deserializer=vmwareengine_resources.PrivateCloud.deserialize,
            )
        return self._stubs["get_private_cloud"]

    @property
    def create_private_cloud(
        self,
    ) -> Callable[[vmwareengine.CreatePrivateCloudRequest], operations_pb2.Operation]:
        r"""Return a callable for the create private cloud method over gRPC.

        Creates a new ``PrivateCloud`` resource in a given project and
        location. Private clouds of type ``STANDARD`` and
        ``TIME_LIMITED`` are zonal resources, ``STRETCHED`` private
        clouds are regional. Creating a private cloud also creates a
        `management
        cluster <https://cloud.google.com/vmware-engine/docs/concepts-vmware-components>`__
        for that private cloud.

        Returns:
            Callable[[~.CreatePrivateCloudRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_private_cloud" not in self._stubs:
            self._stubs["create_private_cloud"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/CreatePrivateCloud",
                request_serializer=vmwareengine.CreatePrivateCloudRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_private_cloud"]

    @property
    def update_private_cloud(
        self,
    ) -> Callable[[vmwareengine.UpdatePrivateCloudRequest], operations_pb2.Operation]:
        r"""Return a callable for the update private cloud method over gRPC.

        Modifies a ``PrivateCloud`` resource. Only the following fields
        can be updated: ``description``. Only fields specified in
        ``updateMask`` are applied.

        During operation processing, the resource is temporarily in the
        ``ACTIVE`` state before the operation fully completes. For that
        period of time, you can't update the resource. Use the operation
        status to determine when the processing fully completes.

        Returns:
            Callable[[~.UpdatePrivateCloudRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_private_cloud" not in self._stubs:
            self._stubs["update_private_cloud"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/UpdatePrivateCloud",
                request_serializer=vmwareengine.UpdatePrivateCloudRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_private_cloud"]

    @property
    def delete_private_cloud(
        self,
    ) -> Callable[[vmwareengine.DeletePrivateCloudRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete private cloud method over gRPC.

        Schedules a ``PrivateCloud`` resource for deletion.

        A ``PrivateCloud`` resource scheduled for deletion has
        ``PrivateCloud.state`` set to ``DELETED`` and ``expireTime`` set
        to the time when deletion is final and can no longer be
        reversed. The delete operation is marked as done as soon as the
        ``PrivateCloud`` is successfully scheduled for deletion (this
        also applies when ``delayHours`` is set to zero), and the
        operation is not kept in pending state until ``PrivateCloud`` is
        purged. ``PrivateCloud`` can be restored using
        ``UndeletePrivateCloud`` method before the ``expireTime``
        elapses. When ``expireTime`` is reached, deletion is final and
        all private cloud resources are irreversibly removed and billing
        stops. During the final removal process, ``PrivateCloud.state``
        is set to ``PURGING``. ``PrivateCloud`` can be polled using
        standard ``GET`` method for the whole period of deletion and
        purging. It will not be returned only when it is completely
        purged.

        Returns:
            Callable[[~.DeletePrivateCloudRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_private_cloud" not in self._stubs:
            self._stubs["delete_private_cloud"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/DeletePrivateCloud",
                request_serializer=vmwareengine.DeletePrivateCloudRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_private_cloud"]

    @property
    def undelete_private_cloud(
        self,
    ) -> Callable[[vmwareengine.UndeletePrivateCloudRequest], operations_pb2.Operation]:
        r"""Return a callable for the undelete private cloud method over gRPC.

        Restores a private cloud that was previously scheduled for
        deletion by ``DeletePrivateCloud``. A ``PrivateCloud`` resource
        scheduled for deletion has ``PrivateCloud.state`` set to
        ``DELETED`` and ``PrivateCloud.expireTime`` set to the time when
        deletion can no longer be reversed.

        Returns:
            Callable[[~.UndeletePrivateCloudRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "undelete_private_cloud" not in self._stubs:
            self._stubs["undelete_private_cloud"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/UndeletePrivateCloud",
                request_serializer=vmwareengine.UndeletePrivateCloudRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["undelete_private_cloud"]

    @property
    def list_clusters(
        self,
    ) -> Callable[
        [vmwareengine.ListClustersRequest], vmwareengine.ListClustersResponse
    ]:
        r"""Return a callable for the list clusters method over gRPC.

        Lists ``Cluster`` resources in a given private cloud.

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
                "/google.cloud.vmwareengine.v1.VmwareEngine/ListClusters",
                request_serializer=vmwareengine.ListClustersRequest.serialize,
                response_deserializer=vmwareengine.ListClustersResponse.deserialize,
            )
        return self._stubs["list_clusters"]

    @property
    def get_cluster(
        self,
    ) -> Callable[[vmwareengine.GetClusterRequest], vmwareengine_resources.Cluster]:
        r"""Return a callable for the get cluster method over gRPC.

        Retrieves a ``Cluster`` resource by its resource name.

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
                "/google.cloud.vmwareengine.v1.VmwareEngine/GetCluster",
                request_serializer=vmwareengine.GetClusterRequest.serialize,
                response_deserializer=vmwareengine_resources.Cluster.deserialize,
            )
        return self._stubs["get_cluster"]

    @property
    def create_cluster(
        self,
    ) -> Callable[[vmwareengine.CreateClusterRequest], operations_pb2.Operation]:
        r"""Return a callable for the create cluster method over gRPC.

        Creates a new cluster in a given private cloud. Creating a new
        cluster provides additional nodes for use in the parent private
        cloud and requires sufficient `node
        quota <https://cloud.google.com/vmware-engine/quotas>`__.

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
                "/google.cloud.vmwareengine.v1.VmwareEngine/CreateCluster",
                request_serializer=vmwareengine.CreateClusterRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_cluster"]

    @property
    def update_cluster(
        self,
    ) -> Callable[[vmwareengine.UpdateClusterRequest], operations_pb2.Operation]:
        r"""Return a callable for the update cluster method over gRPC.

        Modifies a ``Cluster`` resource. Only fields specified in
        ``updateMask`` are applied.

        During operation processing, the resource is temporarily in the
        ``ACTIVE`` state before the operation fully completes. For that
        period of time, you can't update the resource. Use the operation
        status to determine when the processing fully completes.

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
                "/google.cloud.vmwareengine.v1.VmwareEngine/UpdateCluster",
                request_serializer=vmwareengine.UpdateClusterRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_cluster"]

    @property
    def delete_cluster(
        self,
    ) -> Callable[[vmwareengine.DeleteClusterRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete cluster method over gRPC.

        Deletes a ``Cluster`` resource. To avoid unintended data loss,
        migrate or gracefully shut down any workloads running on the
        cluster before deletion. You cannot delete the management
        cluster of a private cloud using this method.

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
                "/google.cloud.vmwareengine.v1.VmwareEngine/DeleteCluster",
                request_serializer=vmwareengine.DeleteClusterRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_cluster"]

    @property
    def list_nodes(
        self,
    ) -> Callable[[vmwareengine.ListNodesRequest], vmwareengine.ListNodesResponse]:
        r"""Return a callable for the list nodes method over gRPC.

        Lists nodes in a given cluster.

        Returns:
            Callable[[~.ListNodesRequest],
                    ~.ListNodesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_nodes" not in self._stubs:
            self._stubs["list_nodes"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/ListNodes",
                request_serializer=vmwareengine.ListNodesRequest.serialize,
                response_deserializer=vmwareengine.ListNodesResponse.deserialize,
            )
        return self._stubs["list_nodes"]

    @property
    def get_node(
        self,
    ) -> Callable[[vmwareengine.GetNodeRequest], vmwareengine_resources.Node]:
        r"""Return a callable for the get node method over gRPC.

        Gets details of a single node.

        Returns:
            Callable[[~.GetNodeRequest],
                    ~.Node]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_node" not in self._stubs:
            self._stubs["get_node"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/GetNode",
                request_serializer=vmwareengine.GetNodeRequest.serialize,
                response_deserializer=vmwareengine_resources.Node.deserialize,
            )
        return self._stubs["get_node"]

    @property
    def list_external_addresses(
        self,
    ) -> Callable[
        [vmwareengine.ListExternalAddressesRequest],
        vmwareengine.ListExternalAddressesResponse,
    ]:
        r"""Return a callable for the list external addresses method over gRPC.

        Lists external IP addresses assigned to VMware
        workload VMs in a given private cloud.

        Returns:
            Callable[[~.ListExternalAddressesRequest],
                    ~.ListExternalAddressesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_external_addresses" not in self._stubs:
            self._stubs["list_external_addresses"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/ListExternalAddresses",
                request_serializer=vmwareengine.ListExternalAddressesRequest.serialize,
                response_deserializer=vmwareengine.ListExternalAddressesResponse.deserialize,
            )
        return self._stubs["list_external_addresses"]

    @property
    def fetch_network_policy_external_addresses(
        self,
    ) -> Callable[
        [vmwareengine.FetchNetworkPolicyExternalAddressesRequest],
        vmwareengine.FetchNetworkPolicyExternalAddressesResponse,
    ]:
        r"""Return a callable for the fetch network policy external
        addresses method over gRPC.

        Lists external IP addresses assigned to VMware
        workload VMs within the scope of the given network
        policy.

        Returns:
            Callable[[~.FetchNetworkPolicyExternalAddressesRequest],
                    ~.FetchNetworkPolicyExternalAddressesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "fetch_network_policy_external_addresses" not in self._stubs:
            self._stubs["fetch_network_policy_external_addresses"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.vmwareengine.v1.VmwareEngine/FetchNetworkPolicyExternalAddresses",
                    request_serializer=vmwareengine.FetchNetworkPolicyExternalAddressesRequest.serialize,
                    response_deserializer=vmwareengine.FetchNetworkPolicyExternalAddressesResponse.deserialize,
                )
            )
        return self._stubs["fetch_network_policy_external_addresses"]

    @property
    def get_external_address(
        self,
    ) -> Callable[
        [vmwareengine.GetExternalAddressRequest], vmwareengine_resources.ExternalAddress
    ]:
        r"""Return a callable for the get external address method over gRPC.

        Gets details of a single external IP address.

        Returns:
            Callable[[~.GetExternalAddressRequest],
                    ~.ExternalAddress]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_external_address" not in self._stubs:
            self._stubs["get_external_address"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/GetExternalAddress",
                request_serializer=vmwareengine.GetExternalAddressRequest.serialize,
                response_deserializer=vmwareengine_resources.ExternalAddress.deserialize,
            )
        return self._stubs["get_external_address"]

    @property
    def create_external_address(
        self,
    ) -> Callable[
        [vmwareengine.CreateExternalAddressRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the create external address method over gRPC.

        Creates a new ``ExternalAddress`` resource in a given private
        cloud. The network policy that corresponds to the private cloud
        must have the external IP address network service enabled
        (``NetworkPolicy.external_ip``).

        Returns:
            Callable[[~.CreateExternalAddressRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_external_address" not in self._stubs:
            self._stubs["create_external_address"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/CreateExternalAddress",
                request_serializer=vmwareengine.CreateExternalAddressRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_external_address"]

    @property
    def update_external_address(
        self,
    ) -> Callable[
        [vmwareengine.UpdateExternalAddressRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the update external address method over gRPC.

        Updates the parameters of a single external IP address. Only
        fields specified in ``update_mask`` are applied.

        During operation processing, the resource is temporarily in the
        ``ACTIVE`` state before the operation fully completes. For that
        period of time, you can't update the resource. Use the operation
        status to determine when the processing fully completes.

        Returns:
            Callable[[~.UpdateExternalAddressRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_external_address" not in self._stubs:
            self._stubs["update_external_address"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/UpdateExternalAddress",
                request_serializer=vmwareengine.UpdateExternalAddressRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_external_address"]

    @property
    def delete_external_address(
        self,
    ) -> Callable[
        [vmwareengine.DeleteExternalAddressRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the delete external address method over gRPC.

        Deletes a single external IP address. When you delete
        an external IP address, connectivity between the
        external IP address and the corresponding internal IP
        address is lost.

        Returns:
            Callable[[~.DeleteExternalAddressRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_external_address" not in self._stubs:
            self._stubs["delete_external_address"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/DeleteExternalAddress",
                request_serializer=vmwareengine.DeleteExternalAddressRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_external_address"]

    @property
    def list_subnets(
        self,
    ) -> Callable[[vmwareengine.ListSubnetsRequest], vmwareengine.ListSubnetsResponse]:
        r"""Return a callable for the list subnets method over gRPC.

        Lists subnets in a given private cloud.

        Returns:
            Callable[[~.ListSubnetsRequest],
                    ~.ListSubnetsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_subnets" not in self._stubs:
            self._stubs["list_subnets"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/ListSubnets",
                request_serializer=vmwareengine.ListSubnetsRequest.serialize,
                response_deserializer=vmwareengine.ListSubnetsResponse.deserialize,
            )
        return self._stubs["list_subnets"]

    @property
    def get_subnet(
        self,
    ) -> Callable[[vmwareengine.GetSubnetRequest], vmwareengine_resources.Subnet]:
        r"""Return a callable for the get subnet method over gRPC.

        Gets details of a single subnet.

        Returns:
            Callable[[~.GetSubnetRequest],
                    ~.Subnet]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_subnet" not in self._stubs:
            self._stubs["get_subnet"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/GetSubnet",
                request_serializer=vmwareengine.GetSubnetRequest.serialize,
                response_deserializer=vmwareengine_resources.Subnet.deserialize,
            )
        return self._stubs["get_subnet"]

    @property
    def update_subnet(
        self,
    ) -> Callable[[vmwareengine.UpdateSubnetRequest], operations_pb2.Operation]:
        r"""Return a callable for the update subnet method over gRPC.

        Updates the parameters of a single subnet. Only fields specified
        in ``update_mask`` are applied.

        *Note*: This API is synchronous and always returns a successful
        ``google.longrunning.Operation`` (LRO). The returned LRO will
        only have ``done`` and ``response`` fields.

        Returns:
            Callable[[~.UpdateSubnetRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_subnet" not in self._stubs:
            self._stubs["update_subnet"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/UpdateSubnet",
                request_serializer=vmwareengine.UpdateSubnetRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_subnet"]

    @property
    def list_external_access_rules(
        self,
    ) -> Callable[
        [vmwareengine.ListExternalAccessRulesRequest],
        vmwareengine.ListExternalAccessRulesResponse,
    ]:
        r"""Return a callable for the list external access rules method over gRPC.

        Lists ``ExternalAccessRule`` resources in the specified network
        policy.

        Returns:
            Callable[[~.ListExternalAccessRulesRequest],
                    ~.ListExternalAccessRulesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_external_access_rules" not in self._stubs:
            self._stubs["list_external_access_rules"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.vmwareengine.v1.VmwareEngine/ListExternalAccessRules",
                    request_serializer=vmwareengine.ListExternalAccessRulesRequest.serialize,
                    response_deserializer=vmwareengine.ListExternalAccessRulesResponse.deserialize,
                )
            )
        return self._stubs["list_external_access_rules"]

    @property
    def get_external_access_rule(
        self,
    ) -> Callable[
        [vmwareengine.GetExternalAccessRuleRequest],
        vmwareengine_resources.ExternalAccessRule,
    ]:
        r"""Return a callable for the get external access rule method over gRPC.

        Gets details of a single external access rule.

        Returns:
            Callable[[~.GetExternalAccessRuleRequest],
                    ~.ExternalAccessRule]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_external_access_rule" not in self._stubs:
            self._stubs["get_external_access_rule"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/GetExternalAccessRule",
                request_serializer=vmwareengine.GetExternalAccessRuleRequest.serialize,
                response_deserializer=vmwareengine_resources.ExternalAccessRule.deserialize,
            )
        return self._stubs["get_external_access_rule"]

    @property
    def create_external_access_rule(
        self,
    ) -> Callable[
        [vmwareengine.CreateExternalAccessRuleRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the create external access rule method over gRPC.

        Creates a new external access rule in a given network
        policy.

        Returns:
            Callable[[~.CreateExternalAccessRuleRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_external_access_rule" not in self._stubs:
            self._stubs["create_external_access_rule"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.vmwareengine.v1.VmwareEngine/CreateExternalAccessRule",
                    request_serializer=vmwareengine.CreateExternalAccessRuleRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["create_external_access_rule"]

    @property
    def update_external_access_rule(
        self,
    ) -> Callable[
        [vmwareengine.UpdateExternalAccessRuleRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the update external access rule method over gRPC.

        Updates the parameters of a single external access rule. Only
        fields specified in ``update_mask`` are applied.

        Returns:
            Callable[[~.UpdateExternalAccessRuleRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_external_access_rule" not in self._stubs:
            self._stubs["update_external_access_rule"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.vmwareengine.v1.VmwareEngine/UpdateExternalAccessRule",
                    request_serializer=vmwareengine.UpdateExternalAccessRuleRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["update_external_access_rule"]

    @property
    def delete_external_access_rule(
        self,
    ) -> Callable[
        [vmwareengine.DeleteExternalAccessRuleRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the delete external access rule method over gRPC.

        Deletes a single external access rule.

        Returns:
            Callable[[~.DeleteExternalAccessRuleRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_external_access_rule" not in self._stubs:
            self._stubs["delete_external_access_rule"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.vmwareengine.v1.VmwareEngine/DeleteExternalAccessRule",
                    request_serializer=vmwareengine.DeleteExternalAccessRuleRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["delete_external_access_rule"]

    @property
    def list_logging_servers(
        self,
    ) -> Callable[
        [vmwareengine.ListLoggingServersRequest],
        vmwareengine.ListLoggingServersResponse,
    ]:
        r"""Return a callable for the list logging servers method over gRPC.

        Lists logging servers configured for a given private
        cloud.

        Returns:
            Callable[[~.ListLoggingServersRequest],
                    ~.ListLoggingServersResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_logging_servers" not in self._stubs:
            self._stubs["list_logging_servers"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/ListLoggingServers",
                request_serializer=vmwareengine.ListLoggingServersRequest.serialize,
                response_deserializer=vmwareengine.ListLoggingServersResponse.deserialize,
            )
        return self._stubs["list_logging_servers"]

    @property
    def get_logging_server(
        self,
    ) -> Callable[
        [vmwareengine.GetLoggingServerRequest], vmwareengine_resources.LoggingServer
    ]:
        r"""Return a callable for the get logging server method over gRPC.

        Gets details of a logging server.

        Returns:
            Callable[[~.GetLoggingServerRequest],
                    ~.LoggingServer]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_logging_server" not in self._stubs:
            self._stubs["get_logging_server"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/GetLoggingServer",
                request_serializer=vmwareengine.GetLoggingServerRequest.serialize,
                response_deserializer=vmwareengine_resources.LoggingServer.deserialize,
            )
        return self._stubs["get_logging_server"]

    @property
    def create_logging_server(
        self,
    ) -> Callable[[vmwareengine.CreateLoggingServerRequest], operations_pb2.Operation]:
        r"""Return a callable for the create logging server method over gRPC.

        Create a new logging server for a given private
        cloud.

        Returns:
            Callable[[~.CreateLoggingServerRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_logging_server" not in self._stubs:
            self._stubs["create_logging_server"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/CreateLoggingServer",
                request_serializer=vmwareengine.CreateLoggingServerRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_logging_server"]

    @property
    def update_logging_server(
        self,
    ) -> Callable[[vmwareengine.UpdateLoggingServerRequest], operations_pb2.Operation]:
        r"""Return a callable for the update logging server method over gRPC.

        Updates the parameters of a single logging server. Only fields
        specified in ``update_mask`` are applied.

        Returns:
            Callable[[~.UpdateLoggingServerRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_logging_server" not in self._stubs:
            self._stubs["update_logging_server"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/UpdateLoggingServer",
                request_serializer=vmwareengine.UpdateLoggingServerRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_logging_server"]

    @property
    def delete_logging_server(
        self,
    ) -> Callable[[vmwareengine.DeleteLoggingServerRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete logging server method over gRPC.

        Deletes a single logging server.

        Returns:
            Callable[[~.DeleteLoggingServerRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_logging_server" not in self._stubs:
            self._stubs["delete_logging_server"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/DeleteLoggingServer",
                request_serializer=vmwareengine.DeleteLoggingServerRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_logging_server"]

    @property
    def list_node_types(
        self,
    ) -> Callable[
        [vmwareengine.ListNodeTypesRequest], vmwareengine.ListNodeTypesResponse
    ]:
        r"""Return a callable for the list node types method over gRPC.

        Lists node types

        Returns:
            Callable[[~.ListNodeTypesRequest],
                    ~.ListNodeTypesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_node_types" not in self._stubs:
            self._stubs["list_node_types"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/ListNodeTypes",
                request_serializer=vmwareengine.ListNodeTypesRequest.serialize,
                response_deserializer=vmwareengine.ListNodeTypesResponse.deserialize,
            )
        return self._stubs["list_node_types"]

    @property
    def get_node_type(
        self,
    ) -> Callable[[vmwareengine.GetNodeTypeRequest], vmwareengine_resources.NodeType]:
        r"""Return a callable for the get node type method over gRPC.

        Gets details of a single ``NodeType``.

        Returns:
            Callable[[~.GetNodeTypeRequest],
                    ~.NodeType]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_node_type" not in self._stubs:
            self._stubs["get_node_type"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/GetNodeType",
                request_serializer=vmwareengine.GetNodeTypeRequest.serialize,
                response_deserializer=vmwareengine_resources.NodeType.deserialize,
            )
        return self._stubs["get_node_type"]

    @property
    def show_nsx_credentials(
        self,
    ) -> Callable[
        [vmwareengine.ShowNsxCredentialsRequest], vmwareengine_resources.Credentials
    ]:
        r"""Return a callable for the show nsx credentials method over gRPC.

        Gets details of credentials for NSX appliance.

        Returns:
            Callable[[~.ShowNsxCredentialsRequest],
                    ~.Credentials]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "show_nsx_credentials" not in self._stubs:
            self._stubs["show_nsx_credentials"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/ShowNsxCredentials",
                request_serializer=vmwareengine.ShowNsxCredentialsRequest.serialize,
                response_deserializer=vmwareengine_resources.Credentials.deserialize,
            )
        return self._stubs["show_nsx_credentials"]

    @property
    def show_vcenter_credentials(
        self,
    ) -> Callable[
        [vmwareengine.ShowVcenterCredentialsRequest], vmwareengine_resources.Credentials
    ]:
        r"""Return a callable for the show vcenter credentials method over gRPC.

        Gets details of credentials for Vcenter appliance.

        Returns:
            Callable[[~.ShowVcenterCredentialsRequest],
                    ~.Credentials]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "show_vcenter_credentials" not in self._stubs:
            self._stubs["show_vcenter_credentials"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/ShowVcenterCredentials",
                request_serializer=vmwareengine.ShowVcenterCredentialsRequest.serialize,
                response_deserializer=vmwareengine_resources.Credentials.deserialize,
            )
        return self._stubs["show_vcenter_credentials"]

    @property
    def reset_nsx_credentials(
        self,
    ) -> Callable[[vmwareengine.ResetNsxCredentialsRequest], operations_pb2.Operation]:
        r"""Return a callable for the reset nsx credentials method over gRPC.

        Resets credentials of the NSX appliance.

        Returns:
            Callable[[~.ResetNsxCredentialsRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "reset_nsx_credentials" not in self._stubs:
            self._stubs["reset_nsx_credentials"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/ResetNsxCredentials",
                request_serializer=vmwareengine.ResetNsxCredentialsRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["reset_nsx_credentials"]

    @property
    def reset_vcenter_credentials(
        self,
    ) -> Callable[
        [vmwareengine.ResetVcenterCredentialsRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the reset vcenter credentials method over gRPC.

        Resets credentials of the Vcenter appliance.

        Returns:
            Callable[[~.ResetVcenterCredentialsRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "reset_vcenter_credentials" not in self._stubs:
            self._stubs["reset_vcenter_credentials"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/ResetVcenterCredentials",
                request_serializer=vmwareengine.ResetVcenterCredentialsRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["reset_vcenter_credentials"]

    @property
    def get_dns_forwarding(
        self,
    ) -> Callable[
        [vmwareengine.GetDnsForwardingRequest], vmwareengine_resources.DnsForwarding
    ]:
        r"""Return a callable for the get dns forwarding method over gRPC.

        Gets details of the ``DnsForwarding`` config.

        Returns:
            Callable[[~.GetDnsForwardingRequest],
                    ~.DnsForwarding]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_dns_forwarding" not in self._stubs:
            self._stubs["get_dns_forwarding"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/GetDnsForwarding",
                request_serializer=vmwareengine.GetDnsForwardingRequest.serialize,
                response_deserializer=vmwareengine_resources.DnsForwarding.deserialize,
            )
        return self._stubs["get_dns_forwarding"]

    @property
    def update_dns_forwarding(
        self,
    ) -> Callable[[vmwareengine.UpdateDnsForwardingRequest], operations_pb2.Operation]:
        r"""Return a callable for the update dns forwarding method over gRPC.

        Updates the parameters of the ``DnsForwarding`` config, like
        associated domains. Only fields specified in ``update_mask`` are
        applied.

        Returns:
            Callable[[~.UpdateDnsForwardingRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_dns_forwarding" not in self._stubs:
            self._stubs["update_dns_forwarding"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/UpdateDnsForwarding",
                request_serializer=vmwareengine.UpdateDnsForwardingRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_dns_forwarding"]

    @property
    def get_network_peering(
        self,
    ) -> Callable[
        [vmwareengine.GetNetworkPeeringRequest], vmwareengine_resources.NetworkPeering
    ]:
        r"""Return a callable for the get network peering method over gRPC.

        Retrieves a ``NetworkPeering`` resource by its resource name.
        The resource contains details of the network peering, such as
        peered networks, import and export custom route configurations,
        and peering state. NetworkPeering is a global resource and
        location can only be global.

        Returns:
            Callable[[~.GetNetworkPeeringRequest],
                    ~.NetworkPeering]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_network_peering" not in self._stubs:
            self._stubs["get_network_peering"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/GetNetworkPeering",
                request_serializer=vmwareengine.GetNetworkPeeringRequest.serialize,
                response_deserializer=vmwareengine_resources.NetworkPeering.deserialize,
            )
        return self._stubs["get_network_peering"]

    @property
    def list_network_peerings(
        self,
    ) -> Callable[
        [vmwareengine.ListNetworkPeeringsRequest],
        vmwareengine.ListNetworkPeeringsResponse,
    ]:
        r"""Return a callable for the list network peerings method over gRPC.

        Lists ``NetworkPeering`` resources in a given project.
        NetworkPeering is a global resource and location can only be
        global.

        Returns:
            Callable[[~.ListNetworkPeeringsRequest],
                    ~.ListNetworkPeeringsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_network_peerings" not in self._stubs:
            self._stubs["list_network_peerings"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/ListNetworkPeerings",
                request_serializer=vmwareengine.ListNetworkPeeringsRequest.serialize,
                response_deserializer=vmwareengine.ListNetworkPeeringsResponse.deserialize,
            )
        return self._stubs["list_network_peerings"]

    @property
    def create_network_peering(
        self,
    ) -> Callable[[vmwareengine.CreateNetworkPeeringRequest], operations_pb2.Operation]:
        r"""Return a callable for the create network peering method over gRPC.

        Creates a new network peering between the peer network and
        VMware Engine network provided in a ``NetworkPeering`` resource.
        NetworkPeering is a global resource and location can only be
        global.

        Returns:
            Callable[[~.CreateNetworkPeeringRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_network_peering" not in self._stubs:
            self._stubs["create_network_peering"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/CreateNetworkPeering",
                request_serializer=vmwareengine.CreateNetworkPeeringRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_network_peering"]

    @property
    def delete_network_peering(
        self,
    ) -> Callable[[vmwareengine.DeleteNetworkPeeringRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete network peering method over gRPC.

        Deletes a ``NetworkPeering`` resource. When a network peering is
        deleted for a VMware Engine network, the peer network becomes
        inaccessible to that VMware Engine network. NetworkPeering is a
        global resource and location can only be global.

        Returns:
            Callable[[~.DeleteNetworkPeeringRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_network_peering" not in self._stubs:
            self._stubs["delete_network_peering"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/DeleteNetworkPeering",
                request_serializer=vmwareengine.DeleteNetworkPeeringRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_network_peering"]

    @property
    def update_network_peering(
        self,
    ) -> Callable[[vmwareengine.UpdateNetworkPeeringRequest], operations_pb2.Operation]:
        r"""Return a callable for the update network peering method over gRPC.

        Modifies a ``NetworkPeering`` resource. Only the ``description``
        field can be updated. Only fields specified in ``updateMask``
        are applied. NetworkPeering is a global resource and location
        can only be global.

        Returns:
            Callable[[~.UpdateNetworkPeeringRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_network_peering" not in self._stubs:
            self._stubs["update_network_peering"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/UpdateNetworkPeering",
                request_serializer=vmwareengine.UpdateNetworkPeeringRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_network_peering"]

    @property
    def list_peering_routes(
        self,
    ) -> Callable[
        [vmwareengine.ListPeeringRoutesRequest], vmwareengine.ListPeeringRoutesResponse
    ]:
        r"""Return a callable for the list peering routes method over gRPC.

        Lists the network peering routes exchanged over a
        peering connection. NetworkPeering is a global resource
        and location can only be global.

        Returns:
            Callable[[~.ListPeeringRoutesRequest],
                    ~.ListPeeringRoutesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_peering_routes" not in self._stubs:
            self._stubs["list_peering_routes"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/ListPeeringRoutes",
                request_serializer=vmwareengine.ListPeeringRoutesRequest.serialize,
                response_deserializer=vmwareengine.ListPeeringRoutesResponse.deserialize,
            )
        return self._stubs["list_peering_routes"]

    @property
    def create_hcx_activation_key(
        self,
    ) -> Callable[
        [vmwareengine.CreateHcxActivationKeyRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the create hcx activation key method over gRPC.

        Creates a new HCX activation key in a given private
        cloud.

        Returns:
            Callable[[~.CreateHcxActivationKeyRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_hcx_activation_key" not in self._stubs:
            self._stubs["create_hcx_activation_key"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/CreateHcxActivationKey",
                request_serializer=vmwareengine.CreateHcxActivationKeyRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_hcx_activation_key"]

    @property
    def list_hcx_activation_keys(
        self,
    ) -> Callable[
        [vmwareengine.ListHcxActivationKeysRequest],
        vmwareengine.ListHcxActivationKeysResponse,
    ]:
        r"""Return a callable for the list hcx activation keys method over gRPC.

        Lists ``HcxActivationKey`` resources in a given private cloud.

        Returns:
            Callable[[~.ListHcxActivationKeysRequest],
                    ~.ListHcxActivationKeysResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_hcx_activation_keys" not in self._stubs:
            self._stubs["list_hcx_activation_keys"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/ListHcxActivationKeys",
                request_serializer=vmwareengine.ListHcxActivationKeysRequest.serialize,
                response_deserializer=vmwareengine.ListHcxActivationKeysResponse.deserialize,
            )
        return self._stubs["list_hcx_activation_keys"]

    @property
    def get_hcx_activation_key(
        self,
    ) -> Callable[
        [vmwareengine.GetHcxActivationKeyRequest],
        vmwareengine_resources.HcxActivationKey,
    ]:
        r"""Return a callable for the get hcx activation key method over gRPC.

        Retrieves a ``HcxActivationKey`` resource by its resource name.

        Returns:
            Callable[[~.GetHcxActivationKeyRequest],
                    ~.HcxActivationKey]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_hcx_activation_key" not in self._stubs:
            self._stubs["get_hcx_activation_key"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/GetHcxActivationKey",
                request_serializer=vmwareengine.GetHcxActivationKeyRequest.serialize,
                response_deserializer=vmwareengine_resources.HcxActivationKey.deserialize,
            )
        return self._stubs["get_hcx_activation_key"]

    @property
    def get_network_policy(
        self,
    ) -> Callable[
        [vmwareengine.GetNetworkPolicyRequest], vmwareengine_resources.NetworkPolicy
    ]:
        r"""Return a callable for the get network policy method over gRPC.

        Retrieves a ``NetworkPolicy`` resource by its resource name.

        Returns:
            Callable[[~.GetNetworkPolicyRequest],
                    ~.NetworkPolicy]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_network_policy" not in self._stubs:
            self._stubs["get_network_policy"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/GetNetworkPolicy",
                request_serializer=vmwareengine.GetNetworkPolicyRequest.serialize,
                response_deserializer=vmwareengine_resources.NetworkPolicy.deserialize,
            )
        return self._stubs["get_network_policy"]

    @property
    def list_network_policies(
        self,
    ) -> Callable[
        [vmwareengine.ListNetworkPoliciesRequest],
        vmwareengine.ListNetworkPoliciesResponse,
    ]:
        r"""Return a callable for the list network policies method over gRPC.

        Lists ``NetworkPolicy`` resources in a specified project and
        location.

        Returns:
            Callable[[~.ListNetworkPoliciesRequest],
                    ~.ListNetworkPoliciesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_network_policies" not in self._stubs:
            self._stubs["list_network_policies"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/ListNetworkPolicies",
                request_serializer=vmwareengine.ListNetworkPoliciesRequest.serialize,
                response_deserializer=vmwareengine.ListNetworkPoliciesResponse.deserialize,
            )
        return self._stubs["list_network_policies"]

    @property
    def create_network_policy(
        self,
    ) -> Callable[[vmwareengine.CreateNetworkPolicyRequest], operations_pb2.Operation]:
        r"""Return a callable for the create network policy method over gRPC.

        Creates a new network policy in a given VMware Engine
        network of a project and location (region). A new
        network policy cannot be created if another network
        policy already exists in the same scope.

        Returns:
            Callable[[~.CreateNetworkPolicyRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_network_policy" not in self._stubs:
            self._stubs["create_network_policy"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/CreateNetworkPolicy",
                request_serializer=vmwareengine.CreateNetworkPolicyRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_network_policy"]

    @property
    def update_network_policy(
        self,
    ) -> Callable[[vmwareengine.UpdateNetworkPolicyRequest], operations_pb2.Operation]:
        r"""Return a callable for the update network policy method over gRPC.

        Modifies a ``NetworkPolicy`` resource. Only the following fields
        can be updated: ``internet_access``, ``external_ip``,
        ``edge_services_cidr``. Only fields specified in ``updateMask``
        are applied. When updating a network policy, the external IP
        network service can only be disabled if there are no external IP
        addresses present in the scope of the policy. Also, a
        ``NetworkService`` cannot be updated when
        ``NetworkService.state`` is set to ``RECONCILING``.

        During operation processing, the resource is temporarily in the
        ``ACTIVE`` state before the operation fully completes. For that
        period of time, you can't update the resource. Use the operation
        status to determine when the processing fully completes.

        Returns:
            Callable[[~.UpdateNetworkPolicyRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_network_policy" not in self._stubs:
            self._stubs["update_network_policy"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/UpdateNetworkPolicy",
                request_serializer=vmwareengine.UpdateNetworkPolicyRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_network_policy"]

    @property
    def delete_network_policy(
        self,
    ) -> Callable[[vmwareengine.DeleteNetworkPolicyRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete network policy method over gRPC.

        Deletes a ``NetworkPolicy`` resource. A network policy cannot be
        deleted when ``NetworkService.state`` is set to ``RECONCILING``
        for either its external IP or internet access service.

        Returns:
            Callable[[~.DeleteNetworkPolicyRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_network_policy" not in self._stubs:
            self._stubs["delete_network_policy"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/DeleteNetworkPolicy",
                request_serializer=vmwareengine.DeleteNetworkPolicyRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_network_policy"]

    @property
    def list_management_dns_zone_bindings(
        self,
    ) -> Callable[
        [vmwareengine.ListManagementDnsZoneBindingsRequest],
        vmwareengine.ListManagementDnsZoneBindingsResponse,
    ]:
        r"""Return a callable for the list management dns zone
        bindings method over gRPC.

        Lists Consumer VPCs bound to Management DNS Zone of a
        given private cloud.

        Returns:
            Callable[[~.ListManagementDnsZoneBindingsRequest],
                    ~.ListManagementDnsZoneBindingsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_management_dns_zone_bindings" not in self._stubs:
            self._stubs["list_management_dns_zone_bindings"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.vmwareengine.v1.VmwareEngine/ListManagementDnsZoneBindings",
                    request_serializer=vmwareengine.ListManagementDnsZoneBindingsRequest.serialize,
                    response_deserializer=vmwareengine.ListManagementDnsZoneBindingsResponse.deserialize,
                )
            )
        return self._stubs["list_management_dns_zone_bindings"]

    @property
    def get_management_dns_zone_binding(
        self,
    ) -> Callable[
        [vmwareengine.GetManagementDnsZoneBindingRequest],
        vmwareengine_resources.ManagementDnsZoneBinding,
    ]:
        r"""Return a callable for the get management dns zone
        binding method over gRPC.

        Retrieves a 'ManagementDnsZoneBinding' resource by
        its resource name.

        Returns:
            Callable[[~.GetManagementDnsZoneBindingRequest],
                    ~.ManagementDnsZoneBinding]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_management_dns_zone_binding" not in self._stubs:
            self._stubs["get_management_dns_zone_binding"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.vmwareengine.v1.VmwareEngine/GetManagementDnsZoneBinding",
                    request_serializer=vmwareengine.GetManagementDnsZoneBindingRequest.serialize,
                    response_deserializer=vmwareengine_resources.ManagementDnsZoneBinding.deserialize,
                )
            )
        return self._stubs["get_management_dns_zone_binding"]

    @property
    def create_management_dns_zone_binding(
        self,
    ) -> Callable[
        [vmwareengine.CreateManagementDnsZoneBindingRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the create management dns zone
        binding method over gRPC.

        Creates a new ``ManagementDnsZoneBinding`` resource in a private
        cloud. This RPC creates the DNS binding and the resource that
        represents the DNS binding of the consumer VPC network to the
        management DNS zone. A management DNS zone is the Cloud DNS
        cross-project binding zone that VMware Engine creates for each
        private cloud. It contains FQDNs and corresponding IP addresses
        for the private cloud's ESXi hosts and management VM appliances
        like vCenter and NSX Manager.

        Returns:
            Callable[[~.CreateManagementDnsZoneBindingRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_management_dns_zone_binding" not in self._stubs:
            self._stubs["create_management_dns_zone_binding"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.vmwareengine.v1.VmwareEngine/CreateManagementDnsZoneBinding",
                    request_serializer=vmwareengine.CreateManagementDnsZoneBindingRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["create_management_dns_zone_binding"]

    @property
    def update_management_dns_zone_binding(
        self,
    ) -> Callable[
        [vmwareengine.UpdateManagementDnsZoneBindingRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the update management dns zone
        binding method over gRPC.

        Updates a ``ManagementDnsZoneBinding`` resource. Only fields
        specified in ``update_mask`` are applied.

        Returns:
            Callable[[~.UpdateManagementDnsZoneBindingRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_management_dns_zone_binding" not in self._stubs:
            self._stubs["update_management_dns_zone_binding"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.vmwareengine.v1.VmwareEngine/UpdateManagementDnsZoneBinding",
                    request_serializer=vmwareengine.UpdateManagementDnsZoneBindingRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["update_management_dns_zone_binding"]

    @property
    def delete_management_dns_zone_binding(
        self,
    ) -> Callable[
        [vmwareengine.DeleteManagementDnsZoneBindingRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the delete management dns zone
        binding method over gRPC.

        Deletes a ``ManagementDnsZoneBinding`` resource. When a
        management DNS zone binding is deleted, the corresponding
        consumer VPC network is no longer bound to the management DNS
        zone.

        Returns:
            Callable[[~.DeleteManagementDnsZoneBindingRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_management_dns_zone_binding" not in self._stubs:
            self._stubs["delete_management_dns_zone_binding"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.vmwareengine.v1.VmwareEngine/DeleteManagementDnsZoneBinding",
                    request_serializer=vmwareengine.DeleteManagementDnsZoneBindingRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["delete_management_dns_zone_binding"]

    @property
    def repair_management_dns_zone_binding(
        self,
    ) -> Callable[
        [vmwareengine.RepairManagementDnsZoneBindingRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the repair management dns zone
        binding method over gRPC.

        Retries to create a ``ManagementDnsZoneBinding`` resource that
        is in failed state.

        Returns:
            Callable[[~.RepairManagementDnsZoneBindingRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "repair_management_dns_zone_binding" not in self._stubs:
            self._stubs["repair_management_dns_zone_binding"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.vmwareengine.v1.VmwareEngine/RepairManagementDnsZoneBinding",
                    request_serializer=vmwareengine.RepairManagementDnsZoneBindingRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["repair_management_dns_zone_binding"]

    @property
    def create_vmware_engine_network(
        self,
    ) -> Callable[
        [vmwareengine.CreateVmwareEngineNetworkRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the create vmware engine network method over gRPC.

        Creates a new VMware Engine network that can be used
        by a private cloud.

        Returns:
            Callable[[~.CreateVmwareEngineNetworkRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_vmware_engine_network" not in self._stubs:
            self._stubs["create_vmware_engine_network"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.vmwareengine.v1.VmwareEngine/CreateVmwareEngineNetwork",
                    request_serializer=vmwareengine.CreateVmwareEngineNetworkRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["create_vmware_engine_network"]

    @property
    def update_vmware_engine_network(
        self,
    ) -> Callable[
        [vmwareengine.UpdateVmwareEngineNetworkRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the update vmware engine network method over gRPC.

        Modifies a VMware Engine network resource. Only the following
        fields can be updated: ``description``. Only fields specified in
        ``updateMask`` are applied.

        Returns:
            Callable[[~.UpdateVmwareEngineNetworkRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_vmware_engine_network" not in self._stubs:
            self._stubs["update_vmware_engine_network"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.vmwareengine.v1.VmwareEngine/UpdateVmwareEngineNetwork",
                    request_serializer=vmwareengine.UpdateVmwareEngineNetworkRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["update_vmware_engine_network"]

    @property
    def delete_vmware_engine_network(
        self,
    ) -> Callable[
        [vmwareengine.DeleteVmwareEngineNetworkRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the delete vmware engine network method over gRPC.

        Deletes a ``VmwareEngineNetwork`` resource. You can only delete
        a VMware Engine network after all resources that refer to it are
        deleted. For example, a private cloud, a network peering, and a
        network policy can all refer to the same VMware Engine network.

        Returns:
            Callable[[~.DeleteVmwareEngineNetworkRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_vmware_engine_network" not in self._stubs:
            self._stubs["delete_vmware_engine_network"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.vmwareengine.v1.VmwareEngine/DeleteVmwareEngineNetwork",
                    request_serializer=vmwareengine.DeleteVmwareEngineNetworkRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["delete_vmware_engine_network"]

    @property
    def get_vmware_engine_network(
        self,
    ) -> Callable[
        [vmwareengine.GetVmwareEngineNetworkRequest],
        vmwareengine_resources.VmwareEngineNetwork,
    ]:
        r"""Return a callable for the get vmware engine network method over gRPC.

        Retrieves a ``VmwareEngineNetwork`` resource by its resource
        name. The resource contains details of the VMware Engine
        network, such as its VMware Engine network type, peered networks
        in a service project, and state (for example, ``CREATING``,
        ``ACTIVE``, ``DELETING``).

        Returns:
            Callable[[~.GetVmwareEngineNetworkRequest],
                    ~.VmwareEngineNetwork]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_vmware_engine_network" not in self._stubs:
            self._stubs["get_vmware_engine_network"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/GetVmwareEngineNetwork",
                request_serializer=vmwareengine.GetVmwareEngineNetworkRequest.serialize,
                response_deserializer=vmwareengine_resources.VmwareEngineNetwork.deserialize,
            )
        return self._stubs["get_vmware_engine_network"]

    @property
    def list_vmware_engine_networks(
        self,
    ) -> Callable[
        [vmwareengine.ListVmwareEngineNetworksRequest],
        vmwareengine.ListVmwareEngineNetworksResponse,
    ]:
        r"""Return a callable for the list vmware engine networks method over gRPC.

        Lists ``VmwareEngineNetwork`` resources in a given project and
        location.

        Returns:
            Callable[[~.ListVmwareEngineNetworksRequest],
                    ~.ListVmwareEngineNetworksResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_vmware_engine_networks" not in self._stubs:
            self._stubs["list_vmware_engine_networks"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.vmwareengine.v1.VmwareEngine/ListVmwareEngineNetworks",
                    request_serializer=vmwareengine.ListVmwareEngineNetworksRequest.serialize,
                    response_deserializer=vmwareengine.ListVmwareEngineNetworksResponse.deserialize,
                )
            )
        return self._stubs["list_vmware_engine_networks"]

    @property
    def create_private_connection(
        self,
    ) -> Callable[
        [vmwareengine.CreatePrivateConnectionRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the create private connection method over gRPC.

        Creates a new private connection that can be used for
        accessing private Clouds.

        Returns:
            Callable[[~.CreatePrivateConnectionRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_private_connection" not in self._stubs:
            self._stubs["create_private_connection"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/CreatePrivateConnection",
                request_serializer=vmwareengine.CreatePrivateConnectionRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_private_connection"]

    @property
    def get_private_connection(
        self,
    ) -> Callable[
        [vmwareengine.GetPrivateConnectionRequest],
        vmwareengine_resources.PrivateConnection,
    ]:
        r"""Return a callable for the get private connection method over gRPC.

        Retrieves a ``PrivateConnection`` resource by its resource name.
        The resource contains details of the private connection, such as
        connected network, routing mode and state.

        Returns:
            Callable[[~.GetPrivateConnectionRequest],
                    ~.PrivateConnection]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_private_connection" not in self._stubs:
            self._stubs["get_private_connection"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/GetPrivateConnection",
                request_serializer=vmwareengine.GetPrivateConnectionRequest.serialize,
                response_deserializer=vmwareengine_resources.PrivateConnection.deserialize,
            )
        return self._stubs["get_private_connection"]

    @property
    def list_private_connections(
        self,
    ) -> Callable[
        [vmwareengine.ListPrivateConnectionsRequest],
        vmwareengine.ListPrivateConnectionsResponse,
    ]:
        r"""Return a callable for the list private connections method over gRPC.

        Lists ``PrivateConnection`` resources in a given project and
        location.

        Returns:
            Callable[[~.ListPrivateConnectionsRequest],
                    ~.ListPrivateConnectionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_private_connections" not in self._stubs:
            self._stubs["list_private_connections"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/ListPrivateConnections",
                request_serializer=vmwareengine.ListPrivateConnectionsRequest.serialize,
                response_deserializer=vmwareengine.ListPrivateConnectionsResponse.deserialize,
            )
        return self._stubs["list_private_connections"]

    @property
    def update_private_connection(
        self,
    ) -> Callable[
        [vmwareengine.UpdatePrivateConnectionRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the update private connection method over gRPC.

        Modifies a ``PrivateConnection`` resource. Only ``description``
        and ``routing_mode`` fields can be updated. Only fields
        specified in ``updateMask`` are applied.

        Returns:
            Callable[[~.UpdatePrivateConnectionRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_private_connection" not in self._stubs:
            self._stubs["update_private_connection"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/UpdatePrivateConnection",
                request_serializer=vmwareengine.UpdatePrivateConnectionRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_private_connection"]

    @property
    def delete_private_connection(
        self,
    ) -> Callable[
        [vmwareengine.DeletePrivateConnectionRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the delete private connection method over gRPC.

        Deletes a ``PrivateConnection`` resource. When a private
        connection is deleted for a VMware Engine network, the connected
        network becomes inaccessible to that VMware Engine network.

        Returns:
            Callable[[~.DeletePrivateConnectionRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_private_connection" not in self._stubs:
            self._stubs["delete_private_connection"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/DeletePrivateConnection",
                request_serializer=vmwareengine.DeletePrivateConnectionRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_private_connection"]

    @property
    def list_private_connection_peering_routes(
        self,
    ) -> Callable[
        [vmwareengine.ListPrivateConnectionPeeringRoutesRequest],
        vmwareengine.ListPrivateConnectionPeeringRoutesResponse,
    ]:
        r"""Return a callable for the list private connection
        peering routes method over gRPC.

        Lists the private connection routes exchanged over a
        peering connection.

        Returns:
            Callable[[~.ListPrivateConnectionPeeringRoutesRequest],
                    ~.ListPrivateConnectionPeeringRoutesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_private_connection_peering_routes" not in self._stubs:
            self._stubs["list_private_connection_peering_routes"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.vmwareengine.v1.VmwareEngine/ListPrivateConnectionPeeringRoutes",
                    request_serializer=vmwareengine.ListPrivateConnectionPeeringRoutesRequest.serialize,
                    response_deserializer=vmwareengine.ListPrivateConnectionPeeringRoutesResponse.deserialize,
                )
            )
        return self._stubs["list_private_connection_peering_routes"]

    @property
    def grant_dns_bind_permission(
        self,
    ) -> Callable[
        [vmwareengine.GrantDnsBindPermissionRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the grant dns bind permission method over gRPC.

        Grants the bind permission to the customer provided
        principal(user / service account) to bind their DNS zone
        with the intranet VPC associated with the project.
        DnsBindPermission is a global resource and location can
        only be global.

        Returns:
            Callable[[~.GrantDnsBindPermissionRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "grant_dns_bind_permission" not in self._stubs:
            self._stubs["grant_dns_bind_permission"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/GrantDnsBindPermission",
                request_serializer=vmwareengine.GrantDnsBindPermissionRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["grant_dns_bind_permission"]

    @property
    def get_dns_bind_permission(
        self,
    ) -> Callable[
        [vmwareengine.GetDnsBindPermissionRequest],
        vmwareengine_resources.DnsBindPermission,
    ]:
        r"""Return a callable for the get dns bind permission method over gRPC.

        Gets all the principals having bind permission on the
        intranet VPC associated with the consumer project
        granted by the Grant API. DnsBindPermission is a global
        resource and location can only be global.

        Returns:
            Callable[[~.GetDnsBindPermissionRequest],
                    ~.DnsBindPermission]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_dns_bind_permission" not in self._stubs:
            self._stubs["get_dns_bind_permission"] = self._logged_channel.unary_unary(
                "/google.cloud.vmwareengine.v1.VmwareEngine/GetDnsBindPermission",
                request_serializer=vmwareengine.GetDnsBindPermissionRequest.serialize,
                response_deserializer=vmwareengine_resources.DnsBindPermission.deserialize,
            )
        return self._stubs["get_dns_bind_permission"]

    @property
    def revoke_dns_bind_permission(
        self,
    ) -> Callable[
        [vmwareengine.RevokeDnsBindPermissionRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the revoke dns bind permission method over gRPC.

        Revokes the bind permission from the customer
        provided principal(user / service account) on the
        intranet VPC associated with the consumer project.
        DnsBindPermission is a global resource and location can
        only be global.

        Returns:
            Callable[[~.RevokeDnsBindPermissionRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "revoke_dns_bind_permission" not in self._stubs:
            self._stubs["revoke_dns_bind_permission"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.vmwareengine.v1.VmwareEngine/RevokeDnsBindPermission",
                    request_serializer=vmwareengine.RevokeDnsBindPermissionRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["revoke_dns_bind_permission"]

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
    def set_iam_policy(
        self,
    ) -> Callable[[iam_policy_pb2.SetIamPolicyRequest], policy_pb2.Policy]:
        r"""Return a callable for the set iam policy method over gRPC.
        Sets the IAM access control policy on the specified
        function. Replaces any existing policy.
        Returns:
            Callable[[~.SetIamPolicyRequest],
                    ~.Policy]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "set_iam_policy" not in self._stubs:
            self._stubs["set_iam_policy"] = self._logged_channel.unary_unary(
                "/google.iam.v1.IAMPolicy/SetIamPolicy",
                request_serializer=iam_policy_pb2.SetIamPolicyRequest.SerializeToString,
                response_deserializer=policy_pb2.Policy.FromString,
            )
        return self._stubs["set_iam_policy"]

    @property
    def get_iam_policy(
        self,
    ) -> Callable[[iam_policy_pb2.GetIamPolicyRequest], policy_pb2.Policy]:
        r"""Return a callable for the get iam policy method over gRPC.
        Gets the IAM access control policy for a function.
        Returns an empty policy if the function exists and does
        not have a policy set.
        Returns:
            Callable[[~.GetIamPolicyRequest],
                    ~.Policy]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_iam_policy" not in self._stubs:
            self._stubs["get_iam_policy"] = self._logged_channel.unary_unary(
                "/google.iam.v1.IAMPolicy/GetIamPolicy",
                request_serializer=iam_policy_pb2.GetIamPolicyRequest.SerializeToString,
                response_deserializer=policy_pb2.Policy.FromString,
            )
        return self._stubs["get_iam_policy"]

    @property
    def test_iam_permissions(
        self,
    ) -> Callable[
        [iam_policy_pb2.TestIamPermissionsRequest],
        iam_policy_pb2.TestIamPermissionsResponse,
    ]:
        r"""Return a callable for the test iam permissions method over gRPC.
        Tests the specified permissions against the IAM access control
        policy for a function. If the function does not exist, this will
        return an empty set of permissions, not a NOT_FOUND error.
        Returns:
            Callable[[~.TestIamPermissionsRequest],
                    ~.TestIamPermissionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "test_iam_permissions" not in self._stubs:
            self._stubs["test_iam_permissions"] = self._logged_channel.unary_unary(
                "/google.iam.v1.IAMPolicy/TestIamPermissions",
                request_serializer=iam_policy_pb2.TestIamPermissionsRequest.SerializeToString,
                response_deserializer=iam_policy_pb2.TestIamPermissionsResponse.FromString,
            )
        return self._stubs["test_iam_permissions"]

    @property
    def kind(self) -> str:
        return "grpc"


__all__ = ("VmwareEngineGrpcTransport",)
