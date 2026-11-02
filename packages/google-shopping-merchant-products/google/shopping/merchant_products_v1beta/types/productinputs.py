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
from google.shopping.type.types import types

from google.shopping.merchant_products_v1beta.types import products_common

__protobuf__ = proto.module(
    package="google.shopping.merchant.products.v1beta",
    manifest={
        "ProductInput",
        "InsertProductInputRequest",
        "UpdateProductInputRequest",
        "DeleteProductInputRequest",
    },
)


class ProductInput(proto.Message):
    r"""This resource represents input data you submit for a product, not
    the processed product that you see in Merchant Center, in Shopping
    ads, or across Google surfaces. Product inputs, rules and
    supplemental data source data are combined to create the processed
    [Product][google.shopping.merchant.products.v1beta.Product]. For
    more information, see `Manage
    products </merchant/api/guides/products/overview>`__.

    Required product input attributes to pass data validation checks are
    primarily defined in the `Products Data
    Specification <https://support.google.com/merchants/answer/188494>`__.

    The following attributes are required:
    [feedLabel][google.shopping.merchant.products.v1beta.Product.feed_label],
    [contentLanguage][google.shopping.merchant.products.v1beta.Product.content_language]
    and
    [offerId][google.shopping.merchant.products.v1beta.Product.offer_id].

    After inserting, updating, or deleting a product input, it may take
    several minutes before the processed product can be retrieved.

    All fields in the product input and its sub-messages match the
    English name of their corresponding attribute in the `Products Data
    Specification <https://support.google.com/merchants/answer/188494>`__
    with `some
    exceptions <https://support.google.com/merchants/answer/7052112>`__.
    The following reference documentation lists the field names in the
    **camelCase** casing style while the Products Data Specification
    lists the names in the **snake_case** casing style.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The name of the product input. Format:
            ``accounts/{account}/productInputs/{productinput}`` where
            the last section ``productinput`` consists of 4 parts:
            ``channel~content_language~feed_label~offer_id`` example for
            product input name is
            ``accounts/123/productInputs/online~en~US~sku123``
        product (str):
            Output only. The name of the processed product. Format:
            ``accounts/{account}/products/{product}``
        channel (google.shopping.type.types.Channel.ChannelEnum):
            Immutable. The
            `channel <https://support.google.com/merchants/answer/7361332>`__
            of the product.
        offer_id (str):
            Required. Immutable. Your unique identifier for the product.
            This is the same for the product input and processed
            product. Leading and trailing whitespaces are stripped and
            multiple whitespaces are replaced by a single whitespace
            upon submission. See the `products data
            specification <https://support.google.com/merchants/answer/188494#id>`__
            for details.
        content_language (str):
            Required. Immutable. The two-letter `ISO
            639-1 <http://en.wikipedia.org/wiki/ISO_639-1>`__ language
            code for the product.
        feed_label (str):
            Required. Immutable. The label that lets you categorize and
            identify your products. The maximum allowed characters are
            20, and the supported characters are ``A-Z``, ``0-9``,
            hyphen, and underscore. The feed label must not include any
            spaces. For more information, see `Using feed
            labels <//support.google.com/merchants/answer/14994087>`__.
        version_number (int):
            Optional. Immutable. Represents the existing version
            (freshness) of the product, which can be used to preserve
            the right order when multiple updates are done at the same
            time.

            If set, the insertion is prevented when version number is
            lower than the current version number of the existing
            product. Re-insertion (for example, product refresh after 30
            days) can be performed with the current ``version_number``.

            Only supported for insertions into primary data sources. Do
            not set this field for updates. Do not set this field for
            insertions into supplemental data sources.

            If the operation is prevented, the aborted exception will be
            thrown.

            This field is a member of `oneof`_ ``_version_number``.
        attributes (google.shopping.merchant_products_v1beta.types.Attributes):
            Optional. A list of product attributes.
        custom_attributes (MutableSequence[google.shopping.type.types.CustomAttribute]):
            Optional. A list of custom (merchant-provided) attributes.
            It can also be used for submitting any attribute of the data
            specification in its generic form (for example,
            ``{ "name": "size type", "value": "regular" }``). This is
            useful for submitting attributes not explicitly exposed by
            the API. Maximum allowed number of characters for each
            custom attribute is 10240 (represents sum of characters for
            name and value). Maximum 2500 custom attributes can be set
            per product, with total size of 102.4kB. Underscores in
            custom attribute names are replaced by spaces upon
            insertion.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    product: str = proto.Field(
        proto.STRING,
        number=2,
    )
    channel: types.Channel.ChannelEnum = proto.Field(
        proto.ENUM,
        number=3,
        enum=types.Channel.ChannelEnum,
    )
    offer_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    content_language: str = proto.Field(
        proto.STRING,
        number=5,
    )
    feed_label: str = proto.Field(
        proto.STRING,
        number=6,
    )
    version_number: int = proto.Field(
        proto.INT64,
        number=7,
        optional=True,
    )
    attributes: products_common.Attributes = proto.Field(
        proto.MESSAGE,
        number=8,
        message=products_common.Attributes,
    )
    custom_attributes: MutableSequence[types.CustomAttribute] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message=types.CustomAttribute,
    )


class InsertProductInputRequest(proto.Message):
    r"""Request message for the InsertProductInput method.

    Attributes:
        parent (str):
            Required. The account where this product will be inserted.
            Format: ``accounts/{account}``
        product_input (google.shopping.merchant_products_v1beta.types.ProductInput):
            Required. The product input to insert.
        data_source (str):
            Required. The primary or supplemental product data source
            name. If the product already exists and data source provided
            is different, then the product will be moved to a new data
            source. For more information, see `Overview of Data sources
            sub-API </merchant/api/guides/data-sources/overview>`__.

            Only API data sources are supported.

            Format: ``accounts/{account}/dataSources/{datasource}``. For
            example, ``accounts/123456/dataSources/104628``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    product_input: "ProductInput" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ProductInput",
    )
    data_source: str = proto.Field(
        proto.STRING,
        number=3,
    )


class UpdateProductInputRequest(proto.Message):
    r"""Request message for the UpdateProductInput method.
    The product (primary input) must exist for the update to
    succeed. If the update is for a primary product input, the
    existing primary product input must be from the same data
    source.

    Attributes:
        product_input (google.shopping.merchant_products_v1beta.types.ProductInput):
            Required. The product input resource to
            update. Information you submit will be applied
            to the processed product as well.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of product attributes to be updated.

            If the update mask is omitted, then it is treated as implied
            field mask equivalent to all fields that are populated (have
            a non-empty value).

            Attributes specified in the update mask without a value
            specified in the body will be deleted from the product.

            Update mask can only be specified for top level fields in
            attributes and custom attributes.

            To specify the update mask for custom attributes you need to
            add the ``custom_attribute.`` prefix.

            Providing special "\*" value for full product replacement is
            not supported.
        data_source (str):
            Required. The primary or supplemental product data source
            where ``data_source`` name identifies the product input to
            be updated.

            Only API data sources are supported.

            Format: ``accounts/{account}/dataSources/{datasource}``. For
            example, ``accounts/123456/dataSources/104628``.
    """

    product_input: "ProductInput" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ProductInput",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    data_source: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteProductInputRequest(proto.Message):
    r"""Request message for the DeleteProductInput method.

    Attributes:
        name (str):
            Required. The name of the product input resource to delete.
            Format: ``accounts/{account}/productInputs/{product}`` where
            the last section ``product`` consists of 4 parts:
            ``channel~content_language~feed_label~offer_id`` example for
            product name is
            ``accounts/123/productInputs/online~en~US~sku123``.
        data_source (str):
            Required. The primary or supplemental data source from which
            the product input should be deleted. Format:
            ``accounts/{account}/dataSources/{datasource}``. For
            example, ``accounts/123456/dataSources/104628``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_source: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
