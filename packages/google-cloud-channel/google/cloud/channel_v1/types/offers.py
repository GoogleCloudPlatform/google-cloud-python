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
import google.type.money_pb2 as money_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.channel_v1.types import common, products

__protobuf__ = proto.module(
    package="google.cloud.channel.v1",
    manifest={
        "PromotionalOrderType",
        "PaymentPlan",
        "PaymentType",
        "ResourceType",
        "PeriodType",
        "DiscountType",
        "Offer",
        "ParameterDefinition",
        "Constraints",
        "CustomerConstraints",
        "Plan",
        "PriceByResource",
        "Price",
        "PricePhase",
        "PriceTier",
        "Period",
        "DiscountComponent",
    },
)


class PromotionalOrderType(proto.Enum):
    r"""Constraints type for Promotional offers.

    Values:
        PROMOTIONAL_TYPE_UNSPECIFIED (0):
            Not used.
        NEW_UPGRADE (1):
            Order used for new customers, trial
            conversions and upgrades.
        TRANSFER (2):
            All orders for transferring an existing
            customer.
        PROMOTION_SWITCH (3):
            Orders for modifying an existing customer's
            promotion on the same SKU.
    """

    PROMOTIONAL_TYPE_UNSPECIFIED = 0
    NEW_UPGRADE = 1
    TRANSFER = 2
    PROMOTION_SWITCH = 3


class PaymentPlan(proto.Enum):
    r"""Describes how the reseller will be billed.

    Values:
        PAYMENT_PLAN_UNSPECIFIED (0):
            Not used.
        COMMITMENT (1):
            Commitment.
        FLEXIBLE (2):
            No commitment.
        FREE (3):
            Free.
        TRIAL (4):
            Trial.
        OFFLINE (5):
            Price and ordering not available through API.
    """

    PAYMENT_PLAN_UNSPECIFIED = 0
    COMMITMENT = 1
    FLEXIBLE = 2
    FREE = 3
    TRIAL = 4
    OFFLINE = 5


class PaymentType(proto.Enum):
    r"""Specifies when the payment needs to happen.

    Values:
        PAYMENT_TYPE_UNSPECIFIED (0):
            Not used.
        PREPAY (1):
            Prepay. Amount has to be paid before service
            is rendered.
        POSTPAY (2):
            Postpay. Reseller is charged at the end of
            the Payment cycle.
    """

    PAYMENT_TYPE_UNSPECIFIED = 0
    PREPAY = 1
    POSTPAY = 2


class ResourceType(proto.Enum):
    r"""Represents the type for a monetizable resource(any entity on
    which billing happens). For example, this could be MINUTES for
    Google Voice and GB for Google Drive. One SKU can map to
    multiple monetizable resources.

    Values:
        RESOURCE_TYPE_UNSPECIFIED (0):
            Not used.
        SEAT (1):
            Seat.
        MAU (2):
            Monthly active user.
        GB (3):
            GB (used for storage SKUs).
        LICENSED_USER (4):
            Active licensed users(for Voice SKUs).
        MINUTES (5):
            Voice usage.
        IAAS_USAGE (6):
            For IaaS SKUs like Google Cloud, monetization
            is based on usage accrued on your billing
            account irrespective of the type of monetizable
            resource. This enum represents an aggregated
            resource/container for all usage SKUs on a
            billing account. Currently, only applicable to
            Google Cloud.
        SUBSCRIPTION (7):
            For Google Cloud subscriptions like Anthos or
            SAP.
    """

    RESOURCE_TYPE_UNSPECIFIED = 0
    SEAT = 1
    MAU = 2
    GB = 3
    LICENSED_USER = 4
    MINUTES = 5
    IAAS_USAGE = 6
    SUBSCRIPTION = 7


class PeriodType(proto.Enum):
    r"""Period Type.

    Values:
        PERIOD_TYPE_UNSPECIFIED (0):
            Not used.
        DAY (1):
            Day.
        MONTH (2):
            Month.
        YEAR (3):
            Year.
    """

    PERIOD_TYPE_UNSPECIFIED = 0
    DAY = 1
    MONTH = 2
    YEAR = 3


class DiscountType(proto.Enum):
    r"""Discount Type.

    Values:
        DISCOUNT_TYPE_UNSPECIFIED (0):
            Not used.
        REGIONAL_DISCOUNT (1):
            Regional discount.
        PROMOTIONAL_DISCOUNT (2):
            Promotional discount.
        SALES_DISCOUNT (3):
            Sales-provided discount.
        RESELLER_MARGIN (4):
            Reseller margin.
        DEAL_CODE (5):
            Deal code discount.
    """

    DISCOUNT_TYPE_UNSPECIFIED = 0
    REGIONAL_DISCOUNT = 1
    PROMOTIONAL_DISCOUNT = 2
    SALES_DISCOUNT = 3
    RESELLER_MARGIN = 4
    DEAL_CODE = 5


class Offer(proto.Message):
    r"""Represents an offer made to resellers for purchase. An offer is
    associated with a [Sku][google.cloud.channel.v1.Sku], has a plan for
    payment, a price, and defines the constraints for buying.

    Attributes:
        name (str):
            Resource Name of the Offer. Format:
            accounts/{account_id}/offers/{offer_id}
        marketing_info (google.cloud.channel_v1.types.MarketingInfo):
            Marketing information for the Offer.
        sku (google.cloud.channel_v1.types.Sku):
            SKU the offer is associated with.
        plan (google.cloud.channel_v1.types.Plan):
            Describes the payment plan for the Offer.
        constraints (google.cloud.channel_v1.types.Constraints):
            Constraints on transacting the Offer.
        price_by_resources (MutableSequence[google.cloud.channel_v1.types.PriceByResource]):
            Price for each monetizable resource type.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Start of the Offer validity time.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. End of the Offer validity time.
        parameter_definitions (MutableSequence[google.cloud.channel_v1.types.ParameterDefinition]):
            Parameters required to use current Offer to
            purchase.
        deal_code (str):
            The deal code of the offer to get a special
            promotion or discount.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    marketing_info: products.MarketingInfo = proto.Field(
        proto.MESSAGE,
        number=2,
        message=products.MarketingInfo,
    )
    sku: products.Sku = proto.Field(
        proto.MESSAGE,
        number=3,
        message=products.Sku,
    )
    plan: "Plan" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="Plan",
    )
    constraints: "Constraints" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="Constraints",
    )
    price_by_resources: MutableSequence["PriceByResource"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="PriceByResource",
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    parameter_definitions: MutableSequence["ParameterDefinition"] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message="ParameterDefinition",
    )
    deal_code: str = proto.Field(
        proto.STRING,
        number=12,
    )


class ParameterDefinition(proto.Message):
    r"""Parameter's definition. Specifies what parameter is required
    to use the current Offer to purchase.

    Attributes:
        name (str):
            Name of the parameter.
        parameter_type (google.cloud.channel_v1.types.ParameterDefinition.ParameterType):
            Data type of the parameter. Minimal value,
            Maximum value and allowed values will use
            specified data type here.
        min_value (google.cloud.channel_v1.types.Value):
            Minimal value of the parameter, if
            applicable. Inclusive. For example, minimal
            commitment when purchasing Anthos is 0.01.
            Applicable to INT64 and DOUBLE parameter types.
        max_value (google.cloud.channel_v1.types.Value):
            Maximum value of the parameter, if
            applicable. Inclusive. For example, maximum
            seats when purchasing Google Workspace Business
            Standard. Applicable to INT64 and DOUBLE
            parameter types.
        allowed_values (MutableSequence[google.cloud.channel_v1.types.Value]):
            If not empty, parameter values must be drawn from this list.
            For example, [us-west1, us-west2, ...] Applicable to STRING
            parameter type.
        optional (bool):
            If set to true, parameter is optional to
            purchase this Offer.
    """

    class ParameterType(proto.Enum):
        r"""Data type of the parameter.

        Values:
            PARAMETER_TYPE_UNSPECIFIED (0):
                Not used.
            INT64 (1):
                Int64 type.
            STRING (2):
                String type.
            DOUBLE (3):
                Double type.
            BOOLEAN (4):
                Boolean type.
        """

        PARAMETER_TYPE_UNSPECIFIED = 0
        INT64 = 1
        STRING = 2
        DOUBLE = 3
        BOOLEAN = 4

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    parameter_type: ParameterType = proto.Field(
        proto.ENUM,
        number=2,
        enum=ParameterType,
    )
    min_value: common.Value = proto.Field(
        proto.MESSAGE,
        number=3,
        message=common.Value,
    )
    max_value: common.Value = proto.Field(
        proto.MESSAGE,
        number=4,
        message=common.Value,
    )
    allowed_values: MutableSequence[common.Value] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message=common.Value,
    )
    optional: bool = proto.Field(
        proto.BOOL,
        number=6,
    )


class Constraints(proto.Message):
    r"""Represents the constraints for buying the Offer.

    Attributes:
        customer_constraints (google.cloud.channel_v1.types.CustomerConstraints):
            Represents constraints required to purchase
            the Offer for a customer.
    """

    customer_constraints: "CustomerConstraints" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="CustomerConstraints",
    )


class CustomerConstraints(proto.Message):
    r"""Represents constraints required to purchase the Offer for a
    customer.

    Attributes:
        allowed_regions (MutableSequence[str]):
            Allowed geographical regions of the customer.
        allowed_customer_types (MutableSequence[google.cloud.channel_v1.types.CloudIdentityInfo.CustomerType]):
            Allowed Customer Type.
        promotional_order_types (MutableSequence[google.cloud.channel_v1.types.PromotionalOrderType]):
            Allowed Promotional Order Type. Present for
            Promotional offers.
    """

    allowed_regions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    allowed_customer_types: MutableSequence[common.CloudIdentityInfo.CustomerType] = (
        proto.RepeatedField(
            proto.ENUM,
            number=2,
            enum=common.CloudIdentityInfo.CustomerType,
        )
    )
    promotional_order_types: MutableSequence["PromotionalOrderType"] = (
        proto.RepeatedField(
            proto.ENUM,
            number=3,
            enum="PromotionalOrderType",
        )
    )


class Plan(proto.Message):
    r"""The payment plan for the Offer. Describes how to make a
    payment.

    Attributes:
        payment_plan (google.cloud.channel_v1.types.PaymentPlan):
            Describes how a reseller will be billed.
        payment_type (google.cloud.channel_v1.types.PaymentType):
            Specifies when the payment needs to happen.
        payment_cycle (google.cloud.channel_v1.types.Period):
            Describes how frequently the reseller will be
            billed, such as once per month.
        trial_period (google.cloud.channel_v1.types.Period):
            Present for Offers with a trial period.
            For trial-only Offers, a paid service needs to
            start before the trial period ends for continued
            service.
            For Regular Offers with a trial period, the
            regular pricing goes into effect when trial
            period ends, or if paid service is started
            before the end of the trial period.
        billing_account (str):
            Reseller Billing account to charge after an
            offer transaction. Only present for Google Cloud
            offers.
    """

    payment_plan: "PaymentPlan" = proto.Field(
        proto.ENUM,
        number=1,
        enum="PaymentPlan",
    )
    payment_type: "PaymentType" = proto.Field(
        proto.ENUM,
        number=2,
        enum="PaymentType",
    )
    payment_cycle: "Period" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Period",
    )
    trial_period: "Period" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="Period",
    )
    billing_account: str = proto.Field(
        proto.STRING,
        number=5,
    )


class PriceByResource(proto.Message):
    r"""Represents price by resource type.

    Attributes:
        resource_type (google.cloud.channel_v1.types.ResourceType):
            Resource Type. Example: SEAT
        price (google.cloud.channel_v1.types.Price):
            Price of the Offer. Present if there are no
            price phases.
        price_phases (MutableSequence[google.cloud.channel_v1.types.PricePhase]):
            Specifies the price by time range.
    """

    resource_type: "ResourceType" = proto.Field(
        proto.ENUM,
        number=1,
        enum="ResourceType",
    )
    price: "Price" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Price",
    )
    price_phases: MutableSequence["PricePhase"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="PricePhase",
    )


class Price(proto.Message):
    r"""Represents the price of the Offer.

    Attributes:
        base_price (google.type.money_pb2.Money):
            Base price.
        discount (float):
            Discount percentage, represented as decimal.
            For example, a 20% discount will be represent as
            0.2.
        effective_price (google.type.money_pb2.Money):
            Effective Price after applying the discounts.
        price_period (google.cloud.channel_v1.types.Period):
            The time period with respect to which base
            and effective prices are defined.
            Example: 1 month, 6 months, 1 year, etc.
        external_price_uri (str):
            Link to external price list, such as link to
            Google Voice rate card.
        discount_components (MutableSequence[google.cloud.channel_v1.types.DiscountComponent]):
            Breakdown of the discount into its
            components. This will be empty if there is no
            discount present.
    """

    base_price: money_pb2.Money = proto.Field(
        proto.MESSAGE,
        number=1,
        message=money_pb2.Money,
    )
    discount: float = proto.Field(
        proto.DOUBLE,
        number=2,
    )
    effective_price: money_pb2.Money = proto.Field(
        proto.MESSAGE,
        number=3,
        message=money_pb2.Money,
    )
    price_period: "Period" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="Period",
    )
    external_price_uri: str = proto.Field(
        proto.STRING,
        number=4,
    )
    discount_components: MutableSequence["DiscountComponent"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="DiscountComponent",
    )


class PricePhase(proto.Message):
    r"""Specifies the price by the duration of months.
    For example, a 20% discount for the first six months, then a 10%
    discount starting on the seventh month.

    Attributes:
        period_type (google.cloud.channel_v1.types.PeriodType):
            Defines the phase period type.
        first_period (int):
            Defines first period for the phase.
        last_period (int):
            Defines first period for the phase.
        price (google.cloud.channel_v1.types.Price):
            Price of the phase. Present if there are no
            price tiers.
        price_tiers (MutableSequence[google.cloud.channel_v1.types.PriceTier]):
            Price by the resource tiers.
    """

    period_type: "PeriodType" = proto.Field(
        proto.ENUM,
        number=1,
        enum="PeriodType",
    )
    first_period: int = proto.Field(
        proto.INT32,
        number=2,
    )
    last_period: int = proto.Field(
        proto.INT32,
        number=3,
    )
    price: "Price" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="Price",
    )
    price_tiers: MutableSequence["PriceTier"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="PriceTier",
    )


class PriceTier(proto.Message):
    r"""Defines price at resource tier level. For example, an offer with
    following definition :

    - Tier 1: Provide 25% discount for all seats between 1 and 25.
    - Tier 2: Provide 10% discount for all seats between 26 and 100.
    - Tier 3: Provide flat 15% discount for all seats above 100.

    Each of these tiers is represented as a PriceTier.

    Attributes:
        first_resource (int):
            First resource for which the tier price
            applies.
        last_resource (int):
            Last resource for which the tier price
            applies.
        price (google.cloud.channel_v1.types.Price):
            Price of the tier.
    """

    first_resource: int = proto.Field(
        proto.INT32,
        number=1,
    )
    last_resource: int = proto.Field(
        proto.INT32,
        number=2,
    )
    price: "Price" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Price",
    )


class Period(proto.Message):
    r"""Represents period in days/months/years.

    Attributes:
        duration (int):
            Total duration of Period Type defined.
        period_type (google.cloud.channel_v1.types.PeriodType):
            Period Type.
    """

    duration: int = proto.Field(
        proto.INT32,
        number=1,
    )
    period_type: "PeriodType" = proto.Field(
        proto.ENUM,
        number=2,
        enum="PeriodType",
    )


class DiscountComponent(proto.Message):
    r"""Represents a single component of the total discount
    applicable on a Price.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        discount_percentage (float):
            Discount percentage, represented as decimal.
            For example, a 20% discount will be represented
            as 0.2.

            This field is a member of `oneof`_ ``discount_value``.
        discount_absolute (google.type.money_pb2.Money):
            Fixed value discount.

            This field is a member of `oneof`_ ``discount_value``.
        discount_type (google.cloud.channel_v1.types.DiscountType):
            Type of the discount.
    """

    discount_percentage: float = proto.Field(
        proto.DOUBLE,
        number=3,
        oneof="discount_value",
    )
    discount_absolute: money_pb2.Money = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="discount_value",
        message=money_pb2.Money,
    )
    discount_type: "DiscountType" = proto.Field(
        proto.ENUM,
        number=2,
        enum="DiscountType",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
