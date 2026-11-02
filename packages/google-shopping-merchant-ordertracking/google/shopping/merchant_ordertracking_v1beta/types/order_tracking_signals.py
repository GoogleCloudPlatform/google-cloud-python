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

import google.type.datetime_pb2 as datetime_pb2  # type: ignore
import proto  # type: ignore
from google.shopping.type.types import types

__protobuf__ = proto.module(
    package="google.shopping.merchant.ordertracking.v1beta",
    manifest={
        "CreateOrderTrackingSignalRequest",
        "OrderTrackingSignal",
    },
)


class CreateOrderTrackingSignalRequest(proto.Message):
    r"""Signals only can be created but not updated.
    Businesses need to call this API only when the order is
    completely shipped. Creates new order signal.

    Attributes:
        parent (str):
            Required. The account of the business for
            which the order signal is created. Format:
            accounts/{account}
        order_tracking_signal_id (str):
            Output only. The ID that uniquely identifies
            this order tracking signal.
        order_tracking_signal (google.shopping.merchant_ordertracking_v1beta.types.OrderTrackingSignal):
            Required. The order signal to be created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    order_tracking_signal_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    order_tracking_signal: "OrderTrackingSignal" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="OrderTrackingSignal",
    )


class OrderTrackingSignal(proto.Message):
    r"""Represents a business trade from which signals are extracted,
    such as shipping.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        order_tracking_signal_id (int):
            Output only. The ID that uniquely identifies
            this order tracking signal.
        merchant_id (int):
            Optional. The Google Merchant Center ID of this order
            tracking signal. This value is optional. If left unset, the
            caller's Merchant Center ID is used. You must request access
            in order to provide data on behalf of another business. For
            more information, see `Submitting Order Tracking
            Signals </shopping-content/guides/order-tracking-signals>`__.
        order_created_time (google.type.datetime_pb2.DateTime):
            Required. The time when the order was created
            on the businesses side. Include the year and
            timezone string, if available.
        order_id (str):
            Required. The ID of the order on the
            businesses side. This field will be hashed in
            returned OrderTrackingSignal creation response.
        shipping_info (MutableSequence[google.shopping.merchant_ordertracking_v1beta.types.OrderTrackingSignal.ShippingInfo]):
            Required. The shipping information for the
            order.
        line_items (MutableSequence[google.shopping.merchant_ordertracking_v1beta.types.OrderTrackingSignal.LineItemDetails]):
            Required. Information about line items in the
            order.
        shipment_line_item_mapping (MutableSequence[google.shopping.merchant_ordertracking_v1beta.types.OrderTrackingSignal.ShipmentLineItemMapping]):
            Optional. The mapping of the line items to
            the shipment information.
        customer_shipping_fee (google.shopping.type.types.Price):
            Optional. The shipping fee of the order;
            this value should be set to zero in the case of
            free shipping.

            This field is a member of `oneof`_ ``_customer_shipping_fee``.
        delivery_postal_code (str):
            Optional. The delivery postal code, as a
            continuous string without spaces or dashes, for
            example "95016". This field will be anonymized
            in returned OrderTrackingSignal creation
            response.
        delivery_region_code (str):
            Optional. The [CLDR territory code]
            (http://www.unicode.org/repos/cldr/tags/latest/common/main/en.xml)
            for the shipping destination.
    """

    class ShippingInfo(proto.Message):
        r"""The shipping information for the order.

        Attributes:
            shipment_id (str):
                Required. The shipment ID. This field will be
                hashed in returned OrderTrackingSignal creation
                response.
            tracking_id (str):
                Optional. The tracking ID of the shipment. This field is
                required if one of the following fields is absent:
                earliest_delivery_promise_time,
                latest_delivery_promise_time, and actual_delivery_time.
            carrier (str):
                Optional. The name of the shipping carrier for the delivery.
                This field is required if one of the following fields is
                absent: earliest_delivery_promise_time,
                latest_delivery_promise_time, and actual_delivery_time.
            carrier_service (str):
                Optional. The service type for fulfillment, such as GROUND,
                FIRST_CLASS, etc.
            shipped_time (google.type.datetime_pb2.DateTime):
                Optional. The time when the shipment was
                shipped. Include the year and timezone string,
                if available.
            earliest_delivery_promise_time (google.type.datetime_pb2.DateTime):
                Optional. The earliest delivery promised time. Include the
                year and timezone string, if available. This field is
                required, if one of the following fields is absent:
                tracking_id or carrier_name.
            latest_delivery_promise_time (google.type.datetime_pb2.DateTime):
                Optional. The latest delivery promised time. Include the
                year and timezone string, if available. This field is
                required, if one of the following fields is absent:
                tracking_id or carrier_name.
            actual_delivery_time (google.type.datetime_pb2.DateTime):
                Optional. The time when the shipment was actually delivered.
                Include the year and timezone string, if available. This
                field is required, if one of the following fields is absent:
                tracking_id or carrier_name.
            shipping_status (google.shopping.merchant_ordertracking_v1beta.types.OrderTrackingSignal.ShippingInfo.ShippingState):
                Required. The status of the shipment.
            origin_postal_code (str):
                Required. The origin postal code, as a
                continuous string without spaces or dashes, for
                example "95016". This field will be anonymized
                in returned OrderTrackingSignal creation
                response.
            origin_region_code (str):
                Required. The [CLDR territory code]
                (http://www.unicode.org/repos/cldr/tags/latest/common/main/en.xml)
                for the shipping origin.
        """

        class ShippingState(proto.Enum):
            r"""The current status of the shipments.

            Values:
                SHIPPING_STATE_UNSPECIFIED (0):
                    The shipping status is not known to business.
                SHIPPED (1):
                    All items are shipped.
                DELIVERED (2):
                    The shipment is already delivered.
            """

            SHIPPING_STATE_UNSPECIFIED = 0
            SHIPPED = 1
            DELIVERED = 2

        shipment_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        tracking_id: str = proto.Field(
            proto.STRING,
            number=2,
        )
        carrier: str = proto.Field(
            proto.STRING,
            number=3,
        )
        carrier_service: str = proto.Field(
            proto.STRING,
            number=4,
        )
        shipped_time: datetime_pb2.DateTime = proto.Field(
            proto.MESSAGE,
            number=5,
            message=datetime_pb2.DateTime,
        )
        earliest_delivery_promise_time: datetime_pb2.DateTime = proto.Field(
            proto.MESSAGE,
            number=6,
            message=datetime_pb2.DateTime,
        )
        latest_delivery_promise_time: datetime_pb2.DateTime = proto.Field(
            proto.MESSAGE,
            number=7,
            message=datetime_pb2.DateTime,
        )
        actual_delivery_time: datetime_pb2.DateTime = proto.Field(
            proto.MESSAGE,
            number=8,
            message=datetime_pb2.DateTime,
        )
        shipping_status: "OrderTrackingSignal.ShippingInfo.ShippingState" = proto.Field(
            proto.ENUM,
            number=9,
            enum="OrderTrackingSignal.ShippingInfo.ShippingState",
        )
        origin_postal_code: str = proto.Field(
            proto.STRING,
            number=10,
        )
        origin_region_code: str = proto.Field(
            proto.STRING,
            number=11,
        )

    class LineItemDetails(proto.Message):
        r"""The line items of the order.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            line_item_id (str):
                Required. The ID for this line item.
            product_id (str):
                Required. The Content API REST ID of the
                product, in the form
                channel:contentLanguage:targetCountry:offerId.
            gtin (str):
                Optional. The Global Trade Item Number.
            mpn (str):
                Optional. The manufacturer part number.
            product_title (str):
                Optional. Plain text title of this product.

                This field is a member of `oneof`_ ``_product_title``.
            brand (str):
                Optional. Brand of the product.

                This field is a member of `oneof`_ ``_brand``.
            quantity (int):
                Required. The quantity of the line item in
                the order.
        """

        line_item_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        product_id: str = proto.Field(
            proto.STRING,
            number=2,
        )
        gtin: str = proto.Field(
            proto.STRING,
            number=3,
        )
        mpn: str = proto.Field(
            proto.STRING,
            number=4,
        )
        product_title: str = proto.Field(
            proto.STRING,
            number=5,
            optional=True,
        )
        brand: str = proto.Field(
            proto.STRING,
            number=6,
            optional=True,
        )
        quantity: int = proto.Field(
            proto.INT64,
            number=7,
        )

    class ShipmentLineItemMapping(proto.Message):
        r"""Represents how many items are in the shipment for the given
        shipment_id and line_item_id.

        Attributes:
            shipment_id (str):
                Required. The shipment ID. This field will be
                hashed in returned OrderTrackingSignal creation
                response.
            line_item_id (str):
                Required. The line item ID.
            quantity (int):
                Required. The line item quantity in the
                shipment.
        """

        shipment_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        line_item_id: str = proto.Field(
            proto.STRING,
            number=2,
        )
        quantity: int = proto.Field(
            proto.INT64,
            number=3,
        )

    order_tracking_signal_id: int = proto.Field(
        proto.INT64,
        number=11,
    )
    merchant_id: int = proto.Field(
        proto.INT64,
        number=12,
    )
    order_created_time: datetime_pb2.DateTime = proto.Field(
        proto.MESSAGE,
        number=1,
        message=datetime_pb2.DateTime,
    )
    order_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    shipping_info: MutableSequence[ShippingInfo] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=ShippingInfo,
    )
    line_items: MutableSequence[LineItemDetails] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=LineItemDetails,
    )
    shipment_line_item_mapping: MutableSequence[ShipmentLineItemMapping] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=5,
            message=ShipmentLineItemMapping,
        )
    )
    customer_shipping_fee: types.Price = proto.Field(
        proto.MESSAGE,
        number=6,
        optional=True,
        message=types.Price,
    )
    delivery_postal_code: str = proto.Field(
        proto.STRING,
        number=9,
    )
    delivery_region_code: str = proto.Field(
        proto.STRING,
        number=10,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
