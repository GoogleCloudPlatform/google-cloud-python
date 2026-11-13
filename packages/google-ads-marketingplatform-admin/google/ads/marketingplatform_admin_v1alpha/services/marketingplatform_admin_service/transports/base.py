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
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.ads.marketingplatform_admin_v1alpha import gapic_version as package_version
from google.ads.marketingplatform_admin_v1alpha.types import (
    marketingplatform_admin,
    resources,
)

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class MarketingplatformAdminServiceTransport(abc.ABC):
    """Abstract transport class for MarketingplatformAdminService."""

    AUTH_SCOPES = (
        "https://www.googleapis.com/auth/marketingplatformadmin.analytics.read",
        "https://www.googleapis.com/auth/marketingplatformadmin.analytics.update",
    )

    DEFAULT_HOST: str = "marketingplatformadmin.googleapis.com"

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
                 The hostname to connect to (default: 'marketingplatformadmin.googleapis.com').
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
            self.get_organization: gapic_v1.method.wrap_method(
                self.get_organization,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_organizations: gapic_v1.method.wrap_method(
                self.list_organizations,
                default_timeout=None,
                client_info=client_info,
            ),
            self.find_sales_partner_managed_clients: gapic_v1.method.wrap_method(
                self.find_sales_partner_managed_clients,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_analytics_account_links: gapic_v1.method.wrap_method(
                self.list_analytics_account_links,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_analytics_account_link: gapic_v1.method.wrap_method(
                self.create_analytics_account_link,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_analytics_account_link: gapic_v1.method.wrap_method(
                self.delete_analytics_account_link,
                default_timeout=None,
                client_info=client_info,
            ),
            self.set_property_service_level: gapic_v1.method.wrap_method(
                self.set_property_service_level,
                default_timeout=None,
                client_info=client_info,
            ),
            self.report_property_usage: gapic_v1.method.wrap_method(
                self.report_property_usage,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_user_group: gapic_v1.method.wrap_method(
                self.get_user_group,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_user_groups: gapic_v1.method.wrap_method(
                self.list_user_groups,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_user_group: gapic_v1.method.wrap_method(
                self.create_user_group,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_user_group: gapic_v1.method.wrap_method(
                self.update_user_group,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_user_group: gapic_v1.method.wrap_method(
                self.delete_user_group,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_user_group_member: gapic_v1.method.wrap_method(
                self.get_user_group_member,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_user_group_members: gapic_v1.method.wrap_method(
                self.list_user_group_members,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_user_group_member: gapic_v1.method.wrap_method(
                self.create_user_group_member,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_user_group_member: gapic_v1.method.wrap_method(
                self.update_user_group_member,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_user_group_member: gapic_v1.method.wrap_method(
                self.delete_user_group_member,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_admin_access_binding: gapic_v1.method.wrap_method(
                self.get_admin_access_binding,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_admin_access_bindings: gapic_v1.method.wrap_method(
                self.list_admin_access_bindings,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_admin_access_binding: gapic_v1.method.wrap_method(
                self.create_admin_access_binding,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_admin_access_binding: gapic_v1.method.wrap_method(
                self.update_admin_access_binding,
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
    def get_organization(
        self,
    ) -> Callable[
        [marketingplatform_admin.GetOrganizationRequest],
        Union[resources.Organization, Awaitable[resources.Organization]],
    ]:
        raise NotImplementedError()

    @property
    def list_organizations(
        self,
    ) -> Callable[
        [marketingplatform_admin.ListOrganizationsRequest],
        Union[
            marketingplatform_admin.ListOrganizationsResponse,
            Awaitable[marketingplatform_admin.ListOrganizationsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def find_sales_partner_managed_clients(
        self,
    ) -> Callable[
        [marketingplatform_admin.FindSalesPartnerManagedClientsRequest],
        Union[
            marketingplatform_admin.FindSalesPartnerManagedClientsResponse,
            Awaitable[marketingplatform_admin.FindSalesPartnerManagedClientsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_analytics_account_links(
        self,
    ) -> Callable[
        [marketingplatform_admin.ListAnalyticsAccountLinksRequest],
        Union[
            marketingplatform_admin.ListAnalyticsAccountLinksResponse,
            Awaitable[marketingplatform_admin.ListAnalyticsAccountLinksResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_analytics_account_link(
        self,
    ) -> Callable[
        [marketingplatform_admin.CreateAnalyticsAccountLinkRequest],
        Union[
            resources.AnalyticsAccountLink, Awaitable[resources.AnalyticsAccountLink]
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_analytics_account_link(
        self,
    ) -> Callable[
        [marketingplatform_admin.DeleteAnalyticsAccountLinkRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def set_property_service_level(
        self,
    ) -> Callable[
        [marketingplatform_admin.SetPropertyServiceLevelRequest],
        Union[
            marketingplatform_admin.SetPropertyServiceLevelResponse,
            Awaitable[marketingplatform_admin.SetPropertyServiceLevelResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def report_property_usage(
        self,
    ) -> Callable[
        [marketingplatform_admin.ReportPropertyUsageRequest],
        Union[
            marketingplatform_admin.ReportPropertyUsageResponse,
            Awaitable[marketingplatform_admin.ReportPropertyUsageResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_user_group(
        self,
    ) -> Callable[
        [marketingplatform_admin.GetUserGroupRequest],
        Union[resources.UserGroup, Awaitable[resources.UserGroup]],
    ]:
        raise NotImplementedError()

    @property
    def list_user_groups(
        self,
    ) -> Callable[
        [marketingplatform_admin.ListUserGroupsRequest],
        Union[
            marketingplatform_admin.ListUserGroupsResponse,
            Awaitable[marketingplatform_admin.ListUserGroupsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_user_group(
        self,
    ) -> Callable[
        [marketingplatform_admin.CreateUserGroupRequest],
        Union[resources.UserGroup, Awaitable[resources.UserGroup]],
    ]:
        raise NotImplementedError()

    @property
    def update_user_group(
        self,
    ) -> Callable[
        [marketingplatform_admin.UpdateUserGroupRequest],
        Union[resources.UserGroup, Awaitable[resources.UserGroup]],
    ]:
        raise NotImplementedError()

    @property
    def delete_user_group(
        self,
    ) -> Callable[
        [marketingplatform_admin.DeleteUserGroupRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def get_user_group_member(
        self,
    ) -> Callable[
        [marketingplatform_admin.GetUserGroupMemberRequest],
        Union[resources.UserGroupMember, Awaitable[resources.UserGroupMember]],
    ]:
        raise NotImplementedError()

    @property
    def list_user_group_members(
        self,
    ) -> Callable[
        [marketingplatform_admin.ListUserGroupMembersRequest],
        Union[
            marketingplatform_admin.ListUserGroupMembersResponse,
            Awaitable[marketingplatform_admin.ListUserGroupMembersResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_user_group_member(
        self,
    ) -> Callable[
        [marketingplatform_admin.CreateUserGroupMemberRequest],
        Union[resources.UserGroupMember, Awaitable[resources.UserGroupMember]],
    ]:
        raise NotImplementedError()

    @property
    def update_user_group_member(
        self,
    ) -> Callable[
        [marketingplatform_admin.UpdateUserGroupMemberRequest],
        Union[resources.UserGroupMember, Awaitable[resources.UserGroupMember]],
    ]:
        raise NotImplementedError()

    @property
    def delete_user_group_member(
        self,
    ) -> Callable[
        [marketingplatform_admin.DeleteUserGroupMemberRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def get_admin_access_binding(
        self,
    ) -> Callable[
        [marketingplatform_admin.GetAdminAccessBindingRequest],
        Union[resources.AdminAccessBinding, Awaitable[resources.AdminAccessBinding]],
    ]:
        raise NotImplementedError()

    @property
    def list_admin_access_bindings(
        self,
    ) -> Callable[
        [marketingplatform_admin.ListAdminAccessBindingsRequest],
        Union[
            marketingplatform_admin.ListAdminAccessBindingsResponse,
            Awaitable[marketingplatform_admin.ListAdminAccessBindingsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_admin_access_binding(
        self,
    ) -> Callable[
        [marketingplatform_admin.CreateAdminAccessBindingRequest],
        Union[resources.AdminAccessBinding, Awaitable[resources.AdminAccessBinding]],
    ]:
        raise NotImplementedError()

    @property
    def update_admin_access_binding(
        self,
    ) -> Callable[
        [marketingplatform_admin.UpdateAdminAccessBindingRequest],
        Union[resources.AdminAccessBinding, Awaitable[resources.AdminAccessBinding]],
    ]:
        raise NotImplementedError()

    @property
    def kind(self) -> str:
        raise NotImplementedError()


__all__ = ("MarketingplatformAdminServiceTransport",)
