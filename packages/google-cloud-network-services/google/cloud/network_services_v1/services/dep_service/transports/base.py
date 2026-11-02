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

from google.cloud.network_services_v1 import gapic_version as package_version
from google.cloud.network_services_v1.types import dep

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class DepServiceTransport(abc.ABC):
    """Abstract transport class for DepService."""

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
            self.list_lb_traffic_extensions: gapic_v1.method.wrap_method(
                self.list_lb_traffic_extensions,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_lb_traffic_extension: gapic_v1.method.wrap_method(
                self.get_lb_traffic_extension,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_lb_traffic_extension: gapic_v1.method.wrap_method(
                self.create_lb_traffic_extension,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_lb_traffic_extension: gapic_v1.method.wrap_method(
                self.update_lb_traffic_extension,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_lb_traffic_extension: gapic_v1.method.wrap_method(
                self.delete_lb_traffic_extension,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_lb_route_extensions: gapic_v1.method.wrap_method(
                self.list_lb_route_extensions,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_lb_route_extension: gapic_v1.method.wrap_method(
                self.get_lb_route_extension,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_lb_route_extension: gapic_v1.method.wrap_method(
                self.create_lb_route_extension,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_lb_route_extension: gapic_v1.method.wrap_method(
                self.update_lb_route_extension,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_lb_route_extension: gapic_v1.method.wrap_method(
                self.delete_lb_route_extension,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_lb_edge_extensions: gapic_v1.method.wrap_method(
                self.list_lb_edge_extensions,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_lb_edge_extension: gapic_v1.method.wrap_method(
                self.get_lb_edge_extension,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_lb_edge_extension: gapic_v1.method.wrap_method(
                self.create_lb_edge_extension,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_lb_edge_extension: gapic_v1.method.wrap_method(
                self.update_lb_edge_extension,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_lb_edge_extension: gapic_v1.method.wrap_method(
                self.delete_lb_edge_extension,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_authz_extensions: gapic_v1.method.wrap_method(
                self.list_authz_extensions,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_authz_extension: gapic_v1.method.wrap_method(
                self.get_authz_extension,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_authz_extension: gapic_v1.method.wrap_method(
                self.create_authz_extension,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_authz_extension: gapic_v1.method.wrap_method(
                self.update_authz_extension,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_authz_extension: gapic_v1.method.wrap_method(
                self.delete_authz_extension,
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
    def list_lb_traffic_extensions(
        self,
    ) -> Callable[
        [dep.ListLbTrafficExtensionsRequest],
        Union[
            dep.ListLbTrafficExtensionsResponse,
            Awaitable[dep.ListLbTrafficExtensionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_lb_traffic_extension(
        self,
    ) -> Callable[
        [dep.GetLbTrafficExtensionRequest],
        Union[dep.LbTrafficExtension, Awaitable[dep.LbTrafficExtension]],
    ]:
        raise NotImplementedError()

    @property
    def create_lb_traffic_extension(
        self,
    ) -> Callable[
        [dep.CreateLbTrafficExtensionRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_lb_traffic_extension(
        self,
    ) -> Callable[
        [dep.UpdateLbTrafficExtensionRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_lb_traffic_extension(
        self,
    ) -> Callable[
        [dep.DeleteLbTrafficExtensionRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_lb_route_extensions(
        self,
    ) -> Callable[
        [dep.ListLbRouteExtensionsRequest],
        Union[
            dep.ListLbRouteExtensionsResponse,
            Awaitable[dep.ListLbRouteExtensionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_lb_route_extension(
        self,
    ) -> Callable[
        [dep.GetLbRouteExtensionRequest],
        Union[dep.LbRouteExtension, Awaitable[dep.LbRouteExtension]],
    ]:
        raise NotImplementedError()

    @property
    def create_lb_route_extension(
        self,
    ) -> Callable[
        [dep.CreateLbRouteExtensionRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_lb_route_extension(
        self,
    ) -> Callable[
        [dep.UpdateLbRouteExtensionRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_lb_route_extension(
        self,
    ) -> Callable[
        [dep.DeleteLbRouteExtensionRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_lb_edge_extensions(
        self,
    ) -> Callable[
        [dep.ListLbEdgeExtensionsRequest],
        Union[
            dep.ListLbEdgeExtensionsResponse,
            Awaitable[dep.ListLbEdgeExtensionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_lb_edge_extension(
        self,
    ) -> Callable[
        [dep.GetLbEdgeExtensionRequest],
        Union[dep.LbEdgeExtension, Awaitable[dep.LbEdgeExtension]],
    ]:
        raise NotImplementedError()

    @property
    def create_lb_edge_extension(
        self,
    ) -> Callable[
        [dep.CreateLbEdgeExtensionRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_lb_edge_extension(
        self,
    ) -> Callable[
        [dep.UpdateLbEdgeExtensionRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_lb_edge_extension(
        self,
    ) -> Callable[
        [dep.DeleteLbEdgeExtensionRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_authz_extensions(
        self,
    ) -> Callable[
        [dep.ListAuthzExtensionsRequest],
        Union[
            dep.ListAuthzExtensionsResponse, Awaitable[dep.ListAuthzExtensionsResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_authz_extension(
        self,
    ) -> Callable[
        [dep.GetAuthzExtensionRequest],
        Union[dep.AuthzExtension, Awaitable[dep.AuthzExtension]],
    ]:
        raise NotImplementedError()

    @property
    def create_authz_extension(
        self,
    ) -> Callable[
        [dep.CreateAuthzExtensionRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_authz_extension(
        self,
    ) -> Callable[
        [dep.UpdateAuthzExtensionRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_authz_extension(
        self,
    ) -> Callable[
        [dep.DeleteAuthzExtensionRequest],
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


__all__ = ("DepServiceTransport",)
