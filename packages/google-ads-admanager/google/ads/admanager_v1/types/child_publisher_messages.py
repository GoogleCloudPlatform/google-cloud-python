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

from google.ads.admanager_v1.types import mcm_enums

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "ChildPublisher",
    },
)


class ChildPublisher(proto.Message):
    r"""The [ChildPublisher][google.ads.admanager.v1.ChildPublisher]
    resource.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the
            [ChildPublisher][google.ads.admanager.v1.ChildPublisher].
            Format:
            ``networks/{network_code}/childPublishers/{child_publisher_id}``
        display_name (str):
            Required. The display name of the
            [ChildPublisher][google.ads.admanager.v1.ChildPublisher].

            This field is a member of `oneof`_ ``_display_name``.
        email (str):
            Required. The email for the
            [ChildPublisher][google.ads.admanager.v1.ChildPublisher].

            This field is a member of `oneof`_ ``_email``.
        child_network (str):
            Immutable. The resource name of the
            [ChildPublisher][google.ads.admanager.v1.ChildPublisher]'s
            Ad Manager network.

            Format: ``networks/{network_code}``

            This field is a member of `oneof`_ ``_child_network``.
        delegation_type (google.ads.admanager_v1.types.DelegationTypeEnum.DelegationType):
            Required. The type of delegation for the
            [ChildPublisher][google.ads.admanager.v1.ChildPublisher].

            This attribute is immutable while the relationship is
            active.

            This field is a member of `oneof`_ ``_delegation_type``.
        parent_revenue_share_millipercent (int):
            Optional. The revenue share that the parent publisher will
            receive in millipercent. For example, 15000 millipercent is
            15%.

            This attribute is only settable for Manage Account
            [ChildPublisher][google.ads.admanager.v1.ChildPublisher]s of
            non-reseller parent publishers. Otherwise, it is read-only
            and always 100%.

            Additionally, this attribute is immutable while the
            relationship is active.

            This field is a member of `oneof`_ ``_parent_revenue_share_millipercent``.
        seller_id (str):
            Optional. The seller ID for the
            [ChildPublisher][google.ads.admanager.v1.ChildPublisher], as
            specified in the parent publisher's sellers.json file.

            This attribute is only applicable to Manage Inventory
            [ChildPublisher][google.ads.admanager.v1.ChildPublisher]s.

            This field is a member of `oneof`_ ``_seller_id``.
        readiness_status (google.ads.admanager_v1.types.McmReadinessStatusEnum.McmReadinessStatus):
            Output only. The overall onboarding readiness of the
            [ChildPublisher][google.ads.admanager.v1.ChildPublisher].

            This status is correlated with ad serving, but does not
            include site-level approval information.

            This field is a member of `oneof`_ ``_readiness_status``.
        invitation_status (google.ads.admanager_v1.types.DelegationInvitationStatusEnum.DelegationInvitationStatus):
            Output only. The status of the invitation request to the
            [ChildPublisher][google.ads.admanager.v1.ChildPublisher].

            This field is a member of `oneof`_ ``_invitation_status``.
        approval_status (google.ads.admanager_v1.types.DelegationApprovalStatusEnum.DelegationApprovalStatus):
            Output only. The approval status of the
            [ChildPublisher][google.ads.admanager.v1.ChildPublisher].

            This field is a member of `oneof`_ ``_approval_status``.
        identity_verification_status (google.ads.admanager_v1.types.ChildPublisherIdentityVerificationStatusEnum.ChildPublisherIdentityVerificationStatus):
            Output only. The status of the
            [ChildPublisher][google.ads.admanager.v1.ChildPublisher]'s
            identity verification.

            This field is a member of `oneof`_ ``_identity_verification_status``.
        address_verification_status (google.ads.admanager_v1.types.ChildPublisherAddressVerificationStatusEnum.ChildPublisherAddressVerificationStatus):
            Output only. The status of the
            [ChildPublisher][google.ads.admanager.v1.ChildPublisher]'s
            address verification (i.e., mail PIN).

            This field is a member of `oneof`_ ``_address_verification_status``.
        pending_onboarding_tasks (MutableSequence[google.ads.admanager_v1.types.ChildPublisherOnboardingTaskEnum.ChildPublisherOnboardingTask]):
            Output only. The pending onboarding tasks that must be
            completed by the child publisher before Google's policy
            compliance (i.e.
            [DelegationApprovalStatusEnum.DelegationApprovalStatus.PENDING_GOOGLE_APPROVAL][google.ads.admanager.v1.DelegationApprovalStatusEnum.DelegationApprovalStatus.PENDING_GOOGLE_APPROVAL])
            can be verified.
        account_status (google.ads.admanager_v1.types.DelegationAccountStatusEnum.DelegationAccountStatus):
            Output only. The account status of the
            [ChildPublisher][google.ads.admanager.v1.ChildPublisher].

            This field is a member of `oneof`_ ``_account_status``.
        approved_manage_account_revenue_share_millipercent (int):
            Output only. Provides the approved revenue share that the
            parent publisher will receive in millipercent. For example,
            15000 millipercent is 15%.

            This attribute is only set for Manage Account
            [ChildPublisher][google.ads.admanager.v1.ChildPublisher]s of
            non-reseller parent publishers.

            This field is a member of `oneof`_ ``_approved_manage_account_revenue_share_millipercent``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    email: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    child_network: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    delegation_type: mcm_enums.DelegationTypeEnum.DelegationType = proto.Field(
        proto.ENUM,
        number=9,
        optional=True,
        enum=mcm_enums.DelegationTypeEnum.DelegationType,
    )
    parent_revenue_share_millipercent: int = proto.Field(
        proto.INT64,
        number=10,
        optional=True,
    )
    seller_id: str = proto.Field(
        proto.STRING,
        number=11,
        optional=True,
    )
    readiness_status: mcm_enums.McmReadinessStatusEnum.McmReadinessStatus = proto.Field(
        proto.ENUM,
        number=12,
        optional=True,
        enum=mcm_enums.McmReadinessStatusEnum.McmReadinessStatus,
    )
    invitation_status: mcm_enums.DelegationInvitationStatusEnum.DelegationInvitationStatus = proto.Field(
        proto.ENUM,
        number=13,
        optional=True,
        enum=mcm_enums.DelegationInvitationStatusEnum.DelegationInvitationStatus,
    )
    approval_status: mcm_enums.DelegationApprovalStatusEnum.DelegationApprovalStatus = (
        proto.Field(
            proto.ENUM,
            number=15,
            optional=True,
            enum=mcm_enums.DelegationApprovalStatusEnum.DelegationApprovalStatus,
        )
    )
    identity_verification_status: mcm_enums.ChildPublisherIdentityVerificationStatusEnum.ChildPublisherIdentityVerificationStatus = proto.Field(
        proto.ENUM,
        number=17,
        optional=True,
        enum=mcm_enums.ChildPublisherIdentityVerificationStatusEnum.ChildPublisherIdentityVerificationStatus,
    )
    address_verification_status: mcm_enums.ChildPublisherAddressVerificationStatusEnum.ChildPublisherAddressVerificationStatus = proto.Field(
        proto.ENUM,
        number=19,
        optional=True,
        enum=mcm_enums.ChildPublisherAddressVerificationStatusEnum.ChildPublisherAddressVerificationStatus,
    )
    pending_onboarding_tasks: MutableSequence[
        mcm_enums.ChildPublisherOnboardingTaskEnum.ChildPublisherOnboardingTask
    ] = proto.RepeatedField(
        proto.ENUM,
        number=22,
        enum=mcm_enums.ChildPublisherOnboardingTaskEnum.ChildPublisherOnboardingTask,
    )
    account_status: mcm_enums.DelegationAccountStatusEnum.DelegationAccountStatus = (
        proto.Field(
            proto.ENUM,
            number=26,
            optional=True,
            enum=mcm_enums.DelegationAccountStatusEnum.DelegationAccountStatus,
        )
    )
    approved_manage_account_revenue_share_millipercent: int = proto.Field(
        proto.INT64,
        number=29,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
