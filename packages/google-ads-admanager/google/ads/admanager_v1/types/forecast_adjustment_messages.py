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

from google.ads.admanager_v1.types import date_range as gaa_date_range
from google.ads.admanager_v1.types import forecast_adjustment_enums
from google.ads.admanager_v1.types import targeting as gaa_targeting

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "ForecastAdjustment",
        "HistoricalBasisVolumeSettings",
        "TotalVolumeSettings",
        "DailyVolumeSettings",
    },
)


class ForecastAdjustment(proto.Message):
    r"""Provides information about the expected volume and
    composition of traffic over a date range for a traffic forecast
    segment.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        daily_volume_settings (google.ads.admanager_v1.types.DailyVolumeSettings):
            Optional. The daily number of ad opportunities for each day
            in the adjustment date range. This field is required if
            volumeType is
            [ForecastAdjustmentVolumeType.DAILY_VOLUME][google.ads.admanager.v1.ForecastAdjustmentVolumeTypeEnum.ForecastAdjustmentVolumeType.DAILY_VOLUME]
            and ignored otherwise.

            This field is a member of `oneof`_ ``volume_settings``.
        total_volume_settings (google.ads.admanager_v1.types.TotalVolumeSettings):
            Optional. The total number of ad opportunities for the
            entire adjustment date range. This field is required if
            volumeType is
            [ForecastAdjustmentVolumeType.TOTAL_VOLUME][google.ads.admanager.v1.ForecastAdjustmentVolumeTypeEnum.ForecastAdjustmentVolumeType.TOTAL_VOLUME]
            and ignored otherwise.

            This field is a member of `oneof`_ ``volume_settings``.
        historical_basis_volume_settings (google.ads.admanager_v1.types.HistoricalBasisVolumeSettings):
            Optional. The daily number of ad opportunities for each day
            in the adjustment date range, determined by reference to the
            ad opportunity volume of a historical reference period. This
            field is required if volumeType is
            [ForecastAdjustmentVolumeType.HISTORICAL_BASIS_VOLUME][google.ads.admanager.v1.ForecastAdjustmentVolumeTypeEnum.ForecastAdjustmentVolumeType.HISTORICAL_BASIS_VOLUME]
            and ignored otherwise.

            This field is a member of `oneof`_ ``volume_settings``.
        name (str):
            Identifier. The resource name of the ``ForecastAdjustment``.
            Format:
            ``networks/{network_code}/forecastAdjustments/{forecastAdjustmentId}``
        traffic_forecast_segment (str):
            Required. Immutable. The resource name of the
            ``TrafficForecastSegment`` that this adjustment is
            associated with. Format:
            ``networks/{network_code}/trafficForecastSegments/{trafficForecastSegmentId}``

            This field is a member of `oneof`_ ``_traffic_forecast_segment``.
        display_name (str):
            Required. Display name of the
            ForecastAdjustment.

            This field is a member of `oneof`_ ``_display_name``.
        date_range (google.ads.admanager_v1.types.DateRange):
            Required. The date range of the adjustment.
        status (google.ads.admanager_v1.types.ForecastAdjustmentStatusEnum.ForecastAdjustmentStatus):
            Output only. The status of the adjustment.

            This field is a member of `oneof`_ ``_status``.
        volume_type (google.ads.admanager_v1.types.ForecastAdjustmentVolumeTypeEnum.ForecastAdjustmentVolumeType):
            Required. The volume type of the adjustment.

            This field is a member of `oneof`_ ``_volume_type``.
        allow_adjusting_forecast_above_recommended_limit (bool):
            Input only. Whether to allow provided volume
            settings to increase the current forecast by
            more than 300%. Due to system constraints,
            adjusting the forecast by more than 300% may
            have unintended consequences for other parts of
            the forecast. Note that this field will not
            persist on the adjustment itself, and will only
            affect the current request.

            This field is a member of `oneof`_ ``_allow_adjusting_forecast_above_recommended_limit``.
        calculated_daily_ad_opportunity_counts (MutableSequence[int]):
            Output only. The daily number of ad
            opportunities calculated to satisfy the provided
            volume settings. Each value in this list
            represents the calculated ad opportunities on
            the corresponding day of the adjustment date
            range. For example: for a dateRange of 2001-8-15
            to 2001-8-17, this field will contain one value
            for 2001-8-15, one value for 2001-8-16, and one
            value for 2001-8-17. This field is read-only and
            is populated by Google after forecast adjustment
            creation or update.
    """

    daily_volume_settings: "DailyVolumeSettings" = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="volume_settings",
        message="DailyVolumeSettings",
    )
    total_volume_settings: "TotalVolumeSettings" = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="volume_settings",
        message="TotalVolumeSettings",
    )
    historical_basis_volume_settings: "HistoricalBasisVolumeSettings" = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="volume_settings",
        message="HistoricalBasisVolumeSettings",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    traffic_forecast_segment: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    date_range: gaa_date_range.DateRange = proto.Field(
        proto.MESSAGE,
        number=5,
        message=gaa_date_range.DateRange,
    )
    status: forecast_adjustment_enums.ForecastAdjustmentStatusEnum.ForecastAdjustmentStatus = proto.Field(
        proto.ENUM,
        number=6,
        optional=True,
        enum=forecast_adjustment_enums.ForecastAdjustmentStatusEnum.ForecastAdjustmentStatus,
    )
    volume_type: forecast_adjustment_enums.ForecastAdjustmentVolumeTypeEnum.ForecastAdjustmentVolumeType = proto.Field(
        proto.ENUM,
        number=7,
        optional=True,
        enum=forecast_adjustment_enums.ForecastAdjustmentVolumeTypeEnum.ForecastAdjustmentVolumeType,
    )
    allow_adjusting_forecast_above_recommended_limit: bool = proto.Field(
        proto.BOOL,
        number=8,
        optional=True,
    )
    calculated_daily_ad_opportunity_counts: MutableSequence[int] = proto.RepeatedField(
        proto.INT64,
        number=12,
    )


class HistoricalBasisVolumeSettings(proto.Message):
    r"""Settings to specify the volume of ad opportunities per day
    over the ForecastAdjustment date range based on the traffic
    volume of a historical reference period. The daily historical
    traffic for the provided targeting and date range is fetched,
    multiplied by the provided multiplier, and used as the daily
    expected traffic for the adjustment. The number of days included
    in the historical date range does not need to be the same as the
    number of days included in the adjustment date range.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        use_parent_traffic_forecast_segment_targeting (bool):
            Whether the parent traffic forecast segment
            targeting's or the targeting's historical volume
            data should be used.

            This field is a member of `oneof`_ ``_use_parent_traffic_forecast_segment_targeting``.
        targeting (google.ads.admanager_v1.types.Targeting):
            Optional. The targeting criteria to use as
            the source of the historical volume data. This
            field is required if
            useParentTrafficForecastSegmentTargeting is
            false and ignored otherwise.
        historical_date_range (google.ads.admanager_v1.types.DateRange):
            Required. The date range to use for the
            historical ad opportunity volume.
        multiplier_milli_percent (int):
            Required. The multiplier to apply to the
            historical traffic volume, expressed in
            thousandths of a percent. For example, to set
            the forecasted traffic as 130% of the historical
            traffic, this value would be 130,000.

            This field is a member of `oneof`_ ``_multiplier_milli_percent``.
    """

    use_parent_traffic_forecast_segment_targeting: bool = proto.Field(
        proto.BOOL,
        number=1,
        optional=True,
    )
    targeting: gaa_targeting.Targeting = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gaa_targeting.Targeting,
    )
    historical_date_range: gaa_date_range.DateRange = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gaa_date_range.DateRange,
    )
    multiplier_milli_percent: int = proto.Field(
        proto.INT64,
        number=4,
        optional=True,
    )


class TotalVolumeSettings(proto.Message):
    r"""Settings to specify a single total traffic volume that will
    be used as the expected total future volume for a forecast
    adjustment. For example, an adOpportunityCount of 3,000
    indicates a forecast goal for the targeting specified on the
    parent traffic forecast segment of 3,000 ad opportunities over
    the entire duration of the adjustment.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        ad_opportunity_count (int):
            Required. The total ad opportunity count over
            the entire forecast adjustment date range.

            This field is a member of `oneof`_ ``_ad_opportunity_count``.
    """

    ad_opportunity_count: int = proto.Field(
        proto.INT64,
        number=1,
        optional=True,
    )


class DailyVolumeSettings(proto.Message):
    r"""Settings to specify daily ad opportunity counts that will be used as
    the expected future traffic volume for a forecast adjustment. For
    example: [10000, 20000, 5000] indicates expected traffic for the
    targeting specified on the parent traffic forecast segment of 10,000
    ad opportunities for the first day, 20,000 ad opportunities for the
    second, and 5,000 for the third.

    Attributes:
        ad_opportunity_counts (MutableSequence[int]):
            Required. The list of ad opportunity counts.
            Each value in this list represents the expected
            number of ad opportunities on the corresponding
            day of the adjustment date range. The number of
            values provided must match the number of days in
            the adjustment date range, inclusive. For
            example, an adjustment date range of June 5-June
            7 would need 3 values in this list, one for June
            5, one for June 6, and one for June 7.
    """

    ad_opportunity_counts: MutableSequence[int] = proto.RepeatedField(
        proto.INT64,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
