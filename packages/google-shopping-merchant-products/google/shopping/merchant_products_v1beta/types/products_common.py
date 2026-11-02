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
import google.type.interval_pb2 as interval_pb2  # type: ignore
import proto  # type: ignore
from google.shopping.type.types import types

__protobuf__ = proto.module(
    package="google.shopping.merchant.products.v1beta",
    manifest={
        "SubscriptionPeriod",
        "Attributes",
        "Tax",
        "ShippingWeight",
        "ShippingDimension",
        "UnitPricingBaseMeasure",
        "UnitPricingMeasure",
        "SubscriptionCost",
        "Installment",
        "LoyaltyPoints",
        "LoyaltyProgram",
        "Shipping",
        "FreeShippingThreshold",
        "ProductDetail",
        "Certification",
        "ProductStructuredTitle",
        "ProductStructuredDescription",
        "ProductDimension",
        "ProductWeight",
        "ProductStatus",
        "CloudExportAdditionalProperties",
        "ProductSustainabilityIncentive",
        "AutomatedDiscounts",
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
    r"""Attributes.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        identifier_exists (bool):
            Set this value to false when the item does
            not have unique product identifiers appropriate
            to its category, such as GTIN, MPN, and brand.
            Defaults to true, if not provided.

            This field is a member of `oneof`_ ``_identifier_exists``.
        is_bundle (bool):
            Whether the item is a business-defined sub-API. A [sub-API]
            (https://support.google.com/merchants/answer/6324449) is a
            custom grouping of different products sold by a business for
            a single price.

            This field is a member of `oneof`_ ``_is_bundle``.
        title (str):
            Title of the item.

            This field is a member of `oneof`_ ``_title``.
        description (str):
            Description of the item.

            This field is a member of `oneof`_ ``_description``.
        link (str):
            URL directly linking to your item's page on
            your online store.

            This field is a member of `oneof`_ ``_link``.
        mobile_link (str):
            URL for the mobile-optimized version of your
            item's landing page.

            This field is a member of `oneof`_ ``_mobile_link``.
        canonical_link (str):
            URL for the canonical version of your item's
            landing page.

            This field is a member of `oneof`_ ``_canonical_link``.
        image_link (str):
            URL of an image of the item.

            This field is a member of `oneof`_ ``_image_link``.
        additional_image_links (MutableSequence[str]):
            Additional URLs of images of the item.
        expiration_date (google.protobuf.timestamp_pb2.Timestamp):
            Date on which the item should expire, as specified upon
            insertion, in `ISO
            8601 <http://en.wikipedia.org/wiki/ISO_8601>`__ format. The
            actual expiration date is exposed in ``productstatuses`` as
            `googleExpirationDate <https://support.google.com/merchants/answer/6324499>`__
            and might be earlier if ``expirationDate`` is too far in the
            future.
        disclosure_date (google.protobuf.timestamp_pb2.Timestamp):
            The date time when an offer becomes visible in search
            results across Google’s YouTube surfaces, in `ISO
            8601 <http://en.wikipedia.org/wiki/ISO_8601>`__ format. See
            `Disclosure
            date <https://support.google.com/merchants/answer/13034208>`__
            for more information.
        adult (bool):
            Set to true if the item is targeted towards
            adults.

            This field is a member of `oneof`_ ``_adult``.
        age_group (str):
            Target `age
            group <https://support.google.com/merchants/answer/6324463>`__
            of the item.

            This field is a member of `oneof`_ ``_age_group``.
        availability (str):
            `Availability <https://support.google.com/merchants/answer/6324448>`__
            status of the item. For example, "in_stock" or
            "out_of_stock".

            This field is a member of `oneof`_ ``_availability``.
        availability_date (google.protobuf.timestamp_pb2.Timestamp):
            The day a pre-ordered product becomes available for
            delivery, in `ISO
            8601 <http://en.wikipedia.org/wiki/ISO_8601>`__ format.
        brand (str):
            `Brand <https://support.google.com/merchants/answer/6324351>`__
            of the item. For example, "Google".

            This field is a member of `oneof`_ ``_brand``.
        color (str):
            `Color <https://support.google.com/merchants/answer/6324487>`__
            of the item. For example, "red".

            This field is a member of `oneof`_ ``_color``.
        condition (str):
            `Condition <https://support.google.com/merchants/answer/6324469>`__
            or state of the item. For example, "new" or "used".

            This field is a member of `oneof`_ ``_condition``.
        gender (str):
            Target
            `gender <https://support.google.com/merchants/answer/6324479>`__
            of the item. For example, "male" or "female".

            This field is a member of `oneof`_ ``_gender``.
        google_product_category (str):
            Google's category of the item (see `Google product
            taxonomy <https://support.google.com/merchants/answer/1705911>`__).
            When querying products, this field will contain the user
            provided value. There is currently no way to get back the
            auto assigned google product categories through the API.

            This field is a member of `oneof`_ ``_google_product_category``.
        gtin (MutableSequence[str]):
            Global Trade Item Numbers
            (`GTIN <https://support.google.com/merchants/answer/188494#gtin>`__)
            of the item. You can provide up to 10 GTINs.

            Deprecated: Use ``gtins`` instead.
        gtins (MutableSequence[str]):
            Global Trade Item Numbers
            (`GTIN <https://support.google.com/merchants/answer/188494#gtin>`__)
            of the item. You can provide up to 10 GTINs.
        item_group_id (str):
            Shared identifier for all variants of the
            same product.

            This field is a member of `oneof`_ ``_item_group_id``.
        material (str):
            The
            `material <https://support.google.com/merchants/answer/6324410>`__
            of which the item is made. For example, "Leather" or
            "Cotton".

            This field is a member of `oneof`_ ``_material``.
        mpn (str):
            Manufacturer Part Number
            (`MPN <https://support.google.com/merchants/answer/188494#mpn>`__)
            of the item.

            This field is a member of `oneof`_ ``_mpn``.
        pattern (str):
            The item's
            `pattern <https://support.google.com/merchants/answer/6324483>`__.
            For example, polka dots.

            This field is a member of `oneof`_ ``_pattern``.
        price (google.shopping.type.types.Price):
            Price of the item.
        maximum_retail_price (google.shopping.type.types.Price):
            Maximum retail price (MRP) of the item.
            Applicable to India only.
        installment (google.shopping.merchant_products_v1beta.types.Installment):
            Number and amount of installments to pay for
            an item.
        subscription_cost (google.shopping.merchant_products_v1beta.types.SubscriptionCost):
            Number of periods (months or years) and
            amount of payment per period for an item with an
            associated subscription contract.
        loyalty_points (google.shopping.merchant_products_v1beta.types.LoyaltyPoints):
            Loyalty points that users receive after
            purchasing the item. Japan only.
        loyalty_programs (MutableSequence[google.shopping.merchant_products_v1beta.types.LoyaltyProgram]):
            A list of loyalty program information that is
            used to surface loyalty benefits (for example,
            better pricing, points, etc) to the user of this
            item.
        product_types (MutableSequence[str]):
            Categories of the item (formatted as in `product data
            specification <https://support.google.com/merchants/answer/7052112#product_category>`__).
        sale_price (google.shopping.type.types.Price):
            Advertised sale price of the item.
        sale_price_effective_date (google.type.interval_pb2.Interval):
            Date range during which the item is on sale, see `product
            data
            specification <https://support.google.com/merchants/answer/7052112#price_and_availability>`__.
        sell_on_google_quantity (int):
            The quantity of the product that is available
            for selling on Google. Supported only for online
            products.

            This field is a member of `oneof`_ ``_sell_on_google_quantity``.
        product_height (google.shopping.merchant_products_v1beta.types.ProductDimension):
            The height of the product in the units
            provided. The value must be between
            0 (exclusive) and 3000 (inclusive).
        product_length (google.shopping.merchant_products_v1beta.types.ProductDimension):
            The length of the product in the units
            provided. The value must be between 0
            (exclusive) and 3000 (inclusive).
        product_width (google.shopping.merchant_products_v1beta.types.ProductDimension):
            The width of the product in the units
            provided. The value must be between 0
            (exclusive) and 3000 (inclusive).
        product_weight (google.shopping.merchant_products_v1beta.types.ProductWeight):
            The weight of the product in the units
            provided. The value must be between 0
            (exclusive) and 2000 (inclusive).
        shipping (MutableSequence[google.shopping.merchant_products_v1beta.types.Shipping]):
            Shipping rules.
        free_shipping_threshold (MutableSequence[google.shopping.merchant_products_v1beta.types.FreeShippingThreshold]):
            Conditions to be met for a product to have
            free shipping.
        shipping_weight (google.shopping.merchant_products_v1beta.types.ShippingWeight):
            Weight of the item for shipping.
        shipping_length (google.shopping.merchant_products_v1beta.types.ShippingDimension):
            Length of the item for shipping.
        shipping_width (google.shopping.merchant_products_v1beta.types.ShippingDimension):
            Width of the item for shipping.
        shipping_height (google.shopping.merchant_products_v1beta.types.ShippingDimension):
            Height of the item for shipping.
        max_handling_time (int):
            Maximal product handling time (in business
            days).

            This field is a member of `oneof`_ ``_max_handling_time``.
        min_handling_time (int):
            Minimal product handling time (in business
            days).

            This field is a member of `oneof`_ ``_min_handling_time``.
        shipping_label (str):
            The shipping label of the product, used to
            group product in account-level shipping rules.

            This field is a member of `oneof`_ ``_shipping_label``.
        transit_time_label (str):
            The transit time label of the product, used
            to group product in account-level transit time
            tables.

            This field is a member of `oneof`_ ``_transit_time_label``.
        size (str):
            Size of the item. Only one value is allowed. For variants
            with different sizes, insert a separate product for each
            size with the same ``itemGroupId`` value, see
            `Size <https://support.google.com/merchants/answer/6324492>`__.

            This field is a member of `oneof`_ ``_size``.
        size_system (str):
            System in which the size is specified. Recommended for
            apparel items. For example, "US", "UK", "DE". For more
            information, see `Size
            system <https://support.google.com/merchants/answer/6324502>`__.

            This field is a member of `oneof`_ ``_size_system``.
        size_types (MutableSequence[str]):
            The cut of the item. It can be used to represent combined
            size types for apparel items. Maximum two of size types can
            be provided, see `Size
            type <https://support.google.com/merchants/answer/6324497>`__.
            For example, "petite", "plus size".
        taxes (MutableSequence[google.shopping.merchant_products_v1beta.types.Tax]):
            Tax information.
        tax_category (str):
            The `tax
            category <https://support.google.com/merchants/answer/7569847>`__
            of the product.

            This field is a member of `oneof`_ ``_tax_category``.
        energy_efficiency_class (str):
            The energy efficiency class as defined in EU
            directive 2010/30/EU.

            This field is a member of `oneof`_ ``_energy_efficiency_class``.
        min_energy_efficiency_class (str):
            The energy efficiency class as defined in EU
            directive 2010/30/EU.

            This field is a member of `oneof`_ ``_min_energy_efficiency_class``.
        max_energy_efficiency_class (str):
            The energy efficiency class as defined in EU
            directive 2010/30/EU.

            This field is a member of `oneof`_ ``_max_energy_efficiency_class``.
        unit_pricing_measure (google.shopping.merchant_products_v1beta.types.UnitPricingMeasure):
            The measure and dimension of an item.
        unit_pricing_base_measure (google.shopping.merchant_products_v1beta.types.UnitPricingBaseMeasure):
            The preference of the denominator of the unit
            price.
        multipack (int):
            The number of identical products in a
            business-defined multipack.

            This field is a member of `oneof`_ ``_multipack``.
        ads_grouping (str):
            Used to group items in an arbitrary way. Only for CPA%,
            discouraged otherwise. For more information, see `Display
            ads
            attribute <https://support.google.com/merchants/answer/6069387>`__.

            This field is a member of `oneof`_ ``_ads_grouping``.
        ads_labels (MutableSequence[str]):
            Similar to ads_grouping, but only works on CPC.
        ads_redirect (str):
            Allows advertisers to override the item URL
            when the product is shown within the context of
            Product ads.

            This field is a member of `oneof`_ ``_ads_redirect``.
        cost_of_goods_sold (google.shopping.type.types.Price):
            Cost of goods sold. Used for gross profit
            reporting.
        product_details (MutableSequence[google.shopping.merchant_products_v1beta.types.ProductDetail]):
            Technical specification or additional product
            details.
        product_highlights (MutableSequence[str]):
            Bullet points describing the most relevant `product
            highlights <https://support.google.com/merchants/answer/9216100>`__.
        display_ads_id (str):
            An identifier for an item for dynamic
            remarketing campaigns.

            This field is a member of `oneof`_ ``_display_ads_id``.
        display_ads_similar_ids (MutableSequence[str]):
            Advertiser-specified recommendations. For more information,
            see `Display ads attribute
            specification <https://support.google.com/merchants/answer/6069387>`__.
        display_ads_title (str):
            Title of an item for dynamic remarketing
            campaigns.

            This field is a member of `oneof`_ ``_display_ads_title``.
        display_ads_link (str):
            URL directly to your item's landing page for
            dynamic remarketing campaigns.

            This field is a member of `oneof`_ ``_display_ads_link``.
        display_ads_value (float):
            Offer margin for dynamic remarketing campaigns. For more
            information, see `Display ads
            attribute <https://support.google.com/merchants/answer/6069387>`__.

            This field is a member of `oneof`_ ``_display_ads_value``.
        promotion_ids (MutableSequence[str]):
            The unique ID of a promotion.
        pickup_method (str):
            The
            `pickup <https://support.google.com/merchants/answer/14634021>`__
            option for the item.

            This field is a member of `oneof`_ ``_pickup_method``.
        pickup_sla (str):
            Item store pickup timeline. For more information, see
            `Pickup
            SLA <https://support.google.com/merchants/answer/14635400>`__.

            This field is a member of `oneof`_ ``_pickup_sla``.
        link_template (str):
            `Link
            template <https://support.google.com/merchants/answer/13871172>`__
            for business hosted local storefront.

            This field is a member of `oneof`_ ``_link_template``.
        mobile_link_template (str):
            `Link
            template <https://support.google.com/merchants/answer/13870216>`__
            for business hosted local storefront optimized for mobile
            devices.

            This field is a member of `oneof`_ ``_mobile_link_template``.
        custom_label_0 (str):
            `Custom label
            0 <https://support.google.com/merchants/answer/6324473>`__
            for custom grouping of items in a Shopping campaign.

            This field is a member of `oneof`_ ``_custom_label_0``.
        custom_label_1 (str):
            `Custom label
            1 <https://support.google.com/merchants/answer/6324473>`__
            for custom grouping of items in a Shopping campaign.

            This field is a member of `oneof`_ ``_custom_label_1``.
        custom_label_2 (str):
            `Custom label
            2 <https://support.google.com/merchants/answer/6324473>`__
            for custom grouping of items in a Shopping campaign.

            This field is a member of `oneof`_ ``_custom_label_2``.
        custom_label_3 (str):
            `Custom label
            3 <https://support.google.com/merchants/answer/6324473>`__
            for custom grouping of items in a Shopping campaign.

            This field is a member of `oneof`_ ``_custom_label_3``.
        custom_label_4 (str):
            `Custom label
            4 <https://support.google.com/merchants/answer/6324473>`__
            for custom grouping of items in a Shopping campaign.

            This field is a member of `oneof`_ ``_custom_label_4``.
        included_destinations (MutableSequence[str]):
            The list of destinations to include for this target
            (corresponds to checked check boxes in Merchant Center).
            Default destinations are always included unless provided in
            ``excludedDestinations``.

            For more information, see `Included
            destination <https://support.google.com/merchants/answer/7501026>`__.

            Note: We recommend setting destinations on datasources level
            for most use cases. Use this field within products to only
            setup exceptions.
        excluded_destinations (MutableSequence[str]):
            The list of destinations to exclude for this target
            (corresponds to unchecked check boxes in Merchant Center).

            For more information, see `Excluded
            destination <https://support.google.com/merchants/answer/6324486>`__.

            Note: We recommend setting destinations on datasources level
            for most use cases. Use this field within products to only
            setup exceptions.
        shopping_ads_excluded_countries (MutableSequence[str]):
            List of country codes `(ISO 3166-1
            alpha-2) <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__
            to exclude the offer from Shopping Ads destination.
            Countries from this list are removed from countries
            configured in data source settings.
        external_seller_id (str):
            Required for multi-seller accounts. Use this
            attribute if you're a marketplace uploading
            products for various sellers to your
            multi-seller account.

            This field is a member of `oneof`_ ``_external_seller_id``.
        pause (str):
            Publication of this item will be temporarily
            `paused <https://support.google.com/merchants/answer/11909930>`__.

            This field is a member of `oneof`_ ``_pause``.
        lifestyle_image_links (MutableSequence[str]):
            Additional URLs of lifestyle images of the item, used to
            explicitly identify images that showcase your item in a
            real-world context. See the `Help Center
            article <https://support.google.com/merchants/answer/9103186>`__
            for more information.
        cloud_export_additional_properties (MutableSequence[google.shopping.merchant_products_v1beta.types.CloudExportAdditionalProperties]):
            Extra fields to export to the Cloud Retail
            program.
        virtual_model_link (str):
            URL of the 3D image of the item. See the `Help Center
            article <https://support.google.com/merchants/answer/13674896>`__
            for more information.

            This field is a member of `oneof`_ ``_virtual_model_link``.
        certifications (MutableSequence[google.shopping.merchant_products_v1beta.types.Certification]):
            Product Certifications, for example for energy efficiency
            labeling of products recorded in the `EU
            EPREL <https://eprel.ec.europa.eu/screen/home>`__ database.
            See the `Help
            Center <https://support.google.com/merchants/answer/13528839>`__
            article for more information.
        structured_title (google.shopping.merchant_products_v1beta.types.ProductStructuredTitle):
            Structured title, for algorithmically
            (AI)-generated titles.

            This field is a member of `oneof`_ ``_structured_title``.
        structured_description (google.shopping.merchant_products_v1beta.types.ProductStructuredDescription):
            Structured description, for algorithmically
            (AI)-generated descriptions.

            This field is a member of `oneof`_ ``_structured_description``.
        auto_pricing_min_price (google.shopping.type.types.Price):
            A safeguard in the [automated discounts]
            (https://support.google.com/merchants/answer/10295759) and
            "Dynamic Promotions"
            (https://support.google.com/merchants/answer/13949249)
            projects, ensuring that discounts on business offers do not
            fall below this value, thereby preserving the offer's value
            and profitability.
        sustainability_incentives (MutableSequence[google.shopping.merchant_products_v1beta.types.ProductSustainabilityIncentive]):
            The list of sustainability incentive
            programs.
    """

    identifier_exists: bool = proto.Field(
        proto.BOOL,
        number=4,
        optional=True,
    )
    is_bundle: bool = proto.Field(
        proto.BOOL,
        number=5,
        optional=True,
    )
    title: str = proto.Field(
        proto.STRING,
        number=6,
        optional=True,
    )
    description: str = proto.Field(
        proto.STRING,
        number=7,
        optional=True,
    )
    link: str = proto.Field(
        proto.STRING,
        number=8,
        optional=True,
    )
    mobile_link: str = proto.Field(
        proto.STRING,
        number=9,
        optional=True,
    )
    canonical_link: str = proto.Field(
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
    expiration_date: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=16,
        message=timestamp_pb2.Timestamp,
    )
    disclosure_date: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=79,
        message=timestamp_pb2.Timestamp,
    )
    adult: bool = proto.Field(
        proto.BOOL,
        number=17,
        optional=True,
    )
    age_group: str = proto.Field(
        proto.STRING,
        number=18,
        optional=True,
    )
    availability: str = proto.Field(
        proto.STRING,
        number=19,
        optional=True,
    )
    availability_date: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=20,
        message=timestamp_pb2.Timestamp,
    )
    brand: str = proto.Field(
        proto.STRING,
        number=21,
        optional=True,
    )
    color: str = proto.Field(
        proto.STRING,
        number=22,
        optional=True,
    )
    condition: str = proto.Field(
        proto.STRING,
        number=23,
        optional=True,
    )
    gender: str = proto.Field(
        proto.STRING,
        number=24,
        optional=True,
    )
    google_product_category: str = proto.Field(
        proto.STRING,
        number=25,
        optional=True,
    )
    gtin: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=26,
    )
    gtins: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=140,
    )
    item_group_id: str = proto.Field(
        proto.STRING,
        number=27,
        optional=True,
    )
    material: str = proto.Field(
        proto.STRING,
        number=28,
        optional=True,
    )
    mpn: str = proto.Field(
        proto.STRING,
        number=29,
        optional=True,
    )
    pattern: str = proto.Field(
        proto.STRING,
        number=30,
        optional=True,
    )
    price: types.Price = proto.Field(
        proto.MESSAGE,
        number=31,
        message=types.Price,
    )
    maximum_retail_price: types.Price = proto.Field(
        proto.MESSAGE,
        number=139,
        message=types.Price,
    )
    installment: "Installment" = proto.Field(
        proto.MESSAGE,
        number=32,
        message="Installment",
    )
    subscription_cost: "SubscriptionCost" = proto.Field(
        proto.MESSAGE,
        number=33,
        message="SubscriptionCost",
    )
    loyalty_points: "LoyaltyPoints" = proto.Field(
        proto.MESSAGE,
        number=34,
        message="LoyaltyPoints",
    )
    loyalty_programs: MutableSequence["LoyaltyProgram"] = proto.RepeatedField(
        proto.MESSAGE,
        number=136,
        message="LoyaltyProgram",
    )
    product_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=35,
    )
    sale_price: types.Price = proto.Field(
        proto.MESSAGE,
        number=36,
        message=types.Price,
    )
    sale_price_effective_date: interval_pb2.Interval = proto.Field(
        proto.MESSAGE,
        number=37,
        message=interval_pb2.Interval,
    )
    sell_on_google_quantity: int = proto.Field(
        proto.INT64,
        number=38,
        optional=True,
    )
    product_height: "ProductDimension" = proto.Field(
        proto.MESSAGE,
        number=119,
        message="ProductDimension",
    )
    product_length: "ProductDimension" = proto.Field(
        proto.MESSAGE,
        number=120,
        message="ProductDimension",
    )
    product_width: "ProductDimension" = proto.Field(
        proto.MESSAGE,
        number=121,
        message="ProductDimension",
    )
    product_weight: "ProductWeight" = proto.Field(
        proto.MESSAGE,
        number=122,
        message="ProductWeight",
    )
    shipping: MutableSequence["Shipping"] = proto.RepeatedField(
        proto.MESSAGE,
        number=39,
        message="Shipping",
    )
    free_shipping_threshold: MutableSequence["FreeShippingThreshold"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=135,
            message="FreeShippingThreshold",
        )
    )
    shipping_weight: "ShippingWeight" = proto.Field(
        proto.MESSAGE,
        number=40,
        message="ShippingWeight",
    )
    shipping_length: "ShippingDimension" = proto.Field(
        proto.MESSAGE,
        number=41,
        message="ShippingDimension",
    )
    shipping_width: "ShippingDimension" = proto.Field(
        proto.MESSAGE,
        number=42,
        message="ShippingDimension",
    )
    shipping_height: "ShippingDimension" = proto.Field(
        proto.MESSAGE,
        number=43,
        message="ShippingDimension",
    )
    max_handling_time: int = proto.Field(
        proto.INT64,
        number=44,
        optional=True,
    )
    min_handling_time: int = proto.Field(
        proto.INT64,
        number=45,
        optional=True,
    )
    shipping_label: str = proto.Field(
        proto.STRING,
        number=46,
        optional=True,
    )
    transit_time_label: str = proto.Field(
        proto.STRING,
        number=47,
        optional=True,
    )
    size: str = proto.Field(
        proto.STRING,
        number=48,
        optional=True,
    )
    size_system: str = proto.Field(
        proto.STRING,
        number=49,
        optional=True,
    )
    size_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=50,
    )
    taxes: MutableSequence["Tax"] = proto.RepeatedField(
        proto.MESSAGE,
        number=51,
        message="Tax",
    )
    tax_category: str = proto.Field(
        proto.STRING,
        number=52,
        optional=True,
    )
    energy_efficiency_class: str = proto.Field(
        proto.STRING,
        number=53,
        optional=True,
    )
    min_energy_efficiency_class: str = proto.Field(
        proto.STRING,
        number=54,
        optional=True,
    )
    max_energy_efficiency_class: str = proto.Field(
        proto.STRING,
        number=55,
        optional=True,
    )
    unit_pricing_measure: "UnitPricingMeasure" = proto.Field(
        proto.MESSAGE,
        number=56,
        message="UnitPricingMeasure",
    )
    unit_pricing_base_measure: "UnitPricingBaseMeasure" = proto.Field(
        proto.MESSAGE,
        number=57,
        message="UnitPricingBaseMeasure",
    )
    multipack: int = proto.Field(
        proto.INT64,
        number=58,
        optional=True,
    )
    ads_grouping: str = proto.Field(
        proto.STRING,
        number=59,
        optional=True,
    )
    ads_labels: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=60,
    )
    ads_redirect: str = proto.Field(
        proto.STRING,
        number=61,
        optional=True,
    )
    cost_of_goods_sold: types.Price = proto.Field(
        proto.MESSAGE,
        number=62,
        message=types.Price,
    )
    product_details: MutableSequence["ProductDetail"] = proto.RepeatedField(
        proto.MESSAGE,
        number=63,
        message="ProductDetail",
    )
    product_highlights: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=64,
    )
    display_ads_id: str = proto.Field(
        proto.STRING,
        number=65,
        optional=True,
    )
    display_ads_similar_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=66,
    )
    display_ads_title: str = proto.Field(
        proto.STRING,
        number=67,
        optional=True,
    )
    display_ads_link: str = proto.Field(
        proto.STRING,
        number=68,
        optional=True,
    )
    display_ads_value: float = proto.Field(
        proto.DOUBLE,
        number=69,
        optional=True,
    )
    promotion_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=70,
    )
    pickup_method: str = proto.Field(
        proto.STRING,
        number=80,
        optional=True,
    )
    pickup_sla: str = proto.Field(
        proto.STRING,
        number=81,
        optional=True,
    )
    link_template: str = proto.Field(
        proto.STRING,
        number=82,
        optional=True,
    )
    mobile_link_template: str = proto.Field(
        proto.STRING,
        number=83,
        optional=True,
    )
    custom_label_0: str = proto.Field(
        proto.STRING,
        number=71,
        optional=True,
    )
    custom_label_1: str = proto.Field(
        proto.STRING,
        number=72,
        optional=True,
    )
    custom_label_2: str = proto.Field(
        proto.STRING,
        number=73,
        optional=True,
    )
    custom_label_3: str = proto.Field(
        proto.STRING,
        number=74,
        optional=True,
    )
    custom_label_4: str = proto.Field(
        proto.STRING,
        number=75,
        optional=True,
    )
    included_destinations: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=76,
    )
    excluded_destinations: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=77,
    )
    shopping_ads_excluded_countries: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=78,
    )
    external_seller_id: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    pause: str = proto.Field(
        proto.STRING,
        number=13,
        optional=True,
    )
    lifestyle_image_links: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=14,
    )
    cloud_export_additional_properties: MutableSequence[
        "CloudExportAdditionalProperties"
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=84,
        message="CloudExportAdditionalProperties",
    )
    virtual_model_link: str = proto.Field(
        proto.STRING,
        number=130,
        optional=True,
    )
    certifications: MutableSequence["Certification"] = proto.RepeatedField(
        proto.MESSAGE,
        number=123,
        message="Certification",
    )
    structured_title: "ProductStructuredTitle" = proto.Field(
        proto.MESSAGE,
        number=132,
        optional=True,
        message="ProductStructuredTitle",
    )
    structured_description: "ProductStructuredDescription" = proto.Field(
        proto.MESSAGE,
        number=133,
        optional=True,
        message="ProductStructuredDescription",
    )
    auto_pricing_min_price: types.Price = proto.Field(
        proto.MESSAGE,
        number=124,
        message=types.Price,
    )
    sustainability_incentives: MutableSequence["ProductSustainabilityIncentive"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=138,
            message="ProductSustainabilityIncentive",
        )
    )


class Tax(proto.Message):
    r"""The Tax of the product.

    Attributes:
        rate (float):
            The percentage of tax rate that applies to
            the item price.
        country (str):
            The country within which the item is taxed, specified as a
            `CLDR territory
            code <http://www.unicode.org/repos/cldr/tags/latest/common/main/en.xml>`__.
        region (str):
            The geographic region to which the tax rate
            applies.
        tax_ship (bool):
            Set to true if tax is charged on shipping.
        location_id (int):
            The numeric ID of a location that the tax rate applies to as
            defined in the `AdWords
            API <https://developers.google.com/adwords/api/docs/appendix/geotargeting>`__.
        postal_code (str):
            The postal code range that the tax rate applies to,
            represented by a ZIP code, a ZIP code prefix using \*
            wildcard, a range between two ZIP codes or two ZIP code
            prefixes of equal length. Examples: 94114, 94\*,
            94002-95460, 94\*-95\*.
    """

    rate: float = proto.Field(
        proto.DOUBLE,
        number=1,
    )
    country: str = proto.Field(
        proto.STRING,
        number=2,
    )
    region: str = proto.Field(
        proto.STRING,
        number=3,
    )
    tax_ship: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    location_id: int = proto.Field(
        proto.INT64,
        number=5,
    )
    postal_code: str = proto.Field(
        proto.STRING,
        number=6,
    )


class ShippingWeight(proto.Message):
    r"""The ShippingWeight of the product.

    Attributes:
        value (float):
            The weight of the product used to calculate
            the shipping cost of the item.
        unit (str):
            The unit of value.
    """

    value: float = proto.Field(
        proto.DOUBLE,
        number=1,
    )
    unit: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ShippingDimension(proto.Message):
    r"""The ShippingDimension of the product.

    Attributes:
        value (float):
            The dimension of the product used to
            calculate the shipping cost of the item.
        unit (str):
            The unit of value.
    """

    value: float = proto.Field(
        proto.DOUBLE,
        number=1,
    )
    unit: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UnitPricingBaseMeasure(proto.Message):
    r"""The UnitPricingBaseMeasure of the product.

    Attributes:
        value (int):
            The denominator of the unit price.
        unit (str):
            The unit of the denominator.
    """

    value: int = proto.Field(
        proto.INT64,
        number=1,
    )
    unit: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UnitPricingMeasure(proto.Message):
    r"""The UnitPricingMeasure of the product.

    Attributes:
        value (float):
            The measure of an item.
        unit (str):
            The unit of the measure.
    """

    value: float = proto.Field(
        proto.DOUBLE,
        number=1,
    )
    unit: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SubscriptionCost(proto.Message):
    r"""The SubscriptionCost of the product.

    Attributes:
        period (google.shopping.merchant_products_v1beta.types.SubscriptionPeriod):
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


class Installment(proto.Message):
    r"""A message that represents installment.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        months (int):
            The number of installments the buyer has to
            pay.
        amount (google.shopping.type.types.Price):
            The amount the buyer has to pay per month.
        downpayment (google.shopping.type.types.Price):
            The up-front down payment amount the buyer
            has to pay.

            This field is a member of `oneof`_ ``_downpayment``.
        credit_type (str):
            Type of installment payments. Supported values are:

            - "``finance``"
            - "``lease``".

            This field is a member of `oneof`_ ``_credit_type``.
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
        optional=True,
        message=types.Price,
    )
    credit_type: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )


class LoyaltyPoints(proto.Message):
    r"""A message that represents loyalty points.

    Attributes:
        name (str):
            Name of loyalty points program. It is
            recommended to limit the name to 12 full-width
            characters or 24 Roman characters.
        points_value (int):
            The retailer's loyalty points in absolute
            value.
        ratio (float):
            The ratio of a point when converted to
            currency. Google assumes currency based on
            Merchant Center settings. If ratio is left out,
            it defaults to 1.0.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    points_value: int = proto.Field(
        proto.INT64,
        number=2,
    )
    ratio: float = proto.Field(
        proto.DOUBLE,
        number=3,
    )


class LoyaltyProgram(proto.Message):
    r"""A message that represents loyalty program.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        program_label (str):
            The label of the loyalty program. This is an
            internal label that uniquely identifies the
            relationship between a business entity and a
            loyalty program entity. The label must be
            provided so that the system can associate the
            assets below (for example, price and points)
            with a business. The corresponding program must
            be linked to the Merchant Center account.

            This field is a member of `oneof`_ ``_program_label``.
        tier_label (str):
            The label of the tier within the loyalty
            program. Must match one of the labels within the
            program.

            This field is a member of `oneof`_ ``_tier_label``.
        price (google.shopping.type.types.Price):
            The price for members of the given tier, that
            is, the instant discount price. Must be smaller
            or equal to the regular price.

            This field is a member of `oneof`_ ``_price``.
        cashback_for_future_use (google.shopping.type.types.Price):
            The cashback that can be used for future
            purchases.

            This field is a member of `oneof`_ ``_cashback_for_future_use``.
        loyalty_points (int):
            The amount of loyalty points earned on a
            purchase.

            This field is a member of `oneof`_ ``_loyalty_points``.
        member_price_effective_date (google.type.interval_pb2.Interval):
            A date range during which the item is
            eligible for member price. If not specified, the
            member price is always applicable. The date
            range is represented by a pair of ISO 8601 dates
            separated by a space, comma, or slash.

            This field is a member of `oneof`_ ``_member_price_effective_date``.
        shipping_label (str):
            The label of the shipping benefit. If the
            field has value, this offer has loyalty shipping
            benefit. If the field value isn't provided, the
            item is not eligible for loyalty shipping for
            the given loyalty tier.

            This field is a member of `oneof`_ ``_shipping_label``.
    """

    program_label: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    tier_label: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    price: types.Price = proto.Field(
        proto.MESSAGE,
        number=3,
        optional=True,
        message=types.Price,
    )
    cashback_for_future_use: types.Price = proto.Field(
        proto.MESSAGE,
        number=4,
        optional=True,
        message=types.Price,
    )
    loyalty_points: int = proto.Field(
        proto.INT64,
        number=5,
        optional=True,
    )
    member_price_effective_date: interval_pb2.Interval = proto.Field(
        proto.MESSAGE,
        number=6,
        optional=True,
        message=interval_pb2.Interval,
    )
    shipping_label: str = proto.Field(
        proto.STRING,
        number=7,
        optional=True,
    )


class Shipping(proto.Message):
    r"""The Shipping of the product.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        price (google.shopping.type.types.Price):
            Fixed shipping price, represented as a
            number.
        country (str):
            The `CLDR territory
            code <http://www.unicode.org/repos/cldr/tags/latest/common/main/en.xml>`__
            of the country to which an item will ship.
        region (str):
            The geographic region to which a shipping rate applies. See
            `region <https://support.google.com/merchants/answer/6324484>`__
            for more information.
        service (str):
            A free-form description of the service class
            or delivery speed.
        location_id (int):
            The numeric ID of a location that the shipping rate applies
            to as defined in the `AdWords
            API <https://developers.google.com/adwords/api/docs/appendix/geotargeting>`__.
        location_group_name (str):
            The location where the shipping is
            applicable, represented by a location group
            name.
        postal_code (str):
            The postal code range that the shipping rate applies to,
            represented by a postal code, a postal code prefix followed
            by a \* wildcard, a range between two postal codes or two
            postal code prefixes of equal length.
        min_handling_time (int):
            Minimum handling time (inclusive) between when the order is
            received and shipped in business days. 0 means that the
            order is shipped on the same day as it is received if it
            happens before the cut-off time.
            [minHandlingTime][google.shopping.merchant.products.v1beta.Shipping.min_handling_time]
            can only be present together with
            [maxHandlingTime][google.shopping.merchant.products.v1beta.Shipping.max_handling_time];
            but it is not required if
            [maxHandlingTime][google.shopping.merchant.products.v1beta.Shipping.max_handling_time]
            is present.

            This field is a member of `oneof`_ ``_min_handling_time``.
        max_handling_time (int):
            Maximum handling time (inclusive) between when the order is
            received and shipped in business days. 0 means that the
            order is shipped on the same day as it is received if it
            happens before the cut-off time. Both
            [maxHandlingTime][google.shopping.merchant.products.v1beta.Shipping.max_handling_time]
            and
            [maxTransitTime][google.shopping.merchant.products.v1beta.Shipping.max_transit_time]
            are required if providing shipping speeds.
            [minHandlingTime][google.shopping.merchant.products.v1beta.Shipping.min_handling_time]
            is optional if
            [maxHandlingTime][google.shopping.merchant.products.v1beta.Shipping.max_handling_time]
            is present.

            This field is a member of `oneof`_ ``_max_handling_time``.
        min_transit_time (int):
            Minimum transit time (inclusive) between when the order has
            shipped and when it is delivered in business days. 0 means
            that the order is delivered on the same day as it ships.
            [minTransitTime][google.shopping.merchant.products.v1beta.Shipping.min_transit_time]
            can only be present together with
            [maxTransitTime][google.shopping.merchant.products.v1beta.Shipping.max_transit_time];
            but it is not required if
            [maxTransitTime][google.shopping.merchant.products.v1beta.Shipping.max_transit_time]
            is present.

            This field is a member of `oneof`_ ``_min_transit_time``.
        max_transit_time (int):
            Maximum transit time (inclusive) between when the order has
            shipped and when it is delivered in business days. 0 means
            that the order is delivered on the same day as it ships.
            Both
            [maxHandlingTime][google.shopping.merchant.products.v1beta.Shipping.max_handling_time]
            and
            [maxTransitTime][google.shopping.merchant.products.v1beta.Shipping.max_transit_time]
            are required if providing shipping speeds.
            [minTransitTime][google.shopping.merchant.products.v1beta.Shipping.min_transit_time]
            is optional if
            [maxTransitTime][google.shopping.merchant.products.v1beta.Shipping.max_transit_time]
            is present.

            This field is a member of `oneof`_ ``_max_transit_time``.
    """

    price: types.Price = proto.Field(
        proto.MESSAGE,
        number=1,
        message=types.Price,
    )
    country: str = proto.Field(
        proto.STRING,
        number=2,
    )
    region: str = proto.Field(
        proto.STRING,
        number=3,
    )
    service: str = proto.Field(
        proto.STRING,
        number=4,
    )
    location_id: int = proto.Field(
        proto.INT64,
        number=5,
    )
    location_group_name: str = proto.Field(
        proto.STRING,
        number=6,
    )
    postal_code: str = proto.Field(
        proto.STRING,
        number=7,
    )
    min_handling_time: int = proto.Field(
        proto.INT64,
        number=8,
        optional=True,
    )
    max_handling_time: int = proto.Field(
        proto.INT64,
        number=9,
        optional=True,
    )
    min_transit_time: int = proto.Field(
        proto.INT64,
        number=10,
        optional=True,
    )
    max_transit_time: int = proto.Field(
        proto.INT64,
        number=11,
        optional=True,
    )


class FreeShippingThreshold(proto.Message):
    r"""Conditions to be met for a product to have free shipping.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        country (str):
            The `CLDR territory
            code <http://www.unicode.org/repos/cldr/tags/latest/common/main/en.xml>`__
            of the country to which an item will ship.

            This field is a member of `oneof`_ ``_country``.
        price_threshold (google.shopping.type.types.Price):
            The minimum product price for the shipping
            cost to become free. Represented as a number.

            This field is a member of `oneof`_ ``_price_threshold``.
    """

    country: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    price_threshold: types.Price = proto.Field(
        proto.MESSAGE,
        number=2,
        optional=True,
        message=types.Price,
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


class Certification(proto.Message):
    r"""Product
    `certification <https://support.google.com/merchants/answer/13528839>`__,
    initially introduced for EU energy efficiency labeling compliance
    using the EU EPREL database.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        certification_authority (str):
            The certification authority, for example
            "European_Commission". Maximum length is 2000 characters.

            This field is a member of `oneof`_ ``_certification_authority``.
        certification_name (str):
            The name of the certification, for example
            "EPREL". Maximum length is 2000 characters.

            This field is a member of `oneof`_ ``_certification_name``.
        certification_code (str):
            The certification code.
            Maximum length is 2000 characters.

            This field is a member of `oneof`_ ``_certification_code``.
        certification_value (str):
            The certification value (also known as class,
            level or grade), for example "A+", "C", "gold".
            Maximum length is 2000 characters.

            This field is a member of `oneof`_ ``_certification_value``.
    """

    certification_authority: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    certification_name: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    certification_code: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    certification_value: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )


class ProductStructuredTitle(proto.Message):
    r"""Structured title, for algorithmically (AI)-generated titles.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        digital_source_type (str):
            The digital source type, for example
            "trained_algorithmic_media". Following
            `IPTC <https://cv.iptc.org/newscodes/digitalsourcetype>`__.
            Maximum length is 40 characters.

            This field is a member of `oneof`_ ``_digital_source_type``.
        content (str):
            The title text
            Maximum length is 150 characters

            This field is a member of `oneof`_ ``_content``.
    """

    digital_source_type: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    content: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )


class ProductStructuredDescription(proto.Message):
    r"""Structured description, for algorithmically (AI)-generated
    descriptions.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        digital_source_type (str):
            The digital source type, for example
            "trained_algorithmic_media". Following
            `IPTC <https://cv.iptc.org/newscodes/digitalsourcetype>`__.
            Maximum length is 40 characters.

            This field is a member of `oneof`_ ``_digital_source_type``.
        content (str):
            The description text
            Maximum length is 5000 characters

            This field is a member of `oneof`_ ``_content``.
    """

    digital_source_type: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    content: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
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


class ProductStatus(proto.Message):
    r"""The status of a product, data validation issues, that is,
    information about a product computed asynchronously.

    Attributes:
        destination_statuses (MutableSequence[google.shopping.merchant_products_v1beta.types.ProductStatus.DestinationStatus]):
            The intended destinations for the product.
        item_level_issues (MutableSequence[google.shopping.merchant_products_v1beta.types.ProductStatus.ItemLevelIssue]):
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
            reporting_context (google.shopping.type.types.ReportingContext.ReportingContextEnum):
                The name of the reporting context.
            approved_countries (MutableSequence[str]):
                List of country codes (ISO 3166-1 alpha-2)
                where the offer is approved.
            pending_countries (MutableSequence[str]):
                List of country codes (ISO 3166-1 alpha-2)
                where the offer is pending approval.
            disapproved_countries (MutableSequence[str]):
                List of country codes (ISO 3166-1 alpha-2)
                where the offer is disapproved.
        """

        reporting_context: types.ReportingContext.ReportingContextEnum = proto.Field(
            proto.ENUM,
            number=1,
            enum=types.ReportingContext.ReportingContextEnum,
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
            severity (google.shopping.merchant_products_v1beta.types.ProductStatus.ItemLevelIssue.Severity):
                How this issue affects serving of the offer.
            resolution (str):
                Whether the issue can be resolved by the
                business.
            attribute (str):
                The attribute's name, if the issue is caused
                by a single attribute.
            reporting_context (google.shopping.type.types.ReportingContext.ReportingContextEnum):
                The reporting context the issue applies to.
            description (str):
                A short issue description in English.
            detail (str):
                A detailed issue description in English.
            documentation (str):
                The URL of a web page to help with resolving
                this issue.
            applicable_countries (MutableSequence[str]):
                List of country codes (ISO 3166-1 alpha-2)
                where issue applies to the offer.
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

        code: str = proto.Field(
            proto.STRING,
            number=1,
        )
        severity: "ProductStatus.ItemLevelIssue.Severity" = proto.Field(
            proto.ENUM,
            number=2,
            enum="ProductStatus.ItemLevelIssue.Severity",
        )
        resolution: str = proto.Field(
            proto.STRING,
            number=3,
        )
        attribute: str = proto.Field(
            proto.STRING,
            number=4,
        )
        reporting_context: types.ReportingContext.ReportingContextEnum = proto.Field(
            proto.ENUM,
            number=5,
            enum=types.ReportingContext.ReportingContextEnum,
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


class CloudExportAdditionalProperties(proto.Message):
    r"""Product property for the Cloud Retail API.
    For example, properties for a TV product could be
    "Screen-Resolution" or "Screen-Size".


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        property_name (str):
            Name of the given property. For example,
            "Screen-Resolution" for a TV product. Maximum
            string size is 256 characters.

            This field is a member of `oneof`_ ``_property_name``.
        text_value (MutableSequence[str]):
            Text value of the given property. For
            example, "8K(UHD)" could be a text value for a
            TV product. Maximum repeatedness of this value
            is 400. Values are stored in an arbitrary but
            consistent order. Maximum string size is 256
            characters.
        bool_value (bool):
            Boolean value of the given property. For
            example for a TV product, "True" or "False" if
            the screen is UHD.

            This field is a member of `oneof`_ ``_bool_value``.
        int_value (MutableSequence[int]):
            Integer values of the given property. For
            example, 1080 for a TV product's Screen
            Resolution. Maximum repeatedness of this value
            is 400. Values are stored in an arbitrary but
            consistent order.
        float_value (MutableSequence[float]):
            Float values of the given property. For
            example for a TV product 1.2345. Maximum
            repeatedness of this value is 400. Values are
            stored in an arbitrary but consistent order.
        min_value (float):
            Minimum float value of the given property.
            For example for a TV product 1.00.

            This field is a member of `oneof`_ ``_min_value``.
        max_value (float):
            Maximum float value of the given property.
            For example for a TV product 100.00.

            This field is a member of `oneof`_ ``_max_value``.
        unit_code (str):
            Unit of the given property. For example,
            "Pixels" for a TV product. Maximum string size
            is 256B.

            This field is a member of `oneof`_ ``_unit_code``.
    """

    property_name: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    text_value: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    bool_value: bool = proto.Field(
        proto.BOOL,
        number=3,
        optional=True,
    )
    int_value: MutableSequence[int] = proto.RepeatedField(
        proto.INT64,
        number=4,
    )
    float_value: MutableSequence[float] = proto.RepeatedField(
        proto.FLOAT,
        number=5,
    )
    min_value: float = proto.Field(
        proto.FLOAT,
        number=6,
        optional=True,
    )
    max_value: float = proto.Field(
        proto.FLOAT,
        number=7,
        optional=True,
    )
    unit_code: str = proto.Field(
        proto.STRING,
        number=8,
        optional=True,
    )


class ProductSustainabilityIncentive(proto.Message):
    r"""Information regarding sustainability-related incentive
    programs such as rebates or tax relief.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        amount (google.shopping.type.types.Price):
            The fixed amount of the incentive.

            This field is a member of `oneof`_ ``value``.
        percentage (float):
            The percentage of the sale price that the
            incentive is applied to.

            This field is a member of `oneof`_ ``value``.
        type_ (google.shopping.merchant_products_v1beta.types.ProductSustainabilityIncentive.Type):
            Sustainability incentive program.

            This field is a member of `oneof`_ ``_type``.
    """

    class Type(proto.Enum):
        r"""Types of supported sustainability incentive programs.

        Values:
            TYPE_UNSPECIFIED (0):
                Unspecified or unknown sustainability
                incentive type.
            EV_TAX_CREDIT (1):
                Program offering tax liability reductions for
                electric vehicles and, in some countries,
                plug-in hybrids. These reductions can be based
                on a specific amount or a percentage of the sale
                price.
            EV_PRICE_DISCOUNT (2):
                A subsidy program, often called an
                environmental bonus, provides a purchase grant
                for electric vehicles and, in some countries,
                plug-in hybrids. The grant amount may be a fixed
                sum or a percentage of the sale price.
        """

        TYPE_UNSPECIFIED = 0
        EV_TAX_CREDIT = 1
        EV_PRICE_DISCOUNT = 2

    amount: types.Price = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="value",
        message=types.Price,
    )
    percentage: float = proto.Field(
        proto.DOUBLE,
        number=3,
        oneof="value",
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=1,
        optional=True,
        enum=Type,
    )


class AutomatedDiscounts(proto.Message):
    r"""Information regarding Automated Discounts.

    Attributes:
        prior_price (google.shopping.type.types.Price):
            The price prior to the application of the
            first price reduction. Absent if the information
            about the prior price of the product is not
            available.
        prior_price_progressive (google.shopping.type.types.Price):
            The price prior to the application of
            consecutive price reductions. Absent if the
            information about the prior price of the product
            is not available.
        gad_price (google.shopping.type.types.Price):
            The current sale price for products with a price optimized
            using Google Automated Discounts (GAD). Absent if the
            information about the GAD_price of the product is not
            available.
    """

    prior_price: types.Price = proto.Field(
        proto.MESSAGE,
        number=1,
        message=types.Price,
    )
    prior_price_progressive: types.Price = proto.Field(
        proto.MESSAGE,
        number=2,
        message=types.Price,
    )
    gad_price: types.Price = proto.Field(
        proto.MESSAGE,
        number=3,
        message=types.Price,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
