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
import google.type.datetime_pb2 as datetime_pb2  # type: ignore
import proto  # type: ignore

from google.shopping.merchant_accounts_v1.types import (
    accountservices,
    verificationmailsettings,
)
from google.shopping.merchant_accounts_v1.types import user as gsma_user

__protobuf__ = proto.module(
    package="google.shopping.merchant.accounts.v1",
    manifest={
        "Account",
        "GetAccountRequest",
        "CreateAndConfigureAccountRequest",
        "CreateTestAccountRequest",
        "DeleteAccountRequest",
        "UpdateAccountRequest",
        "ListAccountsRequest",
        "ListAccountsResponse",
        "ListSubAccountsRequest",
        "ListSubAccountsResponse",
    },
)


class Account(proto.Message):
    r"""The ``Account`` message represents a business's account within
    Shopping Ads. It's the primary entity for managing product data,
    settings, and interactions with Google's services and external
    providers.

    Accounts can operate as standalone entities or be part of a advanced
    account structure. In an advanced account setup the parent account
    manages multiple sub-accounts.

    Establishing an account involves configuring attributes like the
    account name, time zone, and language preferences.

    The ``Account`` message is the parent entity for many other
    resources, for example, ``AccountRelationship``, ``Homepage``,
    ``BusinessInfo`` and so on.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the account. Format:
            ``accounts/{account}``
        account_id (int):
            Output only. The ID of the account.
        account_name (str):
            Required. A human-readable name of the account. Don't use
            punctuation, capitalization, or non-alphanumeric symbols
            such as the "/" or "\_" symbols. See `Adding a business
            name <https://support.google.com/merchants/answer/12159159>`__
            for more information.
        adult_content (bool):
            Optional. Whether this account contains adult
            content.

            This field is a member of `oneof`_ ``_adult_content``.
        test_account (bool):
            Output only. Whether this is a test account.
        time_zone (google.type.datetime_pb2.TimeZone):
            Required. The time zone of the account.

            On writes, ``time_zone`` sets both the
            ``reporting_time_zone`` and the ``display_time_zone``.

            For reads, ``time_zone`` always returns the
            ``display_time_zone``. If ``display_time_zone`` doesn't
            exist for your account, ``time_zone`` is empty.

            The ``version`` field is not supported, won't be set in
            responses and will be silently ignored if specified in
            requests.
        language_code (str):
            Required. The account's `BCP-47 language
            code <https://tools.ietf.org/html/bcp47>`__, such as
            ``en-US`` or ``sr-Latn``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    account_id: int = proto.Field(
        proto.INT64,
        number=2,
    )
    account_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    adult_content: bool = proto.Field(
        proto.BOOL,
        number=4,
        optional=True,
    )
    test_account: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    time_zone: datetime_pb2.TimeZone = proto.Field(
        proto.MESSAGE,
        number=6,
        message=datetime_pb2.TimeZone,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=7,
    )


class GetAccountRequest(proto.Message):
    r"""Request message for the ``GetAccount`` method.

    Attributes:
        name (str):
            Required. The name of the account to retrieve. Format:
            ``accounts/{account}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateAndConfigureAccountRequest(proto.Message):
    r"""Request message for the ``CreateAndConfigureAccount`` method.

    Attributes:
        account (google.shopping.merchant_accounts_v1.types.Account):
            Required. The account to be created.
        user (MutableSequence[google.shopping.merchant_accounts_v1.types.CreateAndConfigureAccountRequest.AddUser]):
            Optional. Users to be added to the account.
        service (MutableSequence[google.shopping.merchant_accounts_v1.types.CreateAndConfigureAccountRequest.AddAccountService]):
            Required. An account service between the account to be
            created and the provider account is initialized as part of
            the creation. At least one such service needs to be
            provided. Currently exactly one of these needs to be
            ``account_aggregation`` and ``accounts.createAndConfigure``
            method can be used to create a sub-account under an existing
            advanced account through this method. Additional
            ``account_management`` or ``products_management`` services
            may be provided.
        set_alias (MutableSequence[google.shopping.merchant_accounts_v1.types.CreateAndConfigureAccountRequest.SetAliasForRelationship]):
            Optional. If a relationship is created with a
            provider, you can set an alias for it with this
            field. The calling user must be an admin on the
            provider to be able to set an alias.
    """

    class AddUser(proto.Message):
        r"""Instruction for adding a user to the account during creation.

        Attributes:
            user_id (str):
                Required. The email address of the user (for example,
                ``john.doe@gmail.com``).
            user (google.shopping.merchant_accounts_v1.types.User):
                Optional. Details about the user to be added.
                At the moment, only access rights may be
                specified.
            verification_mail_settings (google.shopping.merchant_accounts_v1.types.VerificationMailSettings):
                Optional. Settings related to configuring the
                verification email that is sent after adding a
                user.
        """

        user_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        user: gsma_user.User = proto.Field(
            proto.MESSAGE,
            number=2,
            message=gsma_user.User,
        )
        verification_mail_settings: verificationmailsettings.VerificationMailSettings = proto.Field(
            proto.MESSAGE,
            number=3,
            message=verificationmailsettings.VerificationMailSettings,
        )

    class AddAccountService(proto.Message):
        r"""Additional instructions to add account services during
        creation of the account.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            account_aggregation (google.shopping.merchant_accounts_v1.types.AccountAggregation):
                The provider is an
                `aggregator <https://support.google.com/merchants/answer/188487>`__
                for the account. Payload for service type Account
                Aggregation.

                This field is a member of `oneof`_ ``service_type``.
            account_management (google.shopping.merchant_accounts_v1.types.AccountManagement):
                The provider manages this account. Payload
                for service type Account Management.

                This field is a member of `oneof`_ ``service_type``.
            comparison_shopping (google.shopping.merchant_accounts_v1.types.ComparisonShopping):
                The provider is a CSS (Comparison Shopping
                Service) of this account. Payload for service
                type Comparison Shopping.

                This field is a member of `oneof`_ ``service_type``.
            products_management (google.shopping.merchant_accounts_v1.types.ProductsManagement):
                The provider manages products for this
                account. Payload for service type products
                management.

                This field is a member of `oneof`_ ``service_type``.
            campaigns_management (google.shopping.merchant_accounts_v1.types.CampaignsManagement):
                The provider manages campaigns for this
                account. Payload for service type campaigns
                management.

                This field is a member of `oneof`_ ``service_type``.
            provider (str):
                Required. The provider of the service. Either the reference
                to an account such as ``providers/123`` or a well-known
                service provider (one of ``providers/GOOGLE_ADS`` or
                ``providers/GOOGLE_BUSINESS_PROFILE``).

                This field is a member of `oneof`_ ``_provider``.
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

                The external account ID must be specified for the campaigns
                management service type.

                The external account ID must not be specified for the
                account aggregation service type.

                The external account ID is optional / may be specified for
                all other service types.
        """

        account_aggregation: accountservices.AccountAggregation = proto.Field(
            proto.MESSAGE,
            number=103,
            oneof="service_type",
            message=accountservices.AccountAggregation,
        )
        account_management: accountservices.AccountManagement = proto.Field(
            proto.MESSAGE,
            number=104,
            oneof="service_type",
            message=accountservices.AccountManagement,
        )
        comparison_shopping: accountservices.ComparisonShopping = proto.Field(
            proto.MESSAGE,
            number=105,
            oneof="service_type",
            message=accountservices.ComparisonShopping,
        )
        products_management: accountservices.ProductsManagement = proto.Field(
            proto.MESSAGE,
            number=106,
            oneof="service_type",
            message=accountservices.ProductsManagement,
        )
        campaigns_management: accountservices.CampaignsManagement = proto.Field(
            proto.MESSAGE,
            number=107,
            oneof="service_type",
            message=accountservices.CampaignsManagement,
        )
        provider: str = proto.Field(
            proto.STRING,
            number=1,
            optional=True,
        )
        external_account_id: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class SetAliasForRelationship(proto.Message):
        r"""Set an alias for a relationship between a provider and the
        account to be created.

        Attributes:
            provider (str):
                Required. The provider of the service. This is a reference
                to an account such as ``providers/123`` or ``accounts/123``.
                The same provider must be specified in at least one of the
                ``service`` fields.
            account_id_alias (str):
                Required. The unique ID of this account in
                the provider's system. The value must be unique
                across all accounts on the platform for this
                provider.
        """

        provider: str = proto.Field(
            proto.STRING,
            number=1,
        )
        account_id_alias: str = proto.Field(
            proto.STRING,
            number=2,
        )

    account: "Account" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Account",
    )
    user: MutableSequence[AddUser] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=AddUser,
    )
    service: MutableSequence[AddAccountService] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=AddAccountService,
    )
    set_alias: MutableSequence[SetAliasForRelationship] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message=SetAliasForRelationship,
    )


class CreateTestAccountRequest(proto.Message):
    r"""Request message for the CreateTestAccount RPC

    Attributes:
        parent (str):
            Required. The account resource name to create
            the test account under. Format:
            accounts/{account}
        account (google.shopping.merchant_accounts_v1.types.Account):
            Required. The account to be created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    account: "Account" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Account",
    )


class DeleteAccountRequest(proto.Message):
    r"""Request message for the ``DeleteAccount`` method.

    Attributes:
        name (str):
            Required. The name of the account to delete. Format:
            ``accounts/{account}``
        force (bool):
            Optional. If set to ``true``, the account is deleted even if
            it provides services to other accounts or has processed
            offers.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class UpdateAccountRequest(proto.Message):
    r"""Request message for the ``UpdateAccount`` method.

    Attributes:
        account (google.shopping.merchant_accounts_v1.types.Account):
            Required. The new version of the account.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. List of fields being updated.

            The following fields are supported (in both ``snake_case``
            and ``lowerCamelCase``):

            - ``account_name``
            - ``adult_content``
            - ``language_code``
            - ``time_zone``
    """

    account: "Account" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Account",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class ListAccountsRequest(proto.Message):
    r"""Request message for the ``accounts.list`` method.

    Attributes:
        page_size (int):
            Optional. The maximum number of accounts to
            return. The service may return fewer than this
            value.  If unspecified, at most 250 accounts are
            returned. The maximum value is 500; values above
            500 are coerced to 500.
        page_token (str):
            Optional. A page token, received from a previous
            ``accounts.list`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided in the
            ``accounts.list`` request must match the call that provided
            the page token.
        filter (str):
            Optional. Returns only accounts that match the
            `filter <https://developers.google.com/merchant/api/guides/accounts/filter>`__.
            For more details, see the `filter syntax
            reference <https://developers.google.com/merchant/api/guides/accounts/filter-syntax>`__.
    """

    page_size: int = proto.Field(
        proto.INT32,
        number=1,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListAccountsResponse(proto.Message):
    r"""Response message for the ``accounts.list`` method.

    Attributes:
        accounts (MutableSequence[google.shopping.merchant_accounts_v1.types.Account]):
            The accounts matching the ``ListAccountsRequest``.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    accounts: MutableSequence["Account"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Account",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListSubAccountsRequest(proto.Message):
    r"""Request message for the ``ListSubAccounts`` method.

    Attributes:
        provider (str):
            Required. The aggregation service provider. Format:
            ``accounts/{accountId}``
        page_size (int):
            Optional. The maximum number of accounts to
            return. The service may return fewer than this
            value.  If unspecified, at most 250 accounts are
            returned. The maximum value is 500; values above
            500 are coerced to 500.
        page_token (str):
            Optional. A page token, received from a previous
            ``accounts.list`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided in the
            ``accounts.list`` request must match the call that provided
            the page token.
    """

    provider: str = proto.Field(
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


class ListSubAccountsResponse(proto.Message):
    r"""Response message for the ``ListSubAccounts`` method.

    Attributes:
        accounts (MutableSequence[google.shopping.merchant_accounts_v1.types.Account]):
            The accounts for which the given parent
            account is an aggregator.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    accounts: MutableSequence["Account"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Account",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
