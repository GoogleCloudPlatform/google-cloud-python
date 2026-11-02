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
import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore
import google.iam.v1.policy_pb2 as policy_pb2  # type: ignore
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
import google.protobuf.message
import grpc  # type: ignore
import proto  # type: ignore
from google.api_core import gapic_v1, grpc_helpers, operations_v1
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf.json_format import MessageToJson

from google.cloud.securitycenter_v2.types import (
    bigquery_export,
    finding,
    mute_config,
    notification_config,
    resource_value_config,
    securitycenter_service,
    simulation,
    source,
    valued_resource,
)
from google.cloud.securitycenter_v2.types import external_system as gcs_external_system
from google.cloud.securitycenter_v2.types import finding as gcs_finding
from google.cloud.securitycenter_v2.types import mute_config as gcs_mute_config
from google.cloud.securitycenter_v2.types import (
    notification_config as gcs_notification_config,
)
from google.cloud.securitycenter_v2.types import (
    resource_value_config as gcs_resource_value_config,
)
from google.cloud.securitycenter_v2.types import security_marks as gcs_security_marks
from google.cloud.securitycenter_v2.types import source as gcs_source

from .base import DEFAULT_CLIENT_INFO, SecurityCenterTransport

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
                    "serviceName": "google.cloud.securitycenter.v2.SecurityCenter",
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
                    "serviceName": "google.cloud.securitycenter.v2.SecurityCenter",
                    "rpcName": client_call_details.method,
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class SecurityCenterGrpcTransport(SecurityCenterTransport):
    """gRPC backend transport for SecurityCenter.

    V2 APIs for Security Center service.

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
        host: str = "securitycenter.googleapis.com",
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
                 The hostname to connect to (default: 'securitycenter.googleapis.com').
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
        host: str = "securitycenter.googleapis.com",
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
    def batch_create_resource_value_configs(
        self,
    ) -> Callable[
        [securitycenter_service.BatchCreateResourceValueConfigsRequest],
        securitycenter_service.BatchCreateResourceValueConfigsResponse,
    ]:
        r"""Return a callable for the batch create resource value
        configs method over gRPC.

        Creates a ResourceValueConfig for an organization.
        Maps user's tags to difference resource values for use
        by the attack path simulation.

        Returns:
            Callable[[~.BatchCreateResourceValueConfigsRequest],
                    ~.BatchCreateResourceValueConfigsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "batch_create_resource_value_configs" not in self._stubs:
            self._stubs["batch_create_resource_value_configs"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.securitycenter.v2.SecurityCenter/BatchCreateResourceValueConfigs",
                    request_serializer=securitycenter_service.BatchCreateResourceValueConfigsRequest.serialize,
                    response_deserializer=securitycenter_service.BatchCreateResourceValueConfigsResponse.deserialize,
                )
            )
        return self._stubs["batch_create_resource_value_configs"]

    @property
    def bulk_mute_findings(
        self,
    ) -> Callable[
        [securitycenter_service.BulkMuteFindingsRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the bulk mute findings method over gRPC.

        Kicks off an LRO to bulk mute findings for a parent
        based on a filter. If no location is specified, findings
        are muted in global. The parent can be either an
        organization, folder, or project. The findings matched
        by the filter will be muted after the LRO is done.

        Returns:
            Callable[[~.BulkMuteFindingsRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "bulk_mute_findings" not in self._stubs:
            self._stubs["bulk_mute_findings"] = self._logged_channel.unary_unary(
                "/google.cloud.securitycenter.v2.SecurityCenter/BulkMuteFindings",
                request_serializer=securitycenter_service.BulkMuteFindingsRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["bulk_mute_findings"]

    @property
    def create_big_query_export(
        self,
    ) -> Callable[
        [securitycenter_service.CreateBigQueryExportRequest],
        bigquery_export.BigQueryExport,
    ]:
        r"""Return a callable for the create big query export method over gRPC.

        Creates a BigQuery export.

        Returns:
            Callable[[~.CreateBigQueryExportRequest],
                    ~.BigQueryExport]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_big_query_export" not in self._stubs:
            self._stubs["create_big_query_export"] = self._logged_channel.unary_unary(
                "/google.cloud.securitycenter.v2.SecurityCenter/CreateBigQueryExport",
                request_serializer=securitycenter_service.CreateBigQueryExportRequest.serialize,
                response_deserializer=bigquery_export.BigQueryExport.deserialize,
            )
        return self._stubs["create_big_query_export"]

    @property
    def create_finding(
        self,
    ) -> Callable[[securitycenter_service.CreateFindingRequest], gcs_finding.Finding]:
        r"""Return a callable for the create finding method over gRPC.

        Creates a finding in a location. The corresponding
        source must exist for finding creation to succeed.

        Returns:
            Callable[[~.CreateFindingRequest],
                    ~.Finding]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_finding" not in self._stubs:
            self._stubs["create_finding"] = self._logged_channel.unary_unary(
                "/google.cloud.securitycenter.v2.SecurityCenter/CreateFinding",
                request_serializer=securitycenter_service.CreateFindingRequest.serialize,
                response_deserializer=gcs_finding.Finding.deserialize,
            )
        return self._stubs["create_finding"]

    @property
    def create_mute_config(
        self,
    ) -> Callable[
        [securitycenter_service.CreateMuteConfigRequest], gcs_mute_config.MuteConfig
    ]:
        r"""Return a callable for the create mute config method over gRPC.

        Creates a mute config.

        Returns:
            Callable[[~.CreateMuteConfigRequest],
                    ~.MuteConfig]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_mute_config" not in self._stubs:
            self._stubs["create_mute_config"] = self._logged_channel.unary_unary(
                "/google.cloud.securitycenter.v2.SecurityCenter/CreateMuteConfig",
                request_serializer=securitycenter_service.CreateMuteConfigRequest.serialize,
                response_deserializer=gcs_mute_config.MuteConfig.deserialize,
            )
        return self._stubs["create_mute_config"]

    @property
    def create_notification_config(
        self,
    ) -> Callable[
        [securitycenter_service.CreateNotificationConfigRequest],
        gcs_notification_config.NotificationConfig,
    ]:
        r"""Return a callable for the create notification config method over gRPC.

        Creates a notification config.

        Returns:
            Callable[[~.CreateNotificationConfigRequest],
                    ~.NotificationConfig]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_notification_config" not in self._stubs:
            self._stubs["create_notification_config"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.securitycenter.v2.SecurityCenter/CreateNotificationConfig",
                    request_serializer=securitycenter_service.CreateNotificationConfigRequest.serialize,
                    response_deserializer=gcs_notification_config.NotificationConfig.deserialize,
                )
            )
        return self._stubs["create_notification_config"]

    @property
    def create_source(
        self,
    ) -> Callable[[securitycenter_service.CreateSourceRequest], gcs_source.Source]:
        r"""Return a callable for the create source method over gRPC.

        Creates a source.

        Returns:
            Callable[[~.CreateSourceRequest],
                    ~.Source]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_source" not in self._stubs:
            self._stubs["create_source"] = self._logged_channel.unary_unary(
                "/google.cloud.securitycenter.v2.SecurityCenter/CreateSource",
                request_serializer=securitycenter_service.CreateSourceRequest.serialize,
                response_deserializer=gcs_source.Source.deserialize,
            )
        return self._stubs["create_source"]

    @property
    def delete_big_query_export(
        self,
    ) -> Callable[
        [securitycenter_service.DeleteBigQueryExportRequest], empty_pb2.Empty
    ]:
        r"""Return a callable for the delete big query export method over gRPC.

        Deletes an existing BigQuery export.

        Returns:
            Callable[[~.DeleteBigQueryExportRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_big_query_export" not in self._stubs:
            self._stubs["delete_big_query_export"] = self._logged_channel.unary_unary(
                "/google.cloud.securitycenter.v2.SecurityCenter/DeleteBigQueryExport",
                request_serializer=securitycenter_service.DeleteBigQueryExportRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_big_query_export"]

    @property
    def delete_mute_config(
        self,
    ) -> Callable[[securitycenter_service.DeleteMuteConfigRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete mute config method over gRPC.

        Deletes an existing mute config. If no location is
        specified, default is global.

        Returns:
            Callable[[~.DeleteMuteConfigRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_mute_config" not in self._stubs:
            self._stubs["delete_mute_config"] = self._logged_channel.unary_unary(
                "/google.cloud.securitycenter.v2.SecurityCenter/DeleteMuteConfig",
                request_serializer=securitycenter_service.DeleteMuteConfigRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_mute_config"]

    @property
    def delete_notification_config(
        self,
    ) -> Callable[
        [securitycenter_service.DeleteNotificationConfigRequest], empty_pb2.Empty
    ]:
        r"""Return a callable for the delete notification config method over gRPC.

        Deletes a notification config.

        Returns:
            Callable[[~.DeleteNotificationConfigRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_notification_config" not in self._stubs:
            self._stubs["delete_notification_config"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.securitycenter.v2.SecurityCenter/DeleteNotificationConfig",
                    request_serializer=securitycenter_service.DeleteNotificationConfigRequest.serialize,
                    response_deserializer=empty_pb2.Empty.FromString,
                )
            )
        return self._stubs["delete_notification_config"]

    @property
    def delete_resource_value_config(
        self,
    ) -> Callable[
        [securitycenter_service.DeleteResourceValueConfigRequest], empty_pb2.Empty
    ]:
        r"""Return a callable for the delete resource value config method over gRPC.

        Deletes a ResourceValueConfig.

        Returns:
            Callable[[~.DeleteResourceValueConfigRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_resource_value_config" not in self._stubs:
            self._stubs["delete_resource_value_config"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.securitycenter.v2.SecurityCenter/DeleteResourceValueConfig",
                    request_serializer=securitycenter_service.DeleteResourceValueConfigRequest.serialize,
                    response_deserializer=empty_pb2.Empty.FromString,
                )
            )
        return self._stubs["delete_resource_value_config"]

    @property
    def get_big_query_export(
        self,
    ) -> Callable[
        [securitycenter_service.GetBigQueryExportRequest],
        bigquery_export.BigQueryExport,
    ]:
        r"""Return a callable for the get big query export method over gRPC.

        Gets a BigQuery export.

        Returns:
            Callable[[~.GetBigQueryExportRequest],
                    ~.BigQueryExport]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_big_query_export" not in self._stubs:
            self._stubs["get_big_query_export"] = self._logged_channel.unary_unary(
                "/google.cloud.securitycenter.v2.SecurityCenter/GetBigQueryExport",
                request_serializer=securitycenter_service.GetBigQueryExportRequest.serialize,
                response_deserializer=bigquery_export.BigQueryExport.deserialize,
            )
        return self._stubs["get_big_query_export"]

    @property
    def get_simulation(
        self,
    ) -> Callable[[securitycenter_service.GetSimulationRequest], simulation.Simulation]:
        r"""Return a callable for the get simulation method over gRPC.

        Get the simulation by name or the latest simulation
        for the given organization.

        Returns:
            Callable[[~.GetSimulationRequest],
                    ~.Simulation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_simulation" not in self._stubs:
            self._stubs["get_simulation"] = self._logged_channel.unary_unary(
                "/google.cloud.securitycenter.v2.SecurityCenter/GetSimulation",
                request_serializer=securitycenter_service.GetSimulationRequest.serialize,
                response_deserializer=simulation.Simulation.deserialize,
            )
        return self._stubs["get_simulation"]

    @property
    def get_valued_resource(
        self,
    ) -> Callable[
        [securitycenter_service.GetValuedResourceRequest],
        valued_resource.ValuedResource,
    ]:
        r"""Return a callable for the get valued resource method over gRPC.

        Get the valued resource by name

        Returns:
            Callable[[~.GetValuedResourceRequest],
                    ~.ValuedResource]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_valued_resource" not in self._stubs:
            self._stubs["get_valued_resource"] = self._logged_channel.unary_unary(
                "/google.cloud.securitycenter.v2.SecurityCenter/GetValuedResource",
                request_serializer=securitycenter_service.GetValuedResourceRequest.serialize,
                response_deserializer=valued_resource.ValuedResource.deserialize,
            )
        return self._stubs["get_valued_resource"]

    @property
    def get_iam_policy(
        self,
    ) -> Callable[[iam_policy_pb2.GetIamPolicyRequest], policy_pb2.Policy]:
        r"""Return a callable for the get iam policy method over gRPC.

        Gets the access control policy on the specified
        Source.

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
                "/google.cloud.securitycenter.v2.SecurityCenter/GetIamPolicy",
                request_serializer=iam_policy_pb2.GetIamPolicyRequest.SerializeToString,
                response_deserializer=policy_pb2.Policy.FromString,
            )
        return self._stubs["get_iam_policy"]

    @property
    def get_mute_config(
        self,
    ) -> Callable[
        [securitycenter_service.GetMuteConfigRequest], mute_config.MuteConfig
    ]:
        r"""Return a callable for the get mute config method over gRPC.

        Gets a mute config. If no location is specified,
        default is global.

        Returns:
            Callable[[~.GetMuteConfigRequest],
                    ~.MuteConfig]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_mute_config" not in self._stubs:
            self._stubs["get_mute_config"] = self._logged_channel.unary_unary(
                "/google.cloud.securitycenter.v2.SecurityCenter/GetMuteConfig",
                request_serializer=securitycenter_service.GetMuteConfigRequest.serialize,
                response_deserializer=mute_config.MuteConfig.deserialize,
            )
        return self._stubs["get_mute_config"]

    @property
    def get_notification_config(
        self,
    ) -> Callable[
        [securitycenter_service.GetNotificationConfigRequest],
        notification_config.NotificationConfig,
    ]:
        r"""Return a callable for the get notification config method over gRPC.

        Gets a notification config.

        Returns:
            Callable[[~.GetNotificationConfigRequest],
                    ~.NotificationConfig]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_notification_config" not in self._stubs:
            self._stubs["get_notification_config"] = self._logged_channel.unary_unary(
                "/google.cloud.securitycenter.v2.SecurityCenter/GetNotificationConfig",
                request_serializer=securitycenter_service.GetNotificationConfigRequest.serialize,
                response_deserializer=notification_config.NotificationConfig.deserialize,
            )
        return self._stubs["get_notification_config"]

    @property
    def get_resource_value_config(
        self,
    ) -> Callable[
        [securitycenter_service.GetResourceValueConfigRequest],
        resource_value_config.ResourceValueConfig,
    ]:
        r"""Return a callable for the get resource value config method over gRPC.

        Gets a ResourceValueConfig.

        Returns:
            Callable[[~.GetResourceValueConfigRequest],
                    ~.ResourceValueConfig]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_resource_value_config" not in self._stubs:
            self._stubs["get_resource_value_config"] = self._logged_channel.unary_unary(
                "/google.cloud.securitycenter.v2.SecurityCenter/GetResourceValueConfig",
                request_serializer=securitycenter_service.GetResourceValueConfigRequest.serialize,
                response_deserializer=resource_value_config.ResourceValueConfig.deserialize,
            )
        return self._stubs["get_resource_value_config"]

    @property
    def get_source(
        self,
    ) -> Callable[[securitycenter_service.GetSourceRequest], source.Source]:
        r"""Return a callable for the get source method over gRPC.

        Gets a source.

        Returns:
            Callable[[~.GetSourceRequest],
                    ~.Source]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_source" not in self._stubs:
            self._stubs["get_source"] = self._logged_channel.unary_unary(
                "/google.cloud.securitycenter.v2.SecurityCenter/GetSource",
                request_serializer=securitycenter_service.GetSourceRequest.serialize,
                response_deserializer=source.Source.deserialize,
            )
        return self._stubs["get_source"]

    @property
    def group_findings(
        self,
    ) -> Callable[
        [securitycenter_service.GroupFindingsRequest],
        securitycenter_service.GroupFindingsResponse,
    ]:
        r"""Return a callable for the group findings method over gRPC.

        Filters an organization or source's findings and groups them by
        their specified properties in a location. If no location is
        specified, findings are assumed to be in global

        To group across all sources provide a ``-`` as the source id.
        The following list shows some examples:

        - ``/v2/organizations/{organization_id}/sources/-/findings``
        -

        ``/v2/organizations/{organization_id}/sources/-/locations/{location_id}/findings``

        - ``/v2/folders/{folder_id}/sources/-/findings``
        - ``/v2/folders/{folder_id}/sources/-/locations/{location_id}/findings``
        - ``/v2/projects/{project_id}/sources/-/findings``
        - ``/v2/projects/{project_id}/sources/-/locations/{location_id}/findings``

        Returns:
            Callable[[~.GroupFindingsRequest],
                    ~.GroupFindingsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "group_findings" not in self._stubs:
            self._stubs["group_findings"] = self._logged_channel.unary_unary(
                "/google.cloud.securitycenter.v2.SecurityCenter/GroupFindings",
                request_serializer=securitycenter_service.GroupFindingsRequest.serialize,
                response_deserializer=securitycenter_service.GroupFindingsResponse.deserialize,
            )
        return self._stubs["group_findings"]

    @property
    def list_attack_paths(
        self,
    ) -> Callable[
        [securitycenter_service.ListAttackPathsRequest],
        securitycenter_service.ListAttackPathsResponse,
    ]:
        r"""Return a callable for the list attack paths method over gRPC.

        Lists the attack paths for a set of simulation
        results or valued resources and filter.

        Returns:
            Callable[[~.ListAttackPathsRequest],
                    ~.ListAttackPathsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_attack_paths" not in self._stubs:
            self._stubs["list_attack_paths"] = self._logged_channel.unary_unary(
                "/google.cloud.securitycenter.v2.SecurityCenter/ListAttackPaths",
                request_serializer=securitycenter_service.ListAttackPathsRequest.serialize,
                response_deserializer=securitycenter_service.ListAttackPathsResponse.deserialize,
            )
        return self._stubs["list_attack_paths"]

    @property
    def list_big_query_exports(
        self,
    ) -> Callable[
        [securitycenter_service.ListBigQueryExportsRequest],
        securitycenter_service.ListBigQueryExportsResponse,
    ]:
        r"""Return a callable for the list big query exports method over gRPC.

        Lists BigQuery exports. Note that when requesting
        BigQuery exports at a given level all exports under that
        level are also returned e.g. if requesting BigQuery
        exports under a folder, then all BigQuery exports
        immediately under the folder plus the ones created under
        the projects within the folder are returned.

        Returns:
            Callable[[~.ListBigQueryExportsRequest],
                    ~.ListBigQueryExportsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_big_query_exports" not in self._stubs:
            self._stubs["list_big_query_exports"] = self._logged_channel.unary_unary(
                "/google.cloud.securitycenter.v2.SecurityCenter/ListBigQueryExports",
                request_serializer=securitycenter_service.ListBigQueryExportsRequest.serialize,
                response_deserializer=securitycenter_service.ListBigQueryExportsResponse.deserialize,
            )
        return self._stubs["list_big_query_exports"]

    @property
    def list_findings(
        self,
    ) -> Callable[
        [securitycenter_service.ListFindingsRequest],
        securitycenter_service.ListFindingsResponse,
    ]:
        r"""Return a callable for the list findings method over gRPC.

        Lists an organization or source's findings.

        To list across all sources for a given location provide a ``-``
        as the source id. If no location is specified, finding are
        assumed to be in global. The following list shows some examples:

        - ``/v2/organizations/{organization_id}/sources/-/findings``
        -

        ``/v2/organizations/{organization_id}/sources/-/locations/{location_id}/findings``

        Returns:
            Callable[[~.ListFindingsRequest],
                    ~.ListFindingsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_findings" not in self._stubs:
            self._stubs["list_findings"] = self._logged_channel.unary_unary(
                "/google.cloud.securitycenter.v2.SecurityCenter/ListFindings",
                request_serializer=securitycenter_service.ListFindingsRequest.serialize,
                response_deserializer=securitycenter_service.ListFindingsResponse.deserialize,
            )
        return self._stubs["list_findings"]

    @property
    def list_mute_configs(
        self,
    ) -> Callable[
        [securitycenter_service.ListMuteConfigsRequest],
        securitycenter_service.ListMuteConfigsResponse,
    ]:
        r"""Return a callable for the list mute configs method over gRPC.

        Lists mute configs. If no location is specified,
        default is global.

        Returns:
            Callable[[~.ListMuteConfigsRequest],
                    ~.ListMuteConfigsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_mute_configs" not in self._stubs:
            self._stubs["list_mute_configs"] = self._logged_channel.unary_unary(
                "/google.cloud.securitycenter.v2.SecurityCenter/ListMuteConfigs",
                request_serializer=securitycenter_service.ListMuteConfigsRequest.serialize,
                response_deserializer=securitycenter_service.ListMuteConfigsResponse.deserialize,
            )
        return self._stubs["list_mute_configs"]

    @property
    def list_notification_configs(
        self,
    ) -> Callable[
        [securitycenter_service.ListNotificationConfigsRequest],
        securitycenter_service.ListNotificationConfigsResponse,
    ]:
        r"""Return a callable for the list notification configs method over gRPC.

        Lists notification configs.

        Returns:
            Callable[[~.ListNotificationConfigsRequest],
                    ~.ListNotificationConfigsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_notification_configs" not in self._stubs:
            self._stubs["list_notification_configs"] = self._logged_channel.unary_unary(
                "/google.cloud.securitycenter.v2.SecurityCenter/ListNotificationConfigs",
                request_serializer=securitycenter_service.ListNotificationConfigsRequest.serialize,
                response_deserializer=securitycenter_service.ListNotificationConfigsResponse.deserialize,
            )
        return self._stubs["list_notification_configs"]

    @property
    def list_resource_value_configs(
        self,
    ) -> Callable[
        [securitycenter_service.ListResourceValueConfigsRequest],
        securitycenter_service.ListResourceValueConfigsResponse,
    ]:
        r"""Return a callable for the list resource value configs method over gRPC.

        Lists all ResourceValueConfigs.

        Returns:
            Callable[[~.ListResourceValueConfigsRequest],
                    ~.ListResourceValueConfigsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_resource_value_configs" not in self._stubs:
            self._stubs["list_resource_value_configs"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.securitycenter.v2.SecurityCenter/ListResourceValueConfigs",
                    request_serializer=securitycenter_service.ListResourceValueConfigsRequest.serialize,
                    response_deserializer=securitycenter_service.ListResourceValueConfigsResponse.deserialize,
                )
            )
        return self._stubs["list_resource_value_configs"]

    @property
    def list_sources(
        self,
    ) -> Callable[
        [securitycenter_service.ListSourcesRequest],
        securitycenter_service.ListSourcesResponse,
    ]:
        r"""Return a callable for the list sources method over gRPC.

        Lists all sources belonging to an organization.

        Returns:
            Callable[[~.ListSourcesRequest],
                    ~.ListSourcesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_sources" not in self._stubs:
            self._stubs["list_sources"] = self._logged_channel.unary_unary(
                "/google.cloud.securitycenter.v2.SecurityCenter/ListSources",
                request_serializer=securitycenter_service.ListSourcesRequest.serialize,
                response_deserializer=securitycenter_service.ListSourcesResponse.deserialize,
            )
        return self._stubs["list_sources"]

    @property
    def list_valued_resources(
        self,
    ) -> Callable[
        [securitycenter_service.ListValuedResourcesRequest],
        securitycenter_service.ListValuedResourcesResponse,
    ]:
        r"""Return a callable for the list valued resources method over gRPC.

        Lists the valued resources for a set of simulation
        results and filter.

        Returns:
            Callable[[~.ListValuedResourcesRequest],
                    ~.ListValuedResourcesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_valued_resources" not in self._stubs:
            self._stubs["list_valued_resources"] = self._logged_channel.unary_unary(
                "/google.cloud.securitycenter.v2.SecurityCenter/ListValuedResources",
                request_serializer=securitycenter_service.ListValuedResourcesRequest.serialize,
                response_deserializer=securitycenter_service.ListValuedResourcesResponse.deserialize,
            )
        return self._stubs["list_valued_resources"]

    @property
    def set_finding_state(
        self,
    ) -> Callable[[securitycenter_service.SetFindingStateRequest], finding.Finding]:
        r"""Return a callable for the set finding state method over gRPC.

        Updates the state of a finding. If no location is
        specified, finding is assumed to be in global

        Returns:
            Callable[[~.SetFindingStateRequest],
                    ~.Finding]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "set_finding_state" not in self._stubs:
            self._stubs["set_finding_state"] = self._logged_channel.unary_unary(
                "/google.cloud.securitycenter.v2.SecurityCenter/SetFindingState",
                request_serializer=securitycenter_service.SetFindingStateRequest.serialize,
                response_deserializer=finding.Finding.deserialize,
            )
        return self._stubs["set_finding_state"]

    @property
    def set_iam_policy(
        self,
    ) -> Callable[[iam_policy_pb2.SetIamPolicyRequest], policy_pb2.Policy]:
        r"""Return a callable for the set iam policy method over gRPC.

        Sets the access control policy on the specified
        Source.

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
                "/google.cloud.securitycenter.v2.SecurityCenter/SetIamPolicy",
                request_serializer=iam_policy_pb2.SetIamPolicyRequest.SerializeToString,
                response_deserializer=policy_pb2.Policy.FromString,
            )
        return self._stubs["set_iam_policy"]

    @property
    def set_mute(
        self,
    ) -> Callable[[securitycenter_service.SetMuteRequest], finding.Finding]:
        r"""Return a callable for the set mute method over gRPC.

        Updates the mute state of a finding. If no location
        is specified, finding is assumed to be in global

        Returns:
            Callable[[~.SetMuteRequest],
                    ~.Finding]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "set_mute" not in self._stubs:
            self._stubs["set_mute"] = self._logged_channel.unary_unary(
                "/google.cloud.securitycenter.v2.SecurityCenter/SetMute",
                request_serializer=securitycenter_service.SetMuteRequest.serialize,
                response_deserializer=finding.Finding.deserialize,
            )
        return self._stubs["set_mute"]

    @property
    def test_iam_permissions(
        self,
    ) -> Callable[
        [iam_policy_pb2.TestIamPermissionsRequest],
        iam_policy_pb2.TestIamPermissionsResponse,
    ]:
        r"""Return a callable for the test iam permissions method over gRPC.

        Returns the permissions that a caller has on the
        specified source.

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
                "/google.cloud.securitycenter.v2.SecurityCenter/TestIamPermissions",
                request_serializer=iam_policy_pb2.TestIamPermissionsRequest.SerializeToString,
                response_deserializer=iam_policy_pb2.TestIamPermissionsResponse.FromString,
            )
        return self._stubs["test_iam_permissions"]

    @property
    def update_big_query_export(
        self,
    ) -> Callable[
        [securitycenter_service.UpdateBigQueryExportRequest],
        bigquery_export.BigQueryExport,
    ]:
        r"""Return a callable for the update big query export method over gRPC.

        Updates a BigQuery export.

        Returns:
            Callable[[~.UpdateBigQueryExportRequest],
                    ~.BigQueryExport]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_big_query_export" not in self._stubs:
            self._stubs["update_big_query_export"] = self._logged_channel.unary_unary(
                "/google.cloud.securitycenter.v2.SecurityCenter/UpdateBigQueryExport",
                request_serializer=securitycenter_service.UpdateBigQueryExportRequest.serialize,
                response_deserializer=bigquery_export.BigQueryExport.deserialize,
            )
        return self._stubs["update_big_query_export"]

    @property
    def update_external_system(
        self,
    ) -> Callable[
        [securitycenter_service.UpdateExternalSystemRequest],
        gcs_external_system.ExternalSystem,
    ]:
        r"""Return a callable for the update external system method over gRPC.

        Updates external system. This is for a given finding.
        If no location is specified, finding is assumed to be in
        global

        Returns:
            Callable[[~.UpdateExternalSystemRequest],
                    ~.ExternalSystem]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_external_system" not in self._stubs:
            self._stubs["update_external_system"] = self._logged_channel.unary_unary(
                "/google.cloud.securitycenter.v2.SecurityCenter/UpdateExternalSystem",
                request_serializer=securitycenter_service.UpdateExternalSystemRequest.serialize,
                response_deserializer=gcs_external_system.ExternalSystem.deserialize,
            )
        return self._stubs["update_external_system"]

    @property
    def update_finding(
        self,
    ) -> Callable[[securitycenter_service.UpdateFindingRequest], gcs_finding.Finding]:
        r"""Return a callable for the update finding method over gRPC.

        Creates or updates a finding. If no location is
        specified, finding is assumed to be in global. The
        corresponding source must exist for a finding creation
        to succeed.

        Returns:
            Callable[[~.UpdateFindingRequest],
                    ~.Finding]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_finding" not in self._stubs:
            self._stubs["update_finding"] = self._logged_channel.unary_unary(
                "/google.cloud.securitycenter.v2.SecurityCenter/UpdateFinding",
                request_serializer=securitycenter_service.UpdateFindingRequest.serialize,
                response_deserializer=gcs_finding.Finding.deserialize,
            )
        return self._stubs["update_finding"]

    @property
    def update_mute_config(
        self,
    ) -> Callable[
        [securitycenter_service.UpdateMuteConfigRequest], gcs_mute_config.MuteConfig
    ]:
        r"""Return a callable for the update mute config method over gRPC.

        Updates a mute config. If no location is specified,
        default is global.

        Returns:
            Callable[[~.UpdateMuteConfigRequest],
                    ~.MuteConfig]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_mute_config" not in self._stubs:
            self._stubs["update_mute_config"] = self._logged_channel.unary_unary(
                "/google.cloud.securitycenter.v2.SecurityCenter/UpdateMuteConfig",
                request_serializer=securitycenter_service.UpdateMuteConfigRequest.serialize,
                response_deserializer=gcs_mute_config.MuteConfig.deserialize,
            )
        return self._stubs["update_mute_config"]

    @property
    def update_notification_config(
        self,
    ) -> Callable[
        [securitycenter_service.UpdateNotificationConfigRequest],
        gcs_notification_config.NotificationConfig,
    ]:
        r"""Return a callable for the update notification config method over gRPC.

        Updates a notification config. The following update fields are
        allowed: description, pubsub_topic, streaming_config.filter

        Returns:
            Callable[[~.UpdateNotificationConfigRequest],
                    ~.NotificationConfig]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_notification_config" not in self._stubs:
            self._stubs["update_notification_config"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.securitycenter.v2.SecurityCenter/UpdateNotificationConfig",
                    request_serializer=securitycenter_service.UpdateNotificationConfigRequest.serialize,
                    response_deserializer=gcs_notification_config.NotificationConfig.deserialize,
                )
            )
        return self._stubs["update_notification_config"]

    @property
    def update_resource_value_config(
        self,
    ) -> Callable[
        [securitycenter_service.UpdateResourceValueConfigRequest],
        gcs_resource_value_config.ResourceValueConfig,
    ]:
        r"""Return a callable for the update resource value config method over gRPC.

        Updates an existing ResourceValueConfigs with new
        rules.

        Returns:
            Callable[[~.UpdateResourceValueConfigRequest],
                    ~.ResourceValueConfig]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_resource_value_config" not in self._stubs:
            self._stubs["update_resource_value_config"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.securitycenter.v2.SecurityCenter/UpdateResourceValueConfig",
                    request_serializer=securitycenter_service.UpdateResourceValueConfigRequest.serialize,
                    response_deserializer=gcs_resource_value_config.ResourceValueConfig.deserialize,
                )
            )
        return self._stubs["update_resource_value_config"]

    @property
    def update_security_marks(
        self,
    ) -> Callable[
        [securitycenter_service.UpdateSecurityMarksRequest],
        gcs_security_marks.SecurityMarks,
    ]:
        r"""Return a callable for the update security marks method over gRPC.

        Updates security marks. For Finding Security marks,
        if no location is specified, finding is assumed to be in
        global. Assets Security Marks can only be accessed
        through global endpoint.

        Returns:
            Callable[[~.UpdateSecurityMarksRequest],
                    ~.SecurityMarks]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_security_marks" not in self._stubs:
            self._stubs["update_security_marks"] = self._logged_channel.unary_unary(
                "/google.cloud.securitycenter.v2.SecurityCenter/UpdateSecurityMarks",
                request_serializer=securitycenter_service.UpdateSecurityMarksRequest.serialize,
                response_deserializer=gcs_security_marks.SecurityMarks.deserialize,
            )
        return self._stubs["update_security_marks"]

    @property
    def update_source(
        self,
    ) -> Callable[[securitycenter_service.UpdateSourceRequest], gcs_source.Source]:
        r"""Return a callable for the update source method over gRPC.

        Updates a source.

        Returns:
            Callable[[~.UpdateSourceRequest],
                    ~.Source]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_source" not in self._stubs:
            self._stubs["update_source"] = self._logged_channel.unary_unary(
                "/google.cloud.securitycenter.v2.SecurityCenter/UpdateSource",
                request_serializer=securitycenter_service.UpdateSourceRequest.serialize,
                response_deserializer=gcs_source.Source.deserialize,
            )
        return self._stubs["update_source"]

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
    def kind(self) -> str:
        return "grpc"


__all__ = ("SecurityCenterGrpcTransport",)
