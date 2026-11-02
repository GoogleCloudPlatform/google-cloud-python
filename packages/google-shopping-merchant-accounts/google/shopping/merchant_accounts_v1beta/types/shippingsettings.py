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

__protobuf__ = proto.module(
    package="google.shopping.merchant.accounts.v1beta",
    manifest={
        "ShippingSettings",
        "Service",
        "Distance",
        "Warehouse",
        "WarehouseCutoffTime",
        "Address",
        "DeliveryTime",
        "CutoffTime",
        "BusinessDayConfig",
        "WarehouseBasedDeliveryTime",
        "RateGroup",
        "Table",
        "TransitTable",
        "MinimumOrderValueTable",
        "Headers",
        "LocationIdSet",
        "Row",
        "Value",
        "CarrierRate",
        "GetShippingSettingsRequest",
        "InsertShippingSettingsRequest",
    },
)


class ShippingSettings(proto.Message):
    r"""The merchant account's `shipping
    setting <https://support.google.com/merchants/answer/6069284>`__.

    Attributes:
        name (str):
            Identifier. The resource name of the shipping setting.
            Format: ``accounts/{account}/shippingSetting``
        services (MutableSequence[google.shopping.merchant_accounts_v1beta.types.Service]):
            Optional. The target account's list of
            services.
        warehouses (MutableSequence[google.shopping.merchant_accounts_v1beta.types.Warehouse]):
            Optional. A list of warehouses which can be referred to in
            ``services``.
        etag (str):
            Required. This field is used for avoid async
            issue. Make sure shipping setting data
             didn't change between get call and insert call.
            The user should do  following steps：

            1. Set etag field as empty string for initial
                shipping setting creation.

            2. After initial creation, call get method to
                obtain an etag and current shipping setting
                data before call insert.

            3. Modify to wanted shipping setting
                information.

            4. Call insert method with the wanted shipping
                setting information with the etag obtained
                from step 2.

            5. If shipping setting data changed between step
                2 and step 4. Insert request will fail
                because the etag changes every time the
                shipping setting data changes. User should
                repeate step 2-4 with the new etag.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    services: MutableSequence["Service"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="Service",
    )
    warehouses: MutableSequence["Warehouse"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="Warehouse",
    )
    etag: str = proto.Field(
        proto.STRING,
        number=4,
    )


class Service(proto.Message):
    r"""Shipping service.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        service_name (str):
            Required. Free-form name of the service. Must
            be unique within target account.

            This field is a member of `oneof`_ ``_service_name``.
        active (bool):
            Required. A boolean exposing the active
            status of the shipping service.

            This field is a member of `oneof`_ ``_active``.
        delivery_countries (MutableSequence[str]):
            Required. The CLDR territory code of the
            countries to which the service applies.
        currency_code (str):
            The CLDR code of the currency to which this
            service applies. Must match that of the prices
            in rate groups.

            This field is a member of `oneof`_ ``_currency_code``.
        delivery_time (google.shopping.merchant_accounts_v1beta.types.DeliveryTime):
            Required. Time spent in various aspects from
            order to the delivery of the product.

            This field is a member of `oneof`_ ``_delivery_time``.
        rate_groups (MutableSequence[google.shopping.merchant_accounts_v1beta.types.RateGroup]):
            Optional. Shipping rate group definitions. Only the last one
            is allowed to have an empty ``applicable_shipping_labels``,
            which means "everything else". The other
            ``applicable_shipping_labels`` must not overlap.
        shipment_type (google.shopping.merchant_accounts_v1beta.types.Service.ShipmentType):
            Type of locations this service ships orders
            to.

            This field is a member of `oneof`_ ``_shipment_type``.
        minimum_order_value (google.shopping.type.types.Price):
            Minimum order value for this service. If set, indicates that
            customers will have to spend at least this amount. All
            prices within a service must have the same currency. Cannot
            be set together with minimum_order_value_table.

            This field is a member of `oneof`_ ``_minimum_order_value``.
        minimum_order_value_table (google.shopping.merchant_accounts_v1beta.types.MinimumOrderValueTable):
            Table of per store minimum order values for the pickup
            fulfillment type. Cannot be set together with
            minimum_order_value.

            This field is a member of `oneof`_ ``_minimum_order_value_table``.
        store_config (google.shopping.merchant_accounts_v1beta.types.Service.StoreConfig):
            A list of stores your products are delivered
            from. This is only valid for the local delivery
            shipment type.

            This field is a member of `oneof`_ ``_store_config``.
        loyalty_programs (MutableSequence[google.shopping.merchant_accounts_v1beta.types.Service.LoyaltyProgram]):
            Optional. Loyalty programs that this shipping
            service is limited to.
    """

    class ShipmentType(proto.Enum):
        r"""Shipment type of shipping service.

        Values:
            SHIPMENT_TYPE_UNSPECIFIED (0):
                This service did not specify shipment type.
            DELIVERY (1):
                This service ships orders to an address
                chosen by the customer.
            LOCAL_DELIVERY (2):
                This service ships orders to an address
                chosen by the customer. The order is shipped
                from a local store near by.
            COLLECTION_POINT (3):
                This service ships orders to an address
                chosen by the customer. The order is shipped
                from a collection point.
        """

        SHIPMENT_TYPE_UNSPECIFIED = 0
        DELIVERY = 1
        LOCAL_DELIVERY = 2
        COLLECTION_POINT = 3

    class StoreConfig(proto.Message):
        r"""A list of stores your products are delivered from.
        This is only valid for the local delivery shipment type.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            store_service_type (google.shopping.merchant_accounts_v1beta.types.Service.StoreConfig.StoreServiceType):
                Indicates whether all stores, or selected
                stores, listed by this merchant provide local
                delivery.

                This field is a member of `oneof`_ ``_store_service_type``.
            store_codes (MutableSequence[str]):
                Optional. A list of store codes that provide local delivery.
                If empty, then ``all_stores`` must be true.
            cutoff_config (google.shopping.merchant_accounts_v1beta.types.Service.StoreConfig.CutoffConfig):
                Configs related to local delivery ends for
                the day.

                This field is a member of `oneof`_ ``_cutoff_config``.
            service_radius (google.shopping.merchant_accounts_v1beta.types.Distance):
                Maximum delivery radius.
                This is only required for the local delivery
                shipment type.

                This field is a member of `oneof`_ ``_service_radius``.
        """

        class StoreServiceType(proto.Enum):
            r"""Indicates whether all stores, or selected stores, listed by
            the merchant provide local delivery.

            Values:
                STORE_SERVICE_TYPE_UNSPECIFIED (0):
                    Did not specify store service type.
                ALL_STORES (1):
                    Indicates whether all stores, current and
                    future, listed by this merchant provide local
                    delivery.
                SELECTED_STORES (2):
                    Indicates that only the stores listed in ``store_codes`` are
                    eligible for local delivery.
            """

            STORE_SERVICE_TYPE_UNSPECIFIED = 0
            ALL_STORES = 1
            SELECTED_STORES = 2

        class CutoffConfig(proto.Message):
            r"""Configs related to local delivery ends for the day.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                local_cutoff_time (google.shopping.merchant_accounts_v1beta.types.Service.StoreConfig.CutoffConfig.LocalCutoffTime):
                    Time that local delivery ends for the day.

                    This field is a member of `oneof`_ ``_local_cutoff_time``.
                store_close_offset_hours (int):
                    Only valid with local delivery fulfillment. Represents
                    cutoff time as the number of hours before store closing.
                    Mutually exclusive with ``local_cutoff_time``.

                    This field is a member of `oneof`_ ``_store_close_offset_hours``.
                no_delivery_post_cutoff (bool):
                    Merchants can opt-out of showing n+1 day local delivery when
                    they have a shipping service configured to n day local
                    delivery. For example, if the shipping service defines
                    same-day delivery, and it's past the cut-off, setting this
                    field to ``true`` results in the calculated shipping service
                    rate returning ``NO_DELIVERY_POST_CUTOFF``. In the same
                    example, setting this field to ``false`` results in the
                    calculated shipping time being one day. This is only for
                    local delivery.

                    This field is a member of `oneof`_ ``_no_delivery_post_cutoff``.
            """

            class LocalCutoffTime(proto.Message):
                r"""Time that local delivery ends for the day.

                .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

                Attributes:
                    hour (int):
                        Hour local delivery orders must be placed by
                        to process the same day.

                        This field is a member of `oneof`_ ``_hour``.
                    minute (int):
                        Minute local delivery orders must be placed
                        by to process the same day.

                        This field is a member of `oneof`_ ``_minute``.
                """

                hour: int = proto.Field(
                    proto.INT64,
                    number=1,
                    optional=True,
                )
                minute: int = proto.Field(
                    proto.INT64,
                    number=2,
                    optional=True,
                )

            local_cutoff_time: "Service.StoreConfig.CutoffConfig.LocalCutoffTime" = (
                proto.Field(
                    proto.MESSAGE,
                    number=1,
                    optional=True,
                    message="Service.StoreConfig.CutoffConfig.LocalCutoffTime",
                )
            )
            store_close_offset_hours: int = proto.Field(
                proto.INT64,
                number=2,
                optional=True,
            )
            no_delivery_post_cutoff: bool = proto.Field(
                proto.BOOL,
                number=3,
                optional=True,
            )

        store_service_type: "Service.StoreConfig.StoreServiceType" = proto.Field(
            proto.ENUM,
            number=1,
            optional=True,
            enum="Service.StoreConfig.StoreServiceType",
        )
        store_codes: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )
        cutoff_config: "Service.StoreConfig.CutoffConfig" = proto.Field(
            proto.MESSAGE,
            number=3,
            optional=True,
            message="Service.StoreConfig.CutoffConfig",
        )
        service_radius: "Distance" = proto.Field(
            proto.MESSAGE,
            number=4,
            optional=True,
            message="Distance",
        )

    class LoyaltyProgram(proto.Message):
        r"""`Loyalty
        program <https://support.google.com/merchants/answer/12922446>`__
        provided by a merchant.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            program_label (str):
                This is the loyalty program label set in your
                loyalty program settings in Merchant Center.
                This sub-attribute allows Google to map your
                loyalty program to eligible offers.

                This field is a member of `oneof`_ ``_program_label``.
            loyalty_program_tiers (MutableSequence[google.shopping.merchant_accounts_v1beta.types.Service.LoyaltyProgram.LoyaltyProgramTiers]):
                Optional. Loyalty program tier of this
                shipping service.
        """

        class LoyaltyProgramTiers(proto.Message):
            r"""Subset of a merchants loyalty program.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                tier_label (str):
                    The tier label [tier_label] sub-attribute differentiates
                    offer level benefits between each tier. This value is also
                    set in your program settings in Merchant Center, and is
                    required for data source changes even if your loyalty
                    program only has 1 tier.

                    This field is a member of `oneof`_ ``_tier_label``.
            """

            tier_label: str = proto.Field(
                proto.STRING,
                number=1,
                optional=True,
            )

        program_label: str = proto.Field(
            proto.STRING,
            number=1,
            optional=True,
        )
        loyalty_program_tiers: MutableSequence[
            "Service.LoyaltyProgram.LoyaltyProgramTiers"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="Service.LoyaltyProgram.LoyaltyProgramTiers",
        )

    service_name: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    active: bool = proto.Field(
        proto.BOOL,
        number=2,
        optional=True,
    )
    delivery_countries: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    currency_code: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    delivery_time: "DeliveryTime" = proto.Field(
        proto.MESSAGE,
        number=5,
        optional=True,
        message="DeliveryTime",
    )
    rate_groups: MutableSequence["RateGroup"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="RateGroup",
    )
    shipment_type: ShipmentType = proto.Field(
        proto.ENUM,
        number=7,
        optional=True,
        enum=ShipmentType,
    )
    minimum_order_value: types.Price = proto.Field(
        proto.MESSAGE,
        number=8,
        optional=True,
        message=types.Price,
    )
    minimum_order_value_table: "MinimumOrderValueTable" = proto.Field(
        proto.MESSAGE,
        number=9,
        optional=True,
        message="MinimumOrderValueTable",
    )
    store_config: StoreConfig = proto.Field(
        proto.MESSAGE,
        number=10,
        optional=True,
        message=StoreConfig,
    )
    loyalty_programs: MutableSequence[LoyaltyProgram] = proto.RepeatedField(
        proto.MESSAGE,
        number=11,
        message=LoyaltyProgram,
    )


class Distance(proto.Message):
    r"""Maximum delivery radius.
    This is only required for the local delivery shipment type.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        value (int):
            Integer value of distance.

            This field is a member of `oneof`_ ``_value``.
        unit (google.shopping.merchant_accounts_v1beta.types.Distance.Unit):
            Unit can differ based on country, it is
            parameterized to include miles and kilometers.

            This field is a member of `oneof`_ ``_unit``.
    """

    class Unit(proto.Enum):
        r"""Unit can differ based on country, it is parameterized to
        include miles and kilometers.

        Values:
            UNIT_UNSPECIFIED (0):
                Unit unspecified
            MILES (1):
                Unit in miles
            KILOMETERS (2):
                Unit in kilometers
        """

        UNIT_UNSPECIFIED = 0
        MILES = 1
        KILOMETERS = 2

    value: int = proto.Field(
        proto.INT64,
        number=1,
        optional=True,
    )
    unit: Unit = proto.Field(
        proto.ENUM,
        number=2,
        optional=True,
        enum=Unit,
    )


class Warehouse(proto.Message):
    r"""A fulfillment warehouse, which stores and handles inventory.
    Next tag: 7


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. The name of the warehouse. Must be
            unique within account.

            This field is a member of `oneof`_ ``_name``.
        shipping_address (google.shopping.merchant_accounts_v1beta.types.Address):
            Required. Shipping address of the warehouse.

            This field is a member of `oneof`_ ``_shipping_address``.
        cutoff_time (google.shopping.merchant_accounts_v1beta.types.WarehouseCutoffTime):
            Required. The latest time of day that an
            order can be accepted and begin processing.
            Later orders will be processed in the next day.
            The time is based on the warehouse postal code.

            This field is a member of `oneof`_ ``_cutoff_time``.
        handling_days (int):
            Required. The number of days it takes for
            this warehouse to pack up and ship an item. This
            is on the warehouse level, but can be overridden
            on the offer level based on the attributes of an
            item.

            This field is a member of `oneof`_ ``_handling_days``.
        business_day_config (google.shopping.merchant_accounts_v1beta.types.BusinessDayConfig):
            Business days of the warehouse.
            If not set, will be Monday to Friday by default.

            This field is a member of `oneof`_ ``_business_day_config``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    shipping_address: "Address" = proto.Field(
        proto.MESSAGE,
        number=2,
        optional=True,
        message="Address",
    )
    cutoff_time: "WarehouseCutoffTime" = proto.Field(
        proto.MESSAGE,
        number=3,
        optional=True,
        message="WarehouseCutoffTime",
    )
    handling_days: int = proto.Field(
        proto.INT64,
        number=4,
        optional=True,
    )
    business_day_config: "BusinessDayConfig" = proto.Field(
        proto.MESSAGE,
        number=5,
        optional=True,
        message="BusinessDayConfig",
    )


class WarehouseCutoffTime(proto.Message):
    r"""The latest time of day that an order can be accepted and
    begin processing. Later orders will be processed in the next
    day. The time is based on the warehouse postal code.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        hour (int):
            Required. Hour of the cutoff time until which
            an order has to be placed to be processed in the
            same day by the warehouse. Hour is based on the
            timezone of warehouse.

            This field is a member of `oneof`_ ``_hour``.
        minute (int):
            Required. Minute of the cutoff time until
            which an order has to be placed to be processed
            in the same day by the warehouse. Minute is
            based on the timezone of warehouse.

            This field is a member of `oneof`_ ``_minute``.
    """

    hour: int = proto.Field(
        proto.INT32,
        number=1,
        optional=True,
    )
    minute: int = proto.Field(
        proto.INT32,
        number=2,
        optional=True,
    )


class Address(proto.Message):
    r"""Shipping address of the warehouse.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        street_address (str):
            Street-level part of the address. For example:
            ``111w 31st Street``.

            This field is a member of `oneof`_ ``_street_address``.
        city (str):
            Required. City, town or commune. May also
            include dependent localities or sublocalities
            (For example neighborhoods or suburbs).

            This field is a member of `oneof`_ ``_city``.
        administrative_area (str):
            Required. Top-level administrative
            subdivision of the country. For example, a state
            like California ("CA") or a province like Quebec
            ("QC").

            This field is a member of `oneof`_ ``_administrative_area``.
        postal_code (str):
            Required. Postal code or ZIP (For example
            "94043").

            This field is a member of `oneof`_ ``_postal_code``.
        region_code (str):
            Required. `CLDR country
            code <http://www.unicode.org/repos/cldr/tags/latest/common/main/en.xml>`__
            (For example "US").

            This field is a member of `oneof`_ ``_region_code``.
    """

    street_address: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    city: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    administrative_area: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    postal_code: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    region_code: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )


class DeliveryTime(proto.Message):
    r"""Time spent in various aspects from order to the delivery of
    the product.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        min_transit_days (int):
            Minimum number of business days that is spent in transit. 0
            means same day delivery, 1 means next day delivery. Either
            ``min_transit_days``, ``max_transit_days`` or
            ``transit_time_table`` must be set, but not both.

            This field is a member of `oneof`_ ``_min_transit_days``.
        max_transit_days (int):
            Maximum number of business days that is spent in transit. 0
            means same day delivery, 1 means next day delivery. Must be
            greater than or equal to ``min_transit_days``.

            This field is a member of `oneof`_ ``_max_transit_days``.
        cutoff_time (google.shopping.merchant_accounts_v1beta.types.CutoffTime):
            Business days cutoff time definition.
            If not configured the cutoff time will be
            defaulted to 8AM PST.

            This field is a member of `oneof`_ ``_cutoff_time``.
        min_handling_days (int):
            Minimum number of business days spent before an order is
            shipped. 0 means same day shipped, 1 means next day shipped.
            'min_handling_days' and 'max_handling_days' should be either
            set or not set at the same time.

            This field is a member of `oneof`_ ``_min_handling_days``.
        max_handling_days (int):
            Maximum number of business days spent before an order is
            shipped. 0 means same day shipped, 1 means next day shipped.
            Must be greater than or equal to ``min_handling_days``.
            'min_handling_days' and 'max_handling_days' should be either
            set or not set at the same time.

            This field is a member of `oneof`_ ``_max_handling_days``.
        transit_time_table (google.shopping.merchant_accounts_v1beta.types.TransitTable):
            Transit time table, number of business days spent in transit
            based on row and column dimensions. Either
            ``min_transit_days``, ``max_transit_days`` or
            ``transit_time_table`` can be set, but not both.

            This field is a member of `oneof`_ ``_transit_time_table``.
        handling_business_day_config (google.shopping.merchant_accounts_v1beta.types.BusinessDayConfig):
            The business days during which orders can be
            handled. If not provided, Monday to Friday
            business days will be assumed.

            This field is a member of `oneof`_ ``_handling_business_day_config``.
        transit_business_day_config (google.shopping.merchant_accounts_v1beta.types.BusinessDayConfig):
            The business days during which orders can be
            in-transit. If not provided, Monday to Friday
            business days will be assumed.

            This field is a member of `oneof`_ ``_transit_business_day_config``.
        warehouse_based_delivery_times (MutableSequence[google.shopping.merchant_accounts_v1beta.types.WarehouseBasedDeliveryTime]):
            Optional. Indicates that the delivery time should be
            calculated per warehouse (shipping origin location) based on
            the settings of the selected carrier. When set, no other
            transit time related field in [delivery
            time][[google.shopping.content.bundles.ShippingSetting.DeliveryTime]
            should be set.
    """

    min_transit_days: int = proto.Field(
        proto.INT32,
        number=1,
        optional=True,
    )
    max_transit_days: int = proto.Field(
        proto.INT32,
        number=2,
        optional=True,
    )
    cutoff_time: "CutoffTime" = proto.Field(
        proto.MESSAGE,
        number=3,
        optional=True,
        message="CutoffTime",
    )
    min_handling_days: int = proto.Field(
        proto.INT32,
        number=4,
        optional=True,
    )
    max_handling_days: int = proto.Field(
        proto.INT32,
        number=5,
        optional=True,
    )
    transit_time_table: "TransitTable" = proto.Field(
        proto.MESSAGE,
        number=6,
        optional=True,
        message="TransitTable",
    )
    handling_business_day_config: "BusinessDayConfig" = proto.Field(
        proto.MESSAGE,
        number=7,
        optional=True,
        message="BusinessDayConfig",
    )
    transit_business_day_config: "BusinessDayConfig" = proto.Field(
        proto.MESSAGE,
        number=8,
        optional=True,
        message="BusinessDayConfig",
    )
    warehouse_based_delivery_times: MutableSequence["WarehouseBasedDeliveryTime"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=9,
            message="WarehouseBasedDeliveryTime",
        )
    )


class CutoffTime(proto.Message):
    r"""Business days cutoff time definition.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        hour (int):
            Required. Hour of the cutoff time until which
            an order has to be placed to be processed in the
            same day.

            This field is a member of `oneof`_ ``_hour``.
        minute (int):
            Required. Minute of the cutoff time until
            which an order has to be placed to be processed
            in the same day.

            This field is a member of `oneof`_ ``_minute``.
        time_zone (str):
            Required. `Timezone
            identifier <https://developers.google.com/adwords/api/docs/appendix/codes-formats#timezone-ids>`__
            For example "Europe/Zurich".

            This field is a member of `oneof`_ ``_time_zone``.
    """

    hour: int = proto.Field(
        proto.INT32,
        number=1,
        optional=True,
    )
    minute: int = proto.Field(
        proto.INT32,
        number=2,
        optional=True,
    )
    time_zone: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )


class BusinessDayConfig(proto.Message):
    r"""Business days of the warehouse.

    Attributes:
        business_days (MutableSequence[google.shopping.merchant_accounts_v1beta.types.BusinessDayConfig.Weekday]):
            Required. Regular business days.
            May not be empty.
    """

    class Weekday(proto.Enum):
        r"""

        Values:
            WEEKDAY_UNSPECIFIED (0):
                No description available.
            MONDAY (1):
                No description available.
            TUESDAY (2):
                No description available.
            WEDNESDAY (3):
                No description available.
            THURSDAY (4):
                No description available.
            FRIDAY (5):
                No description available.
            SATURDAY (6):
                No description available.
            SUNDAY (7):
                No description available.
        """

        WEEKDAY_UNSPECIFIED = 0
        MONDAY = 1
        TUESDAY = 2
        WEDNESDAY = 3
        THURSDAY = 4
        FRIDAY = 5
        SATURDAY = 6
        SUNDAY = 7

    business_days: MutableSequence[Weekday] = proto.RepeatedField(
        proto.ENUM,
        number=1,
        enum=Weekday,
    )


class WarehouseBasedDeliveryTime(proto.Message):
    r"""Indicates that the delivery time should be calculated per warehouse
    (shipping origin location) based on the settings of the selected
    carrier. When set, no other transit time related field in
    ``delivery_time`` should be set.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        carrier (str):
            Required. Carrier, such as ``"UPS"`` or ``"Fedex"``.

            This field is a member of `oneof`_ ``_carrier``.
        carrier_service (str):
            Required. Carrier service, such as ``"ground"`` or
            ``"2 days"``. The name of the service must be in the
            eddSupportedServices list.

            This field is a member of `oneof`_ ``_carrier_service``.
        warehouse (str):
            Required. Warehouse name. This should match
            [warehouse][ShippingSetting.warehouses.name]

            This field is a member of `oneof`_ ``_warehouse``.
    """

    carrier: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    carrier_service: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    warehouse: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )


class RateGroup(proto.Message):
    r"""Shipping rate group definitions. Only the last one is allowed to
    have an empty ``applicable_shipping_labels``, which means
    "everything else". The other ``applicable_shipping_labels`` must not
    overlap.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        applicable_shipping_labels (MutableSequence[str]):
            Required. A list of `shipping
            labels <https://support.google.com/merchants/answer/6324504>`__
            defining the products to which this rate group applies to.
            This is a disjunction: only one of the labels has to match
            for the rate group to apply. May only be empty for the last
            rate group of a service.
        single_value (google.shopping.merchant_accounts_v1beta.types.Value):
            The value of the rate group (For example flat rate $10). Can
            only be set if ``main_table`` and ``subtables`` are not set.

            This field is a member of `oneof`_ ``_single_value``.
        main_table (google.shopping.merchant_accounts_v1beta.types.Table):
            A table defining the rate group, when ``single_value`` is
            not expressive enough. Can only be set if ``single_value``
            is not set.

            This field is a member of `oneof`_ ``_main_table``.
        subtables (MutableSequence[google.shopping.merchant_accounts_v1beta.types.Table]):
            Optional. A list of subtables referred to by ``main_table``.
            Can only be set if ``main_table`` is set.
        carrier_rates (MutableSequence[google.shopping.merchant_accounts_v1beta.types.CarrierRate]):
            Optional. A list of carrier rates that can be referred to by
            ``main_table`` or ``single_value``.
        name (str):
            Optional. Name of the rate group.
            If set has to be unique within shipping service.

            This field is a member of `oneof`_ ``_name``.
    """

    applicable_shipping_labels: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    single_value: "Value" = proto.Field(
        proto.MESSAGE,
        number=2,
        optional=True,
        message="Value",
    )
    main_table: "Table" = proto.Field(
        proto.MESSAGE,
        number=3,
        optional=True,
        message="Table",
    )
    subtables: MutableSequence["Table"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="Table",
    )
    carrier_rates: MutableSequence["CarrierRate"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="CarrierRate",
    )
    name: str = proto.Field(
        proto.STRING,
        number=6,
        optional=True,
    )


class Table(proto.Message):
    r"""A table defining the rate group, when ``single_value`` is not
    expressive enough.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Name of the table. Required for subtables,
            ignored for the main table.

            This field is a member of `oneof`_ ``_name``.
        row_headers (google.shopping.merchant_accounts_v1beta.types.Headers):
            Required. Headers of the table's rows.

            This field is a member of `oneof`_ ``_row_headers``.
        column_headers (google.shopping.merchant_accounts_v1beta.types.Headers):
            Headers of the table's columns. Optional: if
            not set then the table has only one dimension.

            This field is a member of `oneof`_ ``_column_headers``.
        rows (MutableSequence[google.shopping.merchant_accounts_v1beta.types.Row]):
            Required. The list of rows that constitute the table. Must
            have the same length as ``row_headers``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    row_headers: "Headers" = proto.Field(
        proto.MESSAGE,
        number=2,
        optional=True,
        message="Headers",
    )
    column_headers: "Headers" = proto.Field(
        proto.MESSAGE,
        number=3,
        optional=True,
        message="Headers",
    )
    rows: MutableSequence["Row"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="Row",
    )


class TransitTable(proto.Message):
    r"""Transit time table, number of business days spent in transit based
    on row and column dimensions. Either ``min_transit_days``,
    ``max_transit_days`` or ``transit_time_table`` can be set, but not
    both.

    Attributes:
        postal_code_group_names (MutableSequence[str]):
            Required. A list of region names
            [Region.name][google.shopping.merchant.accounts.v1beta.Region.name]
            . The last value can be ``"all other locations"``. Example:
            ``["zone 1", "zone 2", "all other locations"]``. The
            referred postal code groups must match the delivery country
            of the service.
        transit_time_labels (MutableSequence[str]):
            Required. A list of transit time labels. The last value can
            be ``"all other labels"``. Example:
            ``["food", "electronics", "all other labels"]``.
        rows (MutableSequence[google.shopping.merchant_accounts_v1beta.types.TransitTable.TransitTimeRow]):
            Required. If there's only one dimension set of
            ``postal_code_group_names`` or ``transit_time_labels``,
            there are multiple rows each with one value for that
            dimension. If there are two dimensions, each row corresponds
            to a ``postal_code_group_names``, and columns (values) to a
            ``transit_time_labels``.
    """

    class TransitTimeRow(proto.Message):
        r"""If there's only one dimension set of ``postal_code_group_names`` or
        ``transit_time_labels``, there are multiple rows each with one value
        for that dimension. If there are two dimensions, each row
        corresponds to a ``postal_code_group_names``, and columns (values)
        to a ``transit_time_labels``.

        Attributes:
            values (MutableSequence[google.shopping.merchant_accounts_v1beta.types.TransitTable.TransitTimeRow.TransitTimeValue]):
                Required. Transit time range (min-max) in
                business days.
        """

        class TransitTimeValue(proto.Message):
            r"""Transit time range (min-max) in business days.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                min_transit_days (int):
                    Minimum transit time range in business days.
                    0 means same day delivery, 1 means next day
                    delivery.

                    This field is a member of `oneof`_ ``_min_transit_days``.
                max_transit_days (int):
                    Must be greater than or equal to ``min_transit_days``.

                    This field is a member of `oneof`_ ``_max_transit_days``.
            """

            min_transit_days: int = proto.Field(
                proto.INT32,
                number=1,
                optional=True,
            )
            max_transit_days: int = proto.Field(
                proto.INT32,
                number=2,
                optional=True,
            )

        values: MutableSequence["TransitTable.TransitTimeRow.TransitTimeValue"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=1,
                message="TransitTable.TransitTimeRow.TransitTimeValue",
            )
        )

    postal_code_group_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    transit_time_labels: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    rows: MutableSequence[TransitTimeRow] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=TransitTimeRow,
    )


class MinimumOrderValueTable(proto.Message):
    r"""Table of per store minimum order values for the pickup
    fulfillment type.

    Attributes:
        store_code_set_with_movs (MutableSequence[google.shopping.merchant_accounts_v1beta.types.MinimumOrderValueTable.StoreCodeSetWithMov]):
            Required. A list of store code sets sharing
            the same minimum order value (MOV). At least two
            sets are required and the last one must be
            empty, which signifies 'MOV for all other
            stores'. Each store code can only appear once
            across all the sets. All prices within a service
            must have the same currency.
    """

    class StoreCodeSetWithMov(proto.Message):
        r"""A list of store code sets sharing the same minimum order
        value. At least two sets are required and the last one must be
        empty, which signifies 'MOV for all other stores'.
        Each store code can only appear once across all the sets. All
        prices within a service must have the same currency.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            store_codes (MutableSequence[str]):
                Optional. A list of unique store codes or
                empty for the catch all.
            value (google.shopping.type.types.Price):
                The minimum order value for the given stores.

                This field is a member of `oneof`_ ``_value``.
        """

        store_codes: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        value: types.Price = proto.Field(
            proto.MESSAGE,
            number=2,
            optional=True,
            message=types.Price,
        )

    store_code_set_with_movs: MutableSequence[StoreCodeSetWithMov] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=StoreCodeSetWithMov,
        )
    )


class Headers(proto.Message):
    r"""A non-empty list of row or column headers for a table. Exactly one
    of ``prices``, ``weights``, ``num_items``,
    ``postal_code_group_names``, or ``location`` must be set.

    Attributes:
        prices (MutableSequence[google.shopping.type.types.Price]):
            Required. A list of inclusive order price upper bounds. The
            last price's value can be infinity by setting price
            amount_micros = -1. For example
            ``[{"amount_micros": 10000000, "currency_code": "USD"}, {"amount_micros": 500000000, "currency_code": "USD"}, {"amount_micros": -1, "currency_code": "USD"}]``
            represents the headers "<= $10", "<= $500", and "> $500".
            All prices within a service must have the same currency.
            Must be non-empty. Must be positive except -1. Can only be
            set if all other fields are not set.
        weights (MutableSequence[google.shopping.type.types.Weight]):
            Required. A list of inclusive order weight upper bounds. The
            last weight's value can be infinity by setting price
            amount_micros = -1. For example
            ``[{"amount_micros": 10000000, "unit": "kg"}, {"amount_micros": 50000000, "unit": "kg"}, {"amount_micros": -1, "unit": "kg"}]``
            represents the headers "<= 10kg", "<= 50kg", and "> 50kg".
            All weights within a service must have the same unit. Must
            be non-empty. Must be positive except -1. Can only be set if
            all other fields are not set.
        number_of_items (MutableSequence[str]):
            Required. A list of inclusive number of items upper bounds.
            The last value can be ``"infinity"``. For example
            ``["10", "50", "infinity"]`` represents the headers "<= 10
            items", "<= 50 items", and "> 50 items". Must be non-empty.
            Can only be set if all other fields are not set.
        postal_code_group_names (MutableSequence[str]):
            Required. A list of postal group names. The last value can
            be ``"all other locations"``. Example:
            ``["zone 1", "zone 2", "all other locations"]``. The
            referred postal code groups must match the delivery country
            of the service. Must be non-empty. Can only be set if all
            other fields are not set.
        locations (MutableSequence[google.shopping.merchant_accounts_v1beta.types.LocationIdSet]):
            Required. A list of location ID sets. Must be
            non-empty. Can only be set if all other fields
            are not set.
    """

    prices: MutableSequence[types.Price] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=types.Price,
    )
    weights: MutableSequence[types.Weight] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=types.Weight,
    )
    number_of_items: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    postal_code_group_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    locations: MutableSequence["LocationIdSet"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="LocationIdSet",
    )


class LocationIdSet(proto.Message):
    r"""A list of location ID sets. Must be non-empty. Can only be
    set if all other fields are not set.

    Attributes:
        location_ids (MutableSequence[str]):
            Required. A non-empty list of `location
            IDs <https://developers.google.com/adwords/api/docs/appendix/geotargeting>`__.
            They must all be of the same location type (For example,
            state).
    """

    location_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class Row(proto.Message):
    r"""Include a list of cells.

    Attributes:
        cells (MutableSequence[google.shopping.merchant_accounts_v1beta.types.Value]):
            Required. The list of cells that constitute the row. Must
            have the same length as ``columnHeaders`` for
            two-dimensional tables, a length of 1 for one-dimensional
            tables.
    """

    cells: MutableSequence["Value"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Value",
    )


class Value(proto.Message):
    r"""The single value of a rate group or the value of a rate group
    table's cell. Exactly one of ``no_shipping``, ``flat_rate``,
    ``price_percentage``, ``carrier_rateName``, ``subtable_name`` must
    be set.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        no_shipping (bool):
            If true, then the product can't be shipped.
            Must be true when set, can only be set if all
            other fields are not set.

            This field is a member of `oneof`_ ``_no_shipping``.
        flat_rate (google.shopping.type.types.Price):
            A flat rate. Can only be set if all other
            fields are not set.

            This field is a member of `oneof`_ ``_flat_rate``.
        price_percentage (str):
            A percentage of the price represented as a number in decimal
            notation (For example, ``"5.4"``). Can only be set if all
            other fields are not set.

            This field is a member of `oneof`_ ``_price_percentage``.
        carrier_rate (str):
            The name of a carrier rate referring to a
            carrier rate defined in the same rate group. Can
            only be set if all other fields are not set.

            This field is a member of `oneof`_ ``_carrier_rate``.
        subtable (str):
            The name of a subtable. Can only be set in
            table cells (For example, not for single
            values), and only if all other fields are not
            set.

            This field is a member of `oneof`_ ``_subtable``.
    """

    no_shipping: bool = proto.Field(
        proto.BOOL,
        number=1,
        optional=True,
    )
    flat_rate: types.Price = proto.Field(
        proto.MESSAGE,
        number=2,
        optional=True,
        message=types.Price,
    )
    price_percentage: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    carrier_rate: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    subtable: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )


class CarrierRate(proto.Message):
    r"""A list of carrier rates that can be referred to by ``main_table`` or
    ``single_value``.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. Name of the carrier rate. Must be
            unique per rate group.

            This field is a member of `oneof`_ ``_name``.
        carrier (str):
            Required. Carrier service, such as ``"UPS"`` or ``"Fedex"``.

            This field is a member of `oneof`_ ``_carrier``.
        carrier_service (str):
            Required. Carrier service, such as ``"ground"`` or
            ``"2 days"``.

            This field is a member of `oneof`_ ``_carrier_service``.
        origin_postal_code (str):
            Required. Shipping origin for this carrier
            rate.

            This field is a member of `oneof`_ ``_origin_postal_code``.
        percentage_adjustment (str):
            Optional. Multiplicative shipping rate modifier as a number
            in decimal notation. Can be negative. For example ``"5.4"``
            increases the rate by 5.4%, ``"-3"`` decreases the rate by
            3%.

            This field is a member of `oneof`_ ``_percentage_adjustment``.
        flat_adjustment (google.shopping.type.types.Price):
            Optional. Additive shipping rate modifier. Can be negative.
            For example
            ``{ "amount_micros": 1, "currency_code" : "USD" }`` adds $1
            to the rate,
            ``{ "amount_micros": -3, "currency_code" : "USD" }`` removes
            $3 from the rate.

            This field is a member of `oneof`_ ``_flat_adjustment``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    carrier: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    carrier_service: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    origin_postal_code: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    percentage_adjustment: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    flat_adjustment: types.Price = proto.Field(
        proto.MESSAGE,
        number=6,
        optional=True,
        message=types.Price,
    )


class GetShippingSettingsRequest(proto.Message):
    r"""Request message for the ``GetShippingSetting`` method.

    Attributes:
        name (str):
            Required. The name of the shipping setting to retrieve.
            Format: ``accounts/{account}/shippingsetting``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class InsertShippingSettingsRequest(proto.Message):
    r"""Request message for the ``InsertShippingSetting`` method.

    Attributes:
        parent (str):
            Required. The account where this product will
            be inserted. Format: accounts/{account}
        shipping_setting (google.shopping.merchant_accounts_v1beta.types.ShippingSettings):
            Required. The new version of the account.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    shipping_setting: "ShippingSettings" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ShippingSettings",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
