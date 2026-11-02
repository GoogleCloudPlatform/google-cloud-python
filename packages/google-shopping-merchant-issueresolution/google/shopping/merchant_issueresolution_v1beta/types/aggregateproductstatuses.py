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

__protobuf__ = proto.module(
    package="google.shopping.merchant.issueresolution.v1beta",
    manifest={
        "ListAggregateProductStatusesRequest",
        "ListAggregateProductStatusesResponse",
        "AggregateProductStatus",
    },
)


class ListAggregateProductStatusesRequest(proto.Message):
    r"""Request message for the ``ListAggregateProductStatuses`` method.

    Attributes:
        parent (str):
            Required. The account to list aggregate product statuses
            for. Format: ``accounts/{account}``
        page_size (int):
            Optional. The maximum number of aggregate
            product statuses to return. The service may
            return fewer than this value. If unspecified, at
            most 25 aggregate product statuses are returned.
            The maximum value is 250; values above 250 are
            coerced to 250.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListAggregateProductStatuses`` call. Provide this to
            retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListAggregateProductStatuses`` must match the call that
            provided the page token.
        filter (str):
            Optional. A filter expression that filters the aggregate
            product statuses. Filtering is only supported by the
            ``reporting_context`` and ``country`` field. For example:
            ``reporting_context = "SHOPPING_ADS" AND country = "US"``.
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


class ListAggregateProductStatusesResponse(proto.Message):
    r"""Response message for the ``ListAggregateProductStatuses`` method.

    Attributes:
        aggregate_product_statuses (MutableSequence[google.shopping.merchant_issueresolution_v1beta.types.AggregateProductStatus]):
            The ``AggregateProductStatuses`` resources for the given
            account.
        next_page_token (str):
            A token, which can be sent as ``pageToken`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    aggregate_product_statuses: MutableSequence["AggregateProductStatus"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="AggregateProductStatus",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AggregateProductStatus(proto.Message):
    r"""Aggregate product statuses for a given reporting context and
    country.

    Attributes:
        name (str):
            Identifier. The name of the ``AggregateProductStatuses``
            resource. Format:
            ``accounts/{account}/aggregateProductStatuses/{aggregateProductStatuses}``
        reporting_context (google.shopping.type.types.ReportingContext.ReportingContextEnum):
            The reporting context of the aggregate
            product statuses.
        country (str):
            The country of the aggregate product statuses. Represented
            as a `CLDR territory
            code <https://github.com/unicode-org/cldr/blob/latest/common/main/en.xml>`__.
        stats (google.shopping.merchant_issueresolution_v1beta.types.AggregateProductStatus.Stats):
            Products statistics for the given reporting
            context and country.
        item_level_issues (MutableSequence[google.shopping.merchant_issueresolution_v1beta.types.AggregateProductStatus.ItemLevelIssue]):
            The product issues that affect the given
            reporting context and country.
    """

    class Stats(proto.Message):
        r"""Products statistics.

        Attributes:
            active_count (int):
                The number of products that are active.
            pending_count (int):
                The number of products that are pending.
            disapproved_count (int):
                The number of products that are disapproved.
            expiring_count (int):
                The number of products that are expiring.
        """

        active_count: int = proto.Field(
            proto.INT64,
            number=1,
        )
        pending_count: int = proto.Field(
            proto.INT64,
            number=2,
        )
        disapproved_count: int = proto.Field(
            proto.INT64,
            number=3,
        )
        expiring_count: int = proto.Field(
            proto.INT64,
            number=4,
        )

    class ItemLevelIssue(proto.Message):
        r"""The ItemLevelIssue of the product status.

        Attributes:
            code (str):
                The error code of the issue.
            severity (google.shopping.merchant_issueresolution_v1beta.types.AggregateProductStatus.ItemLevelIssue.Severity):
                How this issue affects serving of the offer.
            resolution (google.shopping.merchant_issueresolution_v1beta.types.AggregateProductStatus.ItemLevelIssue.Resolution):
                Whether the issue can be resolved by the
                merchant.
            attribute (str):
                The attribute's name, if the issue is caused
                by a single attribute.
            description (str):
                A short issue description in English.
            detail (str):
                A detailed issue description in English.
            documentation_uri (str):
                The URL of a web page to help with resolving
                this issue.
            product_count (int):
                The number of products affected by this
                issue.
        """

        class Severity(proto.Enum):
            r"""How the issue affects the serving of the product.

            Values:
                SEVERITY_UNSPECIFIED (0):
                    Not specified.
                NOT_IMPACTED (1):
                    This issue represents a warning and does not
                    have a direct affect on the product.
                DEMOTED (2):
                    The product is demoted and most likely have
                    limited performance in search results
                DISAPPROVED (3):
                    Issue disapproves the product.
            """

            SEVERITY_UNSPECIFIED = 0
            NOT_IMPACTED = 1
            DEMOTED = 2
            DISAPPROVED = 3

        class Resolution(proto.Enum):
            r"""How the issue can be resolved.

            Values:
                RESOLUTION_UNSPECIFIED (0):
                    Not specified.
                MERCHANT_ACTION (1):
                    The issue can be resolved by the merchant.
                PENDING_PROCESSING (2):
                    The issue will be resolved auomatically.
            """

            RESOLUTION_UNSPECIFIED = 0
            MERCHANT_ACTION = 1
            PENDING_PROCESSING = 2

        code: str = proto.Field(
            proto.STRING,
            number=1,
        )
        severity: "AggregateProductStatus.ItemLevelIssue.Severity" = proto.Field(
            proto.ENUM,
            number=2,
            enum="AggregateProductStatus.ItemLevelIssue.Severity",
        )
        resolution: "AggregateProductStatus.ItemLevelIssue.Resolution" = proto.Field(
            proto.ENUM,
            number=3,
            enum="AggregateProductStatus.ItemLevelIssue.Resolution",
        )
        attribute: str = proto.Field(
            proto.STRING,
            number=4,
        )
        description: str = proto.Field(
            proto.STRING,
            number=6,
        )
        detail: str = proto.Field(
            proto.STRING,
            number=7,
        )
        documentation_uri: str = proto.Field(
            proto.STRING,
            number=8,
        )
        product_count: int = proto.Field(
            proto.INT64,
            number=9,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    reporting_context: types.ReportingContext.ReportingContextEnum = proto.Field(
        proto.ENUM,
        number=3,
        enum=types.ReportingContext.ReportingContextEnum,
    )
    country: str = proto.Field(
        proto.STRING,
        number=4,
    )
    stats: Stats = proto.Field(
        proto.MESSAGE,
        number=5,
        message=Stats,
    )
    item_level_issues: MutableSequence[ItemLevelIssue] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message=ItemLevelIssue,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
