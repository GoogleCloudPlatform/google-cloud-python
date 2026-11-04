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

from google.cloud.networkconnectivity_v1 import gapic_version as package_version
from google.cloud.networkconnectivity_v1._compat import (
    ASYNC_WRAP_METHOD_SUPPORTS_KIND as _ASYNC_WRAP_METHOD_SUPPORTS_KIND,
)
from google.cloud.networkconnectivity_v1._compat import (
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

from google.cloud.networkconnectivity_v1.types import hub
from google.cloud.networkconnectivity_v1.types import hub as gcn_hub

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class HubServiceTransport(abc.ABC):
    """Abstract transport class for HubService."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "networkconnectivity.googleapis.com"

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
                 The hostname to connect to (default: 'networkconnectivity.googleapis.com').
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
            self.list_hubs: self._wrap_method(
                self.list_hubs,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkconnectivity.v1.HubService/ListHubs",
            ),
            self.get_hub: self._wrap_method(
                self.get_hub,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkconnectivity.v1.HubService/GetHub",
            ),
            self.create_hub: self._wrap_method(
                self.create_hub,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.networkconnectivity.v1.HubService/CreateHub",
            ),
            self.update_hub: self._wrap_method(
                self.update_hub,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.networkconnectivity.v1.HubService/UpdateHub",
            ),
            self.delete_hub: self._wrap_method(
                self.delete_hub,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.networkconnectivity.v1.HubService/DeleteHub",
            ),
            self.list_hub_spokes: self._wrap_method(
                self.list_hub_spokes,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkconnectivity.v1.HubService/ListHubSpokes",
            ),
            self.query_hub_status: self._wrap_method(
                self.query_hub_status,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkconnectivity.v1.HubService/QueryHubStatus",
            ),
            self.list_spokes: self._wrap_method(
                self.list_spokes,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkconnectivity.v1.HubService/ListSpokes",
            ),
            self.get_spoke: self._wrap_method(
                self.get_spoke,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkconnectivity.v1.HubService/GetSpoke",
            ),
            self.create_spoke: self._wrap_method(
                self.create_spoke,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.networkconnectivity.v1.HubService/CreateSpoke",
            ),
            self.update_spoke: self._wrap_method(
                self.update_spoke,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.networkconnectivity.v1.HubService/UpdateSpoke",
            ),
            self.reject_hub_spoke: self._wrap_method(
                self.reject_hub_spoke,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkconnectivity.v1.HubService/RejectHubSpoke",
            ),
            self.accept_hub_spoke: self._wrap_method(
                self.accept_hub_spoke,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkconnectivity.v1.HubService/AcceptHubSpoke",
            ),
            self.accept_spoke_update: self._wrap_method(
                self.accept_spoke_update,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkconnectivity.v1.HubService/AcceptSpokeUpdate",
            ),
            self.reject_spoke_update: self._wrap_method(
                self.reject_spoke_update,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkconnectivity.v1.HubService/RejectSpokeUpdate",
            ),
            self.delete_spoke: self._wrap_method(
                self.delete_spoke,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.networkconnectivity.v1.HubService/DeleteSpoke",
            ),
            self.get_route_table: self._wrap_method(
                self.get_route_table,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkconnectivity.v1.HubService/GetRouteTable",
            ),
            self.get_route: self._wrap_method(
                self.get_route,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkconnectivity.v1.HubService/GetRoute",
            ),
            self.list_routes: self._wrap_method(
                self.list_routes,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkconnectivity.v1.HubService/ListRoutes",
            ),
            self.list_route_tables: self._wrap_method(
                self.list_route_tables,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkconnectivity.v1.HubService/ListRouteTables",
            ),
            self.get_group: self._wrap_method(
                self.get_group,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkconnectivity.v1.HubService/GetGroup",
            ),
            self.list_groups: self._wrap_method(
                self.list_groups,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkconnectivity.v1.HubService/ListGroups",
            ),
            self.update_group: self._wrap_method(
                self.update_group,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.networkconnectivity.v1.HubService/UpdateGroup",
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
    def list_hubs(
        self,
    ) -> Callable[
        [hub.ListHubsRequest],
        Union[hub.ListHubsResponse, Awaitable[hub.ListHubsResponse]],
    ]:
        raise NotImplementedError()

    @property
    def get_hub(
        self,
    ) -> Callable[[hub.GetHubRequest], Union[hub.Hub, Awaitable[hub.Hub]]]:
        raise NotImplementedError()

    @property
    def create_hub(
        self,
    ) -> Callable[
        [gcn_hub.CreateHubRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_hub(
        self,
    ) -> Callable[
        [gcn_hub.UpdateHubRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_hub(
        self,
    ) -> Callable[
        [hub.DeleteHubRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_hub_spokes(
        self,
    ) -> Callable[
        [hub.ListHubSpokesRequest],
        Union[hub.ListHubSpokesResponse, Awaitable[hub.ListHubSpokesResponse]],
    ]:
        raise NotImplementedError()

    @property
    def query_hub_status(
        self,
    ) -> Callable[
        [hub.QueryHubStatusRequest],
        Union[hub.QueryHubStatusResponse, Awaitable[hub.QueryHubStatusResponse]],
    ]:
        raise NotImplementedError()

    @property
    def list_spokes(
        self,
    ) -> Callable[
        [hub.ListSpokesRequest],
        Union[hub.ListSpokesResponse, Awaitable[hub.ListSpokesResponse]],
    ]:
        raise NotImplementedError()

    @property
    def get_spoke(
        self,
    ) -> Callable[[hub.GetSpokeRequest], Union[hub.Spoke, Awaitable[hub.Spoke]]]:
        raise NotImplementedError()

    @property
    def create_spoke(
        self,
    ) -> Callable[
        [hub.CreateSpokeRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_spoke(
        self,
    ) -> Callable[
        [hub.UpdateSpokeRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def reject_hub_spoke(
        self,
    ) -> Callable[
        [hub.RejectHubSpokeRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def accept_hub_spoke(
        self,
    ) -> Callable[
        [hub.AcceptHubSpokeRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def accept_spoke_update(
        self,
    ) -> Callable[
        [hub.AcceptSpokeUpdateRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def reject_spoke_update(
        self,
    ) -> Callable[
        [hub.RejectSpokeUpdateRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_spoke(
        self,
    ) -> Callable[
        [hub.DeleteSpokeRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_route_table(
        self,
    ) -> Callable[
        [hub.GetRouteTableRequest], Union[hub.RouteTable, Awaitable[hub.RouteTable]]
    ]:
        raise NotImplementedError()

    @property
    def get_route(
        self,
    ) -> Callable[[hub.GetRouteRequest], Union[hub.Route, Awaitable[hub.Route]]]:
        raise NotImplementedError()

    @property
    def list_routes(
        self,
    ) -> Callable[
        [hub.ListRoutesRequest],
        Union[hub.ListRoutesResponse, Awaitable[hub.ListRoutesResponse]],
    ]:
        raise NotImplementedError()

    @property
    def list_route_tables(
        self,
    ) -> Callable[
        [hub.ListRouteTablesRequest],
        Union[hub.ListRouteTablesResponse, Awaitable[hub.ListRouteTablesResponse]],
    ]:
        raise NotImplementedError()

    @property
    def get_group(
        self,
    ) -> Callable[[hub.GetGroupRequest], Union[hub.Group, Awaitable[hub.Group]]]:
        raise NotImplementedError()

    @property
    def list_groups(
        self,
    ) -> Callable[
        [hub.ListGroupsRequest],
        Union[hub.ListGroupsResponse, Awaitable[hub.ListGroupsResponse]],
    ]:
        raise NotImplementedError()

    @property
    def update_group(
        self,
    ) -> Callable[
        [hub.UpdateGroupRequest],
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


__all__ = ("HubServiceTransport",)
