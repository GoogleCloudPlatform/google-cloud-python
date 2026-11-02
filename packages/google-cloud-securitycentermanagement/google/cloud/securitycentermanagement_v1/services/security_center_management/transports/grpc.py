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

from google.cloud.securitycentermanagement_v1.types import security_center_management

from .base import DEFAULT_CLIENT_INFO, SecurityCenterManagementTransport

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
                    "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
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
                    "serviceName": "google.cloud.securitycentermanagement.v1.SecurityCenterManagement",
                    "rpcName": client_call_details.method,
                    "response": grpc_response,
                    "metadata": grpc_response["metadata"],
                },
            )
        return response


class SecurityCenterManagementGrpcTransport(SecurityCenterManagementTransport):
    """gRPC backend transport for SecurityCenterManagement.

    Service describing handlers for resources

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
        host: str = "securitycentermanagement.googleapis.com",
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
                 The hostname to connect to (default: 'securitycentermanagement.googleapis.com').
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
        host: str = "securitycentermanagement.googleapis.com",
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
    def list_effective_security_health_analytics_custom_modules(
        self,
    ) -> Callable[
        [
            security_center_management.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest
        ],
        security_center_management.ListEffectiveSecurityHealthAnalyticsCustomModulesResponse,
    ]:
        r"""Return a callable for the list effective security health
        analytics custom modules method over gRPC.

        Returns a list of all
        [EffectiveSecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.EffectiveSecurityHealthAnalyticsCustomModule]
        resources for the given parent. This includes resident modules
        defined at the scope of the parent, and inherited modules,
        inherited from ancestor organizations, folders, and projects (no
        descendants).

        Returns:
            Callable[[~.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest],
                    ~.ListEffectiveSecurityHealthAnalyticsCustomModulesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_effective_security_health_analytics_custom_modules" not in self._stubs:
            self._stubs["list_effective_security_health_analytics_custom_modules"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.securitycentermanagement.v1.SecurityCenterManagement/ListEffectiveSecurityHealthAnalyticsCustomModules",
                    request_serializer=security_center_management.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest.serialize,
                    response_deserializer=security_center_management.ListEffectiveSecurityHealthAnalyticsCustomModulesResponse.deserialize,
                )
            )
        return self._stubs["list_effective_security_health_analytics_custom_modules"]

    @property
    def get_effective_security_health_analytics_custom_module(
        self,
    ) -> Callable[
        [
            security_center_management.GetEffectiveSecurityHealthAnalyticsCustomModuleRequest
        ],
        security_center_management.EffectiveSecurityHealthAnalyticsCustomModule,
    ]:
        r"""Return a callable for the get effective security health
        analytics custom module method over gRPC.

        Gets details of a single
        [EffectiveSecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.EffectiveSecurityHealthAnalyticsCustomModule].

        Returns:
            Callable[[~.GetEffectiveSecurityHealthAnalyticsCustomModuleRequest],
                    ~.EffectiveSecurityHealthAnalyticsCustomModule]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_effective_security_health_analytics_custom_module" not in self._stubs:
            self._stubs["get_effective_security_health_analytics_custom_module"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.securitycentermanagement.v1.SecurityCenterManagement/GetEffectiveSecurityHealthAnalyticsCustomModule",
                    request_serializer=security_center_management.GetEffectiveSecurityHealthAnalyticsCustomModuleRequest.serialize,
                    response_deserializer=security_center_management.EffectiveSecurityHealthAnalyticsCustomModule.deserialize,
                )
            )
        return self._stubs["get_effective_security_health_analytics_custom_module"]

    @property
    def list_security_health_analytics_custom_modules(
        self,
    ) -> Callable[
        [security_center_management.ListSecurityHealthAnalyticsCustomModulesRequest],
        security_center_management.ListSecurityHealthAnalyticsCustomModulesResponse,
    ]:
        r"""Return a callable for the list security health analytics
        custom modules method over gRPC.

        Returns a list of all
        [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule]
        resources for the given parent. This includes resident modules
        defined at the scope of the parent, and inherited modules,
        inherited from ancestor organizations, folders, and projects (no
        descendants).

        Returns:
            Callable[[~.ListSecurityHealthAnalyticsCustomModulesRequest],
                    ~.ListSecurityHealthAnalyticsCustomModulesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_security_health_analytics_custom_modules" not in self._stubs:
            self._stubs["list_security_health_analytics_custom_modules"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.securitycentermanagement.v1.SecurityCenterManagement/ListSecurityHealthAnalyticsCustomModules",
                    request_serializer=security_center_management.ListSecurityHealthAnalyticsCustomModulesRequest.serialize,
                    response_deserializer=security_center_management.ListSecurityHealthAnalyticsCustomModulesResponse.deserialize,
                )
            )
        return self._stubs["list_security_health_analytics_custom_modules"]

    @property
    def list_descendant_security_health_analytics_custom_modules(
        self,
    ) -> Callable[
        [
            security_center_management.ListDescendantSecurityHealthAnalyticsCustomModulesRequest
        ],
        security_center_management.ListDescendantSecurityHealthAnalyticsCustomModulesResponse,
    ]:
        r"""Return a callable for the list descendant security
        health analytics custom modules method over gRPC.

        Returns a list of all resident
        [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule]
        resources under the given organization, folder, or project and
        all of its descendants.

        Returns:
            Callable[[~.ListDescendantSecurityHealthAnalyticsCustomModulesRequest],
                    ~.ListDescendantSecurityHealthAnalyticsCustomModulesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if (
            "list_descendant_security_health_analytics_custom_modules"
            not in self._stubs
        ):
            self._stubs["list_descendant_security_health_analytics_custom_modules"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.securitycentermanagement.v1.SecurityCenterManagement/ListDescendantSecurityHealthAnalyticsCustomModules",
                    request_serializer=security_center_management.ListDescendantSecurityHealthAnalyticsCustomModulesRequest.serialize,
                    response_deserializer=security_center_management.ListDescendantSecurityHealthAnalyticsCustomModulesResponse.deserialize,
                )
            )
        return self._stubs["list_descendant_security_health_analytics_custom_modules"]

    @property
    def get_security_health_analytics_custom_module(
        self,
    ) -> Callable[
        [security_center_management.GetSecurityHealthAnalyticsCustomModuleRequest],
        security_center_management.SecurityHealthAnalyticsCustomModule,
    ]:
        r"""Return a callable for the get security health analytics
        custom module method over gRPC.

        Retrieves a
        [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule].

        Returns:
            Callable[[~.GetSecurityHealthAnalyticsCustomModuleRequest],
                    ~.SecurityHealthAnalyticsCustomModule]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_security_health_analytics_custom_module" not in self._stubs:
            self._stubs["get_security_health_analytics_custom_module"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.securitycentermanagement.v1.SecurityCenterManagement/GetSecurityHealthAnalyticsCustomModule",
                    request_serializer=security_center_management.GetSecurityHealthAnalyticsCustomModuleRequest.serialize,
                    response_deserializer=security_center_management.SecurityHealthAnalyticsCustomModule.deserialize,
                )
            )
        return self._stubs["get_security_health_analytics_custom_module"]

    @property
    def create_security_health_analytics_custom_module(
        self,
    ) -> Callable[
        [security_center_management.CreateSecurityHealthAnalyticsCustomModuleRequest],
        security_center_management.SecurityHealthAnalyticsCustomModule,
    ]:
        r"""Return a callable for the create security health
        analytics custom module method over gRPC.

        Creates a resident
        [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule]
        at the scope of the given organization, folder, or project, and
        also creates inherited ``SecurityHealthAnalyticsCustomModule``
        resources for all folders and projects that are descendants of
        the given parent. These modules are enabled by default.

        Returns:
            Callable[[~.CreateSecurityHealthAnalyticsCustomModuleRequest],
                    ~.SecurityHealthAnalyticsCustomModule]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_security_health_analytics_custom_module" not in self._stubs:
            self._stubs["create_security_health_analytics_custom_module"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.securitycentermanagement.v1.SecurityCenterManagement/CreateSecurityHealthAnalyticsCustomModule",
                    request_serializer=security_center_management.CreateSecurityHealthAnalyticsCustomModuleRequest.serialize,
                    response_deserializer=security_center_management.SecurityHealthAnalyticsCustomModule.deserialize,
                )
            )
        return self._stubs["create_security_health_analytics_custom_module"]

    @property
    def update_security_health_analytics_custom_module(
        self,
    ) -> Callable[
        [security_center_management.UpdateSecurityHealthAnalyticsCustomModuleRequest],
        security_center_management.SecurityHealthAnalyticsCustomModule,
    ]:
        r"""Return a callable for the update security health
        analytics custom module method over gRPC.

        Updates the
        [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule]
        under the given name based on the given update mask. Updating
        the enablement state is supported on both resident and inherited
        modules (though resident modules cannot have an enablement state
        of "inherited"). Updating the display name and custom
        configuration of a module is supported on resident modules only.

        Returns:
            Callable[[~.UpdateSecurityHealthAnalyticsCustomModuleRequest],
                    ~.SecurityHealthAnalyticsCustomModule]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_security_health_analytics_custom_module" not in self._stubs:
            self._stubs["update_security_health_analytics_custom_module"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.securitycentermanagement.v1.SecurityCenterManagement/UpdateSecurityHealthAnalyticsCustomModule",
                    request_serializer=security_center_management.UpdateSecurityHealthAnalyticsCustomModuleRequest.serialize,
                    response_deserializer=security_center_management.SecurityHealthAnalyticsCustomModule.deserialize,
                )
            )
        return self._stubs["update_security_health_analytics_custom_module"]

    @property
    def delete_security_health_analytics_custom_module(
        self,
    ) -> Callable[
        [security_center_management.DeleteSecurityHealthAnalyticsCustomModuleRequest],
        empty_pb2.Empty,
    ]:
        r"""Return a callable for the delete security health
        analytics custom module method over gRPC.

        Deletes the specified
        [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule]
        and all of its descendants in the resource hierarchy. This
        method is only supported for resident custom modules.

        Returns:
            Callable[[~.DeleteSecurityHealthAnalyticsCustomModuleRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_security_health_analytics_custom_module" not in self._stubs:
            self._stubs["delete_security_health_analytics_custom_module"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.securitycentermanagement.v1.SecurityCenterManagement/DeleteSecurityHealthAnalyticsCustomModule",
                    request_serializer=security_center_management.DeleteSecurityHealthAnalyticsCustomModuleRequest.serialize,
                    response_deserializer=empty_pb2.Empty.FromString,
                )
            )
        return self._stubs["delete_security_health_analytics_custom_module"]

    @property
    def simulate_security_health_analytics_custom_module(
        self,
    ) -> Callable[
        [security_center_management.SimulateSecurityHealthAnalyticsCustomModuleRequest],
        security_center_management.SimulateSecurityHealthAnalyticsCustomModuleResponse,
    ]:
        r"""Return a callable for the simulate security health
        analytics custom module method over gRPC.

        Simulates the result of using a
        [SecurityHealthAnalyticsCustomModule][google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule]
        to check a resource.

        Returns:
            Callable[[~.SimulateSecurityHealthAnalyticsCustomModuleRequest],
                    ~.SimulateSecurityHealthAnalyticsCustomModuleResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "simulate_security_health_analytics_custom_module" not in self._stubs:
            self._stubs["simulate_security_health_analytics_custom_module"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.securitycentermanagement.v1.SecurityCenterManagement/SimulateSecurityHealthAnalyticsCustomModule",
                    request_serializer=security_center_management.SimulateSecurityHealthAnalyticsCustomModuleRequest.serialize,
                    response_deserializer=security_center_management.SimulateSecurityHealthAnalyticsCustomModuleResponse.deserialize,
                )
            )
        return self._stubs["simulate_security_health_analytics_custom_module"]

    @property
    def list_effective_event_threat_detection_custom_modules(
        self,
    ) -> Callable[
        [
            security_center_management.ListEffectiveEventThreatDetectionCustomModulesRequest
        ],
        security_center_management.ListEffectiveEventThreatDetectionCustomModulesResponse,
    ]:
        r"""Return a callable for the list effective event threat
        detection custom modules method over gRPC.

        Lists all effective Event Threat Detection custom
        modules for the given parent. This includes resident
        modules defined at the scope of the parent along with
        modules inherited from its ancestors.

        Returns:
            Callable[[~.ListEffectiveEventThreatDetectionCustomModulesRequest],
                    ~.ListEffectiveEventThreatDetectionCustomModulesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_effective_event_threat_detection_custom_modules" not in self._stubs:
            self._stubs["list_effective_event_threat_detection_custom_modules"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.securitycentermanagement.v1.SecurityCenterManagement/ListEffectiveEventThreatDetectionCustomModules",
                    request_serializer=security_center_management.ListEffectiveEventThreatDetectionCustomModulesRequest.serialize,
                    response_deserializer=security_center_management.ListEffectiveEventThreatDetectionCustomModulesResponse.deserialize,
                )
            )
        return self._stubs["list_effective_event_threat_detection_custom_modules"]

    @property
    def get_effective_event_threat_detection_custom_module(
        self,
    ) -> Callable[
        [
            security_center_management.GetEffectiveEventThreatDetectionCustomModuleRequest
        ],
        security_center_management.EffectiveEventThreatDetectionCustomModule,
    ]:
        r"""Return a callable for the get effective event threat
        detection custom module method over gRPC.

        Gets the effective Event Threat Detection custom module at the
        given level.

        The difference between an
        [EffectiveEventThreatDetectionCustomModule][google.cloud.securitycentermanagement.v1.EffectiveEventThreatDetectionCustomModule]
        and an
        [EventThreatDetectionCustomModule][google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule]
        is that the fields for an
        ``EffectiveEventThreatDetectionCustomModule`` are computed from
        ancestors if needed. For example, the enablement state for an
        ``EventThreatDetectionCustomModule`` can be ``ENABLED``,
        ``DISABLED``, or ``INHERITED``. In contrast, the enablement
        state for an ``EffectiveEventThreatDetectionCustomModule`` is
        always computed as ``ENABLED`` or ``DISABLED``.

        Returns:
            Callable[[~.GetEffectiveEventThreatDetectionCustomModuleRequest],
                    ~.EffectiveEventThreatDetectionCustomModule]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_effective_event_threat_detection_custom_module" not in self._stubs:
            self._stubs["get_effective_event_threat_detection_custom_module"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.securitycentermanagement.v1.SecurityCenterManagement/GetEffectiveEventThreatDetectionCustomModule",
                    request_serializer=security_center_management.GetEffectiveEventThreatDetectionCustomModuleRequest.serialize,
                    response_deserializer=security_center_management.EffectiveEventThreatDetectionCustomModule.deserialize,
                )
            )
        return self._stubs["get_effective_event_threat_detection_custom_module"]

    @property
    def list_event_threat_detection_custom_modules(
        self,
    ) -> Callable[
        [security_center_management.ListEventThreatDetectionCustomModulesRequest],
        security_center_management.ListEventThreatDetectionCustomModulesResponse,
    ]:
        r"""Return a callable for the list event threat detection
        custom modules method over gRPC.

        Lists all Event Threat Detection custom modules for
        the given organization, folder, or project. This
        includes resident modules defined at the scope of the
        parent along with modules inherited from ancestors.

        Returns:
            Callable[[~.ListEventThreatDetectionCustomModulesRequest],
                    ~.ListEventThreatDetectionCustomModulesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_event_threat_detection_custom_modules" not in self._stubs:
            self._stubs["list_event_threat_detection_custom_modules"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.securitycentermanagement.v1.SecurityCenterManagement/ListEventThreatDetectionCustomModules",
                    request_serializer=security_center_management.ListEventThreatDetectionCustomModulesRequest.serialize,
                    response_deserializer=security_center_management.ListEventThreatDetectionCustomModulesResponse.deserialize,
                )
            )
        return self._stubs["list_event_threat_detection_custom_modules"]

    @property
    def list_descendant_event_threat_detection_custom_modules(
        self,
    ) -> Callable[
        [
            security_center_management.ListDescendantEventThreatDetectionCustomModulesRequest
        ],
        security_center_management.ListDescendantEventThreatDetectionCustomModulesResponse,
    ]:
        r"""Return a callable for the list descendant event threat
        detection custom modules method over gRPC.

        Lists all resident Event Threat Detection custom
        modules for the given organization, folder, or project
        and its descendants.

        Returns:
            Callable[[~.ListDescendantEventThreatDetectionCustomModulesRequest],
                    ~.ListDescendantEventThreatDetectionCustomModulesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_descendant_event_threat_detection_custom_modules" not in self._stubs:
            self._stubs["list_descendant_event_threat_detection_custom_modules"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.securitycentermanagement.v1.SecurityCenterManagement/ListDescendantEventThreatDetectionCustomModules",
                    request_serializer=security_center_management.ListDescendantEventThreatDetectionCustomModulesRequest.serialize,
                    response_deserializer=security_center_management.ListDescendantEventThreatDetectionCustomModulesResponse.deserialize,
                )
            )
        return self._stubs["list_descendant_event_threat_detection_custom_modules"]

    @property
    def get_event_threat_detection_custom_module(
        self,
    ) -> Callable[
        [security_center_management.GetEventThreatDetectionCustomModuleRequest],
        security_center_management.EventThreatDetectionCustomModule,
    ]:
        r"""Return a callable for the get event threat detection
        custom module method over gRPC.

        Gets an Event Threat Detection custom module.

        Returns:
            Callable[[~.GetEventThreatDetectionCustomModuleRequest],
                    ~.EventThreatDetectionCustomModule]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_event_threat_detection_custom_module" not in self._stubs:
            self._stubs["get_event_threat_detection_custom_module"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.securitycentermanagement.v1.SecurityCenterManagement/GetEventThreatDetectionCustomModule",
                    request_serializer=security_center_management.GetEventThreatDetectionCustomModuleRequest.serialize,
                    response_deserializer=security_center_management.EventThreatDetectionCustomModule.deserialize,
                )
            )
        return self._stubs["get_event_threat_detection_custom_module"]

    @property
    def create_event_threat_detection_custom_module(
        self,
    ) -> Callable[
        [security_center_management.CreateEventThreatDetectionCustomModuleRequest],
        security_center_management.EventThreatDetectionCustomModule,
    ]:
        r"""Return a callable for the create event threat detection
        custom module method over gRPC.

        Creates a resident Event Threat Detection custom
        module at the scope of the given organization, folder,
        or project, and creates inherited custom modules for all
        descendants of the given parent. These modules are
        enabled by default.

        Returns:
            Callable[[~.CreateEventThreatDetectionCustomModuleRequest],
                    ~.EventThreatDetectionCustomModule]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_event_threat_detection_custom_module" not in self._stubs:
            self._stubs["create_event_threat_detection_custom_module"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.securitycentermanagement.v1.SecurityCenterManagement/CreateEventThreatDetectionCustomModule",
                    request_serializer=security_center_management.CreateEventThreatDetectionCustomModuleRequest.serialize,
                    response_deserializer=security_center_management.EventThreatDetectionCustomModule.deserialize,
                )
            )
        return self._stubs["create_event_threat_detection_custom_module"]

    @property
    def update_event_threat_detection_custom_module(
        self,
    ) -> Callable[
        [security_center_management.UpdateEventThreatDetectionCustomModuleRequest],
        security_center_management.EventThreatDetectionCustomModule,
    ]:
        r"""Return a callable for the update event threat detection
        custom module method over gRPC.

        Updates the Event Threat Detection custom module with
        the given name based on the given update mask. Updating
        the enablement state is supported for both resident and
        inherited modules (though resident modules cannot have
        an enablement state of "inherited"). Updating the
        display name or configuration of a module is supported
        for resident modules only. The type of a module cannot
        be changed.

        Returns:
            Callable[[~.UpdateEventThreatDetectionCustomModuleRequest],
                    ~.EventThreatDetectionCustomModule]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_event_threat_detection_custom_module" not in self._stubs:
            self._stubs["update_event_threat_detection_custom_module"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.securitycentermanagement.v1.SecurityCenterManagement/UpdateEventThreatDetectionCustomModule",
                    request_serializer=security_center_management.UpdateEventThreatDetectionCustomModuleRequest.serialize,
                    response_deserializer=security_center_management.EventThreatDetectionCustomModule.deserialize,
                )
            )
        return self._stubs["update_event_threat_detection_custom_module"]

    @property
    def delete_event_threat_detection_custom_module(
        self,
    ) -> Callable[
        [security_center_management.DeleteEventThreatDetectionCustomModuleRequest],
        empty_pb2.Empty,
    ]:
        r"""Return a callable for the delete event threat detection
        custom module method over gRPC.

        Deletes the specified Event Threat Detection custom
        module and all of its descendants in the resource
        hierarchy. This method is only supported for resident
        custom modules.

        Returns:
            Callable[[~.DeleteEventThreatDetectionCustomModuleRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_event_threat_detection_custom_module" not in self._stubs:
            self._stubs["delete_event_threat_detection_custom_module"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.securitycentermanagement.v1.SecurityCenterManagement/DeleteEventThreatDetectionCustomModule",
                    request_serializer=security_center_management.DeleteEventThreatDetectionCustomModuleRequest.serialize,
                    response_deserializer=empty_pb2.Empty.FromString,
                )
            )
        return self._stubs["delete_event_threat_detection_custom_module"]

    @property
    def validate_event_threat_detection_custom_module(
        self,
    ) -> Callable[
        [security_center_management.ValidateEventThreatDetectionCustomModuleRequest],
        security_center_management.ValidateEventThreatDetectionCustomModuleResponse,
    ]:
        r"""Return a callable for the validate event threat
        detection custom module method over gRPC.

        Validates the given Event Threat Detection custom
        module.

        Returns:
            Callable[[~.ValidateEventThreatDetectionCustomModuleRequest],
                    ~.ValidateEventThreatDetectionCustomModuleResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "validate_event_threat_detection_custom_module" not in self._stubs:
            self._stubs["validate_event_threat_detection_custom_module"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.securitycentermanagement.v1.SecurityCenterManagement/ValidateEventThreatDetectionCustomModule",
                    request_serializer=security_center_management.ValidateEventThreatDetectionCustomModuleRequest.serialize,
                    response_deserializer=security_center_management.ValidateEventThreatDetectionCustomModuleResponse.deserialize,
                )
            )
        return self._stubs["validate_event_threat_detection_custom_module"]

    @property
    def get_security_center_service(
        self,
    ) -> Callable[
        [security_center_management.GetSecurityCenterServiceRequest],
        security_center_management.SecurityCenterService,
    ]:
        r"""Return a callable for the get security center service method over gRPC.

        Gets service settings for the specified Security
        Command Center service.

        Returns:
            Callable[[~.GetSecurityCenterServiceRequest],
                    ~.SecurityCenterService]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_security_center_service" not in self._stubs:
            self._stubs["get_security_center_service"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.securitycentermanagement.v1.SecurityCenterManagement/GetSecurityCenterService",
                    request_serializer=security_center_management.GetSecurityCenterServiceRequest.serialize,
                    response_deserializer=security_center_management.SecurityCenterService.deserialize,
                )
            )
        return self._stubs["get_security_center_service"]

    @property
    def list_security_center_services(
        self,
    ) -> Callable[
        [security_center_management.ListSecurityCenterServicesRequest],
        security_center_management.ListSecurityCenterServicesResponse,
    ]:
        r"""Return a callable for the list security center services method over gRPC.

        Returns a list of all Security Command Center
        services for the given parent.

        Returns:
            Callable[[~.ListSecurityCenterServicesRequest],
                    ~.ListSecurityCenterServicesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_security_center_services" not in self._stubs:
            self._stubs["list_security_center_services"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.securitycentermanagement.v1.SecurityCenterManagement/ListSecurityCenterServices",
                    request_serializer=security_center_management.ListSecurityCenterServicesRequest.serialize,
                    response_deserializer=security_center_management.ListSecurityCenterServicesResponse.deserialize,
                )
            )
        return self._stubs["list_security_center_services"]

    @property
    def update_security_center_service(
        self,
    ) -> Callable[
        [security_center_management.UpdateSecurityCenterServiceRequest],
        security_center_management.SecurityCenterService,
    ]:
        r"""Return a callable for the update security center service method over gRPC.

        Updates a Security Command Center service using the
        given update mask.

        Returns:
            Callable[[~.UpdateSecurityCenterServiceRequest],
                    ~.SecurityCenterService]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_security_center_service" not in self._stubs:
            self._stubs["update_security_center_service"] = (
                self._logged_channel.unary_unary(
                    "/google.cloud.securitycentermanagement.v1.SecurityCenterManagement/UpdateSecurityCenterService",
                    request_serializer=security_center_management.UpdateSecurityCenterServiceRequest.serialize,
                    response_deserializer=security_center_management.SecurityCenterService.deserialize,
                )
            )
        return self._stubs["update_security_center_service"]

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


__all__ = ("SecurityCenterManagementGrpcTransport",)
