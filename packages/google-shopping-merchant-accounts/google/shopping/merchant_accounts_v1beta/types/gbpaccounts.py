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

import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.shopping.merchant.accounts.v1beta",
    manifest={
        "GbpAccount",
        "ListGbpAccountsRequest",
        "ListGbpAccountsResponse",
        "LinkGbpAccountRequest",
        "LinkGbpAccountResponse",
    },
)


class GbpAccount(proto.Message):
    r"""Collection of information related to a Google Business
    Profile (GBP) account.

    Attributes:
        name (str):
            Identifier. The resource name of the GBP account. Format:
            ``accounts/{account}/gbpAccount/{gbp_account}``
        gbp_account_id (str):
            The id of the GBP account.
        type_ (google.shopping.merchant_accounts_v1beta.types.GbpAccount.Type):
            The type of the Business Profile.
        gbp_account_name (str):
            The name of the Business Profile.
            For personal accounts: Email id of the owner.
            For Business accounts: Name of the Business
            Account.
        listing_count (int):
            Number of listings under this account.
    """

    class Type(proto.Enum):
        r"""The type of the GBP account.

        Values:
            TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            USER (1):
                The GBP account is a user account.
            BUSINESS_ACCOUNT (2):
                The GBP account is a business account.
        """

        TYPE_UNSPECIFIED = 0
        USER = 1
        BUSINESS_ACCOUNT = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    gbp_account_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=3,
        enum=Type,
    )
    gbp_account_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    listing_count: int = proto.Field(
        proto.INT64,
        number=6,
    )


class ListGbpAccountsRequest(proto.Message):
    r"""Request message for the ListGbpAccounts method.

    Attributes:
        parent (str):
            Required. The name of the parent resource under which the
            GBP accounts are listed. Format: ``accounts/{account}``.
        page_size (int):
            Optional. The maximum number of ``GbpAccount`` resources to
            return. The service returns fewer than this value if the
            number of gbp accounts is less that than the ``pageSize``.
            The default value is 50. The maximum value is 1000; If a
            value higher than the maximum is specified, then the
            ``pageSize`` will default to the maximum.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListGbpAccounts`` call. Provide the page token to retrieve
            the subsequent page.

            When paginating, all other parameters provided to
            ``ListGbpAccounts`` must match the call that provided the
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


class ListGbpAccountsResponse(proto.Message):
    r"""Response message for the ListGbpAccounts method.

    Attributes:
        gbp_accounts (MutableSequence[google.shopping.merchant_accounts_v1beta.types.GbpAccount]):
            The GBP accounts from the specified merchant
            in the specified country.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    gbp_accounts: MutableSequence["GbpAccount"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="GbpAccount",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class LinkGbpAccountRequest(proto.Message):
    r"""Request message for the LinkGbpAccount method.

    Attributes:
        parent (str):
            Required. The name of the parent resource to which the GBP
            account is linked. Format: ``accounts/{account}``.
        gbp_email (str):
            Required. The email address of the Business
            Profile account.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    gbp_email: str = proto.Field(
        proto.STRING,
        number=2,
    )


class LinkGbpAccountResponse(proto.Message):
    r"""Response message for the LinkGbpAccount method.

    Attributes:
        response (google.protobuf.empty_pb2.Empty):
            Empty response.
    """

    response: empty_pb2.Empty = proto.Field(
        proto.MESSAGE,
        number=1,
        message=empty_pb2.Empty,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
