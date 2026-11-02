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
    package="google.shopping.merchant.quota.v1",
    manifest={
        "ProductLimit",
        "AccountLimit",
        "GetAccountLimitRequest",
        "ListAccountLimitsRequest",
        "ListAccountLimitsResponse",
    },
)


class ProductLimit(proto.Message):
    r"""The limit for products.

    Attributes:
        scope (google.shopping.merchant_quota_v1.types.ProductLimit.Scope):
            Required. The scope of the product limit.
        limit (int):
            Required. The maximum number of products that
            are allowed in the account in the given scope.
    """

    class Scope(proto.Enum):
        r"""The scope of the limit.

        Values:
            SCOPE_UNSPECIFIED (0):
                Default value. Should not be used.
            ADS_NON_EEA (1):
                Limit for products in non-EEA countries.
            ADS_EEA (2):
                Limit for products in EEA countries.
        """

        SCOPE_UNSPECIFIED = 0
        ADS_NON_EEA = 1
        ADS_EEA = 2

    scope: Scope = proto.Field(
        proto.ENUM,
        number=1,
        enum=Scope,
    )
    limit: int = proto.Field(
        proto.INT64,
        number=2,
    )


class AccountLimit(proto.Message):
    r"""A limit of a certain type that is applied to an account.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        products (google.shopping.merchant_quota_v1.types.ProductLimit):
            The limit for products.

            This field is a member of `oneof`_ ``type``.
        name (str):
            Identifier. The limit part of the name will be a combination
            of the type and the scope. For example:
            ``accounts/123/limits/products~ADS_NON_EEA``

            Format: ``accounts/{account}/limits/{limit}``
    """

    products: "ProductLimit" = proto.Field(
        proto.MESSAGE,
        number=100,
        oneof="type",
        message="ProductLimit",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetAccountLimitRequest(proto.Message):
    r"""Request message for the ``GetAccountLimit`` method.

    Attributes:
        name (str):
            Required. The name of the limit to retrieve. Format:
            ``accounts/{account}/limits/{limit}`` For example:
            ``accounts/123/limits/products~ADS_NON_EEA``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListAccountLimitsRequest(proto.Message):
    r"""Request message for the ``ListAccountLimits`` method.

    Attributes:
        parent (str):
            Required. The parent account. Format: ``accounts/{account}``
        page_size (int):
            Optional. The maximum number of limits to
            return. The service may return fewer than this
            value. If unspecified, at most 100 limits will
            be returned. The maximum value is 100; values
            above 100 will be coerced to 100.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListAccountLimits`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListAccountLimits`` must match the call that provided the
            page token.
        filter (str):
            Required. A filter on the limit ``type`` is required, for
            example, ``type = "products"``.
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
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListAccountLimitsResponse(proto.Message):
    r"""Response message for the ``ListAccountLimits`` method.

    Attributes:
        account_limits (MutableSequence[google.shopping.merchant_quota_v1.types.AccountLimit]):
            The limits for the given account.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    account_limits: MutableSequence["AccountLimit"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AccountLimit",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
