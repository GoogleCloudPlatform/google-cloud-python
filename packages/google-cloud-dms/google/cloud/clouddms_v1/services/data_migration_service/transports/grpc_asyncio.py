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
from google.api_core import gapic_v1, grpc_helpers_async, operations_v1
from google.api_core import retry_async as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf.json_format import MessageToJson
from grpc.experimental import aio  # type: ignore

from google.cloud.clouddms_v1.types import (
    clouddms,
    clouddms_resources,
    conversionworkspace_resources,
)

from .base import DEFAULT_CLIENT_INFO, DataMigrationServiceTransport
from .grpc import DataMigrationServiceGrpcTransport

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
                    "serviceName": "google.cloud.clouddms.v1.DataMigrationService",
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
                    "serviceName": "google.cloud.clouddms.v1.DataMigrationService",
                    "rpcName": str(client_call_details.method),
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class DataMigrationServiceGrpcAsyncIOTransport(DataMigrationServiceTransport):
    """gRPC AsyncIO backend transport for DataMigrationService.

    Database Migration service

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
        host: str = "datamigration.googleapis.com",
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
        host: str = "datamigration.googleapis.com",
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
                 The hostname to connect to (default: 'datamigration.googleapis.com').
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
    def list_migration_jobs(
        self,
    ) -> Callable[
        [clouddms.ListMigrationJobsRequest],
        Awaitable[clouddms.ListMigrationJobsResponse],
    ]:
        r"""Return a callable for the list migration jobs method over gRPC.

        Lists migration jobs in a given project and location.

        Returns:
            Callable[[~.ListMigrationJobsRequest],
                    Awaitable[~.ListMigrationJobsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_migration_jobs" not in self._stubs:
            self._stubs["list_migration_jobs"] = self._logged_channel.unary_unary(
                "/google.cloud.clouddms.v1.DataMigrationService/ListMigrationJobs",
                request_serializer=clouddms.ListMigrationJobsRequest.serialize,
                response_deserializer=clouddms.ListMigrationJobsResponse.deserialize,
            )
        return self._stubs["list_migration_jobs"]

    @property
    def get_migration_job(
        self,
    ) -> Callable[
        [clouddms.GetMigrationJobRequest], Awaitable[clouddms_resources.MigrationJob]
    ]:
        r"""Return a callable for the get migration job method over gRPC.

        Gets details of a single migration job.

        Returns:
            Callable[[~.GetMigrationJobRequest],
                    Awaitable[~.MigrationJob]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_migration_job" not in self._stubs:
            self._stubs["get_migration_job"] = self._logged_channel.unary_unary(
                "/google.cloud.clouddms.v1.DataMigrationService/GetMigrationJob",
                request_serializer=clouddms.GetMigrationJobRequest.serialize,
                response_deserializer=clouddms_resources.MigrationJob.deserialize,
            )
        return self._stubs["get_migration_job"]

    @property
    def create_migration_job(
        self,
    ) -> Callable[
        [clouddms.CreateMigrationJobRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create migration job method over gRPC.

        Creates a new migration job in a given project and
        location.

        Returns:
            Callable[[~.CreateMigrationJobRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_migration_job" not in self._stubs:
            self._stubs["create_migration_job"] = self._logged_channel.unary_unary(
                "/google.cloud.clouddms.v1.DataMigrationService/CreateMigrationJob",
                request_serializer=clouddms.CreateMigrationJobRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_migration_job"]

    @property
    def update_migration_job(
        self,
    ) -> Callable[
        [clouddms.UpdateMigrationJobRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update migration job method over gRPC.

        Updates the parameters of a single migration job.

        Returns:
            Callable[[~.UpdateMigrationJobRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_migration_job" not in self._stubs:
            self._stubs["update_migration_job"] = self._logged_channel.unary_unary(
                "/google.cloud.clouddms.v1.DataMigrationService/UpdateMigrationJob",
                request_serializer=clouddms.UpdateMigrationJobRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_migration_job"]

    @property
    def delete_migration_job(
        self,
    ) -> Callable[
        [clouddms.DeleteMigrationJobRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the delete migration job method over gRPC.

        Deletes a single migration job.

        Returns:
            Callable[[~.DeleteMigrationJobRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_migration_job" not in self._stubs:
            self._stubs["delete_migration_job"] = self._logged_channel.unary_unary(
                "/google.cloud.clouddms.v1.DataMigrationService/DeleteMigrationJob",
                request_serializer=clouddms.DeleteMigrationJobRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_migration_job"]

    @property
    def start_migration_job(
        self,
    ) -> Callable[
        [clouddms.StartMigrationJobRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the start migration job method over gRPC.

        Start an already created migration job.

        Returns:
            Callable[[~.StartMigrationJobRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "start_migration_job" not in self._stubs:
            self._stubs["start_migration_job"] = self._logged_channel.unary_unary(
                "/google.cloud.clouddms.v1.DataMigrationService/StartMigrationJob",
                request_serializer=clouddms.StartMigrationJobRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["start_migration_job"]

    @property
    def stop_migration_job(
        self,
    ) -> Callable[
        [clouddms.StopMigrationJobRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the stop migration job method over gRPC.

        Stops a running migration job.

        Returns:
            Callable[[~.StopMigrationJobRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "stop_migration_job" not in self._stubs:
            self._stubs["stop_migration_job"] = self._logged_channel.unary_unary(
                "/google.cloud.clouddms.v1.DataMigrationService/StopMigrationJob",
                request_serializer=clouddms.StopMigrationJobRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["stop_migration_job"]

    @property
    def resume_migration_job(
        self,
    ) -> Callable[
        [clouddms.ResumeMigrationJobRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the resume migration job method over gRPC.

        Resume a migration job that is currently stopped and
        is resumable (was stopped during CDC phase).

        Returns:
            Callable[[~.ResumeMigrationJobRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "resume_migration_job" not in self._stubs:
            self._stubs["resume_migration_job"] = self._logged_channel.unary_unary(
                "/google.cloud.clouddms.v1.DataMigrationService/ResumeMigrationJob",
                request_serializer=clouddms.ResumeMigrationJobRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["resume_migration_job"]

    @property
    def promote_migration_job(
        self,
    ) -> Callable[
        [clouddms.PromoteMigrationJobRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the promote migration job method over gRPC.

        Promote a migration job, stopping replication to the
        destination and promoting the destination to be a
        standalone database.

        Returns:
            Callable[[~.PromoteMigrationJobRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "promote_migration_job" not in self._stubs:
            self._stubs["promote_migration_job"] = self._logged_channel.unary_unary(
                "/google.cloud.clouddms.v1.DataMigrationService/PromoteMigrationJob",
                request_serializer=clouddms.PromoteMigrationJobRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["promote_migration_job"]

    @property
    def verify_migration_job(
        self,
    ) -> Callable[
        [clouddms.VerifyMigrationJobRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the verify migration job method over gRPC.

        Verify a migration job, making sure the destination
        can reach the source and that all configuration and
        prerequisites are met.

        Returns:
            Callable[[~.VerifyMigrationJobRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "verify_migration_job" not in self._stubs:
            self._stubs["verify_migration_job"] = self._logged_channel.unary_unary(
                "/google.cloud.clouddms.v1.DataMigrationService/VerifyMigrationJob",
                request_serializer=clouddms.VerifyMigrationJobRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["verify_migration_job"]

    @property
    def restart_migration_job(
        self,
    ) -> Callable[
        [clouddms.RestartMigrationJobRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the restart migration job method over gRPC.

        Restart a stopped or failed migration job, resetting
        the destination instance to its original state and
        starting the migration process from scratch.

        Returns:
            Callable[[~.RestartMigrationJobRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "restart_migration_job" not in self._stubs:
            self._stubs["restart_migration_job"] = self._logged_channel.unary_unary(
                "/google.cloud.clouddms.v1.DataMigrationService/RestartMigrationJob",
                request_serializer=clouddms.RestartMigrationJobRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["restart_migration_job"]

    @property
    def generate_ssh_script(
        self,
    ) -> Callable[[clouddms.GenerateSshScriptRequest], Awaitable[clouddms.SshScript]]:
        r"""Return a callable for the generate ssh script method over gRPC.

        Generate a SSH configuration script to configure the
        reverse SSH connectivity.

        Returns:
            Callable[[~.GenerateSshScriptRequest],
                    Awaitable[~.SshScript]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "generate_ssh_script" not in self._stubs:
            self._stubs["generate_ssh_script"] = self._logged_channel.unary_unary(
                "/google.cloud.clouddms.v1.DataMigrationService/GenerateSshScript",
                request_serializer=clouddms.GenerateSshScriptRequest.serialize,
                response_deserializer=clouddms.SshScript.deserialize,
            )
        return self._stubs["generate_ssh_script"]

    @property
    def generate_tcp_proxy_script(
        self,
    ) -> Callable[
        [clouddms.GenerateTcpProxyScriptRequest], Awaitable[clouddms.TcpProxyScript]
    ]:
        r"""Return a callable for the generate tcp proxy script method over gRPC.

        Generate a TCP Proxy configuration script to
        configure a cloud-hosted VM running a TCP Proxy.

        Returns:
            Callable[[~.GenerateTcpProxyScriptRequest],
                    Awaitable[~.TcpProxyScript]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "generate_tcp_proxy_script" not in self._stubs:
            self._stubs["generate_tcp_proxy_script"] = self._logged_channel.unary_unary(
                "/google.cloud.clouddms.v1.DataMigrationService/GenerateTcpProxyScript",
                request_serializer=clouddms.GenerateTcpProxyScriptRequest.serialize,
                response_deserializer=clouddms.TcpProxyScript.deserialize,
            )
        return self._stubs["generate_tcp_proxy_script"]

    @property
    def list_connection_profiles(
        self,
    ) -> Callable[
        [clouddms.ListConnectionProfilesRequest],
        Awaitable[clouddms.ListConnectionProfilesResponse],
    ]:
        r"""Return a callable for the list connection profiles method over gRPC.

        Retrieves a list of all connection profiles in a
        given project and location.

        Returns:
            Callable[[~.ListConnectionProfilesRequest],
                    Awaitable[~.ListConnectionProfilesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_connection_profiles" not in self._stubs:
            self._stubs["list_connection_profiles"] = self._logged_channel.unary_unary(
                "/google.cloud.clouddms.v1.DataMigrationService/ListConnectionProfiles",
                request_serializer=clouddms.ListConnectionProfilesRequest.serialize,
                response_deserializer=clouddms.ListConnectionProfilesResponse.deserialize,
            )
        return self._stubs["list_connection_profiles"]

    @property
    def get_connection_profile(
        self,
    ) -> Callable[
        [clouddms.GetConnectionProfileRequest],
        Awaitable[clouddms_resources.ConnectionProfile],
    ]:
        r"""Return a callable for the get connection profile method over gRPC.

        Gets details of a single connection profile.

        Returns:
            Callable[[~.GetConnectionProfileRequest],
                    Awaitable[~.ConnectionProfile]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_connection_profile" not in self._stubs:
            self._stubs["get_connection_profile"] = self._logged_channel.unary_unary(
                "/google.cloud.clouddms.v1.DataMigrationService/GetConnectionProfile",
                request_serializer=clouddms.GetConnectionProfileRequest.serialize,
                response_deserializer=clouddms_resources.ConnectionProfile.deserialize,
            )
        return self._stubs["get_connection_profile"]

    @property
    def create_connection_profile(
        self,
    ) -> Callable[
        [clouddms.CreateConnectionProfileRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create connection profile method over gRPC.

        Creates a new connection profile in a given project
        and location.

        Returns:
            Callable[[~.CreateConnectionProfileRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_connection_profile" not in self._stubs:
            self._stubs["create_connection_profile"] = self._logged_channel.unary_unary(
                "/google.cloud.clouddms.v1.DataMigrationService/CreateConnectionProfile",
                request_serializer=clouddms.CreateConnectionProfileRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_connection_profile"]

    @property
    def update_connection_profile(
        self,
    ) -> Callable[
        [clouddms.UpdateConnectionProfileRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update connection profile method over gRPC.

        Update the configuration of a single connection
        profile.

        Returns:
            Callable[[~.UpdateConnectionProfileRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_connection_profile" not in self._stubs:
            self._stubs["update_connection_profile"] = self._logged_channel.unary_unary(
                "/google.cloud.clouddms.v1.DataMigrationService/UpdateConnectionProfile",
                request_serializer=clouddms.UpdateConnectionProfileRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_connection_profile"]

    @property
    def delete_connection_profile(
        self,
    ) -> Callable[
        [clouddms.DeleteConnectionProfileRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the delete connection profile method over gRPC.

        Deletes a single Database Migration Service
        connection profile. A connection profile can only be
        deleted if it is not in use by any active migration
        jobs.

        Returns:
            Callable[[~.DeleteConnectionProfileRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_connection_profile" not in self._stubs:
            self._stubs["delete_connection_profile"] = self._logged_channel.unary_unary(
                "/google.cloud.clouddms.v1.DataMigrationService/DeleteConnectionProfile",
                request_serializer=clouddms.DeleteConnectionProfileRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_connection_profile"]

    @property
    def create_private_connection(
        self,
    ) -> Callable[
        [clouddms.CreatePrivateConnectionRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create private connection method over gRPC.

        Creates a new private connection in a given project
        and location.

        Returns:
            Callable[[~.CreatePrivateConnectionRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_private_connection" not in self._stubs:
            self._stubs["create_private_connection"] = self._logged_channel.unary_unary(
                "/google.cloud.clouddms.v1.DataMigrationService/CreatePrivateConnection",
                request_serializer=clouddms.CreatePrivateConnectionRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_private_connection"]

    @property
    def get_private_connection(
        self,
    ) -> Callable[
        [clouddms.GetPrivateConnectionRequest],
        Awaitable[clouddms_resources.PrivateConnection],
    ]:
        r"""Return a callable for the get private connection method over gRPC.

        Gets details of a single private connection.

        Returns:
            Callable[[~.GetPrivateConnectionRequest],
                    Awaitable[~.PrivateConnection]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_private_connection" not in self._stubs:
            self._stubs["get_private_connection"] = self._logged_channel.unary_unary(
                "/google.cloud.clouddms.v1.DataMigrationService/GetPrivateConnection",
                request_serializer=clouddms.GetPrivateConnectionRequest.serialize,
                response_deserializer=clouddms_resources.PrivateConnection.deserialize,
            )
        return self._stubs["get_private_connection"]

    @property
    def list_private_connections(
        self,
    ) -> Callable[
        [clouddms.ListPrivateConnectionsRequest],
        Awaitable[clouddms.ListPrivateConnectionsResponse],
    ]:
        r"""Return a callable for the list private connections method over gRPC.

        Retrieves a list of private connections in a given
        project and location.

        Returns:
            Callable[[~.ListPrivateConnectionsRequest],
                    Awaitable[~.ListPrivateConnectionsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_private_connections" not in self._stubs:
            self._stubs["list_private_connections"] = self._logged_channel.unary_unary(
                "/google.cloud.clouddms.v1.DataMigrationService/ListPrivateConnections",
                request_serializer=clouddms.ListPrivateConnectionsRequest.serialize,
                response_deserializer=clouddms.ListPrivateConnectionsResponse.deserialize,
            )
        return self._stubs["list_private_connections"]

    @property
    def delete_private_connection(
        self,
    ) -> Callable[
        [clouddms.DeletePrivateConnectionRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the delete private connection method over gRPC.

        Deletes a single Database Migration Service private
        connection.

        Returns:
            Callable[[~.DeletePrivateConnectionRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_private_connection" not in self._stubs:
            self._stubs["delete_private_connection"] = self._logged_channel.unary_unary(
                "/google.cloud.clouddms.v1.DataMigrationService/DeletePrivateConnection",
                request_serializer=clouddms.DeletePrivateConnectionRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_private_connection"]

    @property
    def get_conversion_workspace(
        self,
    ) -> Callable[
        [clouddms.GetConversionWorkspaceRequest],
        Awaitable[conversionworkspace_resources.ConversionWorkspace],
    ]:
        r"""Return a callable for the get conversion workspace method over gRPC.

        Gets details of a single conversion workspace.

        Returns:
            Callable[[~.GetConversionWorkspaceRequest],
                    Awaitable[~.ConversionWorkspace]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_conversion_workspace" not in self._stubs:
            self._stubs["get_conversion_workspace"] = self._logged_channel.unary_unary(
                "/google.cloud.clouddms.v1.DataMigrationService/GetConversionWorkspace",
                request_serializer=clouddms.GetConversionWorkspaceRequest.serialize,
                response_deserializer=conversionworkspace_resources.ConversionWorkspace.deserialize,
            )
        return self._stubs["get_conversion_workspace"]

    @property
    def list_conversion_workspaces(
        self,
    ) -> Callable[
        [clouddms.ListConversionWorkspacesRequest],
        Awaitable[clouddms.ListConversionWorkspacesResponse],
    ]:
        r"""Return a callable for the list conversion workspaces method over gRPC.

        Lists conversion workspaces in a given project and
        location.

        Returns:
            Callable[[~.ListConversionWorkspacesRequest],
                    Awaitable[~.ListConversionWorkspacesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_conversion_workspaces" not in self._stubs:
            self._stubs["list_conversion_workspaces"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.clouddms.v1.DataMigrationService/ListConversionWorkspaces",
                    request_serializer=clouddms.ListConversionWorkspacesRequest.serialize,
                    response_deserializer=clouddms.ListConversionWorkspacesResponse.deserialize,
                )
            )
        return self._stubs["list_conversion_workspaces"]

    @property
    def create_conversion_workspace(
        self,
    ) -> Callable[
        [clouddms.CreateConversionWorkspaceRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create conversion workspace method over gRPC.

        Creates a new conversion workspace in a given project
        and location.

        Returns:
            Callable[[~.CreateConversionWorkspaceRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_conversion_workspace" not in self._stubs:
            self._stubs["create_conversion_workspace"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.clouddms.v1.DataMigrationService/CreateConversionWorkspace",
                    request_serializer=clouddms.CreateConversionWorkspaceRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["create_conversion_workspace"]

    @property
    def update_conversion_workspace(
        self,
    ) -> Callable[
        [clouddms.UpdateConversionWorkspaceRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update conversion workspace method over gRPC.

        Updates the parameters of a single conversion
        workspace.

        Returns:
            Callable[[~.UpdateConversionWorkspaceRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_conversion_workspace" not in self._stubs:
            self._stubs["update_conversion_workspace"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.clouddms.v1.DataMigrationService/UpdateConversionWorkspace",
                    request_serializer=clouddms.UpdateConversionWorkspaceRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["update_conversion_workspace"]

    @property
    def delete_conversion_workspace(
        self,
    ) -> Callable[
        [clouddms.DeleteConversionWorkspaceRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the delete conversion workspace method over gRPC.

        Deletes a single conversion workspace.

        Returns:
            Callable[[~.DeleteConversionWorkspaceRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_conversion_workspace" not in self._stubs:
            self._stubs["delete_conversion_workspace"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.clouddms.v1.DataMigrationService/DeleteConversionWorkspace",
                    request_serializer=clouddms.DeleteConversionWorkspaceRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["delete_conversion_workspace"]

    @property
    def create_mapping_rule(
        self,
    ) -> Callable[
        [clouddms.CreateMappingRuleRequest],
        Awaitable[conversionworkspace_resources.MappingRule],
    ]:
        r"""Return a callable for the create mapping rule method over gRPC.

        Creates a new mapping rule for a given conversion
        workspace.

        Returns:
            Callable[[~.CreateMappingRuleRequest],
                    Awaitable[~.MappingRule]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_mapping_rule" not in self._stubs:
            self._stubs["create_mapping_rule"] = self._logged_channel.unary_unary(
                "/google.cloud.clouddms.v1.DataMigrationService/CreateMappingRule",
                request_serializer=clouddms.CreateMappingRuleRequest.serialize,
                response_deserializer=conversionworkspace_resources.MappingRule.deserialize,
            )
        return self._stubs["create_mapping_rule"]

    @property
    def delete_mapping_rule(
        self,
    ) -> Callable[[clouddms.DeleteMappingRuleRequest], Awaitable[empty_pb2.Empty]]:
        r"""Return a callable for the delete mapping rule method over gRPC.

        Deletes a single mapping rule.

        Returns:
            Callable[[~.DeleteMappingRuleRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_mapping_rule" not in self._stubs:
            self._stubs["delete_mapping_rule"] = self._logged_channel.unary_unary(
                "/google.cloud.clouddms.v1.DataMigrationService/DeleteMappingRule",
                request_serializer=clouddms.DeleteMappingRuleRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_mapping_rule"]

    @property
    def list_mapping_rules(
        self,
    ) -> Callable[
        [clouddms.ListMappingRulesRequest], Awaitable[clouddms.ListMappingRulesResponse]
    ]:
        r"""Return a callable for the list mapping rules method over gRPC.

        Lists the mapping rules for a specific conversion
        workspace.

        Returns:
            Callable[[~.ListMappingRulesRequest],
                    Awaitable[~.ListMappingRulesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_mapping_rules" not in self._stubs:
            self._stubs["list_mapping_rules"] = self._logged_channel.unary_unary(
                "/google.cloud.clouddms.v1.DataMigrationService/ListMappingRules",
                request_serializer=clouddms.ListMappingRulesRequest.serialize,
                response_deserializer=clouddms.ListMappingRulesResponse.deserialize,
            )
        return self._stubs["list_mapping_rules"]

    @property
    def get_mapping_rule(
        self,
    ) -> Callable[
        [clouddms.GetMappingRuleRequest],
        Awaitable[conversionworkspace_resources.MappingRule],
    ]:
        r"""Return a callable for the get mapping rule method over gRPC.

        Gets the details of a mapping rule.

        Returns:
            Callable[[~.GetMappingRuleRequest],
                    Awaitable[~.MappingRule]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_mapping_rule" not in self._stubs:
            self._stubs["get_mapping_rule"] = self._logged_channel.unary_unary(
                "/google.cloud.clouddms.v1.DataMigrationService/GetMappingRule",
                request_serializer=clouddms.GetMappingRuleRequest.serialize,
                response_deserializer=conversionworkspace_resources.MappingRule.deserialize,
            )
        return self._stubs["get_mapping_rule"]

    @property
    def seed_conversion_workspace(
        self,
    ) -> Callable[
        [clouddms.SeedConversionWorkspaceRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the seed conversion workspace method over gRPC.

        Imports a snapshot of the source database into the
        conversion workspace.

        Returns:
            Callable[[~.SeedConversionWorkspaceRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "seed_conversion_workspace" not in self._stubs:
            self._stubs["seed_conversion_workspace"] = self._logged_channel.unary_unary(
                "/google.cloud.clouddms.v1.DataMigrationService/SeedConversionWorkspace",
                request_serializer=clouddms.SeedConversionWorkspaceRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["seed_conversion_workspace"]

    @property
    def import_mapping_rules(
        self,
    ) -> Callable[
        [clouddms.ImportMappingRulesRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the import mapping rules method over gRPC.

        Imports the mapping rules for a given conversion
        workspace. Supports various formats of external rules
        files.

        Returns:
            Callable[[~.ImportMappingRulesRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "import_mapping_rules" not in self._stubs:
            self._stubs["import_mapping_rules"] = self._logged_channel.unary_unary(
                "/google.cloud.clouddms.v1.DataMigrationService/ImportMappingRules",
                request_serializer=clouddms.ImportMappingRulesRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["import_mapping_rules"]

    @property
    def convert_conversion_workspace(
        self,
    ) -> Callable[
        [clouddms.ConvertConversionWorkspaceRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the convert conversion workspace method over gRPC.

        Creates a draft tree schema for the destination
        database.

        Returns:
            Callable[[~.ConvertConversionWorkspaceRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "convert_conversion_workspace" not in self._stubs:
            self._stubs["convert_conversion_workspace"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.clouddms.v1.DataMigrationService/ConvertConversionWorkspace",
                    request_serializer=clouddms.ConvertConversionWorkspaceRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["convert_conversion_workspace"]

    @property
    def commit_conversion_workspace(
        self,
    ) -> Callable[
        [clouddms.CommitConversionWorkspaceRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the commit conversion workspace method over gRPC.

        Marks all the data in the conversion workspace as
        committed.

        Returns:
            Callable[[~.CommitConversionWorkspaceRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "commit_conversion_workspace" not in self._stubs:
            self._stubs["commit_conversion_workspace"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.clouddms.v1.DataMigrationService/CommitConversionWorkspace",
                    request_serializer=clouddms.CommitConversionWorkspaceRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["commit_conversion_workspace"]

    @property
    def rollback_conversion_workspace(
        self,
    ) -> Callable[
        [clouddms.RollbackConversionWorkspaceRequest],
        Awaitable[operations_pb2.Operation],
    ]:
        r"""Return a callable for the rollback conversion workspace method over gRPC.

        Rolls back a conversion workspace to the last
        committed snapshot.

        Returns:
            Callable[[~.RollbackConversionWorkspaceRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "rollback_conversion_workspace" not in self._stubs:
            self._stubs["rollback_conversion_workspace"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.clouddms.v1.DataMigrationService/RollbackConversionWorkspace",
                    request_serializer=clouddms.RollbackConversionWorkspaceRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["rollback_conversion_workspace"]

    @property
    def apply_conversion_workspace(
        self,
    ) -> Callable[
        [clouddms.ApplyConversionWorkspaceRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the apply conversion workspace method over gRPC.

        Applies draft tree onto a specific destination
        database.

        Returns:
            Callable[[~.ApplyConversionWorkspaceRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "apply_conversion_workspace" not in self._stubs:
            self._stubs["apply_conversion_workspace"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.clouddms.v1.DataMigrationService/ApplyConversionWorkspace",
                    request_serializer=clouddms.ApplyConversionWorkspaceRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["apply_conversion_workspace"]

    @property
    def describe_database_entities(
        self,
    ) -> Callable[
        [clouddms.DescribeDatabaseEntitiesRequest],
        Awaitable[clouddms.DescribeDatabaseEntitiesResponse],
    ]:
        r"""Return a callable for the describe database entities method over gRPC.

        Describes the database entities tree for a specific
        conversion workspace and a specific tree type.

        Database entities are not resources like conversion
        workspaces or mapping rules, and they can't be created,
        updated or deleted. Instead, they are simple data
        objects describing the structure of the client database.

        Returns:
            Callable[[~.DescribeDatabaseEntitiesRequest],
                    Awaitable[~.DescribeDatabaseEntitiesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "describe_database_entities" not in self._stubs:
            self._stubs["describe_database_entities"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.clouddms.v1.DataMigrationService/DescribeDatabaseEntities",
                    request_serializer=clouddms.DescribeDatabaseEntitiesRequest.serialize,
                    response_deserializer=clouddms.DescribeDatabaseEntitiesResponse.deserialize,
                )
            )
        return self._stubs["describe_database_entities"]

    @property
    def search_background_jobs(
        self,
    ) -> Callable[
        [clouddms.SearchBackgroundJobsRequest],
        Awaitable[clouddms.SearchBackgroundJobsResponse],
    ]:
        r"""Return a callable for the search background jobs method over gRPC.

        Searches/lists the background jobs for a specific
        conversion workspace.

        The background jobs are not resources like conversion
        workspaces or mapping rules, and they can't be created,
        updated or deleted. Instead, they are a way to expose
        the data plane jobs log.

        Returns:
            Callable[[~.SearchBackgroundJobsRequest],
                    Awaitable[~.SearchBackgroundJobsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "search_background_jobs" not in self._stubs:
            self._stubs["search_background_jobs"] = self._logged_channel.unary_unary(
                "/google.cloud.clouddms.v1.DataMigrationService/SearchBackgroundJobs",
                request_serializer=clouddms.SearchBackgroundJobsRequest.serialize,
                response_deserializer=clouddms.SearchBackgroundJobsResponse.deserialize,
            )
        return self._stubs["search_background_jobs"]

    @property
    def describe_conversion_workspace_revisions(
        self,
    ) -> Callable[
        [clouddms.DescribeConversionWorkspaceRevisionsRequest],
        Awaitable[clouddms.DescribeConversionWorkspaceRevisionsResponse],
    ]:
        r"""Return a callable for the describe conversion workspace
        revisions method over gRPC.

        Retrieves a list of committed revisions of a specific
        conversion workspace.

        Returns:
            Callable[[~.DescribeConversionWorkspaceRevisionsRequest],
                    Awaitable[~.DescribeConversionWorkspaceRevisionsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "describe_conversion_workspace_revisions" not in self._stubs:
            self._stubs["describe_conversion_workspace_revisions"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.clouddms.v1.DataMigrationService/DescribeConversionWorkspaceRevisions",
                    request_serializer=clouddms.DescribeConversionWorkspaceRevisionsRequest.serialize,
                    response_deserializer=clouddms.DescribeConversionWorkspaceRevisionsResponse.deserialize,
                )
            )
        return self._stubs["describe_conversion_workspace_revisions"]

    @property
    def fetch_static_ips(
        self,
    ) -> Callable[
        [clouddms.FetchStaticIpsRequest], Awaitable[clouddms.FetchStaticIpsResponse]
    ]:
        r"""Return a callable for the fetch static ips method over gRPC.

        Fetches a set of static IP addresses that need to be
        allowlisted by the customer when using the static-IP
        connectivity method.

        Returns:
            Callable[[~.FetchStaticIpsRequest],
                    Awaitable[~.FetchStaticIpsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "fetch_static_ips" not in self._stubs:
            self._stubs["fetch_static_ips"] = self._logged_channel.unary_unary(
                "/google.cloud.clouddms.v1.DataMigrationService/FetchStaticIps",
                request_serializer=clouddms.FetchStaticIpsRequest.serialize,
                response_deserializer=clouddms.FetchStaticIpsResponse.deserialize,
            )
        return self._stubs["fetch_static_ips"]

    def _prep_wrapped_messages(self, client_info):
        """Precompute the wrapped methods, overriding the base class method to use async wrappers."""
        self._wrapped_methods = {
            self.list_migration_jobs: self._wrap_method(
                self.list_migration_jobs,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_migration_job: self._wrap_method(
                self.get_migration_job,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_migration_job: self._wrap_method(
                self.create_migration_job,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_migration_job: self._wrap_method(
                self.update_migration_job,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_migration_job: self._wrap_method(
                self.delete_migration_job,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.start_migration_job: self._wrap_method(
                self.start_migration_job,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.stop_migration_job: self._wrap_method(
                self.stop_migration_job,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.resume_migration_job: self._wrap_method(
                self.resume_migration_job,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.promote_migration_job: self._wrap_method(
                self.promote_migration_job,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.verify_migration_job: self._wrap_method(
                self.verify_migration_job,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.restart_migration_job: self._wrap_method(
                self.restart_migration_job,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.generate_ssh_script: self._wrap_method(
                self.generate_ssh_script,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.generate_tcp_proxy_script: self._wrap_method(
                self.generate_tcp_proxy_script,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_connection_profiles: self._wrap_method(
                self.list_connection_profiles,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_connection_profile: self._wrap_method(
                self.get_connection_profile,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_connection_profile: self._wrap_method(
                self.create_connection_profile,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_connection_profile: self._wrap_method(
                self.update_connection_profile,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_connection_profile: self._wrap_method(
                self.delete_connection_profile,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_private_connection: self._wrap_method(
                self.create_private_connection,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_private_connection: self._wrap_method(
                self.get_private_connection,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_private_connections: self._wrap_method(
                self.list_private_connections,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_private_connection: self._wrap_method(
                self.delete_private_connection,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_conversion_workspace: self._wrap_method(
                self.get_conversion_workspace,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_conversion_workspaces: self._wrap_method(
                self.list_conversion_workspaces,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_conversion_workspace: self._wrap_method(
                self.create_conversion_workspace,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_conversion_workspace: self._wrap_method(
                self.update_conversion_workspace,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_conversion_workspace: self._wrap_method(
                self.delete_conversion_workspace,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_mapping_rule: self._wrap_method(
                self.create_mapping_rule,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_mapping_rule: self._wrap_method(
                self.delete_mapping_rule,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_mapping_rules: self._wrap_method(
                self.list_mapping_rules,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_mapping_rule: self._wrap_method(
                self.get_mapping_rule,
                default_timeout=None,
                client_info=client_info,
            ),
            self.seed_conversion_workspace: self._wrap_method(
                self.seed_conversion_workspace,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.import_mapping_rules: self._wrap_method(
                self.import_mapping_rules,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.convert_conversion_workspace: self._wrap_method(
                self.convert_conversion_workspace,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.commit_conversion_workspace: self._wrap_method(
                self.commit_conversion_workspace,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.rollback_conversion_workspace: self._wrap_method(
                self.rollback_conversion_workspace,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.apply_conversion_workspace: self._wrap_method(
                self.apply_conversion_workspace,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.describe_database_entities: self._wrap_method(
                self.describe_database_entities,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.search_background_jobs: self._wrap_method(
                self.search_background_jobs,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.describe_conversion_workspace_revisions: self._wrap_method(
                self.describe_conversion_workspace_revisions,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.fetch_static_ips: self._wrap_method(
                self.fetch_static_ips,
                default_timeout=60.0,
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
            self.get_iam_policy: self._wrap_method(
                self.get_iam_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.set_iam_policy: self._wrap_method(
                self.set_iam_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.test_iam_permissions: self._wrap_method(
                self.test_iam_permissions,
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


__all__ = ("DataMigrationServiceGrpcAsyncIOTransport",)
