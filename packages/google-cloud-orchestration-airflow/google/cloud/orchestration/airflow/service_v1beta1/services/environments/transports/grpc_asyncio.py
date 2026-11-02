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
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf.json_format import MessageToJson
from grpc.experimental import aio  # type: ignore

from google.cloud.orchestration.airflow.service_v1beta1.types import environments

from .base import DEFAULT_CLIENT_INFO, EnvironmentsTransport
from .grpc import EnvironmentsGrpcTransport

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
                    "serviceName": "google.cloud.orchestration.airflow.service.v1beta1.Environments",
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
                    "serviceName": "google.cloud.orchestration.airflow.service.v1beta1.Environments",
                    "rpcName": str(client_call_details.method),
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class EnvironmentsGrpcAsyncIOTransport(EnvironmentsTransport):
    """gRPC AsyncIO backend transport for Environments.

    Managed Apache Airflow Environments.

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
        host: str = "composer.googleapis.com",
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
        host: str = "composer.googleapis.com",
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
                 The hostname to connect to (default: 'composer.googleapis.com').
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
    def create_environment(
        self,
    ) -> Callable[
        [environments.CreateEnvironmentRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the create environment method over gRPC.

        Create a new environment.

        Returns:
            Callable[[~.CreateEnvironmentRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_environment" not in self._stubs:
            self._stubs["create_environment"] = self._logged_channel.unary_unary(
                "/google.cloud.orchestration.airflow.service.v1beta1.Environments/CreateEnvironment",
                request_serializer=environments.CreateEnvironmentRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_environment"]

    @property
    def get_environment(
        self,
    ) -> Callable[
        [environments.GetEnvironmentRequest], Awaitable[environments.Environment]
    ]:
        r"""Return a callable for the get environment method over gRPC.

        Get an existing environment.

        Returns:
            Callable[[~.GetEnvironmentRequest],
                    Awaitable[~.Environment]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_environment" not in self._stubs:
            self._stubs["get_environment"] = self._logged_channel.unary_unary(
                "/google.cloud.orchestration.airflow.service.v1beta1.Environments/GetEnvironment",
                request_serializer=environments.GetEnvironmentRequest.serialize,
                response_deserializer=environments.Environment.deserialize,
            )
        return self._stubs["get_environment"]

    @property
    def list_environments(
        self,
    ) -> Callable[
        [environments.ListEnvironmentsRequest],
        Awaitable[environments.ListEnvironmentsResponse],
    ]:
        r"""Return a callable for the list environments method over gRPC.

        List environments.

        Returns:
            Callable[[~.ListEnvironmentsRequest],
                    Awaitable[~.ListEnvironmentsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_environments" not in self._stubs:
            self._stubs["list_environments"] = self._logged_channel.unary_unary(
                "/google.cloud.orchestration.airflow.service.v1beta1.Environments/ListEnvironments",
                request_serializer=environments.ListEnvironmentsRequest.serialize,
                response_deserializer=environments.ListEnvironmentsResponse.deserialize,
            )
        return self._stubs["list_environments"]

    @property
    def update_environment(
        self,
    ) -> Callable[
        [environments.UpdateEnvironmentRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the update environment method over gRPC.

        Update an environment.

        Returns:
            Callable[[~.UpdateEnvironmentRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_environment" not in self._stubs:
            self._stubs["update_environment"] = self._logged_channel.unary_unary(
                "/google.cloud.orchestration.airflow.service.v1beta1.Environments/UpdateEnvironment",
                request_serializer=environments.UpdateEnvironmentRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_environment"]

    @property
    def delete_environment(
        self,
    ) -> Callable[
        [environments.DeleteEnvironmentRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the delete environment method over gRPC.

        Delete an environment.

        Returns:
            Callable[[~.DeleteEnvironmentRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_environment" not in self._stubs:
            self._stubs["delete_environment"] = self._logged_channel.unary_unary(
                "/google.cloud.orchestration.airflow.service.v1beta1.Environments/DeleteEnvironment",
                request_serializer=environments.DeleteEnvironmentRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_environment"]

    @property
    def restart_web_server(
        self,
    ) -> Callable[
        [environments.RestartWebServerRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the restart web server method over gRPC.

        Restart Airflow web server.

        Returns:
            Callable[[~.RestartWebServerRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "restart_web_server" not in self._stubs:
            self._stubs["restart_web_server"] = self._logged_channel.unary_unary(
                "/google.cloud.orchestration.airflow.service.v1beta1.Environments/RestartWebServer",
                request_serializer=environments.RestartWebServerRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["restart_web_server"]

    @property
    def check_upgrade(
        self,
    ) -> Callable[
        [environments.CheckUpgradeRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the check upgrade method over gRPC.

        Check if an upgrade operation on the environment will
        succeed.
        In case of problems detailed info can be found in the
        returned Operation.

        Returns:
            Callable[[~.CheckUpgradeRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "check_upgrade" not in self._stubs:
            self._stubs["check_upgrade"] = self._logged_channel.unary_unary(
                "/google.cloud.orchestration.airflow.service.v1beta1.Environments/CheckUpgrade",
                request_serializer=environments.CheckUpgradeRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["check_upgrade"]

    @property
    def execute_airflow_command(
        self,
    ) -> Callable[
        [environments.ExecuteAirflowCommandRequest],
        Awaitable[environments.ExecuteAirflowCommandResponse],
    ]:
        r"""Return a callable for the execute airflow command method over gRPC.

        Executes Airflow CLI command.

        Returns:
            Callable[[~.ExecuteAirflowCommandRequest],
                    Awaitable[~.ExecuteAirflowCommandResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "execute_airflow_command" not in self._stubs:
            self._stubs["execute_airflow_command"] = self._logged_channel.unary_unary(
                "/google.cloud.orchestration.airflow.service.v1beta1.Environments/ExecuteAirflowCommand",
                request_serializer=environments.ExecuteAirflowCommandRequest.serialize,
                response_deserializer=environments.ExecuteAirflowCommandResponse.deserialize,
            )
        return self._stubs["execute_airflow_command"]

    @property
    def stop_airflow_command(
        self,
    ) -> Callable[
        [environments.StopAirflowCommandRequest],
        Awaitable[environments.StopAirflowCommandResponse],
    ]:
        r"""Return a callable for the stop airflow command method over gRPC.

        Stops Airflow CLI command execution.

        Returns:
            Callable[[~.StopAirflowCommandRequest],
                    Awaitable[~.StopAirflowCommandResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "stop_airflow_command" not in self._stubs:
            self._stubs["stop_airflow_command"] = self._logged_channel.unary_unary(
                "/google.cloud.orchestration.airflow.service.v1beta1.Environments/StopAirflowCommand",
                request_serializer=environments.StopAirflowCommandRequest.serialize,
                response_deserializer=environments.StopAirflowCommandResponse.deserialize,
            )
        return self._stubs["stop_airflow_command"]

    @property
    def poll_airflow_command(
        self,
    ) -> Callable[
        [environments.PollAirflowCommandRequest],
        Awaitable[environments.PollAirflowCommandResponse],
    ]:
        r"""Return a callable for the poll airflow command method over gRPC.

        Polls Airflow CLI command execution and fetches logs.

        Returns:
            Callable[[~.PollAirflowCommandRequest],
                    Awaitable[~.PollAirflowCommandResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "poll_airflow_command" not in self._stubs:
            self._stubs["poll_airflow_command"] = self._logged_channel.unary_unary(
                "/google.cloud.orchestration.airflow.service.v1beta1.Environments/PollAirflowCommand",
                request_serializer=environments.PollAirflowCommandRequest.serialize,
                response_deserializer=environments.PollAirflowCommandResponse.deserialize,
            )
        return self._stubs["poll_airflow_command"]

    @property
    def list_workloads(
        self,
    ) -> Callable[
        [environments.ListWorkloadsRequest],
        Awaitable[environments.ListWorkloadsResponse],
    ]:
        r"""Return a callable for the list workloads method over gRPC.

        Lists workloads in a Cloud Composer environment. Workload is a
        unit that runs a single Composer component.

        This method is supported for Cloud Composer environments in
        versions composer-2.\ *.*-airflow-*.*.\* and newer.

        Returns:
            Callable[[~.ListWorkloadsRequest],
                    Awaitable[~.ListWorkloadsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_workloads" not in self._stubs:
            self._stubs["list_workloads"] = self._logged_channel.unary_unary(
                "/google.cloud.orchestration.airflow.service.v1beta1.Environments/ListWorkloads",
                request_serializer=environments.ListWorkloadsRequest.serialize,
                response_deserializer=environments.ListWorkloadsResponse.deserialize,
            )
        return self._stubs["list_workloads"]

    @property
    def create_user_workloads_secret(
        self,
    ) -> Callable[
        [environments.CreateUserWorkloadsSecretRequest],
        Awaitable[environments.UserWorkloadsSecret],
    ]:
        r"""Return a callable for the create user workloads secret method over gRPC.

        Creates a user workloads Secret.

        This method is supported for Cloud Composer environments in
        versions composer-3-airflow-*.*.\ *-build.* and newer.

        Returns:
            Callable[[~.CreateUserWorkloadsSecretRequest],
                    Awaitable[~.UserWorkloadsSecret]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_user_workloads_secret" not in self._stubs:
            self._stubs["create_user_workloads_secret"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.orchestration.airflow.service.v1beta1.Environments/CreateUserWorkloadsSecret",
                    request_serializer=environments.CreateUserWorkloadsSecretRequest.serialize,
                    response_deserializer=environments.UserWorkloadsSecret.deserialize,
                )
            )
        return self._stubs["create_user_workloads_secret"]

    @property
    def get_user_workloads_secret(
        self,
    ) -> Callable[
        [environments.GetUserWorkloadsSecretRequest],
        Awaitable[environments.UserWorkloadsSecret],
    ]:
        r"""Return a callable for the get user workloads secret method over gRPC.

        Gets an existing user workloads Secret. Values of the "data"
        field in the response are cleared.

        This method is supported for Cloud Composer environments in
        versions composer-3-airflow-*.*.\ *-build.* and newer.

        Returns:
            Callable[[~.GetUserWorkloadsSecretRequest],
                    Awaitable[~.UserWorkloadsSecret]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_user_workloads_secret" not in self._stubs:
            self._stubs["get_user_workloads_secret"] = self._logged_channel.unary_unary(
                "/google.cloud.orchestration.airflow.service.v1beta1.Environments/GetUserWorkloadsSecret",
                request_serializer=environments.GetUserWorkloadsSecretRequest.serialize,
                response_deserializer=environments.UserWorkloadsSecret.deserialize,
            )
        return self._stubs["get_user_workloads_secret"]

    @property
    def list_user_workloads_secrets(
        self,
    ) -> Callable[
        [environments.ListUserWorkloadsSecretsRequest],
        Awaitable[environments.ListUserWorkloadsSecretsResponse],
    ]:
        r"""Return a callable for the list user workloads secrets method over gRPC.

        Lists user workloads Secrets.

        This method is supported for Cloud Composer environments in
        versions composer-3-airflow-*.*.\ *-build.* and newer.

        Returns:
            Callable[[~.ListUserWorkloadsSecretsRequest],
                    Awaitable[~.ListUserWorkloadsSecretsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_user_workloads_secrets" not in self._stubs:
            self._stubs["list_user_workloads_secrets"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.orchestration.airflow.service.v1beta1.Environments/ListUserWorkloadsSecrets",
                    request_serializer=environments.ListUserWorkloadsSecretsRequest.serialize,
                    response_deserializer=environments.ListUserWorkloadsSecretsResponse.deserialize,
                )
            )
        return self._stubs["list_user_workloads_secrets"]

    @property
    def update_user_workloads_secret(
        self,
    ) -> Callable[
        [environments.UpdateUserWorkloadsSecretRequest],
        Awaitable[environments.UserWorkloadsSecret],
    ]:
        r"""Return a callable for the update user workloads secret method over gRPC.

        Updates a user workloads Secret.

        This method is supported for Cloud Composer environments in
        versions composer-3-airflow-*.*.\ *-build.* and newer.

        Returns:
            Callable[[~.UpdateUserWorkloadsSecretRequest],
                    Awaitable[~.UserWorkloadsSecret]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_user_workloads_secret" not in self._stubs:
            self._stubs["update_user_workloads_secret"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.orchestration.airflow.service.v1beta1.Environments/UpdateUserWorkloadsSecret",
                    request_serializer=environments.UpdateUserWorkloadsSecretRequest.serialize,
                    response_deserializer=environments.UserWorkloadsSecret.deserialize,
                )
            )
        return self._stubs["update_user_workloads_secret"]

    @property
    def delete_user_workloads_secret(
        self,
    ) -> Callable[
        [environments.DeleteUserWorkloadsSecretRequest], Awaitable[empty_pb2.Empty]
    ]:
        r"""Return a callable for the delete user workloads secret method over gRPC.

        Deletes a user workloads Secret.

        This method is supported for Cloud Composer environments in
        versions composer-3-airflow-*.*.\ *-build.* and newer.

        Returns:
            Callable[[~.DeleteUserWorkloadsSecretRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_user_workloads_secret" not in self._stubs:
            self._stubs["delete_user_workloads_secret"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.orchestration.airflow.service.v1beta1.Environments/DeleteUserWorkloadsSecret",
                    request_serializer=environments.DeleteUserWorkloadsSecretRequest.serialize,
                    response_deserializer=empty_pb2.Empty.FromString,
                )
            )
        return self._stubs["delete_user_workloads_secret"]

    @property
    def create_user_workloads_config_map(
        self,
    ) -> Callable[
        [environments.CreateUserWorkloadsConfigMapRequest],
        Awaitable[environments.UserWorkloadsConfigMap],
    ]:
        r"""Return a callable for the create user workloads config
        map method over gRPC.

        Creates a user workloads ConfigMap.

        This method is supported for Cloud Composer environments in
        versions composer-3-airflow-*.*.\ *-build.* and newer.

        Returns:
            Callable[[~.CreateUserWorkloadsConfigMapRequest],
                    Awaitable[~.UserWorkloadsConfigMap]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_user_workloads_config_map" not in self._stubs:
            self._stubs["create_user_workloads_config_map"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.orchestration.airflow.service.v1beta1.Environments/CreateUserWorkloadsConfigMap",
                    request_serializer=environments.CreateUserWorkloadsConfigMapRequest.serialize,
                    response_deserializer=environments.UserWorkloadsConfigMap.deserialize,
                )
            )
        return self._stubs["create_user_workloads_config_map"]

    @property
    def get_user_workloads_config_map(
        self,
    ) -> Callable[
        [environments.GetUserWorkloadsConfigMapRequest],
        Awaitable[environments.UserWorkloadsConfigMap],
    ]:
        r"""Return a callable for the get user workloads config map method over gRPC.

        Gets an existing user workloads ConfigMap.

        This method is supported for Cloud Composer environments in
        versions composer-3-airflow-*.*.\ *-build.* and newer.

        Returns:
            Callable[[~.GetUserWorkloadsConfigMapRequest],
                    Awaitable[~.UserWorkloadsConfigMap]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_user_workloads_config_map" not in self._stubs:
            self._stubs["get_user_workloads_config_map"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.orchestration.airflow.service.v1beta1.Environments/GetUserWorkloadsConfigMap",
                    request_serializer=environments.GetUserWorkloadsConfigMapRequest.serialize,
                    response_deserializer=environments.UserWorkloadsConfigMap.deserialize,
                )
            )
        return self._stubs["get_user_workloads_config_map"]

    @property
    def list_user_workloads_config_maps(
        self,
    ) -> Callable[
        [environments.ListUserWorkloadsConfigMapsRequest],
        Awaitable[environments.ListUserWorkloadsConfigMapsResponse],
    ]:
        r"""Return a callable for the list user workloads config
        maps method over gRPC.

        Lists user workloads ConfigMaps.

        This method is supported for Cloud Composer environments in
        versions composer-3-airflow-*.*.\ *-build.* and newer.

        Returns:
            Callable[[~.ListUserWorkloadsConfigMapsRequest],
                    Awaitable[~.ListUserWorkloadsConfigMapsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_user_workloads_config_maps" not in self._stubs:
            self._stubs["list_user_workloads_config_maps"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.orchestration.airflow.service.v1beta1.Environments/ListUserWorkloadsConfigMaps",
                    request_serializer=environments.ListUserWorkloadsConfigMapsRequest.serialize,
                    response_deserializer=environments.ListUserWorkloadsConfigMapsResponse.deserialize,
                )
            )
        return self._stubs["list_user_workloads_config_maps"]

    @property
    def update_user_workloads_config_map(
        self,
    ) -> Callable[
        [environments.UpdateUserWorkloadsConfigMapRequest],
        Awaitable[environments.UserWorkloadsConfigMap],
    ]:
        r"""Return a callable for the update user workloads config
        map method over gRPC.

        Updates a user workloads ConfigMap.

        This method is supported for Cloud Composer environments in
        versions composer-3-airflow-*.*.\ *-build.* and newer.

        Returns:
            Callable[[~.UpdateUserWorkloadsConfigMapRequest],
                    Awaitable[~.UserWorkloadsConfigMap]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_user_workloads_config_map" not in self._stubs:
            self._stubs["update_user_workloads_config_map"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.orchestration.airflow.service.v1beta1.Environments/UpdateUserWorkloadsConfigMap",
                    request_serializer=environments.UpdateUserWorkloadsConfigMapRequest.serialize,
                    response_deserializer=environments.UserWorkloadsConfigMap.deserialize,
                )
            )
        return self._stubs["update_user_workloads_config_map"]

    @property
    def delete_user_workloads_config_map(
        self,
    ) -> Callable[
        [environments.DeleteUserWorkloadsConfigMapRequest], Awaitable[empty_pb2.Empty]
    ]:
        r"""Return a callable for the delete user workloads config
        map method over gRPC.

        Deletes a user workloads ConfigMap.

        This method is supported for Cloud Composer environments in
        versions composer-3-airflow-*.*.\ *-build.* and newer.

        Returns:
            Callable[[~.DeleteUserWorkloadsConfigMapRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_user_workloads_config_map" not in self._stubs:
            self._stubs["delete_user_workloads_config_map"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.orchestration.airflow.service.v1beta1.Environments/DeleteUserWorkloadsConfigMap",
                    request_serializer=environments.DeleteUserWorkloadsConfigMapRequest.serialize,
                    response_deserializer=empty_pb2.Empty.FromString,
                )
            )
        return self._stubs["delete_user_workloads_config_map"]

    @property
    def save_snapshot(
        self,
    ) -> Callable[
        [environments.SaveSnapshotRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the save snapshot method over gRPC.

        Creates a snapshots of a Cloud Composer environment.

        As a result of this operation, snapshot of environment's
        state is stored in a location specified in the
        SaveSnapshotRequest.

        Returns:
            Callable[[~.SaveSnapshotRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "save_snapshot" not in self._stubs:
            self._stubs["save_snapshot"] = self._logged_channel.unary_unary(
                "/google.cloud.orchestration.airflow.service.v1beta1.Environments/SaveSnapshot",
                request_serializer=environments.SaveSnapshotRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["save_snapshot"]

    @property
    def load_snapshot(
        self,
    ) -> Callable[
        [environments.LoadSnapshotRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the load snapshot method over gRPC.

        Loads a snapshot of a Cloud Composer environment.

        As a result of this operation, a snapshot of
        environment's specified in LoadSnapshotRequest is loaded
        into the environment.

        Returns:
            Callable[[~.LoadSnapshotRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "load_snapshot" not in self._stubs:
            self._stubs["load_snapshot"] = self._logged_channel.unary_unary(
                "/google.cloud.orchestration.airflow.service.v1beta1.Environments/LoadSnapshot",
                request_serializer=environments.LoadSnapshotRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["load_snapshot"]

    @property
    def database_failover(
        self,
    ) -> Callable[
        [environments.DatabaseFailoverRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the database failover method over gRPC.

        Triggers database failover (only for highly resilient
        environments).

        Returns:
            Callable[[~.DatabaseFailoverRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "database_failover" not in self._stubs:
            self._stubs["database_failover"] = self._logged_channel.unary_unary(
                "/google.cloud.orchestration.airflow.service.v1beta1.Environments/DatabaseFailover",
                request_serializer=environments.DatabaseFailoverRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["database_failover"]

    @property
    def fetch_database_properties(
        self,
    ) -> Callable[
        [environments.FetchDatabasePropertiesRequest],
        Awaitable[environments.FetchDatabasePropertiesResponse],
    ]:
        r"""Return a callable for the fetch database properties method over gRPC.

        Fetches database properties.

        Returns:
            Callable[[~.FetchDatabasePropertiesRequest],
                    Awaitable[~.FetchDatabasePropertiesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "fetch_database_properties" not in self._stubs:
            self._stubs["fetch_database_properties"] = self._logged_channel.unary_unary(
                "/google.cloud.orchestration.airflow.service.v1beta1.Environments/FetchDatabaseProperties",
                request_serializer=environments.FetchDatabasePropertiesRequest.serialize,
                response_deserializer=environments.FetchDatabasePropertiesResponse.deserialize,
            )
        return self._stubs["fetch_database_properties"]

    def _prep_wrapped_messages(self, client_info):
        """Precompute the wrapped methods, overriding the base class method to use async wrappers."""
        self._wrapped_methods = {
            self.create_environment: self._wrap_method(
                self.create_environment,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_environment: self._wrap_method(
                self.get_environment,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_environments: self._wrap_method(
                self.list_environments,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_environment: self._wrap_method(
                self.update_environment,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_environment: self._wrap_method(
                self.delete_environment,
                default_timeout=None,
                client_info=client_info,
            ),
            self.restart_web_server: self._wrap_method(
                self.restart_web_server,
                default_timeout=None,
                client_info=client_info,
            ),
            self.check_upgrade: self._wrap_method(
                self.check_upgrade,
                default_timeout=None,
                client_info=client_info,
            ),
            self.execute_airflow_command: self._wrap_method(
                self.execute_airflow_command,
                default_timeout=None,
                client_info=client_info,
            ),
            self.stop_airflow_command: self._wrap_method(
                self.stop_airflow_command,
                default_timeout=None,
                client_info=client_info,
            ),
            self.poll_airflow_command: self._wrap_method(
                self.poll_airflow_command,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_workloads: self._wrap_method(
                self.list_workloads,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_user_workloads_secret: self._wrap_method(
                self.create_user_workloads_secret,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_user_workloads_secret: self._wrap_method(
                self.get_user_workloads_secret,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_user_workloads_secrets: self._wrap_method(
                self.list_user_workloads_secrets,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_user_workloads_secret: self._wrap_method(
                self.update_user_workloads_secret,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_user_workloads_secret: self._wrap_method(
                self.delete_user_workloads_secret,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_user_workloads_config_map: self._wrap_method(
                self.create_user_workloads_config_map,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_user_workloads_config_map: self._wrap_method(
                self.get_user_workloads_config_map,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_user_workloads_config_maps: self._wrap_method(
                self.list_user_workloads_config_maps,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_user_workloads_config_map: self._wrap_method(
                self.update_user_workloads_config_map,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_user_workloads_config_map: self._wrap_method(
                self.delete_user_workloads_config_map,
                default_timeout=None,
                client_info=client_info,
            ),
            self.save_snapshot: self._wrap_method(
                self.save_snapshot,
                default_timeout=None,
                client_info=client_info,
            ),
            self.load_snapshot: self._wrap_method(
                self.load_snapshot,
                default_timeout=None,
                client_info=client_info,
            ),
            self.database_failover: self._wrap_method(
                self.database_failover,
                default_timeout=None,
                client_info=client_info,
            ),
            self.fetch_database_properties: self._wrap_method(
                self.fetch_database_properties,
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


__all__ = ("EnvironmentsGrpcAsyncIOTransport",)
