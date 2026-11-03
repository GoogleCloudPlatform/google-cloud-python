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

from google.ads.admanager_v1.types import date_range, forecast_messages
from google.ads.admanager_v1.types import targeting as gaa_targeting

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "RunAvailabilityForecastRequest",
        "RunAvailabilityForecastResponse",
        "RunDeliveryForecastRequest",
        "RunDeliveryForecastResponse",
        "RunTrafficDataRequest",
        "RunTrafficDataResponse",
    },
)


class RunAvailabilityForecastRequest(proto.Message):
    r"""Request object for [RunAvailabilityForecast][] method.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        existing_line_item (str):
            Optional. The resource name of the
            [LineItem][google.ads.admanager.v1.LineItem] to be
            forecasted. Format:
            ``networks/{network_code}/lineItems/{line_item_id}``

            This field is a member of `oneof`_ ``line_item_data``.
        parent (str):
            Required. Format: ``networks/{network_code}``
        availability_forecast_options (google.ads.admanager_v1.types.AvailabilityForecastOptions):
            Required. The availability forecast options.
    """

    existing_line_item: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="line_item_data",
    )
    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    availability_forecast_options: forecast_messages.AvailabilityForecastOptions = (
        proto.Field(
            proto.MESSAGE,
            number=2,
            message=forecast_messages.AvailabilityForecastOptions,
        )
    )


class RunAvailabilityForecastResponse(proto.Message):
    r"""Response object for [RunAvailabilityForecast][] method.

    Attributes:
        availability_forecast_result (google.ads.admanager_v1.types.AvailabilityForecast):
            The availability forecast.
    """

    availability_forecast_result: forecast_messages.AvailabilityForecast = proto.Field(
        proto.MESSAGE,
        number=1,
        message=forecast_messages.AvailabilityForecast,
    )


class RunDeliveryForecastRequest(proto.Message):
    r"""Request object for [RunDeliveryForecast][] method.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        existing_line_items (google.ads.admanager_v1.types.ExistingLineItemList):
            Optional. The resource names of the
            [LineItems][google.ads.admanager.v1.LineItem] to be
            forecasted.

            This field is a member of `oneof`_ ``line_item_data``.
        parent (str):
            Required. Format: ``networks/{network_code}``
        delivery_forecast_options (google.ads.admanager_v1.types.DeliveryForecastOptions):
            Required. The delivery forecast options.
    """

    existing_line_items: forecast_messages.ExistingLineItemList = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="line_item_data",
        message=forecast_messages.ExistingLineItemList,
    )
    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    delivery_forecast_options: forecast_messages.DeliveryForecastOptions = proto.Field(
        proto.MESSAGE,
        number=2,
        message=forecast_messages.DeliveryForecastOptions,
    )


class RunDeliveryForecastResponse(proto.Message):
    r"""Response object for [RunDeliveryForecast][] method.

    Attributes:
        delivery_forecast_result (google.ads.admanager_v1.types.DeliveryForecastResult):
            The delivery forecast result.
    """

    delivery_forecast_result: forecast_messages.DeliveryForecastResult = proto.Field(
        proto.MESSAGE,
        number=1,
        message=forecast_messages.DeliveryForecastResult,
    )


class RunTrafficDataRequest(proto.Message):
    r"""Request object for [RunTrafficData][] method.

    Attributes:
        parent (str):
            Required. Format: ``networks/{network_code}``
        targeting (google.ads.admanager_v1.types.Targeting):
            Required. The [Targeting][google.ads.admanager.v1.Targeting]
            resource that defines a segment of traffic.
        requested_date_range (google.ads.admanager_v1.types.DateRange):
            Required. The date range for which traffic
            data are requested. This range may cover
            historical dates, future dates, or both.

            The data returned are not guaranteed to cover
            the entire requested date range. If sufficient
            data are not available to cover the entire
            requested date range, a response may be returned
            with a later start date, earlier end date, or
            both.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    targeting: gaa_targeting.Targeting = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gaa_targeting.Targeting,
    )
    requested_date_range: date_range.DateRange = proto.Field(
        proto.MESSAGE,
        number=3,
        message=date_range.DateRange,
    )


class RunTrafficDataResponse(proto.Message):
    r"""Response object for [RunTrafficData][] method.

    Attributes:
        historical_time_series (google.ads.admanager_v1.types.TimeSeries):
            Time series of historical traffic ad
            opportunity counts.
            This may be null if the requested date range did
            not contain any historical dates, or if no
            historical data are available for the requested
            traffic segment.
        forecasted_time_series (google.ads.admanager_v1.types.TimeSeries):
            Time series of forecasted traffic ad
            opportunity counts.
            This may be null if the requested date range did
            not contain any future dates, or if no
            forecasted data are available for the requested
            traffic segment.
        forecasted_assigned_time_series (google.ads.admanager_v1.types.TimeSeries):
            Time series of future traffic volumes
            forecasted to be sold.
            This may be null if the requested date range did
            not contain any future dates, or if no
            sell-through data are available for the
            requested traffic segment.
        overall_date_range (google.ads.admanager_v1.types.DateRange):
            The overall date range spanned by the union
            of all time series in the response.

            This is a summary field for convenience. The
            value will be set such that the start date is
            equal to the earliest start date of all time
            series included, and the end date is equal to
            the latest end date of all time series included.

            If all time series fields are null, this field
            will also be null.
    """

    historical_time_series: forecast_messages.TimeSeries = proto.Field(
        proto.MESSAGE,
        number=1,
        message=forecast_messages.TimeSeries,
    )
    forecasted_time_series: forecast_messages.TimeSeries = proto.Field(
        proto.MESSAGE,
        number=2,
        message=forecast_messages.TimeSeries,
    )
    forecasted_assigned_time_series: forecast_messages.TimeSeries = proto.Field(
        proto.MESSAGE,
        number=3,
        message=forecast_messages.TimeSeries,
    )
    overall_date_range: date_range.DateRange = proto.Field(
        proto.MESSAGE,
        number=4,
        message=date_range.DateRange,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
