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

from google.shopping.merchant_products_v1.types import products_common

__protobuf__ = proto.module(
    package="google.shopping.merchant.products.v1",
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
    [Product][google.shopping.merchant.products.v1.Product]. For more
    information, see `Manage
    products </merchant/api/guides/products/overview>`__.

    Required product input attributes to pass data validation checks are
    primarily defined in the `Products Data
    Specification <https://support.google.com/merchants/answer/188494>`__.

    The following attributes are required:
    [feedLabel][google.shopping.merchant.products.v1.Product.feed_label],
    [contentLanguage][google.shopping.merchant.products.v1.Product.content_language]
    and
    [offerId][google.shopping.merchant.products.v1.Product.offer_id].

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
            Identifier. The name of the product. Format:
            ``accounts/{account}/productInputs/{productinput}``

            The {productinput} segment is a unique identifier for the
            product. This identifier must be unique within a merchant
            account and generally follows the structure:
            ``content_language~feed_label~offer_id``. Example:
            ``en~US~sku123`` For legacy local products, the structure
            is: ``local~content_language~feed_label~offer_id``. Example:
            ``local~en~US~sku123``

            The format of the {productinput} segment in the URL is
            automatically detected by the server, supporting two
            options:

            1. **Encoded Format**: The ``{productinput}`` segment is an
               unpadded base64url encoded string (RFC 4648 Section 5).
               The decoded string must result in the
               ``content_language~feed_label~offer_id`` structure. This
               encoding MUST be used if any part of the product
               identifier (like ``offer_id``) contains characters such
               as ``/``, ``%``, or ``~``.

               - Example: To represent the product ID ``en~US~sku/123``,
                 the ``{productinput}`` segment must be the unpadded
                 base64url encoding of this string, which is
                 ``ZW5-VVN-c2t1LzEyMw``. The full resource name for the
                 product would be
                 ``accounts/123/productInputs/ZW5-VVN-c2t1LzEyMw``.

            2. **Plain Format**: The ``{productinput}`` segment is the
               tilde-separated string
               ``content_language~feed_label~offer_id``. This format is
               suitable only when ``content_language``, ``feed_label``,
               and ``offer_id`` do not contain URL-problematic
               characters like ``/``, ``%``, or ``~``.

            We recommend using the **Encoded Format** for all product
            IDs to ensure correct parsing, especially those containing
            special characters. The presence of tilde (``~``) characters
            in the ``{productinput}`` segment is used to differentiate
            between the two formats.
        base64_encoded_name (str):
            Output only. The **unpadded base64url encoded name** of the
            product input. Format:
            ``accounts/{account}/productInputs/{productinput}`` where
            the last section ``productinput`` is the unpadded base64url
            encoding of the ``content_language~feed_label~offer_id``
            name. Example:
            ``accounts/123/productInputs/ZW5-VVN-c2t1LzEyMw`` for the
            decoded product input name
            ``accounts/123/productInputs/en~US~sku/123``. This field can
            be used directly as input to the API methods that require
            the product input name to be encoded if it contains special
            characters, for example
            ```GetProductInput`` <https://developers.google.com/merchant/api/reference/rest/products_v1/accounts.productInputs/get>`__.
        product (str):
            Output only. The name of the processed product. Format:
            ``accounts/{account}/products/{product}``
        base64_encoded_product (str):
            Output only. The **unpadded base64url encoded name** of the
            processed product. Format:
            ``accounts/{account}/products/{product}`` where the last
            section ``product`` is the unpadded base64url encoding of
            the ``content_language~feed_label~offer_id`` name. Example:
            ``accounts/123/products/ZW5-VVN-c2t1LzEyMw`` for the decoded
            product name ``accounts/123/products/en~US~sku/123``. This
            field can be used directly as input to the API methods that
            require the product name to be encoded if it contains
            special characters, for example
            ```GetProduct`` <https://developers.google.com/merchant/api/reference/rest/products_v1/accounts.products/get>`__.
        legacy_local (bool):
            Immutable. Determines whether the product is **only**
            targeting local destinations and whether the product name
            should be distinguished with a ``local~`` prefix. For
            example, ``accounts/123/productInputs/local~en~US~sku123``.
            If a product that is not ``legacy_local`` is already
            targeting local destinations, creating a ``legacy_local``
            product with an otherwise matching name will fail.
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
            Required. Immutable. The feed label that lets you categorize
            and identify your products. The maximum allowed characters
            are 20, and the supported characters are ``A-Z``, ``0-9``,
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
        product_attributes (google.shopping.merchant_products_v1.types.ProductAttributes):
            Optional. A list of strongly-typed product
            attributes.
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
    base64_encoded_name: str = proto.Field(
        proto.STRING,
        number=12,
    )
    product: str = proto.Field(
        proto.STRING,
        number=2,
    )
    base64_encoded_product: str = proto.Field(
        proto.STRING,
        number=13,
    )
    legacy_local: bool = proto.Field(
        proto.BOOL,
        number=10,
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
    product_attributes: products_common.ProductAttributes = proto.Field(
        proto.MESSAGE,
        number=11,
        message=products_common.ProductAttributes,
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
        product_input (google.shopping.merchant_products_v1.types.ProductInput):
            Required. The product input to insert.
        data_source (str):
            Required. The primary or supplemental product data source
            name. If the product already exists and data source provided
            is different, then the product will be moved to a new data
            source. For more information, see `Create a primary data
            source </merchant/api/guides/data-sources/api-sources#create-primary-data-source>`__.

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
        product_input (google.shopping.merchant_products_v1.types.ProductInput):
            Required. The product input resource to update. Information
            you submit will be applied to the processed product as well.
            The ``name`` field within this resource identifies the
            product input to be updated.
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
            Required. The name of the product input to delete. Format:
            ``accounts/{account}/productInputs/{productInput}``

            The {productInput} segment is a unique identifier for the
            product. This identifier must be unique within a merchant
            account and generally follows the structure:
            ``content_language~feed_label~offer_id``. Example:
            ``en~US~sku123`` For legacy local products, the structure
            is: ``local~content_language~feed_label~offer_id``. Example:
            ``local~en~US~sku123``

            The format of the {productInput} segment in the URL is
            automatically detected by the server, supporting two
            options:

            1. **Encoded Format**: The ``{productInput}`` segment is an
               unpadded base64url encoded string (RFC 4648 Section 5).
               The decoded string must result in the
               ``content_language~feed_label~offer_id`` structure. This
               encoding MUST be used if any part of the product
               identifier (like ``offer_id``) contains characters such
               as ``/``, ``%``, or ``~``.

               - Example: To represent the product ID ``en~US~sku/123``,
                 the ``{productInput}`` segment must be the unpadded
                 base64url encoding of this string, which is
                 ``ZW5-VVN-c2t1LzEyMw``. The full resource name for the
                 product would be
                 ``accounts/123/productInputs/ZW5-VVN-c2t1LzEyMw``.

            2. **Plain Format**: The ``{productInput}`` segment is the
               tilde-separated string
               ``content_language~feed_label~offer_id``. This format is
               suitable only when ``content_language``, ``feed_label``,
               and ``offer_id`` do not contain URL-problematic
               characters like ``/``, ``%``, or ``~``.

            We recommend using the **Encoded Format** for all product
            IDs to ensure correct parsing, especially those containing
            special characters. The presence of tilde (``~``) characters
            in the ``{productInput}`` segment is used to differentiate
            between the two formats.
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
