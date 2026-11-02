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

from google.shopping.css_v1.types import css_product_common

__protobuf__ = proto.module(
    package="google.shopping.css.v1",
    manifest={
        "GetCssProductRequest",
        "CssProduct",
        "ListCssProductsRequest",
        "ListCssProductsResponse",
    },
)


class GetCssProductRequest(proto.Message):
    r"""The request message for the ``GetCssProduct`` method.

    Attributes:
        name (str):
            Required. The name of the CSS product to retrieve. Format:
            ``accounts/{account}/cssProducts/{css_product}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CssProduct(proto.Message):
    r"""The processed CSS Product.

    Attributes:
        name (str):
            The name of the CSS Product. Format:
            ``"accounts/{account}/cssProducts/{css_product}"``
        raw_provided_id (str):
            Output only. Your unique raw identifier for
            the product.
        content_language (str):
            Output only. The two-letter `ISO
            639-1 <http://en.wikipedia.org/wiki/ISO_639-1>`__ language
            code for the product.
        feed_label (str):
            Output only. The feed label for the product.
        attributes (google.shopping.css_v1.types.Attributes):
            Output only. A list of product attributes.
        custom_attributes (MutableSequence[google.shopping.type.types.CustomAttribute]):
            Output only. A list of custom (CSS-provided) attributes. It
            can also be used to submit any attribute of the feed
            specification in its generic form (for example,
            ``{ "name": "size type", "value": "regular" }``). This is
            useful for submitting attributes not explicitly exposed by
            the API, such as additional attributes used for Buy on
            Google.
        css_product_status (google.shopping.css_v1.types.CssProductStatus):
            Output only. The status of a product, data
            validation issues, that is, information about a
            product computed asynchronously.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    raw_provided_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    content_language: str = proto.Field(
        proto.STRING,
        number=3,
    )
    feed_label: str = proto.Field(
        proto.STRING,
        number=4,
    )
    attributes: css_product_common.Attributes = proto.Field(
        proto.MESSAGE,
        number=5,
        message=css_product_common.Attributes,
    )
    custom_attributes: MutableSequence[types.CustomAttribute] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message=types.CustomAttribute,
    )
    css_product_status: css_product_common.CssProductStatus = proto.Field(
        proto.MESSAGE,
        number=8,
        message=css_product_common.CssProductStatus,
    )


class ListCssProductsRequest(proto.Message):
    r"""Request message for the ListCssProducts method.

    Attributes:
        parent (str):
            Required. The account/domain to list
            processed CSS Products for. Format:
            accounts/{account}
        page_size (int):
            The maximum number of CSS Products to return.
            The service may return fewer than this value.
            The maximum value is 1000; values above 1000
            will be coerced to 1000. If unspecified, the
            maximum number of CSS products will be returned.
        page_token (str):
            A page token, received from a previous ``ListCssProducts``
            call. Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListCssProducts`` must match the call that provided the
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


class ListCssProductsResponse(proto.Message):
    r"""Response message for the ListCssProducts method.

    Attributes:
        css_products (MutableSequence[google.shopping.css_v1.types.CssProduct]):
            The processed CSS products from the specified
            account. These are your processed CSS products
            after applying rules and supplemental feeds.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    css_products: MutableSequence["CssProduct"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="CssProduct",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
