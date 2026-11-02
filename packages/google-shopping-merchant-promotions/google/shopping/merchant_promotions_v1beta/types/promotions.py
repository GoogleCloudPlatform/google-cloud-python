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
from google.shopping.type.types import types

from google.shopping.merchant_promotions_v1beta.types import promotions_common

__protobuf__ = proto.module(
    package="google.shopping.merchant.promotions.v1beta",
    manifest={
        "Promotion",
        "InsertPromotionRequest",
        "GetPromotionRequest",
        "ListPromotionsRequest",
        "ListPromotionsResponse",
    },
)


class Promotion(proto.Message):
    r"""Represents a promotion. See the following articles for more details.

    Required promotion input attributes to pass data validation checks
    are primarily defined below:

    - `Promotions data
      specification <https://support.google.com/merchants/answer/2906014>`__
    - `Local promotions data
      specification <https://support.google.com/merchants/answer/10146130>`__

    After inserting, updating a promotion input, it may take several
    minutes before the final promotion can be retrieved.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The name of the promotion. Format:
            ``accounts/{account}/promotions/{promotion}``
        promotion_id (str):
            Required. The user provided promotion ID to uniquely
            identify the promotion. Follow `minimum
            requirements <https://support.google.com/merchants/answer/7050148?ref_topic=7322920&sjid=871860036916537104-NC#minimum_requirements>`__
            to prevent promotion disapprovals.
        content_language (str):
            Required. The two-letter `ISO
            639-1 <http://en.wikipedia.org/wiki/ISO_639-1>`__ language
            code for the promotion.

            Promotions is only for `selected
            languages <https://support.google.com/merchants/answer/4588281?ref_topic=6396150&sjid=18314938579342094533-NC#option3&zippy=>`__.
        target_country (str):
            Required. The target country used as part of the unique
            identifier. Represented as a `CLDR territory
            code <https://github.com/unicode-org/cldr/blob/latest/common/main/en.xml>`__.

            Promotions are only available in selected countries, `Free
            Listings and Shopping
            ads <https://support.google.com/merchants/answer/4588460>`__
            `Local Inventory
            ads <https://support.google.com/merchants/answer/10146326>`__
        redemption_channel (MutableSequence[google.shopping.merchant_promotions_v1beta.types.RedemptionChannel]):
            Required. `Redemption
            channel <https://support.google.com/merchants/answer/13837674?ref_topic=13773355&sjid=17642868584668136159-NC>`__
            for the promotion. At least one channel is required.
        data_source (str):
            Output only. The primary data source of the
            promotion.
        attributes (google.shopping.merchant_promotions_v1beta.types.Attributes):
            Optional. A list of promotion attributes.
        custom_attributes (MutableSequence[google.shopping.type.types.CustomAttribute]):
            Optional. A list of custom (merchant-provided) attributes.
            It can also be used for submitting any attribute of the data
            specification in its generic form (for example,
            ``{ "name": "size type", "value": "regular" }``). This is
            useful for submitting attributes not explicitly exposed by
            the API.
        promotion_status (google.shopping.merchant_promotions_v1beta.types.PromotionStatus):
            Output only. The `status of a
            promotion <https://support.google.com/merchants/answer/3398326?ref_topic=7322924&sjid=5155774230887277618-NC>`__,
            data validation issues, that is, information about a
            promotion computed asynchronously.
        version_number (int):
            Optional. Represents the existing version (freshness) of the
            promotion, which can be used to preserve the right order
            when multiple updates are done at the same time.

            If set, the insertion is prevented when version number is
            lower than the current version number of the existing
            promotion. Re-insertion (for example, promotion refresh
            after 30 days) can be performed with the current
            ``version_number``.

            If the operation is prevented, the aborted exception will be
            thrown.

            This field is a member of `oneof`_ ``_version_number``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    promotion_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    content_language: str = proto.Field(
        proto.STRING,
        number=3,
    )
    target_country: str = proto.Field(
        proto.STRING,
        number=4,
    )
    redemption_channel: MutableSequence[promotions_common.RedemptionChannel] = (
        proto.RepeatedField(
            proto.ENUM,
            number=5,
            enum=promotions_common.RedemptionChannel,
        )
    )
    data_source: str = proto.Field(
        proto.STRING,
        number=6,
    )
    attributes: promotions_common.Attributes = proto.Field(
        proto.MESSAGE,
        number=7,
        message=promotions_common.Attributes,
    )
    custom_attributes: MutableSequence[types.CustomAttribute] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message=types.CustomAttribute,
    )
    promotion_status: promotions_common.PromotionStatus = proto.Field(
        proto.MESSAGE,
        number=9,
        message=promotions_common.PromotionStatus,
    )
    version_number: int = proto.Field(
        proto.INT64,
        number=10,
        optional=True,
    )


class InsertPromotionRequest(proto.Message):
    r"""Request message for the ``InsertPromotion`` method.

    Attributes:
        parent (str):
            Required. The account where the promotion
            will be inserted. Format: accounts/{account}
        promotion (google.shopping.merchant_promotions_v1beta.types.Promotion):
            Required. The promotion to insert.
        data_source (str):
            Required. The data source of the
            `promotion <https://support.google.com/merchants/answer/6396268?sjid=5155774230887277618-NC>`__
            Format: ``accounts/{account}/dataSources/{datasource}``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    promotion: "Promotion" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Promotion",
    )
    data_source: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GetPromotionRequest(proto.Message):
    r"""Request message for the ``GetPromotion`` method.

    Attributes:
        name (str):
            Required. The name of the promotion to retrieve. Format:
            ``accounts/{account}/promotions/{promotions}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListPromotionsRequest(proto.Message):
    r"""Request message for the ``ListPromotions`` method.

    Attributes:
        parent (str):
            Required. The account to list processed promotions for.
            Format: ``accounts/{account}``
        page_size (int):
            Output only. The maximum number of promotions
            to return. The service may return fewer than
            this value. The maximum value is 1000; values
            above 1000 will be coerced to 1000. If
            unspecified, the maximum number of promotions
            will be returned.
        page_token (str):
            Output only. A page token, received from a previous
            ``ListPromotions`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListPromotions`` must match the call that provided the
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


class ListPromotionsResponse(proto.Message):
    r"""Response message for the ``ListPromotions`` method.

    Attributes:
        promotions (MutableSequence[google.shopping.merchant_promotions_v1beta.types.Promotion]):
            The processed promotions from the specified
            account.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    promotions: MutableSequence["Promotion"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Promotion",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
