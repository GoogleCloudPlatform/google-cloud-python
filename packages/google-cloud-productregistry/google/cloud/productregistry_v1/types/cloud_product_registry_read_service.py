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

from google.cloud.productregistry_v1.types import logical_product as gcp_logical_product
from google.cloud.productregistry_v1.types import (
    logical_product_variant as gcp_logical_product_variant,
)
from google.cloud.productregistry_v1.types import product_suite as gcp_product_suite

__protobuf__ = proto.module(
    package="google.cloud.productregistry.v1",
    manifest={
        "GetProductSuiteRequest",
        "GetLogicalProductRequest",
        "GetLogicalProductVariantRequest",
        "ListProductSuitesRequest",
        "ListProductSuitesResponse",
        "ListLogicalProductsRequest",
        "ListLogicalProductsResponse",
        "ListLogicalProductVariantsRequest",
        "ListLogicalProductVariantsResponse",
        "LookupEntityRequest",
        "LookupEntityResponse",
    },
)


class GetProductSuiteRequest(proto.Message):
    r"""Request message for GetProductSuite.

    Attributes:
        name (str):
            Required. The name of the ProductSuite to retrieve. Format:
            productSuites/{product_suite}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetLogicalProductRequest(proto.Message):
    r"""Request message for GetLogicalProduct.

    Attributes:
        name (str):
            Required. The name of the LogicalProduct to retrieve.
            Format: logicalProducts/{logical_product}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetLogicalProductVariantRequest(proto.Message):
    r"""Request message for GetLogicalProductVariant.

    Attributes:
        name (str):
            Required. The name of the LogicalProductVariant to retrieve.
            Format: logicalProducts/{logical_product}/variants/{variant}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListProductSuitesRequest(proto.Message):
    r"""Request message for ListProductSuites.

    Attributes:
        page_size (int):
            Optional. The maximum number of suites to
            return. The service may return fewer than this
            value. If unspecified, at most 100 suites will
            be returned. The maximum value is 500; values
            above 500 will be coerced to 500.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListProductSuites`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListProductSuites`` must match the call that provided the
            page token.
    """

    page_size: int = proto.Field(
        proto.INT32,
        number=1,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListProductSuitesResponse(proto.Message):
    r"""Response message for ListProductSuites.

    Attributes:
        product_suites (MutableSequence[google.cloud.productregistry_v1.types.ProductSuite]):
            Matched ProductSuites
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    product_suites: MutableSequence[gcp_product_suite.ProductSuite] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=gcp_product_suite.ProductSuite,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListLogicalProductsRequest(proto.Message):
    r"""Request message for ListLogicalProducts.

    Attributes:
        filter (str):
            Optional. The filter expression for listing logical
            products. Filter syntax: https://google.aip.dev/160
            Supported fields: suite_id
        page_size (int):
            Optional. The maximum number of logical
            products to return. The service may return fewer
            than this value. If unspecified, at most 100
            logical products will be returned. The maximum
            value is 500; values above 500 will be coerced
            to 500.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListLogicalProducts`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListLogicalProducts`` must match the call that provided
            the page token.
    """

    filter: str = proto.Field(
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


class ListLogicalProductsResponse(proto.Message):
    r"""Response message for ListLogicalProducts.

    Attributes:
        logical_products (MutableSequence[google.cloud.productregistry_v1.types.LogicalProduct]):
            Matched LogicalProducts
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    logical_products: MutableSequence[gcp_logical_product.LogicalProduct] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=gcp_logical_product.LogicalProduct,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListLogicalProductVariantsRequest(proto.Message):
    r"""Request message for ListLogicalProductVariants.

    Attributes:
        parent (str):
            Required. Parent logical product id. Format:
            logicalProducts/{logical_product}
        page_size (int):
            Optional. The maximum number of logical
            product variants to return. The service may
            return fewer than this value. If unspecified, at
            most 100 logical product variants will be
            returned. The maximum value is 500; values above
            500 will be coerced to 500.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListLogicalProductVariants`` call. Provide this to
            retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListLogicalProductVariants`` must match the call that
            provided the page token.
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


class ListLogicalProductVariantsResponse(proto.Message):
    r"""Response message for ListLogicalProductVariants.

    Attributes:
        logical_product_variants (MutableSequence[google.cloud.productregistry_v1.types.LogicalProductVariant]):
            Matched LogicalProductVariants
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    logical_product_variants: MutableSequence[
        gcp_logical_product_variant.LogicalProductVariant
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcp_logical_product_variant.LogicalProductVariant,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class LookupEntityRequest(proto.Message):
    r"""Request message for LookupEntity.

    Attributes:
        lookup_uri (str):
            Required. Entity uri to look up. Supported Formats:
            logicalProducts/{logical_product}
            logicalProducts/{logical_product}/variants/{variant}
            productSuites/{product_suite}
    """

    lookup_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )


class LookupEntityResponse(proto.Message):
    r"""Response message for LookupEntity.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        logical_product (google.cloud.productregistry_v1.types.LogicalProduct):
            Matched LogicalProduct.

            This field is a member of `oneof`_ ``entity``.
        logical_product_variant (google.cloud.productregistry_v1.types.LogicalProductVariant):
            Matched LogicalProductVariant.

            This field is a member of `oneof`_ ``entity``.
        product_suite (google.cloud.productregistry_v1.types.ProductSuite):
            Matched ProductSuite.

            This field is a member of `oneof`_ ``entity``.
    """

    logical_product: gcp_logical_product.LogicalProduct = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="entity",
        message=gcp_logical_product.LogicalProduct,
    )
    logical_product_variant: gcp_logical_product_variant.LogicalProductVariant = (
        proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="entity",
            message=gcp_logical_product_variant.LogicalProductVariant,
        )
    )
    product_suite: gcp_product_suite.ProductSuite = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="entity",
        message=gcp_product_suite.ProductSuite,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
