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
import dataclasses
import json  # type: ignore
import logging
import warnings
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union

import google.protobuf
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.ads.marketingplatform_admin_v1alpha._compat import transcode_request
from google.ads.marketingplatform_admin_v1alpha.types import (
    marketingplatform_admin,
    resources,
)

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseMarketingplatformAdminServiceRestTransport

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object, None]  # type: ignore

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = logging.getLogger(__name__)

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=BASE_DEFAULT_CLIENT_INFO.gapic_version,
    grpc_version=None,
    rest_version=f"requests@{requests_version}",
)

DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class MarketingplatformAdminServiceRestInterceptor:
    """Interceptor for MarketingplatformAdminService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the MarketingplatformAdminServiceRestTransport.

    .. code-block:: python
        class MyCustomMarketingplatformAdminServiceInterceptor(MarketingplatformAdminServiceRestInterceptor):
            def pre_create_admin_access_binding(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_admin_access_binding(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_analytics_account_link(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_analytics_account_link(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_user_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_user_group(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_user_group_member(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_user_group_member(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_analytics_account_link(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_user_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_user_group_member(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_find_sales_partner_managed_clients(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_find_sales_partner_managed_clients(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_admin_access_binding(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_admin_access_binding(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_organization(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_organization(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_user_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_user_group(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_user_group_member(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_user_group_member(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_admin_access_bindings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_admin_access_bindings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_analytics_account_links(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_analytics_account_links(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_organizations(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_organizations(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_user_group_members(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_user_group_members(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_user_groups(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_user_groups(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_report_property_usage(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_report_property_usage(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_property_service_level(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_property_service_level(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_admin_access_binding(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_admin_access_binding(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_user_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_user_group(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_user_group_member(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_user_group_member(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = MarketingplatformAdminServiceRestTransport(interceptor=MyCustomMarketingplatformAdminServiceInterceptor())
        client = MarketingplatformAdminServiceClient(transport=transport)


    """

    def pre_create_admin_access_binding(
        self,
        request: marketingplatform_admin.CreateAdminAccessBindingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        marketingplatform_admin.CreateAdminAccessBindingRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_admin_access_binding

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MarketingplatformAdminService server.
        """
        return request, metadata

    def post_create_admin_access_binding(
        self, response: resources.AdminAccessBinding
    ) -> resources.AdminAccessBinding:
        """Post-rpc interceptor for create_admin_access_binding

        DEPRECATED. Please use the `post_create_admin_access_binding_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the MarketingplatformAdminService server but before
        it is returned to user code. This `post_create_admin_access_binding` interceptor runs
        before the `post_create_admin_access_binding_with_metadata` interceptor.
        """
        return response

    def post_create_admin_access_binding_with_metadata(
        self,
        response: resources.AdminAccessBinding,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.AdminAccessBinding, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_admin_access_binding

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the MarketingplatformAdminService server but before it is returned to user code.

        We recommend only using this `post_create_admin_access_binding_with_metadata`
        interceptor in new development instead of the `post_create_admin_access_binding` interceptor.
        When both interceptors are used, this `post_create_admin_access_binding_with_metadata` interceptor runs after the
        `post_create_admin_access_binding` interceptor. The (possibly modified) response returned by
        `post_create_admin_access_binding` will be passed to
        `post_create_admin_access_binding_with_metadata`.
        """
        return response, metadata

    def pre_create_analytics_account_link(
        self,
        request: marketingplatform_admin.CreateAnalyticsAccountLinkRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        marketingplatform_admin.CreateAnalyticsAccountLinkRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_analytics_account_link

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MarketingplatformAdminService server.
        """
        return request, metadata

    def post_create_analytics_account_link(
        self, response: resources.AnalyticsAccountLink
    ) -> resources.AnalyticsAccountLink:
        """Post-rpc interceptor for create_analytics_account_link

        DEPRECATED. Please use the `post_create_analytics_account_link_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the MarketingplatformAdminService server but before
        it is returned to user code. This `post_create_analytics_account_link` interceptor runs
        before the `post_create_analytics_account_link_with_metadata` interceptor.
        """
        return response

    def post_create_analytics_account_link_with_metadata(
        self,
        response: resources.AnalyticsAccountLink,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.AnalyticsAccountLink, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_analytics_account_link

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the MarketingplatformAdminService server but before it is returned to user code.

        We recommend only using this `post_create_analytics_account_link_with_metadata`
        interceptor in new development instead of the `post_create_analytics_account_link` interceptor.
        When both interceptors are used, this `post_create_analytics_account_link_with_metadata` interceptor runs after the
        `post_create_analytics_account_link` interceptor. The (possibly modified) response returned by
        `post_create_analytics_account_link` will be passed to
        `post_create_analytics_account_link_with_metadata`.
        """
        return response, metadata

    def pre_create_user_group(
        self,
        request: marketingplatform_admin.CreateUserGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        marketingplatform_admin.CreateUserGroupRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_user_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MarketingplatformAdminService server.
        """
        return request, metadata

    def post_create_user_group(
        self, response: resources.UserGroup
    ) -> resources.UserGroup:
        """Post-rpc interceptor for create_user_group

        DEPRECATED. Please use the `post_create_user_group_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the MarketingplatformAdminService server but before
        it is returned to user code. This `post_create_user_group` interceptor runs
        before the `post_create_user_group_with_metadata` interceptor.
        """
        return response

    def post_create_user_group_with_metadata(
        self,
        response: resources.UserGroup,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.UserGroup, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_user_group

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the MarketingplatformAdminService server but before it is returned to user code.

        We recommend only using this `post_create_user_group_with_metadata`
        interceptor in new development instead of the `post_create_user_group` interceptor.
        When both interceptors are used, this `post_create_user_group_with_metadata` interceptor runs after the
        `post_create_user_group` interceptor. The (possibly modified) response returned by
        `post_create_user_group` will be passed to
        `post_create_user_group_with_metadata`.
        """
        return response, metadata

    def pre_create_user_group_member(
        self,
        request: marketingplatform_admin.CreateUserGroupMemberRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        marketingplatform_admin.CreateUserGroupMemberRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_user_group_member

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MarketingplatformAdminService server.
        """
        return request, metadata

    def post_create_user_group_member(
        self, response: resources.UserGroupMember
    ) -> resources.UserGroupMember:
        """Post-rpc interceptor for create_user_group_member

        DEPRECATED. Please use the `post_create_user_group_member_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the MarketingplatformAdminService server but before
        it is returned to user code. This `post_create_user_group_member` interceptor runs
        before the `post_create_user_group_member_with_metadata` interceptor.
        """
        return response

    def post_create_user_group_member_with_metadata(
        self,
        response: resources.UserGroupMember,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.UserGroupMember, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_user_group_member

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the MarketingplatformAdminService server but before it is returned to user code.

        We recommend only using this `post_create_user_group_member_with_metadata`
        interceptor in new development instead of the `post_create_user_group_member` interceptor.
        When both interceptors are used, this `post_create_user_group_member_with_metadata` interceptor runs after the
        `post_create_user_group_member` interceptor. The (possibly modified) response returned by
        `post_create_user_group_member` will be passed to
        `post_create_user_group_member_with_metadata`.
        """
        return response, metadata

    def pre_delete_analytics_account_link(
        self,
        request: marketingplatform_admin.DeleteAnalyticsAccountLinkRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        marketingplatform_admin.DeleteAnalyticsAccountLinkRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_analytics_account_link

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MarketingplatformAdminService server.
        """
        return request, metadata

    def pre_delete_user_group(
        self,
        request: marketingplatform_admin.DeleteUserGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        marketingplatform_admin.DeleteUserGroupRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_user_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MarketingplatformAdminService server.
        """
        return request, metadata

    def pre_delete_user_group_member(
        self,
        request: marketingplatform_admin.DeleteUserGroupMemberRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        marketingplatform_admin.DeleteUserGroupMemberRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_user_group_member

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MarketingplatformAdminService server.
        """
        return request, metadata

    def pre_find_sales_partner_managed_clients(
        self,
        request: marketingplatform_admin.FindSalesPartnerManagedClientsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        marketingplatform_admin.FindSalesPartnerManagedClientsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for find_sales_partner_managed_clients

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MarketingplatformAdminService server.
        """
        return request, metadata

    def post_find_sales_partner_managed_clients(
        self, response: marketingplatform_admin.FindSalesPartnerManagedClientsResponse
    ) -> marketingplatform_admin.FindSalesPartnerManagedClientsResponse:
        """Post-rpc interceptor for find_sales_partner_managed_clients

        DEPRECATED. Please use the `post_find_sales_partner_managed_clients_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the MarketingplatformAdminService server but before
        it is returned to user code. This `post_find_sales_partner_managed_clients` interceptor runs
        before the `post_find_sales_partner_managed_clients_with_metadata` interceptor.
        """
        return response

    def post_find_sales_partner_managed_clients_with_metadata(
        self,
        response: marketingplatform_admin.FindSalesPartnerManagedClientsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        marketingplatform_admin.FindSalesPartnerManagedClientsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for find_sales_partner_managed_clients

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the MarketingplatformAdminService server but before it is returned to user code.

        We recommend only using this `post_find_sales_partner_managed_clients_with_metadata`
        interceptor in new development instead of the `post_find_sales_partner_managed_clients` interceptor.
        When both interceptors are used, this `post_find_sales_partner_managed_clients_with_metadata` interceptor runs after the
        `post_find_sales_partner_managed_clients` interceptor. The (possibly modified) response returned by
        `post_find_sales_partner_managed_clients` will be passed to
        `post_find_sales_partner_managed_clients_with_metadata`.
        """
        return response, metadata

    def pre_get_admin_access_binding(
        self,
        request: marketingplatform_admin.GetAdminAccessBindingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        marketingplatform_admin.GetAdminAccessBindingRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_admin_access_binding

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MarketingplatformAdminService server.
        """
        return request, metadata

    def post_get_admin_access_binding(
        self, response: resources.AdminAccessBinding
    ) -> resources.AdminAccessBinding:
        """Post-rpc interceptor for get_admin_access_binding

        DEPRECATED. Please use the `post_get_admin_access_binding_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the MarketingplatformAdminService server but before
        it is returned to user code. This `post_get_admin_access_binding` interceptor runs
        before the `post_get_admin_access_binding_with_metadata` interceptor.
        """
        return response

    def post_get_admin_access_binding_with_metadata(
        self,
        response: resources.AdminAccessBinding,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.AdminAccessBinding, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_admin_access_binding

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the MarketingplatformAdminService server but before it is returned to user code.

        We recommend only using this `post_get_admin_access_binding_with_metadata`
        interceptor in new development instead of the `post_get_admin_access_binding` interceptor.
        When both interceptors are used, this `post_get_admin_access_binding_with_metadata` interceptor runs after the
        `post_get_admin_access_binding` interceptor. The (possibly modified) response returned by
        `post_get_admin_access_binding` will be passed to
        `post_get_admin_access_binding_with_metadata`.
        """
        return response, metadata

    def pre_get_organization(
        self,
        request: marketingplatform_admin.GetOrganizationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        marketingplatform_admin.GetOrganizationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_organization

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MarketingplatformAdminService server.
        """
        return request, metadata

    def post_get_organization(
        self, response: resources.Organization
    ) -> resources.Organization:
        """Post-rpc interceptor for get_organization

        DEPRECATED. Please use the `post_get_organization_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the MarketingplatformAdminService server but before
        it is returned to user code. This `post_get_organization` interceptor runs
        before the `post_get_organization_with_metadata` interceptor.
        """
        return response

    def post_get_organization_with_metadata(
        self,
        response: resources.Organization,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.Organization, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_organization

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the MarketingplatformAdminService server but before it is returned to user code.

        We recommend only using this `post_get_organization_with_metadata`
        interceptor in new development instead of the `post_get_organization` interceptor.
        When both interceptors are used, this `post_get_organization_with_metadata` interceptor runs after the
        `post_get_organization` interceptor. The (possibly modified) response returned by
        `post_get_organization` will be passed to
        `post_get_organization_with_metadata`.
        """
        return response, metadata

    def pre_get_user_group(
        self,
        request: marketingplatform_admin.GetUserGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        marketingplatform_admin.GetUserGroupRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_user_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MarketingplatformAdminService server.
        """
        return request, metadata

    def post_get_user_group(self, response: resources.UserGroup) -> resources.UserGroup:
        """Post-rpc interceptor for get_user_group

        DEPRECATED. Please use the `post_get_user_group_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the MarketingplatformAdminService server but before
        it is returned to user code. This `post_get_user_group` interceptor runs
        before the `post_get_user_group_with_metadata` interceptor.
        """
        return response

    def post_get_user_group_with_metadata(
        self,
        response: resources.UserGroup,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.UserGroup, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_user_group

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the MarketingplatformAdminService server but before it is returned to user code.

        We recommend only using this `post_get_user_group_with_metadata`
        interceptor in new development instead of the `post_get_user_group` interceptor.
        When both interceptors are used, this `post_get_user_group_with_metadata` interceptor runs after the
        `post_get_user_group` interceptor. The (possibly modified) response returned by
        `post_get_user_group` will be passed to
        `post_get_user_group_with_metadata`.
        """
        return response, metadata

    def pre_get_user_group_member(
        self,
        request: marketingplatform_admin.GetUserGroupMemberRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        marketingplatform_admin.GetUserGroupMemberRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_user_group_member

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MarketingplatformAdminService server.
        """
        return request, metadata

    def post_get_user_group_member(
        self, response: resources.UserGroupMember
    ) -> resources.UserGroupMember:
        """Post-rpc interceptor for get_user_group_member

        DEPRECATED. Please use the `post_get_user_group_member_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the MarketingplatformAdminService server but before
        it is returned to user code. This `post_get_user_group_member` interceptor runs
        before the `post_get_user_group_member_with_metadata` interceptor.
        """
        return response

    def post_get_user_group_member_with_metadata(
        self,
        response: resources.UserGroupMember,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.UserGroupMember, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_user_group_member

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the MarketingplatformAdminService server but before it is returned to user code.

        We recommend only using this `post_get_user_group_member_with_metadata`
        interceptor in new development instead of the `post_get_user_group_member` interceptor.
        When both interceptors are used, this `post_get_user_group_member_with_metadata` interceptor runs after the
        `post_get_user_group_member` interceptor. The (possibly modified) response returned by
        `post_get_user_group_member` will be passed to
        `post_get_user_group_member_with_metadata`.
        """
        return response, metadata

    def pre_list_admin_access_bindings(
        self,
        request: marketingplatform_admin.ListAdminAccessBindingsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        marketingplatform_admin.ListAdminAccessBindingsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_admin_access_bindings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MarketingplatformAdminService server.
        """
        return request, metadata

    def post_list_admin_access_bindings(
        self, response: marketingplatform_admin.ListAdminAccessBindingsResponse
    ) -> marketingplatform_admin.ListAdminAccessBindingsResponse:
        """Post-rpc interceptor for list_admin_access_bindings

        DEPRECATED. Please use the `post_list_admin_access_bindings_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the MarketingplatformAdminService server but before
        it is returned to user code. This `post_list_admin_access_bindings` interceptor runs
        before the `post_list_admin_access_bindings_with_metadata` interceptor.
        """
        return response

    def post_list_admin_access_bindings_with_metadata(
        self,
        response: marketingplatform_admin.ListAdminAccessBindingsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        marketingplatform_admin.ListAdminAccessBindingsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_admin_access_bindings

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the MarketingplatformAdminService server but before it is returned to user code.

        We recommend only using this `post_list_admin_access_bindings_with_metadata`
        interceptor in new development instead of the `post_list_admin_access_bindings` interceptor.
        When both interceptors are used, this `post_list_admin_access_bindings_with_metadata` interceptor runs after the
        `post_list_admin_access_bindings` interceptor. The (possibly modified) response returned by
        `post_list_admin_access_bindings` will be passed to
        `post_list_admin_access_bindings_with_metadata`.
        """
        return response, metadata

    def pre_list_analytics_account_links(
        self,
        request: marketingplatform_admin.ListAnalyticsAccountLinksRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        marketingplatform_admin.ListAnalyticsAccountLinksRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_analytics_account_links

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MarketingplatformAdminService server.
        """
        return request, metadata

    def post_list_analytics_account_links(
        self, response: marketingplatform_admin.ListAnalyticsAccountLinksResponse
    ) -> marketingplatform_admin.ListAnalyticsAccountLinksResponse:
        """Post-rpc interceptor for list_analytics_account_links

        DEPRECATED. Please use the `post_list_analytics_account_links_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the MarketingplatformAdminService server but before
        it is returned to user code. This `post_list_analytics_account_links` interceptor runs
        before the `post_list_analytics_account_links_with_metadata` interceptor.
        """
        return response

    def post_list_analytics_account_links_with_metadata(
        self,
        response: marketingplatform_admin.ListAnalyticsAccountLinksResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        marketingplatform_admin.ListAnalyticsAccountLinksResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_analytics_account_links

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the MarketingplatformAdminService server but before it is returned to user code.

        We recommend only using this `post_list_analytics_account_links_with_metadata`
        interceptor in new development instead of the `post_list_analytics_account_links` interceptor.
        When both interceptors are used, this `post_list_analytics_account_links_with_metadata` interceptor runs after the
        `post_list_analytics_account_links` interceptor. The (possibly modified) response returned by
        `post_list_analytics_account_links` will be passed to
        `post_list_analytics_account_links_with_metadata`.
        """
        return response, metadata

    def pre_list_organizations(
        self,
        request: marketingplatform_admin.ListOrganizationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        marketingplatform_admin.ListOrganizationsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_organizations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MarketingplatformAdminService server.
        """
        return request, metadata

    def post_list_organizations(
        self, response: marketingplatform_admin.ListOrganizationsResponse
    ) -> marketingplatform_admin.ListOrganizationsResponse:
        """Post-rpc interceptor for list_organizations

        DEPRECATED. Please use the `post_list_organizations_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the MarketingplatformAdminService server but before
        it is returned to user code. This `post_list_organizations` interceptor runs
        before the `post_list_organizations_with_metadata` interceptor.
        """
        return response

    def post_list_organizations_with_metadata(
        self,
        response: marketingplatform_admin.ListOrganizationsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        marketingplatform_admin.ListOrganizationsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_organizations

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the MarketingplatformAdminService server but before it is returned to user code.

        We recommend only using this `post_list_organizations_with_metadata`
        interceptor in new development instead of the `post_list_organizations` interceptor.
        When both interceptors are used, this `post_list_organizations_with_metadata` interceptor runs after the
        `post_list_organizations` interceptor. The (possibly modified) response returned by
        `post_list_organizations` will be passed to
        `post_list_organizations_with_metadata`.
        """
        return response, metadata

    def pre_list_user_group_members(
        self,
        request: marketingplatform_admin.ListUserGroupMembersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        marketingplatform_admin.ListUserGroupMembersRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_user_group_members

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MarketingplatformAdminService server.
        """
        return request, metadata

    def post_list_user_group_members(
        self, response: marketingplatform_admin.ListUserGroupMembersResponse
    ) -> marketingplatform_admin.ListUserGroupMembersResponse:
        """Post-rpc interceptor for list_user_group_members

        DEPRECATED. Please use the `post_list_user_group_members_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the MarketingplatformAdminService server but before
        it is returned to user code. This `post_list_user_group_members` interceptor runs
        before the `post_list_user_group_members_with_metadata` interceptor.
        """
        return response

    def post_list_user_group_members_with_metadata(
        self,
        response: marketingplatform_admin.ListUserGroupMembersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        marketingplatform_admin.ListUserGroupMembersResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_user_group_members

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the MarketingplatformAdminService server but before it is returned to user code.

        We recommend only using this `post_list_user_group_members_with_metadata`
        interceptor in new development instead of the `post_list_user_group_members` interceptor.
        When both interceptors are used, this `post_list_user_group_members_with_metadata` interceptor runs after the
        `post_list_user_group_members` interceptor. The (possibly modified) response returned by
        `post_list_user_group_members` will be passed to
        `post_list_user_group_members_with_metadata`.
        """
        return response, metadata

    def pre_list_user_groups(
        self,
        request: marketingplatform_admin.ListUserGroupsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        marketingplatform_admin.ListUserGroupsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_user_groups

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MarketingplatformAdminService server.
        """
        return request, metadata

    def post_list_user_groups(
        self, response: marketingplatform_admin.ListUserGroupsResponse
    ) -> marketingplatform_admin.ListUserGroupsResponse:
        """Post-rpc interceptor for list_user_groups

        DEPRECATED. Please use the `post_list_user_groups_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the MarketingplatformAdminService server but before
        it is returned to user code. This `post_list_user_groups` interceptor runs
        before the `post_list_user_groups_with_metadata` interceptor.
        """
        return response

    def post_list_user_groups_with_metadata(
        self,
        response: marketingplatform_admin.ListUserGroupsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        marketingplatform_admin.ListUserGroupsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_user_groups

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the MarketingplatformAdminService server but before it is returned to user code.

        We recommend only using this `post_list_user_groups_with_metadata`
        interceptor in new development instead of the `post_list_user_groups` interceptor.
        When both interceptors are used, this `post_list_user_groups_with_metadata` interceptor runs after the
        `post_list_user_groups` interceptor. The (possibly modified) response returned by
        `post_list_user_groups` will be passed to
        `post_list_user_groups_with_metadata`.
        """
        return response, metadata

    def pre_report_property_usage(
        self,
        request: marketingplatform_admin.ReportPropertyUsageRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        marketingplatform_admin.ReportPropertyUsageRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for report_property_usage

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MarketingplatformAdminService server.
        """
        return request, metadata

    def post_report_property_usage(
        self, response: marketingplatform_admin.ReportPropertyUsageResponse
    ) -> marketingplatform_admin.ReportPropertyUsageResponse:
        """Post-rpc interceptor for report_property_usage

        DEPRECATED. Please use the `post_report_property_usage_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the MarketingplatformAdminService server but before
        it is returned to user code. This `post_report_property_usage` interceptor runs
        before the `post_report_property_usage_with_metadata` interceptor.
        """
        return response

    def post_report_property_usage_with_metadata(
        self,
        response: marketingplatform_admin.ReportPropertyUsageResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        marketingplatform_admin.ReportPropertyUsageResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for report_property_usage

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the MarketingplatformAdminService server but before it is returned to user code.

        We recommend only using this `post_report_property_usage_with_metadata`
        interceptor in new development instead of the `post_report_property_usage` interceptor.
        When both interceptors are used, this `post_report_property_usage_with_metadata` interceptor runs after the
        `post_report_property_usage` interceptor. The (possibly modified) response returned by
        `post_report_property_usage` will be passed to
        `post_report_property_usage_with_metadata`.
        """
        return response, metadata

    def pre_set_property_service_level(
        self,
        request: marketingplatform_admin.SetPropertyServiceLevelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        marketingplatform_admin.SetPropertyServiceLevelRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for set_property_service_level

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MarketingplatformAdminService server.
        """
        return request, metadata

    def post_set_property_service_level(
        self, response: marketingplatform_admin.SetPropertyServiceLevelResponse
    ) -> marketingplatform_admin.SetPropertyServiceLevelResponse:
        """Post-rpc interceptor for set_property_service_level

        DEPRECATED. Please use the `post_set_property_service_level_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the MarketingplatformAdminService server but before
        it is returned to user code. This `post_set_property_service_level` interceptor runs
        before the `post_set_property_service_level_with_metadata` interceptor.
        """
        return response

    def post_set_property_service_level_with_metadata(
        self,
        response: marketingplatform_admin.SetPropertyServiceLevelResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        marketingplatform_admin.SetPropertyServiceLevelResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for set_property_service_level

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the MarketingplatformAdminService server but before it is returned to user code.

        We recommend only using this `post_set_property_service_level_with_metadata`
        interceptor in new development instead of the `post_set_property_service_level` interceptor.
        When both interceptors are used, this `post_set_property_service_level_with_metadata` interceptor runs after the
        `post_set_property_service_level` interceptor. The (possibly modified) response returned by
        `post_set_property_service_level` will be passed to
        `post_set_property_service_level_with_metadata`.
        """
        return response, metadata

    def pre_update_admin_access_binding(
        self,
        request: marketingplatform_admin.UpdateAdminAccessBindingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        marketingplatform_admin.UpdateAdminAccessBindingRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_admin_access_binding

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MarketingplatformAdminService server.
        """
        return request, metadata

    def post_update_admin_access_binding(
        self, response: resources.AdminAccessBinding
    ) -> resources.AdminAccessBinding:
        """Post-rpc interceptor for update_admin_access_binding

        DEPRECATED. Please use the `post_update_admin_access_binding_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the MarketingplatformAdminService server but before
        it is returned to user code. This `post_update_admin_access_binding` interceptor runs
        before the `post_update_admin_access_binding_with_metadata` interceptor.
        """
        return response

    def post_update_admin_access_binding_with_metadata(
        self,
        response: resources.AdminAccessBinding,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.AdminAccessBinding, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_admin_access_binding

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the MarketingplatformAdminService server but before it is returned to user code.

        We recommend only using this `post_update_admin_access_binding_with_metadata`
        interceptor in new development instead of the `post_update_admin_access_binding` interceptor.
        When both interceptors are used, this `post_update_admin_access_binding_with_metadata` interceptor runs after the
        `post_update_admin_access_binding` interceptor. The (possibly modified) response returned by
        `post_update_admin_access_binding` will be passed to
        `post_update_admin_access_binding_with_metadata`.
        """
        return response, metadata

    def pre_update_user_group(
        self,
        request: marketingplatform_admin.UpdateUserGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        marketingplatform_admin.UpdateUserGroupRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_user_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MarketingplatformAdminService server.
        """
        return request, metadata

    def post_update_user_group(
        self, response: resources.UserGroup
    ) -> resources.UserGroup:
        """Post-rpc interceptor for update_user_group

        DEPRECATED. Please use the `post_update_user_group_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the MarketingplatformAdminService server but before
        it is returned to user code. This `post_update_user_group` interceptor runs
        before the `post_update_user_group_with_metadata` interceptor.
        """
        return response

    def post_update_user_group_with_metadata(
        self,
        response: resources.UserGroup,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.UserGroup, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_user_group

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the MarketingplatformAdminService server but before it is returned to user code.

        We recommend only using this `post_update_user_group_with_metadata`
        interceptor in new development instead of the `post_update_user_group` interceptor.
        When both interceptors are used, this `post_update_user_group_with_metadata` interceptor runs after the
        `post_update_user_group` interceptor. The (possibly modified) response returned by
        `post_update_user_group` will be passed to
        `post_update_user_group_with_metadata`.
        """
        return response, metadata

    def pre_update_user_group_member(
        self,
        request: marketingplatform_admin.UpdateUserGroupMemberRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        marketingplatform_admin.UpdateUserGroupMemberRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_user_group_member

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MarketingplatformAdminService server.
        """
        return request, metadata

    def post_update_user_group_member(
        self, response: resources.UserGroupMember
    ) -> resources.UserGroupMember:
        """Post-rpc interceptor for update_user_group_member

        DEPRECATED. Please use the `post_update_user_group_member_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the MarketingplatformAdminService server but before
        it is returned to user code. This `post_update_user_group_member` interceptor runs
        before the `post_update_user_group_member_with_metadata` interceptor.
        """
        return response

    def post_update_user_group_member_with_metadata(
        self,
        response: resources.UserGroupMember,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.UserGroupMember, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_user_group_member

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the MarketingplatformAdminService server but before it is returned to user code.

        We recommend only using this `post_update_user_group_member_with_metadata`
        interceptor in new development instead of the `post_update_user_group_member` interceptor.
        When both interceptors are used, this `post_update_user_group_member_with_metadata` interceptor runs after the
        `post_update_user_group_member` interceptor. The (possibly modified) response returned by
        `post_update_user_group_member` will be passed to
        `post_update_user_group_member_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class MarketingplatformAdminServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: MarketingplatformAdminServiceRestInterceptor


class MarketingplatformAdminServiceRestTransport(
    _BaseMarketingplatformAdminServiceRestTransport
):
    """REST backend synchronous transport for MarketingplatformAdminService.

    Service Interface for the Google Marketing Platform Admin
    API.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "marketingplatformadmin.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[MarketingplatformAdminServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
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
                This argument is ignored if ``channel`` is provided. This argument will be
                removed in the next major version of this library.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Callable[[], Tuple[bytes, bytes]]): Client
                certificate to configure mutual TLS HTTP channel. It is ignored
                if ``channel`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you are developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
            url_scheme: the protocol scheme for the API endpoint.  Normally
                "https", but for testing or local servers,
                "http" can be specified.
            interceptor (Optional[MarketingplatformAdminServiceRestInterceptor]): Interceptor used
                to manipulate requests, request metadata, and responses.
            api_audience (Optional[str]): The intended audience for the API calls
                to the service that will be set when using certain 3rd party
                authentication flows. Audience is typically a resource identifier.
                If not set, the host value will be used as a default.
        """
        # Run the base constructor
        # TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.
        # TODO: When custom host (api_endpoint) is set, `scopes` must *also* be set on the
        # credentials object
        super().__init__(
            host=host,
            credentials=credentials,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            url_scheme=url_scheme,
            api_audience=api_audience,
        )
        self._session = AuthorizedSession(
            self._credentials, default_host=self.DEFAULT_HOST
        )
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = (
            interceptor or MarketingplatformAdminServiceRestInterceptor()
        )
        self._prep_wrapped_messages(client_info)

    class _CreateAdminAccessBinding(
        _BaseMarketingplatformAdminServiceRestTransport._BaseCreateAdminAccessBinding,
        MarketingplatformAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "MarketingplatformAdminServiceRestTransport.CreateAdminAccessBinding"
            )

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: marketingplatform_admin.CreateAdminAccessBindingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.AdminAccessBinding:
            r"""Call the create admin access
            binding method over HTTP.

                Args:
                    request (~.marketingplatform_admin.CreateAdminAccessBindingRequest):
                        The request object. Request message for
                    CreateAdminAccessBinding RPC.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.resources.AdminAccessBinding:
                        A resource message representing a
                    binding to a set of roles.

            """

            http_options = _BaseMarketingplatformAdminServiceRestTransport._BaseCreateAdminAccessBinding._get_http_options()
            request, metadata = self._interceptor.pre_create_admin_access_binding(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMarketingplatformAdminServiceRestTransport._BaseCreateAdminAccessBinding,
                    "_BaseCreateAdminAccessBinding__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.marketingplatform.admin_v1alpha.MarketingplatformAdminServiceClient.CreateAdminAccessBinding",
                    extra={
                        "serviceName": "google.marketingplatform.admin.v1alpha.MarketingplatformAdminService",
                        "rpcName": "CreateAdminAccessBinding",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MarketingplatformAdminServiceRestTransport._CreateAdminAccessBinding._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = resources.AdminAccessBinding()
            pb_resp = resources.AdminAccessBinding.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_admin_access_binding(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_admin_access_binding_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.AdminAccessBinding.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.marketingplatform.admin_v1alpha.MarketingplatformAdminServiceClient.create_admin_access_binding",
                    extra={
                        "serviceName": "google.marketingplatform.admin.v1alpha.MarketingplatformAdminService",
                        "rpcName": "CreateAdminAccessBinding",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateAnalyticsAccountLink(
        _BaseMarketingplatformAdminServiceRestTransport._BaseCreateAnalyticsAccountLink,
        MarketingplatformAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "MarketingplatformAdminServiceRestTransport.CreateAnalyticsAccountLink"
            )

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: marketingplatform_admin.CreateAnalyticsAccountLinkRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.AnalyticsAccountLink:
            r"""Call the create analytics account
            link method over HTTP.

                Args:
                    request (~.marketingplatform_admin.CreateAnalyticsAccountLinkRequest):
                        The request object. Request message for
                    CreateAnalyticsAccountLink RPC.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.resources.AnalyticsAccountLink:
                        A resource message representing the
                    link between a Google Analytics account
                    and a Google Marketing Platform
                    organization.

            """

            http_options = _BaseMarketingplatformAdminServiceRestTransport._BaseCreateAnalyticsAccountLink._get_http_options()
            request, metadata = self._interceptor.pre_create_analytics_account_link(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMarketingplatformAdminServiceRestTransport._BaseCreateAnalyticsAccountLink,
                    "_BaseCreateAnalyticsAccountLink__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.marketingplatform.admin_v1alpha.MarketingplatformAdminServiceClient.CreateAnalyticsAccountLink",
                    extra={
                        "serviceName": "google.marketingplatform.admin.v1alpha.MarketingplatformAdminService",
                        "rpcName": "CreateAnalyticsAccountLink",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MarketingplatformAdminServiceRestTransport._CreateAnalyticsAccountLink._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = resources.AnalyticsAccountLink()
            pb_resp = resources.AnalyticsAccountLink.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_analytics_account_link(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_create_analytics_account_link_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.AnalyticsAccountLink.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.marketingplatform.admin_v1alpha.MarketingplatformAdminServiceClient.create_analytics_account_link",
                    extra={
                        "serviceName": "google.marketingplatform.admin.v1alpha.MarketingplatformAdminService",
                        "rpcName": "CreateAnalyticsAccountLink",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateUserGroup(
        _BaseMarketingplatformAdminServiceRestTransport._BaseCreateUserGroup,
        MarketingplatformAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("MarketingplatformAdminServiceRestTransport.CreateUserGroup")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: marketingplatform_admin.CreateUserGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.UserGroup:
            r"""Call the create user group method over HTTP.

            Args:
                request (~.marketingplatform_admin.CreateUserGroupRequest):
                    The request object. Request message for CreateUserGroup
                RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.UserGroup:
                    A resource message representing a
                user group in a GMP organization.

            """

            http_options = _BaseMarketingplatformAdminServiceRestTransport._BaseCreateUserGroup._get_http_options()
            request, metadata = self._interceptor.pre_create_user_group(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMarketingplatformAdminServiceRestTransport._BaseCreateUserGroup,
                    "_BaseCreateUserGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.marketingplatform.admin_v1alpha.MarketingplatformAdminServiceClient.CreateUserGroup",
                    extra={
                        "serviceName": "google.marketingplatform.admin.v1alpha.MarketingplatformAdminService",
                        "rpcName": "CreateUserGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MarketingplatformAdminServiceRestTransport._CreateUserGroup._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = resources.UserGroup()
            pb_resp = resources.UserGroup.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_user_group(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_user_group_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.UserGroup.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.marketingplatform.admin_v1alpha.MarketingplatformAdminServiceClient.create_user_group",
                    extra={
                        "serviceName": "google.marketingplatform.admin.v1alpha.MarketingplatformAdminService",
                        "rpcName": "CreateUserGroup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateUserGroupMember(
        _BaseMarketingplatformAdminServiceRestTransport._BaseCreateUserGroupMember,
        MarketingplatformAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "MarketingplatformAdminServiceRestTransport.CreateUserGroupMember"
            )

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: marketingplatform_admin.CreateUserGroupMemberRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.UserGroupMember:
            r"""Call the create user group member method over HTTP.

            Args:
                request (~.marketingplatform_admin.CreateUserGroupMemberRequest):
                    The request object. Request message for
                CreateUserGroupMember RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.UserGroupMember:
                    A resource message representing a
                member of a user group.

            """

            http_options = _BaseMarketingplatformAdminServiceRestTransport._BaseCreateUserGroupMember._get_http_options()
            request, metadata = self._interceptor.pre_create_user_group_member(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMarketingplatformAdminServiceRestTransport._BaseCreateUserGroupMember,
                    "_BaseCreateUserGroupMember__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.marketingplatform.admin_v1alpha.MarketingplatformAdminServiceClient.CreateUserGroupMember",
                    extra={
                        "serviceName": "google.marketingplatform.admin.v1alpha.MarketingplatformAdminService",
                        "rpcName": "CreateUserGroupMember",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MarketingplatformAdminServiceRestTransport._CreateUserGroupMember._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = resources.UserGroupMember()
            pb_resp = resources.UserGroupMember.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_user_group_member(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_user_group_member_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.UserGroupMember.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.marketingplatform.admin_v1alpha.MarketingplatformAdminServiceClient.create_user_group_member",
                    extra={
                        "serviceName": "google.marketingplatform.admin.v1alpha.MarketingplatformAdminService",
                        "rpcName": "CreateUserGroupMember",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteAnalyticsAccountLink(
        _BaseMarketingplatformAdminServiceRestTransport._BaseDeleteAnalyticsAccountLink,
        MarketingplatformAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "MarketingplatformAdminServiceRestTransport.DeleteAnalyticsAccountLink"
            )

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: marketingplatform_admin.DeleteAnalyticsAccountLinkRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete analytics account
            link method over HTTP.

                Args:
                    request (~.marketingplatform_admin.DeleteAnalyticsAccountLinkRequest):
                        The request object. Request message for
                    DeleteAnalyticsAccountLink RPC.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.
            """

            http_options = _BaseMarketingplatformAdminServiceRestTransport._BaseDeleteAnalyticsAccountLink._get_http_options()
            request, metadata = self._interceptor.pre_delete_analytics_account_link(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMarketingplatformAdminServiceRestTransport._BaseDeleteAnalyticsAccountLink,
                    "_BaseDeleteAnalyticsAccountLink__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.marketingplatform.admin_v1alpha.MarketingplatformAdminServiceClient.DeleteAnalyticsAccountLink",
                    extra={
                        "serviceName": "google.marketingplatform.admin.v1alpha.MarketingplatformAdminService",
                        "rpcName": "DeleteAnalyticsAccountLink",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MarketingplatformAdminServiceRestTransport._DeleteAnalyticsAccountLink._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

    class _DeleteUserGroup(
        _BaseMarketingplatformAdminServiceRestTransport._BaseDeleteUserGroup,
        MarketingplatformAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("MarketingplatformAdminServiceRestTransport.DeleteUserGroup")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: marketingplatform_admin.DeleteUserGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete user group method over HTTP.

            Args:
                request (~.marketingplatform_admin.DeleteUserGroupRequest):
                    The request object. Request message for DeleteUserGroup
                RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseMarketingplatformAdminServiceRestTransport._BaseDeleteUserGroup._get_http_options()
            request, metadata = self._interceptor.pre_delete_user_group(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMarketingplatformAdminServiceRestTransport._BaseDeleteUserGroup,
                    "_BaseDeleteUserGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.marketingplatform.admin_v1alpha.MarketingplatformAdminServiceClient.DeleteUserGroup",
                    extra={
                        "serviceName": "google.marketingplatform.admin.v1alpha.MarketingplatformAdminService",
                        "rpcName": "DeleteUserGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MarketingplatformAdminServiceRestTransport._DeleteUserGroup._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

    class _DeleteUserGroupMember(
        _BaseMarketingplatformAdminServiceRestTransport._BaseDeleteUserGroupMember,
        MarketingplatformAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "MarketingplatformAdminServiceRestTransport.DeleteUserGroupMember"
            )

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: marketingplatform_admin.DeleteUserGroupMemberRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete user group member method over HTTP.

            Args:
                request (~.marketingplatform_admin.DeleteUserGroupMemberRequest):
                    The request object. Request message for
                DeleteUserGroupMember RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseMarketingplatformAdminServiceRestTransport._BaseDeleteUserGroupMember._get_http_options()
            request, metadata = self._interceptor.pre_delete_user_group_member(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMarketingplatformAdminServiceRestTransport._BaseDeleteUserGroupMember,
                    "_BaseDeleteUserGroupMember__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.marketingplatform.admin_v1alpha.MarketingplatformAdminServiceClient.DeleteUserGroupMember",
                    extra={
                        "serviceName": "google.marketingplatform.admin.v1alpha.MarketingplatformAdminService",
                        "rpcName": "DeleteUserGroupMember",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MarketingplatformAdminServiceRestTransport._DeleteUserGroupMember._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

    class _FindSalesPartnerManagedClients(
        _BaseMarketingplatformAdminServiceRestTransport._BaseFindSalesPartnerManagedClients,
        MarketingplatformAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "MarketingplatformAdminServiceRestTransport.FindSalesPartnerManagedClients"
            )

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: marketingplatform_admin.FindSalesPartnerManagedClientsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> marketingplatform_admin.FindSalesPartnerManagedClientsResponse:
            r"""Call the find sales partner
            managed clients method over HTTP.

                Args:
                    request (~.marketingplatform_admin.FindSalesPartnerManagedClientsRequest):
                        The request object. Request message for
                    FindSalesPartnerManagedClients RPC.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.marketingplatform_admin.FindSalesPartnerManagedClientsResponse:
                        Response message for
                    FindSalesPartnerManagedClients RPC.

            """

            http_options = _BaseMarketingplatformAdminServiceRestTransport._BaseFindSalesPartnerManagedClients._get_http_options()
            request, metadata = (
                self._interceptor.pre_find_sales_partner_managed_clients(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMarketingplatformAdminServiceRestTransport._BaseFindSalesPartnerManagedClients,
                    "_BaseFindSalesPartnerManagedClients__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.marketingplatform.admin_v1alpha.MarketingplatformAdminServiceClient.FindSalesPartnerManagedClients",
                    extra={
                        "serviceName": "google.marketingplatform.admin.v1alpha.MarketingplatformAdminService",
                        "rpcName": "FindSalesPartnerManagedClients",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MarketingplatformAdminServiceRestTransport._FindSalesPartnerManagedClients._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = marketingplatform_admin.FindSalesPartnerManagedClientsResponse()
            pb_resp = marketingplatform_admin.FindSalesPartnerManagedClientsResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_find_sales_partner_managed_clients(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_find_sales_partner_managed_clients_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = marketingplatform_admin.FindSalesPartnerManagedClientsResponse.to_json(
                        response
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.marketingplatform.admin_v1alpha.MarketingplatformAdminServiceClient.find_sales_partner_managed_clients",
                    extra={
                        "serviceName": "google.marketingplatform.admin.v1alpha.MarketingplatformAdminService",
                        "rpcName": "FindSalesPartnerManagedClients",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetAdminAccessBinding(
        _BaseMarketingplatformAdminServiceRestTransport._BaseGetAdminAccessBinding,
        MarketingplatformAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "MarketingplatformAdminServiceRestTransport.GetAdminAccessBinding"
            )

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: marketingplatform_admin.GetAdminAccessBindingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.AdminAccessBinding:
            r"""Call the get admin access binding method over HTTP.

            Args:
                request (~.marketingplatform_admin.GetAdminAccessBindingRequest):
                    The request object. Response message for
                GetAdminAccessBinding RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.AdminAccessBinding:
                    A resource message representing a
                binding to a set of roles.

            """

            http_options = _BaseMarketingplatformAdminServiceRestTransport._BaseGetAdminAccessBinding._get_http_options()
            request, metadata = self._interceptor.pre_get_admin_access_binding(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMarketingplatformAdminServiceRestTransport._BaseGetAdminAccessBinding,
                    "_BaseGetAdminAccessBinding__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.marketingplatform.admin_v1alpha.MarketingplatformAdminServiceClient.GetAdminAccessBinding",
                    extra={
                        "serviceName": "google.marketingplatform.admin.v1alpha.MarketingplatformAdminService",
                        "rpcName": "GetAdminAccessBinding",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MarketingplatformAdminServiceRestTransport._GetAdminAccessBinding._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = resources.AdminAccessBinding()
            pb_resp = resources.AdminAccessBinding.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_admin_access_binding(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_admin_access_binding_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.AdminAccessBinding.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.marketingplatform.admin_v1alpha.MarketingplatformAdminServiceClient.get_admin_access_binding",
                    extra={
                        "serviceName": "google.marketingplatform.admin.v1alpha.MarketingplatformAdminService",
                        "rpcName": "GetAdminAccessBinding",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetOrganization(
        _BaseMarketingplatformAdminServiceRestTransport._BaseGetOrganization,
        MarketingplatformAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("MarketingplatformAdminServiceRestTransport.GetOrganization")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: marketingplatform_admin.GetOrganizationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.Organization:
            r"""Call the get organization method over HTTP.

            Args:
                request (~.marketingplatform_admin.GetOrganizationRequest):
                    The request object. Request message for GetOrganization
                RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.Organization:
                    A resource message representing a
                Google Marketing Platform organization.

            """

            http_options = _BaseMarketingplatformAdminServiceRestTransport._BaseGetOrganization._get_http_options()
            request, metadata = self._interceptor.pre_get_organization(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMarketingplatformAdminServiceRestTransport._BaseGetOrganization,
                    "_BaseGetOrganization__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.marketingplatform.admin_v1alpha.MarketingplatformAdminServiceClient.GetOrganization",
                    extra={
                        "serviceName": "google.marketingplatform.admin.v1alpha.MarketingplatformAdminService",
                        "rpcName": "GetOrganization",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MarketingplatformAdminServiceRestTransport._GetOrganization._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = resources.Organization()
            pb_resp = resources.Organization.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_organization(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_organization_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.Organization.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.marketingplatform.admin_v1alpha.MarketingplatformAdminServiceClient.get_organization",
                    extra={
                        "serviceName": "google.marketingplatform.admin.v1alpha.MarketingplatformAdminService",
                        "rpcName": "GetOrganization",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetUserGroup(
        _BaseMarketingplatformAdminServiceRestTransport._BaseGetUserGroup,
        MarketingplatformAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("MarketingplatformAdminServiceRestTransport.GetUserGroup")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: marketingplatform_admin.GetUserGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.UserGroup:
            r"""Call the get user group method over HTTP.

            Args:
                request (~.marketingplatform_admin.GetUserGroupRequest):
                    The request object. Request message for GetUserGroup RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.UserGroup:
                    A resource message representing a
                user group in a GMP organization.

            """

            http_options = _BaseMarketingplatformAdminServiceRestTransport._BaseGetUserGroup._get_http_options()
            request, metadata = self._interceptor.pre_get_user_group(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMarketingplatformAdminServiceRestTransport._BaseGetUserGroup,
                    "_BaseGetUserGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.marketingplatform.admin_v1alpha.MarketingplatformAdminServiceClient.GetUserGroup",
                    extra={
                        "serviceName": "google.marketingplatform.admin.v1alpha.MarketingplatformAdminService",
                        "rpcName": "GetUserGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                MarketingplatformAdminServiceRestTransport._GetUserGroup._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = resources.UserGroup()
            pb_resp = resources.UserGroup.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_user_group(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_user_group_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.UserGroup.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.marketingplatform.admin_v1alpha.MarketingplatformAdminServiceClient.get_user_group",
                    extra={
                        "serviceName": "google.marketingplatform.admin.v1alpha.MarketingplatformAdminService",
                        "rpcName": "GetUserGroup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetUserGroupMember(
        _BaseMarketingplatformAdminServiceRestTransport._BaseGetUserGroupMember,
        MarketingplatformAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("MarketingplatformAdminServiceRestTransport.GetUserGroupMember")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: marketingplatform_admin.GetUserGroupMemberRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.UserGroupMember:
            r"""Call the get user group member method over HTTP.

            Args:
                request (~.marketingplatform_admin.GetUserGroupMemberRequest):
                    The request object. Request message for
                GetUserGroupMember RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.UserGroupMember:
                    A resource message representing a
                member of a user group.

            """

            http_options = _BaseMarketingplatformAdminServiceRestTransport._BaseGetUserGroupMember._get_http_options()
            request, metadata = self._interceptor.pre_get_user_group_member(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMarketingplatformAdminServiceRestTransport._BaseGetUserGroupMember,
                    "_BaseGetUserGroupMember__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.marketingplatform.admin_v1alpha.MarketingplatformAdminServiceClient.GetUserGroupMember",
                    extra={
                        "serviceName": "google.marketingplatform.admin.v1alpha.MarketingplatformAdminService",
                        "rpcName": "GetUserGroupMember",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MarketingplatformAdminServiceRestTransport._GetUserGroupMember._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = resources.UserGroupMember()
            pb_resp = resources.UserGroupMember.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_user_group_member(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_user_group_member_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.UserGroupMember.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.marketingplatform.admin_v1alpha.MarketingplatformAdminServiceClient.get_user_group_member",
                    extra={
                        "serviceName": "google.marketingplatform.admin.v1alpha.MarketingplatformAdminService",
                        "rpcName": "GetUserGroupMember",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListAdminAccessBindings(
        _BaseMarketingplatformAdminServiceRestTransport._BaseListAdminAccessBindings,
        MarketingplatformAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "MarketingplatformAdminServiceRestTransport.ListAdminAccessBindings"
            )

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: marketingplatform_admin.ListAdminAccessBindingsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> marketingplatform_admin.ListAdminAccessBindingsResponse:
            r"""Call the list admin access
            bindings method over HTTP.

                Args:
                    request (~.marketingplatform_admin.ListAdminAccessBindingsRequest):
                        The request object. Request message for
                    ListAdminAccessBindings RPC.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.marketingplatform_admin.ListAdminAccessBindingsResponse:
                        Response message for
                    ListAdminAccessBindings RPC.

            """

            http_options = _BaseMarketingplatformAdminServiceRestTransport._BaseListAdminAccessBindings._get_http_options()
            request, metadata = self._interceptor.pre_list_admin_access_bindings(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMarketingplatformAdminServiceRestTransport._BaseListAdminAccessBindings,
                    "_BaseListAdminAccessBindings__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.marketingplatform.admin_v1alpha.MarketingplatformAdminServiceClient.ListAdminAccessBindings",
                    extra={
                        "serviceName": "google.marketingplatform.admin.v1alpha.MarketingplatformAdminService",
                        "rpcName": "ListAdminAccessBindings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MarketingplatformAdminServiceRestTransport._ListAdminAccessBindings._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = marketingplatform_admin.ListAdminAccessBindingsResponse()
            pb_resp = marketingplatform_admin.ListAdminAccessBindingsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_admin_access_bindings(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_admin_access_bindings_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        marketingplatform_admin.ListAdminAccessBindingsResponse.to_json(
                            response
                        )
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.marketingplatform.admin_v1alpha.MarketingplatformAdminServiceClient.list_admin_access_bindings",
                    extra={
                        "serviceName": "google.marketingplatform.admin.v1alpha.MarketingplatformAdminService",
                        "rpcName": "ListAdminAccessBindings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListAnalyticsAccountLinks(
        _BaseMarketingplatformAdminServiceRestTransport._BaseListAnalyticsAccountLinks,
        MarketingplatformAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "MarketingplatformAdminServiceRestTransport.ListAnalyticsAccountLinks"
            )

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: marketingplatform_admin.ListAnalyticsAccountLinksRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> marketingplatform_admin.ListAnalyticsAccountLinksResponse:
            r"""Call the list analytics account
            links method over HTTP.

                Args:
                    request (~.marketingplatform_admin.ListAnalyticsAccountLinksRequest):
                        The request object. Request message for
                    ListAnalyticsAccountLinks RPC.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.marketingplatform_admin.ListAnalyticsAccountLinksResponse:
                        Response message for
                    ListAnalyticsAccountLinks RPC.

            """

            http_options = _BaseMarketingplatformAdminServiceRestTransport._BaseListAnalyticsAccountLinks._get_http_options()
            request, metadata = self._interceptor.pre_list_analytics_account_links(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMarketingplatformAdminServiceRestTransport._BaseListAnalyticsAccountLinks,
                    "_BaseListAnalyticsAccountLinks__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.marketingplatform.admin_v1alpha.MarketingplatformAdminServiceClient.ListAnalyticsAccountLinks",
                    extra={
                        "serviceName": "google.marketingplatform.admin.v1alpha.MarketingplatformAdminService",
                        "rpcName": "ListAnalyticsAccountLinks",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MarketingplatformAdminServiceRestTransport._ListAnalyticsAccountLinks._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = marketingplatform_admin.ListAnalyticsAccountLinksResponse()
            pb_resp = marketingplatform_admin.ListAnalyticsAccountLinksResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_analytics_account_links(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_analytics_account_links_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = marketingplatform_admin.ListAnalyticsAccountLinksResponse.to_json(
                        response
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.marketingplatform.admin_v1alpha.MarketingplatformAdminServiceClient.list_analytics_account_links",
                    extra={
                        "serviceName": "google.marketingplatform.admin.v1alpha.MarketingplatformAdminService",
                        "rpcName": "ListAnalyticsAccountLinks",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListOrganizations(
        _BaseMarketingplatformAdminServiceRestTransport._BaseListOrganizations,
        MarketingplatformAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("MarketingplatformAdminServiceRestTransport.ListOrganizations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: marketingplatform_admin.ListOrganizationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> marketingplatform_admin.ListOrganizationsResponse:
            r"""Call the list organizations method over HTTP.

            Args:
                request (~.marketingplatform_admin.ListOrganizationsRequest):
                    The request object. Request message for ListOrganizations
                RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.marketingplatform_admin.ListOrganizationsResponse:
                    Response message for
                ListOrganizations RPC.

            """

            http_options = _BaseMarketingplatformAdminServiceRestTransport._BaseListOrganizations._get_http_options()
            request, metadata = self._interceptor.pre_list_organizations(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMarketingplatformAdminServiceRestTransport._BaseListOrganizations,
                    "_BaseListOrganizations__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.marketingplatform.admin_v1alpha.MarketingplatformAdminServiceClient.ListOrganizations",
                    extra={
                        "serviceName": "google.marketingplatform.admin.v1alpha.MarketingplatformAdminService",
                        "rpcName": "ListOrganizations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MarketingplatformAdminServiceRestTransport._ListOrganizations._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = marketingplatform_admin.ListOrganizationsResponse()
            pb_resp = marketingplatform_admin.ListOrganizationsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_organizations(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_organizations_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        marketingplatform_admin.ListOrganizationsResponse.to_json(
                            response
                        )
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.marketingplatform.admin_v1alpha.MarketingplatformAdminServiceClient.list_organizations",
                    extra={
                        "serviceName": "google.marketingplatform.admin.v1alpha.MarketingplatformAdminService",
                        "rpcName": "ListOrganizations",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListUserGroupMembers(
        _BaseMarketingplatformAdminServiceRestTransport._BaseListUserGroupMembers,
        MarketingplatformAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "MarketingplatformAdminServiceRestTransport.ListUserGroupMembers"
            )

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: marketingplatform_admin.ListUserGroupMembersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> marketingplatform_admin.ListUserGroupMembersResponse:
            r"""Call the list user group members method over HTTP.

            Args:
                request (~.marketingplatform_admin.ListUserGroupMembersRequest):
                    The request object. Request message for
                ListUserGroupMembers RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.marketingplatform_admin.ListUserGroupMembersResponse:
                    Response message for
                ListUserGroupMembers RPC.

            """

            http_options = _BaseMarketingplatformAdminServiceRestTransport._BaseListUserGroupMembers._get_http_options()
            request, metadata = self._interceptor.pre_list_user_group_members(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMarketingplatformAdminServiceRestTransport._BaseListUserGroupMembers,
                    "_BaseListUserGroupMembers__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.marketingplatform.admin_v1alpha.MarketingplatformAdminServiceClient.ListUserGroupMembers",
                    extra={
                        "serviceName": "google.marketingplatform.admin.v1alpha.MarketingplatformAdminService",
                        "rpcName": "ListUserGroupMembers",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MarketingplatformAdminServiceRestTransport._ListUserGroupMembers._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = marketingplatform_admin.ListUserGroupMembersResponse()
            pb_resp = marketingplatform_admin.ListUserGroupMembersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_user_group_members(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_user_group_members_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        marketingplatform_admin.ListUserGroupMembersResponse.to_json(
                            response
                        )
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.marketingplatform.admin_v1alpha.MarketingplatformAdminServiceClient.list_user_group_members",
                    extra={
                        "serviceName": "google.marketingplatform.admin.v1alpha.MarketingplatformAdminService",
                        "rpcName": "ListUserGroupMembers",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListUserGroups(
        _BaseMarketingplatformAdminServiceRestTransport._BaseListUserGroups,
        MarketingplatformAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("MarketingplatformAdminServiceRestTransport.ListUserGroups")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: marketingplatform_admin.ListUserGroupsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> marketingplatform_admin.ListUserGroupsResponse:
            r"""Call the list user groups method over HTTP.

            Args:
                request (~.marketingplatform_admin.ListUserGroupsRequest):
                    The request object. Request message for ListUserGroups
                RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.marketingplatform_admin.ListUserGroupsResponse:
                    Response message for ListUserGroups
                RPC.

            """

            http_options = _BaseMarketingplatformAdminServiceRestTransport._BaseListUserGroups._get_http_options()
            request, metadata = self._interceptor.pre_list_user_groups(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMarketingplatformAdminServiceRestTransport._BaseListUserGroups,
                    "_BaseListUserGroups__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.marketingplatform.admin_v1alpha.MarketingplatformAdminServiceClient.ListUserGroups",
                    extra={
                        "serviceName": "google.marketingplatform.admin.v1alpha.MarketingplatformAdminService",
                        "rpcName": "ListUserGroups",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MarketingplatformAdminServiceRestTransport._ListUserGroups._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = marketingplatform_admin.ListUserGroupsResponse()
            pb_resp = marketingplatform_admin.ListUserGroupsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_user_groups(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_user_groups_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        marketingplatform_admin.ListUserGroupsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.marketingplatform.admin_v1alpha.MarketingplatformAdminServiceClient.list_user_groups",
                    extra={
                        "serviceName": "google.marketingplatform.admin.v1alpha.MarketingplatformAdminService",
                        "rpcName": "ListUserGroups",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ReportPropertyUsage(
        _BaseMarketingplatformAdminServiceRestTransport._BaseReportPropertyUsage,
        MarketingplatformAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "MarketingplatformAdminServiceRestTransport.ReportPropertyUsage"
            )

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: marketingplatform_admin.ReportPropertyUsageRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> marketingplatform_admin.ReportPropertyUsageResponse:
            r"""Call the report property usage method over HTTP.

            Args:
                request (~.marketingplatform_admin.ReportPropertyUsageRequest):
                    The request object. Request message for
                ReportPropertyUsage RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.marketingplatform_admin.ReportPropertyUsageResponse:
                    Response message for
                ReportPropertyUsage RPC.

            """

            http_options = _BaseMarketingplatformAdminServiceRestTransport._BaseReportPropertyUsage._get_http_options()
            request, metadata = self._interceptor.pre_report_property_usage(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMarketingplatformAdminServiceRestTransport._BaseReportPropertyUsage,
                    "_BaseReportPropertyUsage__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.marketingplatform.admin_v1alpha.MarketingplatformAdminServiceClient.ReportPropertyUsage",
                    extra={
                        "serviceName": "google.marketingplatform.admin.v1alpha.MarketingplatformAdminService",
                        "rpcName": "ReportPropertyUsage",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MarketingplatformAdminServiceRestTransport._ReportPropertyUsage._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = marketingplatform_admin.ReportPropertyUsageResponse()
            pb_resp = marketingplatform_admin.ReportPropertyUsageResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_report_property_usage(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_report_property_usage_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        marketingplatform_admin.ReportPropertyUsageResponse.to_json(
                            response
                        )
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.marketingplatform.admin_v1alpha.MarketingplatformAdminServiceClient.report_property_usage",
                    extra={
                        "serviceName": "google.marketingplatform.admin.v1alpha.MarketingplatformAdminService",
                        "rpcName": "ReportPropertyUsage",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetPropertyServiceLevel(
        _BaseMarketingplatformAdminServiceRestTransport._BaseSetPropertyServiceLevel,
        MarketingplatformAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "MarketingplatformAdminServiceRestTransport.SetPropertyServiceLevel"
            )

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: marketingplatform_admin.SetPropertyServiceLevelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> marketingplatform_admin.SetPropertyServiceLevelResponse:
            r"""Call the set property service
            level method over HTTP.

                Args:
                    request (~.marketingplatform_admin.SetPropertyServiceLevelRequest):
                        The request object. Request message for
                    SetPropertyServiceLevel RPC.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.marketingplatform_admin.SetPropertyServiceLevelResponse:
                        Response message for
                    SetPropertyServiceLevel RPC.

            """

            http_options = _BaseMarketingplatformAdminServiceRestTransport._BaseSetPropertyServiceLevel._get_http_options()
            request, metadata = self._interceptor.pre_set_property_service_level(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMarketingplatformAdminServiceRestTransport._BaseSetPropertyServiceLevel,
                    "_BaseSetPropertyServiceLevel__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.marketingplatform.admin_v1alpha.MarketingplatformAdminServiceClient.SetPropertyServiceLevel",
                    extra={
                        "serviceName": "google.marketingplatform.admin.v1alpha.MarketingplatformAdminService",
                        "rpcName": "SetPropertyServiceLevel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MarketingplatformAdminServiceRestTransport._SetPropertyServiceLevel._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = marketingplatform_admin.SetPropertyServiceLevelResponse()
            pb_resp = marketingplatform_admin.SetPropertyServiceLevelResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_set_property_service_level(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_set_property_service_level_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        marketingplatform_admin.SetPropertyServiceLevelResponse.to_json(
                            response
                        )
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.marketingplatform.admin_v1alpha.MarketingplatformAdminServiceClient.set_property_service_level",
                    extra={
                        "serviceName": "google.marketingplatform.admin.v1alpha.MarketingplatformAdminService",
                        "rpcName": "SetPropertyServiceLevel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateAdminAccessBinding(
        _BaseMarketingplatformAdminServiceRestTransport._BaseUpdateAdminAccessBinding,
        MarketingplatformAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "MarketingplatformAdminServiceRestTransport.UpdateAdminAccessBinding"
            )

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: marketingplatform_admin.UpdateAdminAccessBindingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.AdminAccessBinding:
            r"""Call the update admin access
            binding method over HTTP.

                Args:
                    request (~.marketingplatform_admin.UpdateAdminAccessBindingRequest):
                        The request object. Request message for
                    UpdateAdminAccessBinding RPC.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.resources.AdminAccessBinding:
                        A resource message representing a
                    binding to a set of roles.

            """

            http_options = _BaseMarketingplatformAdminServiceRestTransport._BaseUpdateAdminAccessBinding._get_http_options()
            request, metadata = self._interceptor.pre_update_admin_access_binding(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMarketingplatformAdminServiceRestTransport._BaseUpdateAdminAccessBinding,
                    "_BaseUpdateAdminAccessBinding__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.marketingplatform.admin_v1alpha.MarketingplatformAdminServiceClient.UpdateAdminAccessBinding",
                    extra={
                        "serviceName": "google.marketingplatform.admin.v1alpha.MarketingplatformAdminService",
                        "rpcName": "UpdateAdminAccessBinding",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MarketingplatformAdminServiceRestTransport._UpdateAdminAccessBinding._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = resources.AdminAccessBinding()
            pb_resp = resources.AdminAccessBinding.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_admin_access_binding(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_admin_access_binding_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.AdminAccessBinding.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.marketingplatform.admin_v1alpha.MarketingplatformAdminServiceClient.update_admin_access_binding",
                    extra={
                        "serviceName": "google.marketingplatform.admin.v1alpha.MarketingplatformAdminService",
                        "rpcName": "UpdateAdminAccessBinding",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateUserGroup(
        _BaseMarketingplatformAdminServiceRestTransport._BaseUpdateUserGroup,
        MarketingplatformAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash("MarketingplatformAdminServiceRestTransport.UpdateUserGroup")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: marketingplatform_admin.UpdateUserGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.UserGroup:
            r"""Call the update user group method over HTTP.

            Args:
                request (~.marketingplatform_admin.UpdateUserGroupRequest):
                    The request object. Request message for UpdateUserGroup
                RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.UserGroup:
                    A resource message representing a
                user group in a GMP organization.

            """

            http_options = _BaseMarketingplatformAdminServiceRestTransport._BaseUpdateUserGroup._get_http_options()
            request, metadata = self._interceptor.pre_update_user_group(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMarketingplatformAdminServiceRestTransport._BaseUpdateUserGroup,
                    "_BaseUpdateUserGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.marketingplatform.admin_v1alpha.MarketingplatformAdminServiceClient.UpdateUserGroup",
                    extra={
                        "serviceName": "google.marketingplatform.admin.v1alpha.MarketingplatformAdminService",
                        "rpcName": "UpdateUserGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MarketingplatformAdminServiceRestTransport._UpdateUserGroup._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = resources.UserGroup()
            pb_resp = resources.UserGroup.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_user_group(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_user_group_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.UserGroup.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.marketingplatform.admin_v1alpha.MarketingplatformAdminServiceClient.update_user_group",
                    extra={
                        "serviceName": "google.marketingplatform.admin.v1alpha.MarketingplatformAdminService",
                        "rpcName": "UpdateUserGroup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateUserGroupMember(
        _BaseMarketingplatformAdminServiceRestTransport._BaseUpdateUserGroupMember,
        MarketingplatformAdminServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "MarketingplatformAdminServiceRestTransport.UpdateUserGroupMember"
            )

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: marketingplatform_admin.UpdateUserGroupMemberRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.UserGroupMember:
            r"""Call the update user group member method over HTTP.

            Args:
                request (~.marketingplatform_admin.UpdateUserGroupMemberRequest):
                    The request object. Request message for
                UpdateUserGroupMember RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.UserGroupMember:
                    A resource message representing a
                member of a user group.

            """

            http_options = _BaseMarketingplatformAdminServiceRestTransport._BaseUpdateUserGroupMember._get_http_options()
            request, metadata = self._interceptor.pre_update_user_group_member(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMarketingplatformAdminServiceRestTransport._BaseUpdateUserGroupMember,
                    "_BaseUpdateUserGroupMember__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.marketingplatform.admin_v1alpha.MarketingplatformAdminServiceClient.UpdateUserGroupMember",
                    extra={
                        "serviceName": "google.marketingplatform.admin.v1alpha.MarketingplatformAdminService",
                        "rpcName": "UpdateUserGroupMember",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MarketingplatformAdminServiceRestTransport._UpdateUserGroupMember._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = resources.UserGroupMember()
            pb_resp = resources.UserGroupMember.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_user_group_member(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_user_group_member_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.UserGroupMember.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.marketingplatform.admin_v1alpha.MarketingplatformAdminServiceClient.update_user_group_member",
                    extra={
                        "serviceName": "google.marketingplatform.admin.v1alpha.MarketingplatformAdminService",
                        "rpcName": "UpdateUserGroupMember",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_admin_access_binding(
        self,
    ) -> Callable[
        [marketingplatform_admin.CreateAdminAccessBindingRequest],
        resources.AdminAccessBinding,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateAdminAccessBinding(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_analytics_account_link(
        self,
    ) -> Callable[
        [marketingplatform_admin.CreateAnalyticsAccountLinkRequest],
        resources.AnalyticsAccountLink,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateAnalyticsAccountLink(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_user_group(
        self,
    ) -> Callable[
        [marketingplatform_admin.CreateUserGroupRequest], resources.UserGroup
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateUserGroup(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_user_group_member(
        self,
    ) -> Callable[
        [marketingplatform_admin.CreateUserGroupMemberRequest],
        resources.UserGroupMember,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateUserGroupMember(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_analytics_account_link(
        self,
    ) -> Callable[
        [marketingplatform_admin.DeleteAnalyticsAccountLinkRequest], empty_pb2.Empty
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteAnalyticsAccountLink(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_user_group(
        self,
    ) -> Callable[[marketingplatform_admin.DeleteUserGroupRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteUserGroup(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_user_group_member(
        self,
    ) -> Callable[
        [marketingplatform_admin.DeleteUserGroupMemberRequest], empty_pb2.Empty
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteUserGroupMember(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def find_sales_partner_managed_clients(
        self,
    ) -> Callable[
        [marketingplatform_admin.FindSalesPartnerManagedClientsRequest],
        marketingplatform_admin.FindSalesPartnerManagedClientsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FindSalesPartnerManagedClients(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_admin_access_binding(
        self,
    ) -> Callable[
        [marketingplatform_admin.GetAdminAccessBindingRequest],
        resources.AdminAccessBinding,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAdminAccessBinding(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_organization(
        self,
    ) -> Callable[
        [marketingplatform_admin.GetOrganizationRequest], resources.Organization
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetOrganization(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_user_group(
        self,
    ) -> Callable[[marketingplatform_admin.GetUserGroupRequest], resources.UserGroup]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetUserGroup(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_user_group_member(
        self,
    ) -> Callable[
        [marketingplatform_admin.GetUserGroupMemberRequest], resources.UserGroupMember
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetUserGroupMember(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_admin_access_bindings(
        self,
    ) -> Callable[
        [marketingplatform_admin.ListAdminAccessBindingsRequest],
        marketingplatform_admin.ListAdminAccessBindingsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAdminAccessBindings(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_analytics_account_links(
        self,
    ) -> Callable[
        [marketingplatform_admin.ListAnalyticsAccountLinksRequest],
        marketingplatform_admin.ListAnalyticsAccountLinksResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAnalyticsAccountLinks(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_organizations(
        self,
    ) -> Callable[
        [marketingplatform_admin.ListOrganizationsRequest],
        marketingplatform_admin.ListOrganizationsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListOrganizations(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_user_group_members(
        self,
    ) -> Callable[
        [marketingplatform_admin.ListUserGroupMembersRequest],
        marketingplatform_admin.ListUserGroupMembersResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListUserGroupMembers(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_user_groups(
        self,
    ) -> Callable[
        [marketingplatform_admin.ListUserGroupsRequest],
        marketingplatform_admin.ListUserGroupsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListUserGroups(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def report_property_usage(
        self,
    ) -> Callable[
        [marketingplatform_admin.ReportPropertyUsageRequest],
        marketingplatform_admin.ReportPropertyUsageResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ReportPropertyUsage(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def set_property_service_level(
        self,
    ) -> Callable[
        [marketingplatform_admin.SetPropertyServiceLevelRequest],
        marketingplatform_admin.SetPropertyServiceLevelResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetPropertyServiceLevel(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_admin_access_binding(
        self,
    ) -> Callable[
        [marketingplatform_admin.UpdateAdminAccessBindingRequest],
        resources.AdminAccessBinding,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateAdminAccessBinding(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_user_group(
        self,
    ) -> Callable[
        [marketingplatform_admin.UpdateUserGroupRequest], resources.UserGroup
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateUserGroup(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_user_group_member(
        self,
    ) -> Callable[
        [marketingplatform_admin.UpdateUserGroupMemberRequest],
        resources.UserGroupMember,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateUserGroupMember(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("MarketingplatformAdminServiceRestTransport",)
