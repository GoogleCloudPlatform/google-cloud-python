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
import google.type.date_pb2 as date_pb2  # type: ignore
import google.type.decimal_pb2 as decimal_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.channel.v1",
    manifest={
        "RebillingBasis",
        "CustomerRepricingConfig",
        "ChannelPartnerRepricingConfig",
        "RepricingConfig",
        "RepricingAdjustment",
        "PercentageAdjustment",
        "ConditionalOverride",
        "RepricingCondition",
        "SkuGroupCondition",
    },
)


class RebillingBasis(proto.Enum):
    r"""Specifies the different costs that the modified bill can be
    based on.

    Values:
        REBILLING_BASIS_UNSPECIFIED (0):
            Not used.
        COST_AT_LIST (1):
            Use the list cost, also known as the MSRP.
        DIRECT_CUSTOMER_COST (2):
            Pass through all discounts except the
            Reseller Program Discount. If this is the
            default cost base and no adjustments are
            specified, the output cost will be exactly what
            the customer would see if they viewed the bill
            in the Google Cloud Console.
    """

    REBILLING_BASIS_UNSPECIFIED = 0
    COST_AT_LIST = 1
    DIRECT_CUSTOMER_COST = 2


class CustomerRepricingConfig(proto.Message):
    r"""Configuration for how a reseller will reprice a Customer.

    Attributes:
        name (str):
            Output only. Resource name of the CustomerRepricingConfig.
            Format:
            accounts/{account_id}/customers/{customer_id}/customerRepricingConfigs/{id}.
        repricing_config (google.cloud.channel_v1.types.RepricingConfig):
            Required. The configuration for bill
            modifications made by a reseller before sending
            it to customers.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp of an update to the repricing rule.
            If ``update_time`` is after
            [RepricingConfig.effective_invoice_month][google.cloud.channel.v1.RepricingConfig.effective_invoice_month]
            then it indicates this was set mid-month.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    repricing_config: "RepricingConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="RepricingConfig",
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


class ChannelPartnerRepricingConfig(proto.Message):
    r"""Configuration for how a distributor will rebill a channel
    partner (also known as a distributor-authorized reseller).

    Attributes:
        name (str):
            Output only. Resource name of the
            ChannelPartnerRepricingConfig. Format:
            accounts/{account_id}/channelPartnerLinks/{channel_partner_id}/channelPartnerRepricingConfigs/{id}.
        repricing_config (google.cloud.channel_v1.types.RepricingConfig):
            Required. The configuration for bill
            modifications made by a reseller before sending
            it to ChannelPartner.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp of an update to the repricing rule.
            If ``update_time`` is after
            [RepricingConfig.effective_invoice_month][google.cloud.channel.v1.RepricingConfig.effective_invoice_month]
            then it indicates this was set mid-month.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    repricing_config: "RepricingConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="RepricingConfig",
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


class RepricingConfig(proto.Message):
    r"""Configuration for repricing a Google bill over a period of
    time.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        entitlement_granularity (google.cloud.channel_v1.types.RepricingConfig.EntitlementGranularity):
            Required. Applies the repricing configuration at the
            entitlement level.

            Note: If a
            [ChannelPartnerRepricingConfig][google.cloud.channel.v1.ChannelPartnerRepricingConfig]
            using
            [RepricingConfig.EntitlementGranularity][google.cloud.channel.v1.RepricingConfig.EntitlementGranularity]
            becomes effective, then no existing or future
            [RepricingConfig.ChannelPartnerGranularity][google.cloud.channel.v1.RepricingConfig.ChannelPartnerGranularity]
            will apply to the
            [RepricingConfig.EntitlementGranularity.entitlement][google.cloud.channel.v1.RepricingConfig.EntitlementGranularity.entitlement].
            This is the recommended value for both
            [CustomerRepricingConfig][google.cloud.channel.v1.CustomerRepricingConfig]
            and
            [ChannelPartnerRepricingConfig][google.cloud.channel.v1.ChannelPartnerRepricingConfig].

            This field is a member of `oneof`_ ``granularity``.
        channel_partner_granularity (google.cloud.channel_v1.types.RepricingConfig.ChannelPartnerGranularity):
            Applies the repricing configuration at the channel partner
            level. Only
            [ChannelPartnerRepricingConfig][google.cloud.channel.v1.ChannelPartnerRepricingConfig]
            supports this value. Deprecated: This is no longer
            supported. Use
            [RepricingConfig.entitlement_granularity][google.cloud.channel.v1.RepricingConfig.entitlement_granularity]
            instead.

            This field is a member of `oneof`_ ``granularity``.
        effective_invoice_month (google.type.date_pb2.Date):
            Required. The YearMonth when these
            adjustments activate. The Day field needs to be
            "0" since we only accept YearMonth repricing
            boundaries.
        adjustment (google.cloud.channel_v1.types.RepricingAdjustment):
            Required. Information about the adjustment.
        rebilling_basis (google.cloud.channel_v1.types.RebillingBasis):
            Required. The
            [RebillingBasis][google.cloud.channel.v1.RebillingBasis] to
            use for this bill. Specifies the relative cost based on
            repricing costs you will apply.
        conditional_overrides (MutableSequence[google.cloud.channel_v1.types.ConditionalOverride]):
            The conditional overrides to apply for this
            configuration. If you list multiple overrides,
            only the first valid override is used.  If you
            don't list any overrides, the API uses the
            normal adjustment and rebilling basis.
    """

    class EntitlementGranularity(proto.Message):
        r"""Applies the repricing configuration at the entitlement level.

        Attributes:
            entitlement (str):
                Resource name of the entitlement. Format:
                accounts/{account_id}/customers/{customer_id}/entitlements/{entitlement_id}
        """

        entitlement: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class ChannelPartnerGranularity(proto.Message):
        r"""Applies the repricing configuration at the channel partner level.
        The channel partner value is derived from the resource name. Takes
        an empty json object. Deprecated: This is no longer supported. Use
        [RepricingConfig.EntitlementGranularity][google.cloud.channel.v1.RepricingConfig.EntitlementGranularity]
        instead.

        """

    entitlement_granularity: EntitlementGranularity = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="granularity",
        message=EntitlementGranularity,
    )
    channel_partner_granularity: ChannelPartnerGranularity = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="granularity",
        message=ChannelPartnerGranularity,
    )
    effective_invoice_month: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=1,
        message=date_pb2.Date,
    )
    adjustment: "RepricingAdjustment" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="RepricingAdjustment",
    )
    rebilling_basis: "RebillingBasis" = proto.Field(
        proto.ENUM,
        number=3,
        enum="RebillingBasis",
    )
    conditional_overrides: MutableSequence["ConditionalOverride"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="ConditionalOverride",
    )


class RepricingAdjustment(proto.Message):
    r"""A type that represents the various adjustments you can apply
    to a bill.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        percentage_adjustment (google.cloud.channel_v1.types.PercentageAdjustment):
            Flat markup or markdown on an entire bill.

            This field is a member of `oneof`_ ``adjustment``.
    """

    percentage_adjustment: "PercentageAdjustment" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="adjustment",
        message="PercentageAdjustment",
    )


class PercentageAdjustment(proto.Message):
    r"""An adjustment that applies a flat markup or markdown to an
    entire bill.

    Attributes:
        percentage (google.type.decimal_pb2.Decimal):
            The percentage of the bill to adjust.
            For example:

            Mark down by 1% => "-1.00"
            Mark up by 1%   => "1.00"
            Pass-Through    => "0.00".
    """

    percentage: decimal_pb2.Decimal = proto.Field(
        proto.MESSAGE,
        number=2,
        message=decimal_pb2.Decimal,
    )


class ConditionalOverride(proto.Message):
    r"""Specifies the override to conditionally apply.

    Attributes:
        adjustment (google.cloud.channel_v1.types.RepricingAdjustment):
            Required. Information about the applied
            override's adjustment.
        rebilling_basis (google.cloud.channel_v1.types.RebillingBasis):
            Required. The
            [RebillingBasis][google.cloud.channel.v1.RebillingBasis] to
            use for the applied override. Shows the relative cost based
            on your repricing costs.
        repricing_condition (google.cloud.channel_v1.types.RepricingCondition):
            Required. Specifies the condition which, if
            met, will apply the override.
    """

    adjustment: "RepricingAdjustment" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="RepricingAdjustment",
    )
    rebilling_basis: "RebillingBasis" = proto.Field(
        proto.ENUM,
        number=2,
        enum="RebillingBasis",
    )
    repricing_condition: "RepricingCondition" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="RepricingCondition",
    )


class RepricingCondition(proto.Message):
    r"""Represents the various repricing conditions you can use for a
    conditional override.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        sku_group_condition (google.cloud.channel_v1.types.SkuGroupCondition):
            SKU Group condition for override.

            This field is a member of `oneof`_ ``condition``.
    """

    sku_group_condition: "SkuGroupCondition" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="condition",
        message="SkuGroupCondition",
    )


class SkuGroupCondition(proto.Message):
    r"""A condition that applies the override if a line item SKU is
    found in the SKU group.

    Attributes:
        sku_group (str):
            Specifies a SKU group
            (https://cloud.google.com/skus/sku-groups). Resource name of
            SKU group. Format: accounts/{account}/skuGroups/{sku_group}.
            Example:
            "accounts/C01234/skuGroups/3d50fd57-3157-4577-a5a9-a219b8490041".
    """

    sku_group: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
