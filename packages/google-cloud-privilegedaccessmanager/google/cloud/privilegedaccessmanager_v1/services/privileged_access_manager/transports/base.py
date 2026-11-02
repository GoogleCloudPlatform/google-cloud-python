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
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.privilegedaccessmanager_v1 import gapic_version as package_version
from google.cloud.privilegedaccessmanager_v1.types import privilegedaccessmanager

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class PrivilegedAccessManagerTransport(abc.ABC):
    """Abstract transport class for PrivilegedAccessManager."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "privilegedaccessmanager.googleapis.com"

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
                 The hostname to connect to (default: 'privilegedaccessmanager.googleapis.com').
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
            self.check_onboarding_status: gapic_v1.method.wrap_method(
                self.check_onboarding_status,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_entitlements: gapic_v1.method.wrap_method(
                self.list_entitlements,
                default_timeout=None,
                client_info=client_info,
            ),
            self.search_entitlements: gapic_v1.method.wrap_method(
                self.search_entitlements,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_entitlement: gapic_v1.method.wrap_method(
                self.get_entitlement,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_entitlement: gapic_v1.method.wrap_method(
                self.create_entitlement,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_entitlement: gapic_v1.method.wrap_method(
                self.delete_entitlement,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_entitlement: gapic_v1.method.wrap_method(
                self.update_entitlement,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_grants: gapic_v1.method.wrap_method(
                self.list_grants,
                default_timeout=None,
                client_info=client_info,
            ),
            self.search_grants: gapic_v1.method.wrap_method(
                self.search_grants,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_grant: gapic_v1.method.wrap_method(
                self.get_grant,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_grant: gapic_v1.method.wrap_method(
                self.create_grant,
                default_timeout=None,
                client_info=client_info,
            ),
            self.approve_grant: gapic_v1.method.wrap_method(
                self.approve_grant,
                default_timeout=None,
                client_info=client_info,
            ),
            self.deny_grant: gapic_v1.method.wrap_method(
                self.deny_grant,
                default_timeout=None,
                client_info=client_info,
            ),
            self.revoke_grant: gapic_v1.method.wrap_method(
                self.revoke_grant,
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
    def check_onboarding_status(
        self,
    ) -> Callable[
        [privilegedaccessmanager.CheckOnboardingStatusRequest],
        Union[
            privilegedaccessmanager.CheckOnboardingStatusResponse,
            Awaitable[privilegedaccessmanager.CheckOnboardingStatusResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_entitlements(
        self,
    ) -> Callable[
        [privilegedaccessmanager.ListEntitlementsRequest],
        Union[
            privilegedaccessmanager.ListEntitlementsResponse,
            Awaitable[privilegedaccessmanager.ListEntitlementsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def search_entitlements(
        self,
    ) -> Callable[
        [privilegedaccessmanager.SearchEntitlementsRequest],
        Union[
            privilegedaccessmanager.SearchEntitlementsResponse,
            Awaitable[privilegedaccessmanager.SearchEntitlementsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_entitlement(
        self,
    ) -> Callable[
        [privilegedaccessmanager.GetEntitlementRequest],
        Union[
            privilegedaccessmanager.Entitlement,
            Awaitable[privilegedaccessmanager.Entitlement],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_entitlement(
        self,
    ) -> Callable[
        [privilegedaccessmanager.CreateEntitlementRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_entitlement(
        self,
    ) -> Callable[
        [privilegedaccessmanager.DeleteEntitlementRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_entitlement(
        self,
    ) -> Callable[
        [privilegedaccessmanager.UpdateEntitlementRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_grants(
        self,
    ) -> Callable[
        [privilegedaccessmanager.ListGrantsRequest],
        Union[
            privilegedaccessmanager.ListGrantsResponse,
            Awaitable[privilegedaccessmanager.ListGrantsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def search_grants(
        self,
    ) -> Callable[
        [privilegedaccessmanager.SearchGrantsRequest],
        Union[
            privilegedaccessmanager.SearchGrantsResponse,
            Awaitable[privilegedaccessmanager.SearchGrantsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_grant(
        self,
    ) -> Callable[
        [privilegedaccessmanager.GetGrantRequest],
        Union[privilegedaccessmanager.Grant, Awaitable[privilegedaccessmanager.Grant]],
    ]:
        raise NotImplementedError()

    @property
    def create_grant(
        self,
    ) -> Callable[
        [privilegedaccessmanager.CreateGrantRequest],
        Union[privilegedaccessmanager.Grant, Awaitable[privilegedaccessmanager.Grant]],
    ]:
        raise NotImplementedError()

    @property
    def approve_grant(
        self,
    ) -> Callable[
        [privilegedaccessmanager.ApproveGrantRequest],
        Union[privilegedaccessmanager.Grant, Awaitable[privilegedaccessmanager.Grant]],
    ]:
        raise NotImplementedError()

    @property
    def deny_grant(
        self,
    ) -> Callable[
        [privilegedaccessmanager.DenyGrantRequest],
        Union[privilegedaccessmanager.Grant, Awaitable[privilegedaccessmanager.Grant]],
    ]:
        raise NotImplementedError()

    @property
    def revoke_grant(
        self,
    ) -> Callable[
        [privilegedaccessmanager.RevokeGrantRequest],
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
    def delete_operation(
        self,
    ) -> Callable[
        [operations_pb2.DeleteOperationRequest],
        None,
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


__all__ = ("PrivilegedAccessManagerTransport",)
