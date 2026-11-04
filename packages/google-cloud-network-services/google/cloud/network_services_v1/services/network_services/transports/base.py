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
import abc
from typing import Awaitable, Callable, Dict, Optional, Sequence, Union

from google.cloud.network_services_v1 import gapic_version as package_version
from google.cloud.network_services_v1._compat import (
    ASYNC_WRAP_METHOD_SUPPORTS_KIND as _ASYNC_WRAP_METHOD_SUPPORTS_KIND,
)
from google.cloud.network_services_v1._compat import (
    WRAP_METHOD_SUPPORTS_TRACING as _WRAP_METHOD_SUPPORTS_TRACING,
)

_ASYNC_WRAP_METHOD_SUPPORTS_TRACING = _WRAP_METHOD_SUPPORTS_TRACING
_WRAP_METHOD_SUPPORTS_KIND = _WRAP_METHOD_SUPPORTS_TRACING

import google.api_core
import google.auth  # type: ignore
import google.protobuf
from google.api_core import client_options as client_options_lib
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, operations_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.network_services_v1.types import (
    agent_gateway,
    endpoint_policy,
    extensibility,
    gateway,
    grpc_route,
    http_route,
    mesh,
    route_view,
    service_binding,
    service_lb_policy,
    tcp_route,
    tls_route,
)
from google.cloud.network_services_v1.types import agent_gateway as gcn_agent_gateway
from google.cloud.network_services_v1.types import (
    endpoint_policy as gcn_endpoint_policy,
)
from google.cloud.network_services_v1.types import gateway as gcn_gateway
from google.cloud.network_services_v1.types import grpc_route as gcn_grpc_route
from google.cloud.network_services_v1.types import http_route as gcn_http_route
from google.cloud.network_services_v1.types import mesh as gcn_mesh
from google.cloud.network_services_v1.types import (
    service_binding as gcn_service_binding,
)
from google.cloud.network_services_v1.types import (
    service_lb_policy as gcn_service_lb_policy,
)
from google.cloud.network_services_v1.types import tcp_route as gcn_tcp_route
from google.cloud.network_services_v1.types import tls_route as gcn_tls_route

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class NetworkServicesTransport(abc.ABC):
    """Abstract transport class for NetworkServices."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "networkservices.googleapis.com"

    def __init__(
        self,
        *,
        host: str = DEFAULT_HOST,
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        api_audience: Optional[str] = None,
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = None,
        **kwargs,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'networkservices.googleapis.com').
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            credentials_file (Optional[str]): Deprecated. A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials. This argument will be
                removed in the next major version of this library.
            scopes (Optional[Sequence[str]]): A list of scopes.
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
            client_options (Optional[Union[google.api_core.client_options.ClientOptions, dict]]):
                Custom options for the client, containing options such as
                custom OpenTelemetry tracer providers.
        """

        # Save the scopes.
        self._scopes = scopes
        if not hasattr(self, "_ignore_credentials"):
            self._ignore_credentials: bool = False

        # If no credentials are provided, then determine the appropriate
        # defaults.
        if credentials and credentials_file:
            raise core_exceptions.DuplicateCredentialArgs(
                "'credentials_file' and 'credentials' are mutually exclusive"
            )

        if credentials_file is not None:
            credentials, _ = google.auth.load_credentials_from_file(
                credentials_file,
                scopes=scopes,
                quota_project_id=quota_project_id,
                default_scopes=self.AUTH_SCOPES,
            )
        elif credentials is None and not self._ignore_credentials:
            credentials, _ = google.auth.default(
                scopes=scopes,
                quota_project_id=quota_project_id,
                default_scopes=self.AUTH_SCOPES,
            )
            # Don't apply audience if the credentials file passed from user.
            if hasattr(credentials, "with_gdch_audience"):
                credentials = credentials.with_gdch_audience(
                    api_audience if api_audience else host
                )

        # If the credentials are service account credentials, then always try to use self signed JWT.
        if (
            always_use_jwt_access
            and isinstance(credentials, service_account.Credentials)
            and hasattr(service_account.Credentials, "with_always_use_jwt_access")
        ):
            credentials = credentials.with_always_use_jwt_access(True)

        # Save the credentials.
        self._credentials = credentials

        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ":" not in host:
            host += ":443"
        self._host = host

        self._client_options = client_options
        self._wrapped_methods: Dict[Callable, Callable] = {}

    @property
    def host(self):
        return self._host

    def _wrap_method(self, func, *args, **kwargs):
        """Wrap an RPC method with common client-level features.

        Applies retry, timeout, metadata, and tracing wrappers to the
        underlying RPC method callable. If the runtime `google-api-core`
        version supports tracing, transport attributes (`client_options` and
        `kind`) are injected. Otherwise, tracing-specific arguments are
        stripped for backward compatibility with older `google-api-core`
        versions.
        """
        if _WRAP_METHOD_SUPPORTS_TRACING:
            kwargs["client_options"] = self._client_options
            try:
                kind = self.kind
            except NotImplementedError:
                kind = None
            if kind:
                kwargs["kind"] = kind
            return gapic_v1.method.wrap_method(func, *args, **kwargs)
        # Fallback for older runtime versions of google-api-core:
        # - Era 1 (< 2.29.0): Neither tracing args nor `kind` are supported.
        # - Era 2 (>= 2.29.0, < 2.36.0): `kind` is supported (prevents REST from
        #   falling back to gRPC wrapping), but tracing args are not.
        # (These fallbacks can be removed once google-api-core < 2.36.0 is no longer supported.)
        for k in ["client_options", "method_name", "is_streaming"]:
            kwargs.pop(k, None)

        try:
            kind = self.kind
        except NotImplementedError:
            kind = None

        if _WRAP_METHOD_SUPPORTS_KIND and kind:
            kwargs["kind"] = kind
        else:
            kwargs.pop("kind", None)

        return gapic_v1.method.wrap_method(func, *args, **kwargs)

    def _wrap_async_method(self, func, *args, **kwargs):
        """Wrap an async RPC method with common client-level features.

        Applies asynchronous retry, timeout, metadata, and tracing wrappers
        to the underlying RPC method callable. If the runtime `google-api-core`
        version supports tracing, transport attributes (`client_options` and
        `kind`) are injected. Otherwise, tracing-specific arguments are
        stripped for backward compatibility with older `google-api-core`
        versions.
        """
        if _ASYNC_WRAP_METHOD_SUPPORTS_TRACING:
            kwargs["client_options"] = self._client_options
            try:
                kind = self.kind
            except NotImplementedError:
                kind = None
            if kind:
                kwargs["kind"] = kind
            return gapic_v1.method_async.wrap_method(func, *args, **kwargs)
        # Fallback for older runtime versions of google-api-core:
        # - Era 1 (< 2.29.0): Neither tracing args nor `kind` are supported.
        # - Era 2 (>= 2.29.0, < 2.36.0): `kind` is supported (prevents REST from
        #   falling back to gRPC wrapping), but tracing args are not.
        # (These fallbacks can be removed once google-api-core < 2.36.0 is no longer supported.)
        for k in ["client_options", "method_name", "is_streaming"]:
            kwargs.pop(k, None)

        try:
            kind = self.kind
        except NotImplementedError:
            kind = None

        if _ASYNC_WRAP_METHOD_SUPPORTS_KIND and kind:
            kwargs["kind"] = kind
        else:
            kwargs.pop("kind", None)

        return gapic_v1.method_async.wrap_method(func, *args, **kwargs)

    def _prep_wrapped_messages(self, client_info):
        """Precompute and cache wrapped methods for RPC dispatch."""
        self._wrapped_methods = {
            self.list_endpoint_policies: self._wrap_method(
                self.list_endpoint_policies,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/ListEndpointPolicies",
            ),
            self.get_endpoint_policy: self._wrap_method(
                self.get_endpoint_policy,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/GetEndpointPolicy",
            ),
            self.create_endpoint_policy: self._wrap_method(
                self.create_endpoint_policy,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/CreateEndpointPolicy",
            ),
            self.update_endpoint_policy: self._wrap_method(
                self.update_endpoint_policy,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/UpdateEndpointPolicy",
            ),
            self.delete_endpoint_policy: self._wrap_method(
                self.delete_endpoint_policy,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/DeleteEndpointPolicy",
            ),
            self.list_wasm_plugin_versions: self._wrap_method(
                self.list_wasm_plugin_versions,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/ListWasmPluginVersions",
            ),
            self.get_wasm_plugin_version: self._wrap_method(
                self.get_wasm_plugin_version,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/GetWasmPluginVersion",
            ),
            self.create_wasm_plugin_version: self._wrap_method(
                self.create_wasm_plugin_version,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/CreateWasmPluginVersion",
            ),
            self.delete_wasm_plugin_version: self._wrap_method(
                self.delete_wasm_plugin_version,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/DeleteWasmPluginVersion",
            ),
            self.list_wasm_plugins: self._wrap_method(
                self.list_wasm_plugins,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/ListWasmPlugins",
            ),
            self.get_wasm_plugin: self._wrap_method(
                self.get_wasm_plugin,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/GetWasmPlugin",
            ),
            self.create_wasm_plugin: self._wrap_method(
                self.create_wasm_plugin,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/CreateWasmPlugin",
            ),
            self.update_wasm_plugin: self._wrap_method(
                self.update_wasm_plugin,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/UpdateWasmPlugin",
            ),
            self.delete_wasm_plugin: self._wrap_method(
                self.delete_wasm_plugin,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/DeleteWasmPlugin",
            ),
            self.list_gateways: self._wrap_method(
                self.list_gateways,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/ListGateways",
            ),
            self.get_gateway: self._wrap_method(
                self.get_gateway,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/GetGateway",
            ),
            self.create_gateway: self._wrap_method(
                self.create_gateway,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/CreateGateway",
            ),
            self.update_gateway: self._wrap_method(
                self.update_gateway,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/UpdateGateway",
            ),
            self.delete_gateway: self._wrap_method(
                self.delete_gateway,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/DeleteGateway",
            ),
            self.list_grpc_routes: self._wrap_method(
                self.list_grpc_routes,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/ListGrpcRoutes",
            ),
            self.get_grpc_route: self._wrap_method(
                self.get_grpc_route,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/GetGrpcRoute",
            ),
            self.create_grpc_route: self._wrap_method(
                self.create_grpc_route,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/CreateGrpcRoute",
            ),
            self.update_grpc_route: self._wrap_method(
                self.update_grpc_route,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/UpdateGrpcRoute",
            ),
            self.delete_grpc_route: self._wrap_method(
                self.delete_grpc_route,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/DeleteGrpcRoute",
            ),
            self.list_http_routes: self._wrap_method(
                self.list_http_routes,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/ListHttpRoutes",
            ),
            self.get_http_route: self._wrap_method(
                self.get_http_route,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/GetHttpRoute",
            ),
            self.create_http_route: self._wrap_method(
                self.create_http_route,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/CreateHttpRoute",
            ),
            self.update_http_route: self._wrap_method(
                self.update_http_route,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/UpdateHttpRoute",
            ),
            self.delete_http_route: self._wrap_method(
                self.delete_http_route,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/DeleteHttpRoute",
            ),
            self.list_tcp_routes: self._wrap_method(
                self.list_tcp_routes,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/ListTcpRoutes",
            ),
            self.get_tcp_route: self._wrap_method(
                self.get_tcp_route,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/GetTcpRoute",
            ),
            self.create_tcp_route: self._wrap_method(
                self.create_tcp_route,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/CreateTcpRoute",
            ),
            self.update_tcp_route: self._wrap_method(
                self.update_tcp_route,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/UpdateTcpRoute",
            ),
            self.delete_tcp_route: self._wrap_method(
                self.delete_tcp_route,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/DeleteTcpRoute",
            ),
            self.list_tls_routes: self._wrap_method(
                self.list_tls_routes,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/ListTlsRoutes",
            ),
            self.get_tls_route: self._wrap_method(
                self.get_tls_route,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/GetTlsRoute",
            ),
            self.create_tls_route: self._wrap_method(
                self.create_tls_route,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/CreateTlsRoute",
            ),
            self.update_tls_route: self._wrap_method(
                self.update_tls_route,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/UpdateTlsRoute",
            ),
            self.delete_tls_route: self._wrap_method(
                self.delete_tls_route,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/DeleteTlsRoute",
            ),
            self.list_service_bindings: self._wrap_method(
                self.list_service_bindings,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/ListServiceBindings",
            ),
            self.get_service_binding: self._wrap_method(
                self.get_service_binding,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/GetServiceBinding",
            ),
            self.create_service_binding: self._wrap_method(
                self.create_service_binding,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/CreateServiceBinding",
            ),
            self.update_service_binding: self._wrap_method(
                self.update_service_binding,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/UpdateServiceBinding",
            ),
            self.delete_service_binding: self._wrap_method(
                self.delete_service_binding,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/DeleteServiceBinding",
            ),
            self.list_meshes: self._wrap_method(
                self.list_meshes,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/ListMeshes",
            ),
            self.get_mesh: self._wrap_method(
                self.get_mesh,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/GetMesh",
            ),
            self.create_mesh: self._wrap_method(
                self.create_mesh,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/CreateMesh",
            ),
            self.update_mesh: self._wrap_method(
                self.update_mesh,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/UpdateMesh",
            ),
            self.delete_mesh: self._wrap_method(
                self.delete_mesh,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/DeleteMesh",
            ),
            self.list_service_lb_policies: self._wrap_method(
                self.list_service_lb_policies,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/ListServiceLbPolicies",
            ),
            self.get_service_lb_policy: self._wrap_method(
                self.get_service_lb_policy,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/GetServiceLbPolicy",
            ),
            self.create_service_lb_policy: self._wrap_method(
                self.create_service_lb_policy,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/CreateServiceLbPolicy",
            ),
            self.update_service_lb_policy: self._wrap_method(
                self.update_service_lb_policy,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/UpdateServiceLbPolicy",
            ),
            self.delete_service_lb_policy: self._wrap_method(
                self.delete_service_lb_policy,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/DeleteServiceLbPolicy",
            ),
            self.get_gateway_route_view: self._wrap_method(
                self.get_gateway_route_view,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/GetGatewayRouteView",
            ),
            self.get_mesh_route_view: self._wrap_method(
                self.get_mesh_route_view,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/GetMeshRouteView",
            ),
            self.list_gateway_route_views: self._wrap_method(
                self.list_gateway_route_views,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/ListGatewayRouteViews",
            ),
            self.list_mesh_route_views: self._wrap_method(
                self.list_mesh_route_views,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/ListMeshRouteViews",
            ),
            self.list_agent_gateways: self._wrap_method(
                self.list_agent_gateways,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/ListAgentGateways",
            ),
            self.get_agent_gateway: self._wrap_method(
                self.get_agent_gateway,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/GetAgentGateway",
            ),
            self.create_agent_gateway: self._wrap_method(
                self.create_agent_gateway,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/CreateAgentGateway",
            ),
            self.update_agent_gateway: self._wrap_method(
                self.update_agent_gateway,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/UpdateAgentGateway",
            ),
            self.delete_agent_gateway: self._wrap_method(
                self.delete_agent_gateway,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkservices.v1.NetworkServices/DeleteAgentGateway",
            ),
            self.get_location: self._wrap_method(
                self.get_location,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.location.Locations/GetLocation",
            ),
            self.list_locations: self._wrap_method(
                self.list_locations,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.location.Locations/ListLocations",
            ),
            self.get_iam_policy: self._wrap_method(
                self.get_iam_policy,
                default_timeout=None,
                client_info=client_info,
                method_name="google.iam.v1.IAMPolicy/GetIamPolicy",
            ),
            self.set_iam_policy: self._wrap_method(
                self.set_iam_policy,
                default_timeout=None,
                client_info=client_info,
                method_name="google.iam.v1.IAMPolicy/SetIamPolicy",
            ),
            self.test_iam_permissions: self._wrap_method(
                self.test_iam_permissions,
                default_timeout=None,
                client_info=client_info,
                method_name="google.iam.v1.IAMPolicy/TestIamPermissions",
            ),
            self.cancel_operation: self._wrap_method(
                self.cancel_operation,
                default_timeout=None,
                client_info=client_info,
                method_name="google.longrunning.Operations/CancelOperation",
            ),
            self.delete_operation: self._wrap_method(
                self.delete_operation,
                default_timeout=None,
                client_info=client_info,
                method_name="google.longrunning.Operations/DeleteOperation",
            ),
            self.get_operation: self._wrap_method(
                self.get_operation,
                default_timeout=None,
                client_info=client_info,
                method_name="google.longrunning.Operations/GetOperation",
            ),
            self.list_operations: self._wrap_method(
                self.list_operations,
                default_timeout=None,
                client_info=client_info,
                method_name="google.longrunning.Operations/ListOperations",
            ),
        }

    def close(self):
        """Closes resources associated with the transport.

        .. warning::
             Only call this method if the transport is NOT shared
             with other clients - this may cause errors in other clients!
        """
        raise NotImplementedError()

    @property
    def operations_client(self):
        """Return the client designed to process long-running operations."""
        raise NotImplementedError()

    @property
    def list_endpoint_policies(
        self,
    ) -> Callable[
        [endpoint_policy.ListEndpointPoliciesRequest],
        Union[
            endpoint_policy.ListEndpointPoliciesResponse,
            Awaitable[endpoint_policy.ListEndpointPoliciesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_endpoint_policy(
        self,
    ) -> Callable[
        [endpoint_policy.GetEndpointPolicyRequest],
        Union[
            endpoint_policy.EndpointPolicy, Awaitable[endpoint_policy.EndpointPolicy]
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_endpoint_policy(
        self,
    ) -> Callable[
        [gcn_endpoint_policy.CreateEndpointPolicyRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_endpoint_policy(
        self,
    ) -> Callable[
        [gcn_endpoint_policy.UpdateEndpointPolicyRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_endpoint_policy(
        self,
    ) -> Callable[
        [endpoint_policy.DeleteEndpointPolicyRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_wasm_plugin_versions(
        self,
    ) -> Callable[
        [extensibility.ListWasmPluginVersionsRequest],
        Union[
            extensibility.ListWasmPluginVersionsResponse,
            Awaitable[extensibility.ListWasmPluginVersionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_wasm_plugin_version(
        self,
    ) -> Callable[
        [extensibility.GetWasmPluginVersionRequest],
        Union[
            extensibility.WasmPluginVersion, Awaitable[extensibility.WasmPluginVersion]
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_wasm_plugin_version(
        self,
    ) -> Callable[
        [extensibility.CreateWasmPluginVersionRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_wasm_plugin_version(
        self,
    ) -> Callable[
        [extensibility.DeleteWasmPluginVersionRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_wasm_plugins(
        self,
    ) -> Callable[
        [extensibility.ListWasmPluginsRequest],
        Union[
            extensibility.ListWasmPluginsResponse,
            Awaitable[extensibility.ListWasmPluginsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_wasm_plugin(
        self,
    ) -> Callable[
        [extensibility.GetWasmPluginRequest],
        Union[extensibility.WasmPlugin, Awaitable[extensibility.WasmPlugin]],
    ]:
        raise NotImplementedError()

    @property
    def create_wasm_plugin(
        self,
    ) -> Callable[
        [extensibility.CreateWasmPluginRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_wasm_plugin(
        self,
    ) -> Callable[
        [extensibility.UpdateWasmPluginRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_wasm_plugin(
        self,
    ) -> Callable[
        [extensibility.DeleteWasmPluginRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_gateways(
        self,
    ) -> Callable[
        [gateway.ListGatewaysRequest],
        Union[gateway.ListGatewaysResponse, Awaitable[gateway.ListGatewaysResponse]],
    ]:
        raise NotImplementedError()

    @property
    def get_gateway(
        self,
    ) -> Callable[
        [gateway.GetGatewayRequest], Union[gateway.Gateway, Awaitable[gateway.Gateway]]
    ]:
        raise NotImplementedError()

    @property
    def create_gateway(
        self,
    ) -> Callable[
        [gcn_gateway.CreateGatewayRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_gateway(
        self,
    ) -> Callable[
        [gcn_gateway.UpdateGatewayRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_gateway(
        self,
    ) -> Callable[
        [gateway.DeleteGatewayRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_grpc_routes(
        self,
    ) -> Callable[
        [grpc_route.ListGrpcRoutesRequest],
        Union[
            grpc_route.ListGrpcRoutesResponse,
            Awaitable[grpc_route.ListGrpcRoutesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_grpc_route(
        self,
    ) -> Callable[
        [grpc_route.GetGrpcRouteRequest],
        Union[grpc_route.GrpcRoute, Awaitable[grpc_route.GrpcRoute]],
    ]:
        raise NotImplementedError()

    @property
    def create_grpc_route(
        self,
    ) -> Callable[
        [gcn_grpc_route.CreateGrpcRouteRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_grpc_route(
        self,
    ) -> Callable[
        [gcn_grpc_route.UpdateGrpcRouteRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_grpc_route(
        self,
    ) -> Callable[
        [grpc_route.DeleteGrpcRouteRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_http_routes(
        self,
    ) -> Callable[
        [http_route.ListHttpRoutesRequest],
        Union[
            http_route.ListHttpRoutesResponse,
            Awaitable[http_route.ListHttpRoutesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_http_route(
        self,
    ) -> Callable[
        [http_route.GetHttpRouteRequest],
        Union[http_route.HttpRoute, Awaitable[http_route.HttpRoute]],
    ]:
        raise NotImplementedError()

    @property
    def create_http_route(
        self,
    ) -> Callable[
        [gcn_http_route.CreateHttpRouteRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_http_route(
        self,
    ) -> Callable[
        [gcn_http_route.UpdateHttpRouteRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_http_route(
        self,
    ) -> Callable[
        [http_route.DeleteHttpRouteRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_tcp_routes(
        self,
    ) -> Callable[
        [tcp_route.ListTcpRoutesRequest],
        Union[
            tcp_route.ListTcpRoutesResponse, Awaitable[tcp_route.ListTcpRoutesResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_tcp_route(
        self,
    ) -> Callable[
        [tcp_route.GetTcpRouteRequest],
        Union[tcp_route.TcpRoute, Awaitable[tcp_route.TcpRoute]],
    ]:
        raise NotImplementedError()

    @property
    def create_tcp_route(
        self,
    ) -> Callable[
        [gcn_tcp_route.CreateTcpRouteRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_tcp_route(
        self,
    ) -> Callable[
        [gcn_tcp_route.UpdateTcpRouteRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_tcp_route(
        self,
    ) -> Callable[
        [tcp_route.DeleteTcpRouteRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_tls_routes(
        self,
    ) -> Callable[
        [tls_route.ListTlsRoutesRequest],
        Union[
            tls_route.ListTlsRoutesResponse, Awaitable[tls_route.ListTlsRoutesResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_tls_route(
        self,
    ) -> Callable[
        [tls_route.GetTlsRouteRequest],
        Union[tls_route.TlsRoute, Awaitable[tls_route.TlsRoute]],
    ]:
        raise NotImplementedError()

    @property
    def create_tls_route(
        self,
    ) -> Callable[
        [gcn_tls_route.CreateTlsRouteRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_tls_route(
        self,
    ) -> Callable[
        [gcn_tls_route.UpdateTlsRouteRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_tls_route(
        self,
    ) -> Callable[
        [tls_route.DeleteTlsRouteRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_service_bindings(
        self,
    ) -> Callable[
        [service_binding.ListServiceBindingsRequest],
        Union[
            service_binding.ListServiceBindingsResponse,
            Awaitable[service_binding.ListServiceBindingsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_service_binding(
        self,
    ) -> Callable[
        [service_binding.GetServiceBindingRequest],
        Union[
            service_binding.ServiceBinding, Awaitable[service_binding.ServiceBinding]
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_service_binding(
        self,
    ) -> Callable[
        [gcn_service_binding.CreateServiceBindingRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_service_binding(
        self,
    ) -> Callable[
        [gcn_service_binding.UpdateServiceBindingRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_service_binding(
        self,
    ) -> Callable[
        [service_binding.DeleteServiceBindingRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_meshes(
        self,
    ) -> Callable[
        [mesh.ListMeshesRequest],
        Union[mesh.ListMeshesResponse, Awaitable[mesh.ListMeshesResponse]],
    ]:
        raise NotImplementedError()

    @property
    def get_mesh(
        self,
    ) -> Callable[[mesh.GetMeshRequest], Union[mesh.Mesh, Awaitable[mesh.Mesh]]]:
        raise NotImplementedError()

    @property
    def create_mesh(
        self,
    ) -> Callable[
        [gcn_mesh.CreateMeshRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_mesh(
        self,
    ) -> Callable[
        [gcn_mesh.UpdateMeshRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_mesh(
        self,
    ) -> Callable[
        [mesh.DeleteMeshRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_service_lb_policies(
        self,
    ) -> Callable[
        [service_lb_policy.ListServiceLbPoliciesRequest],
        Union[
            service_lb_policy.ListServiceLbPoliciesResponse,
            Awaitable[service_lb_policy.ListServiceLbPoliciesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_service_lb_policy(
        self,
    ) -> Callable[
        [service_lb_policy.GetServiceLbPolicyRequest],
        Union[
            service_lb_policy.ServiceLbPolicy,
            Awaitable[service_lb_policy.ServiceLbPolicy],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_service_lb_policy(
        self,
    ) -> Callable[
        [gcn_service_lb_policy.CreateServiceLbPolicyRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_service_lb_policy(
        self,
    ) -> Callable[
        [gcn_service_lb_policy.UpdateServiceLbPolicyRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_service_lb_policy(
        self,
    ) -> Callable[
        [service_lb_policy.DeleteServiceLbPolicyRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_gateway_route_view(
        self,
    ) -> Callable[
        [route_view.GetGatewayRouteViewRequest],
        Union[route_view.GatewayRouteView, Awaitable[route_view.GatewayRouteView]],
    ]:
        raise NotImplementedError()

    @property
    def get_mesh_route_view(
        self,
    ) -> Callable[
        [route_view.GetMeshRouteViewRequest],
        Union[route_view.MeshRouteView, Awaitable[route_view.MeshRouteView]],
    ]:
        raise NotImplementedError()

    @property
    def list_gateway_route_views(
        self,
    ) -> Callable[
        [route_view.ListGatewayRouteViewsRequest],
        Union[
            route_view.ListGatewayRouteViewsResponse,
            Awaitable[route_view.ListGatewayRouteViewsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_mesh_route_views(
        self,
    ) -> Callable[
        [route_view.ListMeshRouteViewsRequest],
        Union[
            route_view.ListMeshRouteViewsResponse,
            Awaitable[route_view.ListMeshRouteViewsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_agent_gateways(
        self,
    ) -> Callable[
        [agent_gateway.ListAgentGatewaysRequest],
        Union[
            agent_gateway.ListAgentGatewaysResponse,
            Awaitable[agent_gateway.ListAgentGatewaysResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_agent_gateway(
        self,
    ) -> Callable[
        [agent_gateway.GetAgentGatewayRequest],
        Union[agent_gateway.AgentGateway, Awaitable[agent_gateway.AgentGateway]],
    ]:
        raise NotImplementedError()

    @property
    def create_agent_gateway(
        self,
    ) -> Callable[
        [gcn_agent_gateway.CreateAgentGatewayRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_agent_gateway(
        self,
    ) -> Callable[
        [gcn_agent_gateway.UpdateAgentGatewayRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_agent_gateway(
        self,
    ) -> Callable[
        [agent_gateway.DeleteAgentGatewayRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_operations(
        self,
    ) -> Callable[
        [operations_pb2.ListOperationsRequest],
        Union[
            operations_pb2.ListOperationsResponse,
            Awaitable[operations_pb2.ListOperationsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_operation(
        self,
    ) -> Callable[
        [operations_pb2.GetOperationRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def cancel_operation(
        self,
    ) -> Callable[
        [operations_pb2.CancelOperationRequest],
        None,
    ]:
        raise NotImplementedError()

    @property
    def delete_operation(
        self,
    ) -> Callable[
        [operations_pb2.DeleteOperationRequest],
        None,
    ]:
        raise NotImplementedError()

    @property
    def set_iam_policy(
        self,
    ) -> Callable[
        [iam_policy_pb2.SetIamPolicyRequest],
        Union[policy_pb2.Policy, Awaitable[policy_pb2.Policy]],
    ]:
        raise NotImplementedError()

    @property
    def get_iam_policy(
        self,
    ) -> Callable[
        [iam_policy_pb2.GetIamPolicyRequest],
        Union[policy_pb2.Policy, Awaitable[policy_pb2.Policy]],
    ]:
        raise NotImplementedError()

    @property
    def test_iam_permissions(
        self,
    ) -> Callable[
        [iam_policy_pb2.TestIamPermissionsRequest],
        Union[
            iam_policy_pb2.TestIamPermissionsResponse,
            Awaitable[iam_policy_pb2.TestIamPermissionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_location(
        self,
    ) -> Callable[
        [locations_pb2.GetLocationRequest],
        Union[locations_pb2.Location, Awaitable[locations_pb2.Location]],
    ]:
        raise NotImplementedError()

    @property
    def list_locations(
        self,
    ) -> Callable[
        [locations_pb2.ListLocationsRequest],
        Union[
            locations_pb2.ListLocationsResponse,
            Awaitable[locations_pb2.ListLocationsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def kind(self) -> str:
        raise NotImplementedError()


__all__ = ("NetworkServicesTransport",)
