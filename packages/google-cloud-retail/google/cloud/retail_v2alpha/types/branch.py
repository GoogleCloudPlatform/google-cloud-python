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

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.retail_v2alpha.types import product

__protobuf__ = proto.module(
    package="google.cloud.retail.v2alpha",
    manifest={
        "BranchView",
        "Branch",
    },
)


class BranchView(proto.Enum):
    r"""A view that specifies different level of fields of a
    [Branch][google.cloud.retail.v2alpha.Branch] to show in responses.

    Values:
        BRANCH_VIEW_UNSPECIFIED (0):
            The value when it's unspecified. This
            defaults to the BASIC view.
        BRANCH_VIEW_BASIC (1):
            Includes basic metadata about the branch, but not
            statistical fields. See documentation of fields of
            [Branch][google.cloud.retail.v2alpha.Branch] to find what
            fields are excluded from BASIC view.
        BRANCH_VIEW_FULL (2):
            Includes all fields of a
            [Branch][google.cloud.retail.v2alpha.Branch].
    """

    BRANCH_VIEW_UNSPECIFIED = 0
    BRANCH_VIEW_BASIC = 1
    BRANCH_VIEW_FULL = 2


class Branch(proto.Message):
    r"""A data branch that stores all instances of
    [Product][google.cloud.retail.v2alpha.Product]s.

    Attributes:
        name (str):
            Immutable. Full resource name of the branch, such as
            ``projects/*/locations/global/catalogs/default_catalog/branches/branch_id``.
        display_name (str):
            Output only. Human readable name of the
            branch to display in the UI.
        is_default (bool):
            Output only. Indicates whether this branch is
            set as the default branch of its parent catalog.
        last_product_import_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp of last import through
            [ProductService.ImportProducts][google.cloud.retail.v2alpha.ProductService.ImportProducts].
            Empty value means no import has been made to this branch.
        product_count_stats (MutableSequence[google.cloud.retail_v2alpha.types.Branch.ProductCountStatistic]):
            Output only. Statistics for number of products in the
            branch, provided for different
            [scopes][google.cloud.retail.v2alpha.Branch.ProductCountStatistic.ProductCountScope].

            This field is not populated in [BranchView.BASIC][] view.
        quality_metrics (MutableSequence[google.cloud.retail_v2alpha.types.Branch.QualityMetric]):
            Output only. The quality metrics measured among products of
            this branch.

            See
            [QualityMetric.requirement_key][google.cloud.retail.v2alpha.Branch.QualityMetric.requirement_key]
            for supported metrics. Metrics could be missing if failed to
            retrieve.

            This field is not populated in [BranchView.BASIC][] view.
    """

    class ProductCountStatistic(proto.Message):
        r"""A statistic about the number of products in a branch.

        Attributes:
            scope (google.cloud.retail_v2alpha.types.Branch.ProductCountStatistic.ProductCountScope):
                [ProductCountScope] of the [counts].
            counts (MutableMapping[str, int]):
                The number of products in
                [scope][google.cloud.retail.v2alpha.Branch.ProductCountStatistic.scope]
                broken down into different groups.

                The key is a group representing a set of products, and the
                value is the number of products in that group. Note: keys in
                this map may change over time.

                Possible keys:

                - "primary-in-stock", products have
                  [Product.Type.PRIMARY][google.cloud.retail.v2alpha.Product.Type.PRIMARY]
                  type and
                  [Product.Availability.IN_STOCK][google.cloud.retail.v2alpha.Product.Availability.IN_STOCK]
                  availability.

                - "primary-out-of-stock", products have
                  [Product.Type.PRIMARY][google.cloud.retail.v2alpha.Product.Type.PRIMARY]
                  type and
                  [Product.Availability.OUT_OF_STOCK][google.cloud.retail.v2alpha.Product.Availability.OUT_OF_STOCK]
                  availability.

                - "primary-preorder", products have
                  [Product.Type.PRIMARY][google.cloud.retail.v2alpha.Product.Type.PRIMARY]
                  type and
                  [Product.Availability.PREORDER][google.cloud.retail.v2alpha.Product.Availability.PREORDER]
                  availability.

                - "primary-backorder", products have
                  [Product.Type.PRIMARY][google.cloud.retail.v2alpha.Product.Type.PRIMARY]
                  type and
                  [Product.Availability.BACKORDER][google.cloud.retail.v2alpha.Product.Availability.BACKORDER]
                  availability.

                - "variant-in-stock", products have
                  [Product.Type.VARIANT][google.cloud.retail.v2alpha.Product.Type.VARIANT]
                  type and
                  [Product.Availability.IN_STOCK][google.cloud.retail.v2alpha.Product.Availability.IN_STOCK]
                  availability.

                - "variant-out-of-stock", products have
                  [Product.Type.VARIANT][google.cloud.retail.v2alpha.Product.Type.VARIANT]
                  type and
                  [Product.Availability.OUT_OF_STOCK][google.cloud.retail.v2alpha.Product.Availability.OUT_OF_STOCK]
                  availability.

                - "variant-preorder", products have
                  [Product.Type.VARIANT][google.cloud.retail.v2alpha.Product.Type.VARIANT]
                  type and
                  [Product.Availability.PREORDER][google.cloud.retail.v2alpha.Product.Availability.PREORDER]
                  availability.

                - "variant-backorder", products have
                  [Product.Type.VARIANT][google.cloud.retail.v2alpha.Product.Type.VARIANT]
                  type and
                  [Product.Availability.BACKORDER][google.cloud.retail.v2alpha.Product.Availability.BACKORDER]
                  availability.

                - "price-discounted", products have
                  [Product.price_info.price] <
                  [Product.price_info.original_price].
        """

        class ProductCountScope(proto.Enum):
            r"""Scope of what products are included for this count.

            Values:
                PRODUCT_COUNT_SCOPE_UNSPECIFIED (0):
                    Default value for enum. This value is not
                    used in the API response.
                ALL_PRODUCTS (1):
                    Scope for all existing products in the
                    branch. Useful for understanding how many
                    products there are in a branch.
                LAST_24_HOUR_UPDATE (2):
                    Scope for products created or updated in the
                    last 24 hours.
            """

            PRODUCT_COUNT_SCOPE_UNSPECIFIED = 0
            ALL_PRODUCTS = 1
            LAST_24_HOUR_UPDATE = 2

        scope: "Branch.ProductCountStatistic.ProductCountScope" = proto.Field(
            proto.ENUM,
            number=1,
            enum="Branch.ProductCountStatistic.ProductCountScope",
        )
        counts: MutableMapping[str, int] = proto.MapField(
            proto.STRING,
            proto.INT64,
            number=2,
        )

    class QualityMetric(proto.Message):
        r"""Metric measured on a group of
        [Product][google.cloud.retail.v2alpha.Product]s against a certain
        quality requirement. Contains the number of products that pass the
        check and the number of products that don't.

        Attributes:
            requirement_key (str):
                The key that represents a quality requirement rule.

                Supported keys:

                - "has-valid-uri": product has a valid and accessible
                  [uri][google.cloud.retail.v2alpha.Product.uri].

                - "available-expire-time-conformance":
                  [Product.available_time][google.cloud.retail.v2alpha.Product.available_time]
                  is early than "now", and
                  [Product.expire_time][google.cloud.retail.v2alpha.Product.expire_time]
                  is greater than "now".

                - "has-searchable-attributes": product has at least one
                  [attribute][google.cloud.retail.v2alpha.Product.attributes]
                  set to searchable.

                - "has-description": product has non-empty
                  [description][google.cloud.retail.v2alpha.Product.description].

                - "has-at-least-bigram-title": Product
                  [title][google.cloud.retail.v2alpha.Product.title] has at
                  least two words. A comprehensive title helps to improve
                  search quality.

                - "variant-has-image": the
                  [variant][google.cloud.retail.v2alpha.Product.Type.VARIANT]
                  products has at least one
                  [image][google.cloud.retail.v2alpha.Product.images]. You
                  may ignore this metric if all your products are at
                  [primary][google.cloud.retail.v2alpha.Product.Type.PRIMARY]
                  level.

                - "variant-has-price-info": the
                  [variant][google.cloud.retail.v2alpha.Product.Type.VARIANT]
                  products has
                  [price_info][google.cloud.retail.v2alpha.Product.price_info]
                  set. You may ignore this metric if all your products are
                  at
                  [primary][google.cloud.retail.v2alpha.Product.Type.PRIMARY]
                  level.

                - "has-publish-time": product has non-empty
                  [publish_time][google.cloud.retail.v2alpha.Product.publish_time].
            qualified_product_count (int):
                Number of products passing the quality
                requirement check. We only check searchable
                products.
            unqualified_product_count (int):
                Number of products failing the quality
                requirement check. We only check searchable
                products.
            suggested_quality_percent_threshold (float):
                Value from 0 to 100 representing the suggested percentage of
                products that meet the quality requirements to get good
                search and recommendation performance. 100 \*
                (qualified_product_count) / (qualified_product_count +
                unqualified_product_count) should be greater or equal to
                this suggestion.
            unqualified_sample_products (MutableSequence[google.cloud.retail_v2alpha.types.Product]):
                A list of a maximum of 100 sample products that do not
                qualify for this requirement.

                This field is only populated in the response to
                [BranchService.GetBranch][google.cloud.retail.v2alpha.BranchService.GetBranch]
                API, and is always empty for
                [BranchService.ListBranches][google.cloud.retail.v2alpha.BranchService.ListBranches].

                Only the following fields are set in the
                [Product][google.cloud.retail.v2alpha.Product].

                - [Product.name][google.cloud.retail.v2alpha.Product.name]
                - [Product.id][google.cloud.retail.v2alpha.Product.id]
                - [Product.title][google.cloud.retail.v2alpha.Product.title]
        """

        requirement_key: str = proto.Field(
            proto.STRING,
            number=1,
        )
        qualified_product_count: int = proto.Field(
            proto.INT32,
            number=2,
        )
        unqualified_product_count: int = proto.Field(
            proto.INT32,
            number=3,
        )
        suggested_quality_percent_threshold: float = proto.Field(
            proto.DOUBLE,
            number=4,
        )
        unqualified_sample_products: MutableSequence[product.Product] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=5,
                message=product.Product,
            )
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    is_default: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    last_product_import_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    product_count_stats: MutableSequence[ProductCountStatistic] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message=ProductCountStatistic,
    )
    quality_metrics: MutableSequence[QualityMetric] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message=QualityMetric,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
