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
from google.api_core import gapic_v1, grpc_helpers
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.protobuf.json_format import MessageToJson

from google.cloud.bigquery_datatransfer_v1.types import datatransfer, transfer

from .base import DEFAULT_CLIENT_INFO, DataTransferServiceTransport

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
                    "serviceName": "google.cloud.bigquery.datatransfer.v1.DataTransferService",
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
                    "serviceName": "google.cloud.bigquery.datatransfer.v1.DataTransferService",
                    "rpcName": client_call_details.method,
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class DataTransferServiceGrpcTransport(DataTransferServiceTransport):
    """gRPC backend transport for DataTransferService.

    This API allows users to manage their data transfers into
    BigQuery.

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
        host: str = "bigquerydatatransfer.googleapis.com",
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
                 The hostname to connect to (default: 'bigquerydatatransfer.googleapis.com').
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
        host: str = "bigquerydatatransfer.googleapis.com",
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
    def get_data_source(
        self,
    ) -> Callable[[datatransfer.GetDataSourceRequest], datatransfer.DataSource]:
        r"""Return a callable for the get data source method over gRPC.

        Retrieves a supported data source and returns its
        settings.

        Returns:
            Callable[[~.GetDataSourceRequest],
                    ~.DataSource]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_data_source" not in self._stubs:
            self._stubs["get_data_source"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.datatransfer.v1.DataTransferService/GetDataSource",
                request_serializer=datatransfer.GetDataSourceRequest.serialize,
                response_deserializer=datatransfer.DataSource.deserialize,
            )
        return self._stubs["get_data_source"]

    @property
    def list_data_sources(
        self,
    ) -> Callable[
        [datatransfer.ListDataSourcesRequest], datatransfer.ListDataSourcesResponse
    ]:
        r"""Return a callable for the list data sources method over gRPC.

        Lists supported data sources and returns their
        settings.

        Returns:
            Callable[[~.ListDataSourcesRequest],
                    ~.ListDataSourcesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_data_sources" not in self._stubs:
            self._stubs["list_data_sources"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.datatransfer.v1.DataTransferService/ListDataSources",
                request_serializer=datatransfer.ListDataSourcesRequest.serialize,
                response_deserializer=datatransfer.ListDataSourcesResponse.deserialize,
            )
        return self._stubs["list_data_sources"]

    @property
    def create_transfer_config(
        self,
    ) -> Callable[[datatransfer.CreateTransferConfigRequest], transfer.TransferConfig]:
        r"""Return a callable for the create transfer config method over gRPC.

        Creates a new data transfer configuration.

        Returns:
            Callable[[~.CreateTransferConfigRequest],
                    ~.TransferConfig]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_transfer_config" not in self._stubs:
            self._stubs["create_transfer_config"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.datatransfer.v1.DataTransferService/CreateTransferConfig",
                request_serializer=datatransfer.CreateTransferConfigRequest.serialize,
                response_deserializer=transfer.TransferConfig.deserialize,
            )
        return self._stubs["create_transfer_config"]

    @property
    def update_transfer_config(
        self,
    ) -> Callable[[datatransfer.UpdateTransferConfigRequest], transfer.TransferConfig]:
        r"""Return a callable for the update transfer config method over gRPC.

        Updates a data transfer configuration.
        All fields must be set, even if they are not updated.

        Returns:
            Callable[[~.UpdateTransferConfigRequest],
                    ~.TransferConfig]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_transfer_config" not in self._stubs:
            self._stubs["update_transfer_config"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.datatransfer.v1.DataTransferService/UpdateTransferConfig",
                request_serializer=datatransfer.UpdateTransferConfigRequest.serialize,
                response_deserializer=transfer.TransferConfig.deserialize,
            )
        return self._stubs["update_transfer_config"]

    @property
    def delete_transfer_config(
        self,
    ) -> Callable[[datatransfer.DeleteTransferConfigRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete transfer config method over gRPC.

        Deletes a data transfer configuration, including any
        associated transfer runs and logs.

        Returns:
            Callable[[~.DeleteTransferConfigRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_transfer_config" not in self._stubs:
            self._stubs["delete_transfer_config"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.datatransfer.v1.DataTransferService/DeleteTransferConfig",
                request_serializer=datatransfer.DeleteTransferConfigRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_transfer_config"]

    @property
    def get_transfer_config(
        self,
    ) -> Callable[[datatransfer.GetTransferConfigRequest], transfer.TransferConfig]:
        r"""Return a callable for the get transfer config method over gRPC.

        Returns information about a data transfer config.

        Returns:
            Callable[[~.GetTransferConfigRequest],
                    ~.TransferConfig]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_transfer_config" not in self._stubs:
            self._stubs["get_transfer_config"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.datatransfer.v1.DataTransferService/GetTransferConfig",
                request_serializer=datatransfer.GetTransferConfigRequest.serialize,
                response_deserializer=transfer.TransferConfig.deserialize,
            )
        return self._stubs["get_transfer_config"]

    @property
    def list_transfer_configs(
        self,
    ) -> Callable[
        [datatransfer.ListTransferConfigsRequest],
        datatransfer.ListTransferConfigsResponse,
    ]:
        r"""Return a callable for the list transfer configs method over gRPC.

        Returns information about all transfer configs owned
        by a project in the specified location.

        Returns:
            Callable[[~.ListTransferConfigsRequest],
                    ~.ListTransferConfigsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_transfer_configs" not in self._stubs:
            self._stubs["list_transfer_configs"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.datatransfer.v1.DataTransferService/ListTransferConfigs",
                request_serializer=datatransfer.ListTransferConfigsRequest.serialize,
                response_deserializer=datatransfer.ListTransferConfigsResponse.deserialize,
            )
        return self._stubs["list_transfer_configs"]

    @property
    def schedule_transfer_runs(
        self,
    ) -> Callable[
        [datatransfer.ScheduleTransferRunsRequest],
        datatransfer.ScheduleTransferRunsResponse,
    ]:
        r"""Return a callable for the schedule transfer runs method over gRPC.

        Creates transfer runs for a time range [start_time, end_time].
        For each date - or whatever granularity the data source supports
        - in the range, one transfer run is created. Note that runs are
        created per UTC time in the time range. DEPRECATED: use
        StartManualTransferRuns instead.

        Returns:
            Callable[[~.ScheduleTransferRunsRequest],
                    ~.ScheduleTransferRunsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "schedule_transfer_runs" not in self._stubs:
            self._stubs["schedule_transfer_runs"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.datatransfer.v1.DataTransferService/ScheduleTransferRuns",
                request_serializer=datatransfer.ScheduleTransferRunsRequest.serialize,
                response_deserializer=datatransfer.ScheduleTransferRunsResponse.deserialize,
            )
        return self._stubs["schedule_transfer_runs"]

    @property
    def start_manual_transfer_runs(
        self,
    ) -> Callable[
        [datatransfer.StartManualTransferRunsRequest],
        datatransfer.StartManualTransferRunsResponse,
    ]:
        r"""Return a callable for the start manual transfer runs method over gRPC.

        Start manual transfer runs to be executed now with schedule_time
        equal to current time. The transfer runs can be created for a
        time range where the run_time is between start_time (inclusive)
        and end_time (exclusive), or for a specific run_time.

        Returns:
            Callable[[~.StartManualTransferRunsRequest],
                    ~.StartManualTransferRunsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "start_manual_transfer_runs" not in self._stubs:
            self._stubs["start_manual_transfer_runs"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.bigquery.datatransfer.v1.DataTransferService/StartManualTransferRuns",
                    request_serializer=datatransfer.StartManualTransferRunsRequest.serialize,
                    response_deserializer=datatransfer.StartManualTransferRunsResponse.deserialize,
                )
            )
        return self._stubs["start_manual_transfer_runs"]

    @property
    def get_transfer_run(
        self,
    ) -> Callable[[datatransfer.GetTransferRunRequest], transfer.TransferRun]:
        r"""Return a callable for the get transfer run method over gRPC.

        Returns information about the particular transfer
        run.

        Returns:
            Callable[[~.GetTransferRunRequest],
                    ~.TransferRun]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_transfer_run" not in self._stubs:
            self._stubs["get_transfer_run"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.datatransfer.v1.DataTransferService/GetTransferRun",
                request_serializer=datatransfer.GetTransferRunRequest.serialize,
                response_deserializer=transfer.TransferRun.deserialize,
            )
        return self._stubs["get_transfer_run"]

    @property
    def delete_transfer_run(
        self,
    ) -> Callable[[datatransfer.DeleteTransferRunRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete transfer run method over gRPC.

        Deletes the specified transfer run.

        Returns:
            Callable[[~.DeleteTransferRunRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_transfer_run" not in self._stubs:
            self._stubs["delete_transfer_run"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.datatransfer.v1.DataTransferService/DeleteTransferRun",
                request_serializer=datatransfer.DeleteTransferRunRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_transfer_run"]

    @property
    def list_transfer_runs(
        self,
    ) -> Callable[
        [datatransfer.ListTransferRunsRequest], datatransfer.ListTransferRunsResponse
    ]:
        r"""Return a callable for the list transfer runs method over gRPC.

        Returns information about running and completed
        transfer runs.

        Returns:
            Callable[[~.ListTransferRunsRequest],
                    ~.ListTransferRunsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_transfer_runs" not in self._stubs:
            self._stubs["list_transfer_runs"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.datatransfer.v1.DataTransferService/ListTransferRuns",
                request_serializer=datatransfer.ListTransferRunsRequest.serialize,
                response_deserializer=datatransfer.ListTransferRunsResponse.deserialize,
            )
        return self._stubs["list_transfer_runs"]

    @property
    def list_transfer_logs(
        self,
    ) -> Callable[
        [datatransfer.ListTransferLogsRequest], datatransfer.ListTransferLogsResponse
    ]:
        r"""Return a callable for the list transfer logs method over gRPC.

        Returns log messages for the transfer run.

        Returns:
            Callable[[~.ListTransferLogsRequest],
                    ~.ListTransferLogsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_transfer_logs" not in self._stubs:
            self._stubs["list_transfer_logs"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.datatransfer.v1.DataTransferService/ListTransferLogs",
                request_serializer=datatransfer.ListTransferLogsRequest.serialize,
                response_deserializer=datatransfer.ListTransferLogsResponse.deserialize,
            )
        return self._stubs["list_transfer_logs"]

    @property
    def check_valid_creds(
        self,
    ) -> Callable[
        [datatransfer.CheckValidCredsRequest], datatransfer.CheckValidCredsResponse
    ]:
        r"""Return a callable for the check valid creds method over gRPC.

        Returns true if valid credentials exist for the given
        data source and requesting user.

        Returns:
            Callable[[~.CheckValidCredsRequest],
                    ~.CheckValidCredsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "check_valid_creds" not in self._stubs:
            self._stubs["check_valid_creds"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.datatransfer.v1.DataTransferService/CheckValidCreds",
                request_serializer=datatransfer.CheckValidCredsRequest.serialize,
                response_deserializer=datatransfer.CheckValidCredsResponse.deserialize,
            )
        return self._stubs["check_valid_creds"]

    @property
    def enroll_data_sources(
        self,
    ) -> Callable[[datatransfer.EnrollDataSourcesRequest], empty_pb2.Empty]:
        r"""Return a callable for the enroll data sources method over gRPC.

        Enroll data sources in a user project. This allows users to
        create transfer configurations for these data sources. They will
        also appear in the ListDataSources RPC and as such, will appear
        in the `BigQuery
        UI <https://console.cloud.google.com/bigquery>`__, and the
        documents can be found in the public guide for `BigQuery Web
        UI <https://cloud.google.com/bigquery/bigquery-web-ui>`__ and
        `Data Transfer
        Service <https://cloud.google.com/bigquery/docs/working-with-transfers>`__.

        Returns:
            Callable[[~.EnrollDataSourcesRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "enroll_data_sources" not in self._stubs:
            self._stubs["enroll_data_sources"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.datatransfer.v1.DataTransferService/EnrollDataSources",
                request_serializer=datatransfer.EnrollDataSourcesRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["enroll_data_sources"]

    @property
    def unenroll_data_sources(
        self,
    ) -> Callable[[datatransfer.UnenrollDataSourcesRequest], empty_pb2.Empty]:
        r"""Return a callable for the unenroll data sources method over gRPC.

        Unenroll data sources in a user project. This allows users to
        remove transfer configurations for these data sources. They will
        no longer appear in the ListDataSources RPC and will also no
        longer appear in the `BigQuery
        UI <https://console.cloud.google.com/bigquery>`__. Data
        transfers configurations of unenrolled data sources will not be
        scheduled.

        Returns:
            Callable[[~.UnenrollDataSourcesRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "unenroll_data_sources" not in self._stubs:
            self._stubs["unenroll_data_sources"] = self._logged_channel.unary_unary(
                "/google.cloud.bigquery.datatransfer.v1.DataTransferService/UnenrollDataSources",
                request_serializer=datatransfer.UnenrollDataSourcesRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["unenroll_data_sources"]

    def close(self):
        self._logged_channel.close()

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


__all__ = ("DataTransferServiceGrpcTransport",)
