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
from google.shopping.type.types import types

__protobuf__ = proto.module(
    package="google.shopping.css.v1",
    manifest={
        "SubscriptionPeriod",
        "Attributes",
        "Certification",
        "ProductDetail",
        "ProductDimension",
        "ProductWeight",
        "CssProductStatus",
        "HeadlineOfferSubscriptionCost",
        "HeadlineOfferInstallment",
    },
)


class SubscriptionPeriod(proto.Enum):
    r"""The subscription period of the product.

    Values:
        SUBSCRIPTION_PERIOD_UNSPECIFIED (0):
            Indicates that the subscription period is
            unspecified.
        MONTH (1):
            Indicates that the subscription period is
            month.
        YEAR (2):
            Indicates that the subscription period is
            year.
    """

    SUBSCRIPTION_PERIOD_UNSPECIFIED = 0
    MONTH = 1
    YEAR = 2


class Attributes(proto.Message):
    r"""Attributes for CSS Product.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        cpp_link (str):
            URL directly linking to your the Product
            Detail Page of the CSS.

            This field is a member of `oneof`_ ``_cpp_link``.
        cpp_mobile_link (str):
            URL for the mobile-optimized version of the
            Product Detail Page of the CSS.

            This field is a member of `oneof`_ ``_cpp_mobile_link``.
        cpp_ads_redirect (str):
            Allows advertisers to override the item URL
            when the product is shown within the context of
            Product Ads.

            This field is a member of `oneof`_ ``_cpp_ads_redirect``.
        low_price (google.shopping.type.types.Price):
            Low Price of the CSS Product.
        high_price (google.shopping.type.types.Price):
            High Price of the CSS Product.
        number_of_offers (int):
            The number of CSS Products.

            This field is a member of `oneof`_ ``_number_of_offers``.
        headline_offer_condition (str):
            Condition of the headline offer.

            This field is a member of `oneof`_ ``_headline_offer_condition``.
        headline_offer_price (google.shopping.type.types.Price):
            Headline Price of the CSS Product.
        headline_offer_link (str):
            Link to the headline offer.

            This field is a member of `oneof`_ ``_headline_offer_link``.
        headline_offer_mobile_link (str):
            Mobile Link to the headline offer.

            This field is a member of `oneof`_ ``_headline_offer_mobile_link``.
        headline_offer_shipping_price (google.shopping.type.types.Price):
            Headline Price of the CSS Product.
        title (str):
            Title of the item.

            This field is a member of `oneof`_ ``_title``.
        image_link (str):
            URL of an image of the item.

            This field is a member of `oneof`_ ``_image_link``.
        additional_image_links (MutableSequence[str]):
            Additional URL of images of the item.
        description (str):
            Description of the item.

            This field is a member of `oneof`_ ``_description``.
        brand (str):
            Product Related Attributes.[14-36] Brand of the item.

            This field is a member of `oneof`_ ``_brand``.
        mpn (str):
            Manufacturer Part Number
            (`MPN <https://support.google.com/merchants/answer/188494#mpn>`__)
            of the item.

            This field is a member of `oneof`_ ``_mpn``.
        gtin (str):
            Global Trade Item Number
            (`GTIN <https://support.google.com/merchants/answer/188494#gtin>`__)
            of the item.

            This field is a member of `oneof`_ ``_gtin``.
        product_types (MutableSequence[str]):
            Categories of the item (formatted as in `products data
            specification <https://support.google.com/merchants/answer/6324406>`__).
        google_product_category (str):
            Google's category of the item (see `Google product
            taxonomy <https://support.google.com/merchants/answer/1705911>`__).
            When querying products, this field will contain the user
            provided value. There is currently no way to get back the
            auto assigned google product categories through the API.

            This field is a member of `oneof`_ ``_google_product_category``.
        adult (bool):
            Set to true if the item is targeted towards
            adults.

            This field is a member of `oneof`_ ``_adult``.
        multipack (int):
            The number of identical products in a
            merchant-defined multipack.

            This field is a member of `oneof`_ ``_multipack``.
        is_bundle (bool):
            Whether the item is a merchant-defined
            bundle. A bundle is a custom grouping of
            different products sold by a merchant for a
            single price.

            This field is a member of `oneof`_ ``_is_bundle``.
        age_group (str):
            Target age group of the item.

            This field is a member of `oneof`_ ``_age_group``.
        color (str):
            Color of the item.

            This field is a member of `oneof`_ ``_color``.
        gender (str):
            Target gender of the item.

            This field is a member of `oneof`_ ``_gender``.
        material (str):
            The material of which the item is made.

            This field is a member of `oneof`_ ``_material``.
        pattern (str):
            The item's pattern (e.g. polka dots).

            This field is a member of `oneof`_ ``_pattern``.
        size (str):
            Size of the item. Only one value is allowed. For variants
            with different sizes, insert a separate product for each
            size with the same ``itemGroupId`` value (see
            [https://support.google.com/merchants/answer/6324492](size
            definition)).

            This field is a member of `oneof`_ ``_size``.
        size_system (str):
            System in which the size is specified.
            Recommended for apparel items.

            This field is a member of `oneof`_ ``_size_system``.
        size_types (MutableSequence[str]):
            The cut of the item. It can be used to represent combined
            size types for apparel items. Maximum two of size types can
            be provided (see `size
            type <https://support.google.com/merchants/answer/6324497>`__.
        item_group_id (str):
            Shared identifier for all variants of the
            same product.

            This field is a member of `oneof`_ ``_item_group_id``.
        product_details (MutableSequence[google.shopping.css_v1.types.ProductDetail]):
            Technical specification or additional product
            details.
        product_weight (google.shopping.css_v1.types.ProductWeight):
            The weight of the product in the units
            provided. The value must be between 0
            (exclusive) and 2000 (inclusive).
        product_length (google.shopping.css_v1.types.ProductDimension):
            The length of the product in the units
            provided. The value must be between 0
            (exclusive) and 3000 (inclusive).
        product_width (google.shopping.css_v1.types.ProductDimension):
            The width of the product in the units
            provided. The value must be between 0
            (exclusive) and 3000 (inclusive).
        product_height (google.shopping.css_v1.types.ProductDimension):
            The height of the product in the units
            provided. The value must be between
            0 (exclusive) and 3000 (inclusive).
        product_highlights (MutableSequence[str]):
            Bullet points describing the most relevant
            highlights of a product.
        certifications (MutableSequence[google.shopping.css_v1.types.Certification]):
            A list of certificates claimed by the CSS for
            the given product.
        expiration_date (google.protobuf.timestamp_pb2.Timestamp):
            Date on which the item should expire, as specified upon
            insertion, in `ISO
            8601 <http://en.wikipedia.org/wiki/ISO_8601>`__ format. The
            actual expiration date is exposed in ``productstatuses`` as
            `googleExpirationDate <https://support.google.com/merchants/answer/6324499>`__
            and might be earlier if ``expirationDate`` is too far in the
            future. Note: It may take 2+ days from the expiration date
            for the item to actually get deleted.
        included_destinations (MutableSequence[str]):
            The list of destinations to include for this target
            (corresponds to checked check boxes in Merchant Center).
            Default destinations are always included unless provided in
            ``excludedDestinations``.
        excluded_destinations (MutableSequence[str]):
            The list of destinations to exclude for this
            target (corresponds to unchecked check boxes in
            Merchant Center).
        pause (str):
            Publication of this item will be temporarily
            paused.

            This field is a member of `oneof`_ ``_pause``.
        custom_label_0 (str):
            Custom label 0 for custom grouping of items
            in a Shopping campaign.

            This field is a member of `oneof`_ ``_custom_label_0``.
        custom_label_1 (str):
            Custom label 1 for custom grouping of items
            in a Shopping campaign.

            This field is a member of `oneof`_ ``_custom_label_1``.
        custom_label_2 (str):
            Custom label 2 for custom grouping of items
            in a Shopping campaign.

            This field is a member of `oneof`_ ``_custom_label_2``.
        custom_label_3 (str):
            Custom label 3 for custom grouping of items
            in a Shopping campaign.

            This field is a member of `oneof`_ ``_custom_label_3``.
        custom_label_4 (str):
            Custom label 4 for custom grouping of items
            in a Shopping campaign.

            This field is a member of `oneof`_ ``_custom_label_4``.
        headline_offer_installment (google.shopping.css_v1.types.HeadlineOfferInstallment):
            Number and amount of installments to pay for
            an item.
        headline_offer_subscription_cost (google.shopping.css_v1.types.HeadlineOfferSubscriptionCost):
            Number of periods (months or years) and
            amount of payment per period for an item with an
            associated subscription contract.
        review_count (int):
            Number of reviews of the product. Required if
            [``rating``][google.shopping.css.v1.Attributes.rating] is
            provided. This field is for an upcoming feature and is not
            yet used.

            This field is a member of `oneof`_ ``_review_count``.
        min_rating (int):
            Minimum rating score of the product. Required if
            [``rating``][google.shopping.css.v1.Attributes.rating] is
            provided. This field is for an upcoming feature and is not
            yet used.

            This field is a member of `oneof`_ ``_min_rating``.
        max_rating (int):
            Maximum rating score of the product. Required if
            [``rating``][google.shopping.css.v1.Attributes.rating] is
            provided. This field is for an upcoming feature and is not
            yet used.

            This field is a member of `oneof`_ ``_max_rating``.
        rating (float):
            Average rating score of the product. The value must be
            within the range of [``min_rating``, ``max_rating``],
            inclusive. When displayed on the product page, this rating
            is normalized to a scale of [1, 5] with one decimal place.
            If provided,
            [``review_count``][google.shopping.css.v1.Attributes.review_count],
            [``min_rating``][google.shopping.css.v1.Attributes.min_rating],
            and
            [``max_rating``][google.shopping.css.v1.Attributes.max_rating]
            are also required. This field is for an upcoming feature and
            is not yet used.

            This field is a member of `oneof`_ ``_rating``.
    """

    cpp_link: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    cpp_mobile_link: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    cpp_ads_redirect: str = proto.Field(
        proto.STRING,
        number=42,
        optional=True,
    )
    low_price: types.Price = proto.Field(
        proto.MESSAGE,
        number=3,
        message=types.Price,
    )
    high_price: types.Price = proto.Field(
        proto.MESSAGE,
        number=4,
        message=types.Price,
    )
    number_of_offers: int = proto.Field(
        proto.INT64,
        number=5,
        optional=True,
    )
    headline_offer_condition: str = proto.Field(
        proto.STRING,
        number=6,
        optional=True,
    )
    headline_offer_price: types.Price = proto.Field(
        proto.MESSAGE,
        number=7,
        message=types.Price,
    )
    headline_offer_link: str = proto.Field(
        proto.STRING,
        number=8,
        optional=True,
    )
    headline_offer_mobile_link: str = proto.Field(
        proto.STRING,
        number=9,
        optional=True,
    )
    headline_offer_shipping_price: types.Price = proto.Field(
        proto.MESSAGE,
        number=41,
        message=types.Price,
    )
    title: str = proto.Field(
        proto.STRING,
        number=10,
        optional=True,
    )
    image_link: str = proto.Field(
        proto.STRING,
        number=11,
        optional=True,
    )
    additional_image_links: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=12,
    )
    description: str = proto.Field(
        proto.STRING,
        number=13,
        optional=True,
    )
    brand: str = proto.Field(
        proto.STRING,
        number=14,
        optional=True,
    )
    mpn: str = proto.Field(
        proto.STRING,
        number=15,
        optional=True,
    )
    gtin: str = proto.Field(
        proto.STRING,
        number=16,
        optional=True,
    )
    product_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=36,
    )
    google_product_category: str = proto.Field(
        proto.STRING,
        number=17,
        optional=True,
    )
    adult: bool = proto.Field(
        proto.BOOL,
        number=18,
        optional=True,
    )
    multipack: int = proto.Field(
        proto.INT64,
        number=19,
        optional=True,
    )
    is_bundle: bool = proto.Field(
        proto.BOOL,
        number=20,
        optional=True,
    )
    age_group: str = proto.Field(
        proto.STRING,
        number=21,
        optional=True,
    )
    color: str = proto.Field(
        proto.STRING,
        number=22,
        optional=True,
    )
    gender: str = proto.Field(
        proto.STRING,
        number=23,
        optional=True,
    )
    material: str = proto.Field(
        proto.STRING,
        number=24,
        optional=True,
    )
    pattern: str = proto.Field(
        proto.STRING,
        number=25,
        optional=True,
    )
    size: str = proto.Field(
        proto.STRING,
        number=26,
        optional=True,
    )
    size_system: str = proto.Field(
        proto.STRING,
        number=27,
        optional=True,
    )
    size_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=28,
    )
    item_group_id: str = proto.Field(
        proto.STRING,
        number=29,
        optional=True,
    )
    product_details: MutableSequence["ProductDetail"] = proto.RepeatedField(
        proto.MESSAGE,
        number=30,
        message="ProductDetail",
    )
    product_weight: "ProductWeight" = proto.Field(
        proto.MESSAGE,
        number=31,
        message="ProductWeight",
    )
    product_length: "ProductDimension" = proto.Field(
        proto.MESSAGE,
        number=32,
        message="ProductDimension",
    )
    product_width: "ProductDimension" = proto.Field(
        proto.MESSAGE,
        number=33,
        message="ProductDimension",
    )
    product_height: "ProductDimension" = proto.Field(
        proto.MESSAGE,
        number=34,
        message="ProductDimension",
    )
    product_highlights: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=35,
    )
    certifications: MutableSequence["Certification"] = proto.RepeatedField(
        proto.MESSAGE,
        number=39,
        message="Certification",
    )
    expiration_date: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=40,
        message=timestamp_pb2.Timestamp,
    )
    included_destinations: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=43,
    )
    excluded_destinations: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=44,
    )
    pause: str = proto.Field(
        proto.STRING,
        number=45,
        optional=True,
    )
    custom_label_0: str = proto.Field(
        proto.STRING,
        number=46,
        optional=True,
    )
    custom_label_1: str = proto.Field(
        proto.STRING,
        number=47,
        optional=True,
    )
    custom_label_2: str = proto.Field(
        proto.STRING,
        number=48,
        optional=True,
    )
    custom_label_3: str = proto.Field(
        proto.STRING,
        number=49,
        optional=True,
    )
    custom_label_4: str = proto.Field(
        proto.STRING,
        number=50,
        optional=True,
    )
    headline_offer_installment: "HeadlineOfferInstallment" = proto.Field(
        proto.MESSAGE,
        number=51,
        message="HeadlineOfferInstallment",
    )
    headline_offer_subscription_cost: "HeadlineOfferSubscriptionCost" = proto.Field(
        proto.MESSAGE,
        number=52,
        message="HeadlineOfferSubscriptionCost",
    )
    review_count: int = proto.Field(
        proto.INT64,
        number=54,
        optional=True,
    )
    min_rating: int = proto.Field(
        proto.INT64,
        number=55,
        optional=True,
    )
    max_rating: int = proto.Field(
        proto.INT64,
        number=56,
        optional=True,
    )
    rating: float = proto.Field(
        proto.DOUBLE,
        number=57,
        optional=True,
    )


class Certification(proto.Message):
    r"""The certification for the product. Use the this attribute to
    describe certifications, such as energy efficiency ratings,
    associated with a product.

    Attributes:
        name (str):
            The name of the certification. At this time,
            the most common value is "EPREL", which
            represents energy efficiency certifications in
            the EU European Registry for Energy Labeling
            (EPREL) database.
        authority (str):
            The authority or certification body responsible for issuing
            the certification. At this time, the most common value is
            "EC" or “European_Commission” for energy labels in the EU.
        code (str):
            The code of the certification. For example,
            for the EPREL certificate with the link
            https://eprel.ec.europa.eu/screen/product/dishwashers2019/123456
            the code is 123456. The code is required for
            European Energy Labels.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    authority: str = proto.Field(
        proto.STRING,
        number=2,
    )
    code: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ProductDetail(proto.Message):
    r"""The product details.

    Attributes:
        section_name (str):
            The section header used to group a set of
            product details.
        attribute_name (str):
            The name of the product detail.
        attribute_value (str):
            The value of the product detail.
    """

    section_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    attribute_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    attribute_value: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ProductDimension(proto.Message):
    r"""The dimension of the product.

    Attributes:
        value (float):
            Required. The dimension value represented as
            a number. The value can have a maximum precision
            of four decimal places.
        unit (str):
            Required. The dimension units. Acceptable values are:

            - "``in``"
            - "``cm``".
    """

    value: float = proto.Field(
        proto.DOUBLE,
        number=1,
    )
    unit: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ProductWeight(proto.Message):
    r"""The weight of the product.

    Attributes:
        value (float):
            Required. The weight represented as a number.
            The weight can have a maximum precision of four
            decimal places.
        unit (str):
            Required. The weight unit. Acceptable values are:

            - "``g``"
            - "``kg``"
            - "``oz``"
            - "``lb``".
    """

    value: float = proto.Field(
        proto.DOUBLE,
        number=1,
    )
    unit: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CssProductStatus(proto.Message):
    r"""The status of the Css Product, data validation issues, that
    is, information about the Css Product computed asynchronously.

    Attributes:
        destination_statuses (MutableSequence[google.shopping.css_v1.types.CssProductStatus.DestinationStatus]):
            The intended destinations for the product.
        item_level_issues (MutableSequence[google.shopping.css_v1.types.CssProductStatus.ItemLevelIssue]):
            A list of all issues associated with the
            product.
        creation_date (google.protobuf.timestamp_pb2.Timestamp):
            Date on which the item has been created, in `ISO
            8601 <http://en.wikipedia.org/wiki/ISO_8601>`__ format.
        last_update_date (google.protobuf.timestamp_pb2.Timestamp):
            Date on which the item has been last updated, in `ISO
            8601 <http://en.wikipedia.org/wiki/ISO_8601>`__ format.
        google_expiration_date (google.protobuf.timestamp_pb2.Timestamp):
            Date on which the item expires, in `ISO
            8601 <http://en.wikipedia.org/wiki/ISO_8601>`__ format.
    """

    class DestinationStatus(proto.Message):
        r"""The destination status of the product status.

        Attributes:
            destination (str):
                The name of the destination
            approved_countries (MutableSequence[str]):
                List of country codes (ISO 3166-1 alpha-2)
                where the CSS Product is approved.
            pending_countries (MutableSequence[str]):
                List of country codes (ISO 3166-1 alpha-2)
                where the CSS Product is pending approval.
            disapproved_countries (MutableSequence[str]):
                List of country codes (ISO 3166-1 alpha-2)
                where the CSS Product is disapproved.
        """

        destination: str = proto.Field(
            proto.STRING,
            number=1,
        )
        approved_countries: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )
        pending_countries: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=3,
        )
        disapproved_countries: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=4,
        )

    class ItemLevelIssue(proto.Message):
        r"""The ItemLevelIssue of the product status.

        Attributes:
            code (str):
                The error code of the issue.
            servability (str):
                How this issue affects serving of the CSS
                Product.
            resolution (str):
                Whether the issue can be resolved by the
                merchant.
            attribute (str):
                The attribute's name, if the issue is caused
                by a single attribute.
            destination (str):
                The destination the issue applies to.
            description (str):
                A short issue description in English.
            detail (str):
                A detailed issue description in English.
            documentation (str):
                The URL of a web page to help with resolving
                this issue.
            applicable_countries (MutableSequence[str]):
                List of country codes (ISO 3166-1 alpha-2)
                where issue applies to the CSS Product.
        """

        code: str = proto.Field(
            proto.STRING,
            number=1,
        )
        servability: str = proto.Field(
            proto.STRING,
            number=2,
        )
        resolution: str = proto.Field(
            proto.STRING,
            number=3,
        )
        attribute: str = proto.Field(
            proto.STRING,
            number=4,
        )
        destination: str = proto.Field(
            proto.STRING,
            number=5,
        )
        description: str = proto.Field(
            proto.STRING,
            number=6,
        )
        detail: str = proto.Field(
            proto.STRING,
            number=7,
        )
        documentation: str = proto.Field(
            proto.STRING,
            number=8,
        )
        applicable_countries: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=9,
        )

    destination_statuses: MutableSequence[DestinationStatus] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=DestinationStatus,
    )
    item_level_issues: MutableSequence[ItemLevelIssue] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=ItemLevelIssue,
    )
    creation_date: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    last_update_date: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    google_expiration_date: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )


class HeadlineOfferSubscriptionCost(proto.Message):
    r"""The SubscriptionCost of the product.

    Attributes:
        period (google.shopping.css_v1.types.SubscriptionPeriod):
            The type of subscription period. Supported values are:

            - "``month``"
            - "``year``".
        period_length (int):
            The number of subscription periods the buyer
            has to pay.
        amount (google.shopping.type.types.Price):
            The amount the buyer has to pay per
            subscription period.
    """

    period: "SubscriptionPeriod" = proto.Field(
        proto.ENUM,
        number=1,
        enum="SubscriptionPeriod",
    )
    period_length: int = proto.Field(
        proto.INT64,
        number=2,
    )
    amount: types.Price = proto.Field(
        proto.MESSAGE,
        number=3,
        message=types.Price,
    )


class HeadlineOfferInstallment(proto.Message):
    r"""A message that represents installment.

    Attributes:
        months (int):
            The number of installments the buyer has to
            pay.
        amount (google.shopping.type.types.Price):
            The amount the buyer has to pay per month.
        downpayment (google.shopping.type.types.Price):
            The up-front down payment amount the buyer
            has to pay.
    """

    months: int = proto.Field(
        proto.INT64,
        number=1,
    )
    amount: types.Price = proto.Field(
        proto.MESSAGE,
        number=2,
        message=types.Price,
    )
    downpayment: types.Price = proto.Field(
        proto.MESSAGE,
        number=3,
        message=types.Price,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
