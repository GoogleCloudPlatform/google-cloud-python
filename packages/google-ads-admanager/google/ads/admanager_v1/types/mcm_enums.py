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
    package="google.ads.admanager.v1",
    manifest={
        "DelegationTypeEnum",
        "McmReadinessStatusEnum",
        "DelegationInvitationStatusEnum",
        "DelegationAccountStatusEnum",
        "DelegationApprovalStatusEnum",
        "ChildPublisherIdentityVerificationStatusEnum",
        "ChildPublisherAddressVerificationStatusEnum",
        "ChildPublisherOnboardingTaskEnum",
        "McmEarningsProductTypeEnum",
    },
)


class DelegationTypeEnum(proto.Message):
    r"""Wrapper for
    [DelegationType][google.ads.admanager.v1.DelegationTypeEnum.DelegationType]

    """

    class DelegationType(proto.Enum):
        r"""The delegation type of the MCM child publisher.

        Values:
            DELEGATION_TYPE_UNSPECIFIED (0):
                No value specified
            MANAGE_ACCOUNT (1):
                Indicates the parent network gets complete
                access to the child network's account.
            MANAGE_INVENTORY (2):
                Indicates a subset of the ad requests from
                the child are delegated to the parent,
                determined by the tag on the child network's web
                pages. The parent network does not have access
                to the child network, as a subset of the
                inventory could be owned and operated by the
                child network.
        """

        DELEGATION_TYPE_UNSPECIFIED = 0
        MANAGE_ACCOUNT = 1
        MANAGE_INVENTORY = 2


class McmReadinessStatusEnum(proto.Message):
    r"""Wrapper for
    [McmReadinessStatus][google.ads.admanager.v1.McmReadinessStatusEnum.McmReadinessStatus]

    """

    class McmReadinessStatus(proto.Enum):
        r"""Status of the MCM child publisher's Ad Manager network
        onboarding readiness status

        Values:
            MCM_READINESS_STATUS_UNSPECIFIED (0):
                No value specified
            INACTIVE (1):
                Indicates the invitation to the child is
                declined or withdrawn.
            NOT_READY (2):
                Indicates the MCM setup has not yet
                completed. It could be child not yet accepted
                the invitation, Google found noncompliance
                settings or child has not yet completed identity
                or address verifications.
            READY (3):
                Indicates MCM setup has completed. Including
                the child publisher accepted the invite, Google
                found it to be compliant with its policies, i.e.
                no policy violations were found, related
                verifications have completed and the child
                publisher can be served ads.
        """

        MCM_READINESS_STATUS_UNSPECIFIED = 0
        INACTIVE = 1
        NOT_READY = 2
        READY = 3


class DelegationInvitationStatusEnum(proto.Message):
    r"""Wrapper for
    [DelegationInvitationStatus][google.ads.admanager.v1.DelegationInvitationStatusEnum.DelegationInvitationStatus]

    """

    class DelegationInvitationStatus(proto.Enum):
        r"""Status of the association between networks. When a parent
        network requests access, it is marked as pending. Once the child
        network accepts the agreement, it is marked as accepted.

        Values:
            DELEGATION_INVITATION_STATUS_UNSPECIFIED (0):
                No value specified
            ACCEPTED (1):
                Indicates the association request from the
                parent network is accepted by the child network.
            EXPIRED (2):
                Indicates the invite was sent to the child
                publisher more than 90 days ago, due to which it
                has been deactivated.
            PENDING (3):
                Indicates the child publisher has not acted
                on the invite from the parent.
            REJECTED (4):
                Indicates the child publisher has declined
                the invite.
            WITHDRAWN (5):
                Indicates the parent network withdrew the
                invite.
            DEACTIVATED_BY_AD_MANAGER (6):
                Indicates the invitation was disapproved by
                Google.
        """

        DELEGATION_INVITATION_STATUS_UNSPECIFIED = 0
        ACCEPTED = 1
        EXPIRED = 2
        PENDING = 3
        REJECTED = 4
        WITHDRAWN = 5
        DEACTIVATED_BY_AD_MANAGER = 6


class DelegationAccountStatusEnum(proto.Message):
    r"""Wrapper for
    [DelegationAccountStatus][google.ads.admanager.v1.DelegationAccountStatusEnum.DelegationAccountStatus]

    """

    class DelegationAccountStatus(proto.Enum):
        r"""Status of the MCM child publisher's Ad Manager account with
        respect to delegated serving. In order for the child network to
        be served ads for MCM, it must have accepted the invite from the
        parent network, and must have passed Google's policy compliance
        verifications.

        Values:
            DELEGATION_ACCOUNT_STATUS_UNSPECIFIED (0):
                No value specified
            INVITED (1):
                Indicates the child publisher has not acted
                on the invite from the parent.
            DECLINED (2):
                Indicates the child publisher has declined
                the invite.
            APPROVED (3):
                Indicates the child publisher accepted the
                invite, and Google found it to be compliant with
                its policies, i.e. no policy violations were
                found, and the child publisher can be served
                ads.
            CLOSED_BY_PUBLISHER (4):
                Indicates the child publisher has closed
                their own account.
            CLOSED_INVALID_ACTIVITY (5):
                Indicates the child publisher accepted the
                invite, but was disapproved by Google for
                invalid activity.
            CLOSED_POLICY_VIOLATION (6):
                Indicates the child publisher accepted the
                invite, but was disapproved by Google for
                violating its policies.
            DEACTIVATED_BY_AD_MANAGER (7):
                Indicates the child publisher accepted the
                invite, but was disapproved by a Googler.
            DISAPPROVED_DUPLICATE_ACCOUNT (8):
                Indicates the child publisher accepted the
                invite, but was disapproved by Google for being
                a duplicate of another account.
            DISAPPROVED_INELIGIBLE (9):
                Indicates the child publisher accepted the
                invite, but was disapproved as ineligible by
                Google.
            PENDING_GOOGLE_APPROVAL (10):
                Indicates the child publisher has accepted
                the invite, and is awaiting Google's policy
                compliance verifications.
            EXPIRED (11):
                Indicates the invite was sent to the child
                publisher more than 90 days ago, due to which it
                has been deactivated.
            INACTIVE (12):
                Indicates either the child publisher
                disconnected from the parent network, or the
                parent network withdrew the invite.
        """

        DELEGATION_ACCOUNT_STATUS_UNSPECIFIED = 0
        INVITED = 1
        DECLINED = 2
        APPROVED = 3
        CLOSED_BY_PUBLISHER = 4
        CLOSED_INVALID_ACTIVITY = 5
        CLOSED_POLICY_VIOLATION = 6
        DEACTIVATED_BY_AD_MANAGER = 7
        DISAPPROVED_DUPLICATE_ACCOUNT = 8
        DISAPPROVED_INELIGIBLE = 9
        PENDING_GOOGLE_APPROVAL = 10
        EXPIRED = 11
        INACTIVE = 12


class DelegationApprovalStatusEnum(proto.Message):
    r"""Wrapper for
    [DelegationApprovalStatus][google.ads.admanager.v1.DelegationApprovalStatusEnum.DelegationApprovalStatus]

    """

    class DelegationApprovalStatus(proto.Enum):
        r"""Status of the MCM child publisher's Ad Manager network with
        respect to delegated serving. It is only valid when the
        invitation is accepted by the child network. If the child has
        not yet accepted the parent's invite, this will be null.

        Values:
            DELEGATION_APPROVAL_STATUS_UNSPECIFIED (0):
                No value specified
            APPROVED (1):
                Indicates the child publisher accepted the
                invite, and Google found it to be compliant with
                its policies, i.e. no policy violations were
                found, and the child publisher can be served
                ads.
            CLOSED_BY_PUBLISHER (2):
                Indicates the child publisher has closed
                their own account.
            CLOSED_INVALID_ACTIVITY (3):
                Indicates the child publisher accepted the
                invite, but was disapproved by Google for
                invalid activity.
            CLOSED_POLICY_VIOLATION (4):
                Indicates the child publisher accepted the
                invite, but was disapproved by Google for
                violating its policies.
            DEACTIVATED_BY_AD_MANAGER (5):
                Indicates the child publisher accepted the
                invite, but was disapproved by a Googler.
            DISAPPROVED_DUPLICATE_ACCOUNT (6):
                Indicates the child publisher accepted the
                invite, but was disapproved by Google for being
                a duplicate of another account.
            DISAPPROVED_INELIGIBLE (7):
                Indicates the child publisher accepted the
                invite, but was disapproved as ineligible by
                Google.
            PENDING_GOOGLE_APPROVAL (8):
                Indicates the child publisher has accepted
                the invite, and is awaiting Google's policy
                compliance verifications.
        """

        DELEGATION_APPROVAL_STATUS_UNSPECIFIED = 0
        APPROVED = 1
        CLOSED_BY_PUBLISHER = 2
        CLOSED_INVALID_ACTIVITY = 3
        CLOSED_POLICY_VIOLATION = 4
        DEACTIVATED_BY_AD_MANAGER = 5
        DISAPPROVED_DUPLICATE_ACCOUNT = 6
        DISAPPROVED_INELIGIBLE = 7
        PENDING_GOOGLE_APPROVAL = 8


class ChildPublisherIdentityVerificationStatusEnum(proto.Message):
    r"""Wrapper for
    [ChildPublisherIdentityVerificationStatus][google.ads.admanager.v1.ChildPublisherIdentityVerificationStatusEnum.ChildPublisherIdentityVerificationStatus]

    """

    class ChildPublisherIdentityVerificationStatus(proto.Enum):
        r"""The status of the Mcm child identity verification.

        Values:
            CHILD_PUBLISHER_IDENTITY_VERIFICATION_STATUS_UNSPECIFIED (0):
                No value specified
            EXEMPT (1):
                Indicates publisher is exempt from identify
                verification.
            EXPIRED (2):
                Indicates publisher hasn't completed identity
                verification before the expiration date.
            FAILED (3):
                Indicates publisher failed identity
                verification.
            PENDING (4):
                Indicates publisher is pending identity
                verification.
            NOT_ELIGIBLE (5):
                Indicates publisher is not eligible for
                identity verification.
            VERIFIED (6):
                Indicates publisher has completed identity
                verification.
        """

        CHILD_PUBLISHER_IDENTITY_VERIFICATION_STATUS_UNSPECIFIED = 0
        EXEMPT = 1
        EXPIRED = 2
        FAILED = 3
        PENDING = 4
        NOT_ELIGIBLE = 5
        VERIFIED = 6


class ChildPublisherAddressVerificationStatusEnum(proto.Message):
    r"""Wrapper for
    [ChildPublisherAddressVerificationStatus][google.ads.admanager.v1.ChildPublisherAddressVerificationStatusEnum.ChildPublisherAddressVerificationStatus]

    """

    class ChildPublisherAddressVerificationStatus(proto.Enum):
        r"""The status of the Mcm child address verification.

        Values:
            CHILD_PUBLISHER_ADDRESS_VERIFICATION_STATUS_UNSPECIFIED (0):
                No value specified
            EXEMPT (1):
                Indicates publisher is exempt from address
                verification.
            EXPIRED (2):
                Indicates publisher hasn't completed address
                verification before the expiration date.
            FAILED (3):
                Indicates publisher failed address
                verification.
            PENDING (4):
                Indicates publisher's address pin has been
                mailed and must be verified.
            NOT_ELIGIBLE (5):
                Indicates publisher is not eligible for
                address verification.
            VERIFIED (6):
                Indicates publisher's address is verified.
        """

        CHILD_PUBLISHER_ADDRESS_VERIFICATION_STATUS_UNSPECIFIED = 0
        EXEMPT = 1
        EXPIRED = 2
        FAILED = 3
        PENDING = 4
        NOT_ELIGIBLE = 5
        VERIFIED = 6


class ChildPublisherOnboardingTaskEnum(proto.Message):
    r"""Wrapper for
    [ChildPublisherOnboardingTask][google.ads.admanager.v1.ChildPublisherOnboardingTaskEnum.ChildPublisherOnboardingTask]

    """

    class ChildPublisherOnboardingTask(proto.Enum):
        r"""The pending tasks that must be completed by the child publisher
        before Google's policy complicance (i.e.,
        [PENDING_GOOGLE_APPROVAL][google.ads.admanager.v1.DelegationApprovalStatusEnum.DelegationApprovalStatus.PENDING_GOOGLE_APPROVAL])
        can be verified.

        Values:
            CHILD_PUBLISHER_ONBOARDING_TASK_UNSPECIFIED (0):
                No value specified
            BILLING_PROFILE_CREATION (1):
                Indicates the child publisher is required to
                create a payments billing profile.
            PHONE_PIN_VERIFICATION (2):
                Indicates the child publisher is required to
                verify their phone number.
            AD_MANAGER_ACCOUNT_SETUP (4):
                Indicates the child publisher is required to
                setup their Ad Manager account.
        """

        CHILD_PUBLISHER_ONBOARDING_TASK_UNSPECIFIED = 0
        BILLING_PROFILE_CREATION = 1
        PHONE_PIN_VERIFICATION = 2
        AD_MANAGER_ACCOUNT_SETUP = 4


class McmEarningsProductTypeEnum(proto.Message):
    r"""Wrapper for
    [McmEarningsProductType][google.ads.admanager.v1.McmEarningsProductTypeEnum.McmEarningsProductType]

    """

    class McmEarningsProductType(proto.Enum):
        r"""The syndication product type of the child's earnings in MCM.

        Values:
            MCM_EARNINGS_PRODUCT_TYPE_UNSPECIFIED (0):
                No value specified
            AD_EXCHANGE_CONTENT (1):
                Indicates the child network's earnings from
                Google Ad Exchange Content.
            AD_EXCHANGE_CONTENT_HOST (2):
                Indicates the child network's earnings from
                Google Ad Exchange Content made by a host.
            AD_EXCHANGE_GAMES (3):
                Indicates the child network's earnings from
                Google Ad Exchange Games.
            AD_EXCHANGE_GAMES_HOST (4):
                Indicates the child network's earnings from
                Google Ad Exchange Games made by a host.
            AD_EXCHANGE_MOBILE_CONTENT_APP (5):
                Indicates the child network's earnings from
                Google Ad Exchange Content Applications.
            AD_EXCHANGE_MOBILE_CONTENT_APP_HOST (6):
                Indicates the child network's earnings from
                Google Ad Exchange Content Applications made by
                a host.
            AD_EXCHANGE_VIDEO (7):
                Indicates the child network's earnings from
                Google Ad Exchange Video.
            AD_EXCHANGE_VIDEO_HOST (8):
                Indicates the child network's earnings from
                Google Ad Exchange Video made by a host.
            AD_EXCHANGE_RESERVATIONS (9):
                Indicates the child network's earnings from
                Ad Exchange Reservations deals (known externally
                as Programmatic Reservations).
            AD_EXCHANGE_PREFERRED_DEALS (10):
                Indicates the child network's earnings from
                Ad Exchange Preferred deals.
            OFFERWALL (11):
                Indicates the child network's earnings from
                Monteverdi Offerwall.
            BUYER_DIRECT (12):
                Indicates the child network's earnings from
                Agency Direct.
        """

        MCM_EARNINGS_PRODUCT_TYPE_UNSPECIFIED = 0
        AD_EXCHANGE_CONTENT = 1
        AD_EXCHANGE_CONTENT_HOST = 2
        AD_EXCHANGE_GAMES = 3
        AD_EXCHANGE_GAMES_HOST = 4
        AD_EXCHANGE_MOBILE_CONTENT_APP = 5
        AD_EXCHANGE_MOBILE_CONTENT_APP_HOST = 6
        AD_EXCHANGE_VIDEO = 7
        AD_EXCHANGE_VIDEO_HOST = 8
        AD_EXCHANGE_RESERVATIONS = 9
        AD_EXCHANGE_PREFERRED_DEALS = 10
        OFFERWALL = 11
        BUYER_DIRECT = 12


__all__ = tuple(sorted(__protobuf__.manifest))
