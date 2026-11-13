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
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.type.date_pb2 as date_pb2  # type: ignore
import google.type.money_pb2 as money_pb2  # type: ignore
import proto  # type: ignore

from google.ads.marketingplatform_admin_v1alpha.types import resources

__protobuf__ = proto.module(
    package="google.marketingplatform.admin.v1alpha",
    manifest={
        "GetOrganizationRequest",
        "ListOrganizationsRequest",
        "ListOrganizationsResponse",
        "FindSalesPartnerManagedClientsRequest",
        "FindSalesPartnerManagedClientsResponse",
        "ListAnalyticsAccountLinksRequest",
        "ListAnalyticsAccountLinksResponse",
        "CreateAnalyticsAccountLinkRequest",
        "DeleteAnalyticsAccountLinkRequest",
        "SetPropertyServiceLevelRequest",
        "SetPropertyServiceLevelResponse",
        "ReportPropertyUsageRequest",
        "ReportPropertyUsageResponse",
        "GetUserGroupRequest",
        "ListUserGroupsRequest",
        "ListUserGroupsResponse",
        "CreateUserGroupRequest",
        "UpdateUserGroupRequest",
        "DeleteUserGroupRequest",
        "GetUserGroupMemberRequest",
        "ListUserGroupMembersRequest",
        "ListUserGroupMembersResponse",
        "CreateUserGroupMemberRequest",
        "UpdateUserGroupMemberRequest",
        "DeleteUserGroupMemberRequest",
        "GetAdminAccessBindingRequest",
        "ListAdminAccessBindingsRequest",
        "ListAdminAccessBindingsResponse",
        "CreateAdminAccessBindingRequest",
        "UpdateAdminAccessBindingRequest",
    },
)


class GetOrganizationRequest(proto.Message):
    r"""Request message for GetOrganization RPC.

    Attributes:
        name (str):
            Required. The name of the Organization to retrieve. Format:
            organizations/{org_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListOrganizationsRequest(proto.Message):
    r"""Request message for ListOrganizations RPC.

    Attributes:
        page_size (int):
            Optional. The maximum number of organizations
            to return in one call. The service may return
            fewer than this value.

            If unspecified, at most 50 organizations will be
            returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ListOrganizations call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListOrganizations`` must match the call that provided the
            page token.
    """

    page_size: int = proto.Field(
        proto.INT32,
        number=1,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListOrganizationsResponse(proto.Message):
    r"""Response message for ListOrganizations RPC.

    Attributes:
        organizations (MutableSequence[google.ads.marketingplatform_admin_v1alpha.types.Organization]):
            The Organization resource that the user has
            access to, which includes the org id and display
            name.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    organizations: MutableSequence[resources.Organization] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Organization,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class FindSalesPartnerManagedClientsRequest(proto.Message):
    r"""Request message for FindSalesPartnerManagedClients RPC.

    Attributes:
        organization (str):
            Required. The name of the sales partner organization.
            Format: organizations/{org_id}
        is_active (bool):
            Optional. If set, only active and just ended
            clients will be returned.
    """

    organization: str = proto.Field(
        proto.STRING,
        number=1,
    )
    is_active: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class FindSalesPartnerManagedClientsResponse(proto.Message):
    r"""Response message for FindSalesPartnerManagedClients RPC.

    Attributes:
        client_data (MutableSequence[google.ads.marketingplatform_admin_v1alpha.types.FindSalesPartnerManagedClientsResponse.ClientData]):
            The clients managed by the sales org.
    """

    class ClientData(proto.Message):
        r"""Contains the client data.

        Attributes:
            organization (google.ads.marketingplatform_admin_v1alpha.types.Organization):
                The end client that has/had contract with the
                requested sales org.
            start_date (google.type.date_pb2.Date):
                The start date of the contract between the
                sales org and the end client.
            end_date (google.type.date_pb2.Date):
                The end date of the contract between the
                sales org and the end client.
        """

        organization: resources.Organization = proto.Field(
            proto.MESSAGE,
            number=1,
            message=resources.Organization,
        )
        start_date: date_pb2.Date = proto.Field(
            proto.MESSAGE,
            number=2,
            message=date_pb2.Date,
        )
        end_date: date_pb2.Date = proto.Field(
            proto.MESSAGE,
            number=3,
            message=date_pb2.Date,
        )

    client_data: MutableSequence[ClientData] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=ClientData,
    )


class ListAnalyticsAccountLinksRequest(proto.Message):
    r"""Request message for ListAnalyticsAccountLinks RPC.

    Attributes:
        parent (str):
            Required. The parent organization, which owns this
            collection of Analytics account links. Format:
            organizations/{org_id}
        page_size (int):
            Optional. The maximum number of Analytics
            account links to return in one call. The service
            may return fewer than this value.

            If unspecified, at most 50 Analytics account
            links will be returned. The maximum value is
            1000; values above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ListAnalyticsAccountLinks call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListAnalyticsAccountLinks`` must match the call that
            provided the page token.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListAnalyticsAccountLinksResponse(proto.Message):
    r"""Response message for ListAnalyticsAccountLinks RPC.

    Attributes:
        analytics_account_links (MutableSequence[google.ads.marketingplatform_admin_v1alpha.types.AnalyticsAccountLink]):
            Analytics account links in this organization.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    analytics_account_links: MutableSequence[resources.AnalyticsAccountLink] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=resources.AnalyticsAccountLink,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateAnalyticsAccountLinkRequest(proto.Message):
    r"""Request message for CreateAnalyticsAccountLink RPC.

    Attributes:
        parent (str):
            Required. The parent resource where this Analytics account
            link will be created. Format: organizations/{org_id}
        analytics_account_link (google.ads.marketingplatform_admin_v1alpha.types.AnalyticsAccountLink):
            Required. The Analytics account link to
            create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    analytics_account_link: resources.AnalyticsAccountLink = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.AnalyticsAccountLink,
    )


class DeleteAnalyticsAccountLinkRequest(proto.Message):
    r"""Request message for DeleteAnalyticsAccountLink RPC.

    Attributes:
        name (str):
            Required. The name of the Analytics account link to delete.
            Format:
            organizations/{org_id}/analyticsAccountLinks/{analytics_account_link_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class SetPropertyServiceLevelRequest(proto.Message):
    r"""Request message for SetPropertyServiceLevel RPC.

    Attributes:
        analytics_account_link (str):
            Required. The parent AnalyticsAccountLink scope where this
            property is in. Format:
            organizations/{org_id}/analyticsAccountLinks/{analytics_account_link_id}
        analytics_property (str):
            Required. The Analytics property to change the ServiceLevel
            setting. This field is the name of the Google Analytics
            Admin API property resource.

            Format:
            analyticsadmin.googleapis.com/properties/{property_id}
        service_level (google.ads.marketingplatform_admin_v1alpha.types.AnalyticsServiceLevel):
            Required. The service level to set for this
            property.
    """

    analytics_account_link: str = proto.Field(
        proto.STRING,
        number=1,
    )
    analytics_property: str = proto.Field(
        proto.STRING,
        number=2,
    )
    service_level: resources.AnalyticsServiceLevel = proto.Field(
        proto.ENUM,
        number=3,
        enum=resources.AnalyticsServiceLevel,
    )


class SetPropertyServiceLevelResponse(proto.Message):
    r"""Response message for SetPropertyServiceLevel RPC."""


class ReportPropertyUsageRequest(proto.Message):
    r"""Request message for ReportPropertyUsage RPC.

    Attributes:
        organization (str):
            Required. Specifies the organization whose property usage
            will be listed.

            Format: organizations/{org_id}
        month (str):
            Required. The target month to list property
            usages.
            Format: YYYY-MM. For example, "2025-05".
    """

    organization: str = proto.Field(
        proto.STRING,
        number=1,
    )
    month: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ReportPropertyUsageResponse(proto.Message):
    r"""Response message for ReportPropertyUsage RPC.

    Attributes:
        property_usages (MutableSequence[google.ads.marketingplatform_admin_v1alpha.types.ReportPropertyUsageResponse.PropertyUsage]):
            Usage data for all properties in the
            specified organization and month.
        bill_info (google.ads.marketingplatform_admin_v1alpha.types.ReportPropertyUsageResponse.BillInfo):
            Bill amount in the specified organization and
            month.
            Will be empty if user only has access to usage
            data.
    """

    class PropertyUsage(proto.Message):
        r"""Contains the count of events received by the property, along with
        metadata that influences the volume of ``billable`` events.

        Attributes:
            property (str):
                The name of the Google Analytics Admin API property
                resource.

                Format:
                analyticsadmin.googleapis.com/properties/{property_id}
            display_name (str):
                The display name of the property.
            account_id (int):
                The ID of the property's parent account.
            service_level (google.ads.marketingplatform_admin_v1alpha.types.AnalyticsServiceLevel):
                The service level of the property.
            property_type (google.ads.marketingplatform_admin_v1alpha.types.AnalyticsPropertyType):
                The subtype of the analytics property. This
                affects the billable event count.
            total_event_count (int):
                Total event count that the property received
                during the requested month.
            billable_event_count (int):
                The number of events for which the property
                is billed in the requested month.
        """

        property: str = proto.Field(
            proto.STRING,
            number=1,
        )
        display_name: str = proto.Field(
            proto.STRING,
            number=2,
        )
        account_id: int = proto.Field(
            proto.INT64,
            number=3,
        )
        service_level: resources.AnalyticsServiceLevel = proto.Field(
            proto.ENUM,
            number=4,
            enum=resources.AnalyticsServiceLevel,
        )
        property_type: resources.AnalyticsPropertyType = proto.Field(
            proto.ENUM,
            number=5,
            enum=resources.AnalyticsPropertyType,
        )
        total_event_count: int = proto.Field(
            proto.INT64,
            number=6,
        )
        billable_event_count: int = proto.Field(
            proto.INT64,
            number=7,
        )

    class BillInfo(proto.Message):
        r"""Contains the bill amount.

        Attributes:
            base_fee (google.type.money_pb2.Money):
                The amount of the monthly base fee.
            event_fee (google.type.money_pb2.Money):
                The amount of the event fee.
            price_protection_credit (google.type.money_pb2.Money):
                The amount of the price protection credit,
                this is only available for eligible customers.
            total (google.type.money_pb2.Money):
                The total amount of the bill.
        """

        base_fee: money_pb2.Money = proto.Field(
            proto.MESSAGE,
            number=1,
            message=money_pb2.Money,
        )
        event_fee: money_pb2.Money = proto.Field(
            proto.MESSAGE,
            number=2,
            message=money_pb2.Money,
        )
        price_protection_credit: money_pb2.Money = proto.Field(
            proto.MESSAGE,
            number=3,
            message=money_pb2.Money,
        )
        total: money_pb2.Money = proto.Field(
            proto.MESSAGE,
            number=4,
            message=money_pb2.Money,
        )

    property_usages: MutableSequence[PropertyUsage] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=PropertyUsage,
    )
    bill_info: BillInfo = proto.Field(
        proto.MESSAGE,
        number=2,
        message=BillInfo,
    )


class GetUserGroupRequest(proto.Message):
    r"""Request message for GetUserGroup RPC.

    Attributes:
        name (str):
            Required. The name of the UserGroup to retrieve. Format:
            organizations/{org_id}/userGroups/{user_group_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListUserGroupsRequest(proto.Message):
    r"""Request message for ListUserGroups RPC.

    Attributes:
        parent (str):
            Required. The parent org where this UserGroup will be
            listed. Format: organizations/{org_id}
        page_size (int):
            Optional. The maximum number of user groups
            to return in one call. The service may return
            fewer than this value.

            If unspecified, at most 50 user groups will be
            returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ListUserGroups call. Provide this to retrieve the subsequent
            page.

            When paginating, all other parameters provided to
            ``ListUserGroups`` must match the call that provided the
            page token.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListUserGroupsResponse(proto.Message):
    r"""Response message for ListUserGroups RPC.

    Attributes:
        user_groups (MutableSequence[google.ads.marketingplatform_admin_v1alpha.types.UserGroup]):
            User groups in the organization.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    user_groups: MutableSequence[resources.UserGroup] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.UserGroup,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateUserGroupRequest(proto.Message):
    r"""Request message for CreateUserGroup RPC.

    Attributes:
        parent (str):
            Required. The parent resource where this UserGroup will be
            created. Format: organizations/{org_id}
        user_group (google.ads.marketingplatform_admin_v1alpha.types.UserGroup):
            Required. The user group to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    user_group: resources.UserGroup = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.UserGroup,
    )


class UpdateUserGroupRequest(proto.Message):
    r"""Request message for UpdateUserGroup RPC.

    Attributes:
        user_group (google.ads.marketingplatform_admin_v1alpha.types.UserGroup):
            Required. The user group to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to update. Field names must be
            in snake case (for example, "field_to_update"). Omitted
            fields will not be updated. To replace the entire entity,
            use one path with the string "\*" to match all fields.
    """

    user_group: resources.UserGroup = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.UserGroup,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteUserGroupRequest(proto.Message):
    r"""Request message for DeleteUserGroup RPC.

    Attributes:
        name (str):
            Required. The name of the user group to delete. Format:
            organizations/{org_id}/userGroups/{user_group_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetUserGroupMemberRequest(proto.Message):
    r"""Request message for GetUserGroupMember RPC.

    Attributes:
        name (str):
            Required. The name of the user group member to retrieve.
            Format:
            organizations/{org_id}/userGroups/{user_group_id}/members/{member_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListUserGroupMembersRequest(proto.Message):
    r"""Request message for ListUserGroupMembers RPC.

    Attributes:
        parent (str):
            Required. The parent user group where this UserGroupMember
            will be listed. Format:
            organizations/{org_id}/userGroups/{user_group_id}
        page_size (int):
            Optional. The maximum number of user group
            members to return in one call. The service may
            return fewer than this value.

            If unspecified, at most 50 user group members
            will be returned. The maximum value is 1000;
            values above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ListUserGroupMembers call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListUserGroupMembers`` must match the call that provided
            the page token.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListUserGroupMembersResponse(proto.Message):
    r"""Response message for ListUserGroupMembers RPC.

    Attributes:
        user_group_members (MutableSequence[google.ads.marketingplatform_admin_v1alpha.types.UserGroupMember]):
            User group members in the user group.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    user_group_members: MutableSequence[resources.UserGroupMember] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=resources.UserGroupMember,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateUserGroupMemberRequest(proto.Message):
    r"""Request message for CreateUserGroupMember RPC.

    Attributes:
        parent (str):
            Required. The parent resource where this UserGroupMember
            will be created. Format:
            organizations/{org_id}/userGroups/{user_group_id}
        user_group_member (google.ads.marketingplatform_admin_v1alpha.types.UserGroupMember):
            Required. The user group member to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    user_group_member: resources.UserGroupMember = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.UserGroupMember,
    )


class UpdateUserGroupMemberRequest(proto.Message):
    r"""Request message for UpdateUserGroupMember RPC.

    Attributes:
        user_group_member (google.ads.marketingplatform_admin_v1alpha.types.UserGroupMember):
            Required. The user group member to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to update. Field names must be
            in snake case (for example, "field_to_update"). Omitted
            fields will not be updated. To replace the entire entity,
            use one path with the string "\*" to match all fields.
    """

    user_group_member: resources.UserGroupMember = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.UserGroupMember,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteUserGroupMemberRequest(proto.Message):
    r"""Request message for DeleteUserGroupMember RPC.

    Attributes:
        name (str):
            Required. The name of the user group member to delete.
            Format:
            organizations/{org_id}/userGroups/{user_group_id}/members/{member_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetAdminAccessBindingRequest(proto.Message):
    r"""Response message for GetAdminAccessBinding RPC.

    Attributes:
        name (str):
            Required. The name of the AdminAccessBinding to retrieve.
            Format:
            organizations/{org_id}/adminAccessBindings/{admin_access_binding_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListAdminAccessBindingsRequest(proto.Message):
    r"""Request message for ListAdminAccessBindings RPC.

    Attributes:
        parent (str):
            Required. The parent organization, which owns this
            collection of Admin Access Bindings. Format:
            organizations/{org_id}
        page_size (int):
            Optional. The maximum number of Admin Access
            Bindings to return in one call. The service may
            return fewer than this value.

            If unspecified, at most 50 Admin Access Bindings
            will be returned. The maximum value is 1000;
            values above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ListAdminAccessBindings call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListAdminAccessBindings`` must match the call that
            provided the page token.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListAdminAccessBindingsResponse(proto.Message):
    r"""Response message for ListAdminAccessBindings RPC.

    Attributes:
        admin_access_bindings (MutableSequence[google.ads.marketingplatform_admin_v1alpha.types.AdminAccessBinding]):
            Admin Access Bindings in the organization.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    admin_access_bindings: MutableSequence[resources.AdminAccessBinding] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=resources.AdminAccessBinding,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateAdminAccessBindingRequest(proto.Message):
    r"""Request message for CreateAdminAccessBinding RPC.

    Attributes:
        parent (str):
            Required. The parent organization, which owns this Admin
            Access Binding. Format: organizations/{org_id}
        admin_access_binding (google.ads.marketingplatform_admin_v1alpha.types.AdminAccessBinding):
            Required. The Admin Access Binding to create.

            Only 'user_email' input is allowed.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    admin_access_binding: resources.AdminAccessBinding = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.AdminAccessBinding,
    )


class UpdateAdminAccessBindingRequest(proto.Message):
    r"""Request message for UpdateAdminAccessBinding RPC.

    Attributes:
        admin_access_binding (google.ads.marketingplatform_admin_v1alpha.types.AdminAccessBinding):
            Required. The AdminAccessBinding to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to update. Field names must be
            in snake case (for example, "field_to_update"). Omitted
            fields will not be updated. To replace the entire entity,
            use one path with the string "\*" to match all fields.
    """

    admin_access_binding: resources.AdminAccessBinding = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.AdminAccessBinding,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
