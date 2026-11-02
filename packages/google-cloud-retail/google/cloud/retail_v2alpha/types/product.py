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

import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.protobuf.wrappers_pb2 as wrappers_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.retail_v2alpha.types import common, promotion

__protobuf__ = proto.module(
    package="google.cloud.retail.v2alpha",
    manifest={
        "Product",
    },
)


class Product(proto.Message):
    r"""Product captures all metadata information of items to be
    recommended or searched.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            Note that this field is applied in the following ways:

            - If the [Product][google.cloud.retail.v2alpha.Product] is
              already expired when it is uploaded, this product is not
              indexed for search.

            - If the [Product][google.cloud.retail.v2alpha.Product] is
              not expired when it is uploaded, only the
              [Type.PRIMARY][google.cloud.retail.v2alpha.Product.Type.PRIMARY]'s
              and
              [Type.COLLECTION][google.cloud.retail.v2alpha.Product.Type.COLLECTION]'s
              expireTime is respected, and
              [Type.VARIANT][google.cloud.retail.v2alpha.Product.Type.VARIANT]'s
              expireTime is not used.

            In general, we suggest the users to delete the stale
            products explicitly, instead of using this field to
            determine staleness.

            [expire_time][google.cloud.retail.v2alpha.Product.expire_time]
            must be later than
            [available_time][google.cloud.retail.v2alpha.Product.available_time]
            and
            [publish_time][google.cloud.retail.v2alpha.Product.publish_time],
            otherwise an INVALID_ARGUMENT error is thrown.

            Corresponding properties: Google Merchant Center property
            `expiration_date <https://support.google.com/merchants/answer/6324499>`__.

            This field is a member of `oneof`_ ``expiration``.
        ttl (google.protobuf.duration_pb2.Duration):
            Input only. The TTL (time to live) of the product. Note that
            this is only applicable to
            [Type.PRIMARY][google.cloud.retail.v2alpha.Product.Type.PRIMARY]
            and
            [Type.COLLECTION][google.cloud.retail.v2alpha.Product.Type.COLLECTION],
            and ignored for
            [Type.VARIANT][google.cloud.retail.v2alpha.Product.Type.VARIANT].
            In general, we suggest the users to delete the stale
            products explicitly, instead of using this field to
            determine staleness.

            If it is set, it must be a non-negative value, and
            [expire_time][google.cloud.retail.v2alpha.Product.expire_time]
            is set as current timestamp plus
            [ttl][google.cloud.retail.v2alpha.Product.ttl]. The derived
            [expire_time][google.cloud.retail.v2alpha.Product.expire_time]
            is returned in the output and
            [ttl][google.cloud.retail.v2alpha.Product.ttl] is left blank
            when retrieving the
            [Product][google.cloud.retail.v2alpha.Product].

            If it is set, the product is not available for
            [SearchService.Search][google.cloud.retail.v2alpha.SearchService.Search]
            after current timestamp plus
            [ttl][google.cloud.retail.v2alpha.Product.ttl]. However, the
            product can still be retrieved by
            [ProductService.GetProduct][google.cloud.retail.v2alpha.ProductService.GetProduct]
            and
            [ProductService.ListProducts][google.cloud.retail.v2alpha.ProductService.ListProducts].

            This field is a member of `oneof`_ ``expiration``.
        name (str):
            Immutable. Full resource name of the product, such as
            ``projects/*/locations/global/catalogs/default_catalog/branches/default_branch/products/product_id``.
        id (str):
            Immutable. [Product][google.cloud.retail.v2alpha.Product]
            identifier, which is the final component of
            [name][google.cloud.retail.v2alpha.Product.name]. For
            example, this field is "id_1", if
            [name][google.cloud.retail.v2alpha.Product.name] is
            ``projects/*/locations/global/catalogs/default_catalog/branches/default_branch/products/id_1``.

            This field must be a UTF-8 encoded string with a length
            limit of 128 characters. Otherwise, an INVALID_ARGUMENT
            error is returned.

            Corresponding properties: Google Merchant Center property
            `id <https://support.google.com/merchants/answer/6324405>`__.
            Schema.org property
            `Product.sku <https://schema.org/sku>`__.
        type_ (google.cloud.retail_v2alpha.types.Product.Type):
            Immutable. The type of the product. Default to
            [Catalog.product_level_config.ingestion_product_type][google.cloud.retail.v2alpha.ProductLevelConfig.ingestion_product_type]
            if unset.
        primary_product_id (str):
            Variant group identifier. Must be an
            [id][google.cloud.retail.v2alpha.Product.id], with the same
            parent branch with this product. Otherwise, an error is
            thrown.

            For
            [Type.PRIMARY][google.cloud.retail.v2alpha.Product.Type.PRIMARY]
            [Product][google.cloud.retail.v2alpha.Product]s, this field
            can only be empty or set to the same value as
            [id][google.cloud.retail.v2alpha.Product.id].

            For VARIANT [Product][google.cloud.retail.v2alpha.Product]s,
            this field cannot be empty. A maximum of 2,000 products are
            allowed to share the same
            [Type.PRIMARY][google.cloud.retail.v2alpha.Product.Type.PRIMARY]
            [Product][google.cloud.retail.v2alpha.Product]. Otherwise,
            an INVALID_ARGUMENT error is returned.

            Corresponding properties: Google Merchant Center property
            `item_group_id <https://support.google.com/merchants/answer/6324507>`__.
            Schema.org property
            `Product.inProductGroupWithID <https://schema.org/inProductGroupWithID>`__.
        collection_member_ids (MutableSequence[str]):
            The [id][google.cloud.retail.v2alpha.Product.id] of the
            collection members when
            [type][google.cloud.retail.v2alpha.Product.type] is
            [Type.COLLECTION][google.cloud.retail.v2alpha.Product.Type.COLLECTION].

            Non-existent product ids are allowed. The
            [type][google.cloud.retail.v2alpha.Product.type] of the
            members must be either
            [Type.PRIMARY][google.cloud.retail.v2alpha.Product.Type.PRIMARY]
            or
            [Type.VARIANT][google.cloud.retail.v2alpha.Product.Type.VARIANT]
            otherwise an INVALID_ARGUMENT error is thrown. Should not
            set it for other types. A maximum of 1000 values are
            allowed. Otherwise, an INVALID_ARGUMENT error is return.
        gtin (str):
            The Global Trade Item Number (GTIN) of the product.

            This field must be a UTF-8 encoded string with a length
            limit of 128 characters. Otherwise, an INVALID_ARGUMENT
            error is returned.

            This field must be a Unigram. Otherwise, an INVALID_ARGUMENT
            error is returned.

            Corresponding properties: Google Merchant Center property
            `gtin <https://support.google.com/merchants/answer/6324461>`__.
            Schema.org property
            `Product.isbn <https://schema.org/isbn>`__,
            `Product.gtin8 <https://schema.org/gtin8>`__,
            `Product.gtin12 <https://schema.org/gtin12>`__,
            `Product.gtin13 <https://schema.org/gtin13>`__, or
            `Product.gtin14 <https://schema.org/gtin14>`__.

            If the value is not a valid GTIN, an INVALID_ARGUMENT error
            is returned.
        categories (MutableSequence[str]):
            Product categories. This field is repeated for supporting
            one product belonging to several parallel categories.
            Strongly recommended using the full path for better search /
            recommendation quality.

            To represent full path of category, use '>' sign to separate
            different hierarchies. If '>' is part of the category name,
            replace it with other character(s).

            For example, if a shoes product belongs to both ["Shoes &
            Accessories" -> "Shoes"] and ["Sports & Fitness" ->
            "Athletic Clothing" -> "Shoes"], it could be represented as:

            ::

                 "categories": [
                   "Shoes & Accessories > Shoes",
                   "Sports & Fitness > Athletic Clothing > Shoes"
                 ]

            Must be set for
            [Type.PRIMARY][google.cloud.retail.v2alpha.Product.Type.PRIMARY]
            [Product][google.cloud.retail.v2alpha.Product] otherwise an
            INVALID_ARGUMENT error is returned.

            At most 250 values are allowed per
            [Product][google.cloud.retail.v2alpha.Product] unless
            overridden through the Google Cloud console. Empty values
            are not allowed. Each value must be a UTF-8 encoded string
            with a length limit of 5,000 characters. Otherwise, an
            INVALID_ARGUMENT error is returned.

            Corresponding properties: Google Merchant Center property
            `google_product_category <https://support.google.com/merchants/answer/6324436>`__.
            Schema.org property [Product.category]
            (https://schema.org/category).
        title (str):
            Required. Product title.

            This field must be a UTF-8 encoded string with a length
            limit of 1,000 characters. Otherwise, an INVALID_ARGUMENT
            error is returned.

            Corresponding properties: Google Merchant Center property
            `title <https://support.google.com/merchants/answer/6324415>`__.
            Schema.org property
            `Product.name <https://schema.org/name>`__.
        brands (MutableSequence[str]):
            The brands of the product.

            A maximum of 30 brands are allowed unless overridden through
            the Google Cloud console. Each brand must be a UTF-8 encoded
            string with a length limit of 1,000 characters. Otherwise,
            an INVALID_ARGUMENT error is returned.

            Corresponding properties: Google Merchant Center property
            `brand <https://support.google.com/merchants/answer/6324351>`__.
            Schema.org property
            `Product.brand <https://schema.org/brand>`__.
        description (str):
            Product description.

            This field must be a UTF-8 encoded string with a length
            limit of 5,000 characters. Otherwise, an INVALID_ARGUMENT
            error is returned.

            Corresponding properties: Google Merchant Center property
            `description <https://support.google.com/merchants/answer/6324468>`__.
            Schema.org property
            `Product.description <https://schema.org/description>`__.
        language_code (str):
            Language of the title/description and other string
            attributes. Use language tags defined by `BCP
            47 <https://www.rfc-editor.org/rfc/bcp/bcp47.txt>`__.

            For product prediction, this field is ignored and the model
            automatically detects the text language. The
            [Product][google.cloud.retail.v2alpha.Product] can include
            text in different languages, but duplicating
            [Product][google.cloud.retail.v2alpha.Product]s to provide
            text in multiple languages can result in degraded model
            performance.

            For product search this field is in use. It defaults to
            "en-US" if unset.
        attributes (MutableMapping[str, google.cloud.retail_v2alpha.types.CustomAttribute]):
            Highly encouraged. Extra product attributes to be included.
            For example, for products, this could include the store
            name, vendor, style, color, etc. These are very strong
            signals for recommendation model, thus we highly recommend
            providing the attributes here.

            Features that can take on one of a limited number of
            possible values. Two types of features can be set are:

            Textual features. some examples would be the brand/maker of
            a product, or country of a customer. Numerical features.
            Some examples would be the height/weight of a product, or
            age of a customer.

            For example:
            ``{ "vendor": {"text": ["vendor123", "vendor456"]}, "lengths_cm": {"numbers":[2.3, 15.4]}, "heights_cm": {"numbers":[8.1, 6.4]} }``.

            This field needs to pass all below criteria, otherwise an
            INVALID_ARGUMENT error is returned:

            - Max entries count: 200.
            - The key must be a UTF-8 encoded string with a length limit
              of 128 characters.
            - For indexable attribute, the key must match the pattern:
              ``[a-zA-Z0-9][a-zA-Z0-9_]*``. For example,
              ``key0LikeThis`` or ``KEY_1_LIKE_THIS``.
            - For text attributes, at most 400 values are allowed. Empty
              values are not allowed. Each value must be a non-empty
              UTF-8 encoded string with a length limit of 256
              characters.
            - For number attributes, at most 400 values are allowed.
        tags (MutableSequence[str]):
            Custom tags associated with the product.

            At most 250 values are allowed per
            [Product][google.cloud.retail.v2alpha.Product]. This value
            must be a UTF-8 encoded string with a length limit of 1,000
            characters. Otherwise, an INVALID_ARGUMENT error is
            returned.

            This tag can be used for filtering recommendation results by
            passing the tag as part of the
            [PredictRequest.filter][google.cloud.retail.v2alpha.PredictRequest.filter].

            Corresponding properties: Google Merchant Center property
            `custom_label_0–4 <https://support.google.com/merchants/answer/6324473>`__.
        price_info (google.cloud.retail_v2alpha.types.PriceInfo):
            Product price and cost information.

            Corresponding properties: Google Merchant Center property
            `price <https://support.google.com/merchants/answer/6324371>`__.
        rating (google.cloud.retail_v2alpha.types.Rating):
            The rating of this product.
        available_time (google.protobuf.timestamp_pb2.Timestamp):
            The timestamp when this
            [Product][google.cloud.retail.v2alpha.Product] becomes
            available for
            [SearchService.Search][google.cloud.retail.v2alpha.SearchService.Search].
            Note that this is only applicable to
            [Type.PRIMARY][google.cloud.retail.v2alpha.Product.Type.PRIMARY]
            and
            [Type.COLLECTION][google.cloud.retail.v2alpha.Product.Type.COLLECTION],
            and ignored for
            [Type.VARIANT][google.cloud.retail.v2alpha.Product.Type.VARIANT].
        availability (google.cloud.retail_v2alpha.types.Product.Availability):
            The online availability of the
            [Product][google.cloud.retail.v2alpha.Product]. Default to
            [Availability.IN_STOCK][google.cloud.retail.v2alpha.Product.Availability.IN_STOCK].

            For primary products with variants set the availability of
            the primary as
            [Availability.OUT_OF_STOCK][google.cloud.retail.v2alpha.Product.Availability.OUT_OF_STOCK]
            and set the true availability at the variant level. This way
            the primary product will be considered "in stock" as long as
            it has at least one variant in stock.

            For primary products with no variants set the true
            availability at the primary level.

            Corresponding properties: Google Merchant Center property
            `availability <https://support.google.com/merchants/answer/6324448>`__.
            Schema.org property
            `Offer.availability <https://schema.org/availability>`__.
        available_quantity (google.protobuf.wrappers_pb2.Int32Value):
            The available quantity of the item.
        fulfillment_info (MutableSequence[google.cloud.retail_v2alpha.types.FulfillmentInfo]):
            Fulfillment information, such as the store IDs for in-store
            pickup or region IDs for different shipping methods.

            All the elements must have distinct
            [FulfillmentInfo.type][google.cloud.retail.v2alpha.FulfillmentInfo.type].
            Otherwise, an INVALID_ARGUMENT error is returned.
        uri (str):
            Canonical URL directly linking to the product detail page.

            It is strongly recommended to provide a valid uri for the
            product, otherwise the service performance could be
            significantly degraded.

            This field must be a UTF-8 encoded string with a length
            limit of 5,000 characters. Otherwise, an INVALID_ARGUMENT
            error is returned.

            Corresponding properties: Google Merchant Center property
            `link <https://support.google.com/merchants/answer/6324416>`__.
            Schema.org property `Offer.url <https://schema.org/url>`__.
        images (MutableSequence[google.cloud.retail_v2alpha.types.Image]):
            Product images for the product. We highly recommend putting
            the main image first.

            A maximum of 300 images are allowed.

            Corresponding properties: Google Merchant Center property
            `image_link <https://support.google.com/merchants/answer/6324350>`__.
            Schema.org property
            `Product.image <https://schema.org/image>`__.
        audience (google.cloud.retail_v2alpha.types.Audience):
            The target group associated with a given
            audience (e.g. male, veterans, car owners,
            musicians, etc.) of the product.
        color_info (google.cloud.retail_v2alpha.types.ColorInfo):
            The color of the product.

            Corresponding properties: Google Merchant Center property
            `color <https://support.google.com/merchants/answer/6324487>`__.
            Schema.org property
            `Product.color <https://schema.org/color>`__.
        sizes (MutableSequence[str]):
            The size of the product. To represent different size systems
            or size types, consider using this format:
            [[[size_system:]size_type:]size_value].

            For example, in "US:MENS:M", "US" represents size system;
            "MENS" represents size type; "M" represents size value. In
            "GIRLS:27", size system is empty; "GIRLS" represents size
            type; "27" represents size value. In "32 inches", both size
            system and size type are empty, while size value is "32
            inches".

            A maximum of 20 values are allowed per
            [Product][google.cloud.retail.v2alpha.Product]. Each value
            must be a UTF-8 encoded string with a length limit of 128
            characters. Otherwise, an INVALID_ARGUMENT error is
            returned.

            Corresponding properties: Google Merchant Center property
            `size <https://support.google.com/merchants/answer/6324492>`__,
            `size_type <https://support.google.com/merchants/answer/6324497>`__,
            and
            `size_system <https://support.google.com/merchants/answer/6324502>`__.
            Schema.org property
            `Product.size <https://schema.org/size>`__.
        materials (MutableSequence[str]):
            The material of the product. For example, "leather",
            "wooden".

            A maximum of 20 values are allowed. Each value must be a
            UTF-8 encoded string with a length limit of 200 characters.
            Otherwise, an INVALID_ARGUMENT error is returned.

            Corresponding properties: Google Merchant Center property
            `material <https://support.google.com/merchants/answer/6324410>`__.
            Schema.org property
            `Product.material <https://schema.org/material>`__.
        patterns (MutableSequence[str]):
            The pattern or graphic print of the product. For example,
            "striped", "polka dot", "paisley".

            A maximum of 20 values are allowed per
            [Product][google.cloud.retail.v2alpha.Product]. Each value
            must be a UTF-8 encoded string with a length limit of 128
            characters. Otherwise, an INVALID_ARGUMENT error is
            returned.

            Corresponding properties: Google Merchant Center property
            `pattern <https://support.google.com/merchants/answer/6324483>`__.
            Schema.org property
            `Product.pattern <https://schema.org/pattern>`__.
        conditions (MutableSequence[str]):
            The condition of the product. Strongly encouraged to use the
            standard values: "new", "refurbished", "used".

            A maximum of 1 value is allowed per
            [Product][google.cloud.retail.v2alpha.Product]. Each value
            must be a UTF-8 encoded string with a length limit of 128
            characters. Otherwise, an INVALID_ARGUMENT error is
            returned.

            Corresponding properties: Google Merchant Center property
            `condition <https://support.google.com/merchants/answer/6324469>`__.
            Schema.org property
            `Offer.itemCondition <https://schema.org/itemCondition>`__.
        promotions (MutableSequence[google.cloud.retail_v2alpha.types.Promotion]):
            The promotions applied to the product. A maximum of 10
            values are allowed per
            [Product][google.cloud.retail.v2alpha.Product]. Only
            [Promotion.promotion_id][google.cloud.retail.v2alpha.Promotion.promotion_id]
            will be used, other fields will be ignored if set.
        publish_time (google.protobuf.timestamp_pb2.Timestamp):
            The timestamp when the product is published by the retailer
            for the first time, which indicates the freshness of the
            products. Note that this field is different from
            [available_time][google.cloud.retail.v2alpha.Product.available_time],
            given it purely describes product freshness regardless of
            when it is available on search and recommendation.
        retrievable_fields (google.protobuf.field_mask_pb2.FieldMask):
            Indicates which fields in the
            [Product][google.cloud.retail.v2alpha.Product]s are returned
            in
            [SearchResponse][google.cloud.retail.v2alpha.SearchResponse].

            Supported fields for all
            [type][google.cloud.retail.v2alpha.Product.type]s:

            - [audience][google.cloud.retail.v2alpha.Product.audience]
            - [availability][google.cloud.retail.v2alpha.Product.availability]
            - [brands][google.cloud.retail.v2alpha.Product.brands]
            - [color_info][google.cloud.retail.v2alpha.Product.color_info]
            - [conditions][google.cloud.retail.v2alpha.Product.conditions]
            - [gtin][google.cloud.retail.v2alpha.Product.gtin]
            - [materials][google.cloud.retail.v2alpha.Product.materials]
            - [name][google.cloud.retail.v2alpha.Product.name]
            - [patterns][google.cloud.retail.v2alpha.Product.patterns]
            - [price_info][google.cloud.retail.v2alpha.Product.price_info]
            - [rating][google.cloud.retail.v2alpha.Product.rating]
            - [sizes][google.cloud.retail.v2alpha.Product.sizes]
            - [title][google.cloud.retail.v2alpha.Product.title]
            - [uri][google.cloud.retail.v2alpha.Product.uri]

            Supported fields only for
            [Type.PRIMARY][google.cloud.retail.v2alpha.Product.Type.PRIMARY]
            and
            [Type.COLLECTION][google.cloud.retail.v2alpha.Product.Type.COLLECTION]:

            - [categories][google.cloud.retail.v2alpha.Product.categories]
            - [description][google.cloud.retail.v2alpha.Product.description]
            - [images][google.cloud.retail.v2alpha.Product.images]

            Supported fields only for
            [Type.VARIANT][google.cloud.retail.v2alpha.Product.Type.VARIANT]:

            - Only the first image in
              [images][google.cloud.retail.v2alpha.Product.images]

            To mark
            [attributes][google.cloud.retail.v2alpha.Product.attributes]
            as retrievable, include paths of the form "attributes.key"
            where "key" is the key of a custom attribute, as specified
            in
            [attributes][google.cloud.retail.v2alpha.Product.attributes].

            For
            [Type.PRIMARY][google.cloud.retail.v2alpha.Product.Type.PRIMARY]
            and
            [Type.COLLECTION][google.cloud.retail.v2alpha.Product.Type.COLLECTION],
            the following fields are always returned in
            [SearchResponse][google.cloud.retail.v2alpha.SearchResponse]
            by default:

            - [name][google.cloud.retail.v2alpha.Product.name]

            For
            [Type.VARIANT][google.cloud.retail.v2alpha.Product.Type.VARIANT],
            the following fields are always returned in by default:

            - [name][google.cloud.retail.v2alpha.Product.name]
            - [color_info][google.cloud.retail.v2alpha.Product.color_info]

            Note: Returning more fields in
            [SearchResponse][google.cloud.retail.v2alpha.SearchResponse]
            can increase response payload size and serving latency.

            This field is deprecated. Use the retrievable site-wide
            control instead.
        variants (MutableSequence[google.cloud.retail_v2alpha.types.Product]):
            Output only. Product variants grouped together on primary
            product which share similar product attributes. It's
            automatically grouped by
            [primary_product_id][google.cloud.retail.v2alpha.Product.primary_product_id]
            for all the product variants. Only populated for
            [Type.PRIMARY][google.cloud.retail.v2alpha.Product.Type.PRIMARY]
            [Product][google.cloud.retail.v2alpha.Product]s.

            Note: This field is OUTPUT_ONLY for
            [ProductService.GetProduct][google.cloud.retail.v2alpha.ProductService.GetProduct].
            Do not set this field in API requests.
        local_inventories (MutableSequence[google.cloud.retail_v2alpha.types.LocalInventory]):
            Output only. A list of local inventories specific to
            different places.

            This field can be managed by
            [ProductService.AddLocalInventories][google.cloud.retail.v2alpha.ProductService.AddLocalInventories]
            and
            [ProductService.RemoveLocalInventories][google.cloud.retail.v2alpha.ProductService.RemoveLocalInventories]
            APIs if fine-grained, high-volume updates are necessary.
    """

    class Type(proto.Enum):
        r"""The type of this product.

        Values:
            TYPE_UNSPECIFIED (0):
                Default value. Default to
                [Catalog.product_level_config.ingestion_product_type][google.cloud.retail.v2alpha.ProductLevelConfig.ingestion_product_type]
                if unset.
            PRIMARY (1):
                The primary type.

                As the primary unit for predicting, indexing and search
                serving, a
                [Type.PRIMARY][google.cloud.retail.v2alpha.Product.Type.PRIMARY]
                [Product][google.cloud.retail.v2alpha.Product] is grouped
                with multiple
                [Type.VARIANT][google.cloud.retail.v2alpha.Product.Type.VARIANT]
                [Product][google.cloud.retail.v2alpha.Product]s.
            VARIANT (2):
                The variant type.

                [Type.VARIANT][google.cloud.retail.v2alpha.Product.Type.VARIANT]
                [Product][google.cloud.retail.v2alpha.Product]s usually
                share some common attributes on the same
                [Type.PRIMARY][google.cloud.retail.v2alpha.Product.Type.PRIMARY]
                [Product][google.cloud.retail.v2alpha.Product]s, but they
                have variant attributes like different colors, sizes and
                prices, etc.
            COLLECTION (3):
                The collection type. Collection products are bundled
                [Type.PRIMARY][google.cloud.retail.v2alpha.Product.Type.PRIMARY]
                [Product][google.cloud.retail.v2alpha.Product]s or
                [Type.VARIANT][google.cloud.retail.v2alpha.Product.Type.VARIANT]
                [Product][google.cloud.retail.v2alpha.Product]s that are
                sold together, such as a jewelry set with necklaces,
                earrings and rings, etc.
        """

        TYPE_UNSPECIFIED = 0
        PRIMARY = 1
        VARIANT = 2
        COLLECTION = 3

    class Availability(proto.Enum):
        r"""Product availability. If this field is unspecified, the
        product is assumed to be in stock.

        Values:
            AVAILABILITY_UNSPECIFIED (0):
                Default product availability. Default to
                [Availability.IN_STOCK][google.cloud.retail.v2alpha.Product.Availability.IN_STOCK]
                if unset.
            IN_STOCK (1):
                Product in stock.
            OUT_OF_STOCK (2):
                Product out of stock.
            PREORDER (3):
                Product that is in pre-order state.
            BACKORDER (4):
                Product that is back-ordered (i.e.
                temporarily out of stock).
        """

        AVAILABILITY_UNSPECIFIED = 0
        IN_STOCK = 1
        OUT_OF_STOCK = 2
        PREORDER = 3
        BACKORDER = 4

    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=16,
        oneof="expiration",
        message=timestamp_pb2.Timestamp,
    )
    ttl: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=17,
        oneof="expiration",
        message=duration_pb2.Duration,
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=3,
        enum=Type,
    )
    primary_product_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    collection_member_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    gtin: str = proto.Field(
        proto.STRING,
        number=6,
    )
    categories: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    title: str = proto.Field(
        proto.STRING,
        number=8,
    )
    brands: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=9,
    )
    description: str = proto.Field(
        proto.STRING,
        number=10,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=11,
    )
    attributes: MutableMapping[str, common.CustomAttribute] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=12,
        message=common.CustomAttribute,
    )
    tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=13,
    )
    price_info: common.PriceInfo = proto.Field(
        proto.MESSAGE,
        number=14,
        message=common.PriceInfo,
    )
    rating: common.Rating = proto.Field(
        proto.MESSAGE,
        number=15,
        message=common.Rating,
    )
    available_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=18,
        message=timestamp_pb2.Timestamp,
    )
    availability: Availability = proto.Field(
        proto.ENUM,
        number=19,
        enum=Availability,
    )
    available_quantity: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=20,
        message=wrappers_pb2.Int32Value,
    )
    fulfillment_info: MutableSequence[common.FulfillmentInfo] = proto.RepeatedField(
        proto.MESSAGE,
        number=21,
        message=common.FulfillmentInfo,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=22,
    )
    images: MutableSequence[common.Image] = proto.RepeatedField(
        proto.MESSAGE,
        number=23,
        message=common.Image,
    )
    audience: common.Audience = proto.Field(
        proto.MESSAGE,
        number=24,
        message=common.Audience,
    )
    color_info: common.ColorInfo = proto.Field(
        proto.MESSAGE,
        number=25,
        message=common.ColorInfo,
    )
    sizes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=26,
    )
    materials: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=27,
    )
    patterns: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=28,
    )
    conditions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=29,
    )
    promotions: MutableSequence[promotion.Promotion] = proto.RepeatedField(
        proto.MESSAGE,
        number=34,
        message=promotion.Promotion,
    )
    publish_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=33,
        message=timestamp_pb2.Timestamp,
    )
    retrievable_fields: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=30,
        message=field_mask_pb2.FieldMask,
    )
    variants: MutableSequence["Product"] = proto.RepeatedField(
        proto.MESSAGE,
        number=31,
        message="Product",
    )
    local_inventories: MutableSequence[common.LocalInventory] = proto.RepeatedField(
        proto.MESSAGE,
        number=35,
        message=common.LocalInventory,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
