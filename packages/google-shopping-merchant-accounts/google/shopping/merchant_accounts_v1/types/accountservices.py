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
    package="google.shopping.merchant.accounts.v1",
    manifest={
        "AccountService",
        "GetAccountServiceRequest",
        "ListAccountServicesRequest",
        "ListAccountServicesResponse",
        "ProposeAccountServiceRequest",
        "ApproveAccountServiceRequest",
        "RejectAccountServiceRequest",
        "ProductsManagement",
        "CampaignsManagement",
        "AccountManagement",
        "AccountAggregation",
        "LocalListingManagement",
        "ComparisonShopping",
        "Handshake",
    },
)


class AccountService(proto.Message):
    r"""The ``AccountService`` message represents a specific service that a
    provider account offers to a Merchant Center account.

    ``AccountService`` defines the permissions and capabilities granted
    to the provider, allowing for operations such as product management
    or campaign management.

    The lifecycle of an ``AccountService`` involves a proposal phase,
    where one party suggests the service, and an approval phase, where
    the other party accepts or rejects it. This handshake mechanism
    ensures mutual consent before any access is granted. This mechanism
    safeguards both parties by ensuring that access rights are granted
    appropriately and that both the business and provider are aware of
    the services enabled. In scenarios where a user is an admin of both
    accounts, the approval can happen automatically.

    The mutability of a service is also managed through
    ``AccountService``. Some services might be immutable, for example,
    if they were established through other systems or APIs, and you
    cannot alter them through this API.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        products_management (google.shopping.merchant_accounts_v1.types.ProductsManagement):
            Service type for managing products. This
            allows the provider to handle product data on
            behalf of the business, including reading and
            writing product listings. It's commonly used
            when the provider offers inventory management or
            catalog synchronization services to keep the
            business's product information up-to-date across
            platforms.

            This field is a member of `oneof`_ ``service_type``.
        campaigns_management (google.shopping.merchant_accounts_v1.types.CampaignsManagement):
            Service type for managing advertising
            campaigns. Grants the provider access to create
            and manage the business's ad campaigns,
            including setting up campaigns, adjusting bids,
            and optimizing performance.

            This field is a member of `oneof`_ ``service_type``.
        account_management (google.shopping.merchant_accounts_v1.types.AccountManagement):
            Service type for account management. Enables
            the provider to perform administrative actions
            on the business's account, such as configuring
            account settings, managing users, or updating
            business information.

            This field is a member of `oneof`_ ``service_type``.
        account_aggregation (google.shopping.merchant_accounts_v1.types.AccountAggregation):
            Service type for account aggregation. This
            enables the provider, which is an advanced
            account, to manage multiple sub-accounts (client
            accounts). Through this service, the advanced
            account provider can perform administrative and
            operational tasks across all linked
            sub-accounts.

            This is useful for agencies, aggregators, or
            large retailers that need centralized control
            over many Merchant Center accounts.

            This field is a member of `oneof`_ ``service_type``.
        local_listing_management (google.shopping.merchant_accounts_v1.types.LocalListingManagement):
            Service type for local listings management.
            The business group associated with the external
            account id will be used to provide local
            inventory to this Merchant Center account.

            This field is a member of `oneof`_ ``service_type``.
        comparison_shopping (google.shopping.merchant_accounts_v1.types.ComparisonShopping):
            Service type for comparison shopping. The
            provider is a CSS (Comparison Shopping Service)
            managing the account. See
            https://support.google.com/merchants/answer/12653197

            This field is a member of `oneof`_ ``service_type``.
        name (str):
            Identifier. The resource name of the account service.
            Format: ``accounts/{account}/services/{service}``
        provider (str):
            Output only. The provider of the service. Either the
            reference to an account such as ``providers/123`` or a
            well-known service provider (one of ``providers/GOOGLE_ADS``
            or ``providers/GOOGLE_BUSINESS_PROFILE``).

            This field is a member of `oneof`_ ``_provider``.
        provider_display_name (str):
            Output only. The human-readable display name
            of the provider account.
        handshake (google.shopping.merchant_accounts_v1.types.Handshake):
            Output only. Information about the state of
            the service in terms of establishing it (e.g. is
            it pending approval or approved).
        mutability (google.shopping.merchant_accounts_v1.types.AccountService.Mutability):
            Output only. Whether the service is mutable
            (e.g. through Approve / Reject RPCs). A service
            that was created through another system or API
            might be immutable.
        external_account_id (str):
            Immutable. An optional, immutable identifier that Google
            uses to refer to this account when communicating with the
            provider. This should be the unique account ID within the
            provider's system (for example, your shop ID in Shopify).

            If you have multiple accounts with the same provider - for
            instance, different accounts for various regions — the
            ``external_account_id`` differentiates between them,
            ensuring accurate linking and integration between Google and
            the provider.
    """

    class Mutability(proto.Enum):
        r"""The list of mutability option settings a service can have.

        Values:
            MUTABILITY_UNSPECIFIED (0):
                Unused default value
            MUTABLE (1):
                The service can be mutated without
                restrictions.
            IMMUTABLE (2):
                The service is read-only and must not be
                mutated.
        """

        MUTABILITY_UNSPECIFIED = 0
        MUTABLE = 1
        IMMUTABLE = 2

    products_management: "ProductsManagement" = proto.Field(
        proto.MESSAGE,
        number=100,
        oneof="service_type",
        message="ProductsManagement",
    )
    campaigns_management: "CampaignsManagement" = proto.Field(
        proto.MESSAGE,
        number=101,
        oneof="service_type",
        message="CampaignsManagement",
    )
    account_management: "AccountManagement" = proto.Field(
        proto.MESSAGE,
        number=102,
        oneof="service_type",
        message="AccountManagement",
    )
    account_aggregation: "AccountAggregation" = proto.Field(
        proto.MESSAGE,
        number=103,
        oneof="service_type",
        message="AccountAggregation",
    )
    local_listing_management: "LocalListingManagement" = proto.Field(
        proto.MESSAGE,
        number=104,
        oneof="service_type",
        message="LocalListingManagement",
    )
    comparison_shopping: "ComparisonShopping" = proto.Field(
        proto.MESSAGE,
        number=105,
        oneof="service_type",
        message="ComparisonShopping",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    provider: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    provider_display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    handshake: "Handshake" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="Handshake",
    )
    mutability: Mutability = proto.Field(
        proto.ENUM,
        number=5,
        enum=Mutability,
    )
    external_account_id: str = proto.Field(
        proto.STRING,
        number=6,
    )


class GetAccountServiceRequest(proto.Message):
    r"""Request to get an account service.

    Attributes:
        name (str):
            Required. The resource name of the account service to get.
            Format: ``accounts/{account}/services/{service}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListAccountServicesRequest(proto.Message):
    r"""Request to list account services.

    Attributes:
        parent (str):
            Required. The parent account of the account service to
            filter by. Format: ``accounts/{account}``
        page_token (str):
            Optional. The token returned by the previous ``list``
            request.
        page_size (int):
            Optional. The maximum number of elements to return in the
            response. Use for paging. If no ``page_size`` is specified,
            ``100`` is used as the default value. The maximum allowed
            value is ``1000``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=5,
    )


class ListAccountServicesResponse(proto.Message):
    r"""Response after trying to list account services.

    Attributes:
        account_services (MutableSequence[google.shopping.merchant_accounts_v1.types.AccountService]):
            The account services that match your filter.
        next_page_token (str):
            A page token. You can send the ``page_token`` to get the
            next page. Only included in the ``list`` response if there
            are more pages.
    """

    @property
    def raw_page(self):
        return self

    account_services: MutableSequence["AccountService"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AccountService",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ProposeAccountServiceRequest(proto.Message):
    r"""Request to propose an account service.

    Attributes:
        parent (str):
            Required. The resource name of the parent account for the
            service. Format: ``accounts/{account}``
        provider (str):
            Required. The provider of the service. Either the reference
            to an account such as ``providers/123`` or a well-known
            service provider (one of ``providers/GOOGLE_ADS`` or
            ``providers/GOOGLE_BUSINESS_PROFILE``).
        account_service (google.shopping.merchant_accounts_v1.types.AccountService):
            Required. The account service to propose.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    provider: str = proto.Field(
        proto.STRING,
        number=2,
    )
    account_service: "AccountService" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="AccountService",
    )


class ApproveAccountServiceRequest(proto.Message):
    r"""Request to approve an account service.

    Attributes:
        name (str):
            Required. The resource name of the account service to
            approve. Format: ``accounts/{account}/services/{service}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class RejectAccountServiceRequest(proto.Message):
    r"""Request to reject an account service.

    Attributes:
        name (str):
            Required. The resource name of the account service to
            reject. Format: ``accounts/{account}/services/{service}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ProductsManagement(proto.Message):
    r"""``ProductsManagement`` payload."""


class CampaignsManagement(proto.Message):
    r"""``CampaignManagement`` payload."""


class AccountManagement(proto.Message):
    r"""``AccountManagement`` payload."""


class AccountAggregation(proto.Message):
    r"""``AccountAggregation`` payload."""


class LocalListingManagement(proto.Message):
    r"""``LocalListingManagement`` payload."""


class ComparisonShopping(proto.Message):
    r"""``ComparisonShopping`` payload."""


class Handshake(proto.Message):
    r"""The current status of establishing of the service.
    (for example, pending approval or approved).

    Attributes:
        approval_state (google.shopping.merchant_accounts_v1.types.Handshake.ApprovalState):
            Output only. The approval state of this
            handshake.
        actor (google.shopping.merchant_accounts_v1.types.Handshake.Actor):
            Output only. The most recent account to modify the account
            service's ``approval_status``.
    """

    class ApprovalState(proto.Enum):
        r"""The approal state of a handshake.

        Values:
            APPROVAL_STATE_UNSPECIFIED (0):
                Unspecified approval status.
            PENDING (1):
                The service was proposed and is waiting to be
                confirmed.
            ESTABLISHED (2):
                Both parties have confirmed the service.
            REJECTED (3):
                The service proposal was rejected.
        """

        APPROVAL_STATE_UNSPECIFIED = 0
        PENDING = 1
        ESTABLISHED = 2
        REJECTED = 3

    class Actor(proto.Enum):
        r"""The various actors that can be involved in a handshake.

        Values:
            ACTOR_UNSPECIFIED (0):
                Unspecified actor.
            ACCOUNT (1):
                The last change was done by the account who
                has this service.
            OTHER_PARTY (2):
                The last change was done by the other party
                who this service points to.
        """

        ACTOR_UNSPECIFIED = 0
        ACCOUNT = 1
        OTHER_PARTY = 2

    approval_state: ApprovalState = proto.Field(
        proto.ENUM,
        number=1,
        enum=ApprovalState,
    )
    actor: Actor = proto.Field(
        proto.ENUM,
        number=2,
        enum=Actor,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
