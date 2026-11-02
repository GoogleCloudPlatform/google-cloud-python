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

import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.marketingplatform.admin.v1alpha",
    manifest={
        "LinkVerificationState",
        "AnalyticsServiceLevel",
        "AnalyticsPropertyType",
        "OrganizationRole",
        "Organization",
        "AnalyticsAccountLink",
        "UserGroup",
        "UserGroupMember",
        "AdminAccessBinding",
    },
)


class LinkVerificationState(proto.Enum):
    r"""The verification state of the link between a product account
    and a GMP organization.

    Values:
        LINK_VERIFICATION_STATE_UNSPECIFIED (0):
            The link state is unknown.
        LINK_VERIFICATION_STATE_VERIFIED (1):
            The link is established.
        LINK_VERIFICATION_STATE_NOT_VERIFIED (2):
            The link is requested, but hasn't been
            approved by the product account admin.
    """

    LINK_VERIFICATION_STATE_UNSPECIFIED = 0
    LINK_VERIFICATION_STATE_VERIFIED = 1
    LINK_VERIFICATION_STATE_NOT_VERIFIED = 2


class AnalyticsServiceLevel(proto.Enum):
    r"""Various levels of service for Google Analytics.

    Values:
        ANALYTICS_SERVICE_LEVEL_UNSPECIFIED (0):
            Service level unspecified.
        ANALYTICS_SERVICE_LEVEL_STANDARD (1):
            The standard version of Google Analytics.
        ANALYTICS_SERVICE_LEVEL_360 (2):
            The premium version of Google Analytics.
    """

    ANALYTICS_SERVICE_LEVEL_UNSPECIFIED = 0
    ANALYTICS_SERVICE_LEVEL_STANDARD = 1
    ANALYTICS_SERVICE_LEVEL_360 = 2


class AnalyticsPropertyType(proto.Enum):
    r"""Types of the Google Analytics Property.

    Values:
        ANALYTICS_PROPERTY_TYPE_UNSPECIFIED (0):
            Unknown or unspecified property type
        ANALYTICS_PROPERTY_TYPE_ORDINARY (1):
            Ordinary Google Analytics property
        ANALYTICS_PROPERTY_TYPE_SUBPROPERTY (2):
            Google Analytics subproperty
        ANALYTICS_PROPERTY_TYPE_ROLLUP (3):
            Google Analytics rollup property
    """

    ANALYTICS_PROPERTY_TYPE_UNSPECIFIED = 0
    ANALYTICS_PROPERTY_TYPE_ORDINARY = 1
    ANALYTICS_PROPERTY_TYPE_SUBPROPERTY = 2
    ANALYTICS_PROPERTY_TYPE_ROLLUP = 3


class OrganizationRole(proto.Enum):
    r"""Roles that can be assigned to a user or user group in a GMP
    organization.

    Values:
        ORGANIZATION_ROLE_UNSPECIFIED (0):
            Unknown or unspecified organization role.
        ORG_ADMIN_ROLE (1):
            Organization admin role that grants all
            administrative privileges.
        USER_ADMIN_ROLE (2):
            User admin role that grants access to the
            Users section to perform various user management
            functions.
        BILLING_ADMIN_ROLE (3):
            Billing admin role that grants access to the
            Billing section to perform various
            billing-related functions.
    """

    ORGANIZATION_ROLE_UNSPECIFIED = 0
    ORG_ADMIN_ROLE = 1
    USER_ADMIN_ROLE = 2
    BILLING_ADMIN_ROLE = 3


class Organization(proto.Message):
    r"""A resource message representing a Google Marketing Platform
    organization.

    Attributes:
        name (str):
            Identifier. The resource name of the GMP organization.
            Format: organizations/{org_id}
        display_name (str):
            The human-readable name for the organization.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AnalyticsAccountLink(proto.Message):
    r"""A resource message representing the link between a Google
    Analytics account and a Google Marketing Platform organization.

    Attributes:
        name (str):
            Identifier. Resource name of this AnalyticsAccountLink. Note
            the resource ID is the same as the ID of the Analtyics
            account.

            Format:
            organizations/{org_id}/analyticsAccountLinks/{analytics_account_link_id}
            Example: "organizations/xyz/analyticsAccountLinks/1234".
        analytics_account (str):
            Required. Immutable. The resource name of the AnalyticsAdmin
            API account. The account ID will be used as the ID of this
            AnalyticsAccountLink resource, which will become the final
            component of the resource name.

            Format: analyticsadmin.googleapis.com/accounts/{account_id}
        display_name (str):
            Output only. The human-readable name for the
            Analytics account.
        link_verification_state (google.ads.marketingplatform_admin_v1alpha.types.LinkVerificationState):
            Output only. The verification state of the
            link between the Analytics account and the
            parent organization.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    analytics_account: str = proto.Field(
        proto.STRING,
        number=2,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    link_verification_state: "LinkVerificationState" = proto.Field(
        proto.ENUM,
        number=4,
        enum="LinkVerificationState",
    )


class UserGroup(proto.Message):
    r"""A resource message representing a user group in a GMP
    organization.

    Attributes:
        name (str):
            Identifier. Resource name of this UserGroup.

            Format: organizations/{org_id}/userGroups/{user_group_id}
            Example: "organizations/123abc/userGroups/456def".
        display_name (str):
            Optional. The human-readable name for the
            user group.
        description (str):
            Optional. The description of the user group.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )


class UserGroupMember(proto.Message):
    r"""A resource message representing a member of a user group.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        user_email (str):
            Email address of the user member.

            This field is a member of `oneof`_ ``member``.
        user_group (str):
            User group resource name of the group member.

            This field is a member of `oneof`_ ``member``.
        name (str):
            Identifier. The resource name of this UserGroupMember.

            Format:
            organizations/{org_id}/userGroups/{user_group_id}/members/{member_id}
            Example:
            "organizations/123abc/userGroups/456def/members/789ghi".
        membership_role (google.ads.marketingplatform_admin_v1alpha.types.UserGroupMember.MembershipRole):
            Optional. The role of the member in the user
            group.
    """

    class MembershipRole(proto.Enum):
        r"""The role of the member in the user group.

        Values:
            MEMBERSHIP_ROLE_UNSPECIFIED (0):
                Unspecified membership role.
            MEMBERSHIP_ROLE_OWNER (1):
                Owner role that can add and remove group
                members.
            MEMBERSHIP_ROLE_MEMBER (2):
                Member role that receives all permissions
                assigned to the group.
        """

        MEMBERSHIP_ROLE_UNSPECIFIED = 0
        MEMBERSHIP_ROLE_OWNER = 1
        MEMBERSHIP_ROLE_MEMBER = 2

    user_email: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="member",
    )
    user_group: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="member",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    membership_role: MembershipRole = proto.Field(
        proto.ENUM,
        number=4,
        enum=MembershipRole,
    )


class AdminAccessBinding(proto.Message):
    r"""A resource message representing a binding to a set of roles.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        user_email (str):
            Email address of the user.

            This field is a member of `oneof`_ ``access_target``.
        user_group (str):
            Resource name of the user group.

            This field is a member of `oneof`_ ``access_target``.
        name (str):
            Identifier. The resource name of this AdminAccessBinding.

            Format:
            organizations/{org_id}/adminAccessBindings/{admin_access_binding_id}
            Example: "organizations/123abc/adminAccessBindings/456def".
        organization_roles (MutableSequence[google.ads.marketingplatform_admin_v1alpha.types.OrganizationRole]):
            Optional. A list of roles granted to the parent
            organization.

            USER_ADMIN_ROLE and BILLING_ADMIN_ROLE will be automatically
            added if ORG_ADMIN_ROLE is assigned.

            No roles will be assigned if no roles are specified.
    """

    user_email: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="access_target",
    )
    user_group: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="access_target",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    organization_roles: MutableSequence["OrganizationRole"] = proto.RepeatedField(
        proto.ENUM,
        number=4,
        enum="OrganizationRole",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
