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

from google.cloud.netapp_v1.types import (
    active_directory,
    backup,
    backup_policy,
    backup_vault,
    host_group,
    kms,
    ontap,
    quota_rule,
    replication,
    snapshot,
    storage_pool,
    volume,
)
from google.cloud.netapp_v1.types import active_directory as gcn_active_directory
from google.cloud.netapp_v1.types import backup as gcn_backup
from google.cloud.netapp_v1.types import backup_policy as gcn_backup_policy
from google.cloud.netapp_v1.types import backup_vault as gcn_backup_vault
from google.cloud.netapp_v1.types import host_group as gcn_host_group
from google.cloud.netapp_v1.types import quota_rule as gcn_quota_rule
from google.cloud.netapp_v1.types import replication as gcn_replication
from google.cloud.netapp_v1.types import snapshot as gcn_snapshot
from google.cloud.netapp_v1.types import storage_pool as gcn_storage_pool
from google.cloud.netapp_v1.types import volume as gcn_volume

from .base import DEFAULT_CLIENT_INFO, NetAppTransport
from .grpc import NetAppGrpcTransport

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
                    "serviceName": "google.cloud.netapp.v1.NetApp",
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
                    "serviceName": "google.cloud.netapp.v1.NetApp",
                    "rpcName": str(client_call_details.method),
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class NetAppGrpcAsyncIOTransport(NetAppTransport):
    """gRPC AsyncIO backend transport for NetApp.

    NetApp Files Google Cloud Service

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
        host: str = "netapp.googleapis.com",
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
        host: str = "netapp.googleapis.com",
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
                 The hostname to connect to (default: 'netapp.googleapis.com').
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
    def list_storage_pools(
        self,
    ) -> Callable[
        [storage_pool.ListStoragePoolsRequest],
        Awaitable[storage_pool.ListStoragePoolsResponse],
    ]:
        r"""Return a callable for the list storage pools method over gRPC.

        Returns descriptions of all storage pools owned by
        the caller.

        Returns:
            Callable[[~.ListStoragePoolsRequest],
                    Awaitable[~.ListStoragePoolsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_storage_pools" not in self._stubs:
            self._stubs["list_storage_pools"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/ListStoragePools",
                request_serializer=storage_pool.ListStoragePoolsRequest.serialize,
                response_deserializer=storage_pool.ListStoragePoolsResponse.deserialize,
            )
        return self._stubs["list_storage_pools"]

    @property
    def create_storage_pool(
        self,
    ) -> Callable[
        [gcn_storage_pool.CreateStoragePoolRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create storage pool method over gRPC.

        Creates a new storage pool.

        Returns:
            Callable[[~.CreateStoragePoolRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_storage_pool" not in self._stubs:
            self._stubs["create_storage_pool"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/CreateStoragePool",
                request_serializer=gcn_storage_pool.CreateStoragePoolRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_storage_pool"]

    @property
    def get_storage_pool(
        self,
    ) -> Callable[
        [storage_pool.GetStoragePoolRequest], Awaitable[storage_pool.StoragePool]
    ]:
        r"""Return a callable for the get storage pool method over gRPC.

        Returns the description of the specified storage pool
        by poolId.

        Returns:
            Callable[[~.GetStoragePoolRequest],
                    Awaitable[~.StoragePool]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_storage_pool" not in self._stubs:
            self._stubs["get_storage_pool"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/GetStoragePool",
                request_serializer=storage_pool.GetStoragePoolRequest.serialize,
                response_deserializer=storage_pool.StoragePool.deserialize,
            )
        return self._stubs["get_storage_pool"]

    @property
    def update_storage_pool(
        self,
    ) -> Callable[
        [gcn_storage_pool.UpdateStoragePoolRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update storage pool method over gRPC.

        Updates the storage pool properties with the full
        spec

        Returns:
            Callable[[~.UpdateStoragePoolRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_storage_pool" not in self._stubs:
            self._stubs["update_storage_pool"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/UpdateStoragePool",
                request_serializer=gcn_storage_pool.UpdateStoragePoolRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_storage_pool"]

    @property
    def delete_storage_pool(
        self,
    ) -> Callable[
        [storage_pool.DeleteStoragePoolRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the delete storage pool method over gRPC.

        Warning! This operation will permanently delete the
        storage pool.

        Returns:
            Callable[[~.DeleteStoragePoolRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_storage_pool" not in self._stubs:
            self._stubs["delete_storage_pool"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/DeleteStoragePool",
                request_serializer=storage_pool.DeleteStoragePoolRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_storage_pool"]

    @property
    def validate_directory_service(
        self,
    ) -> Callable[
        [storage_pool.ValidateDirectoryServiceRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the validate directory service method over gRPC.

        ValidateDirectoryService does a connectivity check
        for a directory service policy attached to the storage
        pool.

        Returns:
            Callable[[~.ValidateDirectoryServiceRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "validate_directory_service" not in self._stubs:
            self._stubs["validate_directory_service"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.netapp.v1.NetApp/ValidateDirectoryService",
                    request_serializer=storage_pool.ValidateDirectoryServiceRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["validate_directory_service"]

    @property
    def switch_active_replica_zone(
        self,
    ) -> Callable[
        [storage_pool.SwitchActiveReplicaZoneRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the switch active replica zone method over gRPC.

        This operation will switch the active/replica zone
        for a regional storagePool.

        Returns:
            Callable[[~.SwitchActiveReplicaZoneRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "switch_active_replica_zone" not in self._stubs:
            self._stubs["switch_active_replica_zone"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.netapp.v1.NetApp/SwitchActiveReplicaZone",
                    request_serializer=storage_pool.SwitchActiveReplicaZoneRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["switch_active_replica_zone"]

    @property
    def list_volumes(
        self,
    ) -> Callable[[volume.ListVolumesRequest], Awaitable[volume.ListVolumesResponse]]:
        r"""Return a callable for the list volumes method over gRPC.

        Lists Volumes in a given project.

        Returns:
            Callable[[~.ListVolumesRequest],
                    Awaitable[~.ListVolumesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_volumes" not in self._stubs:
            self._stubs["list_volumes"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/ListVolumes",
                request_serializer=volume.ListVolumesRequest.serialize,
                response_deserializer=volume.ListVolumesResponse.deserialize,
            )
        return self._stubs["list_volumes"]

    @property
    def get_volume(
        self,
    ) -> Callable[[volume.GetVolumeRequest], Awaitable[volume.Volume]]:
        r"""Return a callable for the get volume method over gRPC.

        Gets details of a single Volume.

        Returns:
            Callable[[~.GetVolumeRequest],
                    Awaitable[~.Volume]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_volume" not in self._stubs:
            self._stubs["get_volume"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/GetVolume",
                request_serializer=volume.GetVolumeRequest.serialize,
                response_deserializer=volume.Volume.deserialize,
            )
        return self._stubs["get_volume"]

    @property
    def create_volume(
        self,
    ) -> Callable[
        [gcn_volume.CreateVolumeRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create volume method over gRPC.

        Creates a new Volume in a given project and location.

        Returns:
            Callable[[~.CreateVolumeRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_volume" not in self._stubs:
            self._stubs["create_volume"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/CreateVolume",
                request_serializer=gcn_volume.CreateVolumeRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_volume"]

    @property
    def update_volume(
        self,
    ) -> Callable[
        [gcn_volume.UpdateVolumeRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update volume method over gRPC.

        Updates the parameters of a single Volume.

        Returns:
            Callable[[~.UpdateVolumeRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_volume" not in self._stubs:
            self._stubs["update_volume"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/UpdateVolume",
                request_serializer=gcn_volume.UpdateVolumeRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_volume"]

    @property
    def delete_volume(
        self,
    ) -> Callable[[volume.DeleteVolumeRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the delete volume method over gRPC.

        Deletes a single Volume.

        Returns:
            Callable[[~.DeleteVolumeRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_volume" not in self._stubs:
            self._stubs["delete_volume"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/DeleteVolume",
                request_serializer=volume.DeleteVolumeRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_volume"]

    @property
    def revert_volume(
        self,
    ) -> Callable[[volume.RevertVolumeRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the revert volume method over gRPC.

        Revert an existing volume to a specified snapshot.
        Warning! This operation will permanently revert all
        changes made after the snapshot was created.

        Returns:
            Callable[[~.RevertVolumeRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "revert_volume" not in self._stubs:
            self._stubs["revert_volume"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/RevertVolume",
                request_serializer=volume.RevertVolumeRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["revert_volume"]

    @property
    def start_split(
        self,
    ) -> Callable[[volume.StartSplitRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the start split method over gRPC.

        Splits a clone volume from its source volume. This operation
        will only work for volumes which have clone_details set(clones).
        For volumes that are not clones, this operation will return an
        error.

        Returns:
            Callable[[~.StartSplitRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "start_split" not in self._stubs:
            self._stubs["start_split"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/StartSplit",
                request_serializer=volume.StartSplitRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["start_split"]

    @property
    def get_split_status(
        self,
    ) -> Callable[[volume.GetSplitStatusRequest], Awaitable[volume.SplitStatus]]:
        r"""Return a callable for the get split status method over gRPC.

        Retrieves the current state, progress, and details of
        a split operation for a volume. This method is relevant
        when the volume is a clone. For volumes that are not
        clones, this method will return an error.

        Returns:
            Callable[[~.GetSplitStatusRequest],
                    Awaitable[~.SplitStatus]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_split_status" not in self._stubs:
            self._stubs["get_split_status"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/GetSplitStatus",
                request_serializer=volume.GetSplitStatusRequest.serialize,
                response_deserializer=volume.SplitStatus.deserialize,
            )
        return self._stubs["get_split_status"]

    @property
    def establish_volume_peering(
        self,
    ) -> Callable[
        [volume.EstablishVolumePeeringRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the establish volume peering method over gRPC.

        Establish volume peering. This is used to establish
        cluster and svm peerings between the GCNV and OnPrem
        clusters.

        Returns:
            Callable[[~.EstablishVolumePeeringRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "establish_volume_peering" not in self._stubs:
            self._stubs["establish_volume_peering"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/EstablishVolumePeering",
                request_serializer=volume.EstablishVolumePeeringRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["establish_volume_peering"]

    @property
    def list_snapshots(
        self,
    ) -> Callable[
        [snapshot.ListSnapshotsRequest], Awaitable[snapshot.ListSnapshotsResponse]
    ]:
        r"""Return a callable for the list snapshots method over gRPC.

        Returns descriptions of all snapshots for a volume.

        Returns:
            Callable[[~.ListSnapshotsRequest],
                    Awaitable[~.ListSnapshotsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_snapshots" not in self._stubs:
            self._stubs["list_snapshots"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/ListSnapshots",
                request_serializer=snapshot.ListSnapshotsRequest.serialize,
                response_deserializer=snapshot.ListSnapshotsResponse.deserialize,
            )
        return self._stubs["list_snapshots"]

    @property
    def get_snapshot(
        self,
    ) -> Callable[[snapshot.GetSnapshotRequest], Awaitable[snapshot.Snapshot]]:
        r"""Return a callable for the get snapshot method over gRPC.

        Describe a snapshot for a volume.

        Returns:
            Callable[[~.GetSnapshotRequest],
                    Awaitable[~.Snapshot]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_snapshot" not in self._stubs:
            self._stubs["get_snapshot"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/GetSnapshot",
                request_serializer=snapshot.GetSnapshotRequest.serialize,
                response_deserializer=snapshot.Snapshot.deserialize,
            )
        return self._stubs["get_snapshot"]

    @property
    def create_snapshot(
        self,
    ) -> Callable[
        [gcn_snapshot.CreateSnapshotRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create snapshot method over gRPC.

        Create a new snapshot for a volume.

        Returns:
            Callable[[~.CreateSnapshotRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_snapshot" not in self._stubs:
            self._stubs["create_snapshot"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/CreateSnapshot",
                request_serializer=gcn_snapshot.CreateSnapshotRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_snapshot"]

    @property
    def delete_snapshot(
        self,
    ) -> Callable[
        [snapshot.DeleteSnapshotRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the delete snapshot method over gRPC.

        Deletes a snapshot.

        Returns:
            Callable[[~.DeleteSnapshotRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_snapshot" not in self._stubs:
            self._stubs["delete_snapshot"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/DeleteSnapshot",
                request_serializer=snapshot.DeleteSnapshotRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_snapshot"]

    @property
    def update_snapshot(
        self,
    ) -> Callable[
        [gcn_snapshot.UpdateSnapshotRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update snapshot method over gRPC.

        Updates the settings of a specific snapshot.

        Returns:
            Callable[[~.UpdateSnapshotRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_snapshot" not in self._stubs:
            self._stubs["update_snapshot"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/UpdateSnapshot",
                request_serializer=gcn_snapshot.UpdateSnapshotRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_snapshot"]

    @property
    def list_active_directories(
        self,
    ) -> Callable[
        [active_directory.ListActiveDirectoriesRequest],
        Awaitable[active_directory.ListActiveDirectoriesResponse],
    ]:
        r"""Return a callable for the list active directories method over gRPC.

        Lists active directories.

        Returns:
            Callable[[~.ListActiveDirectoriesRequest],
                    Awaitable[~.ListActiveDirectoriesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_active_directories" not in self._stubs:
            self._stubs["list_active_directories"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/ListActiveDirectories",
                request_serializer=active_directory.ListActiveDirectoriesRequest.serialize,
                response_deserializer=active_directory.ListActiveDirectoriesResponse.deserialize,
            )
        return self._stubs["list_active_directories"]

    @property
    def get_active_directory(
        self,
    ) -> Callable[
        [active_directory.GetActiveDirectoryRequest],
        Awaitable[active_directory.ActiveDirectory],
    ]:
        r"""Return a callable for the get active directory method over gRPC.

        Describes a specified active directory.

        Returns:
            Callable[[~.GetActiveDirectoryRequest],
                    Awaitable[~.ActiveDirectory]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_active_directory" not in self._stubs:
            self._stubs["get_active_directory"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/GetActiveDirectory",
                request_serializer=active_directory.GetActiveDirectoryRequest.serialize,
                response_deserializer=active_directory.ActiveDirectory.deserialize,
            )
        return self._stubs["get_active_directory"]

    @property
    def create_active_directory(
        self,
    ) -> Callable[
        [gcn_active_directory.CreateActiveDirectoryRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the create active directory method over gRPC.

        CreateActiveDirectory
        Creates the active directory specified in the request.

        Returns:
            Callable[[~.CreateActiveDirectoryRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_active_directory" not in self._stubs:
            self._stubs["create_active_directory"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/CreateActiveDirectory",
                request_serializer=gcn_active_directory.CreateActiveDirectoryRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_active_directory"]

    @property
    def update_active_directory(
        self,
    ) -> Callable[
        [gcn_active_directory.UpdateActiveDirectoryRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the update active directory method over gRPC.

        Update the parameters of an active directories.

        Returns:
            Callable[[~.UpdateActiveDirectoryRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_active_directory" not in self._stubs:
            self._stubs["update_active_directory"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/UpdateActiveDirectory",
                request_serializer=gcn_active_directory.UpdateActiveDirectoryRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_active_directory"]

    @property
    def delete_active_directory(
        self,
    ) -> Callable[
        [active_directory.DeleteActiveDirectoryRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the delete active directory method over gRPC.

        Delete the active directory specified in the request.

        Returns:
            Callable[[~.DeleteActiveDirectoryRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_active_directory" not in self._stubs:
            self._stubs["delete_active_directory"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/DeleteActiveDirectory",
                request_serializer=active_directory.DeleteActiveDirectoryRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_active_directory"]

    @property
    def list_kms_configs(
        self,
    ) -> Callable[[kms.ListKmsConfigsRequest], Awaitable[kms.ListKmsConfigsResponse]]:
        r"""Return a callable for the list kms configs method over gRPC.

        Returns descriptions of all KMS configs owned by the
        caller.

        Returns:
            Callable[[~.ListKmsConfigsRequest],
                    Awaitable[~.ListKmsConfigsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_kms_configs" not in self._stubs:
            self._stubs["list_kms_configs"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/ListKmsConfigs",
                request_serializer=kms.ListKmsConfigsRequest.serialize,
                response_deserializer=kms.ListKmsConfigsResponse.deserialize,
            )
        return self._stubs["list_kms_configs"]

    @property
    def create_kms_config(
        self,
    ) -> Callable[[kms.CreateKmsConfigRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the create kms config method over gRPC.

        Creates a new KMS config.

        Returns:
            Callable[[~.CreateKmsConfigRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_kms_config" not in self._stubs:
            self._stubs["create_kms_config"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/CreateKmsConfig",
                request_serializer=kms.CreateKmsConfigRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_kms_config"]

    @property
    def get_kms_config(
        self,
    ) -> Callable[[kms.GetKmsConfigRequest], Awaitable[kms.KmsConfig]]:
        r"""Return a callable for the get kms config method over gRPC.

        Returns the description of the specified KMS config by
        kms_config_id.

        Returns:
            Callable[[~.GetKmsConfigRequest],
                    Awaitable[~.KmsConfig]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_kms_config" not in self._stubs:
            self._stubs["get_kms_config"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/GetKmsConfig",
                request_serializer=kms.GetKmsConfigRequest.serialize,
                response_deserializer=kms.KmsConfig.deserialize,
            )
        return self._stubs["get_kms_config"]

    @property
    def update_kms_config(
        self,
    ) -> Callable[[kms.UpdateKmsConfigRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the update kms config method over gRPC.

        Updates the Kms config properties with the full spec

        Returns:
            Callable[[~.UpdateKmsConfigRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_kms_config" not in self._stubs:
            self._stubs["update_kms_config"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/UpdateKmsConfig",
                request_serializer=kms.UpdateKmsConfigRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_kms_config"]

    @property
    def encrypt_volumes(
        self,
    ) -> Callable[[kms.EncryptVolumesRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the encrypt volumes method over gRPC.

        Encrypt the existing volumes without CMEK encryption
        with the desired the KMS config for the whole region.

        Returns:
            Callable[[~.EncryptVolumesRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "encrypt_volumes" not in self._stubs:
            self._stubs["encrypt_volumes"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/EncryptVolumes",
                request_serializer=kms.EncryptVolumesRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["encrypt_volumes"]

    @property
    def verify_kms_config(
        self,
    ) -> Callable[[kms.VerifyKmsConfigRequest], Awaitable[kms.VerifyKmsConfigResponse]]:
        r"""Return a callable for the verify kms config method over gRPC.

        Verifies KMS config reachability.

        Returns:
            Callable[[~.VerifyKmsConfigRequest],
                    Awaitable[~.VerifyKmsConfigResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "verify_kms_config" not in self._stubs:
            self._stubs["verify_kms_config"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/VerifyKmsConfig",
                request_serializer=kms.VerifyKmsConfigRequest.serialize,
                response_deserializer=kms.VerifyKmsConfigResponse.deserialize,
            )
        return self._stubs["verify_kms_config"]

    @property
    def delete_kms_config(
        self,
    ) -> Callable[[kms.DeleteKmsConfigRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the delete kms config method over gRPC.

        Warning! This operation will permanently delete the
        Kms config.

        Returns:
            Callable[[~.DeleteKmsConfigRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_kms_config" not in self._stubs:
            self._stubs["delete_kms_config"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/DeleteKmsConfig",
                request_serializer=kms.DeleteKmsConfigRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_kms_config"]

    @property
    def list_replications(
        self,
    ) -> Callable[
        [replication.ListReplicationsRequest],
        Awaitable[replication.ListReplicationsResponse],
    ]:
        r"""Return a callable for the list replications method over gRPC.

        Returns descriptions of all replications for a
        volume.

        Returns:
            Callable[[~.ListReplicationsRequest],
                    Awaitable[~.ListReplicationsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_replications" not in self._stubs:
            self._stubs["list_replications"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/ListReplications",
                request_serializer=replication.ListReplicationsRequest.serialize,
                response_deserializer=replication.ListReplicationsResponse.deserialize,
            )
        return self._stubs["list_replications"]

    @property
    def get_replication(
        self,
    ) -> Callable[
        [replication.GetReplicationRequest], Awaitable[replication.Replication]
    ]:
        r"""Return a callable for the get replication method over gRPC.

        Describe a replication for a volume.

        Returns:
            Callable[[~.GetReplicationRequest],
                    Awaitable[~.Replication]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_replication" not in self._stubs:
            self._stubs["get_replication"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/GetReplication",
                request_serializer=replication.GetReplicationRequest.serialize,
                response_deserializer=replication.Replication.deserialize,
            )
        return self._stubs["get_replication"]

    @property
    def create_replication(
        self,
    ) -> Callable[
        [gcn_replication.CreateReplicationRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create replication method over gRPC.

        Create a new replication for a volume.

        Returns:
            Callable[[~.CreateReplicationRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_replication" not in self._stubs:
            self._stubs["create_replication"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/CreateReplication",
                request_serializer=gcn_replication.CreateReplicationRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_replication"]

    @property
    def delete_replication(
        self,
    ) -> Callable[
        [replication.DeleteReplicationRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the delete replication method over gRPC.

        Deletes a replication.

        Returns:
            Callable[[~.DeleteReplicationRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_replication" not in self._stubs:
            self._stubs["delete_replication"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/DeleteReplication",
                request_serializer=replication.DeleteReplicationRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_replication"]

    @property
    def update_replication(
        self,
    ) -> Callable[
        [gcn_replication.UpdateReplicationRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update replication method over gRPC.

        Updates the settings of a specific replication.

        Returns:
            Callable[[~.UpdateReplicationRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_replication" not in self._stubs:
            self._stubs["update_replication"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/UpdateReplication",
                request_serializer=gcn_replication.UpdateReplicationRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_replication"]

    @property
    def stop_replication(
        self,
    ) -> Callable[
        [replication.StopReplicationRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the stop replication method over gRPC.

        Stop Cross Region Replication.

        Returns:
            Callable[[~.StopReplicationRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "stop_replication" not in self._stubs:
            self._stubs["stop_replication"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/StopReplication",
                request_serializer=replication.StopReplicationRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["stop_replication"]

    @property
    def resume_replication(
        self,
    ) -> Callable[
        [replication.ResumeReplicationRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the resume replication method over gRPC.

        Resume Cross Region Replication.

        Returns:
            Callable[[~.ResumeReplicationRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "resume_replication" not in self._stubs:
            self._stubs["resume_replication"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/ResumeReplication",
                request_serializer=replication.ResumeReplicationRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["resume_replication"]

    @property
    def reverse_replication_direction(
        self,
    ) -> Callable[
        [replication.ReverseReplicationDirectionRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the reverse replication direction method over gRPC.

        Reverses direction of replication. Source becomes
        destination and destination becomes source.

        Returns:
            Callable[[~.ReverseReplicationDirectionRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "reverse_replication_direction" not in self._stubs:
            self._stubs["reverse_replication_direction"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.netapp.v1.NetApp/ReverseReplicationDirection",
                    request_serializer=replication.ReverseReplicationDirectionRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["reverse_replication_direction"]

    @property
    def establish_peering(
        self,
    ) -> Callable[
        [replication.EstablishPeeringRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the establish peering method over gRPC.

        Establish replication peering.

        Returns:
            Callable[[~.EstablishPeeringRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "establish_peering" not in self._stubs:
            self._stubs["establish_peering"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/EstablishPeering",
                request_serializer=replication.EstablishPeeringRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["establish_peering"]

    @property
    def sync_replication(
        self,
    ) -> Callable[
        [replication.SyncReplicationRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the sync replication method over gRPC.

        Syncs the replication. This will invoke one time
        volume data transfer from source to destination.

        Returns:
            Callable[[~.SyncReplicationRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "sync_replication" not in self._stubs:
            self._stubs["sync_replication"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/SyncReplication",
                request_serializer=replication.SyncReplicationRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["sync_replication"]

    @property
    def create_backup_vault(
        self,
    ) -> Callable[
        [gcn_backup_vault.CreateBackupVaultRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create backup vault method over gRPC.

        Creates new backup vault

        Returns:
            Callable[[~.CreateBackupVaultRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_backup_vault" not in self._stubs:
            self._stubs["create_backup_vault"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/CreateBackupVault",
                request_serializer=gcn_backup_vault.CreateBackupVaultRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_backup_vault"]

    @property
    def get_backup_vault(
        self,
    ) -> Callable[
        [backup_vault.GetBackupVaultRequest], Awaitable[backup_vault.BackupVault]
    ]:
        r"""Return a callable for the get backup vault method over gRPC.

        Returns the description of the specified backup vault

        Returns:
            Callable[[~.GetBackupVaultRequest],
                    Awaitable[~.BackupVault]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_backup_vault" not in self._stubs:
            self._stubs["get_backup_vault"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/GetBackupVault",
                request_serializer=backup_vault.GetBackupVaultRequest.serialize,
                response_deserializer=backup_vault.BackupVault.deserialize,
            )
        return self._stubs["get_backup_vault"]

    @property
    def list_backup_vaults(
        self,
    ) -> Callable[
        [backup_vault.ListBackupVaultsRequest],
        Awaitable[backup_vault.ListBackupVaultsResponse],
    ]:
        r"""Return a callable for the list backup vaults method over gRPC.

        Returns list of all available backup vaults.

        Returns:
            Callable[[~.ListBackupVaultsRequest],
                    Awaitable[~.ListBackupVaultsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_backup_vaults" not in self._stubs:
            self._stubs["list_backup_vaults"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/ListBackupVaults",
                request_serializer=backup_vault.ListBackupVaultsRequest.serialize,
                response_deserializer=backup_vault.ListBackupVaultsResponse.deserialize,
            )
        return self._stubs["list_backup_vaults"]

    @property
    def update_backup_vault(
        self,
    ) -> Callable[
        [gcn_backup_vault.UpdateBackupVaultRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update backup vault method over gRPC.

        Updates the settings of a specific backup vault.

        Returns:
            Callable[[~.UpdateBackupVaultRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_backup_vault" not in self._stubs:
            self._stubs["update_backup_vault"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/UpdateBackupVault",
                request_serializer=gcn_backup_vault.UpdateBackupVaultRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_backup_vault"]

    @property
    def delete_backup_vault(
        self,
    ) -> Callable[
        [backup_vault.DeleteBackupVaultRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the delete backup vault method over gRPC.

        Warning! This operation will permanently delete the
        backup vault.

        Returns:
            Callable[[~.DeleteBackupVaultRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_backup_vault" not in self._stubs:
            self._stubs["delete_backup_vault"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/DeleteBackupVault",
                request_serializer=backup_vault.DeleteBackupVaultRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_backup_vault"]

    @property
    def create_backup(
        self,
    ) -> Callable[
        [gcn_backup.CreateBackupRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create backup method over gRPC.

        Creates a backup from the volume specified in the
        request The backup can be created from the given
        snapshot if specified in the request. If no snapshot
        specified, there'll be a new snapshot taken to initiate
        the backup creation.

        Returns:
            Callable[[~.CreateBackupRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_backup" not in self._stubs:
            self._stubs["create_backup"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/CreateBackup",
                request_serializer=gcn_backup.CreateBackupRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_backup"]

    @property
    def get_backup(
        self,
    ) -> Callable[[backup.GetBackupRequest], Awaitable[backup.Backup]]:
        r"""Return a callable for the get backup method over gRPC.

        Returns the description of the specified backup

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
                "/google.cloud.netapp.v1.NetApp/GetBackup",
                request_serializer=backup.GetBackupRequest.serialize,
                response_deserializer=backup.Backup.deserialize,
            )
        return self._stubs["get_backup"]

    @property
    def list_backups(
        self,
    ) -> Callable[[backup.ListBackupsRequest], Awaitable[backup.ListBackupsResponse]]:
        r"""Return a callable for the list backups method over gRPC.

        Returns descriptions of all backups for a
        backupVault.

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
                "/google.cloud.netapp.v1.NetApp/ListBackups",
                request_serializer=backup.ListBackupsRequest.serialize,
                response_deserializer=backup.ListBackupsResponse.deserialize,
            )
        return self._stubs["list_backups"]

    @property
    def delete_backup(
        self,
    ) -> Callable[[backup.DeleteBackupRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the delete backup method over gRPC.

        Warning! This operation will permanently delete the
        backup.

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
                "/google.cloud.netapp.v1.NetApp/DeleteBackup",
                request_serializer=backup.DeleteBackupRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_backup"]

    @property
    def update_backup(
        self,
    ) -> Callable[
        [gcn_backup.UpdateBackupRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update backup method over gRPC.

        Update backup with full spec.

        Returns:
            Callable[[~.UpdateBackupRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_backup" not in self._stubs:
            self._stubs["update_backup"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/UpdateBackup",
                request_serializer=gcn_backup.UpdateBackupRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_backup"]

    @property
    def create_backup_policy(
        self,
    ) -> Callable[
        [gcn_backup_policy.CreateBackupPolicyRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the create backup policy method over gRPC.

        Creates new backup policy

        Returns:
            Callable[[~.CreateBackupPolicyRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_backup_policy" not in self._stubs:
            self._stubs["create_backup_policy"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/CreateBackupPolicy",
                request_serializer=gcn_backup_policy.CreateBackupPolicyRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_backup_policy"]

    @property
    def get_backup_policy(
        self,
    ) -> Callable[
        [backup_policy.GetBackupPolicyRequest], Awaitable[backup_policy.BackupPolicy]
    ]:
        r"""Return a callable for the get backup policy method over gRPC.

        Returns the description of the specified backup policy by
        backup_policy_id.

        Returns:
            Callable[[~.GetBackupPolicyRequest],
                    Awaitable[~.BackupPolicy]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_backup_policy" not in self._stubs:
            self._stubs["get_backup_policy"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/GetBackupPolicy",
                request_serializer=backup_policy.GetBackupPolicyRequest.serialize,
                response_deserializer=backup_policy.BackupPolicy.deserialize,
            )
        return self._stubs["get_backup_policy"]

    @property
    def list_backup_policies(
        self,
    ) -> Callable[
        [backup_policy.ListBackupPoliciesRequest],
        Awaitable[backup_policy.ListBackupPoliciesResponse],
    ]:
        r"""Return a callable for the list backup policies method over gRPC.

        Returns list of all available backup policies.

        Returns:
            Callable[[~.ListBackupPoliciesRequest],
                    Awaitable[~.ListBackupPoliciesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_backup_policies" not in self._stubs:
            self._stubs["list_backup_policies"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/ListBackupPolicies",
                request_serializer=backup_policy.ListBackupPoliciesRequest.serialize,
                response_deserializer=backup_policy.ListBackupPoliciesResponse.deserialize,
            )
        return self._stubs["list_backup_policies"]

    @property
    def update_backup_policy(
        self,
    ) -> Callable[
        [gcn_backup_policy.UpdateBackupPolicyRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the update backup policy method over gRPC.

        Updates settings of a specific backup policy.

        Returns:
            Callable[[~.UpdateBackupPolicyRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_backup_policy" not in self._stubs:
            self._stubs["update_backup_policy"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/UpdateBackupPolicy",
                request_serializer=gcn_backup_policy.UpdateBackupPolicyRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_backup_policy"]

    @property
    def delete_backup_policy(
        self,
    ) -> Callable[
        [backup_policy.DeleteBackupPolicyRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the delete backup policy method over gRPC.

        Warning! This operation will permanently delete the
        backup policy.

        Returns:
            Callable[[~.DeleteBackupPolicyRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_backup_policy" not in self._stubs:
            self._stubs["delete_backup_policy"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/DeleteBackupPolicy",
                request_serializer=backup_policy.DeleteBackupPolicyRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_backup_policy"]

    @property
    def list_quota_rules(
        self,
    ) -> Callable[
        [quota_rule.ListQuotaRulesRequest], Awaitable[quota_rule.ListQuotaRulesResponse]
    ]:
        r"""Return a callable for the list quota rules method over gRPC.

        Returns list of all quota rules in a location.

        Returns:
            Callable[[~.ListQuotaRulesRequest],
                    Awaitable[~.ListQuotaRulesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_quota_rules" not in self._stubs:
            self._stubs["list_quota_rules"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/ListQuotaRules",
                request_serializer=quota_rule.ListQuotaRulesRequest.serialize,
                response_deserializer=quota_rule.ListQuotaRulesResponse.deserialize,
            )
        return self._stubs["list_quota_rules"]

    @property
    def get_quota_rule(
        self,
    ) -> Callable[[quota_rule.GetQuotaRuleRequest], Awaitable[quota_rule.QuotaRule]]:
        r"""Return a callable for the get quota rule method over gRPC.

        Returns details of the specified quota rule.

        Returns:
            Callable[[~.GetQuotaRuleRequest],
                    Awaitable[~.QuotaRule]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_quota_rule" not in self._stubs:
            self._stubs["get_quota_rule"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/GetQuotaRule",
                request_serializer=quota_rule.GetQuotaRuleRequest.serialize,
                response_deserializer=quota_rule.QuotaRule.deserialize,
            )
        return self._stubs["get_quota_rule"]

    @property
    def create_quota_rule(
        self,
    ) -> Callable[
        [gcn_quota_rule.CreateQuotaRuleRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create quota rule method over gRPC.

        Creates a new quota rule.

        Returns:
            Callable[[~.CreateQuotaRuleRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_quota_rule" not in self._stubs:
            self._stubs["create_quota_rule"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/CreateQuotaRule",
                request_serializer=gcn_quota_rule.CreateQuotaRuleRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_quota_rule"]

    @property
    def update_quota_rule(
        self,
    ) -> Callable[
        [gcn_quota_rule.UpdateQuotaRuleRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update quota rule method over gRPC.

        Updates a quota rule.

        Returns:
            Callable[[~.UpdateQuotaRuleRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_quota_rule" not in self._stubs:
            self._stubs["update_quota_rule"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/UpdateQuotaRule",
                request_serializer=gcn_quota_rule.UpdateQuotaRuleRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_quota_rule"]

    @property
    def delete_quota_rule(
        self,
    ) -> Callable[
        [quota_rule.DeleteQuotaRuleRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the delete quota rule method over gRPC.

        Deletes a quota rule.

        Returns:
            Callable[[~.DeleteQuotaRuleRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_quota_rule" not in self._stubs:
            self._stubs["delete_quota_rule"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/DeleteQuotaRule",
                request_serializer=quota_rule.DeleteQuotaRuleRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_quota_rule"]

    @property
    def restore_backup_files(
        self,
    ) -> Callable[
        [volume.RestoreBackupFilesRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the restore backup files method over gRPC.

        Restore files from a backup to a volume.

        Returns:
            Callable[[~.RestoreBackupFilesRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "restore_backup_files" not in self._stubs:
            self._stubs["restore_backup_files"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/RestoreBackupFiles",
                request_serializer=volume.RestoreBackupFilesRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["restore_backup_files"]

    @property
    def list_host_groups(
        self,
    ) -> Callable[
        [host_group.ListHostGroupsRequest], Awaitable[host_group.ListHostGroupsResponse]
    ]:
        r"""Return a callable for the list host groups method over gRPC.

        Returns a list of host groups in a ``location``. Use ``-`` as
        location to list host groups across all locations.

        Returns:
            Callable[[~.ListHostGroupsRequest],
                    Awaitable[~.ListHostGroupsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_host_groups" not in self._stubs:
            self._stubs["list_host_groups"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/ListHostGroups",
                request_serializer=host_group.ListHostGroupsRequest.serialize,
                response_deserializer=host_group.ListHostGroupsResponse.deserialize,
            )
        return self._stubs["list_host_groups"]

    @property
    def get_host_group(
        self,
    ) -> Callable[[host_group.GetHostGroupRequest], Awaitable[host_group.HostGroup]]:
        r"""Return a callable for the get host group method over gRPC.

        Returns details of the specified host group.

        Returns:
            Callable[[~.GetHostGroupRequest],
                    Awaitable[~.HostGroup]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_host_group" not in self._stubs:
            self._stubs["get_host_group"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/GetHostGroup",
                request_serializer=host_group.GetHostGroupRequest.serialize,
                response_deserializer=host_group.HostGroup.deserialize,
            )
        return self._stubs["get_host_group"]

    @property
    def create_host_group(
        self,
    ) -> Callable[
        [gcn_host_group.CreateHostGroupRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create host group method over gRPC.

        Creates a new host group.

        Returns:
            Callable[[~.CreateHostGroupRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_host_group" not in self._stubs:
            self._stubs["create_host_group"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/CreateHostGroup",
                request_serializer=gcn_host_group.CreateHostGroupRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_host_group"]

    @property
    def update_host_group(
        self,
    ) -> Callable[
        [gcn_host_group.UpdateHostGroupRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update host group method over gRPC.

        Updates an existing host group.

        Returns:
            Callable[[~.UpdateHostGroupRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_host_group" not in self._stubs:
            self._stubs["update_host_group"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/UpdateHostGroup",
                request_serializer=gcn_host_group.UpdateHostGroupRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_host_group"]

    @property
    def delete_host_group(
        self,
    ) -> Callable[
        [host_group.DeleteHostGroupRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the delete host group method over gRPC.

        Deletes a host group.

        Returns:
            Callable[[~.DeleteHostGroupRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_host_group" not in self._stubs:
            self._stubs["delete_host_group"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/DeleteHostGroup",
                request_serializer=host_group.DeleteHostGroupRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_host_group"]

    @property
    def execute_ontap_post(
        self,
    ) -> Callable[
        [ontap.ExecuteOntapPostRequest], Awaitable[ontap.ExecuteOntapPostResponse]
    ]:
        r"""Return a callable for the execute ontap post method over gRPC.

        ``ExecuteOntapPost`` sends the ONTAP ``POST`` request to the
        ``StoragePool`` cluster.

        Returns:
            Callable[[~.ExecuteOntapPostRequest],
                    Awaitable[~.ExecuteOntapPostResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "execute_ontap_post" not in self._stubs:
            self._stubs["execute_ontap_post"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/ExecuteOntapPost",
                request_serializer=ontap.ExecuteOntapPostRequest.serialize,
                response_deserializer=ontap.ExecuteOntapPostResponse.deserialize,
            )
        return self._stubs["execute_ontap_post"]

    @property
    def execute_ontap_get(
        self,
    ) -> Callable[
        [ontap.ExecuteOntapGetRequest], Awaitable[ontap.ExecuteOntapGetResponse]
    ]:
        r"""Return a callable for the execute ontap get method over gRPC.

        ``ExecuteOntapGet`` sends the ONTAP ``GET`` request to the
        ``StoragePool`` cluster.

        Returns:
            Callable[[~.ExecuteOntapGetRequest],
                    Awaitable[~.ExecuteOntapGetResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "execute_ontap_get" not in self._stubs:
            self._stubs["execute_ontap_get"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/ExecuteOntapGet",
                request_serializer=ontap.ExecuteOntapGetRequest.serialize,
                response_deserializer=ontap.ExecuteOntapGetResponse.deserialize,
            )
        return self._stubs["execute_ontap_get"]

    @property
    def execute_ontap_delete(
        self,
    ) -> Callable[
        [ontap.ExecuteOntapDeleteRequest], Awaitable[ontap.ExecuteOntapDeleteResponse]
    ]:
        r"""Return a callable for the execute ontap delete method over gRPC.

        ``ExecuteOntapDelete`` sends the ONTAP ``DELETE`` request to the
        ``StoragePool`` cluster.

        Returns:
            Callable[[~.ExecuteOntapDeleteRequest],
                    Awaitable[~.ExecuteOntapDeleteResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "execute_ontap_delete" not in self._stubs:
            self._stubs["execute_ontap_delete"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/ExecuteOntapDelete",
                request_serializer=ontap.ExecuteOntapDeleteRequest.serialize,
                response_deserializer=ontap.ExecuteOntapDeleteResponse.deserialize,
            )
        return self._stubs["execute_ontap_delete"]

    @property
    def execute_ontap_patch(
        self,
    ) -> Callable[
        [ontap.ExecuteOntapPatchRequest], Awaitable[ontap.ExecuteOntapPatchResponse]
    ]:
        r"""Return a callable for the execute ontap patch method over gRPC.

        ``ExecuteOntapPatch`` sends the ONTAP ``PATCH`` request to the
        ``StoragePool`` cluster.

        Returns:
            Callable[[~.ExecuteOntapPatchRequest],
                    Awaitable[~.ExecuteOntapPatchResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "execute_ontap_patch" not in self._stubs:
            self._stubs["execute_ontap_patch"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/ExecuteOntapPatch",
                request_serializer=ontap.ExecuteOntapPatchRequest.serialize,
                response_deserializer=ontap.ExecuteOntapPatchResponse.deserialize,
            )
        return self._stubs["execute_ontap_patch"]

    @property
    def restore_volume(
        self,
    ) -> Callable[[volume.RestoreVolumeRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the restore volume method over gRPC.

        Restores a backup to an ONTAP-mode volume.

        Returns:
            Callable[[~.RestoreVolumeRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "restore_volume" not in self._stubs:
            self._stubs["restore_volume"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/RestoreVolume",
                request_serializer=volume.RestoreVolumeRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["restore_volume"]

    @property
    def list_backup_configs(
        self,
    ) -> Callable[
        [volume.ListBackupConfigsRequest], Awaitable[volume.ListBackupConfigsResponse]
    ]:
        r"""Return a callable for the list backup configs method over gRPC.

        Lists backup configurations for all volumes in an
        ONTAP-mode Storage Pool.

        Returns:
            Callable[[~.ListBackupConfigsRequest],
                    Awaitable[~.ListBackupConfigsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_backup_configs" not in self._stubs:
            self._stubs["list_backup_configs"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/ListBackupConfigs",
                request_serializer=volume.ListBackupConfigsRequest.serialize,
                response_deserializer=volume.ListBackupConfigsResponse.deserialize,
            )
        return self._stubs["list_backup_configs"]

    @property
    def update_backup_config(
        self,
    ) -> Callable[
        [volume.UpdateBackupConfigRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update backup config method over gRPC.

        Updates the backup configuration for an ONTAP-mode
        volume.

        Returns:
            Callable[[~.UpdateBackupConfigRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_backup_config" not in self._stubs:
            self._stubs["update_backup_config"] = self._logged_channel.unary_unary(
                "/google.cloud.netapp.v1.NetApp/UpdateBackupConfig",
                request_serializer=volume.UpdateBackupConfigRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_backup_config"]

    def _prep_wrapped_messages(self, client_info):
        """Precompute the wrapped methods, overriding the base class method to use async wrappers."""
        self._wrapped_methods = {
            self.list_storage_pools: self._wrap_method(
                self.list_storage_pools,
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
            self.create_storage_pool: self._wrap_method(
                self.create_storage_pool,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_storage_pool: self._wrap_method(
                self.get_storage_pool,
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
            self.update_storage_pool: self._wrap_method(
                self.update_storage_pool,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_storage_pool: self._wrap_method(
                self.delete_storage_pool,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.validate_directory_service: self._wrap_method(
                self.validate_directory_service,
                default_timeout=None,
                client_info=client_info,
            ),
            self.switch_active_replica_zone: self._wrap_method(
                self.switch_active_replica_zone,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_volumes: self._wrap_method(
                self.list_volumes,
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
            self.get_volume: self._wrap_method(
                self.get_volume,
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
            self.create_volume: self._wrap_method(
                self.create_volume,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_volume: self._wrap_method(
                self.update_volume,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_volume: self._wrap_method(
                self.delete_volume,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.revert_volume: self._wrap_method(
                self.revert_volume,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.start_split: self._wrap_method(
                self.start_split,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_split_status: self._wrap_method(
                self.get_split_status,
                default_timeout=None,
                client_info=client_info,
            ),
            self.establish_volume_peering: self._wrap_method(
                self.establish_volume_peering,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_snapshots: self._wrap_method(
                self.list_snapshots,
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
            self.get_snapshot: self._wrap_method(
                self.get_snapshot,
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
            self.create_snapshot: self._wrap_method(
                self.create_snapshot,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_snapshot: self._wrap_method(
                self.delete_snapshot,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_snapshot: self._wrap_method(
                self.update_snapshot,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_active_directories: self._wrap_method(
                self.list_active_directories,
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
            self.get_active_directory: self._wrap_method(
                self.get_active_directory,
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
            self.create_active_directory: self._wrap_method(
                self.create_active_directory,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_active_directory: self._wrap_method(
                self.update_active_directory,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_active_directory: self._wrap_method(
                self.delete_active_directory,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_kms_configs: self._wrap_method(
                self.list_kms_configs,
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
            self.create_kms_config: self._wrap_method(
                self.create_kms_config,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_kms_config: self._wrap_method(
                self.get_kms_config,
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
            self.update_kms_config: self._wrap_method(
                self.update_kms_config,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.encrypt_volumes: self._wrap_method(
                self.encrypt_volumes,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.verify_kms_config: self._wrap_method(
                self.verify_kms_config,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_kms_config: self._wrap_method(
                self.delete_kms_config,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_replications: self._wrap_method(
                self.list_replications,
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
            self.get_replication: self._wrap_method(
                self.get_replication,
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
            self.create_replication: self._wrap_method(
                self.create_replication,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_replication: self._wrap_method(
                self.delete_replication,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_replication: self._wrap_method(
                self.update_replication,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.stop_replication: self._wrap_method(
                self.stop_replication,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.resume_replication: self._wrap_method(
                self.resume_replication,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.reverse_replication_direction: self._wrap_method(
                self.reverse_replication_direction,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.establish_peering: self._wrap_method(
                self.establish_peering,
                default_timeout=None,
                client_info=client_info,
            ),
            self.sync_replication: self._wrap_method(
                self.sync_replication,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_backup_vault: self._wrap_method(
                self.create_backup_vault,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_backup_vault: self._wrap_method(
                self.get_backup_vault,
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
            self.list_backup_vaults: self._wrap_method(
                self.list_backup_vaults,
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
            self.update_backup_vault: self._wrap_method(
                self.update_backup_vault,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_backup_vault: self._wrap_method(
                self.delete_backup_vault,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_backup: self._wrap_method(
                self.create_backup,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_backup: self._wrap_method(
                self.get_backup,
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
            self.list_backups: self._wrap_method(
                self.list_backups,
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
            self.delete_backup: self._wrap_method(
                self.delete_backup,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_backup: self._wrap_method(
                self.update_backup,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_backup_policy: self._wrap_method(
                self.create_backup_policy,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_backup_policy: self._wrap_method(
                self.get_backup_policy,
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
            self.list_backup_policies: self._wrap_method(
                self.list_backup_policies,
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
            self.update_backup_policy: self._wrap_method(
                self.update_backup_policy,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_backup_policy: self._wrap_method(
                self.delete_backup_policy,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_quota_rules: self._wrap_method(
                self.list_quota_rules,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_quota_rule: self._wrap_method(
                self.get_quota_rule,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_quota_rule: self._wrap_method(
                self.create_quota_rule,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_quota_rule: self._wrap_method(
                self.update_quota_rule,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_quota_rule: self._wrap_method(
                self.delete_quota_rule,
                default_timeout=None,
                client_info=client_info,
            ),
            self.restore_backup_files: self._wrap_method(
                self.restore_backup_files,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_host_groups: self._wrap_method(
                self.list_host_groups,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_host_group: self._wrap_method(
                self.get_host_group,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_host_group: self._wrap_method(
                self.create_host_group,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_host_group: self._wrap_method(
                self.update_host_group,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_host_group: self._wrap_method(
                self.delete_host_group,
                default_timeout=None,
                client_info=client_info,
            ),
            self.execute_ontap_post: self._wrap_method(
                self.execute_ontap_post,
                default_timeout=None,
                client_info=client_info,
            ),
            self.execute_ontap_get: self._wrap_method(
                self.execute_ontap_get,
                default_timeout=None,
                client_info=client_info,
            ),
            self.execute_ontap_delete: self._wrap_method(
                self.execute_ontap_delete,
                default_timeout=None,
                client_info=client_info,
            ),
            self.execute_ontap_patch: self._wrap_method(
                self.execute_ontap_patch,
                default_timeout=None,
                client_info=client_info,
            ),
            self.restore_volume: self._wrap_method(
                self.restore_volume,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_backup_configs: self._wrap_method(
                self.list_backup_configs,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_backup_config: self._wrap_method(
                self.update_backup_config,
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


__all__ = ("NetAppGrpcAsyncIOTransport",)
