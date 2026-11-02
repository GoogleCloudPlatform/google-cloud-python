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

from google.cloud.ces_v1beta.types import (
    agent,
    agent_service,
    app,
    app_version,
    changelog,
    conversation,
    deployment,
    example,
    guardrail,
    security_settings,
    tool,
    toolset,
)
from google.cloud.ces_v1beta.types import agent as gcc_agent
from google.cloud.ces_v1beta.types import app as gcc_app
from google.cloud.ces_v1beta.types import app_version as gcc_app_version
from google.cloud.ces_v1beta.types import deployment as gcc_deployment
from google.cloud.ces_v1beta.types import example as gcc_example
from google.cloud.ces_v1beta.types import guardrail as gcc_guardrail
from google.cloud.ces_v1beta.types import security_settings as gcc_security_settings
from google.cloud.ces_v1beta.types import tool as gcc_tool
from google.cloud.ces_v1beta.types import toolset as gcc_toolset

from .base import DEFAULT_CLIENT_INFO, AgentServiceTransport

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
                    "serviceName": "google.cloud.ces.v1beta.AgentService",
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
                    "serviceName": "google.cloud.ces.v1beta.AgentService",
                    "rpcName": client_call_details.method,
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class AgentServiceGrpcTransport(AgentServiceTransport):
    """gRPC backend transport for AgentService.

    The service that manages agent-related resources in Gemini
    Enterprise for Customer Engagement (CES).

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
        host: str = "ces.googleapis.com",
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
                 The hostname to connect to (default: 'ces.googleapis.com').
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
        host: str = "ces.googleapis.com",
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
    def list_apps(
        self,
    ) -> Callable[[agent_service.ListAppsRequest], agent_service.ListAppsResponse]:
        r"""Return a callable for the list apps method over gRPC.

        Lists apps in the given project and location.

        Returns:
            Callable[[~.ListAppsRequest],
                    ~.ListAppsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_apps" not in self._stubs:
            self._stubs["list_apps"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/ListApps",
                request_serializer=agent_service.ListAppsRequest.serialize,
                response_deserializer=agent_service.ListAppsResponse.deserialize,
            )
        return self._stubs["list_apps"]

    @property
    def get_app(self) -> Callable[[agent_service.GetAppRequest], app.App]:
        r"""Return a callable for the get app method over gRPC.

        Gets details of the specified app.

        Returns:
            Callable[[~.GetAppRequest],
                    ~.App]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_app" not in self._stubs:
            self._stubs["get_app"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/GetApp",
                request_serializer=agent_service.GetAppRequest.serialize,
                response_deserializer=app.App.deserialize,
            )
        return self._stubs["get_app"]

    @property
    def create_app(
        self,
    ) -> Callable[[agent_service.CreateAppRequest], operations_pb2.Operation]:
        r"""Return a callable for the create app method over gRPC.

        Creates a new app in the given project and location.

        Returns:
            Callable[[~.CreateAppRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_app" not in self._stubs:
            self._stubs["create_app"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/CreateApp",
                request_serializer=agent_service.CreateAppRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_app"]

    @property
    def update_app(self) -> Callable[[agent_service.UpdateAppRequest], gcc_app.App]:
        r"""Return a callable for the update app method over gRPC.

        Updates the specified app.

        Returns:
            Callable[[~.UpdateAppRequest],
                    ~.App]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_app" not in self._stubs:
            self._stubs["update_app"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/UpdateApp",
                request_serializer=agent_service.UpdateAppRequest.serialize,
                response_deserializer=gcc_app.App.deserialize,
            )
        return self._stubs["update_app"]

    @property
    def delete_app(
        self,
    ) -> Callable[[agent_service.DeleteAppRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete app method over gRPC.

        Deletes the specified app.

        Returns:
            Callable[[~.DeleteAppRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_app" not in self._stubs:
            self._stubs["delete_app"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/DeleteApp",
                request_serializer=agent_service.DeleteAppRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_app"]

    @property
    def export_app(
        self,
    ) -> Callable[[agent_service.ExportAppRequest], operations_pb2.Operation]:
        r"""Return a callable for the export app method over gRPC.

        Exports the specified app.

        Returns:
            Callable[[~.ExportAppRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "export_app" not in self._stubs:
            self._stubs["export_app"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/ExportApp",
                request_serializer=agent_service.ExportAppRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["export_app"]

    @property
    def import_app(
        self,
    ) -> Callable[[agent_service.ImportAppRequest], operations_pb2.Operation]:
        r"""Return a callable for the import app method over gRPC.

        Imports the specified app.

        Returns:
            Callable[[~.ImportAppRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "import_app" not in self._stubs:
            self._stubs["import_app"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/ImportApp",
                request_serializer=agent_service.ImportAppRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["import_app"]

    @property
    def get_security_settings(
        self,
    ) -> Callable[
        [agent_service.GetSecuritySettingsRequest], security_settings.SecuritySettings
    ]:
        r"""Return a callable for the get security settings method over gRPC.

        Retrieves the security settings for the project and
        location.

        Returns:
            Callable[[~.GetSecuritySettingsRequest],
                    ~.SecuritySettings]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_security_settings" not in self._stubs:
            self._stubs["get_security_settings"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/GetSecuritySettings",
                request_serializer=agent_service.GetSecuritySettingsRequest.serialize,
                response_deserializer=security_settings.SecuritySettings.deserialize,
            )
        return self._stubs["get_security_settings"]

    @property
    def update_security_settings(
        self,
    ) -> Callable[
        [agent_service.UpdateSecuritySettingsRequest],
        gcc_security_settings.SecuritySettings,
    ]:
        r"""Return a callable for the update security settings method over gRPC.

        Updates the security settings for the project and
        location.

        Returns:
            Callable[[~.UpdateSecuritySettingsRequest],
                    ~.SecuritySettings]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_security_settings" not in self._stubs:
            self._stubs["update_security_settings"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/UpdateSecuritySettings",
                request_serializer=agent_service.UpdateSecuritySettingsRequest.serialize,
                response_deserializer=gcc_security_settings.SecuritySettings.deserialize,
            )
        return self._stubs["update_security_settings"]

    @property
    def list_agents(
        self,
    ) -> Callable[[agent_service.ListAgentsRequest], agent_service.ListAgentsResponse]:
        r"""Return a callable for the list agents method over gRPC.

        Lists agents in the given app.

        Returns:
            Callable[[~.ListAgentsRequest],
                    ~.ListAgentsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_agents" not in self._stubs:
            self._stubs["list_agents"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/ListAgents",
                request_serializer=agent_service.ListAgentsRequest.serialize,
                response_deserializer=agent_service.ListAgentsResponse.deserialize,
            )
        return self._stubs["list_agents"]

    @property
    def get_agent(self) -> Callable[[agent_service.GetAgentRequest], agent.Agent]:
        r"""Return a callable for the get agent method over gRPC.

        Gets details of the specified agent.

        Returns:
            Callable[[~.GetAgentRequest],
                    ~.Agent]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_agent" not in self._stubs:
            self._stubs["get_agent"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/GetAgent",
                request_serializer=agent_service.GetAgentRequest.serialize,
                response_deserializer=agent.Agent.deserialize,
            )
        return self._stubs["get_agent"]

    @property
    def create_agent(
        self,
    ) -> Callable[[agent_service.CreateAgentRequest], gcc_agent.Agent]:
        r"""Return a callable for the create agent method over gRPC.

        Creates a new agent in the given app.

        Returns:
            Callable[[~.CreateAgentRequest],
                    ~.Agent]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_agent" not in self._stubs:
            self._stubs["create_agent"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/CreateAgent",
                request_serializer=agent_service.CreateAgentRequest.serialize,
                response_deserializer=gcc_agent.Agent.deserialize,
            )
        return self._stubs["create_agent"]

    @property
    def update_agent(
        self,
    ) -> Callable[[agent_service.UpdateAgentRequest], gcc_agent.Agent]:
        r"""Return a callable for the update agent method over gRPC.

        Updates the specified agent.

        Returns:
            Callable[[~.UpdateAgentRequest],
                    ~.Agent]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_agent" not in self._stubs:
            self._stubs["update_agent"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/UpdateAgent",
                request_serializer=agent_service.UpdateAgentRequest.serialize,
                response_deserializer=gcc_agent.Agent.deserialize,
            )
        return self._stubs["update_agent"]

    @property
    def delete_agent(
        self,
    ) -> Callable[[agent_service.DeleteAgentRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete agent method over gRPC.

        Deletes the specified agent.

        Returns:
            Callable[[~.DeleteAgentRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_agent" not in self._stubs:
            self._stubs["delete_agent"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/DeleteAgent",
                request_serializer=agent_service.DeleteAgentRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_agent"]

    @property
    def list_examples(
        self,
    ) -> Callable[
        [agent_service.ListExamplesRequest], agent_service.ListExamplesResponse
    ]:
        r"""Return a callable for the list examples method over gRPC.

        Lists examples in the given app.

        Returns:
            Callable[[~.ListExamplesRequest],
                    ~.ListExamplesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_examples" not in self._stubs:
            self._stubs["list_examples"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/ListExamples",
                request_serializer=agent_service.ListExamplesRequest.serialize,
                response_deserializer=agent_service.ListExamplesResponse.deserialize,
            )
        return self._stubs["list_examples"]

    @property
    def get_example(
        self,
    ) -> Callable[[agent_service.GetExampleRequest], example.Example]:
        r"""Return a callable for the get example method over gRPC.

        Gets details of the specified example.

        Returns:
            Callable[[~.GetExampleRequest],
                    ~.Example]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_example" not in self._stubs:
            self._stubs["get_example"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/GetExample",
                request_serializer=agent_service.GetExampleRequest.serialize,
                response_deserializer=example.Example.deserialize,
            )
        return self._stubs["get_example"]

    @property
    def create_example(
        self,
    ) -> Callable[[agent_service.CreateExampleRequest], gcc_example.Example]:
        r"""Return a callable for the create example method over gRPC.

        Creates a new example in the given app.

        Returns:
            Callable[[~.CreateExampleRequest],
                    ~.Example]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_example" not in self._stubs:
            self._stubs["create_example"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/CreateExample",
                request_serializer=agent_service.CreateExampleRequest.serialize,
                response_deserializer=gcc_example.Example.deserialize,
            )
        return self._stubs["create_example"]

    @property
    def update_example(
        self,
    ) -> Callable[[agent_service.UpdateExampleRequest], gcc_example.Example]:
        r"""Return a callable for the update example method over gRPC.

        Updates the specified example.

        Returns:
            Callable[[~.UpdateExampleRequest],
                    ~.Example]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_example" not in self._stubs:
            self._stubs["update_example"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/UpdateExample",
                request_serializer=agent_service.UpdateExampleRequest.serialize,
                response_deserializer=gcc_example.Example.deserialize,
            )
        return self._stubs["update_example"]

    @property
    def delete_example(
        self,
    ) -> Callable[[agent_service.DeleteExampleRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete example method over gRPC.

        Deletes the specified example.

        Returns:
            Callable[[~.DeleteExampleRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_example" not in self._stubs:
            self._stubs["delete_example"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/DeleteExample",
                request_serializer=agent_service.DeleteExampleRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_example"]

    @property
    def list_tools(
        self,
    ) -> Callable[[agent_service.ListToolsRequest], agent_service.ListToolsResponse]:
        r"""Return a callable for the list tools method over gRPC.

        Lists tools in the given app.

        Returns:
            Callable[[~.ListToolsRequest],
                    ~.ListToolsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_tools" not in self._stubs:
            self._stubs["list_tools"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/ListTools",
                request_serializer=agent_service.ListToolsRequest.serialize,
                response_deserializer=agent_service.ListToolsResponse.deserialize,
            )
        return self._stubs["list_tools"]

    @property
    def get_tool(self) -> Callable[[agent_service.GetToolRequest], tool.Tool]:
        r"""Return a callable for the get tool method over gRPC.

        Gets details of the specified tool.

        Returns:
            Callable[[~.GetToolRequest],
                    ~.Tool]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_tool" not in self._stubs:
            self._stubs["get_tool"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/GetTool",
                request_serializer=agent_service.GetToolRequest.serialize,
                response_deserializer=tool.Tool.deserialize,
            )
        return self._stubs["get_tool"]

    @property
    def list_conversations(
        self,
    ) -> Callable[
        [agent_service.ListConversationsRequest],
        agent_service.ListConversationsResponse,
    ]:
        r"""Return a callable for the list conversations method over gRPC.

        Lists conversations in the given app.

        Returns:
            Callable[[~.ListConversationsRequest],
                    ~.ListConversationsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_conversations" not in self._stubs:
            self._stubs["list_conversations"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/ListConversations",
                request_serializer=agent_service.ListConversationsRequest.serialize,
                response_deserializer=agent_service.ListConversationsResponse.deserialize,
            )
        return self._stubs["list_conversations"]

    @property
    def get_conversation(
        self,
    ) -> Callable[[agent_service.GetConversationRequest], conversation.Conversation]:
        r"""Return a callable for the get conversation method over gRPC.

        Gets details of the specified conversation.

        Returns:
            Callable[[~.GetConversationRequest],
                    ~.Conversation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_conversation" not in self._stubs:
            self._stubs["get_conversation"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/GetConversation",
                request_serializer=agent_service.GetConversationRequest.serialize,
                response_deserializer=conversation.Conversation.deserialize,
            )
        return self._stubs["get_conversation"]

    @property
    def delete_conversation(
        self,
    ) -> Callable[[agent_service.DeleteConversationRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete conversation method over gRPC.

        Deletes the specified conversation.

        Returns:
            Callable[[~.DeleteConversationRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_conversation" not in self._stubs:
            self._stubs["delete_conversation"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/DeleteConversation",
                request_serializer=agent_service.DeleteConversationRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_conversation"]

    @property
    def batch_delete_conversations(
        self,
    ) -> Callable[
        [agent_service.BatchDeleteConversationsRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the batch delete conversations method over gRPC.

        Batch deletes the specified conversations.

        Returns:
            Callable[[~.BatchDeleteConversationsRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "batch_delete_conversations" not in self._stubs:
            self._stubs["batch_delete_conversations"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.ces.v1beta.AgentService/BatchDeleteConversations",
                    request_serializer=agent_service.BatchDeleteConversationsRequest.serialize,
                    response_deserializer=operations_pb2.Operation.FromString,
                )
            )
        return self._stubs["batch_delete_conversations"]

    @property
    def create_tool(self) -> Callable[[agent_service.CreateToolRequest], gcc_tool.Tool]:
        r"""Return a callable for the create tool method over gRPC.

        Creates a new tool in the given app.

        Returns:
            Callable[[~.CreateToolRequest],
                    ~.Tool]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_tool" not in self._stubs:
            self._stubs["create_tool"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/CreateTool",
                request_serializer=agent_service.CreateToolRequest.serialize,
                response_deserializer=gcc_tool.Tool.deserialize,
            )
        return self._stubs["create_tool"]

    @property
    def update_tool(self) -> Callable[[agent_service.UpdateToolRequest], gcc_tool.Tool]:
        r"""Return a callable for the update tool method over gRPC.

        Updates the specified tool.

        Returns:
            Callable[[~.UpdateToolRequest],
                    ~.Tool]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_tool" not in self._stubs:
            self._stubs["update_tool"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/UpdateTool",
                request_serializer=agent_service.UpdateToolRequest.serialize,
                response_deserializer=gcc_tool.Tool.deserialize,
            )
        return self._stubs["update_tool"]

    @property
    def delete_tool(
        self,
    ) -> Callable[[agent_service.DeleteToolRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete tool method over gRPC.

        Deletes the specified tool.

        Returns:
            Callable[[~.DeleteToolRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_tool" not in self._stubs:
            self._stubs["delete_tool"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/DeleteTool",
                request_serializer=agent_service.DeleteToolRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_tool"]

    @property
    def list_guardrails(
        self,
    ) -> Callable[
        [agent_service.ListGuardrailsRequest], agent_service.ListGuardrailsResponse
    ]:
        r"""Return a callable for the list guardrails method over gRPC.

        Lists guardrails in the given app.

        Returns:
            Callable[[~.ListGuardrailsRequest],
                    ~.ListGuardrailsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_guardrails" not in self._stubs:
            self._stubs["list_guardrails"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/ListGuardrails",
                request_serializer=agent_service.ListGuardrailsRequest.serialize,
                response_deserializer=agent_service.ListGuardrailsResponse.deserialize,
            )
        return self._stubs["list_guardrails"]

    @property
    def get_guardrail(
        self,
    ) -> Callable[[agent_service.GetGuardrailRequest], guardrail.Guardrail]:
        r"""Return a callable for the get guardrail method over gRPC.

        Gets details of the specified guardrail.

        Returns:
            Callable[[~.GetGuardrailRequest],
                    ~.Guardrail]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_guardrail" not in self._stubs:
            self._stubs["get_guardrail"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/GetGuardrail",
                request_serializer=agent_service.GetGuardrailRequest.serialize,
                response_deserializer=guardrail.Guardrail.deserialize,
            )
        return self._stubs["get_guardrail"]

    @property
    def create_guardrail(
        self,
    ) -> Callable[[agent_service.CreateGuardrailRequest], gcc_guardrail.Guardrail]:
        r"""Return a callable for the create guardrail method over gRPC.

        Creates a new guardrail in the given app.

        Returns:
            Callable[[~.CreateGuardrailRequest],
                    ~.Guardrail]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_guardrail" not in self._stubs:
            self._stubs["create_guardrail"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/CreateGuardrail",
                request_serializer=agent_service.CreateGuardrailRequest.serialize,
                response_deserializer=gcc_guardrail.Guardrail.deserialize,
            )
        return self._stubs["create_guardrail"]

    @property
    def update_guardrail(
        self,
    ) -> Callable[[agent_service.UpdateGuardrailRequest], gcc_guardrail.Guardrail]:
        r"""Return a callable for the update guardrail method over gRPC.

        Updates the specified guardrail.

        Returns:
            Callable[[~.UpdateGuardrailRequest],
                    ~.Guardrail]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_guardrail" not in self._stubs:
            self._stubs["update_guardrail"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/UpdateGuardrail",
                request_serializer=agent_service.UpdateGuardrailRequest.serialize,
                response_deserializer=gcc_guardrail.Guardrail.deserialize,
            )
        return self._stubs["update_guardrail"]

    @property
    def delete_guardrail(
        self,
    ) -> Callable[[agent_service.DeleteGuardrailRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete guardrail method over gRPC.

        Deletes the specified guardrail.

        Returns:
            Callable[[~.DeleteGuardrailRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_guardrail" not in self._stubs:
            self._stubs["delete_guardrail"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/DeleteGuardrail",
                request_serializer=agent_service.DeleteGuardrailRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_guardrail"]

    @property
    def list_deployments(
        self,
    ) -> Callable[
        [agent_service.ListDeploymentsRequest], agent_service.ListDeploymentsResponse
    ]:
        r"""Return a callable for the list deployments method over gRPC.

        Lists deployments in the given app.

        Returns:
            Callable[[~.ListDeploymentsRequest],
                    ~.ListDeploymentsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_deployments" not in self._stubs:
            self._stubs["list_deployments"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/ListDeployments",
                request_serializer=agent_service.ListDeploymentsRequest.serialize,
                response_deserializer=agent_service.ListDeploymentsResponse.deserialize,
            )
        return self._stubs["list_deployments"]

    @property
    def get_deployment(
        self,
    ) -> Callable[[agent_service.GetDeploymentRequest], deployment.Deployment]:
        r"""Return a callable for the get deployment method over gRPC.

        Gets details of the specified deployment.

        Returns:
            Callable[[~.GetDeploymentRequest],
                    ~.Deployment]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_deployment" not in self._stubs:
            self._stubs["get_deployment"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/GetDeployment",
                request_serializer=agent_service.GetDeploymentRequest.serialize,
                response_deserializer=deployment.Deployment.deserialize,
            )
        return self._stubs["get_deployment"]

    @property
    def create_deployment(
        self,
    ) -> Callable[[agent_service.CreateDeploymentRequest], gcc_deployment.Deployment]:
        r"""Return a callable for the create deployment method over gRPC.

        Creates a new deployment in the given app.

        Returns:
            Callable[[~.CreateDeploymentRequest],
                    ~.Deployment]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_deployment" not in self._stubs:
            self._stubs["create_deployment"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/CreateDeployment",
                request_serializer=agent_service.CreateDeploymentRequest.serialize,
                response_deserializer=gcc_deployment.Deployment.deserialize,
            )
        return self._stubs["create_deployment"]

    @property
    def update_deployment(
        self,
    ) -> Callable[[agent_service.UpdateDeploymentRequest], gcc_deployment.Deployment]:
        r"""Return a callable for the update deployment method over gRPC.

        Updates the specified deployment.

        Returns:
            Callable[[~.UpdateDeploymentRequest],
                    ~.Deployment]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_deployment" not in self._stubs:
            self._stubs["update_deployment"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/UpdateDeployment",
                request_serializer=agent_service.UpdateDeploymentRequest.serialize,
                response_deserializer=gcc_deployment.Deployment.deserialize,
            )
        return self._stubs["update_deployment"]

    @property
    def delete_deployment(
        self,
    ) -> Callable[[agent_service.DeleteDeploymentRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete deployment method over gRPC.

        Deletes the specified deployment.

        Returns:
            Callable[[~.DeleteDeploymentRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_deployment" not in self._stubs:
            self._stubs["delete_deployment"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/DeleteDeployment",
                request_serializer=agent_service.DeleteDeploymentRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_deployment"]

    @property
    def list_toolsets(
        self,
    ) -> Callable[
        [agent_service.ListToolsetsRequest], agent_service.ListToolsetsResponse
    ]:
        r"""Return a callable for the list toolsets method over gRPC.

        Lists toolsets in the given app.

        Returns:
            Callable[[~.ListToolsetsRequest],
                    ~.ListToolsetsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_toolsets" not in self._stubs:
            self._stubs["list_toolsets"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/ListToolsets",
                request_serializer=agent_service.ListToolsetsRequest.serialize,
                response_deserializer=agent_service.ListToolsetsResponse.deserialize,
            )
        return self._stubs["list_toolsets"]

    @property
    def get_toolset(
        self,
    ) -> Callable[[agent_service.GetToolsetRequest], toolset.Toolset]:
        r"""Return a callable for the get toolset method over gRPC.

        Gets details of the specified toolset.

        Returns:
            Callable[[~.GetToolsetRequest],
                    ~.Toolset]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_toolset" not in self._stubs:
            self._stubs["get_toolset"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/GetToolset",
                request_serializer=agent_service.GetToolsetRequest.serialize,
                response_deserializer=toolset.Toolset.deserialize,
            )
        return self._stubs["get_toolset"]

    @property
    def create_toolset(
        self,
    ) -> Callable[[agent_service.CreateToolsetRequest], gcc_toolset.Toolset]:
        r"""Return a callable for the create toolset method over gRPC.

        Creates a new toolset in the given app.

        Returns:
            Callable[[~.CreateToolsetRequest],
                    ~.Toolset]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_toolset" not in self._stubs:
            self._stubs["create_toolset"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/CreateToolset",
                request_serializer=agent_service.CreateToolsetRequest.serialize,
                response_deserializer=gcc_toolset.Toolset.deserialize,
            )
        return self._stubs["create_toolset"]

    @property
    def update_toolset(
        self,
    ) -> Callable[[agent_service.UpdateToolsetRequest], gcc_toolset.Toolset]:
        r"""Return a callable for the update toolset method over gRPC.

        Updates the specified toolset.

        Returns:
            Callable[[~.UpdateToolsetRequest],
                    ~.Toolset]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_toolset" not in self._stubs:
            self._stubs["update_toolset"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/UpdateToolset",
                request_serializer=agent_service.UpdateToolsetRequest.serialize,
                response_deserializer=gcc_toolset.Toolset.deserialize,
            )
        return self._stubs["update_toolset"]

    @property
    def delete_toolset(
        self,
    ) -> Callable[[agent_service.DeleteToolsetRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete toolset method over gRPC.

        Deletes the specified toolset.

        Returns:
            Callable[[~.DeleteToolsetRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_toolset" not in self._stubs:
            self._stubs["delete_toolset"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/DeleteToolset",
                request_serializer=agent_service.DeleteToolsetRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_toolset"]

    @property
    def list_app_versions(
        self,
    ) -> Callable[
        [agent_service.ListAppVersionsRequest], agent_service.ListAppVersionsResponse
    ]:
        r"""Return a callable for the list app versions method over gRPC.

        Lists all app versions in the given app.

        Returns:
            Callable[[~.ListAppVersionsRequest],
                    ~.ListAppVersionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_app_versions" not in self._stubs:
            self._stubs["list_app_versions"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/ListAppVersions",
                request_serializer=agent_service.ListAppVersionsRequest.serialize,
                response_deserializer=agent_service.ListAppVersionsResponse.deserialize,
            )
        return self._stubs["list_app_versions"]

    @property
    def get_app_version(
        self,
    ) -> Callable[[agent_service.GetAppVersionRequest], app_version.AppVersion]:
        r"""Return a callable for the get app version method over gRPC.

        Gets details of the specified app version.

        Returns:
            Callable[[~.GetAppVersionRequest],
                    ~.AppVersion]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_app_version" not in self._stubs:
            self._stubs["get_app_version"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/GetAppVersion",
                request_serializer=agent_service.GetAppVersionRequest.serialize,
                response_deserializer=app_version.AppVersion.deserialize,
            )
        return self._stubs["get_app_version"]

    @property
    def create_app_version(
        self,
    ) -> Callable[[agent_service.CreateAppVersionRequest], gcc_app_version.AppVersion]:
        r"""Return a callable for the create app version method over gRPC.

        Creates a new app version in the given app.

        Returns:
            Callable[[~.CreateAppVersionRequest],
                    ~.AppVersion]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_app_version" not in self._stubs:
            self._stubs["create_app_version"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/CreateAppVersion",
                request_serializer=agent_service.CreateAppVersionRequest.serialize,
                response_deserializer=gcc_app_version.AppVersion.deserialize,
            )
        return self._stubs["create_app_version"]

    @property
    def delete_app_version(
        self,
    ) -> Callable[[agent_service.DeleteAppVersionRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete app version method over gRPC.

        Deletes the specified app version.

        Returns:
            Callable[[~.DeleteAppVersionRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_app_version" not in self._stubs:
            self._stubs["delete_app_version"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/DeleteAppVersion",
                request_serializer=agent_service.DeleteAppVersionRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_app_version"]

    @property
    def restore_app_version(
        self,
    ) -> Callable[[agent_service.RestoreAppVersionRequest], operations_pb2.Operation]:
        r"""Return a callable for the restore app version method over gRPC.

        Restores the specified app version.
        This will create a new app version from the current
        draft app and overwrite the current draft with the
        specified app version.

        Returns:
            Callable[[~.RestoreAppVersionRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "restore_app_version" not in self._stubs:
            self._stubs["restore_app_version"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/RestoreAppVersion",
                request_serializer=agent_service.RestoreAppVersionRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["restore_app_version"]

    @property
    def generate_app_resource(
        self,
    ) -> Callable[[agent_service.GenerateAppResourceRequest], operations_pb2.Operation]:
        r"""Return a callable for the generate app resource method over gRPC.

        Generates specific resources (e.g. agent) in the app
        using LLM assistant.

        Returns:
            Callable[[~.GenerateAppResourceRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "generate_app_resource" not in self._stubs:
            self._stubs["generate_app_resource"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/GenerateAppResource",
                request_serializer=agent_service.GenerateAppResourceRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["generate_app_resource"]

    @property
    def list_changelogs(
        self,
    ) -> Callable[
        [agent_service.ListChangelogsRequest], agent_service.ListChangelogsResponse
    ]:
        r"""Return a callable for the list changelogs method over gRPC.

        Lists the changelogs of the specified app.

        Returns:
            Callable[[~.ListChangelogsRequest],
                    ~.ListChangelogsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_changelogs" not in self._stubs:
            self._stubs["list_changelogs"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/ListChangelogs",
                request_serializer=agent_service.ListChangelogsRequest.serialize,
                response_deserializer=agent_service.ListChangelogsResponse.deserialize,
            )
        return self._stubs["list_changelogs"]

    @property
    def get_changelog(
        self,
    ) -> Callable[[agent_service.GetChangelogRequest], changelog.Changelog]:
        r"""Return a callable for the get changelog method over gRPC.

        Gets the specified changelog.

        Returns:
            Callable[[~.GetChangelogRequest],
                    ~.Changelog]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_changelog" not in self._stubs:
            self._stubs["get_changelog"] = self._logged_channel.unary_unary(
                "/google.cloud.ces.v1beta.AgentService/GetChangelog",
                request_serializer=agent_service.GetChangelogRequest.serialize,
                response_deserializer=changelog.Changelog.deserialize,
            )
        return self._stubs["get_changelog"]

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


__all__ = ("AgentServiceGrpcTransport",)
