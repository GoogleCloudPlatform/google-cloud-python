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

import google.api_core
import google.auth  # type: ignore
import google.protobuf
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

from google.cloud.networkconnectivity_v1beta import gapic_version as package_version
from google.cloud.networkconnectivity_v1beta.types import hub
from google.cloud.networkconnectivity_v1beta.types import hub as gcn_hub

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

        self._wrapped_methods: Dict[Callable, Callable] = {}

    @property
    def host(self):
        return self._host

    def _prep_wrapped_messages(self, client_info):
        # Precompute the wrapped methods.
        self._wrapped_methods = {
            self.list_hubs: gapic_v1.method.wrap_method(
                self.list_hubs,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_hub: gapic_v1.method.wrap_method(
                self.get_hub,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_hub: gapic_v1.method.wrap_method(
                self.create_hub,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_hub: gapic_v1.method.wrap_method(
                self.update_hub,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_hub: gapic_v1.method.wrap_method(
                self.delete_hub,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_hub_spokes: gapic_v1.method.wrap_method(
                self.list_hub_spokes,
                default_timeout=None,
                client_info=client_info,
            ),
            self.query_hub_status: gapic_v1.method.wrap_method(
                self.query_hub_status,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_spokes: gapic_v1.method.wrap_method(
                self.list_spokes,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_spoke: gapic_v1.method.wrap_method(
                self.get_spoke,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_spoke: gapic_v1.method.wrap_method(
                self.create_spoke,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_spoke: gapic_v1.method.wrap_method(
                self.update_spoke,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.reject_hub_spoke: gapic_v1.method.wrap_method(
                self.reject_hub_spoke,
                default_timeout=None,
                client_info=client_info,
            ),
            self.accept_hub_spoke: gapic_v1.method.wrap_method(
                self.accept_hub_spoke,
                default_timeout=None,
                client_info=client_info,
            ),
            self.accept_spoke_update: gapic_v1.method.wrap_method(
                self.accept_spoke_update,
                default_timeout=None,
                client_info=client_info,
            ),
            self.reject_spoke_update: gapic_v1.method.wrap_method(
                self.reject_spoke_update,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_spoke: gapic_v1.method.wrap_method(
                self.delete_spoke,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_route_table: gapic_v1.method.wrap_method(
                self.get_route_table,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_route: gapic_v1.method.wrap_method(
                self.get_route,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_routes: gapic_v1.method.wrap_method(
                self.list_routes,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_route_tables: gapic_v1.method.wrap_method(
                self.list_route_tables,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_group: gapic_v1.method.wrap_method(
                self.get_group,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_groups: gapic_v1.method.wrap_method(
                self.list_groups,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_group: gapic_v1.method.wrap_method(
                self.update_group,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_gateway_advertised_route: gapic_v1.method.wrap_method(
                self.create_gateway_advertised_route,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_gateway_advertised_route: gapic_v1.method.wrap_method(
                self.get_gateway_advertised_route,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_gateway_advertised_routes: gapic_v1.method.wrap_method(
                self.list_gateway_advertised_routes,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_gateway_advertised_route: gapic_v1.method.wrap_method(
                self.update_gateway_advertised_route,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_gateway_advertised_route: gapic_v1.method.wrap_method(
                self.delete_gateway_advertised_route,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_location: gapic_v1.method.wrap_method(
                self.get_location,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_locations: gapic_v1.method.wrap_method(
                self.list_locations,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_iam_policy: gapic_v1.method.wrap_method(
                self.get_iam_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.set_iam_policy: gapic_v1.method.wrap_method(
                self.set_iam_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.test_iam_permissions: gapic_v1.method.wrap_method(
                self.test_iam_permissions,
                default_timeout=None,
                client_info=client_info,
            ),
            self.cancel_operation: gapic_v1.method.wrap_method(
                self.cancel_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_operation: gapic_v1.method.wrap_method(
                self.delete_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_operation: gapic_v1.method.wrap_method(
                self.get_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_operations: gapic_v1.method.wrap_method(
                self.list_operations,
                default_timeout=None,
                client_info=client_info,
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
    def create_gateway_advertised_route(
        self,
    ) -> Callable[
        [hub.CreateGatewayAdvertisedRouteRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_gateway_advertised_route(
        self,
    ) -> Callable[
        [hub.GetGatewayAdvertisedRouteRequest],
        Union[hub.GatewayAdvertisedRoute, Awaitable[hub.GatewayAdvertisedRoute]],
    ]:
        raise NotImplementedError()

    @property
    def list_gateway_advertised_routes(
        self,
    ) -> Callable[
        [hub.ListGatewayAdvertisedRoutesRequest],
        Union[
            hub.ListGatewayAdvertisedRoutesResponse,
            Awaitable[hub.ListGatewayAdvertisedRoutesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_gateway_advertised_route(
        self,
    ) -> Callable[
        [hub.UpdateGatewayAdvertisedRouteRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_gateway_advertised_route(
        self,
    ) -> Callable[
        [hub.DeleteGatewayAdvertisedRouteRequest],
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
