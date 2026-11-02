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

from google.cloud.datacatalog_lineage_v1.types import lineage

from .base import DEFAULT_CLIENT_INFO, LineageTransport
from .grpc import LineageGrpcTransport

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
                    "serviceName": "google.cloud.datacatalog.lineage.v1.Lineage",
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
                    "serviceName": "google.cloud.datacatalog.lineage.v1.Lineage",
                    "rpcName": str(client_call_details.method),
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class LineageGrpcAsyncIOTransport(LineageTransport):
    """gRPC AsyncIO backend transport for Lineage.

    Lineage is used to track data flows between assets over time. You
    can create
    [LineageEvents][google.cloud.datacatalog.lineage.v1.LineageEvent] to
    record lineage between multiple sources and a single target, for
    example, when table data is based on data from multiple tables.

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
        host: str = "datalineage.googleapis.com",
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
        host: str = "datalineage.googleapis.com",
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
                 The hostname to connect to (default: 'datalineage.googleapis.com').
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
    def process_open_lineage_run_event(
        self,
    ) -> Callable[
        [lineage.ProcessOpenLineageRunEventRequest],
        Awaitable[lineage.ProcessOpenLineageRunEventResponse],
    ]:
        r"""Return a callable for the process open lineage run event method over gRPC.

        Creates new lineage events together with their
        parents: process and run. Updates the process and run if
        they already exist. Mapped from Open Lineage
        specification:

        https://github.com/OpenLineage/OpenLineage/blob/main/spec/OpenLineage.json.

        Returns:
            Callable[[~.ProcessOpenLineageRunEventRequest],
                    Awaitable[~.ProcessOpenLineageRunEventResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "process_open_lineage_run_event" not in self._stubs:
            self._stubs["process_open_lineage_run_event"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.datacatalog.lineage.v1.Lineage/ProcessOpenLineageRunEvent",
                    request_serializer=lineage.ProcessOpenLineageRunEventRequest.serialize,
                    response_deserializer=lineage.ProcessOpenLineageRunEventResponse.deserialize,
                )
            )
        return self._stubs["process_open_lineage_run_event"]

    @property
    def create_process(
        self,
    ) -> Callable[[lineage.CreateProcessRequest], Awaitable[lineage.Process]]:
        r"""Return a callable for the create process method over gRPC.

        Creates a new process.

        Returns:
            Callable[[~.CreateProcessRequest],
                    Awaitable[~.Process]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_process" not in self._stubs:
            self._stubs["create_process"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.lineage.v1.Lineage/CreateProcess",
                request_serializer=lineage.CreateProcessRequest.serialize,
                response_deserializer=lineage.Process.deserialize,
            )
        return self._stubs["create_process"]

    @property
    def update_process(
        self,
    ) -> Callable[[lineage.UpdateProcessRequest], Awaitable[lineage.Process]]:
        r"""Return a callable for the update process method over gRPC.

        Updates a process.

        Returns:
            Callable[[~.UpdateProcessRequest],
                    Awaitable[~.Process]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_process" not in self._stubs:
            self._stubs["update_process"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.lineage.v1.Lineage/UpdateProcess",
                request_serializer=lineage.UpdateProcessRequest.serialize,
                response_deserializer=lineage.Process.deserialize,
            )
        return self._stubs["update_process"]

    @property
    def get_process(
        self,
    ) -> Callable[[lineage.GetProcessRequest], Awaitable[lineage.Process]]:
        r"""Return a callable for the get process method over gRPC.

        Gets the details of the specified process.

        Returns:
            Callable[[~.GetProcessRequest],
                    Awaitable[~.Process]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_process" not in self._stubs:
            self._stubs["get_process"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.lineage.v1.Lineage/GetProcess",
                request_serializer=lineage.GetProcessRequest.serialize,
                response_deserializer=lineage.Process.deserialize,
            )
        return self._stubs["get_process"]

    @property
    def list_processes(
        self,
    ) -> Callable[
        [lineage.ListProcessesRequest], Awaitable[lineage.ListProcessesResponse]
    ]:
        r"""Return a callable for the list processes method over gRPC.

        List processes in the given project and location.
        List order is descending by insertion time.

        Returns:
            Callable[[~.ListProcessesRequest],
                    Awaitable[~.ListProcessesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_processes" not in self._stubs:
            self._stubs["list_processes"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.lineage.v1.Lineage/ListProcesses",
                request_serializer=lineage.ListProcessesRequest.serialize,
                response_deserializer=lineage.ListProcessesResponse.deserialize,
            )
        return self._stubs["list_processes"]

    @property
    def delete_process(
        self,
    ) -> Callable[[lineage.DeleteProcessRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the delete process method over gRPC.

        Deletes the process with the specified name.

        Returns:
            Callable[[~.DeleteProcessRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_process" not in self._stubs:
            self._stubs["delete_process"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.lineage.v1.Lineage/DeleteProcess",
                request_serializer=lineage.DeleteProcessRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_process"]

    @property
    def create_run(
        self,
    ) -> Callable[[lineage.CreateRunRequest], Awaitable[lineage.Run]]:
        r"""Return a callable for the create run method over gRPC.

        Creates a new run.

        Returns:
            Callable[[~.CreateRunRequest],
                    Awaitable[~.Run]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_run" not in self._stubs:
            self._stubs["create_run"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.lineage.v1.Lineage/CreateRun",
                request_serializer=lineage.CreateRunRequest.serialize,
                response_deserializer=lineage.Run.deserialize,
            )
        return self._stubs["create_run"]

    @property
    def update_run(
        self,
    ) -> Callable[[lineage.UpdateRunRequest], Awaitable[lineage.Run]]:
        r"""Return a callable for the update run method over gRPC.

        Updates a run.

        Returns:
            Callable[[~.UpdateRunRequest],
                    Awaitable[~.Run]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_run" not in self._stubs:
            self._stubs["update_run"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.lineage.v1.Lineage/UpdateRun",
                request_serializer=lineage.UpdateRunRequest.serialize,
                response_deserializer=lineage.Run.deserialize,
            )
        return self._stubs["update_run"]

    @property
    def get_run(self) -> Callable[[lineage.GetRunRequest], Awaitable[lineage.Run]]:
        r"""Return a callable for the get run method over gRPC.

        Gets the details of the specified run.

        Returns:
            Callable[[~.GetRunRequest],
                    Awaitable[~.Run]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_run" not in self._stubs:
            self._stubs["get_run"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.lineage.v1.Lineage/GetRun",
                request_serializer=lineage.GetRunRequest.serialize,
                response_deserializer=lineage.Run.deserialize,
            )
        return self._stubs["get_run"]

    @property
    def list_runs(
        self,
    ) -> Callable[[lineage.ListRunsRequest], Awaitable[lineage.ListRunsResponse]]:
        r"""Return a callable for the list runs method over gRPC.

        Lists runs in the given project and location. List order is
        descending by ``start_time``.

        Returns:
            Callable[[~.ListRunsRequest],
                    Awaitable[~.ListRunsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_runs" not in self._stubs:
            self._stubs["list_runs"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.lineage.v1.Lineage/ListRuns",
                request_serializer=lineage.ListRunsRequest.serialize,
                response_deserializer=lineage.ListRunsResponse.deserialize,
            )
        return self._stubs["list_runs"]

    @property
    def delete_run(
        self,
    ) -> Callable[[lineage.DeleteRunRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the delete run method over gRPC.

        Deletes the run with the specified name.

        Returns:
            Callable[[~.DeleteRunRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_run" not in self._stubs:
            self._stubs["delete_run"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.lineage.v1.Lineage/DeleteRun",
                request_serializer=lineage.DeleteRunRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_run"]

    @property
    def create_lineage_event(
        self,
    ) -> Callable[[lineage.CreateLineageEventRequest], Awaitable[lineage.LineageEvent]]:
        r"""Return a callable for the create lineage event method over gRPC.

        Creates a new lineage event.

        Returns:
            Callable[[~.CreateLineageEventRequest],
                    Awaitable[~.LineageEvent]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_lineage_event" not in self._stubs:
            self._stubs["create_lineage_event"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.lineage.v1.Lineage/CreateLineageEvent",
                request_serializer=lineage.CreateLineageEventRequest.serialize,
                response_deserializer=lineage.LineageEvent.deserialize,
            )
        return self._stubs["create_lineage_event"]

    @property
    def get_lineage_event(
        self,
    ) -> Callable[[lineage.GetLineageEventRequest], Awaitable[lineage.LineageEvent]]:
        r"""Return a callable for the get lineage event method over gRPC.

        Gets details of a specified lineage event.

        Returns:
            Callable[[~.GetLineageEventRequest],
                    Awaitable[~.LineageEvent]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_lineage_event" not in self._stubs:
            self._stubs["get_lineage_event"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.lineage.v1.Lineage/GetLineageEvent",
                request_serializer=lineage.GetLineageEventRequest.serialize,
                response_deserializer=lineage.LineageEvent.deserialize,
            )
        return self._stubs["get_lineage_event"]

    @property
    def list_lineage_events(
        self,
    ) -> Callable[
        [lineage.ListLineageEventsRequest], Awaitable[lineage.ListLineageEventsResponse]
    ]:
        r"""Return a callable for the list lineage events method over gRPC.

        Lists lineage events in the given project and
        location. The list order is not defined.

        Returns:
            Callable[[~.ListLineageEventsRequest],
                    Awaitable[~.ListLineageEventsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_lineage_events" not in self._stubs:
            self._stubs["list_lineage_events"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.lineage.v1.Lineage/ListLineageEvents",
                request_serializer=lineage.ListLineageEventsRequest.serialize,
                response_deserializer=lineage.ListLineageEventsResponse.deserialize,
            )
        return self._stubs["list_lineage_events"]

    @property
    def delete_lineage_event(
        self,
    ) -> Callable[[lineage.DeleteLineageEventRequest], Awaitable[empty_pb2.Empty]]:
        r"""Return a callable for the delete lineage event method over gRPC.

        Deletes the lineage event with the specified name.

        Returns:
            Callable[[~.DeleteLineageEventRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_lineage_event" not in self._stubs:
            self._stubs["delete_lineage_event"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.lineage.v1.Lineage/DeleteLineageEvent",
                request_serializer=lineage.DeleteLineageEventRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_lineage_event"]

    @property
    def search_links(
        self,
    ) -> Callable[[lineage.SearchLinksRequest], Awaitable[lineage.SearchLinksResponse]]:
        r"""Return a callable for the search links method over gRPC.

        Retrieve a list of links connected to a specific asset. Links
        represent the data flow between **source** (upstream) and
        **target** (downstream) assets in transformation pipelines.
        Links are stored in the same project as the Lineage Events that
        create them.

        You can retrieve links in every project where you have the
        ``datalineage.events.get`` permission. The project provided in
        the URL is used for Billing and Quota.

        Returns:
            Callable[[~.SearchLinksRequest],
                    Awaitable[~.SearchLinksResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "search_links" not in self._stubs:
            self._stubs["search_links"] = self._logged_channel.unary_unary(
                "/google.cloud.datacatalog.lineage.v1.Lineage/SearchLinks",
                request_serializer=lineage.SearchLinksRequest.serialize,
                response_deserializer=lineage.SearchLinksResponse.deserialize,
            )
        return self._stubs["search_links"]

    @property
    def batch_search_link_processes(
        self,
    ) -> Callable[
        [lineage.BatchSearchLinkProcessesRequest],
        Awaitable[lineage.BatchSearchLinkProcessesResponse],
    ]:
        r"""Return a callable for the batch search link processes method over gRPC.

        Retrieve information about LineageProcesses associated with
        specific links. LineageProcesses are transformation pipelines
        that result in data flowing from **source** to **target**
        assets. Links between assets represent this operation.

        If you have specific link names, you can use this method to
        verify which LineageProcesses contribute to creating those
        links. See the
        [SearchLinks][google.cloud.datacatalog.lineage.v1.Lineage.SearchLinks]
        method for more information on how to retrieve link name.

        You can retrieve the LineageProcess information in every project
        where you have the ``datalineage.events.get`` permission. The
        project provided in the URL is used for Billing and Quota.

        Returns:
            Callable[[~.BatchSearchLinkProcessesRequest],
                    Awaitable[~.BatchSearchLinkProcessesResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "batch_search_link_processes" not in self._stubs:
            self._stubs["batch_search_link_processes"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.datacatalog.lineage.v1.Lineage/BatchSearchLinkProcesses",
                    request_serializer=lineage.BatchSearchLinkProcessesRequest.serialize,
                    response_deserializer=lineage.BatchSearchLinkProcessesResponse.deserialize,
                )
            )
        return self._stubs["batch_search_link_processes"]

    @property
    def search_lineage_streaming(
        self,
    ) -> Callable[
        [lineage.SearchLineageStreamingRequest],
        Awaitable[lineage.SearchLineageStreamingResponse],
    ]:
        r"""Return a callable for the search lineage streaming method over gRPC.

        Retrieves a streaming response of lineage links connected to the
        requested assets by performing a breadth-first search in the
        given direction. Links represent the data flow between
        **source** (upstream) and **target** (downstream) assets in
        transformation pipelines. Links are stored in the same project
        as the Lineage Events that create them. This method retrieves
        links from all valid locations provided in the request. This
        method supports Column-Level Lineage (CLL) along with wildcard
        support to retrieve all CLL for an Entity FQN.

        Following permissions are required to retrieve links:

        - ``datalineage.events.get`` permission for the project where
          the link is stored for entity-level lineage.
        - ``datalineage.events.getFields`` permission for the project
          where the link is stored for column-level lineage.

        This method also returns processes that created the links if
        explicitly requested by setting
        `max_process_per_link <google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequest.limits.max_process_per_link>`__
        is non-zero and full process details are requested via
        ``links.processes.process`` in the
        `FieldMask <https://developers.google.com/workspace/docs/api/how-tos/field-masks#read_with_a_field_mask>`__.

        Permission required to retrieve processes:

        - ``datalineage.processes.get`` permission for the project where
          the process is stored.

        Returns:
            Callable[[~.SearchLineageStreamingRequest],
                    Awaitable[~.SearchLineageStreamingResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "search_lineage_streaming" not in self._stubs:
            self._stubs["search_lineage_streaming"] = self._logged_channel.unary_stream(
                "/google.cloud.datacatalog.lineage.v1.Lineage/SearchLineageStreaming",
                request_serializer=lineage.SearchLineageStreamingRequest.serialize,
                response_deserializer=lineage.SearchLineageStreamingResponse.deserialize,
            )
        return self._stubs["search_lineage_streaming"]

    def _prep_wrapped_messages(self, client_info):
        """Precompute the wrapped methods, overriding the base class method to use async wrappers."""
        self._wrapped_methods = {
            self.process_open_lineage_run_event: self._wrap_method(
                self.process_open_lineage_run_event,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_process: self._wrap_method(
                self.create_process,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_process: self._wrap_method(
                self.update_process,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_process: self._wrap_method(
                self.get_process,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_processes: self._wrap_method(
                self.list_processes,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_process: self._wrap_method(
                self.delete_process,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_run: self._wrap_method(
                self.create_run,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_run: self._wrap_method(
                self.update_run,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_run: self._wrap_method(
                self.get_run,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_runs: self._wrap_method(
                self.list_runs,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_run: self._wrap_method(
                self.delete_run,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_lineage_event: self._wrap_method(
                self.create_lineage_event,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_lineage_event: self._wrap_method(
                self.get_lineage_event,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_lineage_events: self._wrap_method(
                self.list_lineage_events,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_lineage_event: self._wrap_method(
                self.delete_lineage_event,
                default_timeout=None,
                client_info=client_info,
            ),
            self.search_links: self._wrap_method(
                self.search_links,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_search_link_processes: self._wrap_method(
                self.batch_search_link_processes,
                default_timeout=None,
                client_info=client_info,
            ),
            self.search_lineage_streaming: self._wrap_method(
                self.search_lineage_streaming,
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


__all__ = ("LineageGrpcAsyncIOTransport",)
