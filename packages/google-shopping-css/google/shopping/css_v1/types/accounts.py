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
    package="google.shopping.css.v1",
    manifest={
        "ListChildAccountsRequest",
        "ListChildAccountsResponse",
        "GetAccountRequest",
        "UpdateAccountLabelsRequest",
        "Account",
    },
)


class ListChildAccountsRequest(proto.Message):
    r"""The request message for the ``ListChildAccounts`` method.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        parent (str):
            Required. The parent account. Must be a CSS
            group or domain. Format: accounts/{account}
        label_id (int):
            If set, only the MC accounts with the given
            label ID will be returned.

            This field is a member of `oneof`_ ``_label_id``.
        full_name (str):
            If set, only the MC accounts with the given
            name (case sensitive) will be returned.

            This field is a member of `oneof`_ ``_full_name``.
        page_size (int):
            Optional. The maximum number of accounts to
            return. The service may return fewer than this
            value. If unspecified, at most 50 accounts will
            be returned. The maximum value is 100; values
            above 100 will be coerced to 100.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListChildAccounts`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListChildAccounts`` must match the call that provided the
            page token.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    label_id: int = proto.Field(
        proto.INT64,
        number=2,
        optional=True,
    )
    full_name: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=4,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListChildAccountsResponse(proto.Message):
    r"""Response message for the ``ListChildAccounts`` method.

    Attributes:
        accounts (MutableSequence[google.shopping.css_v1.types.Account]):
            The CSS/MC accounts returned for the
            specified CSS parent account.
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


class GetAccountRequest(proto.Message):
    r"""The request message for the ``GetAccount`` method.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. The name of the managed CSS/MC
            account. Format: accounts/{account}
        parent (str):
            Optional. Only required when retrieving MC
            account information. The CSS domain that is the
            parent resource of the MC account. Format:
            accounts/{account}

            This field is a member of `oneof`_ ``_parent``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    parent: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )


class UpdateAccountLabelsRequest(proto.Message):
    r"""The request message for the ``UpdateLabels`` method.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. The label resource name.
            Format: accounts/{account}
        label_ids (MutableSequence[int]):
            The list of label IDs to overwrite the
            existing account label IDs. If the list is
            empty, all currently assigned label IDs will be
            deleted.
        parent (str):
            Optional. Only required when updating MC
            account labels. The CSS domain that is the
            parent resource of the MC account. Format:
            accounts/{account}

            This field is a member of `oneof`_ ``_parent``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    label_ids: MutableSequence[int] = proto.RepeatedField(
        proto.INT64,
        number=2,
    )
    parent: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )


class Account(proto.Message):
    r"""Information about CSS/MC account.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            The label resource name.
            Format: accounts/{account}
        full_name (str):
            Output only. Immutable. The CSS/MC account's
            full name.
        display_name (str):
            The CSS/MC account's short display name.

            This field is a member of `oneof`_ ``_display_name``.
        homepage_uri (str):
            Output only. Immutable. The CSS/MC account's
            homepage.

            This field is a member of `oneof`_ ``_homepage_uri``.
        parent (str):
            The CSS/MC account's parent resource. CSS
            group for CSS domains; CSS domain for MC
            accounts. Returned only if the user has access
            to the parent account.
            Note: For MC sub-accounts, this is also the CSS
            domain that is the parent resource of the MCA
            account, since we are effectively flattening the
            hierarchy.".

            This field is a member of `oneof`_ ``_parent``.
        label_ids (MutableSequence[int]):
            Manually created label IDs assigned to the
            CSS/MC account by a CSS parent account.
        automatic_label_ids (MutableSequence[int]):
            Automatically created label IDs assigned to
            the MC account by CSS Center.
        account_type (google.shopping.css_v1.types.Account.AccountType):
            Output only. The type of this account.
    """

    class AccountType(proto.Enum):
        r"""The account type.

        Values:
            ACCOUNT_TYPE_UNSPECIFIED (0):
                Unknown account type.
            CSS_GROUP (1):
                CSS group account.
            CSS_DOMAIN (2):
                CSS domain account.
            MC_PRIMARY_CSS_MCA (3):
                MC Primary CSS MCA account.
            MC_CSS_MCA (4):
                MC CSS MCA account.
            MC_MARKETPLACE_MCA (5):
                MC Marketplace MCA account.
            MC_OTHER_MCA (6):
                MC Other MCA account.
            MC_STANDALONE (7):
                MC Standalone account.
            MC_MCA_SUBACCOUNT (8):
                MC MCA sub-account.
        """

        ACCOUNT_TYPE_UNSPECIFIED = 0
        CSS_GROUP = 1
        CSS_DOMAIN = 2
        MC_PRIMARY_CSS_MCA = 3
        MC_CSS_MCA = 4
        MC_MARKETPLACE_MCA = 5
        MC_OTHER_MCA = 6
        MC_STANDALONE = 7
        MC_MCA_SUBACCOUNT = 8

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    full_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    homepage_uri: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    parent: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    label_ids: MutableSequence[int] = proto.RepeatedField(
        proto.INT64,
        number=6,
    )
    automatic_label_ids: MutableSequence[int] = proto.RepeatedField(
        proto.INT64,
        number=7,
    )
    account_type: AccountType = proto.Field(
        proto.ENUM,
        number=8,
        enum=AccountType,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
