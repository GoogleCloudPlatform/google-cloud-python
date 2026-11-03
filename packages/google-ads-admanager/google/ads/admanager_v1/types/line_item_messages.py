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
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.type.money_pb2 as money_pb2  # type: ignore
import proto  # type: ignore

from google.ads.admanager_v1.types import (
    applied_label,
    child_content_eligibility_enum,
    creative_placeholder,
    creative_targeting,
    custom_field_value,
    delivery_enums,
    environment_type_enum,
    exclusion_scope_enum,
    frequency_cap,
    line_item_allowed_format_enum,
    line_item_deal_info,
    line_item_delivery_forecast_source_enum,
    line_item_discount,
    line_item_enums,
    line_item_stats,
    skippable_ad_type_enum,
)
from google.ads.admanager_v1.types import custom_pacing_curve as gaa_custom_pacing_curve
from google.ads.admanager_v1.types import delivery_indicator as gaa_delivery_indicator
from google.ads.admanager_v1.types import goal as gaa_goal
from google.ads.admanager_v1.types import grp_settings as gaa_grp_settings
from google.ads.admanager_v1.types import targeting as gaa_targeting
from google.ads.admanager_v1.types import (
    third_party_measurement_settings as gaa_third_party_measurement_settings,
)

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "LineItem",
    },
)


class LineItem(proto.Message):
    r"""A LineItem contains information about how specific ad
    creatives are intended to serve to your website or app along
    with pricing and other delivery details.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the ``LineItem``. Format:
            ``networks/{network_code}/lineItems/{line_item_id}``
        order (str):
            Required. Immutable. The ID of the Order to which the
            LineItem belongs. Format:
            ``networks/{network_code}/orders/{order}``

            This field is a member of `oneof`_ ``_order``.
        display_name (str):
            Required. The name of the line item. This
            attribute has a maximum length of 255
            characters.

            This field is a member of `oneof`_ ``_display_name``.
        external_line_item_id (str):
            Optional. An identifier for the LineItem that
            is meaningful to the publisher. This attribute
            has a maximum length of 255 characters.

            This field is a member of `oneof`_ ``_external_line_item_id``.
        order_display_name (str):
            Output only. The name of the Order.

            This field is a member of `oneof`_ ``_order_display_name``.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Required. The date and time on which the
            LineItem is enabled to begin serving. This
            attribute is required and must be in the future.

            This field is a member of `oneof`_ ``_start_time``.
        target_end_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. The target end time of the line item. This
            attribute is required unless
            [end_time_unlimited][google.ads.admanager.v1.LineItem.end_time_unlimited]
            is set to true. If specified, it must be after the
            [start_time][google.ads.admanager.v1.LineItem.start_time].
            This does not include auto extension days.

            This field is a member of `oneof`_ ``_target_end_time``.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the LineItem
            will stop serving. This attribute includes auto
            extension days.

            This field is a member of `oneof`_ ``_end_time``.
        auto_extension_days (int):
            Optional. The number of days to allow a line item to deliver
            past its
            [target_end_time][google.ads.admanager.v1.LineItem.target_end_time].
            A maximum of 7 days is allowed. This is feature is only
            available for Ad Manager 360 accounts.

            This field is a member of `oneof`_ ``_auto_extension_days``.
        end_time_unlimited (bool):
            Optional. Non-empty default. Specifies whether or not the
            LineItem has an end time. This attribute defaults to false.
            It can be be set to true for only line items of type
            SPONSORSHIP, NETWORK, PRICE_PRIORITY and HOUSE.

            This field is a member of `oneof`_ ``_end_time_unlimited``.
        creative_rotation_type (google.ads.admanager_v1.types.CreativeRotationTypeEnum.CreativeRotationType):
            Required. The strategy used for displaying
            multiple Creative objects that are associated
            with the LineItem.

            This field is a member of `oneof`_ ``_creative_rotation_type``.
        delivery_rate_type (google.ads.admanager_v1.types.LineItemDeliveryRateTypeEnum.LineItemDeliveryRateType):
            Optional. Non-empty default. The strategy for
            delivering ads over the course of the line
            item's duration. This attribute defaults to
            EVENLY or FRONTLOADED depending on the network's
            configuration.

            This field is a member of `oneof`_ ``_delivery_rate_type``.
        delivery_forecast_source (google.ads.admanager_v1.types.LineItemDeliveryForecastSourceEnum.LineItemDeliveryForecastSource):
            Optional. Non-empty default. Strategy for
            choosing forecasted traffic shapes to pace line
            items. This field defaults to HISTORICAL.

            This field is a member of `oneof`_ ``_delivery_forecast_source``.
        custom_pacing_curve (google.ads.admanager_v1.types.CustomPacingCurve):
            Optional. The curve that is used to pace the line item's
            delivery. This field is required if and only if the delivery
            forecast source is CUSTOM_PACING_CURVE.

            This field is a member of `oneof`_ ``_custom_pacing_curve``.
        roadblocking_type (google.ads.admanager_v1.types.RoadblockingTypeEnum.RoadblockingType):
            Optional. Non-empty default. The strategy for serving
            roadblocked creatives, that is, instances where multiple
            creatives must be served together on a single web page. This
            attribute defaults to ONE_OR_MORE.

            This field is a member of `oneof`_ ``_roadblocking_type``.
        skippable_ad_type (google.ads.admanager_v1.types.SkippableAdTypeEnum.SkippableAdType):
            Optional. Non-empty default. The nature of the line item's
            creatives' skippability. This attribute is only applicable
            for video line items, and defaults to NOT_SKIPPABLE.

            This field is a member of `oneof`_ ``_skippable_ad_type``.
        frequency_caps (MutableSequence[google.ads.admanager_v1.types.FrequencyCap]):
            Optional. The set of frequency capping units
            for this LineItem.
        line_item_type (google.ads.admanager_v1.types.LineItemTypeEnum.LineItemType):
            Required. Indicates the line item type of a
            LineItem. The line item type determines the
            default priority of the line item. More
            information can be found at
            https://support.google.com/admanager/answer/177279.

            This field is a member of `oneof`_ ``_line_item_type``.
        priority (int):
            Optional. Non-empty default. The priority for the line item.
            Valid values range from 1 to 16. This field defaults to the
            default priority of the LineItemType. The following list
            shows the default, minimum, and maximum priority values are
            for each line item type:

            - LineItemType: default priority (minimum priority, maximum
              priority)
            - SPONSORSHIP: 4 (2, 5)
            - STANDARD: 8 (6, 10)
            - NETWORK: 12 (11, 14)
            - BULK: 12 (11, 14)
            - PRICE_PRIORITY: 12 (11, 14)
            - HOUSE: 16 (15, 16)
            - CLICK_TRACKING: 16 (1, 16)
            - AD_EXCHANGE: 12 (1, 16)
            - ADSENSE: 12 (1, 16)
            - BUMPER: 16 (15, 16)
            - ADMOB: 21 (1, 16)
            - PREFERRED_DEAL: 12 (12, 12) This field can only be edited
              by certain networks, otherwise a PermissionError will
              occur.

            This field is a member of `oneof`_ ``_priority``.
        rate (google.type.money_pb2.Money):
            Required. The amount of money to spend per
            impression or click.

            This field is a member of `oneof`_ ``_rate``.
        value_cpm (google.type.money_pb2.Money):
            Optional. Non-empty default. An amount to help the adserver
            rank inventory.
            [value_cpm][google.ads.admanager.v1.LineItem.value_cpm]
            artificially raises the value of inventory over the
            [rate][google.ads.admanager.v1.LineItem.rate] but avoids
            raising the actual
            [rate][google.ads.admanager.v1.LineItem.rate]. This
            attribute defaults to a Money object in the local currency
            with units and nanos set to 0.

            This field is a member of `oneof`_ ``_value_cpm``.
        cost_type (google.ads.admanager_v1.types.LineItemCostTypeEnum.LineItemCostType):
            Required. The method used for billing this
            LineItem.

            This field is a member of `oneof`_ ``_cost_type``.
        discount (google.ads.admanager_v1.types.LineItemDiscount):
            Optional. Discount information for the line
            item.

            This field is a member of `oneof`_ ``_discount``.
        contracted_units_bought (int):
            Optional. This attribute is only applicable
            for certain line item types and acts as an "FYI"
            or note, which does not impact adserving or
            other backend systems. For SPONSORSHIP line
            items, this represents the minimum quantity,
            which is a lifetime impression volume goal for
            reporting purposes only. For STANDARD line
            items, this represent the contracted quantity,
            which is the number of units specified in the
            contract the advertiser has bought for this
            LineItem. This field is just a "FYI" for
            traffickers to manually intervene with the
            LineItem when needed. This attribute is only
            available for STANDARD line items if you have
            this feature enabled on your network.

            This field is a member of `oneof`_ ``_contracted_units_bought``.
        creative_placeholders (MutableSequence[google.ads.admanager_v1.types.CreativePlaceholder]):
            Required. Details about the creatives that
            are expected to serve through this LineItem.
        environment_type (google.ads.admanager_v1.types.EnvironmentTypeEnum.EnvironmentType):
            Optional. Non-empty default. The environment that the
            LineItem is targeting. The default value is BROWSER. If this
            value is VIDEO_PLAYER, then this line item can only target
            AdUnits that have AdUnitSizes whose environmentType is also
            VIDEO_PLAYER.

            This field is a member of `oneof`_ ``_environment_type``.
        companion_delivery_option (google.ads.admanager_v1.types.CompanionDeliveryOptionEnum.CompanionDeliveryOption):
            Optional. The delivery option for companions. Setting this
            field is only meaningful if the following conditions are
            met:

            - The "Guaranteed roadblocks" feature is enabled on your
              network.
            - One of the following is true (both cannot be true, these
              are mutually exclusive).

              - The environmentType is VIDEO_PLAYER.
              - The roadblockingType is CREATIVE_SET. This field
                defaults to OPTIONAL if the conditions are met. In all
                other cases it defaults to UNKNOWN and is not
                meaningful.

            This field is a member of `oneof`_ ``_companion_delivery_option``.
        allow_overbook (bool):
            Input only. The flag indicates whether
            overbooking should be allowed when creating or
            updating reservations of line item types
            SPONSORSHIP and STANDARD. When true, operations
            on this line item will never trigger a
            ForecastError, which corresponds to an overbook
            warning in the UI. The default value is false.
            Note: this field won't persist on the line item
            itself, and the value will only affect the
            current request.

            This field is a member of `oneof`_ ``_allow_overbook``.
        skip_inventory_check (bool):
            Input only. The flag indicates whether the
            inventory check should be skipped when creating
            or updating a line item. The default value is
            false. Note: this field won't persist on the
            line item itself, and the value will only affect
            the current request.

            This field is a member of `oneof`_ ``_skip_inventory_check``.
        skip_cross_selling_rule_warning_checks (bool):
            Input only. True to skip checks for warnings
            from rules applied to line items targeting
            inventory shared by a distributor partner for
            cross selling when performing an action on this
            line item. The default is false. Note:

            this field won't persist on the line item
            itself, and the value will only affect the
            current request.

            This field is a member of `oneof`_ ``_skip_cross_selling_rule_warning_checks``.
        reserve_on_creation (bool):
            Input only. The flag indicates whether
            inventory should be reserved when creating a
            line item of types SPONSORSHIP and STANDARD in
            an unapproved Order. The default value is false.

            This field is a member of `oneof`_ ``_reserve_on_creation``.
        stats (google.ads.admanager_v1.types.LineItemStats):
            Output only. Contains trafficking statistics
            for the line item. This will be empty in case
            there are no statistics for a line item yet.

            This field is a member of `oneof`_ ``_stats``.
        delivery_indicator (google.ads.admanager_v1.types.DeliveryIndicator):
            Output only. Indicates how well the line item
            has been performing. This will be empty if the
            delivery indicator information is not available
            due to one of the following reasons:

              - The line item is not delivering.
              - The line item has an unlimited goal or cap.
              - The line item has a percentage based goal or
              cap.

            This field is a member of `oneof`_ ``_delivery_indicator``.
        budget (google.type.money_pb2.Money):
            Output only. The amount of money allocated to
            the LineItem. This attribute is readonly and is
            populated by Google. The currency code is
            readonly.

            This field is a member of `oneof`_ ``_budget``.
        status (google.ads.admanager_v1.types.LineItemComputedStatusEnum.LineItemComputedStatus):
            Output only. The status of the LineItem.

            This field is a member of `oneof`_ ``_status``.
        reservation_status (google.ads.admanager_v1.types.LineItemReservationStatusEnum.LineItemReservationStatus):
            Output only. Describes whether or not
            inventory has been reserved for the LineItem.

            This field is a member of `oneof`_ ``_reservation_status``.
        archived (bool):
            Output only. The archival status of the
            LineItem.

            This field is a member of `oneof`_ ``_archived``.
        web_property_code (str):
            Optional. The web property code used for dynamic allocation
            line items. This web property is only required with line
            item types AD_EXCHANGE and ADSENSE.

            This field is a member of `oneof`_ ``_web_property_code``.
        applied_labels (MutableSequence[google.ads.admanager_v1.types.AppliedLabel]):
            Optional. The set of labels applied directly
            to this line item.
        effective_applied_labels (MutableSequence[google.ads.admanager_v1.types.AppliedLabel]):
            Output only. Contains the set of labels
            inherited from the order that contains this line
            item and the advertiser that owns the order. If
            a label has been negated, only the negated label
            is returned.
        same_advertiser_exception_enabled (bool):
            Optional. If a line item has a series of
            competitive exclusions on it, it could be
            blocked from serving with line items from the
            same advertiser. Setting this to true will allow
            line items from the same advertiser to serve
            regardless of the other competitive exclusion
            labels being applied.

            This field is a member of `oneof`_ ``_same_advertiser_exception_enabled``.
        update_source (str):
            Output only. The application that last
            modified this line item.

            This field is a member of `oneof`_ ``_update_source``.
        notes (str):
            Optional. Provides any additional notes that
            may annotate the LineItem. This attribute has a
            maximum length of 65,535 characters.

            This field is a member of `oneof`_ ``_notes``.
        competitive_constraint_scope (google.ads.admanager_v1.types.ExclusionScopeEnum.ExclusionScope):
            Optional. Non-empty default. The
            CompetitiveConstraintScope for the competitive
            exclusion labels assigned to this line item.
            This field defaults to POD.

            This field is a member of `oneof`_ ``_competitive_constraint_scope``.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time this line item was last
            modified.

            This field is a member of `oneof`_ ``_update_time``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time this line item was
            created.

            This field is a member of `oneof`_ ``_create_time``.
        custom_field_values (MutableSequence[google.ads.admanager_v1.types.CustomFieldValue]):
            Optional. The values of the custom fields
            associated with this line item.
        missing_creatives (bool):
            Output only. Indicates if a LineItem is missing any Creative
            creatives for the creativePlaceholders specified. Creative
            Creatives can be considered missing for several reasons
            including:

            - Not enough Creative creatives of a certain size have been
              uploaded, as determined by
              [expected_creative_count][google.ads.admanager.v1.CreativePlaceholder.expected_creative_count].
              For example a LineItem specifies 750x350, 400x200 but only
              a 750x350 was uploaded. Or LineItem specifies 750x350 with
              an expected count of 2, but only one was uploaded.
            - The
              [Creative.applied_labels][google.ads.admanager.v1.Creative.applied_labels]
              of an associated Creative don't match the
              [CreativePlaceholder.applied_labels][google.ads.admanager.v1.CreativePlaceholder.applied_labels]
              of the LineItem. For example LineItem specifies 750x350
              with a Foo AppliedLabel but a 750x350 creative without a
              AppliedLabel was uploaded.

            This field is a member of `oneof`_ ``_missing_creatives``.
        third_party_measurement_settings (google.ads.admanager_v1.types.ThirdPartyMeasurementSettings):
            Optional. Third party auto-pixeling settings
            for cross-sell Partners.

            This field is a member of `oneof`_ ``_third_party_measurement_settings``.
        youtube_kids_restricted (bool):
            Optional. Designates this line item as
            intended for YT Kids app. If true, all creatives
            associated with this line item must be reviewed
            and approved. See the help center article for
            more information:

            https://support.google.com/yt-partner-sales/answer/10015534.

            This field is a member of `oneof`_ ``_youtube_kids_restricted``.
        max_video_creative_duration (google.protobuf.duration_pb2.Duration):
            Optional. The max duration of a video
            creative associated with this LineItem. This
            attribute is only meaningful for video line
            items. This attribute is required for video line
            items and must be greater than 0.

            This field is a member of `oneof`_ ``_max_video_creative_duration``.
        goal (google.ads.admanager_v1.types.Goal):
            Optional. The primary goal that this LineItem
            is associated with, which is used in its pacing
            and budgeting.

            This field is a member of `oneof`_ ``_goal``.
        secondary_goals (MutableSequence[google.ads.admanager_v1.types.Goal]):
            Optional. The secondary goals that this LineItem is
            associated with. This is required and meaningful only if the
            [line_item_type][google.ads.admanager.v1.LineItem.line_item_type]
            is SPONSORSHIP and
            [cost_type][google.ads.admanager.v1.LineItem.cost_type] is
            CPM.
        grp_settings (google.ads.admanager_v1.types.GrpSettings):
            Optional. Contains the information for a line
            item which has a target GRP demographic.

            This field is a member of `oneof`_ ``_grp_settings``.
        deal_info (google.ads.admanager_v1.types.LineItemDealInfo):
            Optional. The deal information associated
            with this line item, if it is programmatic.

            This field is a member of `oneof`_ ``_deal_info``.
        viewability_provider_companies (MutableSequence[str]):
            Optional. Optional IDs of the Company that
            provide ad verification for this line item.
        child_content_eligibility (google.ads.admanager_v1.types.ChildContentEligibilityEnum.ChildContentEligibility):
            Optional. Non-empty default. Child content
            eligibility designation for this line item. This
            field defaults to DISALLOWED.

            This field is a member of `oneof`_ ``_child_content_eligibility``.
        custom_vast_extension (str):
            Optional. Custom XML to be rendered in a
            custom VAST response at serving time.

            This field is a member of `oneof`_ ``_custom_vast_extension``.
        sponsorship_exclusivity_enabled (bool):
            Optional. Whether the line item is enabled
            for sponsorship exclusivity.  If true, only
            exclusive sponsorships can be served on
            inventory targeted by this LineItem. This
            control should only be available for 100% video
            sponsorships.

            This field is a member of `oneof`_ ``_sponsorship_exclusivity_enabled``.
        repeated_creative_serving_enabled (bool):
            Optional. Indicates whether repeated creative
            serving is enabled for this line item.

            This field is a member of `oneof`_ ``_repeated_creative_serving_enabled``.
        targeting (google.ads.admanager_v1.types.Targeting):
            Required. Contains the targeting criteria for
            the ad campaign.

            This field is a member of `oneof`_ ``_targeting``.
        creative_targetings (MutableSequence[google.ads.admanager_v1.types.CreativeTargeting]):
            Optional. A list of CreativeTargeting objects that can be
            used to specify creative level targeting for this line item.
            Creative level targeting is specified in a
            [CreativePlaceholder.creative_targeting_display_name][google.ads.admanager.v1.CreativePlaceholder.creative_targeting_display_name]
            field by referencing the [CreativeTargeting.display_name][]
            field. It also needs to be re-specified in the
            [LineItemCreativeAssociation.targeting_display_name][google.ads.admanager.v1.LineItemCreativeAssociation.targeting_display_name]
            field when associating a line item with a creative that fits
            into that placeholder.
        allowed_formats (MutableSequence[google.ads.admanager_v1.types.LineItemAllowedFormatEnum.LineItemAllowedFormat]):
            Optional. The set of allowed formats for this
            line item. If empty, all formats are allowed.
            This property only applies to programmatic video
            line items.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    order: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    external_line_item_id: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    order_display_name: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    target_end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=95,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    auto_extension_days: int = proto.Field(
        proto.INT32,
        number=8,
        optional=True,
    )
    end_time_unlimited: bool = proto.Field(
        proto.BOOL,
        number=9,
        optional=True,
    )
    creative_rotation_type: delivery_enums.CreativeRotationTypeEnum.CreativeRotationType = proto.Field(
        proto.ENUM,
        number=10,
        optional=True,
        enum=delivery_enums.CreativeRotationTypeEnum.CreativeRotationType,
    )
    delivery_rate_type: delivery_enums.LineItemDeliveryRateTypeEnum.LineItemDeliveryRateType = proto.Field(
        proto.ENUM,
        number=11,
        optional=True,
        enum=delivery_enums.LineItemDeliveryRateTypeEnum.LineItemDeliveryRateType,
    )
    delivery_forecast_source: line_item_delivery_forecast_source_enum.LineItemDeliveryForecastSourceEnum.LineItemDeliveryForecastSource = proto.Field(
        proto.ENUM,
        number=12,
        optional=True,
        enum=line_item_delivery_forecast_source_enum.LineItemDeliveryForecastSourceEnum.LineItemDeliveryForecastSource,
    )
    custom_pacing_curve: gaa_custom_pacing_curve.CustomPacingCurve = proto.Field(
        proto.MESSAGE,
        number=13,
        optional=True,
        message=gaa_custom_pacing_curve.CustomPacingCurve,
    )
    roadblocking_type: delivery_enums.RoadblockingTypeEnum.RoadblockingType = (
        proto.Field(
            proto.ENUM,
            number=14,
            optional=True,
            enum=delivery_enums.RoadblockingTypeEnum.RoadblockingType,
        )
    )
    skippable_ad_type: skippable_ad_type_enum.SkippableAdTypeEnum.SkippableAdType = (
        proto.Field(
            proto.ENUM,
            number=15,
            optional=True,
            enum=skippable_ad_type_enum.SkippableAdTypeEnum.SkippableAdType,
        )
    )
    frequency_caps: MutableSequence[frequency_cap.FrequencyCap] = proto.RepeatedField(
        proto.MESSAGE,
        number=16,
        message=frequency_cap.FrequencyCap,
    )
    line_item_type: line_item_enums.LineItemTypeEnum.LineItemType = proto.Field(
        proto.ENUM,
        number=17,
        optional=True,
        enum=line_item_enums.LineItemTypeEnum.LineItemType,
    )
    priority: int = proto.Field(
        proto.INT32,
        number=19,
        optional=True,
    )
    rate: money_pb2.Money = proto.Field(
        proto.MESSAGE,
        number=20,
        optional=True,
        message=money_pb2.Money,
    )
    value_cpm: money_pb2.Money = proto.Field(
        proto.MESSAGE,
        number=21,
        optional=True,
        message=money_pb2.Money,
    )
    cost_type: line_item_enums.LineItemCostTypeEnum.LineItemCostType = proto.Field(
        proto.ENUM,
        number=22,
        optional=True,
        enum=line_item_enums.LineItemCostTypeEnum.LineItemCostType,
    )
    discount: line_item_discount.LineItemDiscount = proto.Field(
        proto.MESSAGE,
        number=23,
        optional=True,
        message=line_item_discount.LineItemDiscount,
    )
    contracted_units_bought: int = proto.Field(
        proto.INT64,
        number=24,
        optional=True,
    )
    creative_placeholders: MutableSequence[creative_placeholder.CreativePlaceholder] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=25,
            message=creative_placeholder.CreativePlaceholder,
        )
    )
    environment_type: environment_type_enum.EnvironmentTypeEnum.EnvironmentType = (
        proto.Field(
            proto.ENUM,
            number=26,
            optional=True,
            enum=environment_type_enum.EnvironmentTypeEnum.EnvironmentType,
        )
    )
    companion_delivery_option: delivery_enums.CompanionDeliveryOptionEnum.CompanionDeliveryOption = proto.Field(
        proto.ENUM,
        number=27,
        optional=True,
        enum=delivery_enums.CompanionDeliveryOptionEnum.CompanionDeliveryOption,
    )
    allow_overbook: bool = proto.Field(
        proto.BOOL,
        number=28,
        optional=True,
    )
    skip_inventory_check: bool = proto.Field(
        proto.BOOL,
        number=29,
        optional=True,
    )
    skip_cross_selling_rule_warning_checks: bool = proto.Field(
        proto.BOOL,
        number=30,
        optional=True,
    )
    reserve_on_creation: bool = proto.Field(
        proto.BOOL,
        number=31,
        optional=True,
    )
    stats: line_item_stats.LineItemStats = proto.Field(
        proto.MESSAGE,
        number=32,
        optional=True,
        message=line_item_stats.LineItemStats,
    )
    delivery_indicator: gaa_delivery_indicator.DeliveryIndicator = proto.Field(
        proto.MESSAGE,
        number=33,
        optional=True,
        message=gaa_delivery_indicator.DeliveryIndicator,
    )
    budget: money_pb2.Money = proto.Field(
        proto.MESSAGE,
        number=35,
        optional=True,
        message=money_pb2.Money,
    )
    status: line_item_enums.LineItemComputedStatusEnum.LineItemComputedStatus = (
        proto.Field(
            proto.ENUM,
            number=36,
            optional=True,
            enum=line_item_enums.LineItemComputedStatusEnum.LineItemComputedStatus,
        )
    )
    reservation_status: line_item_enums.LineItemReservationStatusEnum.LineItemReservationStatus = proto.Field(
        proto.ENUM,
        number=38,
        optional=True,
        enum=line_item_enums.LineItemReservationStatusEnum.LineItemReservationStatus,
    )
    archived: bool = proto.Field(
        proto.BOOL,
        number=39,
        optional=True,
    )
    web_property_code: str = proto.Field(
        proto.STRING,
        number=49,
        optional=True,
    )
    applied_labels: MutableSequence[applied_label.AppliedLabel] = proto.RepeatedField(
        proto.MESSAGE,
        number=50,
        message=applied_label.AppliedLabel,
    )
    effective_applied_labels: MutableSequence[applied_label.AppliedLabel] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=51,
            message=applied_label.AppliedLabel,
        )
    )
    same_advertiser_exception_enabled: bool = proto.Field(
        proto.BOOL,
        number=52,
        optional=True,
    )
    update_source: str = proto.Field(
        proto.STRING,
        number=53,
        optional=True,
    )
    notes: str = proto.Field(
        proto.STRING,
        number=54,
        optional=True,
    )
    competitive_constraint_scope: exclusion_scope_enum.ExclusionScopeEnum.ExclusionScope = proto.Field(
        proto.ENUM,
        number=56,
        optional=True,
        enum=exclusion_scope_enum.ExclusionScopeEnum.ExclusionScope,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=57,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=58,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    custom_field_values: MutableSequence[custom_field_value.CustomFieldValue] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=59,
            message=custom_field_value.CustomFieldValue,
        )
    )
    missing_creatives: bool = proto.Field(
        proto.BOOL,
        number=61,
        optional=True,
    )
    third_party_measurement_settings: gaa_third_party_measurement_settings.ThirdPartyMeasurementSettings = proto.Field(
        proto.MESSAGE,
        number=67,
        optional=True,
        message=gaa_third_party_measurement_settings.ThirdPartyMeasurementSettings,
    )
    youtube_kids_restricted: bool = proto.Field(
        proto.BOOL,
        number=74,
        optional=True,
    )
    max_video_creative_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=75,
        optional=True,
        message=duration_pb2.Duration,
    )
    goal: gaa_goal.Goal = proto.Field(
        proto.MESSAGE,
        number=76,
        optional=True,
        message=gaa_goal.Goal,
    )
    secondary_goals: MutableSequence[gaa_goal.Goal] = proto.RepeatedField(
        proto.MESSAGE,
        number=100,
        message=gaa_goal.Goal,
    )
    grp_settings: gaa_grp_settings.GrpSettings = proto.Field(
        proto.MESSAGE,
        number=78,
        optional=True,
        message=gaa_grp_settings.GrpSettings,
    )
    deal_info: line_item_deal_info.LineItemDealInfo = proto.Field(
        proto.MESSAGE,
        number=79,
        optional=True,
        message=line_item_deal_info.LineItemDealInfo,
    )
    viewability_provider_companies: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=85,
    )
    child_content_eligibility: child_content_eligibility_enum.ChildContentEligibilityEnum.ChildContentEligibility = proto.Field(
        proto.ENUM,
        number=86,
        optional=True,
        enum=child_content_eligibility_enum.ChildContentEligibilityEnum.ChildContentEligibility,
    )
    custom_vast_extension: str = proto.Field(
        proto.STRING,
        number=88,
        optional=True,
    )
    sponsorship_exclusivity_enabled: bool = proto.Field(
        proto.BOOL,
        number=89,
        optional=True,
    )
    repeated_creative_serving_enabled: bool = proto.Field(
        proto.BOOL,
        number=90,
        optional=True,
    )
    targeting: gaa_targeting.Targeting = proto.Field(
        proto.MESSAGE,
        number=93,
        optional=True,
        message=gaa_targeting.Targeting,
    )
    creative_targetings: MutableSequence[creative_targeting.CreativeTargeting] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=94,
            message=creative_targeting.CreativeTargeting,
        )
    )
    allowed_formats: MutableSequence[
        line_item_allowed_format_enum.LineItemAllowedFormatEnum.LineItemAllowedFormat
    ] = proto.RepeatedField(
        proto.ENUM,
        number=112,
        enum=line_item_allowed_format_enum.LineItemAllowedFormatEnum.LineItemAllowedFormat,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
