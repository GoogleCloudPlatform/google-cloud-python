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

from google.ads.admanager_v1.types import (
    creative_placeholder as gaa_creative_placeholder,
)
from google.ads.admanager_v1.types import date_range, forecasting_enums, goal_enums
from google.ads.admanager_v1.types import targeting as gaa_targeting

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "AvailabilityForecastOptions",
        "AvailabilityForecast",
        "DeliveryForecastOptions",
        "DeliveryForecastResult",
        "ForecastBreakdownOptions",
        "ForecastBreakdownTarget",
        "ForecastBreakdown",
        "ForecastBreakdownEntry",
        "DeliveryForecast",
        "TargetingCriteriaBreakdown",
        "ContendingLineItem",
        "AlternativeUnitTypeForecast",
        "GrpDemographicBreakdown",
        "LineItemDeliveryForecast",
        "TimeSeries",
        "ExistingLineItemList",
    },
)


class AvailabilityForecastOptions(proto.Message):
    r"""Forecasting options for ProspectiveLineItem availability
    forecasts.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        targeting_criteria_breakdown_included (bool):
            Optional. When specified, forecast result for the
            availability line item will also include breakdowns by its
            targeting in
            [AvailabilityForecast.targetingCriteriaBreakdowns][].

            This field is a member of `oneof`_ ``_targeting_criteria_breakdown_included``.
        contending_line_items_included (bool):
            Optional. When specified, the forecast result for the
            availability line item will also include contending line
            items in [AvailabilityForecast.contendingLineItems][].

            This field is a member of `oneof`_ ``_contending_line_items_included``.
        breakdown (google.ads.admanager_v1.types.ForecastBreakdownOptions):
            Optional. Configurations of forecast
            breakdowns.

            This field is a member of `oneof`_ ``_breakdown``.
    """

    targeting_criteria_breakdown_included: bool = proto.Field(
        proto.BOOL,
        number=1,
        optional=True,
    )
    contending_line_items_included: bool = proto.Field(
        proto.BOOL,
        number=2,
        optional=True,
    )
    breakdown: "ForecastBreakdownOptions" = proto.Field(
        proto.MESSAGE,
        number=3,
        optional=True,
        message="ForecastBreakdownOptions",
    )


class AvailabilityForecast(proto.Message):
    r"""Describes predicted inventory availability for a
    ProspectiveLineItem. Inventory has three threshold values along
    a line of possible inventory. From least to most, these are:

      Available units -- How many units can be booked without
    affecting any   other line items.
          Booking more than this number can cause lower and same
    priority line       items to underdeliver.
      Possible units -- How many units can be booked without
    affecting any   higher priority line
          items. Booking more than this number can cause the line
    item to       underdeliver.
      Matched (forecast) units -- How many units satisfy all
    specified   criteria.

    Underdelivery is caused by overbooking. However, if more
    impressions are served than are predicted, the extra available
    inventory might enable all inventory is able to be met without
    overbooking.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        line_item (str):
            Uniquely identifies this availability forecast. This value
            is read-only and is assigned by Google when the forecast is
            created. The attribute will be either the resource name of
            the [LineItem][google.ads.admanager.v1.LineItem] object it
            represents, or null if the forecast represents a prospective
            line item. Format:
            ``networks/{network_code}/lineItems/{line_item_id}``

            This field is a member of `oneof`_ ``_line_item``.
        order (str):
            The resource name for the
            [Order][google.ads.admanager.v1.Order] object that this line
            item belongs to, or null if the forecast represents a
            prospective line item without an
            [LineItem.order][google.ads.admanager.v1.LineItem.order]
            set. Format: ``networks/{network_code}/orders/{order_id}``

            This field is a member of `oneof`_ ``_order``.
        unit_type (google.ads.admanager_v1.types.UnitTypeEnum.UnitType):
            The unit with which the goal or cap of the LineItem is
            defined. Will be the same value as [Goal.unitType][] for
            both a set line item or a prospective one.

            This field is a member of `oneof`_ ``_unit_type``.
        available_units (int):
            The number of units, defined by [Goal.unitType][], that can
            be booked without affecting the delivery of any reserved
            line items. Exceeding this value won't cause an overbook,
            but lower priority line items may not run.

            This field is a member of `oneof`_ ``_available_units``.
        delivered_units (int):
            The number of units, defined by [Goal.unitType][], that have
            already been served if the reservation is already running.

            This field is a member of `oneof`_ ``_delivered_units``.
        matched_units (int):
            The number of units, defined by [Goal.unitType][], that
            match the specified targeting and delivery settings.

            This field is a member of `oneof`_ ``_matched_units``.
        possible_units (int):
            The maximum number of units, defined by [Goal.unitType][],
            that could be booked by taking inventory away from lower
            priority line items and some same priority line items.

            Booking this number may cause lower priority line items and
            some same priority line items to underdeliver.

            This field is a member of `oneof`_ ``_possible_units``.
        reserved_units (int):
            The number of reserved units, defined by [Goal.unitType][],
            requested. This can be an absolute or percentage value.

            This field is a member of `oneof`_ ``_reserved_units``.
        breakdowns (MutableSequence[google.ads.admanager_v1.types.ForecastBreakdown]):
            The breakdowns for each time window defined in
            [ForecastBreakdownOptions.timeWindows][].

            If no breakdown was requested through
            [AvailabilityForecastOptions.breakdown][google.ads.admanager.v1.AvailabilityForecastOptions.breakdown],
            this field will be empty.
        targeting_criteria_breakdowns (MutableSequence[google.ads.admanager_v1.types.TargetingCriteriaBreakdown]):
            The forecast result broken down by the
            targeting of the forecasted line item.
        contending_line_items (MutableSequence[google.ads.admanager_v1.types.ContendingLineItem]):
            List of ContendingLineItem contending line
            items for this forecast.
        alternative_unit_type_forecasts (MutableSequence[google.ads.admanager_v1.types.AlternativeUnitTypeForecast]):
            Views of this forecast, with alternative unit
            types.
        demographic_breakdowns (MutableSequence[google.ads.admanager_v1.types.GrpDemographicBreakdown]):
            The forecast result broken down by
            demographics.
    """

    line_item: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    order: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    unit_type: goal_enums.UnitTypeEnum.UnitType = proto.Field(
        proto.ENUM,
        number=3,
        optional=True,
        enum=goal_enums.UnitTypeEnum.UnitType,
    )
    available_units: int = proto.Field(
        proto.INT64,
        number=4,
        optional=True,
    )
    delivered_units: int = proto.Field(
        proto.INT64,
        number=5,
        optional=True,
    )
    matched_units: int = proto.Field(
        proto.INT64,
        number=6,
        optional=True,
    )
    possible_units: int = proto.Field(
        proto.INT64,
        number=7,
        optional=True,
    )
    reserved_units: int = proto.Field(
        proto.INT64,
        number=8,
        optional=True,
    )
    breakdowns: MutableSequence["ForecastBreakdown"] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message="ForecastBreakdown",
    )
    targeting_criteria_breakdowns: MutableSequence["TargetingCriteriaBreakdown"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=10,
            message="TargetingCriteriaBreakdown",
        )
    )
    contending_line_items: MutableSequence["ContendingLineItem"] = proto.RepeatedField(
        proto.MESSAGE,
        number=11,
        message="ContendingLineItem",
    )
    alternative_unit_type_forecasts: MutableSequence["AlternativeUnitTypeForecast"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=12,
            message="AlternativeUnitTypeForecast",
        )
    )
    demographic_breakdowns: MutableSequence["GrpDemographicBreakdown"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=14,
            message="GrpDemographicBreakdown",
        )
    )


class DeliveryForecastOptions(proto.Message):
    r"""Forecasting options for line item delivery forecasts.

    Attributes:
        ignored_line_items (MutableSequence[str]):
            Optional. The resource names of line items to be ignored
            while performing the delivery simulation. Format:
            ``networks/{network_code}/lineItems/{line_item_id}``
    """

    ignored_line_items: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class DeliveryForecastResult(proto.Message):
    r"""The forecast of delivery for a list of [ProposalLineItem][] or
    [LineItem][google.ads.admanager.v1.LineItem] objects to be reserved
    at the same time.

    Attributes:
        line_item_delivery_forecasts (MutableSequence[google.ads.admanager_v1.types.LineItemDeliveryForecast]):
            The delivery forecasts of the forecasted line
            items.
    """

    line_item_delivery_forecasts: MutableSequence["LineItemDeliveryForecast"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="LineItemDeliveryForecast",
        )
    )


class ForecastBreakdownOptions(proto.Message):
    r"""Configuration of forecast breakdown.

    Attributes:
        time_windows (MutableSequence[google.protobuf.timestamp_pb2.Timestamp]):
            Optional. The boundaries of time windows to configure time
            breakdown.

            By default, the time window of the forecasted
            [LineItem][google.ads.admanager.v1.LineItem] is assumed if
            none are explicitly specified in this field. But if set, at
            least two DateTimes are needed to define the boundaries of
            minimally one time window.

            Also, the time boundaries are required to be in the same
            time zone, in strictly ascending order.
        targets (MutableSequence[google.ads.admanager_v1.types.ForecastBreakdownTarget]):
            Optional. For each time window, these are the breakdown
            targets. If none specified, the targeting of the forecasted
            [LineItem][google.ads.admanager.v1.LineItem] is assumed.
    """

    time_windows: MutableSequence[timestamp_pb2.Timestamp] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    targets: MutableSequence["ForecastBreakdownTarget"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="ForecastBreakdownTarget",
    )


class ForecastBreakdownTarget(proto.Message):
    r"""Specifies inventory targeted by a breakdown entry.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        display_name (str):
            An optional name for this breakdown target, to be populated
            in the corresponding [ForecastBreakdownEntry.displayName][]
            field.

            This field is a member of `oneof`_ ``_display_name``.
        targeting (google.ads.admanager_v1.types.Targeting):
            If specified, the targeting for this breakdown. Format:
            ``networks/{network_code}/targetings/{targeting}``

            This field is a member of `oneof`_ ``_targeting``.
        creative_placeholder (google.ads.admanager_v1.types.CreativePlaceholder):
            If specified, restrict the breakdown to only
            inventory matching this creative.

            This field is a member of `oneof`_ ``_creative_placeholder``.
    """

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    targeting: gaa_targeting.Targeting = proto.Field(
        proto.MESSAGE,
        number=2,
        optional=True,
        message=gaa_targeting.Targeting,
    )
    creative_placeholder: gaa_creative_placeholder.CreativePlaceholder = proto.Field(
        proto.MESSAGE,
        number=3,
        optional=True,
        message=gaa_creative_placeholder.CreativePlaceholder,
    )


class ForecastBreakdown(proto.Message):
    r"""Represents the breakdown entries for a list of targetings and
    creatives.

    Attributes:
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            The starting time of the represented
            breakdown.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            The end time of the represented breakdown.
        named_entries (MutableSequence[google.ads.admanager_v1.types.ForecastBreakdownEntry]):
            The forecast breakdown entries in the same order as in the
            [ForecastBreakdownOptions.targets][google.ads.admanager.v1.ForecastBreakdownOptions.targets]
            field.
    """

    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    named_entries: MutableSequence["ForecastBreakdownEntry"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="ForecastBreakdownEntry",
    )


class ForecastBreakdownEntry(proto.Message):
    r"""A single forecast breakdown entry.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        display_name (str):
            The optional name of this entry, as specified in the
            corresponding [ForecastBreakdownTarget.displayName][] field.

            This field is a member of `oneof`_ ``_display_name``.
        forecast (google.ads.admanager_v1.types.DeliveryForecast):
            The forecast of this entry.
    """

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    forecast: "DeliveryForecast" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DeliveryForecast",
    )


class DeliveryForecast(proto.Message):
    r"""Represents a single delivery data point, with both available
    and forecast number.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        matched (int):
            The number of units matching the specified
            targeting and delivery settings.

            This field is a member of `oneof`_ ``_matched``.
        available (int):
            The number of units that can be booked without affecting the
            delivery of any reserved
            [LineItem][google.ads.admanager.v1.LineItem]s.

            This field is a member of `oneof`_ ``_available``.
        possible (int):
            The number of units that can be booked without affecting the
            delivery of any reserved
            [LineItem][google.ads.admanager.v1.LineItem] or lower
            priority [LineItem][google.ads.admanager.v1.LineItem].

            This field is a member of `oneof`_ ``_possible``.
    """

    matched: int = proto.Field(
        proto.INT64,
        number=1,
        optional=True,
    )
    available: int = proto.Field(
        proto.INT64,
        number=2,
        optional=True,
    )
    possible: int = proto.Field(
        proto.INT64,
        number=3,
        optional=True,
    )


class TargetingCriteriaBreakdown(proto.Message):
    r"""A single targeting criteria breakdown result.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        targeting_dimension (google.ads.admanager_v1.types.ForecastingTargetingDimensionEnum.ForecastingTargetingDimension):
            The dimension of this breakdown

            This field is a member of `oneof`_ ``_targeting_dimension``.
        targeting_criteria_id (int):
            The unique ID of the targeting criteria.

            This field is a member of `oneof`_ ``_targeting_criteria_id``.
        targeting_criteria (str):
            The name of the targeting criteria.

            This field is a member of `oneof`_ ``_targeting_criteria``.
        excluded (bool):
            When true, the breakdown is negative.

            This field is a member of `oneof`_ ``_excluded``.
        available_units (int):
            The available units for this breakdown.

            This field is a member of `oneof`_ ``_available_units``.
        matched_units (int):
            The matched units for this breakdown.

            This field is a member of `oneof`_ ``_matched_units``.
    """

    targeting_dimension: forecasting_enums.ForecastingTargetingDimensionEnum.ForecastingTargetingDimension = proto.Field(
        proto.ENUM,
        number=1,
        optional=True,
        enum=forecasting_enums.ForecastingTargetingDimensionEnum.ForecastingTargetingDimension,
    )
    targeting_criteria_id: int = proto.Field(
        proto.INT64,
        number=2,
        optional=True,
    )
    targeting_criteria: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    excluded: bool = proto.Field(
        proto.BOOL,
        number=4,
        optional=True,
    )
    available_units: int = proto.Field(
        proto.INT64,
        number=5,
        optional=True,
    )
    matched_units: int = proto.Field(
        proto.INT64,
        number=6,
        optional=True,
    )


class ContendingLineItem(proto.Message):
    r"""Describes contending line items for a forecast.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        line_item (str):
            The resource name of the contending line item. Format:
            ``networks/{network_code}/lineItems/{line_item_id}``

            This field is a member of `oneof`_ ``_line_item``.
        contending_units (int):
            The number of impressions contended for by
            both the forecasted line item and this line
            item.

            This field is a member of `oneof`_ ``_contending_units``.
    """

    line_item: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    contending_units: int = proto.Field(
        proto.INT64,
        number=2,
        optional=True,
    )


class AlternativeUnitTypeForecast(proto.Message):
    r"""Views of this forecast, with alternative unit types.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        unit_type (google.ads.admanager_v1.types.UnitTypeEnum.UnitType):
            The alternative unit type being presented.

            This field is a member of `oneof`_ ``_unit_type``.
        matched_units (int):
            The number of units matching the specified
            targeting and delivery settings.

            This field is a member of `oneof`_ ``_matched_units``.
        available_units (int):
            The number of units that can be booked
            without affecting the delivery of any reserved
            line items.

            This field is a member of `oneof`_ ``_available_units``.
        possible_units (int):
            The number of units that can be booked
            without affecting the delivery of any reserved
            line items or lower priority line items.

            This field is a member of `oneof`_ ``_possible_units``.
    """

    unit_type: goal_enums.UnitTypeEnum.UnitType = proto.Field(
        proto.ENUM,
        number=1,
        optional=True,
        enum=goal_enums.UnitTypeEnum.UnitType,
    )
    matched_units: int = proto.Field(
        proto.INT64,
        number=2,
        optional=True,
    )
    available_units: int = proto.Field(
        proto.INT64,
        number=3,
        optional=True,
    )
    possible_units: int = proto.Field(
        proto.INT64,
        number=4,
        optional=True,
    )


class GrpDemographicBreakdown(proto.Message):
    r"""GRP forecast breakdown counts associated with a gender and
    age demographic.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        available_units (int):
            The number of units matching the demographic
            breakdown that can be booked without affecting
            the delivery of any reserved line items.

            This field is a member of `oneof`_ ``_available_units``.
        matched_units (int):
            The number of units matching the demographic
            and matching specified targeting and delivery
            settings.

            This field is a member of `oneof`_ ``_matched_units``.
        unit_type (google.ads.admanager_v1.types.ForecastingGrpUnitEnum.ForecastingGrpUnit):
            The GrpUnitType associated with this
            demographic breakdown.

            This field is a member of `oneof`_ ``_unit_type``.
        gender (google.ads.admanager_v1.types.ForecastingGrpGenderEnum.ForecastingGrpGender):
            The GrpGender associated with this
            demographic breakdown.

            This field is a member of `oneof`_ ``_gender``.
        age (google.ads.admanager_v1.types.ForecastingGrpAgeEnum.ForecastingGrpAge):
            The GrpAge associated with this demographic
            breakdown.

            This field is a member of `oneof`_ ``_age``.
    """

    available_units: int = proto.Field(
        proto.INT64,
        number=1,
        optional=True,
    )
    matched_units: int = proto.Field(
        proto.INT64,
        number=2,
        optional=True,
    )
    unit_type: forecasting_enums.ForecastingGrpUnitEnum.ForecastingGrpUnit = (
        proto.Field(
            proto.ENUM,
            number=3,
            optional=True,
            enum=forecasting_enums.ForecastingGrpUnitEnum.ForecastingGrpUnit,
        )
    )
    gender: forecasting_enums.ForecastingGrpGenderEnum.ForecastingGrpGender = (
        proto.Field(
            proto.ENUM,
            number=4,
            optional=True,
            enum=forecasting_enums.ForecastingGrpGenderEnum.ForecastingGrpGender,
        )
    )
    age: forecasting_enums.ForecastingGrpAgeEnum.ForecastingGrpAge = proto.Field(
        proto.ENUM,
        number=5,
        optional=True,
        enum=forecasting_enums.ForecastingGrpAgeEnum.ForecastingGrpAge,
    )


class LineItemDeliveryForecast(proto.Message):
    r"""The forecasted delivery of a [ProposalLineItem][] or
    [LineItem][google.ads.admanager.v1.LineItem].


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        line_item (str):
            Uniquely identifies this line item delivery forecast. This
            value is read-only and will be either the resource name of
            the [LineItem][google.ads.admanager.v1.LineItem] resource it
            represents, or unset if the forecast represents a
            prospective line item. Format:
            ``networks/{network_code}/lineItems/{line_item_id}``

            This field is a member of `oneof`_ ``_line_item``.
        order (str):
            The resource name of the
            [Order][google.ads.admanager.v1.Order] object that this line
            item belongs to, or null if the forecast represents a
            prospective line item without an
            [LineItem.order][google.ads.admanager.v1.LineItem.order]
            set. Format: ``networks/{network_code}/orders/{order_id}``

            This field is a member of `oneof`_ ``_order``.
        unit_type (google.ads.admanager_v1.types.UnitTypeEnum.UnitType):
            The unit with which the goal or cap of the LineItem is
            defined. Will be the same value as [Goal.unitType][] for
            both a set line item or a prospective one.

            This field is a member of `oneof`_ ``_unit_type``.
        predicted_delivery_units (int):
            The number of units, defined by [Goal.unitType][], that will
            be delivered by the line item. Delivery of existing line
            items that are of same or lower priorities may be impacted.

            This field is a member of `oneof`_ ``_predicted_delivery_units``.
        delivered_units (int):
            The number of units, defined by [Goal.unitType][], that have
            already been served if the reservation is already running.

            This field is a member of `oneof`_ ``_delivered_units``.
        matched_units (int):
            The number of units, defined by [Goal.unitType][], that
            match the specified LineItem#targeting and delivery
            settings.

            This field is a member of `oneof`_ ``_matched_units``.
    """

    line_item: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    order: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    unit_type: goal_enums.UnitTypeEnum.UnitType = proto.Field(
        proto.ENUM,
        number=3,
        optional=True,
        enum=goal_enums.UnitTypeEnum.UnitType,
    )
    predicted_delivery_units: int = proto.Field(
        proto.INT64,
        number=4,
        optional=True,
    )
    delivered_units: int = proto.Field(
        proto.INT64,
        number=5,
        optional=True,
    )
    matched_units: int = proto.Field(
        proto.INT64,
        number=6,
        optional=True,
    )


class TimeSeries(proto.Message):
    r"""Represents a chronological sequence of daily values.

    Attributes:
        time_series_date_range (google.ads.admanager_v1.types.DateRange):
            The date range of the time series.
        values (MutableSequence[int]):
            The daily values constituting the time
            series.
            The number of time series values must equal the
            number of days spanned by the time series date
            range, inclusive. For example, a
            timeSeriesDateRange of 2001-08-15 to 2001-08-17
            contains one value for the 15th, one value for
            the 16th, and one value for the 17th.
    """

    time_series_date_range: date_range.DateRange = proto.Field(
        proto.MESSAGE,
        number=1,
        message=date_range.DateRange,
    )
    values: MutableSequence[int] = proto.RepeatedField(
        proto.INT64,
        number=2,
    )


class ExistingLineItemList(proto.Message):
    r"""[ExistingLineItemList][google.ads.admanager.v1.ExistingLineItemList]
    is a wrapper around a repeated field of string representing a
    [LineItem][google.ads.admanager.v1.LineItem] resource name.

    Attributes:
        line_items (MutableSequence[str]):
            Required. The list of
            [LineItem][google.ads.admanager.v1.LineItem] resource names
            to be forecasted. Format:
            ``networks/{network_code}/lineItems/{line_item_id}``
    """

    line_items: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
