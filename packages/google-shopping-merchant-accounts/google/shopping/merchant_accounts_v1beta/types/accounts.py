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

from google.shopping.merchant_accounts_v1beta.types import accountservices, user

__protobuf__ = proto.module(
    package="google.shopping.merchant.accounts.v1beta",
    manifest={
        "Account",
        "GetAccountRequest",
        "CreateAndConfigureAccountRequest",
        "DeleteAccountRequest",
        "UpdateAccountRequest",
        "ListAccountsRequest",
        "ListAccountsResponse",
        "ListSubAccountsRequest",
        "ListSubAccountsResponse",
    },
)


class Account(proto.Message):
    r"""An account.

    Attributes:
        name (str):
            Identifier. The resource name of the account. Format:
            ``accounts/{account}``
        account_id (int):
            Output only. The ID of the account.
        account_name (str):
            Required. A human-readable name of the account. See `store
            name <https://support.google.com/merchants/answer/160556>`__
            and `business
            name <https://support.google.com/merchants/answer/12159159>`__
            for more information.
        adult_content (bool):
            Whether this account contains adult content.
        test_account (bool):
            Output only. Whether this is a test account.
        time_zone (google.type.datetime_pb2.TimeZone):
            Required. The time zone of the account.

            On writes, ``time_zone`` sets both the
            ``reporting_time_zone`` and the ``display_time_zone``.

            For reads, ``time_zone`` always returns the
            ``display_time_zone``. If ``display_time_zone`` doesn't
            exist for your account, ``time_zone`` is empty.
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

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        account (google.shopping.merchant_accounts_v1beta.types.Account):
            Required. The account to be created.
        users (MutableSequence[google.shopping.merchant_accounts_v1beta.types.CreateUserRequest]):
            Optional. Users to be added to the account.
        accept_terms_of_service (google.shopping.merchant_accounts_v1beta.types.CreateAndConfigureAccountRequest.AcceptTermsOfService):
            Optional. The Terms of Service (ToS) to be
            accepted immediately upon account creation.

            This field is a member of `oneof`_ ``_accept_terms_of_service``.
        service (MutableSequence[google.shopping.merchant_accounts_v1beta.types.CreateAndConfigureAccountRequest.AddAccountService]):
            Required. An account service between the account to be
            created and the provider account is initialized as part of
            the creation. At least one such service needs to be
            provided. Currently exactly one of these needs to be
            ``account_aggregation``, which means you can only create sub
            accounts, not standalone account through this method.
            Additional ``account_management`` or ``product_management``
            services may be provided.
    """

    class AcceptTermsOfService(proto.Message):
        r"""Reference to a Terms of Service resource.

        Attributes:
            name (str):
                Required. The resource name of the terms of service version
                in the format ``termsOfService/{version}``. To retrieve the
                latest version, use the
                `termsOfService.retrieveLatest </merchant/api/reference/rest/accounts_v1beta/termsOfService/retrieveLatest>`__
                method.
            region_code (str):
                Required. Region code as defined by
                `CLDR <https://cldr.unicode.org/>`__. This is either a
                country when the ToS applies specifically to that country or
                ``001`` when it applies globally.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        region_code: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class AddAccountService(proto.Message):
        r"""Additional instructions to add account services during
        creation of the account.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            account_aggregation (google.shopping.merchant_accounts_v1beta.types.AccountAggregation):
                The provider is an
                `aggregator <https://support.google.com/merchants/answer/188487>`__
                for the account. Payload for service type Account
                Aggregation.

                This field is a member of `oneof`_ ``service_type``.
            provider (str):
                Optional. The provider of the service. Format:
                ``accounts/{account}``

                This field is a member of `oneof`_ ``_provider``.
        """

        account_aggregation: accountservices.AccountAggregation = proto.Field(
            proto.MESSAGE,
            number=103,
            oneof="service_type",
            message=accountservices.AccountAggregation,
        )
        provider: str = proto.Field(
            proto.STRING,
            number=1,
            optional=True,
        )

    account: "Account" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Account",
    )
    users: MutableSequence[user.CreateUserRequest] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=user.CreateUserRequest,
    )
    accept_terms_of_service: AcceptTermsOfService = proto.Field(
        proto.MESSAGE,
        number=3,
        optional=True,
        message=AcceptTermsOfService,
    )
    service: MutableSequence[AddAccountService] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=AddAccountService,
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
        account (google.shopping.merchant_accounts_v1beta.types.Account):
            Required. The new version of the account.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. List of fields being updated.
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
    r"""Request message for the ``ListAccounts`` method.

    Attributes:
        page_size (int):
            Optional. The maximum number of accounts to
            return. The service may return fewer than this
            value.  If unspecified, at most 250 accounts are
            returned. The maximum value is 500; values above
            500 are coerced to 500.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListAccounts`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListAccounts`` must match the call that provided the page
            token.
        filter (str):
            Optional. Returns only accounts that match the
            `filter </merchant/api/guides/accounts/filter>`__. For more
            details, see the `filter syntax
            reference </merchant/api/guides/accounts/filter-syntax>`__.
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
    r"""Response message for the ``ListAccounts`` method.

    Attributes:
        accounts (MutableSequence[google.shopping.merchant_accounts_v1beta.types.Account]):
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
            Required. The parent account. Format: ``accounts/{account}``
        page_size (int):
            Optional. The maximum number of accounts to
            return. The service may return fewer than this
            value.  If unspecified, at most 250 accounts are
            returned. The maximum value is 500; values above
            500 are coerced to 500.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListAccounts`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListAccounts`` must match the call that provided the page
            token.
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
        accounts (MutableSequence[google.shopping.merchant_accounts_v1beta.types.Account]):
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
