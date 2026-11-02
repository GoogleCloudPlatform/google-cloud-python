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
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore
from google.shopping.type.types import types

from google.shopping.css_v1.types import css_product_common

__protobuf__ = proto.module(
    package="google.shopping.css.v1",
    manifest={
        "CssProductInput",
        "InsertCssProductInputRequest",
        "UpdateCssProductInputRequest",
        "DeleteCssProductInputRequest",
    },
)


class CssProductInput(proto.Message):
    r"""This resource represents input data you submit for a CSS
    Product, not the processed CSS Product that you see in CSS
    Center, in Shopping Ads, or across Google surfaces.

    Attributes:
        name (str):
            Identifier. The name of the CSS Product input. Format:
            ``accounts/{account}/cssProductInputs/{css_product_input}``,
            where the last section ``css_product_input`` consists of 3
            parts: contentLanguage~feedLabel~offerId. Example:
            accounts/123/cssProductInputs/de~DE~rawProvidedId123
        final_name (str):
            Output only. The name of the processed CSS Product. Format:
            ``accounts/{account}/cssProducts/{css_product}`` ".
        raw_provided_id (str):
            Required. Your unique identifier for the CSS Product. This
            is the same for the CSS Product input and processed CSS
            Product. We only allow ids with alphanumerics, underscores
            and dashes. See the `products feed
            specification <https://support.google.com/merchants/answer/188494#id>`__
            for details.
        content_language (str):
            Required. The two-letter `ISO
            639-1 <http://en.wikipedia.org/wiki/ISO_639-1>`__ language
            code for the CSS Product.
        feed_label (str):
            Required. The `feed
            label <https://developers.google.com/shopping-content/guides/products/feed-labels>`__
            for the CSS Product. Feed Label is synonymous to "target
            country" and hence should always be a valid region code. For
            example: 'DE' for Germany, 'FR' for France.
        freshness_time (google.protobuf.timestamp_pb2.Timestamp):
            DEPRECATED. Use expiration_date instead. Represents the
            existing version (freshness) of the CSS Product, which can
            be used to preserve the right order when multiple updates
            are done at the same time.

            This field must not be set to the future time.

            If set, the update is prevented if a newer version of the
            item already exists in our system (that is the last update
            time of the existing CSS products is later than the
            freshness time set in the update). If the update happens,
            the last update time is then set to this freshness time.

            If not set, the update will not be prevented and the last
            update time will default to when this request was received
            by the CSS API.

            If the operation is prevented, the aborted exception will be
            thrown.
        attributes (google.shopping.css_v1.types.Attributes):
            A list of CSS Product attributes.
        custom_attributes (MutableSequence[google.shopping.type.types.CustomAttribute]):
            A list of custom (CSS-provided) attributes. It can also be
            used for submitting any attribute of the feed specification
            in its generic form (for example:
            ``{ "name": "size type", "value": "regular" }``). This is
            useful for submitting attributes not explicitly exposed by
            the API, such as additional attributes used for Buy on
            Google.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    final_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    raw_provided_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    content_language: str = proto.Field(
        proto.STRING,
        number=4,
    )
    feed_label: str = proto.Field(
        proto.STRING,
        number=5,
    )
    freshness_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    attributes: css_product_common.Attributes = proto.Field(
        proto.MESSAGE,
        number=7,
        message=css_product_common.Attributes,
    )
    custom_attributes: MutableSequence[types.CustomAttribute] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message=types.CustomAttribute,
    )


class InsertCssProductInputRequest(proto.Message):
    r"""Request message for the InsertCssProductInput method.

    Attributes:
        parent (str):
            Required. The account where this CSS Product
            will be inserted. Format: accounts/{account}
        css_product_input (google.shopping.css_v1.types.CssProductInput):
            Required. The CSS Product Input to insert.
        feed_id (int):
            Optional. DEPRECATED. Feed id is not required
            for CSS Products. The primary or supplemental
            feed id. If CSS Product already exists and feed
            id provided is different, then the CSS Product
            will be moved to a new feed.
            Note: For now, CSSs do not need to provide feed
            ids as we create feeds on the fly.
            We do not have supplemental feed support for CSS
            Products yet.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    css_product_input: "CssProductInput" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="CssProductInput",
    )
    feed_id: int = proto.Field(
        proto.INT64,
        number=3,
    )


class UpdateCssProductInputRequest(proto.Message):
    r"""Request message for the UpdateCssProductInput method.

    Attributes:
        css_product_input (google.shopping.css_v1.types.CssProductInput):
            Required. The CSS product input resource to
            update. Information you submit will be applied
            to the processed CSS product as well.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of CSS product attributes to be updated.

            If the update mask is omitted, then it is treated as implied
            field mask equivalent to all fields that are populated (have
            a non-empty value).

            Attributes specified in the update mask without a value
            specified in the body will be deleted from the CSS product.

            Update mask can only be specified for top level fields in
            attributes and custom attributes.

            To specify the update mask for custom attributes you need to
            add the ``custom_attribute.`` prefix.

            Providing special "\*" value for full CSS product
            replacement is not supported.
    """

    css_product_input: "CssProductInput" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="CssProductInput",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteCssProductInputRequest(proto.Message):
    r"""Request message for the DeleteCssProductInput method.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. The name of the CSS product input resource to
            delete. Format:
            accounts/{account}/cssProductInputs/{css_product_input},
            where the last section ``css_product_input`` consists of 3
            parts: contentLanguage~feedLabel~offerId. Example:
            accounts/123/cssProductInputs/de~DE~rawProvidedId123
        supplemental_feed_id (int):
            The Content API Supplemental Feed ID.
            The field must not be set if the action applies
            to a primary feed. If the field is set, then
            product action applies to a supplemental feed
            instead of primary Content API feed.

            This field is a member of `oneof`_ ``_supplemental_feed_id``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    supplemental_feed_id: int = proto.Field(
        proto.INT64,
        number=2,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
