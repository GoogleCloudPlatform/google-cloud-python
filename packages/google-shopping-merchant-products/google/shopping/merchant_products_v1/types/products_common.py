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
    package="google.shopping.merchant.products.v1",
    manifest={
        "SubscriptionPeriod",
        "AgeGroup",
        "Availability",
        "Condition",
        "Gender",
        "CreditType",
        "SizeSystem",
        "SizeType",
        "EnergyEfficiencyClass",
        "PickupMethod",
        "PickupSla",
        "Pause",
        "CertificationAuthority",
        "CertificationName",
        "DigitalSourceType",
        "CarrierTransitTimeOption",
        "ProductAttributes",
        "ShippingWeight",
        "ShippingDimension",
        "UnitPricingBaseMeasure",
        "UnitPricingMeasure",
        "SubscriptionCost",
        "ProductInstallment",
        "LoyaltyPoints",
        "LoyaltyProgram",
        "Shipping",
        "FreeShippingThreshold",
        "ProductDetail",
        "ProductCertification",
        "StructuredTitle",
        "StructuredDescription",
        "ProductDimension",
        "ProductWeight",
        "ProductStatus",
        "CloudExportAdditionalProperties",
        "ProductSustainabilityIncentive",
        "AutomatedDiscounts",
        "PickupCost",
        "HandlingCutoffTime",
        "ProductMinimumOrderValue",
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
        WEEK (3):
            Indicates that the subscription period is
            week.
    """

    SUBSCRIPTION_PERIOD_UNSPECIFIED = 0
    MONTH = 1
    YEAR = 2
    WEEK = 3


class AgeGroup(proto.Enum):
    r"""Target `age
    group <https://support.google.com/merchants/answer/6324463>`__ of
    the item.

    Values:
        AGE_GROUP_UNSPECIFIED (0):
            Age group is not specified.
        ADULT (1):
            Teens or older.
        KIDS (2):
            5-13 years old.
        TODDLER (3):
            1-5 years old.
        INFANT (4):
            3-12 months old.
        NEWBORN (5):
            0-3 months old.
    """

    AGE_GROUP_UNSPECIFIED = 0
    ADULT = 1
    KIDS = 2
    TODDLER = 3
    INFANT = 4
    NEWBORN = 5


class Availability(proto.Enum):
    r"""`Availability <https://support.google.com/merchants/answer/6324448>`__
    status of the item.

    Values:
        AVAILABILITY_UNSPECIFIED (0):
            Availability is not specified.
        IN_STOCK (1):
            In stock.
        OUT_OF_STOCK (2):
            Out of stock.
        PREORDER (3):
            Pre-order.
        LIMITED_AVAILABILITY (4):
            Limited availability.
        BACKORDER (5):
            Backorder.
    """

    AVAILABILITY_UNSPECIFIED = 0
    IN_STOCK = 1
    OUT_OF_STOCK = 2
    PREORDER = 3
    LIMITED_AVAILABILITY = 4
    BACKORDER = 5


class Condition(proto.Enum):
    r"""`Condition <https://support.google.com/merchants/answer/6324469>`__
    or state of the item.

    Values:
        CONDITION_UNSPECIFIED (0):
            Default value. This value is unused.
        NEW (1):
            Brand new, original, unopened packaging.
        USED (2):
            Previously used, original packaging opened or
            missing.
        REFURBISHED (3):
            Professionally restored to working order,
            comes with a warranty, may or may not have the
            original packaging.
    """

    CONDITION_UNSPECIFIED = 0
    NEW = 1
    USED = 2
    REFURBISHED = 3


class Gender(proto.Enum):
    r"""Target
    `gender <https://support.google.com/merchants/answer/6324479>`__ of
    the item.

    Values:
        GENDER_UNSPECIFIED (0):
            Gender is not specified.
        MALE (1):
            Male.
        FEMALE (2):
            Female.
        UNISEX (3):
            Unisex.
    """

    GENDER_UNSPECIFIED = 0
    MALE = 1
    FEMALE = 2
    UNISEX = 3


class CreditType(proto.Enum):
    r"""Type of installment payments.

    Values:
        CREDIT_TYPE_UNSPECIFIED (0):
            Default value. This value is unused.
        FINANCE (1):
            Finance.
        LEASE (2):
            Lease.
    """

    CREDIT_TYPE_UNSPECIFIED = 0
    FINANCE = 1
    LEASE = 2


class SizeSystem(proto.Enum):
    r"""System in which the size is specified. Recommended for apparel
    items. For more information, see `Size
    system <https://support.google.com/merchants/answer/6324502>`__.

    Values:
        SIZE_SYSTEM_UNSPECIFIED (0):
            Unspecified size system.
        AU (1):
            AU.
        BR (2):
            BR.
        CN (3):
            CN.
        DE (4):
            DE.
        EU (5):
            EU.
        FR (6):
            FR.
        IT (7):
            IT.
        JP (8):
            JP.
        MEX (9):
            MEX.
        UK (10):
            UK.
        US (11):
            US.
    """

    SIZE_SYSTEM_UNSPECIFIED = 0
    AU = 1
    BR = 2
    CN = 3
    DE = 4
    EU = 5
    FR = 6
    IT = 7
    JP = 8
    MEX = 9
    UK = 10
    US = 11


class SizeType(proto.Enum):
    r"""The cut of the item. It can be used to represent combined size types
    for apparel items. Maximum two of size types can be provided, see
    `Size type <https://support.google.com/merchants/answer/6324497>`__.

    Values:
        SIZE_TYPE_UNSPECIFIED (0):
            The size type is not specified.
        REGULAR (1):
            Regular size.
        PETITE (2):
            Petite size.
        MATERNITY (3):
            Maternity size.
        BIG (4):
            Big size.
        TALL (5):
            Tall size.
        PLUS (6):
            Plus size.
    """

    SIZE_TYPE_UNSPECIFIED = 0
    REGULAR = 1
    PETITE = 2
    MATERNITY = 3
    BIG = 4
    TALL = 5
    PLUS = 6


class EnergyEfficiencyClass(proto.Enum):
    r"""The `energy efficiency
    class <https://support.google.com/merchants/answer/7562785>`__ as
    defined in EU directive 2010/30/EU.

    Values:
        ENERGY_EFFICIENCY_CLASS_UNSPECIFIED (0):
            The energy efficiency class is unspecified.
        APPP (1):
            A+++.
        APP (2):
            A++.
        AP (3):
            A+.
        A (4):
            A.
        B (5):
            B.
        C (6):
            C.
        D (7):
            D.
        E (8):
            E.
        F (9):
            F.
        G (10):
            G.
    """

    ENERGY_EFFICIENCY_CLASS_UNSPECIFIED = 0
    APPP = 1
    APP = 2
    AP = 3
    A = 4
    B = 5
    C = 6
    D = 7
    E = 8
    F = 9
    G = 10


class PickupMethod(proto.Enum):
    r"""The
    `pickup <https://support.google.com/merchants/answer/14634021>`__
    option for the item.

    Values:
        PICKUP_METHOD_UNSPECIFIED (0):
            Pickup method is not specified.
        NOT_SUPPORTED (1):
            The item is not available for store pickup.
        BUY (2):
            The entire transaction occurs online.
        RESERVE (3):
            The item is reserved online and the
            transaction occurs in-store.
        SHIP_TO_STORE (4):
            The item is purchased online and shipped to a
            local store for the customer to pick up.
    """

    PICKUP_METHOD_UNSPECIFIED = 0
    NOT_SUPPORTED = 1
    BUY = 2
    RESERVE = 3
    SHIP_TO_STORE = 4


class PickupSla(proto.Enum):
    r"""Item store pickup timeline. For more information, see `Pickup
    SLA <https://support.google.com/merchants/answer/14635400>`__.

    Values:
        PICKUP_SLA_UNSPECIFIED (0):
            Pickup SLA is not specified.
        SAME_DAY (1):
            Indicates that the product is available for
            pickup the same day that the order is placed,
            subject to cut off times.
        NEXT_DAY (2):
            Indicates that the product is available for
            pickup the following day that the order is
            placed.
        TWO_DAY (3):
            Indicates that the product will be shipped to
            a store for a customer to pick up in 2 days.
        THREE_DAY (4):
            Indicates that the product will be shipped to
            a store for a customer to pick up in 3 days.
        FOUR_DAY (5):
            Indicates that the product will be shipped to
            a store for a customer to pick up in 4 days
        FIVE_DAY (6):
            Indicates that the product will be shipped to
            a store for a customer to pick up in 5 days.
        SIX_DAY (7):
            Indicates that the product will be shipped to
            a store for a customer to pick up in 6 days.
        MULTI_WEEK (8):
            Indicates that the product will be shipped to
            a store for a customer to pick up in one week or
            more.
    """

    PICKUP_SLA_UNSPECIFIED = 0
    SAME_DAY = 1
    NEXT_DAY = 2
    TWO_DAY = 3
    THREE_DAY = 4
    FOUR_DAY = 5
    FIVE_DAY = 6
    SIX_DAY = 7
    MULTI_WEEK = 8


class Pause(proto.Enum):
    r"""Publication of this item will be temporarily
    `paused <https://support.google.com/merchants/answer/11909930>`__.

    Values:
        PAUSE_UNSPECIFIED (0):
            The pause is unspecified.
        ADS (1):
            You’re currently pausing your product for all
            ads locations (including Shopping Ads, Display
            Ads, and local inventory ads).
        ALL (2):
            You’re currently pausing your product for all
            Shopping locations (including Shopping Ads,
            Display Ads, local inventory ads, Buy on Google,
            and free listings).
    """

    PAUSE_UNSPECIFIED = 0
    ADS = 1
    ALL = 2


class CertificationAuthority(proto.Enum):
    r"""The certification authority.

    Values:
        CERTIFICATION_AUTHORITY_UNSPECIFIED (0):
            Certification authority is not specified.
        ADEME (1):
            For the French CO2 emissions class for
            vehicles.
        BMWK (2):
            For the German CO2 emissions classes for
            vehicles.
        EPA (3):
            Environment Protection Agency.
        EC (4):
            European Commission for energy labels in the
            EU.
    """

    CERTIFICATION_AUTHORITY_UNSPECIFIED = 0
    ADEME = 1
    BMWK = 2
    EPA = 3
    EC = 4


class CertificationName(proto.Enum):
    r"""The name of the certification.

    Values:
        CERTIFICATION_NAME_UNSPECIFIED (0):
            Certification name is not specified.
        ENERGY_STAR (1):
            Energy Star.
        ENERGY_STAR_MOST_EFFICIENT (2):
            Energy Star Most Efficient.
        EPREL (3):
            Represents energy efficiency certifications
            in the EU European Registry for Energy Labeling
            (EPREL) database.
        EU_ECOLABEL (4):
            EU Ecolabel.
        VEHICLE_ENERGY_EFFICIENCY (5):
            The overall CO2 class of a vehicle
        VEHICLE_ENERGY_EFFICIENCY_DISCHARGED_BATTERY (6):
            For the CO2 class of a vehicle with a
            discharged battery.
    """

    CERTIFICATION_NAME_UNSPECIFIED = 0
    ENERGY_STAR = 1
    ENERGY_STAR_MOST_EFFICIENT = 2
    EPREL = 3
    EU_ECOLABEL = 4
    VEHICLE_ENERGY_EFFICIENCY = 5
    VEHICLE_ENERGY_EFFICIENCY_DISCHARGED_BATTERY = 6


class DigitalSourceType(proto.Enum):
    r"""The digital source type. Following
    `IPTC <https://cv.iptc.org/newscodes/digitalsourcetype>`__.

    Values:
        DIGITAL_SOURCE_TYPE_UNSPECIFIED (0):
            Digital source type is unspecified.
        TRAINED_ALGORITHMIC_MEDIA (1):
            Text created algorithmically using a model
            derived from sampled content.
        DEFAULT (2):
            Text NOT created algorithmically using a
            model derived from sampled content (the default)
    """

    DIGITAL_SOURCE_TYPE_UNSPECIFIED = 0
    TRAINED_ALGORITHMIC_MEDIA = 1
    DEFAULT = 2


class CarrierTransitTimeOption(proto.Enum):
    r"""Possible carrier where transit time is coming from.

    Values:
        CARRIER_TRANSIT_TIME_OPTION_UNSPECIFIED (0):
            Carrier transit time option is unspecified.
        DHL_PAKET (1):
            DHL Paket shipping service.
        DHL_PACKCHEN (2):
            DHL Packchen shipping service.
        DHL_EXPRESSEASY (3):
            DHL Express Easy shipping service.
        DPD_EXPRESS (4):
            DPD Express shipping service.
        DPD_CLASSIC_PARCEL (5):
            DPD Classic Parcel shipping service.
        HERMES_HAUSTUR (6):
            Hermes Haustur shipping service.
        HERMES_PAKETSHOP (7):
            Hermes Paketshop shipping service.
        GLS_BUSINESS (8):
            GLS Business shipping service.
        GLS_EXPRESS (9):
            GLS Express shipping service.
        GLS_PRIVATE (10):
            GLS Private shipping service.
        COLISSIMO_DOMICILE (11):
            Colissimo Domicile shipping service.
        DHL_EXPRESS_12AM (12):
            DHL Express 12 AM shipping service.
        DHL_EXPRESS_9AM (13):
            DHL Express 9 AM shipping service.
        GEODIS_EXPRESS (14):
            GEODIS Express shipping service.
        GEODIS_PACK_30 (15):
            GEODIS Pack 30 shipping service.
        GEODIS_SAME_DAY (16):
            GEODIS Same Day shipping service.
        GEODIS_TOP_24 (17):
            GEODIS Top 24 shipping service.
        TNT_ESSENTIEL_24H (18):
            TNT Essentiel 24H shipping service.
        TNT_ESSENTIEL_FLEXIBILITE (19):
            TNT Essentiel Flexibilite shipping service.
        FEDEX_GROUND (20):
            FedEx Ground shipping service.
        FEDEX_HOME_DELIVERY (21):
            FedEx Home Delivery shipping service.
        FEDEX_EXPRESS_SAVER (22):
            FedEx Express Saver shipping service.
        FEDEX_FIRST_OVERNIGHT (23):
            FedEx First Overnight shipping service.
        FEDEX_PRIORITY_OVERNIGHT (24):
            FedEx Priority Overnight shipping service.
        FEDEX_STANDARD_OVERNIGHT (25):
            FedEx Standard Overnight shipping service.
        FEDEX_2DAY (26):
            FedEx 2Day shipping service.
        UPS_2ND_DAY_AIR (27):
            UPS 2nd Day Air shipping service.
        UPS_2ND_DAY_AM (28):
            UPS 2nd Day AM shipping service.
        UPS_3_DAY_SELECT (29):
            UPS 3 Day Select shipping service.
        UPS_GROUND (30):
            UPS Ground shipping service.
        UPS_NEXT_DAY_AIR (31):
            UPS Next Day Air shipping service.
        UPS_NEXT_DAY_AIR_EARLY_AM (32):
            UPS Next Day Air Early AM shipping service.
        UPS_NEXT_DAY_AIR_SAVER (33):
            UPS Next Day Air Saver shipping service.
        USPS_PRIORITY_MAIL_EXPRESS (34):
            USPS Priority Mail Express shipping service.
        USPS_MEDIA_MAIL (35):
            USPS Media Mail shipping service.
        USPS_GROUND_ADVANTAGE_RETAIL (36):
            USPS Ground Advantage Retail shipping
            service.
        USPS_PRIORITY_MAIL (37):
            USPS Priority Mail shipping service.
        USPS_GROUND_ADVANTAGE_COMMERCIAL (38):
            USPS Ground Advantage Commercial shipping
            service.
        USPS_FIRST_CLASS_MAIL (39):
            USPS First Class Mail shipping service.
    """

    CARRIER_TRANSIT_TIME_OPTION_UNSPECIFIED = 0
    DHL_PAKET = 1
    DHL_PACKCHEN = 2
    DHL_EXPRESSEASY = 3
    DPD_EXPRESS = 4
    DPD_CLASSIC_PARCEL = 5
    HERMES_HAUSTUR = 6
    HERMES_PAKETSHOP = 7
    GLS_BUSINESS = 8
    GLS_EXPRESS = 9
    GLS_PRIVATE = 10
    COLISSIMO_DOMICILE = 11
    DHL_EXPRESS_12AM = 12
    DHL_EXPRESS_9AM = 13
    GEODIS_EXPRESS = 14
    GEODIS_PACK_30 = 15
    GEODIS_SAME_DAY = 16
    GEODIS_TOP_24 = 17
    TNT_ESSENTIEL_24H = 18
    TNT_ESSENTIEL_FLEXIBILITE = 19
    FEDEX_GROUND = 20
    FEDEX_HOME_DELIVERY = 21
    FEDEX_EXPRESS_SAVER = 22
    FEDEX_FIRST_OVERNIGHT = 23
    FEDEX_PRIORITY_OVERNIGHT = 24
    FEDEX_STANDARD_OVERNIGHT = 25
    FEDEX_2DAY = 26
    UPS_2ND_DAY_AIR = 27
    UPS_2ND_DAY_AM = 28
    UPS_3_DAY_SELECT = 29
    UPS_GROUND = 30
    UPS_NEXT_DAY_AIR = 31
    UPS_NEXT_DAY_AIR_EARLY_AM = 32
    UPS_NEXT_DAY_AIR_SAVER = 33
    USPS_PRIORITY_MAIL_EXPRESS = 34
    USPS_MEDIA_MAIL = 35
    USPS_GROUND_ADVANTAGE_RETAIL = 36
    USPS_PRIORITY_MAIL = 37
    USPS_GROUND_ADVANTAGE_COMMERCIAL = 38
    USPS_FIRST_CLASS_MAIL = 39


class ProductAttributes(proto.Message):
    r"""Product attributes.

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
        age_group (google.shopping.merchant_products_v1.types.AgeGroup):
            Target `age
            group <https://support.google.com/merchants/answer/6324463>`__
            of the item.

            This field is a member of `oneof`_ ``_age_group``.
        availability (google.shopping.merchant_products_v1.types.Availability):
            `Availability <https://support.google.com/merchants/answer/6324448>`__
            status of the item.

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
        condition (google.shopping.merchant_products_v1.types.Condition):
            `Condition <https://support.google.com/merchants/answer/6324469>`__
            or state of the item.

            This field is a member of `oneof`_ ``_condition``.
        gender (google.shopping.merchant_products_v1.types.Gender):
            Target
            `gender <https://support.google.com/merchants/answer/6324479>`__
            of the item.

            This field is a member of `oneof`_ ``_gender``.
        google_product_category (str):
            Google's category of the item (see `Google product
            taxonomy <https://support.google.com/merchants/answer/1705911>`__).
            When querying products, this field will contain the user
            provided value. There is currently no way to get back the
            auto assigned google product categories through the API.

            This field is a member of `oneof`_ ``_google_product_category``.
        gtins (MutableSequence[str]):
            Global Trade Item Numbers
            (`GTIN <https://support.google.com/merchants/answer/6324461>`__)
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
            (`MPN <https://support.google.com/merchants/answer/6324482>`__)
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
        installment (google.shopping.merchant_products_v1.types.ProductInstallment):
            Number and amount of installments to pay for
            an item.
        subscription_cost (google.shopping.merchant_products_v1.types.SubscriptionCost):
            Number of periods (weeks, months or years)
            and amount of payment per period for an item
            with an associated subscription contract.
        loyalty_points (google.shopping.merchant_products_v1.types.LoyaltyPoints):
            Loyalty points that users receive after
            purchasing the item. Japan only.
        loyalty_programs (MutableSequence[google.shopping.merchant_products_v1.types.LoyaltyProgram]):
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
        product_height (google.shopping.merchant_products_v1.types.ProductDimension):
            The height of the product in the units
            provided. The value must be between
            0 (exclusive) and 3000 (inclusive).
        product_length (google.shopping.merchant_products_v1.types.ProductDimension):
            The length of the product in the units
            provided. The value must be between 0
            (exclusive) and 3000 (inclusive).
        product_width (google.shopping.merchant_products_v1.types.ProductDimension):
            The width of the product in the units
            provided. The value must be between 0
            (exclusive) and 3000 (inclusive).
        product_weight (google.shopping.merchant_products_v1.types.ProductWeight):
            The weight of the product in the units
            provided. The value must be between 0
            (exclusive) and 2000 (inclusive).
        shipping (MutableSequence[google.shopping.merchant_products_v1.types.Shipping]):
            Shipping rules.
        carrier_shipping (MutableSequence[google.shopping.merchant_products_v1.types.ProductAttributes.CarrierShipping]):
            Rules for carrier-based shipping.
        free_shipping_threshold (MutableSequence[google.shopping.merchant_products_v1.types.FreeShippingThreshold]):
            Conditions to be met for a product to have
            free shipping.
        shipping_weight (google.shopping.merchant_products_v1.types.ShippingWeight):
            Weight of the item for shipping.
        shipping_length (google.shopping.merchant_products_v1.types.ShippingDimension):
            Length of the item for shipping.
        shipping_width (google.shopping.merchant_products_v1.types.ShippingDimension):
            Width of the item for shipping.
        shipping_height (google.shopping.merchant_products_v1.types.ShippingDimension):
            Height of the item for shipping.
        max_handling_time (int):
            Maximal product handling time (in business
            days).

            This field is a member of `oneof`_ ``_max_handling_time``.
        min_handling_time (int):
            Minimal product handling time (in business
            days).

            This field is a member of `oneof`_ ``_min_handling_time``.
        shipping_handling_business_days (MutableSequence[google.shopping.merchant_products_v1.types.ProductAttributes.ShippingBusinessDaysConfig]):
            The business days during which orders can be
            handled. If not provided, Monday to Friday
            business days will be assumed.
        shipping_transit_business_days (MutableSequence[google.shopping.merchant_products_v1.types.ProductAttributes.ShippingBusinessDaysConfig]):
            The business days during which orders are in
            transit. If not provided, Monday to Friday
            business days will be assumed.
        handling_cutoff_times (MutableSequence[google.shopping.merchant_products_v1.types.HandlingCutoffTime]):
            The handling cutoff times for shipping.
        shipping_label (str):
            The shipping label of the product, used to group products in
            account-level shipping rules. Max. 100 characters. For more
            information, see `Shipping
            label <https://support.google.com/merchants/answer/6324504>`__.

            This field is a member of `oneof`_ ``_shipping_label``.
        return_policy_label (str):
            The return label of the product, used to group products in
            account-level return policies. Max. 100 characters. For more
            information, see `Return policy
            label <https://support.google.com/merchants/answer/9445425>`__.

            This field is a member of `oneof`_ ``_return_policy_label``.
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
        size_system (google.shopping.merchant_products_v1.types.SizeSystem):
            System in which the size is specified. Recommended for
            apparel items. For more information, see `Size
            system <https://support.google.com/merchants/answer/6324502>`__.

            This field is a member of `oneof`_ ``_size_system``.
        size_types (MutableSequence[google.shopping.merchant_products_v1.types.SizeType]):
            The cut of the item. It can be used to represent combined
            size types for apparel items. Maximum two of size types can
            be provided, see `Size
            type <https://support.google.com/merchants/answer/6324497>`__.
        energy_efficiency_class (google.shopping.merchant_products_v1.types.EnergyEfficiencyClass):
            The `energy efficiency
            class <https://support.google.com/merchants/answer/7562785>`__
            as defined in EU directive 2010/30/EU.

            This field is a member of `oneof`_ ``_energy_efficiency_class``.
        min_energy_efficiency_class (google.shopping.merchant_products_v1.types.EnergyEfficiencyClass):
            The `energy efficiency
            class <https://support.google.com/merchants/answer/7562785>`__
            as defined in EU directive 2010/30/EU.

            This field is a member of `oneof`_ ``_min_energy_efficiency_class``.
        max_energy_efficiency_class (google.shopping.merchant_products_v1.types.EnergyEfficiencyClass):
            The `energy efficiency
            class <https://support.google.com/merchants/answer/7562785>`__
            as defined in EU directive 2010/30/EU.

            This field is a member of `oneof`_ ``_max_energy_efficiency_class``.
        unit_pricing_measure (google.shopping.merchant_products_v1.types.UnitPricingMeasure):
            The measure and dimension of an item.
        unit_pricing_base_measure (google.shopping.merchant_products_v1.types.UnitPricingBaseMeasure):
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
        product_details (MutableSequence[google.shopping.merchant_products_v1.types.ProductDetail]):
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
        pickup_method (google.shopping.merchant_products_v1.types.PickupMethod):
            The
            `pickup <https://support.google.com/merchants/answer/14634021>`__
            option for the item.

            This field is a member of `oneof`_ ``_pickup_method``.
        pickup_sla (google.shopping.merchant_products_v1.types.PickupSla):
            Item store pickup timeline. For more information, see
            `Pickup
            SLA <https://support.google.com/merchants/answer/14635400>`__.

            This field is a member of `oneof`_ ``_pickup_sla``.
        pickup_cost (google.shopping.merchant_products_v1.types.PickupCost):
            Optional. The `pickup
            cost <https://support.google.com/merchants/answer/16988704>`__
            for an item when a customer buys it online and picks it up
            at a store.

            This field is a member of `oneof`_ ``_pickup_cost``.
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
        included_destinations (MutableSequence[google.shopping.type.types.Destination.DestinationEnum]):
            The list of destinations to include for this target
            (corresponds to checked check boxes in Merchant Center).
            Default destinations are always included unless provided in
            ``excludedDestinations``.

            For more information, see `Included
            destination <https://support.google.com/merchants/answer/7501026>`__.

            Note: We recommend setting destinations on datasources level
            for most use cases. Use this field within products to only
            setup exceptions.
        excluded_destinations (MutableSequence[google.shopping.type.types.Destination.DestinationEnum]):
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
        pause (google.shopping.merchant_products_v1.types.Pause):
            Publication of this item will be temporarily
            `paused <https://support.google.com/merchants/answer/11909930>`__.

            This field is a member of `oneof`_ ``_pause``.
        lifestyle_image_links (MutableSequence[str]):
            Additional URLs of lifestyle images of the item, used to
            explicitly identify images that showcase your item in a
            real-world context. See the `Help Center
            article <https://support.google.com/merchants/answer/9103186>`__
            for more information.
        cloud_export_additional_properties (MutableSequence[google.shopping.merchant_products_v1.types.CloudExportAdditionalProperties]):
            Extra fields to export to the Cloud Retail
            program.
        virtual_model_link (str):
            URL of the 3D image of the item. See the `Help Center
            article <https://support.google.com/merchants/answer/13674896>`__
            for more information.

            This field is a member of `oneof`_ ``_virtual_model_link``.
        certifications (MutableSequence[google.shopping.merchant_products_v1.types.ProductCertification]):
            Product Certifications, for example for energy efficiency
            labeling of products recorded in the `EU
            EPREL <https://eprel.ec.europa.eu/screen/home>`__ database.
            For more information, see
            `Certification <https://support.google.com/merchants/answer/13528839>`__.
        structured_title (google.shopping.merchant_products_v1.types.StructuredTitle):
            Structured title, for algorithmically
            (AI)-generated titles.

            This field is a member of `oneof`_ ``_structured_title``.
        structured_description (google.shopping.merchant_products_v1.types.StructuredDescription):
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
        sustainability_incentives (MutableSequence[google.shopping.merchant_products_v1.types.ProductSustainabilityIncentive]):
            The list of sustainability incentive
            programs.
        video_links (MutableSequence[str]):
            Optional. A list of video URLs for the item. Use this
            attribute to provide more visuals for your product beyond
            your image attributes. See the `Help Center
            article <https://support.google.com/merchants/answer/15216925>`__
            for more information.
        minimum_order_values (MutableSequence[google.shopping.merchant_products_v1.types.ProductMinimumOrderValue]):
            The `minimum
            value <https://support.google.com/merchants/answer/16989009>`__
            in the cart before a customer can initiate checkout.
            Supports multiple minimum order values. Different minimum
            order values can be specified per country, service and
            surface. Maximum entries: 100.
        warranty (google.shopping.merchant_products_v1.types.ProductAttributes.Warranty):
            The
            `warranty <https://support.google.com/merchants/answer/15957626>`__
            of the product.
        vin (str):
            The `Vehicle Identification Number
            (VIN) <https://support.google.com/google-ads/answer/14154510>`__
            of the vehicle.
        model (str):
            The
            `Model <https://support.google.com/google-ads/answer/14154511>`__
            of the vehicle, such as ``LX``, ``EX``, and others.
        trim (str):
            The
            `Trim <https://support.google.com/google-ads/answer/14154176>`__
            of the vehicle model, such as ``S``, ``SV``, ``SL`` and
            others.
        body_style (google.shopping.merchant_products_v1.types.ProductAttributes.VehicleBodyStyle):
            The `body
            style <https://support.google.com/google-ads/answer/14157085>`__
            of the vehicle.
        year (int):
            The
            `Year <https://support.google.com/google-ads/answer/14152816>`__
            of the vehicle model.
        mileage (google.shopping.merchant_products_v1.types.ProductAttributes.Mileage):
            The number of miles/kms on the vehicle. See the
            `Mileage <https://support.google.com/google-ads/answer/14156166>`__
            for more information.
        electric_range (google.shopping.merchant_products_v1.types.ProductAttributes.Mileage):
            The `electric
            range <https://support.google.com/google-ads/answer/15162232>`__
            of the vehicle in miles/kms.
        fuel_consumption (google.shopping.merchant_products_v1.types.ProductAttributes.FuelConsumption):
            The `fuel
            consumption <https://support.google.com/google-ads/answer/14543580>`__
            of the vehicle.
        fuel_consumption_discharged_battery (google.shopping.merchant_products_v1.types.ProductAttributes.FuelConsumption):
            The fuel consumption of the vehicle when the hybrid battery
            is discharged. See the `Help Center
            article <https://support.google.com/google-ads/answer/15162033>`__
            for more information.
        energy_consumption (google.shopping.merchant_products_v1.types.ProductAttributes.EnergyConsumption):
            The `energy
            consumption <https://support.google.com/google-ads/answer/14546149>`__
            of the vehicle.
        co2_emissions (google.shopping.merchant_products_v1.types.ProductAttributes.Co2Emissions):
            The `co2
            emission <https://support.google.com/google-ads/answer/14546146>`__
            of the vehicle.
        date_first_registered (str):
            The date the vehicle was first registered. Format:
            ``YYYY-MM``. See the `Date first
            registered <https://support.google.com/google-ads/answer/14546138>`__
            for more information.
        engine (google.shopping.merchant_products_v1.types.ProductAttributes.EngineType):
            The
            `engine <https://support.google.com/google-ads/answer/14156068>`__
            type of the vehicle.
        emissions_standard (google.shopping.merchant_products_v1.types.ProductAttributes.EmissionsStandard):
            The `emission
            standard <https://support.google.com/google-ads/answer/14869021>`__
            of the vehicle.
        certified_pre_owned (bool):
            Whether the vehicle is OEM `certified
            pre-owned <https://support.google.com/google-ads/answer/14156475>`__.
        vehicle_msrp (google.shopping.type.types.Price):
            The MSRP (Manufacturer Suggested Retail Price) for the
            vehicle in its current configuration. See the `Vehicle
            MSRP <https://support.google.com/google-ads/answer/14154171>`__
            for more information.
        vehicle_all_in_price (google.shopping.type.types.Price):
            The all-in advertised price for a vehicle, which includes
            costs for the following – any accessories attached to the
            vehicle, environmental levies, extra warranty, fuel,
            freight, pre-delivery inspection (PDI), dealer fees for
            handling licensing, provincial regulatory fees,
            miscellaneous dealer charges for security etching and
            nitrogen tire fill, and factory-to-customer or
            dealer-to-customer discounts or incentives. See the `Vehicle
            all-in
            price <https://support.google.com/google-ads/answer/14156981>`__
            for more information.
        vehicle_price_type (google.shopping.merchant_products_v1.types.ProductAttributes.VehiclePriceType):
            The `price
            type <https://support.google.com/google-ads/answer/14592783>`__
            of the vehicle.
        vehicle_mandatory_inspection_included (bool):
            Whether the vehicle is sold with mandatory inspection and
            maintenance performed before delivery. See the `Vehicle
            mandatory inspection
            included <https://support.google.com/google-ads/answer/15956630>`__
            for more information.\`
        vehicle_expenses (google.shopping.type.types.Price):
            The miscellaneous expenses like insurance and registration
            fees of the vehicle. See the `Vehicle
            expenses <https://support.google.com/google-ads/answer/15957154>`__
            for more information.
        returns (MutableSequence[google.shopping.merchant_products_v1.types.ProductAttributes.Returns]):
            Optional. `Return
            rules <https://support.google.com/merchants/answer/17081382>`__
            for the product.
        display_address (google.shopping.merchant_products_v1.types.ProductAttributes.DisplayAddress):
            The display address of the property.
        latitude (float):
            The latitude of the property. The value must
            be between -90 (inclusive) and 90 (inclusive),
            up to 6 decimal places.

            This field is a member of `oneof`_ ``_latitude``.
        longitude (float):
            The longitude of the property. The value must
            be between -180 (inclusive) and 180 (inclusive),
            up to 6 decimal places.

            This field is a member of `oneof`_ ``_longitude``.
        neighborhood (str):
            The neighborhood (locality) of the property, such as
            ``Wallingford``, ``Greenwood``, etc.
        unit_area (google.shopping.merchant_products_v1.types.ProductAttributes.UnitArea):
            The unit area of the property, such as ``1000 sqft``.
        number_of_units (int):
            The number of units available for a specific
            floor plan of the property. The value must be
            greater than 0.

            This field is a member of `oneof`_ ``_number_of_units``.
        property_name (str):
            The name of the property.
        number_of_bedrooms (float):
            The number of bedrooms in the property. The
            value must be greater than or equal to 0 and a
            multiple of 1.0.

            This field is a member of `oneof`_ ``_number_of_bedrooms``.
        number_of_bathrooms (float):
            The number of bathrooms in the property. The
            value must be greater than 0 and a multiple of
            0.5.

            This field is a member of `oneof`_ ``_number_of_bathrooms``.
        property_type (google.shopping.merchant_products_v1.types.ProductAttributes.PropertyType):
            The type of property.
        amenity_feature (MutableSequence[google.shopping.merchant_products_v1.types.ProductAttributes.AmenityFeature]):
            The amenity features for the property.
        utilities_included (MutableSequence[google.shopping.merchant_products_v1.types.ProductAttributes.UtilitiesIncluded]):
            The utilities included for the property.
        pet_policy (google.shopping.merchant_products_v1.types.ProductAttributes.PetPolicy):
            The pet policy for the property.
        specialty_housing_type (google.shopping.merchant_products_v1.types.ProductAttributes.SpecialtyHousingType):
            The specialty housing type for the property.
        product_fee (MutableSequence[google.shopping.merchant_products_v1.types.ProductAttributes.ProductFee]):
            The product fee for the property.
        short_title (str):
            The short title of the item.

            This field is a member of `oneof`_ ``_short_title``.
        lease_term (google.shopping.merchant_products_v1.types.ProductAttributes.LeaseTerm):
            The lease term of the property.
        questions_and_answers (MutableSequence[google.shopping.merchant_products_v1.types.ProductAttributes.QuestionAndAnswer]):
            Optional. Contains user-, merchant-, and
            manufacturer-authored `questions and
            answers <https://support.google.com/merchants/answer/17085211>`__
            about the product. Max 30 question and answer pairs. Max
            10000 characters total. Each question can have max 1000
            characters. Each answer can have max 1000 characters.
        popularity_rank (float):
            Optional. Indicates the
            `popularity <https://support.google.com/merchants/answer/17085297>`__
            of the product in a merchant's inventory. Using a scale of
            0.0 (lowest) to 100.0 (highest).
        item_group_title (str):
            Optional. Represents the `title of the product
            group <https://support.google.com/merchants/answer/17085146>`__
            to which this variant product belongs. This can be used
            along with the `item group
            id <https://support.google.com/merchants/answer/6324507>`__
            attribute. It lets you perform better grouping of variant
            products, and helps identifying common product
            characteristics more efficiently.
        document_links (MutableSequence[str]):
            Optional. Contains a list of PDF `document
            URLs <https://support.google.com/merchants/answer/17084656>`__
            for the product. Examples are training manuals, user guides,
            assembly instructions, package inserts, etc. Must start with
            "http://" or "https://"), ASCII characters only, and RFC
            3986 compliant.
        variant_options (MutableSequence[google.shopping.merchant_products_v1.types.ProductAttributes.VariantOption]):
            Optional. Contains the `list of all variant-identifying
            options <https://support.google.com/merchants/answer/17085214>`__
            of this product.
        related_products (MutableSequence[google.shopping.merchant_products_v1.types.ProductAttributes.RelatedProduct]):
            Optional. Specifies how other `products are
            related <https://support.google.com/merchants/answer/17085213>`__
            to this product.
    """

    class CarrierPriceOption(proto.Enum):
        r"""Possible carrier where price is coming from.

        Values:
            CARRIER_PRICE_OPTION_UNSPECIFIED (0):
                Carrier price option is unspecified.
            AUSTRALIA_POST_REGULAR (1):
                Australia Post Regular shipping service.
            AUSTRALIA_POST_EXPRESS (2):
                Australia Post Express shipping service.
            AUSTRALIA_POST_REGULAR_S (3):
                Australia Post Regular Small shipping
                service.
            AUSTRALIA_POST_REGULAR_M (4):
                Australia Post Regular Medium shipping
                service.
            AUSTRALIA_POST_REGULAR_L (5):
                Australia Post Regular Large shipping
                service.
            AUSTRALIA_POST_REGULAR_XL (6):
                Australia Post Regular XL shipping service.
            AUSTRALIA_POST_EXPRESS_S (7):
                Australia Post Express Small shipping
                service.
            AUSTRALIA_POST_EXPRESS_M (8):
                Australia Post Express Medium shipping
                service.
            AUSTRALIA_POST_EXPRESS_L (9):
                Australia Post Express Large shipping
                service.
            AUSTRALIA_POST_EXPRESS_XL (10):
                Australia Post Express XL shipping service.
            TNT_ROAD_EXPRESS (11):
                TNT Road Express shipping service.
            TNT_OVERNIGHT_EXPRESS (12):
                TNT Overnight Express shipping service.
            TOLL_ROAD_DELIVERY (13):
                Toll Road Delivery shipping service.
            TOLL_OVERNIGHT_PRIORITY (14):
                Toll Overnight Priority shipping service.
            DHL_PAKET (15):
                DHL Paket shipping service.
            DHL_PACKCHEN (16):
                DHL Packchen shipping service.
            DPD_EXPRESS_12 (17):
                DPD Express 12 shipping service.
            DPD_EXPRESS (18):
                DPD Express shipping service.
            DPD_CLASSIC_PARCEL (19):
                DPD Classic Parcel shipping service.
            HERMES_PACKCHEN (20):
                Hermes Packchen shipping service.
            HERMES_PAKETKLASSE_S (21):
                Hermes Paketklasse S shipping service.
            HERMES_PAKETKLASSE_M (22):
                Hermes Paketklasse M shipping service.
            HERMES_PAKETKLASSE_L (23):
                Hermes Paketklasse L shipping service.
            UPS_EXPRESS (24):
                UPS Express shipping service.
            UPS_EXPRESS_SAVER (25):
                UPS Express Saver shipping service.
            UPS_EXPRESS_STANDARD (26):
                UPS Express Standard shipping service.
            DHL_EXPRESS (27):
                DHL Express shipping service.
            DHL_EXPRESS_12 (28):
                DHL Express 12 shipping service.
            DPD_NEXT_DAY (29):
                DPD Next Day shipping service.
            DPD_STANDARD_NEXT_DAY (30):
                DPD Standard Next Day shipping service.
            DPD_STANDARD_TWO_DAY (31):
                DPD Standard Two Day shipping service.
            RMG_1ST_CLASS_SMALL (32):
                RMG 1st Class Small shipping service.
            RMG_1ST_CLASS_MEDIUM (33):
                RMG 1st Class Medium shipping service.
            RMG_2ND_CLASS_SMALL (34):
                RMG 2nd Class Small shipping service.
            RMG_2ND_CLASS_MEDIUM (35):
                RMG 2nd Class Medium shipping service.
            TNT_EXPRESS (36):
                TNT Express shipping service.
            TNT_EXPRESS_10 (37):
                TNT Express 10 shipping service.
            TNT_EXPRESS_12 (38):
                TNT Express 12 shipping service.
            YODEL_B2C_48HR (39):
                Yodel B2C 48HR shipping service.
            YODEL_B2C_72HR (40):
                Yodel B2C 72HR shipping service.
            YODEL_B2C_PACKET (41):
                Yodel B2C Packet shipping service.
            FEDEX_GROUND (42):
                FedEx Ground shipping service.
            FEDEX_HOME_DELIVERY (43):
                FedEx Home Delivery shipping service.
            FEDEX_EXPRESS_SAVER (44):
                FedEx Express Saver shipping service.
            FEDEX_FIRST_OVERNIGHT (45):
                FedEx First Overnight shipping service.
            FEDEX_PRIORITY_OVERNIGHT (46):
                FedEx Priority Overnight shipping service.
            FEDEX_STANDARD_OVERNIGHT (47):
                FedEx Standard Overnight shipping service.
            FEDEX_2DAY (48):
                FedEx 2Day shipping service.
            UPS_STANDARD (49):
                UPS Standard shipping service.
            UPS_2ND_DAY_AIR (50):
                UPS 2nd Day Air shipping service.
            UPS_2ND_DAY_AM (51):
                UPS 2nd Day AM shipping service.
            UPS_3_DAY_SELECT (52):
                UPS 3 Day Select shipping service.
            UPS_GROUND (53):
                UPS Ground shipping service.
            UPS_NEXT_DAY_AIR (54):
                UPS Next Day Air shipping service.
            UPS_NEXT_DAY_AIR_EARLY_AM (55):
                UPS Next Day Air Early AM shipping service.
            UPS_NEXT_DAY_AIR_SAVER (56):
                UPS Next Day Air Saver shipping service.
            USPS_PRIORITY_MAIL_EXPRESS (57):
                USPS Priority Mail Express shipping service.
            USPS_MEDIA_MAIL (58):
                USPS Media Mail shipping service.
            USPS_GROUND_ADVANTAGE_RETAIL (59):
                USPS Ground Advantage Retail shipping
                service.
            USPS_PRIORITY_MAIL (60):
                USPS Priority Mail shipping service.
            USPS_GROUND_ADVANTAGE_COMMERCIAL (61):
                USPS Ground Advantage Commercial shipping
                service.
        """

        CARRIER_PRICE_OPTION_UNSPECIFIED = 0
        AUSTRALIA_POST_REGULAR = 1
        AUSTRALIA_POST_EXPRESS = 2
        AUSTRALIA_POST_REGULAR_S = 3
        AUSTRALIA_POST_REGULAR_M = 4
        AUSTRALIA_POST_REGULAR_L = 5
        AUSTRALIA_POST_REGULAR_XL = 6
        AUSTRALIA_POST_EXPRESS_S = 7
        AUSTRALIA_POST_EXPRESS_M = 8
        AUSTRALIA_POST_EXPRESS_L = 9
        AUSTRALIA_POST_EXPRESS_XL = 10
        TNT_ROAD_EXPRESS = 11
        TNT_OVERNIGHT_EXPRESS = 12
        TOLL_ROAD_DELIVERY = 13
        TOLL_OVERNIGHT_PRIORITY = 14
        DHL_PAKET = 15
        DHL_PACKCHEN = 16
        DPD_EXPRESS_12 = 17
        DPD_EXPRESS = 18
        DPD_CLASSIC_PARCEL = 19
        HERMES_PACKCHEN = 20
        HERMES_PAKETKLASSE_S = 21
        HERMES_PAKETKLASSE_M = 22
        HERMES_PAKETKLASSE_L = 23
        UPS_EXPRESS = 24
        UPS_EXPRESS_SAVER = 25
        UPS_EXPRESS_STANDARD = 26
        DHL_EXPRESS = 27
        DHL_EXPRESS_12 = 28
        DPD_NEXT_DAY = 29
        DPD_STANDARD_NEXT_DAY = 30
        DPD_STANDARD_TWO_DAY = 31
        RMG_1ST_CLASS_SMALL = 32
        RMG_1ST_CLASS_MEDIUM = 33
        RMG_2ND_CLASS_SMALL = 34
        RMG_2ND_CLASS_MEDIUM = 35
        TNT_EXPRESS = 36
        TNT_EXPRESS_10 = 37
        TNT_EXPRESS_12 = 38
        YODEL_B2C_48HR = 39
        YODEL_B2C_72HR = 40
        YODEL_B2C_PACKET = 41
        FEDEX_GROUND = 42
        FEDEX_HOME_DELIVERY = 43
        FEDEX_EXPRESS_SAVER = 44
        FEDEX_FIRST_OVERNIGHT = 45
        FEDEX_PRIORITY_OVERNIGHT = 46
        FEDEX_STANDARD_OVERNIGHT = 47
        FEDEX_2DAY = 48
        UPS_STANDARD = 49
        UPS_2ND_DAY_AIR = 50
        UPS_2ND_DAY_AM = 51
        UPS_3_DAY_SELECT = 52
        UPS_GROUND = 53
        UPS_NEXT_DAY_AIR = 54
        UPS_NEXT_DAY_AIR_EARLY_AM = 55
        UPS_NEXT_DAY_AIR_SAVER = 56
        USPS_PRIORITY_MAIL_EXPRESS = 57
        USPS_MEDIA_MAIL = 58
        USPS_GROUND_ADVANTAGE_RETAIL = 59
        USPS_PRIORITY_MAIL = 60
        USPS_GROUND_ADVANTAGE_COMMERCIAL = 61

    class VehicleBodyStyle(proto.Enum):
        r"""The vehicle body style. See the `Body
        style <https://support.google.com/google-ads/answer/14157085>`__ for
        more information.

        Values:
            VEHICLE_BODY_STYLE_UNSPECIFIED (0):
                Unspecified vehicle body style.
            ATV_SPORT (1):
                ATV Sport.
            ATV_TOURING (2):
                ATV Touring.
            ATV_UTILITY (3):
                ATV Utility.
            ATV_YOUTH (4):
                ATV Youth.
            CITY_CAR (5):
                City car.
            CLASS_A_MOTORHOME (6):
                Class A motorhome.
            CLASS_B_MOTORHOME (7):
                Class B motorhome.
            CLASS_C_MOTORHOME (8):
                Class C motorhome.
            COMPACT_SUV (9):
                Compact SUV.
            CONVERTIBLE (10):
                Convertible.
            COUPE (11):
                Coupe.
            CROSSOVER (12):
                Crossover.
            FIFTH_WHEEL (13):
                Fifth wheel.
            FULL_SIZE_VAN (14):
                Full size van.
            HATCHBACK (15):
                Hatchback.
            LIMOUSINE (16):
                Limousine.
            MINIVAN (17):
                Minivan.
            NOTCHBACK (18):
                Notchback.
            POP_UP_CAMPER (19):
                Pop up camper.
            SEDAN (20):
                Sedan.
            SIDE_BY_SIDE (21):
                Side by side.
            STATION_WAGON (22):
                Station wagon.
            SUV (23):
                SUV.
            TRAVEL_TRAILER (24):
                Travel trailer.
            TRUCK (25):
                Truck.
            TRUCK_CAMPER (26):
                Truck camper.
            UTE (27):
                Ute.
            UTV_RECREATIONAL_UTILITY (28):
                UTV Recreational utility.
            UTV_SPORT (29):
                UTV Sport.
            UTV_UTILITY (30):
                UTV Utility.
            UTV_YOUTH (31):
                UTV Youth.
        """

        VEHICLE_BODY_STYLE_UNSPECIFIED = 0
        ATV_SPORT = 1
        ATV_TOURING = 2
        ATV_UTILITY = 3
        ATV_YOUTH = 4
        CITY_CAR = 5
        CLASS_A_MOTORHOME = 6
        CLASS_B_MOTORHOME = 7
        CLASS_C_MOTORHOME = 8
        COMPACT_SUV = 9
        CONVERTIBLE = 10
        COUPE = 11
        CROSSOVER = 12
        FIFTH_WHEEL = 13
        FULL_SIZE_VAN = 14
        HATCHBACK = 15
        LIMOUSINE = 16
        MINIVAN = 17
        NOTCHBACK = 18
        POP_UP_CAMPER = 19
        SEDAN = 20
        SIDE_BY_SIDE = 21
        STATION_WAGON = 22
        SUV = 23
        TRAVEL_TRAILER = 24
        TRUCK = 25
        TRUCK_CAMPER = 26
        UTE = 27
        UTV_RECREATIONAL_UTILITY = 28
        UTV_SPORT = 29
        UTV_UTILITY = 30
        UTV_YOUTH = 31

    class EngineType(proto.Enum):
        r"""The engine type of the vehicle.

        Values:
            ENGINE_TYPE_UNSPECIFIED (0):
                Unspecified engine type.
            GASOLINE (1):
                Gasoline.
            DIESEL (2):
                Diesel.
            ELECTRIC (3):
                Electric.
            HYBRID (4):
                Hybrid.
            PLUG_IN_HYBRID (5):
                Plug-in hybrid.
            NATURAL_GAS (6):
                Natural gas.
            LPG (7):
                LPG.
            METHANE (8):
                Methane.
            OTHER (9):
                Other.
        """

        ENGINE_TYPE_UNSPECIFIED = 0
        GASOLINE = 1
        DIESEL = 2
        ELECTRIC = 3
        HYBRID = 4
        PLUG_IN_HYBRID = 5
        NATURAL_GAS = 6
        LPG = 7
        METHANE = 8
        OTHER = 9

    class EmissionsStandard(proto.Enum):
        r"""The emission standard of the vehicle.

        Values:
            EMISSIONS_STANDARD_UNSPECIFIED (0):
                Unspecified emission standard.
            ZERO_EMISSIONS (1):
                Zero emissions.
            EURO1 (2):
                Euro 1.
            EURO2 (3):
                Euro 2.
            EURO3 (4):
                Euro 3.
            EURO4 (5):
                Euro 4.
            EURO5 (6):
                Euro 5.
            EURO5B (7):
                Euro 5b.
            EURO6 (8):
                Euro 6.
            EURO6C (9):
                Euro 6c.
            EURO6D (10):
                Euro 6d.
            EURO6D_TEMP (11):
                Euro 6d-TEMP.
            EURO6E (12):
                Euro 6e.
        """

        EMISSIONS_STANDARD_UNSPECIFIED = 0
        ZERO_EMISSIONS = 1
        EURO1 = 2
        EURO2 = 3
        EURO3 = 4
        EURO4 = 5
        EURO5 = 6
        EURO5B = 7
        EURO6 = 8
        EURO6C = 9
        EURO6D = 10
        EURO6D_TEMP = 11
        EURO6E = 12

    class VehiclePriceType(proto.Enum):
        r"""The vehicle price type.

        Values:
            VEHICLE_PRICE_TYPE_UNSPECIFIED (0):
                Unspecified vehicle price type.
            ALL_IN_PRICE (1):
                All in price.
            DRIVE_AWAY_PRICE (2):
                Drive away price.
            ESTIMATED_DRIVE_AWAY_PRICE (3):
                Estimated drive away price.
            EXCLUDING_GOVERNMENT_CHARGES_PRICE (4):
                Excluding government charges price.
            VEHICLE_BASE_PRICE (5):
                Vehicle base price.
        """

        VEHICLE_PRICE_TYPE_UNSPECIFIED = 0
        ALL_IN_PRICE = 1
        DRIVE_AWAY_PRICE = 2
        ESTIMATED_DRIVE_AWAY_PRICE = 3
        EXCLUDING_GOVERNMENT_CHARGES_PRICE = 4
        VEHICLE_BASE_PRICE = 5

    class PropertyType(proto.Enum):
        r"""The property type.

        Values:
            PROPERTY_TYPE_UNSPECIFIED (0):
                Unspecified property type.
            APARTMENT (1):
                Apartment.
            CONDO (2):
                Condo.
            LOFT (3):
                Loft.
            MULTI_FAMILY_HOME (4):
                Multi-family home.
            PENTHOUSE (5):
                Penthouse.
            ROOM (6):
                Room.
            SINGLE_FAMILY_HOME (7):
                Single-family home.
            STUDIO (8):
                Studio.
            TOWNHOUSE (9):
                Townhouse.
        """

        PROPERTY_TYPE_UNSPECIFIED = 0
        APARTMENT = 1
        CONDO = 2
        LOFT = 3
        MULTI_FAMILY_HOME = 4
        PENTHOUSE = 5
        ROOM = 6
        SINGLE_FAMILY_HOME = 7
        STUDIO = 8
        TOWNHOUSE = 9

    class AmenityFeature(proto.Enum):
        r"""The amenity features for the property.

        Values:
            AMENITY_FEATURE_UNSPECIFIED (0):
                Unspecified amenity feature.
            BALCONY (1):
                Balcony.
            BASEMENT (2):
                Basement.
            BASKETBALL_COURT (3):
                Basketball court.
            BIKE_STORAGE (4):
                Bike storage.
            CENTRAL_AC (5):
                Central air conditioning.
            DISHWASHER (6):
                Dishwasher.
            DOG_PARK (7):
                Dog park.
            ELEVATOR (8):
                Elevator.
            EV_CHARGING (9):
                EV charging.
            FENCED_LOT (10):
                Fenced lot.
            FIREPLACE (11):
                Fireplace.
            FITNESS_CENTER (12):
                Fitness center.
            FORCED_AIR_HEATING (13):
                Forced air heating.
            FULLY_FURNISHED (14):
                Fully furnished.
            GARAGE (15):
                Garage.
            GATED_COMMUNITY (16):
                Gated community.
            HARDWOOD_FLOORS (17):
                Hardwood floors.
            HIGH_SPEED_INTERNET (18):
                High speed internet.
            INTERCOM (19):
                Intercom.
            IN_UNIT_WASHER_DRYER (20):
                In-unit washer and dryer.
            KITCHEN (21):
                Kitchen.
            LARGE_CLOSETS (22):
                Large closets.
            MULTISPORT_COURT (23):
                Multisport court.
            ONSITE_LAUNDRY (24):
                Onsite laundry.
            OUTDOOR_LOUNGE (25):
                Outdoor lounge.
            PARKING (26):
                Parking.
            PATIO (27):
                Patio.
            PICKLEBALL_COURT (28):
                Pickleball court.
            POOL (29):
                Pool.
            REFRIGERATOR (30):
                Refrigerator.
            SOCCER_FIELD (31):
                Soccer field.
            TENNIS_COURT (32):
                Tennis court.
            WALK_IN_CLOSETS (33):
                Walk-in closets.
            WHEELCHAIR_ACCESS (34):
                Wheelchair accessibility.
        """

        AMENITY_FEATURE_UNSPECIFIED = 0
        BALCONY = 1
        BASEMENT = 2
        BASKETBALL_COURT = 3
        BIKE_STORAGE = 4
        CENTRAL_AC = 5
        DISHWASHER = 6
        DOG_PARK = 7
        ELEVATOR = 8
        EV_CHARGING = 9
        FENCED_LOT = 10
        FIREPLACE = 11
        FITNESS_CENTER = 12
        FORCED_AIR_HEATING = 13
        FULLY_FURNISHED = 14
        GARAGE = 15
        GATED_COMMUNITY = 16
        HARDWOOD_FLOORS = 17
        HIGH_SPEED_INTERNET = 18
        INTERCOM = 19
        IN_UNIT_WASHER_DRYER = 20
        KITCHEN = 21
        LARGE_CLOSETS = 22
        MULTISPORT_COURT = 23
        ONSITE_LAUNDRY = 24
        OUTDOOR_LOUNGE = 25
        PARKING = 26
        PATIO = 27
        PICKLEBALL_COURT = 28
        POOL = 29
        REFRIGERATOR = 30
        SOCCER_FIELD = 31
        TENNIS_COURT = 32
        WALK_IN_CLOSETS = 33
        WHEELCHAIR_ACCESS = 34

    class UtilitiesIncluded(proto.Enum):
        r"""The utilities included for the property.

        Values:
            UTILITIES_INCLUDED_UNSPECIFIED (0):
                Unspecified utilities included.
            ELECTRICITY (1):
                Electricity.
            GAS (2):
                Gas.
            INTERNET (3):
                Internet.
            TRASH (4):
                Trash.
            WATER (5):
                Water.
        """

        UTILITIES_INCLUDED_UNSPECIFIED = 0
        ELECTRICITY = 1
        GAS = 2
        INTERNET = 3
        TRASH = 4
        WATER = 5

    class SpecialtyHousingType(proto.Enum):
        r"""The specialty housing type for the property.

        Values:
            SPECIALTY_HOUSING_TYPE_UNSPECIFIED (0):
                Unspecified specialty housing type.
            CORPORATE (1):
                Corporate housing.
            LOW_INCOME (2):
                Low income housing.
            MILITARY (3):
                Military housing.
            SENIOR (4):
                Senior housing.
            SHORT_TERM (5):
                Short term housing.
            STUDENT (6):
                Student housing.
        """

        SPECIALTY_HOUSING_TYPE_UNSPECIFIED = 0
        CORPORATE = 1
        LOW_INCOME = 2
        MILITARY = 3
        SENIOR = 4
        SHORT_TERM = 5
        STUDENT = 6

    class ShippingBusinessDaysConfig(proto.Message):
        r"""The business days during which orders are on their path to
        fulfillment. If not provided, Monday to Friday business days
        will be assumed.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            country (str):
                The `CLDR territory
                code <http://www.unicode.org/repos/cldr/tags/latest/common/main/en.xml>`__
                of the country to which an item will ship.

                This field is a member of `oneof`_ ``_country``.
            business_days (str):
                Effective days of the week considered for the delivery time
                calculation. May not be empty. The more business days
                included the faster the delivery. Can be set through
                individual days (e.g. ``MTWRF``), or day ranges (e.g.
                ``Mon-Fri``). For more information about accepted formats,
                see `Shipping handling business
                days <https://support.google.com/merchants/answer/16072859>`__.

                This field is a member of `oneof`_ ``_business_days``.
        """

        country: str = proto.Field(
            proto.STRING,
            number=1,
            optional=True,
        )
        business_days: str = proto.Field(
            proto.STRING,
            number=2,
            optional=True,
        )

    class CarrierShipping(proto.Message):
        r"""Carrier-based shipping configuration. Allows for setting
        shipping speed or shipping cost based on a carrier's provided
        info.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            country (str):
                The `CLDR territory
                code <http://www.unicode.org/repos/cldr/tags/latest/common/main/en.xml>`__
                of the country to which an item will ship.

                This field is a member of `oneof`_ ``_country``.
            region (str):
                The geographic region to which a shipping rate applies. See
                `region <https://support.google.com/merchants/answer/6324484>`__
                for more information.

                This field is a member of `oneof`_ ``_region``.
            postal_code (str):
                The postal code range that the shipping rate applies to,
                represented by a postal code (eg. ``94043``), a postal code
                prefix followed by a \* wildcard (eg. ``94*``), a range
                between two postal codes (eg. ``94043-98033``) or two postal
                code prefixes of equal length (eg. ``94*-98*``).

                This field is a member of `oneof`_ ``_postal_code``.
            origin_postal_code (str):
                The source location postal code from which
                this offer ships. Represented only by a
                full-length postal code.

                This field is a member of `oneof`_ ``_origin_postal_code``.
            flat_price (google.shopping.type.types.Price):
                Fixed shipping price, represented as a number with currency.
                Cannot be set together with
                [carrierPrice][google.shopping.merchant.products.v1.ProductAttributes.CarrierShipping.carrier_price]
                or its adjustments
                ([carrierPriceFlatAdjustment][google.shopping.merchant.products.v1.ProductAttributes.CarrierShipping.carrier_price_flat_adjustment],
                [carrierPricePercentageAdjustment][google.shopping.merchant.products.v1.ProductAttributes.CarrierShipping.carrier_price_percentage_adjustment]).

                This field is a member of `oneof`_ ``_flat_price``.
            carrier_price (google.shopping.merchant_products_v1.types.ProductAttributes.CarrierPriceOption):
                Selected carrier to calculate the shipping price from.
                Select a carrier from the `available carriers
                list <https://support.google.com/merchants/answer/15449142#Supported>`__,
                for example ``AUSTRALIA_POST_REGULAR``. Price will be
                calculated by this selected carrier, the location expressed
                in
                [originPostalCode][google.shopping.merchant.products.v1.ProductAttributes.CarrierShipping.origin_postal_code],
                along with the user location to determine the accurate
                shipping price. Carrier is represented by a carrier service
                name or a carrier service ID. Cannot be set together with
                [flatPrice][google.shopping.merchant.products.v1.ProductAttributes.CarrierShipping.flat_price].

                This field is a member of `oneof`_ ``_carrier_price``.
            carrier_price_flat_adjustment (google.shopping.type.types.Price):
                A flat adjustment on the carrier price. Can be either
                positive or negative. Cannot be zero. Requires
                ``carrier_price`` to be present. Cannot be set together with
                [flatPrice][google.shopping.merchant.products.v1.ProductAttributes.CarrierShipping.flat_price]
                and
                [carrierPricePercentageAdjustment][google.shopping.merchant.products.v1.ProductAttributes.CarrierShipping.carrier_price_percentage_adjustment].

                This field is a member of `oneof`_ ``_carrier_price_flat_adjustment``.
            carrier_price_percentage_adjustment (float):
                A percentual adjustment on the carrier price. Can be either
                positive or negative. Cannot be zero. Requires
                ``carrier_price`` to be present. Cannot be set together with
                [flatPrice][google.shopping.merchant.products.v1.ProductAttributes.CarrierShipping.flat_price]
                and
                [carrierPriceFlatAdjustment][google.shopping.merchant.products.v1.ProductAttributes.CarrierShipping.carrier_price_flat_adjustment].

                This field is a member of `oneof`_ ``_carrier_price_percentage_adjustment``.
            min_handling_time (int):
                Minimum handling time (inclusive) between when the order is
                received and shipped in business days. 0 means that the
                order is shipped on the same day as it is received if it
                happens before the cut-off time.
                [minHandlingTime][google.shopping.merchant.products.v1.ProductAttributes.CarrierShipping.min_handling_time]
                can only be set if
                [maxHandlingTime][google.shopping.merchant.products.v1.ProductAttributes.CarrierShipping.max_handling_time]
                is also set.

                This field is a member of `oneof`_ ``_min_handling_time``.
            max_handling_time (int):
                Maximum handling time (inclusive) between when the order is
                received and shipped in business days. 0 means that the
                order is shipped on the same day as it is received if it
                happens before the cut-off time. Both
                [maxHandlingTime][google.shopping.merchant.products.v1.ProductAttributes.CarrierShipping.max_handling_time]
                and
                [fixedMaxTransitTime][google.shopping.merchant.products.v1.ProductAttributes.CarrierShipping.fixed_max_transit_time]
                or
                [carrierTransitTime][google.shopping.merchant.products.v1.ProductAttributes.CarrierShipping.carrier_transit_time]
                are required if providing shipping speeds.

                This field is a member of `oneof`_ ``_max_handling_time``.
            fixed_min_transit_time (int):
                Minimum transit time (inclusive) between when the order has
                shipped and when it is delivered in business days. 0 means
                that the order is delivered on the same day as it ships.
                [fixedMinTransitTime][google.shopping.merchant.products.v1.ProductAttributes.CarrierShipping.fixed_min_transit_time]
                can only be set if
                [fixedMaxTransitTime][google.shopping.merchant.products.v1.ProductAttributes.CarrierShipping.fixed_max_transit_time]
                is set. Cannot be set if
                [carrierTransitTime][google.shopping.merchant.products.v1.ProductAttributes.CarrierShipping.carrier_transit_time]
                is present.

                This field is a member of `oneof`_ ``_fixed_min_transit_time``.
            fixed_max_transit_time (int):
                Maximum transit time (inclusive) between when the order has
                shipped and when it is delivered in business days. 0 means
                that the order is delivered on the same day as it ships.
                Needs to be provided together with
                [maxHandlingTime][google.shopping.merchant.products.v1.ProductAttributes.CarrierShipping.max_handling_time].
                Cannot be set if
                [carrierTransitTime][google.shopping.merchant.products.v1.ProductAttributes.CarrierShipping.carrier_transit_time]
                is present.

                This field is a member of `oneof`_ ``_fixed_max_transit_time``.
            carrier_transit_time (google.shopping.merchant_products_v1.types.CarrierTransitTimeOption):
                Selected carrier to calculate the shipping speed from.
                Select a carrier from the `available carriers
                list <https://support.google.com/merchants/answer/15449142#Supported>`__,
                for example ``AUSTRALIA_POST_REGULAR``. Speed will be
                calculated by this selected carrier, the location expressed
                in
                [originPostalCode][google.shopping.merchant.products.v1.ProductAttributes.CarrierShipping.origin_postal_code],
                along with the user location to determine the accurate
                delivery speed. Carrier is represented by a carrier service
                name or a carrier service ID. Cannot be set together with
                [fixedMaxTransitTime][google.shopping.merchant.products.v1.ProductAttributes.CarrierShipping.fixed_max_transit_time]
                or
                [fixedMinTransitTime][google.shopping.merchant.products.v1.ProductAttributes.CarrierShipping.fixed_min_transit_time].

                This field is a member of `oneof`_ ``_carrier_transit_time``.
        """

        country: str = proto.Field(
            proto.STRING,
            number=1,
            optional=True,
        )
        region: str = proto.Field(
            proto.STRING,
            number=2,
            optional=True,
        )
        postal_code: str = proto.Field(
            proto.STRING,
            number=3,
            optional=True,
        )
        origin_postal_code: str = proto.Field(
            proto.STRING,
            number=4,
            optional=True,
        )
        flat_price: types.Price = proto.Field(
            proto.MESSAGE,
            number=5,
            optional=True,
            message=types.Price,
        )
        carrier_price: "ProductAttributes.CarrierPriceOption" = proto.Field(
            proto.ENUM,
            number=6,
            optional=True,
            enum="ProductAttributes.CarrierPriceOption",
        )
        carrier_price_flat_adjustment: types.Price = proto.Field(
            proto.MESSAGE,
            number=7,
            optional=True,
            message=types.Price,
        )
        carrier_price_percentage_adjustment: float = proto.Field(
            proto.DOUBLE,
            number=8,
            optional=True,
        )
        min_handling_time: int = proto.Field(
            proto.INT64,
            number=9,
            optional=True,
        )
        max_handling_time: int = proto.Field(
            proto.INT64,
            number=10,
            optional=True,
        )
        fixed_min_transit_time: int = proto.Field(
            proto.INT64,
            number=11,
            optional=True,
        )
        fixed_max_transit_time: int = proto.Field(
            proto.INT64,
            number=12,
            optional=True,
        )
        carrier_transit_time: "CarrierTransitTimeOption" = proto.Field(
            proto.ENUM,
            number=13,
            optional=True,
            enum="CarrierTransitTimeOption",
        )

    class Mileage(proto.Message):
        r"""The mileage of the vehicle.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            value (int):
                The distance value.

                This field is a member of `oneof`_ ``_value``.
            unit (google.shopping.merchant_products_v1.types.ProductAttributes.Mileage.Unit):
                The unit of the mileage.
        """

        class Unit(proto.Enum):
            r"""The unit of the mileage.

            Values:
                UNIT_UNSPECIFIED (0):
                    Unspecified unit.
                MILES (1):
                    Miles.
                KM (2):
                    Kilometers.
            """

            UNIT_UNSPECIFIED = 0
            MILES = 1
            KM = 2

        value: int = proto.Field(
            proto.INT64,
            number=1,
            optional=True,
        )
        unit: "ProductAttributes.Mileage.Unit" = proto.Field(
            proto.ENUM,
            number=2,
            enum="ProductAttributes.Mileage.Unit",
        )

    class FuelConsumption(proto.Message):
        r"""The fuel consumption of the vehicle.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            value (float):
                The fuel consumption value.

                This field is a member of `oneof`_ ``_value``.
            unit (google.shopping.merchant_products_v1.types.ProductAttributes.FuelConsumption.Unit):
                The unit of the fuel consumption.
        """

        class Unit(proto.Enum):
            r"""The unit of the fuel consumption.

            Values:
                UNIT_UNSPECIFIED (0):
                    Unspecified unit.
                LPER100KM (1):
                    Liter per 100 kilometers.
                KGPER100KM (2):
                    Kilograms per 100 kilometers.
            """

            UNIT_UNSPECIFIED = 0
            LPER100KM = 1
            KGPER100KM = 2

        value: float = proto.Field(
            proto.DOUBLE,
            number=1,
            optional=True,
        )
        unit: "ProductAttributes.FuelConsumption.Unit" = proto.Field(
            proto.ENUM,
            number=2,
            enum="ProductAttributes.FuelConsumption.Unit",
        )

    class EnergyConsumption(proto.Message):
        r"""The energy consumption of the vehicle.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            value (float):
                The energy consumption value.

                This field is a member of `oneof`_ ``_value``.
            unit (google.shopping.merchant_products_v1.types.ProductAttributes.EnergyConsumption.Unit):
                The unit of the energy consumption.
        """

        class Unit(proto.Enum):
            r"""The unit of the energy consumption.

            Values:
                UNIT_UNSPECIFIED (0):
                    Unspecified unit.
                KWHPER100KM (1):
                    Kilowatt hours per 100 kilometers.
            """

            UNIT_UNSPECIFIED = 0
            KWHPER100KM = 1

        value: float = proto.Field(
            proto.DOUBLE,
            number=1,
            optional=True,
        )
        unit: "ProductAttributes.EnergyConsumption.Unit" = proto.Field(
            proto.ENUM,
            number=2,
            enum="ProductAttributes.EnergyConsumption.Unit",
        )

    class Co2Emissions(proto.Message):
        r"""The co2 emission of the vehicle.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            value (int):
                The co2 emission value.

                This field is a member of `oneof`_ ``_value``.
            unit (google.shopping.merchant_products_v1.types.ProductAttributes.Co2Emissions.Unit):
                The unit of the co2 emission.
        """

        class Unit(proto.Enum):
            r"""The unit of the co2 emission.

            Values:
                UNIT_UNSPECIFIED (0):
                    Unspecified unit.
                GPERKM (1):
                    Grams per kilometer.
            """

            UNIT_UNSPECIFIED = 0
            GPERKM = 1

        value: int = proto.Field(
            proto.INT64,
            number=1,
            optional=True,
        )
        unit: "ProductAttributes.Co2Emissions.Unit" = proto.Field(
            proto.ENUM,
            number=2,
            enum="ProductAttributes.Co2Emissions.Unit",
        )

    class Warranty(proto.Message):
        r"""The warranty of the vehicle.

        Attributes:
            duration (int):
                The warranty duration in units. Default is in months, can be
                overridden by the ``duration_unit`` field.
            mileage (google.shopping.merchant_products_v1.types.ProductAttributes.Mileage):
                The warranty mileage (only applies to
                vehicles).
            duration_unit (google.shopping.merchant_products_v1.types.ProductAttributes.Warranty.WarrantyDurationUnit):
                The unit for the warranty duration. Assumed to be ``MONTH``
                if equal to ``WARRANTY_DURATION_UNIT_UNSPECIFIED``.
        """

        class WarrantyDurationUnit(proto.Enum):
            r"""The warranty duration unit of the product.

            Values:
                WARRANTY_DURATION_UNIT_UNSPECIFIED (0):
                    Indicates that the warranty duration unit is
                    unspecified.
                MONTH (1):
                    Indicates that the warranty duration unit is
                    month.
                YEAR (2):
                    Indicates that the warranty duration unit is
                    year.
            """

            WARRANTY_DURATION_UNIT_UNSPECIFIED = 0
            MONTH = 1
            YEAR = 2

        duration: int = proto.Field(
            proto.INT64,
            number=1,
        )
        mileage: "ProductAttributes.Mileage" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="ProductAttributes.Mileage",
        )
        duration_unit: "ProductAttributes.Warranty.WarrantyDurationUnit" = proto.Field(
            proto.ENUM,
            number=3,
            enum="ProductAttributes.Warranty.WarrantyDurationUnit",
        )

    class ProductFee(proto.Message):
        r"""The product fee attribute containing type and amount.

        Attributes:
            type_ (google.shopping.merchant_products_v1.types.ProductAttributes.ProductFee.FeeType):
                The type of product fee.
            amount (google.shopping.type.types.Price):
                The amount of product fee.
        """

        class FeeType(proto.Enum):
            r"""The type of product fee.

            Values:
                FEE_TYPE_UNSPECIFIED (0):
                    Unspecified fee type.
                ADMIN_FEE (1):
                    Admin fee.
                APPLICATION_FEE (2):
                    Application fee.
                SECURITY_DEPOSIT (3):
                    Security deposit.
            """

            FEE_TYPE_UNSPECIFIED = 0
            ADMIN_FEE = 1
            APPLICATION_FEE = 2
            SECURITY_DEPOSIT = 3

        type_: "ProductAttributes.ProductFee.FeeType" = proto.Field(
            proto.ENUM,
            number=1,
            enum="ProductAttributes.ProductFee.FeeType",
        )
        amount: types.Price = proto.Field(
            proto.MESSAGE,
            number=2,
            message=types.Price,
        )

    class DisplayAddress(proto.Message):
        r"""The display address of the property.

        Attributes:
            street_number (str):
                The street number.
            street_name (str):
                The street name.
            city (str):
                The city such as Seattle, New York, etc.
            region (str):
                The region(state), such as WA, OH, etc.
            postal_code (str):
                The postal code, such as 94043.
        """

        street_number: str = proto.Field(
            proto.STRING,
            number=1,
        )
        street_name: str = proto.Field(
            proto.STRING,
            number=2,
        )
        city: str = proto.Field(
            proto.STRING,
            number=3,
        )
        region: str = proto.Field(
            proto.STRING,
            number=4,
        )
        postal_code: str = proto.Field(
            proto.STRING,
            number=5,
        )

    class UnitArea(proto.Message):
        r"""The unit area of the property.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            value (float):
                The area value.

                This field is a member of `oneof`_ ``_value``.
            unit (google.shopping.merchant_products_v1.types.ProductAttributes.UnitArea.Unit):
                The unit of area.
        """

        class Unit(proto.Enum):
            r"""The unit of area.

            Values:
                UNIT_UNSPECIFIED (0):
                    Unspecified unit.
                SQM (1):
                    Square meters.
                SQFT (2):
                    Square feet.
            """

            UNIT_UNSPECIFIED = 0
            SQM = 1
            SQFT = 2

        value: float = proto.Field(
            proto.DOUBLE,
            number=1,
            optional=True,
        )
        unit: "ProductAttributes.UnitArea.Unit" = proto.Field(
            proto.ENUM,
            number=2,
            enum="ProductAttributes.UnitArea.Unit",
        )

    class PetPolicy(proto.Message):
        r"""The pet policy of the property.

        Attributes:
            pets_allowed (bool):
                Whether pets are allowed.
            pet_types (MutableSequence[google.shopping.merchant_products_v1.types.ProductAttributes.PetPolicy.PetType]):
                The pet types allowed.
        """

        class PetType(proto.Enum):
            r"""The pet types.

            Values:
                PET_TYPE_UNSPECIFIED (0):
                    Unspecified pet type.
                CATS (1):
                    Cats.
                LARGE_DOGS (2):
                    Large dogs.
                SMALL_DOGS (3):
                    Small dogs.
            """

            PET_TYPE_UNSPECIFIED = 0
            CATS = 1
            LARGE_DOGS = 2
            SMALL_DOGS = 3

        pets_allowed: bool = proto.Field(
            proto.BOOL,
            number=1,
        )
        pet_types: MutableSequence["ProductAttributes.PetPolicy.PetType"] = (
            proto.RepeatedField(
                proto.ENUM,
                number=2,
                enum="ProductAttributes.PetPolicy.PetType",
            )
        )

    class LeaseTerm(proto.Message):
        r"""The lease term of the property.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            type_ (google.shopping.merchant_products_v1.types.ProductAttributes.LeaseTerm.LeaseTermType):
                The type of lease term.
            duration_value (int):
                The duration value of the lease term.

                This field is a member of `oneof`_ ``_duration_value``.
            duration_unit (google.shopping.merchant_products_v1.types.ProductAttributes.LeaseTerm.DurationUnit):
                The duration unit of the lease term.
        """

        class LeaseTermType(proto.Enum):
            r"""The type of lease term.

            Values:
                LEASE_TERM_TYPE_UNSPECIFIED (0):
                    Unspecified lease term type.
                FIXED_TERM (1):
                    Fixed term.
            """

            LEASE_TERM_TYPE_UNSPECIFIED = 0
            FIXED_TERM = 1

        class DurationUnit(proto.Enum):
            r"""The unit of duration.

            Values:
                DURATION_UNIT_UNSPECIFIED (0):
                    Unspecified duration unit.
                MONTHS (1):
                    Month.
                WEEKS (2):
                    Week.
            """

            DURATION_UNIT_UNSPECIFIED = 0
            MONTHS = 1
            WEEKS = 2

        type_: "ProductAttributes.LeaseTerm.LeaseTermType" = proto.Field(
            proto.ENUM,
            number=1,
            enum="ProductAttributes.LeaseTerm.LeaseTermType",
        )
        duration_value: int = proto.Field(
            proto.INT64,
            number=2,
            optional=True,
        )
        duration_unit: "ProductAttributes.LeaseTerm.DurationUnit" = proto.Field(
            proto.ENUM,
            number=3,
            enum="ProductAttributes.LeaseTerm.DurationUnit",
        )

    class Returns(proto.Message):
        r"""The returns of the product.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            restocking_fee (google.shopping.type.types.Price):
                A flat restocking fee penalty.

                This field is a member of `oneof`_ ``restocking_fee_oneof``.
            restocking_percentage_fee (float):
                A percentage restocking fee penalty.

                This field is a member of `oneof`_ ``restocking_fee_oneof``.
            countries (MutableSequence[str]):
                The `CLDR territory
                code <http://www.unicode.org/repos/cldr/tags/latest/common/main/en.xml>`__
                of the countries to which an item can be returned.
            window_days (int):
                The duration of the return window in days.

                This field is a member of `oneof`_ ``_window_days``.
            window_type (google.shopping.merchant_products_v1.types.ProductAttributes.Returns.ReturnWindowType):
                Special return window behavior.

                This field is a member of `oneof`_ ``_window_type``.
            item_conditions (MutableSequence[google.shopping.merchant_products_v1.types.ProductAttributes.Returns.ItemCondition]):
                The condition the item must be in to be
                accepted.
            methods (MutableSequence[google.shopping.merchant_products_v1.types.ProductAttributes.Returns.ReturnMethod]):
                The physical methods by which the item can be
                returned.
            outcomes (MutableSequence[google.shopping.merchant_products_v1.types.ProductAttributes.Returns.ReturnOutcome]):
                The financial outcomes available for a
                return.
            shipping_fee (google.shopping.type.types.Price):
                The fixed cost out-of-pocket for a customer
                to return an item.

                This field is a member of `oneof`_ ``_shipping_fee``.
            shipping_fee_type (google.shopping.merchant_products_v1.types.ProductAttributes.Returns.ReturnShippingFeeType):
                The type of return shipping fee.

                This field is a member of `oneof`_ ``_shipping_fee_type``.
            policy_url (str):
                The URL of the return policy.

                This field is a member of `oneof`_ ``_policy_url``.
        """

        class ReturnWindowType(proto.Enum):
            r"""Type of return window for the return policy.

            Values:
                RETURN_WINDOW_TYPE_UNSPECIFIED (0):
                    The return window type is unspecified.
                FINITE_RETURN_WINDOW (1):
                    Window with a fixed number of days. If this is set, the
                    ``window_days`` field must be set.
                NO_RETURNS (2):
                    No returns accepted.
                LIFETIME (3):
                    Lifetime returns accepted.
            """

            RETURN_WINDOW_TYPE_UNSPECIFIED = 0
            FINITE_RETURN_WINDOW = 1
            NO_RETURNS = 2
            LIFETIME = 3

        class ReturnMethod(proto.Enum):
            r"""The physical method by which the item can be returned.

            Values:
                RETURN_METHOD_UNSPECIFIED (0):
                    The return method is unspecified.
                BY_MAIL (1):
                    Customer returns the item by mail.
                IN_STORE (2):
                    Customer returns the item in a store.
                AT_A_KIOSK (3):
                    Customer drops off the item at a kiosk.
                DROP_OFF_LOCATION (4):
                    Customer drops off the item at a 3rd party
                    partner location.
            """

            RETURN_METHOD_UNSPECIFIED = 0
            BY_MAIL = 1
            IN_STORE = 2
            AT_A_KIOSK = 3
            DROP_OFF_LOCATION = 4

        class ItemCondition(proto.Enum):
            r"""The acceptable item condition for a return.

            Values:
                ITEM_CONDITION_UNSPECIFIED (0):
                    The item condition is unspecified.
                NEW (1):
                    New condition.
                LIKE_NEW (2):
                    Like new condition.
                USED (3):
                    Used condition.
                DEFECTIVE_ONLY (4):
                    Only defective items are accepted.
            """

            ITEM_CONDITION_UNSPECIFIED = 0
            NEW = 1
            LIKE_NEW = 2
            USED = 3
            DEFECTIVE_ONLY = 4

        class ReturnOutcome(proto.Enum):
            r"""The financial outcome of a return.

            Values:
                RETURN_OUTCOME_UNSPECIFIED (0):
                    The return outcome is unspecified.
                REFUND (1):
                    Customer receives a refund.
                EXCHANGE (2):
                    Customer receives an exchange.
                STORE_CREDIT (3):
                    Customer receives store credit.
            """

            RETURN_OUTCOME_UNSPECIFIED = 0
            REFUND = 1
            EXCHANGE = 2
            STORE_CREDIT = 3

        class ReturnShippingFeeType(proto.Enum):
            r"""The type of the return shipping fee.

            Values:
                RETURN_SHIPPING_FEE_TYPE_UNSPECIFIED (0):
                    The return shipping fee type is unspecified.
                CUSTOMER_RESPONSIBILITY (1):
                    The customer is responsible for shipping
                    costs.
                DEDUCTED_FROM_REFUND (2):
                    The shipping cost is deducted from the
                    refund.
            """

            RETURN_SHIPPING_FEE_TYPE_UNSPECIFIED = 0
            CUSTOMER_RESPONSIBILITY = 1
            DEDUCTED_FROM_REFUND = 2

        restocking_fee: types.Price = proto.Field(
            proto.MESSAGE,
            number=9,
            oneof="restocking_fee_oneof",
            message=types.Price,
        )
        restocking_percentage_fee: float = proto.Field(
            proto.DOUBLE,
            number=10,
            oneof="restocking_fee_oneof",
        )
        countries: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        window_days: int = proto.Field(
            proto.INT64,
            number=2,
            optional=True,
        )
        window_type: "ProductAttributes.Returns.ReturnWindowType" = proto.Field(
            proto.ENUM,
            number=3,
            optional=True,
            enum="ProductAttributes.Returns.ReturnWindowType",
        )
        item_conditions: MutableSequence["ProductAttributes.Returns.ItemCondition"] = (
            proto.RepeatedField(
                proto.ENUM,
                number=4,
                enum="ProductAttributes.Returns.ItemCondition",
            )
        )
        methods: MutableSequence["ProductAttributes.Returns.ReturnMethod"] = (
            proto.RepeatedField(
                proto.ENUM,
                number=5,
                enum="ProductAttributes.Returns.ReturnMethod",
            )
        )
        outcomes: MutableSequence["ProductAttributes.Returns.ReturnOutcome"] = (
            proto.RepeatedField(
                proto.ENUM,
                number=6,
                enum="ProductAttributes.Returns.ReturnOutcome",
            )
        )
        shipping_fee: types.Price = proto.Field(
            proto.MESSAGE,
            number=7,
            optional=True,
            message=types.Price,
        )
        shipping_fee_type: "ProductAttributes.Returns.ReturnShippingFeeType" = (
            proto.Field(
                proto.ENUM,
                number=8,
                optional=True,
                enum="ProductAttributes.Returns.ReturnShippingFeeType",
            )
        )
        policy_url: str = proto.Field(
            proto.STRING,
            number=11,
            optional=True,
        )

    class QuestionAndAnswer(proto.Message):
        r"""The question and answer for the product.

        Attributes:
            question (str):
                Required. The question text.
            answer (str):
                Required. The answer text.
        """

        question: str = proto.Field(
            proto.STRING,
            number=1,
        )
        answer: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class VariantOption(proto.Message):
        r"""Additional product variants for the product.

        Attributes:
            name (str):
                Required. The name of the variant. For
                example, "Color", "Memory", "Size", "Length".
            value (str):
                Required. The value of the variant. For
                example, "Red", "128GB", "XL", "100cm".
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        value: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class RelatedProduct(proto.Message):
        r"""Specifies how other products are related to this product.

        Attributes:
            relationship_type (google.shopping.merchant_products_v1.types.ProductAttributes.RelatedProduct.RelationshipType):
                Required. The type of the relationship
                between this product and the related product.
            id_type (google.shopping.merchant_products_v1.types.ProductAttributes.RelatedProduct.IdType):
                Required. The type of the identifier of the related product.
                For example,
                `GTIN <https://support.google.com/merchants/answer/6219078>`__
                or `product
                ID <https://support.google.com/merchants/answer/6324405>`__.
            id (str):
                Required. The identifier of the related
                product.
        """

        class RelationshipType(proto.Enum):
            r"""The various types of the relationships between this product
            and the related product.

            Values:
                RELATIONSHIP_TYPE_UNSPECIFIED (0):
                    The relationship type is unspecified.
                PART_OF_SET (1):
                    Part of a set of products that are often
                    purchased together.
                REQUIRED_PART (2):
                    Part that is necessary for the product to
                    function, for example a battery for a
                    battery-operated lamp.
                OFTEN_BOUGHT_WITH (3):
                    A product that this product is often
                    purchased together with, for example a phone
                    case with a phone.
                SUBSTITUTE (4):
                    Product that this product can be substituted
                    for. For example a printer comparable in
                    function to another printer.
                DIFFERENT_BRAND (5):
                    An identical product sold under a different
                    brand, for example a cheaper house brand.
                ACCESSORY (6):
                    An accessory to this product, for example a
                    side table that matches the style of a couch.
            """

            RELATIONSHIP_TYPE_UNSPECIFIED = 0
            PART_OF_SET = 1
            REQUIRED_PART = 2
            OFTEN_BOUGHT_WITH = 3
            SUBSTITUTE = 4
            DIFFERENT_BRAND = 5
            ACCESSORY = 6

        class IdType(proto.Enum):
            r"""The type of the identifier of the related product.

            Values:
                ID_TYPE_UNSPECIFIED (0):
                    The identifier type is unspecified.
                GTIN (1):
                    The identifier is a GTIN.
                ID (2):
                    The identifier is a product ID in the feed.
            """

            ID_TYPE_UNSPECIFIED = 0
            GTIN = 1
            ID = 2

        relationship_type: "ProductAttributes.RelatedProduct.RelationshipType" = (
            proto.Field(
                proto.ENUM,
                number=1,
                enum="ProductAttributes.RelatedProduct.RelationshipType",
            )
        )
        id_type: "ProductAttributes.RelatedProduct.IdType" = proto.Field(
            proto.ENUM,
            number=2,
            enum="ProductAttributes.RelatedProduct.IdType",
        )
        id: str = proto.Field(
            proto.STRING,
            number=3,
        )

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
    age_group: "AgeGroup" = proto.Field(
        proto.ENUM,
        number=18,
        optional=True,
        enum="AgeGroup",
    )
    availability: "Availability" = proto.Field(
        proto.ENUM,
        number=19,
        optional=True,
        enum="Availability",
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
    condition: "Condition" = proto.Field(
        proto.ENUM,
        number=23,
        optional=True,
        enum="Condition",
    )
    gender: "Gender" = proto.Field(
        proto.ENUM,
        number=24,
        optional=True,
        enum="Gender",
    )
    google_product_category: str = proto.Field(
        proto.STRING,
        number=25,
        optional=True,
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
    installment: "ProductInstallment" = proto.Field(
        proto.MESSAGE,
        number=32,
        message="ProductInstallment",
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
    carrier_shipping: MutableSequence[CarrierShipping] = proto.RepeatedField(
        proto.MESSAGE,
        number=142,
        message=CarrierShipping,
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
    shipping_handling_business_days: MutableSequence[ShippingBusinessDaysConfig] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=143,
            message=ShippingBusinessDaysConfig,
        )
    )
    shipping_transit_business_days: MutableSequence[ShippingBusinessDaysConfig] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=144,
            message=ShippingBusinessDaysConfig,
        )
    )
    handling_cutoff_times: MutableSequence["HandlingCutoffTime"] = proto.RepeatedField(
        proto.MESSAGE,
        number=141,
        message="HandlingCutoffTime",
    )
    shipping_label: str = proto.Field(
        proto.STRING,
        number=46,
        optional=True,
    )
    return_policy_label: str = proto.Field(
        proto.STRING,
        number=170,
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
    size_system: "SizeSystem" = proto.Field(
        proto.ENUM,
        number=49,
        optional=True,
        enum="SizeSystem",
    )
    size_types: MutableSequence["SizeType"] = proto.RepeatedField(
        proto.ENUM,
        number=50,
        enum="SizeType",
    )
    energy_efficiency_class: "EnergyEfficiencyClass" = proto.Field(
        proto.ENUM,
        number=53,
        optional=True,
        enum="EnergyEfficiencyClass",
    )
    min_energy_efficiency_class: "EnergyEfficiencyClass" = proto.Field(
        proto.ENUM,
        number=54,
        optional=True,
        enum="EnergyEfficiencyClass",
    )
    max_energy_efficiency_class: "EnergyEfficiencyClass" = proto.Field(
        proto.ENUM,
        number=55,
        optional=True,
        enum="EnergyEfficiencyClass",
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
    pickup_method: "PickupMethod" = proto.Field(
        proto.ENUM,
        number=80,
        optional=True,
        enum="PickupMethod",
    )
    pickup_sla: "PickupSla" = proto.Field(
        proto.ENUM,
        number=81,
        optional=True,
        enum="PickupSla",
    )
    pickup_cost: "PickupCost" = proto.Field(
        proto.MESSAGE,
        number=172,
        optional=True,
        message="PickupCost",
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
    included_destinations: MutableSequence[types.Destination.DestinationEnum] = (
        proto.RepeatedField(
            proto.ENUM,
            number=76,
            enum=types.Destination.DestinationEnum,
        )
    )
    excluded_destinations: MutableSequence[types.Destination.DestinationEnum] = (
        proto.RepeatedField(
            proto.ENUM,
            number=77,
            enum=types.Destination.DestinationEnum,
        )
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
    pause: "Pause" = proto.Field(
        proto.ENUM,
        number=13,
        optional=True,
        enum="Pause",
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
    certifications: MutableSequence["ProductCertification"] = proto.RepeatedField(
        proto.MESSAGE,
        number=123,
        message="ProductCertification",
    )
    structured_title: "StructuredTitle" = proto.Field(
        proto.MESSAGE,
        number=132,
        optional=True,
        message="StructuredTitle",
    )
    structured_description: "StructuredDescription" = proto.Field(
        proto.MESSAGE,
        number=133,
        optional=True,
        message="StructuredDescription",
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
    video_links: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=169,
    )
    minimum_order_values: MutableSequence["ProductMinimumOrderValue"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=146,
            message="ProductMinimumOrderValue",
        )
    )
    warranty: Warranty = proto.Field(
        proto.MESSAGE,
        number=168,
        message=Warranty,
    )
    vin: str = proto.Field(
        proto.STRING,
        number=147,
    )
    model: str = proto.Field(
        proto.STRING,
        number=148,
    )
    trim: str = proto.Field(
        proto.STRING,
        number=149,
    )
    body_style: VehicleBodyStyle = proto.Field(
        proto.ENUM,
        number=150,
        enum=VehicleBodyStyle,
    )
    year: int = proto.Field(
        proto.INT64,
        number=151,
    )
    mileage: Mileage = proto.Field(
        proto.MESSAGE,
        number=152,
        message=Mileage,
    )
    electric_range: Mileage = proto.Field(
        proto.MESSAGE,
        number=153,
        message=Mileage,
    )
    fuel_consumption: FuelConsumption = proto.Field(
        proto.MESSAGE,
        number=154,
        message=FuelConsumption,
    )
    fuel_consumption_discharged_battery: FuelConsumption = proto.Field(
        proto.MESSAGE,
        number=155,
        message=FuelConsumption,
    )
    energy_consumption: EnergyConsumption = proto.Field(
        proto.MESSAGE,
        number=156,
        message=EnergyConsumption,
    )
    co2_emissions: Co2Emissions = proto.Field(
        proto.MESSAGE,
        number=157,
        message=Co2Emissions,
    )
    date_first_registered: str = proto.Field(
        proto.STRING,
        number=158,
    )
    engine: EngineType = proto.Field(
        proto.ENUM,
        number=159,
        enum=EngineType,
    )
    emissions_standard: EmissionsStandard = proto.Field(
        proto.ENUM,
        number=160,
        enum=EmissionsStandard,
    )
    certified_pre_owned: bool = proto.Field(
        proto.BOOL,
        number=161,
    )
    vehicle_msrp: types.Price = proto.Field(
        proto.MESSAGE,
        number=162,
        message=types.Price,
    )
    vehicle_all_in_price: types.Price = proto.Field(
        proto.MESSAGE,
        number=163,
        message=types.Price,
    )
    vehicle_price_type: VehiclePriceType = proto.Field(
        proto.ENUM,
        number=164,
        enum=VehiclePriceType,
    )
    vehicle_mandatory_inspection_included: bool = proto.Field(
        proto.BOOL,
        number=166,
    )
    vehicle_expenses: types.Price = proto.Field(
        proto.MESSAGE,
        number=167,
        message=types.Price,
    )
    returns: MutableSequence[Returns] = proto.RepeatedField(
        proto.MESSAGE,
        number=171,
        message=Returns,
    )
    display_address: DisplayAddress = proto.Field(
        proto.MESSAGE,
        number=179,
        message=DisplayAddress,
    )
    latitude: float = proto.Field(
        proto.DOUBLE,
        number=180,
        optional=True,
    )
    longitude: float = proto.Field(
        proto.DOUBLE,
        number=181,
        optional=True,
    )
    neighborhood: str = proto.Field(
        proto.STRING,
        number=182,
    )
    unit_area: UnitArea = proto.Field(
        proto.MESSAGE,
        number=183,
        message=UnitArea,
    )
    number_of_units: int = proto.Field(
        proto.INT64,
        number=184,
        optional=True,
    )
    property_name: str = proto.Field(
        proto.STRING,
        number=185,
    )
    number_of_bedrooms: float = proto.Field(
        proto.DOUBLE,
        number=186,
        optional=True,
    )
    number_of_bathrooms: float = proto.Field(
        proto.DOUBLE,
        number=187,
        optional=True,
    )
    property_type: PropertyType = proto.Field(
        proto.ENUM,
        number=188,
        enum=PropertyType,
    )
    amenity_feature: MutableSequence[AmenityFeature] = proto.RepeatedField(
        proto.ENUM,
        number=189,
        enum=AmenityFeature,
    )
    utilities_included: MutableSequence[UtilitiesIncluded] = proto.RepeatedField(
        proto.ENUM,
        number=190,
        enum=UtilitiesIncluded,
    )
    pet_policy: PetPolicy = proto.Field(
        proto.MESSAGE,
        number=191,
        message=PetPolicy,
    )
    specialty_housing_type: SpecialtyHousingType = proto.Field(
        proto.ENUM,
        number=192,
        enum=SpecialtyHousingType,
    )
    product_fee: MutableSequence[ProductFee] = proto.RepeatedField(
        proto.MESSAGE,
        number=193,
        message=ProductFee,
    )
    short_title: str = proto.Field(
        proto.STRING,
        number=194,
        optional=True,
    )
    lease_term: LeaseTerm = proto.Field(
        proto.MESSAGE,
        number=195,
        message=LeaseTerm,
    )
    questions_and_answers: MutableSequence[QuestionAndAnswer] = proto.RepeatedField(
        proto.MESSAGE,
        number=173,
        message=QuestionAndAnswer,
    )
    popularity_rank: float = proto.Field(
        proto.FLOAT,
        number=174,
    )
    item_group_title: str = proto.Field(
        proto.STRING,
        number=175,
    )
    document_links: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=176,
    )
    variant_options: MutableSequence[VariantOption] = proto.RepeatedField(
        proto.MESSAGE,
        number=177,
        message=VariantOption,
    )
    related_products: MutableSequence[RelatedProduct] = proto.RepeatedField(
        proto.MESSAGE,
        number=178,
        message=RelatedProduct,
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
        period (google.shopping.merchant_products_v1.types.SubscriptionPeriod):
            The type of subscription period. Supported values are:

            - "``month``"
            - "``year``"
            - "``week``".
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


class ProductInstallment(proto.Message):
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
        credit_type (google.shopping.merchant_products_v1.types.CreditType):
            Type of installment payments.

            This field is a member of `oneof`_ ``_credit_type``.
        annual_percentage_rate (float):
            Optional. Annual percentage rate for ``credit_type`` finance

            This field is a member of `oneof`_ ``_annual_percentage_rate``.
        total_amount (google.shopping.type.types.Price):
            Optional. Total amount the buyer has to pay,
            including interest.

            This field is a member of `oneof`_ ``_total_amount``.
        mileage_allowance (google.shopping.merchant_products_v1.types.ProductAttributes.Mileage):
            Optional. The mileage allowance for the lease
            of the vehicle. Only applicable to vehicle
            products.

            This field is a member of `oneof`_ ``_mileage_allowance``.
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
    credit_type: "CreditType" = proto.Field(
        proto.ENUM,
        number=4,
        optional=True,
        enum="CreditType",
    )
    annual_percentage_rate: float = proto.Field(
        proto.DOUBLE,
        number=5,
        optional=True,
    )
    total_amount: types.Price = proto.Field(
        proto.MESSAGE,
        number=6,
        optional=True,
        message=types.Price,
    )
    mileage_allowance: "ProductAttributes.Mileage" = proto.Field(
        proto.MESSAGE,
        number=7,
        optional=True,
        message="ProductAttributes.Mileage",
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

    For more information on loyalty programs, see `Overview of loyalty
    programs </merchant/api/guides/loyalty/loyalty-programs>`__.


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
            [minHandlingTime][google.shopping.merchant.products.v1.Shipping.min_handling_time]
            can only be present together with
            [maxHandlingTime][google.shopping.merchant.products.v1.Shipping.max_handling_time];
            but it is not required if
            [maxHandlingTime][google.shopping.merchant.products.v1.Shipping.max_handling_time]
            is present.

            This field is a member of `oneof`_ ``_min_handling_time``.
        max_handling_time (int):
            Maximum handling time (inclusive) between when the order is
            received and shipped in business days. 0 means that the
            order is shipped on the same day as it is received if it
            happens before the cut-off time. Both
            [maxHandlingTime][google.shopping.merchant.products.v1.Shipping.max_handling_time]
            and
            [maxTransitTime][google.shopping.merchant.products.v1.Shipping.max_transit_time]
            are required if providing shipping speeds.
            [minHandlingTime][google.shopping.merchant.products.v1.Shipping.min_handling_time]
            is optional if
            [maxHandlingTime][google.shopping.merchant.products.v1.Shipping.max_handling_time]
            is present.

            This field is a member of `oneof`_ ``_max_handling_time``.
        min_transit_time (int):
            Minimum transit time (inclusive) between when the order has
            shipped and when it is delivered in business days. 0 means
            that the order is delivered on the same day as it ships.
            [minTransitTime][google.shopping.merchant.products.v1.Shipping.min_transit_time]
            can only be present together with
            [maxTransitTime][google.shopping.merchant.products.v1.Shipping.max_transit_time];
            but it is not required if
            [maxTransitTime][google.shopping.merchant.products.v1.Shipping.max_transit_time]
            is present.

            This field is a member of `oneof`_ ``_min_transit_time``.
        max_transit_time (int):
            Maximum transit time (inclusive) between when the order has
            shipped and when it is delivered in business days. 0 means
            that the order is delivered on the same day as it ships.
            Both
            [maxHandlingTime][google.shopping.merchant.products.v1.Shipping.max_handling_time]
            and
            [maxTransitTime][google.shopping.merchant.products.v1.Shipping.max_transit_time]
            are required if providing shipping speeds.
            [minTransitTime][google.shopping.merchant.products.v1.Shipping.min_transit_time]
            is optional if
            [maxTransitTime][google.shopping.merchant.products.v1.Shipping.max_transit_time]
            is present.

            This field is a member of `oneof`_ ``_max_transit_time``.
        handling_cutoff_time (str):
            The handling cutoff time until which an order has to be
            placed to be processed in the same day. This is a string in
            format of HHMM (e.g. ``1530``) for 3:30 PM. If not
            configured, the cutoff time will be defaulted to 8AM PST and
            ``handling_cutoff_timezone`` will be ignored.

            This field is a member of `oneof`_ ``_handling_cutoff_time``.
        handling_cutoff_timezone (str):
            `Timezone
            identifier <https://developers.google.com/adwords/api/docs/appendix/codes-formats#timezone-ids>`__
            For example ``Europe/Zurich``. This field only applies if
            ``handling_cutoff_time`` is set. If ``handling_cutoff_time``
            is set but this field is not set, the shipping destination
            timezone will be used. If both fields are not set, the
            handling cutoff time will default to 8AM PST.

            This field is a member of `oneof`_ ``_handling_cutoff_timezone``.
        loyalty_program_label (str):
            Optional. The label of the `loyalty
            program <https://support.google.com/merchants/answer/6324484>`__.
            Must match one of the program labels set in
            [loyalty_programs][google.shopping.merchant.products.v1.LoyaltyProgram].
            When set (in combination with
            `loyalty_tier_label <https://support.google.com/merchants/answer/6324484>`__),
            this shipping option is only applicable to loyalty program
            members of the specified tier.
        loyalty_tier_label (str):
            Optional. The label of the `loyalty
            tier <https://support.google.com/merchants/answer/6324484>`__
            within the loyalty program. Must match one of the tiers set
            in the
            [loyalty_programs][google.shopping.merchant.products.v1.LoyaltyProgram].
            When set (in combination with
            `loyalty_program_label <https://support.google.com/merchants/answer/6324484>`__),
            this shipping option is only applicable to loyalty program
            members of the specified tier.
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
    handling_cutoff_time: str = proto.Field(
        proto.STRING,
        number=12,
        optional=True,
    )
    handling_cutoff_timezone: str = proto.Field(
        proto.STRING,
        number=13,
        optional=True,
    )
    loyalty_program_label: str = proto.Field(
        proto.STRING,
        number=14,
    )
    loyalty_tier_label: str = proto.Field(
        proto.STRING,
        number=15,
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


class ProductCertification(proto.Message):
    r"""Product
    `certification <https://support.google.com/merchants/answer/13528839>`__,
    initially introduced for EU energy efficiency labeling compliance
    using the EU EPREL database.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        certification_authority (google.shopping.merchant_products_v1.types.CertificationAuthority):
            The certification authority.

            This field is a member of `oneof`_ ``_certification_authority``.
        certification_name (google.shopping.merchant_products_v1.types.CertificationName):
            The name of the certification.

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
        certification_document_link (str):
            Optional. URL to the certification document (eg.
            ``https://www.example.com/document``), for example, the
            product data sheet or fiche required by UK's DESNZ or EU's
            EPREL. Maximum length is 2000 characters. For more
            information, see
            `Certification <https://support.google.com/merchants/answer/13528839>`__.

            This field is a member of `oneof`_ ``_certification_document_link``.
        certification_label_link (str):
            Optional. URL to the certification label (eg.
            ``https://www.example.com/label``), for example, the energy
            efficiency label required by UK's DESNZ or EU's EPREL.
            Maximum length is 2000 characters. For more information, see
            `Certification <https://support.google.com/merchants/answer/13528839>`__.

            This field is a member of `oneof`_ ``_certification_label_link``.
    """

    certification_authority: "CertificationAuthority" = proto.Field(
        proto.ENUM,
        number=1,
        optional=True,
        enum="CertificationAuthority",
    )
    certification_name: "CertificationName" = proto.Field(
        proto.ENUM,
        number=2,
        optional=True,
        enum="CertificationName",
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
    certification_document_link: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    certification_label_link: str = proto.Field(
        proto.STRING,
        number=6,
        optional=True,
    )


class StructuredTitle(proto.Message):
    r"""Structured title, for algorithmically (AI)-generated titles.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        digital_source_type (google.shopping.merchant_products_v1.types.DigitalSourceType):
            The digital source type. Following
            `IPTC <https://cv.iptc.org/newscodes/digitalsourcetype>`__.

            This field is a member of `oneof`_ ``_digital_source_type``.
        content (str):
            The title text
            Maximum length is 150 characters

            This field is a member of `oneof`_ ``_content``.
    """

    digital_source_type: "DigitalSourceType" = proto.Field(
        proto.ENUM,
        number=1,
        optional=True,
        enum="DigitalSourceType",
    )
    content: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )


class StructuredDescription(proto.Message):
    r"""Structured description, for algorithmically (AI)-generated
    descriptions.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        digital_source_type (google.shopping.merchant_products_v1.types.DigitalSourceType):
            The digital source type. Following
            `IPTC <https://cv.iptc.org/newscodes/digitalsourcetype>`__.

            This field is a member of `oneof`_ ``_digital_source_type``.
        content (str):
            The description text
            Maximum length is 5000 characters

            This field is a member of `oneof`_ ``_content``.
    """

    digital_source_type: "DigitalSourceType" = proto.Field(
        proto.ENUM,
        number=1,
        optional=True,
        enum="DigitalSourceType",
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
        destination_statuses (MutableSequence[google.shopping.merchant_products_v1.types.ProductStatus.DestinationStatus]):
            The intended destinations for the product.
        item_level_issues (MutableSequence[google.shopping.merchant_products_v1.types.ProductStatus.ItemLevelIssue]):
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

        Equivalent to
        [``StatusPerReportingContext``][google.shopping.merchant.reports.v1.ProductView.StatusPerReportingContext]
        in Reports API.

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
            severity (google.shopping.merchant_products_v1.types.ProductStatus.ItemLevelIssue.Severity):
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
        type_ (google.shopping.merchant_products_v1.types.ProductSustainabilityIncentive.Type):
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


class PickupCost(proto.Message):
    r"""The pickup cost of the item.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        flat_rate (google.shopping.type.types.Price):
            Required. The flat rate pickup cost of the
            item.

            This field is a member of `oneof`_ ``_flat_rate``.
        free_threshold (google.shopping.type.types.Price):
            Optional. The price threshold above which
            pickup is free of charge.

            This field is a member of `oneof`_ ``_free_threshold``.
    """

    flat_rate: types.Price = proto.Field(
        proto.MESSAGE,
        number=1,
        optional=True,
        message=types.Price,
    )
    free_threshold: types.Price = proto.Field(
        proto.MESSAGE,
        number=2,
        optional=True,
        message=types.Price,
    )


class HandlingCutoffTime(proto.Message):
    r"""Configuration for offer or offer-country level shipping
    handling cutoff time.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        country (str):
            The `CLDR territory
            code <http://www.unicode.org/repos/cldr/tags/latest/common/main/en.xml>`__
            of the country to which the handling cutoff time applies.

            This field is a member of `oneof`_ ``_country``.
        cutoff_time (str):
            The handling cutoff time until which an order has to be
            placed to be processed in the same day. This is a string in
            format of HHMM (e.g. ``1530``) for 3:30 PM. If not
            configured, the cutoff time will be defaulted to 8AM PST.

            This field is a member of `oneof`_ ``_cutoff_time``.
        cutoff_timezone (str):
            `Timezone
            identifier <https://developers.google.com/adwords/api/docs/appendix/codes-formats#timezone-ids>`__
            For example 'Europe/Zurich'. If not set, the shipping
            destination timezone will be used.

            This field is a member of `oneof`_ ``_cutoff_timezone``.
        disable_delivery_after_cutoff (bool):
            This field only applies to same-day delivery.
            If true, prevents next-day delivery from being
            shown for this offer after the cutoff time. This
            field only applies to same-day delivery offers,
            for merchants who want to explicitly disable it.

            This field is a member of `oneof`_ ``_disable_delivery_after_cutoff``.
    """

    country: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    cutoff_time: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    cutoff_timezone: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    disable_delivery_after_cutoff: bool = proto.Field(
        proto.BOOL,
        number=4,
        optional=True,
    )


class ProductMinimumOrderValue(proto.Message):
    r"""The minimum order value in the cart before the checkout is
    permitted.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        country (str):
            Required. The `CLDR territory
            code <http://www.unicode.org/repos/cldr/tags/latest/common/main/en.xml>`__
            of the country to which an item will ship.

            This field is a member of `oneof`_ ``_country``.
        service (str):
            A free-form description of the service class or delivery
            speed. This should match the service value set for the
            Shipping attribute. See
            [service][google.shopping.merchant.products.v1.Shipping.service].

            This field is a member of `oneof`_ ``_service``.
        surface (google.shopping.merchant_products_v1.types.ProductMinimumOrderValue.Surface):
            The surface to which the minimum order value applies.
            Defaults to ``ONLINE_LOCAL`` if not configured.

            This field is a member of `oneof`_ ``_surface``.
        price (google.shopping.type.types.Price):
            Required. The minimum cart or basket value
            before the checkout is permitted.

            This field is a member of `oneof`_ ``_price``.
    """

    class Surface(proto.Enum):
        r"""The surface values to which the minimum order value applies.

        Values:
            SURFACE_UNSPECIFIED (0):
                Surface is unspecified.
            ONLINE (1):
                Surface value to indicate online purchases.
            LOCAL (2):
                Surface value to indicate local purchases.
            ONLINE_LOCAL (3):
                Surface value to indicate online and local
                purchases.
        """

        SURFACE_UNSPECIFIED = 0
        ONLINE = 1
        LOCAL = 2
        ONLINE_LOCAL = 3

    country: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    service: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    surface: Surface = proto.Field(
        proto.ENUM,
        number=3,
        optional=True,
        enum=Surface,
    )
    price: types.Price = proto.Field(
        proto.MESSAGE,
        number=4,
        optional=True,
        message=types.Price,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
