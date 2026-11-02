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
import proto  # type: ignore

from google.shopping.merchant_accounts_v1beta.types import tax_rule

__protobuf__ = proto.module(
    package="google.shopping.merchant.accounts.v1beta",
    manifest={
        "AccountTax",
        "GetAccountTaxRequest",
        "UpdateAccountTaxRequest",
        "ListAccountTaxRequest",
        "ListAccountTaxResponse",
    },
)


class AccountTax(proto.Message):
    r"""The tax settings of a merchant account. All methods require
    the admin role.

    Attributes:
        name (str):
            Identifier. The name of the tax setting. Format:
            "{account_tax.name=accounts/{account}}".
        account (int):
            Output only. The ID of the account to which
            these account tax settings belong.
        tax_rules (MutableSequence[google.shopping.merchant_accounts_v1beta.types.TaxRule]):
            Tax rules. "Define the tax rules in each
            region. No tax will be presented if a region has
            no rule.".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    account: int = proto.Field(
        proto.INT64,
        number=2,
    )
    tax_rules: MutableSequence[tax_rule.TaxRule] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=tax_rule.TaxRule,
    )


class GetAccountTaxRequest(proto.Message):
    r"""Request to get tax settings

    Attributes:
        name (str):
            Required. The name from which tax settings
            will be retrieved
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateAccountTaxRequest(proto.Message):
    r"""Request to update the tax settings

    Attributes:
        account_tax (google.shopping.merchant_accounts_v1beta.types.AccountTax):
            Required. The tax setting that will be
            updated
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields to be updated
    """

    account_tax: "AccountTax" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="AccountTax",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class ListAccountTaxRequest(proto.Message):
    r"""Request to list all sub-account tax settings only for the
    requesting merchant This method can only be called on a
    multi-client account, otherwise it'll return an error.

    Attributes:
        parent (str):
            Required. The parent, which owns this
            collection of account tax. Format:
            accounts/{account}
        page_size (int):
            The maximum number of tax settings to return
            in the response, used for paging.
        page_token (str):
            The token returned by the previous request.
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


class ListAccountTaxResponse(proto.Message):
    r"""Response to account tax list request
    This method can only be called on a multi-client account,
    otherwise it'll return an error.

    Attributes:
        account_taxes (MutableSequence[google.shopping.merchant_accounts_v1beta.types.AccountTax]):
            Page of accounttax settings
        next_page_token (str):
            The token for the retrieval of the next page
            of account tax settings.
    """

    @property
    def raw_page(self):
        return self

    account_taxes: MutableSequence["AccountTax"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AccountTax",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
