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
import proto  # type: ignore

from google.cloud.capacityplanner_v1beta.types import allocation, future_reservation

__protobuf__ = proto.module(
    package="google.cloud.capacityplanner.v1beta",
    manifest={
        "QueryUsageHistoriesRequest",
        "QueryUsageHistoriesResponse",
        "QueryForecastsRequest",
        "QueryForecastsResponse",
        "QueryReservationsRequest",
        "QueryReservationsResponse",
        "Point",
        "Forecast",
        "UsageHistory",
        "TimeSeries",
        "ReservationData",
        "MachineShape",
        "ExportUsageHistoriesRequest",
        "ExportForecastsRequest",
        "ExportReservationsUsageRequest",
        "OutputConfig",
        "GcsDestination",
        "BigQueryDestination",
        "OperationMetadata",
        "ExportUsageHistoriesResponse",
        "ExportForecastsResponse",
        "ExportReservationsUsageResponse",
    },
)


class QueryUsageHistoriesRequest(proto.Message):
    r"""The ``QueryUsageHistories`` request. Next : 16

    Attributes:
        parent (str):
            Required. The compute engine resource and
            location for the time series values to return.
            The format is:

                projects/{project}/locations/{location} or
            organizations/{organization}/locations/{location}
            or     folders/{folder}/locations/{location}
        location_level (google.cloud.capacityplanner_v1beta.types.TimeSeries.LocationType):
            Optional. The location level of the
            reservations usage timeseries.
        is_spot (bool):
            Optional. The is_spot flag is used to fetch the usage data
            for preemptible Resources.
        machine_family (str):
            The machine family for the ``UsageHistory`` values to
            return. Possible values include "n1", and "n2d". See
            https://cloud.google.com/compute/docs/machine-types for more
            examples. Empty machine_family will return results matching
            all machine families.
        machine_shape (google.cloud.capacityplanner_v1beta.types.MachineShape):
            Optional. The machine shape for the ``UsageHistory`` values
            to return.
        disk_type (str):
            Optional. The disk_type for the ``UsageHistory`` values to
            return request with persistent-disk cloud_resource_type.
            Empty disk_type will return results matching all disk types.
        confidential_mode (bool):
            Optional. Whether the persistent disk is in
            confidential mode.
        gpu_type (str):
            Optional. The GPU type for the ``UsageHistory`` values to
            return. Sample values are "nvidia-tesla-t4", and
            "nvidia-tesla-a100". See
            https://cloud.google.com/compute/docs/gpus for a list. Empty
            gpu_type will return results matching all GPUs.
        tpu_type (str):
            Optional. The TPU type for the ``UsageHistory`` values to
            return. Empty tpu_type will return results matching all
            TPUs.
        cloud_resource_type (str):
            Required. The resource for the ``UsageHistory`` values to
            return. Possible values include "gce-vcpus", "gce-ram",
            "gce-local-ssd", "gce-persistent-disk", "gce-gpu" and
            "gce-tpu". Empty cloud_resource_type will return results
            matching all resources.
        usage_aggregation_method (google.cloud.capacityplanner_v1beta.types.UsageHistory.AggregationMethod):
            The method that should be used to convert sampled usage data
            to daily usage values. AGGREGATION_METHOD_UNSPECIFIED will
            return results matching all the aggregation methods.
        start_date (google.type.date_pb2.Date):
            Optional. The start date of reservations
            usage.
        end_date (google.type.date_pb2.Date):
            Optional. The end date of reservations usage.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    location_level: "TimeSeries.LocationType" = proto.Field(
        proto.ENUM,
        number=11,
        enum="TimeSeries.LocationType",
    )
    is_spot: bool = proto.Field(
        proto.BOOL,
        number=14,
    )
    machine_family: str = proto.Field(
        proto.STRING,
        number=2,
    )
    machine_shape: "MachineShape" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="MachineShape",
    )
    disk_type: str = proto.Field(
        proto.STRING,
        number=7,
    )
    confidential_mode: bool = proto.Field(
        proto.BOOL,
        number=15,
    )
    gpu_type: str = proto.Field(
        proto.STRING,
        number=8,
    )
    tpu_type: str = proto.Field(
        proto.STRING,
        number=12,
    )
    cloud_resource_type: str = proto.Field(
        proto.STRING,
        number=3,
    )
    usage_aggregation_method: "UsageHistory.AggregationMethod" = proto.Field(
        proto.ENUM,
        number=4,
        enum="UsageHistory.AggregationMethod",
    )
    start_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=9,
        message=date_pb2.Date,
    )
    end_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=10,
        message=date_pb2.Date,
    )


class QueryUsageHistoriesResponse(proto.Message):
    r"""The ``QueryUsageHistories`` response.

    Attributes:
        usage_histories (MutableSequence[google.cloud.capacityplanner_v1beta.types.UsageHistory]):
            The usage histories that match the request.
    """

    usage_histories: MutableSequence["UsageHistory"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="UsageHistory",
    )


class QueryForecastsRequest(proto.Message):
    r"""The ``QueryForecasts`` request. Next : 14

    Attributes:
        parent (str):
            Required. The compute engine resource and
            location for the time series values to return.
            The format is:

            projects/{project}/locations/{location} or
            organizations/{organization}/locations/{location}
            or folders/{folder}/locations/{location}
        machine_family (str):
            The machine family to use to select the ``Forecast`` values
            to return. Possible values include "n1", and "n2d". Empty
            machine_family will return results matching all machine
            families.
        machine_shape (google.cloud.capacityplanner_v1beta.types.MachineShape):
            Optional. The machine shape for the time
            series values to return.
        disk_type (str):
            Optional. The disk_type for the ``Forecast`` values to
            return with request persistent-disk cloud_resource_type.
            Empty disk_type will return results matching all disk types.
        confidential_mode (bool):
            Optional. Whether the persistent disk is in
            confidential mode.
        gpu_type (str):
            Optional. The GPU type for the ``Forecast`` values to
            return. Sample values are "nvidia-tesla-t4", and
            "nvidia-tesla-a100". See
            https://cloud.google.com/compute/docs/gpus for a list. Empty
            gpu_type will return results matching all GPUs.
        tpu_type (str):
            Optional. The TPU type for the ``Forecast`` values to
            return. Empty tpu_type will return results matching all
            TPUs.
        cloud_resource_type (str):
            Required. The resource for the ``Forecast`` values to
            return. Possible values include "gce-vcpus", "gce-ram",
            "gce-local-ssd", "gce-persistent-disk", "gce-gpu" and
            "gce-tpu". Empty cloud_resource_type will return results
            matching all resources.
        forecast_type (google.cloud.capacityplanner_v1beta.types.Forecast.ForecastType):
            The type of forecast to use to select the ``Forecast``
            values to return. FORECAST_TYPE_UNSPECIFIED will return
            results matching all the forecast types.
        prediction_interval (google.cloud.capacityplanner_v1beta.types.Forecast.PredictionInterval):
            The prediction interval to use to select the ``Forecast``
            values to return. PREDICTION_INTERVAL_UNSPECIFIED will
            return results matching all prediction intervals.
        aggregation_method (google.cloud.capacityplanner_v1beta.types.UsageHistory.AggregationMethod):
            Aggregation Method of the historical usage
            for which the forecast is generated
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    machine_family: str = proto.Field(
        proto.STRING,
        number=2,
    )
    machine_shape: "MachineShape" = proto.Field(
        proto.MESSAGE,
        number=12,
        message="MachineShape",
    )
    disk_type: str = proto.Field(
        proto.STRING,
        number=9,
    )
    confidential_mode: bool = proto.Field(
        proto.BOOL,
        number=13,
    )
    gpu_type: str = proto.Field(
        proto.STRING,
        number=10,
    )
    tpu_type: str = proto.Field(
        proto.STRING,
        number=11,
    )
    cloud_resource_type: str = proto.Field(
        proto.STRING,
        number=3,
    )
    forecast_type: "Forecast.ForecastType" = proto.Field(
        proto.ENUM,
        number=4,
        enum="Forecast.ForecastType",
    )
    prediction_interval: "Forecast.PredictionInterval" = proto.Field(
        proto.ENUM,
        number=5,
        enum="Forecast.PredictionInterval",
    )
    aggregation_method: "UsageHistory.AggregationMethod" = proto.Field(
        proto.ENUM,
        number=8,
        enum="UsageHistory.AggregationMethod",
    )


class QueryForecastsResponse(proto.Message):
    r"""The ``QueryForecasts`` response.

    Attributes:
        forecasts (MutableSequence[google.cloud.capacityplanner_v1beta.types.Forecast]):
            The forecasts that match the request.
    """

    forecasts: MutableSequence["Forecast"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Forecast",
    )


class QueryReservationsRequest(proto.Message):
    r"""The ``QueryReservations`` request.

    Attributes:
        parent (str):
            Required. The compute engine resource and
            location for the time series values to return.
            The format is:

            projects/{project}/locations/{location} or
            organizations/{organization}/locations/{location}
            or folders/{folder}/locations/{location}
        location_level (google.cloud.capacityplanner_v1beta.types.TimeSeries.LocationType):
            Optional. The location level of the
            reservations usage timeseries.
        machine_family (str):
            Optional. The machine family to use to select the aggregate
            reserved values to return. Possible values include "n1", and
            "n2d" etc. Empty machine_family will return results matching
            all machine families.
        machine_shape (google.cloud.capacityplanner_v1beta.types.MachineShape):
            Optional. The machine_shape as a filter to select matching
            reservations.
        gpu_type (str):
            Optional. The GPU type for the reserved values to return.
            Sample values are "nvidia-tesla-t4", and
            "nvidia-tesla-a100". See
            https://cloud.google.com/compute/docs/gpus for a list. Empty
            gpu_type will return results matching all GPUs.
        cloud_resource_type (str):
            Required. The resource for the reserved
            values to return. Possible values include
            "gce-vcpus", "gce-ram", "gce-local-ssd",
            "gce-gpu" and "gce-vm".
        reservation_type (google.cloud.capacityplanner_v1beta.types.QueryReservationsRequest.ReservationType):
            Required. The Reservation type for example,
            future reservation request and allocation. If
            unspecified, all types are included.
        share_type (google.cloud.capacityplanner_v1beta.types.QueryReservationsRequest.ShareType):
            Optional. Types of share settings to filter
            reservations in response. If unspecified, all
            types are included.
        ownership_type (google.cloud.capacityplanner_v1beta.types.QueryReservationsRequest.OwnershipType):
            Optional. Types of ownerships to filter
            reservations based on. In case of OWNED, it
            filters reservations which are owned by selected
            parent project/folder/organization. If
            unspecified, all types are included.
        reservation_data_level (google.cloud.capacityplanner_v1beta.types.QueryReservationsRequest.ReservationDataLevel):
            Required. Reservations output data format.
        include_unapproved_reservations (bool):
            Optional. Whether to include pending for
            approval reservations in the response. This
            field is only applicable for future
            reservations.
        aggregation_method (google.cloud.capacityplanner_v1beta.types.UsageHistory.AggregationMethod):
            Optional. Aggregation Method of the
            historical reservation usage
        start_date (google.type.date_pb2.Date):
            Optional. The start date of reservations
            usage.
        end_date (google.type.date_pb2.Date):
            Optional. The end date of reservations usage.
    """

    class ReservationType(proto.Enum):
        r"""Type of the reservation

        Values:
            RESERVATION_TYPE_UNSPECIFIED (0):
                No reservation type specified.
            RESERVATION_TYPE_ALLOCATION (1):
                Allocation refers to realized reservation
                either auto created or created by the users on
                demand.
            RESERVATION_TYPE_FUTURE_RESERVATION (2):
                Future Reservation requests created by users.
            RESERVATION_TYPE_ALL (3):
                All reservations.
        """

        RESERVATION_TYPE_UNSPECIFIED = 0
        RESERVATION_TYPE_ALLOCATION = 1
        RESERVATION_TYPE_FUTURE_RESERVATION = 2
        RESERVATION_TYPE_ALL = 3

    class ShareType(proto.Enum):
        r"""Possible scope in which the reservation can be shared.

        Values:
            SHARE_TYPE_UNSPECIFIED (0):
                No share type specified.
            SHARE_TYPE_LOCAL (1):
                Default value, for which reservation is open
                to only owner project.
            SHARE_TYPE_SPECIFIC_PROJECTS (2):
                Shared-reservation is open to specific
                projects.
        """

        SHARE_TYPE_UNSPECIFIED = 0
        SHARE_TYPE_LOCAL = 1
        SHARE_TYPE_SPECIFIC_PROJECTS = 2

    class OwnershipType(proto.Enum):
        r"""Reservation ownership status to provide distinction for
        Capacity Planning.

        Values:
            OWNERSHIP_TYPE_UNSPECIFIED (0):
                No ownership status specified.
            OWNERSHIP_TYPE_OWNED (1):
                For the reservations owned within selected
                Google Cloud Platform Resource Container
                (project/folder/organization).
            OWNERSHIP_TYPE_SHARED_BY_OTHERS (2):
                For the reservations consumable within
                selected Google Cloud Platform Resource
                Container (project/folder/organization), but not
                owned by them.
        """

        OWNERSHIP_TYPE_UNSPECIFIED = 0
        OWNERSHIP_TYPE_OWNED = 1
        OWNERSHIP_TYPE_SHARED_BY_OTHERS = 2

    class ReservationDataLevel(proto.Enum):
        r"""The form in which data of reservations should be returned.
        In case of AGGREGATED, timeseries for selected reservations is
        returned. If unspecified, all levels are included.

        Values:
            RESERVATION_DATA_LEVEL_UNSPECIFIED (0):
                No reservation data level specified.
            RESERVATION_DATA_LEVEL_AGGREGATED (1):
                aggregated reservations data in a timeseries
                or aggregation over timeseries.
            RESERVATION_DATA_LEVEL_PER_RESERVATION (2):
                per reservation detail which is equivalent of
                Arcus Future Reservation or Allocation with only
                limited fields which are useful for Capacity
                Planning.
        """

        RESERVATION_DATA_LEVEL_UNSPECIFIED = 0
        RESERVATION_DATA_LEVEL_AGGREGATED = 1
        RESERVATION_DATA_LEVEL_PER_RESERVATION = 2

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    location_level: "TimeSeries.LocationType" = proto.Field(
        proto.ENUM,
        number=16,
        enum="TimeSeries.LocationType",
    )
    machine_family: str = proto.Field(
        proto.STRING,
        number=2,
    )
    machine_shape: "MachineShape" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="MachineShape",
    )
    gpu_type: str = proto.Field(
        proto.STRING,
        number=3,
    )
    cloud_resource_type: str = proto.Field(
        proto.STRING,
        number=4,
    )
    reservation_type: ReservationType = proto.Field(
        proto.ENUM,
        number=5,
        enum=ReservationType,
    )
    share_type: ShareType = proto.Field(
        proto.ENUM,
        number=6,
        enum=ShareType,
    )
    ownership_type: OwnershipType = proto.Field(
        proto.ENUM,
        number=7,
        enum=OwnershipType,
    )
    reservation_data_level: ReservationDataLevel = proto.Field(
        proto.ENUM,
        number=8,
        enum=ReservationDataLevel,
    )
    include_unapproved_reservations: bool = proto.Field(
        proto.BOOL,
        number=12,
    )
    aggregation_method: "UsageHistory.AggregationMethod" = proto.Field(
        proto.ENUM,
        number=13,
        enum="UsageHistory.AggregationMethod",
    )
    start_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=14,
        message=date_pb2.Date,
    )
    end_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=15,
        message=date_pb2.Date,
    )


class QueryReservationsResponse(proto.Message):
    r"""The ``QueryReservations`` response.

    Attributes:
        reservations (MutableSequence[google.cloud.capacityplanner_v1beta.types.ReservationData]):
            The reservations data that match the request.
    """

    reservations: MutableSequence["ReservationData"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ReservationData",
    )


class Point(proto.Message):
    r"""A single data point in a time series.

    Attributes:
        event_time (google.protobuf.timestamp_pb2.Timestamp):
            The time which the data point applies.
        value (float):
            The value of the data point.
    """

    event_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    value: float = proto.Field(
        proto.DOUBLE,
        number=2,
    )


class Forecast(proto.Message):
    r"""A collection of data points that describes the predicted
    time-varying values of a resource.

    Attributes:
        name (str):
            The resource name of the connection in the form of:
            ``projects/{project_id}/locations/{location_id}/forecasts/{forecast_id}``
            or
            ``organizations/{organization_id}/locations/{location_id}/forecasts/{forecast_id}``
            or
            ``folders/{folder_id}/locations/{location_id}/forecasts/{forecast_id}``
        time_series (google.cloud.capacityplanner_v1beta.types.TimeSeries):
            The collection of data points that represent
            the predicted values. Note that some of these
            values may be in the past (if, for example, the
            forecast was created in the past and predicted
            values for the present day).
        forecast_type (google.cloud.capacityplanner_v1beta.types.Forecast.ForecastType):
            The type of forecast.
        bounds (google.cloud.capacityplanner_v1beta.types.Forecast.Bounds):
            The bounds represented by this forecast time
            series.
        prediction_interval (google.cloud.capacityplanner_v1beta.types.Forecast.PredictionInterval):
            The prediction interval represented by the
            time series.
        aggregation_method (google.cloud.capacityplanner_v1beta.types.UsageHistory.AggregationMethod):
            Aggregation Method of the historical usage
            for which the forecast is generated
    """

    class ForecastType(proto.Enum):
        r"""The type of the forecast. This describes the method that was
        used to produce future time series values from historical time
        series values.

        Values:
            FORECAST_TYPE_UNSPECIFIED (0):
                No forecast type is specified.
            STATISTICAL (1):
                Statistical forecast.
            STATISTICAL_WITH_BFCM (2):
                Statistical forecast that attempts to predict
                the seasonal affects of Black Friday and Cyber
                Monday.
            YEARLY_SEASONALITY (3):
                Yearly Seasonality model provides generic
                seasonality beyond BFCM.
        """

        FORECAST_TYPE_UNSPECIFIED = 0
        STATISTICAL = 1
        STATISTICAL_WITH_BFCM = 2
        YEARLY_SEASONALITY = 3

    class Bounds(proto.Enum):
        r"""The bounds of the forecast time series.

        Values:
            BOUNDS_UNSPECIFIED (0):
                No bounds is specified.
            LOWER_BOUND (1):
                The time series represents the upper bound of
                the forecast.
            MEDIAN (2):
                The time series represents the median
                expected forecast value.
            UPPER_BOUND (3):
                The time series represents the lower bound of
                the forecast.
        """

        BOUNDS_UNSPECIFIED = 0
        LOWER_BOUND = 1
        MEDIAN = 2
        UPPER_BOUND = 3

    class PredictionInterval(proto.Enum):
        r"""The prediction interval represented by a forecast.

        Values:
            PREDICTION_INTERVAL_UNSPECIFIED (0):
                No prediction interval is specified.
            PREDICTION_INTERVAL_90 (1):
                This represents a prediction interval that has 90%
                confidence. For example, for a symmetric prediction
                interval, a ``PredictionInterval`` of
                ``PREDICTION_INTERVAL_90`` means that the ``UPPER_BOUND``
                will represent the 95th precentile.
            PREDICTION_INTERVAL_50 (2):
                This represents a prediction interval that has 50%
                confidence. For example, for a symmetric prediction
                interval, a ``PredictionInterval`` of
                ``PREDICTION_INTERVAL_50`` means that the ``UPPER_BOUND``
                will represent the 75th precentile.
        """

        PREDICTION_INTERVAL_UNSPECIFIED = 0
        PREDICTION_INTERVAL_90 = 1
        PREDICTION_INTERVAL_50 = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    time_series: "TimeSeries" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="TimeSeries",
    )
    forecast_type: ForecastType = proto.Field(
        proto.ENUM,
        number=3,
        enum=ForecastType,
    )
    bounds: Bounds = proto.Field(
        proto.ENUM,
        number=4,
        enum=Bounds,
    )
    prediction_interval: PredictionInterval = proto.Field(
        proto.ENUM,
        number=5,
        enum=PredictionInterval,
    )
    aggregation_method: "UsageHistory.AggregationMethod" = proto.Field(
        proto.ENUM,
        number=6,
        enum="UsageHistory.AggregationMethod",
    )


class UsageHistory(proto.Message):
    r"""A collection of data points that describes the historical
    time-varying values of a resource.

    Attributes:
        time_series (google.cloud.capacityplanner_v1beta.types.TimeSeries):
            The collection of data points that represent
            the historical values.
        aggregation_method (google.cloud.capacityplanner_v1beta.types.UsageHistory.AggregationMethod):
            Method used to convert sampled usage data to
            time series values.
    """

    class AggregationMethod(proto.Enum):
        r"""Methods for converting sampled data to time series values.

        Values:
            AGGREGATION_METHOD_UNSPECIFIED (0):
                No aggregation method is specified.
            MEDIAN (1):
                No description available.
            PEAK (2):
                Time series values represent the 99th
                percentile of the sampled values.
            P50 (3):
                Time series values represent the 50th(median)
                percentile of the sampled values.
            P75 (4):
                Time series values represent the 75th
                percentile of the sampled values.
            P99 (5):
                Time series values represent the 99th
                percentile of the sampled values.
        """

        AGGREGATION_METHOD_UNSPECIFIED = 0
        MEDIAN = 1
        PEAK = 2
        P50 = 3
        P75 = 4
        P99 = 5

    time_series: "TimeSeries" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="TimeSeries",
    )
    aggregation_method: AggregationMethod = proto.Field(
        proto.ENUM,
        number=2,
        enum=AggregationMethod,
    )


class TimeSeries(proto.Message):
    r"""A collection of data points that describes the time-varying
    values of a resource. A time series is identified by its ID.
    Next : 13

    Attributes:
        location_type (google.cloud.capacityplanner_v1beta.types.TimeSeries.LocationType):
            Required. The type of location that the time
            series is summarizing.
        location (str):
            Optional. The location of the usage data in
            time series.
        is_spot (bool):
            Optional. The location of the usage data in
            time series.
        machine_family (str):
            The machine family for the time series values
            to return. Possible values include "n1" and
            "n2d".
        disk_type (str):
            The disk type for the time series values to
            return.
        confidential_mode (bool):
            Optional. The confidential mode for disk.
        gpu_type (str):
            The GPU type of the time series.
        tpu_type (str):
            The TPU type of the time series.
        machine_shape (google.cloud.capacityplanner_v1beta.types.MachineShape):
            The machine shape of the time series.
        cloud_resource_type (str):
            The resource for the time series values to
            return. Possible values include "gce-vcpus",
            "gce-ram", "gce-local-ssd",
            "gce-persistent-disk", "gce-gpu", "gce-tpu" and
            "gce-vm".
        points (MutableSequence[google.cloud.capacityplanner_v1beta.types.Point]):
            The data points of this time series. When
            listing time series, points are returned in
            chronological order.
        unit (str):
            The units in which the values are reported.
    """

    class LocationType(proto.Enum):
        r"""The type of location that the time series is summarizing.

        Values:
            LOCATION_TYPE_UNSPECIFIED (0):
                No location type was specified.
            REGIONAL (1):
                Time series values represent usage aggregated
                at the region level.
            ZONAL (2):
                Time series values represent usage aggregated
                at the zone level.
        """

        LOCATION_TYPE_UNSPECIFIED = 0
        REGIONAL = 1
        ZONAL = 2

    location_type: LocationType = proto.Field(
        proto.ENUM,
        number=1,
        enum=LocationType,
    )
    location: str = proto.Field(
        proto.STRING,
        number=9,
    )
    is_spot: bool = proto.Field(
        proto.BOOL,
        number=11,
    )
    machine_family: str = proto.Field(
        proto.STRING,
        number=2,
    )
    disk_type: str = proto.Field(
        proto.STRING,
        number=6,
    )
    confidential_mode: bool = proto.Field(
        proto.BOOL,
        number=12,
    )
    gpu_type: str = proto.Field(
        proto.STRING,
        number=7,
    )
    tpu_type: str = proto.Field(
        proto.STRING,
        number=10,
    )
    machine_shape: "MachineShape" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="MachineShape",
    )
    cloud_resource_type: str = proto.Field(
        proto.STRING,
        number=3,
    )
    points: MutableSequence["Point"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="Point",
    )
    unit: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ReservationData(proto.Message):
    r"""Response entity for reservations data.

    Attributes:
        name (str):
            Identifier. The resource name of the connection in the form
            of:
            ``projects/{project_id}/locations/{location_id}/reservations/{reservation_id}``
            or
            ``organizations/{organization_id}/locations/{location_id}/reservations/{reservation_id}``
            or
            ``folders/{folder_id}/locations/{location_id}/reservations/{reservation_id}``
        time_series (google.cloud.capacityplanner_v1beta.types.TimeSeries):
            The collection of data points that represent
            the aggregated reserved value for reservations
            filtered by the criteria.
        used_reservation_values (google.cloud.capacityplanner_v1beta.types.TimeSeries):
            The collection of data points that represent
            the aggregated used value for reservations
            filtered by the criteria.
        future_reservations (MutableSequence[google.cloud.capacityplanner_v1beta.types.FutureReservation]):
            Future reservations filtered by the criteria.
        allocations (MutableSequence[google.cloud.capacityplanner_v1beta.types.Allocation]):
            Allocations filtered by the criteria.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    time_series: "TimeSeries" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="TimeSeries",
    )
    used_reservation_values: "TimeSeries" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="TimeSeries",
    )
    future_reservations: MutableSequence[future_reservation.FutureReservation] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message=future_reservation.FutureReservation,
        )
    )
    allocations: MutableSequence[allocation.Allocation] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=allocation.Allocation,
    )


class MachineShape(proto.Message):
    r"""Machine shape details
    Next : 13

    Attributes:
        machine_family (str):
            Optional. The VM family.
        machine_type (str):
            Optional. The characteristics of the sampled
            VM expressed as a string.
        machine_shape (str):
            Optional. The customer visible string
            representing the type of VM.
        cpu_cores (float):
            Optional. Number of CPU cores per VM.
        gpu_type (str):
            Optional. The type of GPU with the VM.
        gpu_compute_type (str):
            Optional. The GPU name recognized by Compute
            Engine APIs.
        gpu_cores (int):
            Optional. The number of GPU cores per VM.
        local_ssd_partitions (int):
            Optional. The number of local SSD partitions
            per VM.
        local_ssd_gb (float):
            Optional. Total amount of local SSD storage.
        memory_gb (float):
            Optional. Total amount of memory with the VM.
        local_ssd_interface (str):
            Optional. The local SSD interface used such
            as nvme or scsi
        min_cpu_platform (str):
            Optional. The Min-cpu platform used such as
            icelake
    """

    machine_family: str = proto.Field(
        proto.STRING,
        number=1,
    )
    machine_type: str = proto.Field(
        proto.STRING,
        number=2,
    )
    machine_shape: str = proto.Field(
        proto.STRING,
        number=3,
    )
    cpu_cores: float = proto.Field(
        proto.DOUBLE,
        number=4,
    )
    gpu_type: str = proto.Field(
        proto.STRING,
        number=5,
    )
    gpu_compute_type: str = proto.Field(
        proto.STRING,
        number=10,
    )
    gpu_cores: int = proto.Field(
        proto.INT64,
        number=6,
    )
    local_ssd_partitions: int = proto.Field(
        proto.INT64,
        number=7,
    )
    local_ssd_gb: float = proto.Field(
        proto.DOUBLE,
        number=8,
    )
    memory_gb: float = proto.Field(
        proto.DOUBLE,
        number=9,
    )
    local_ssd_interface: str = proto.Field(
        proto.STRING,
        number=11,
    )
    min_cpu_platform: str = proto.Field(
        proto.STRING,
        number=12,
    )


class ExportUsageHistoriesRequest(proto.Message):
    r"""The ``ExportUsageHistories`` request Next : 12

    Attributes:
        parent (str):
            Required. The compute engine resource and
            location for the time series values to return.
            The format is:

               projects/{project}/locations/{location} or
            organizations/{organization}/locations/{location}
            or    folders/{folder}/locations/{location}
        is_spot (bool):
            Optional. Set true to export usage for spot
            resources.
        machine_family (str):
            Optional. The machine family for the ``UsageHistory`` values
            to return. Possible values include "n1", and "n2d". See
            https://cloud.google.com/compute/docs/machine-types for more
            examples.
        machine_shape (google.cloud.capacityplanner_v1beta.types.MachineShape):
            Optional. The machine shape for the time
            series values to export.
        disk_type (str):
            Optional. The disk_type for the ``UsageHistory`` values to
            return request with persistent-disk resource_type. Possible
            values include "pd-ssd", "pd-standard", "pd-balanced", and
            "pd-extreme".
        gpu_type (str):
            Optional. The GPU type for the ``UsageHistory`` values to
            return. Sample values are "nvidia-tesla-t4", and
            "nvidia-tesla-a100". See
            https://cloud.google.com/compute/docs/gpus for a list. Empty
            gpu_type will return results matching all GPUs.
        tpu_type (str):
            Optional. The TPU type for the ``UsageHistory`` values to
            return. Empty tpu_type will return results matching all
            TPUs.
        resource_type (str):
            Required. The resource for the ``UsageHistory`` values to
            return. Possible values include "gce-vcpus", "gce-ram",
            "gce-local-ssd", "gce-persistent-disk", "gce-gpu" and
            "gce-tpu".
        usage_aggregation_method (google.cloud.capacityplanner_v1beta.types.UsageHistory.AggregationMethod):
            Optional. The method that should be used to convert sampled
            usage data to daily usage values.
            AGGREGATION_METHOD_UNSPECIFIED will return results matching
            all the aggregation methods.
        start_date (google.type.date_pb2.Date):
            Optional. The start date of usage.
        end_date (google.type.date_pb2.Date):
            Optional. The end date of usage.
        output_config (google.cloud.capacityplanner_v1beta.types.OutputConfig):
            Required. Output configuration indicating
            where the results will be output to.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    is_spot: bool = proto.Field(
        proto.BOOL,
        number=11,
    )
    machine_family: str = proto.Field(
        proto.STRING,
        number=2,
    )
    machine_shape: "MachineShape" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="MachineShape",
    )
    disk_type: str = proto.Field(
        proto.STRING,
        number=3,
    )
    gpu_type: str = proto.Field(
        proto.STRING,
        number=9,
    )
    tpu_type: str = proto.Field(
        proto.STRING,
        number=10,
    )
    resource_type: str = proto.Field(
        proto.STRING,
        number=4,
    )
    usage_aggregation_method: "UsageHistory.AggregationMethod" = proto.Field(
        proto.ENUM,
        number=5,
        enum="UsageHistory.AggregationMethod",
    )
    start_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=6,
        message=date_pb2.Date,
    )
    end_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=7,
        message=date_pb2.Date,
    )
    output_config: "OutputConfig" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="OutputConfig",
    )


class ExportForecastsRequest(proto.Message):
    r"""The ``ExportForecasts`` request Next : 13

    Attributes:
        parent (str):
            Required. The compute engine resource and
            location for the time series values to return.
            The format is:

               projects/{project}/locations/{location} or
            organizations/{organization}/locations/{location}
            or    folders/{folder}/locations/{location}
        machine_family (str):
            Optional. The machine family to use to select the
            ``Forecast`` values to return. Possible values include "n1",
            and "n2d".
        machine_shape (google.cloud.capacityplanner_v1beta.types.MachineShape):
            Optional. The machine shape for the time
            series values to export.
        disk_type (str):
            Optional. The disk_type for the ``Forecast`` values to
            return with request persistent-disk resource_type.
        gpu_type (str):
            Optional. The GPU type for the ``Forecast`` values to
            return. Sample values are "nvidia-tesla-t4", and
            "nvidia-tesla-a100". See
            https://cloud.google.com/compute/docs/gpus for a list. Empty
            gpu_type will return results matching all GPUs.
        tpu_type (str):
            Optional. The TPU type for the ``Forecast`` values to
            return. Empty tpu_type will return results matching all
            TPUs.
        resource_type (str):
            Required. The resource for the ``Forecast`` values to
            return. Possible values include "gce-vcpus", "gce-ram",
            "gce-local-ssd", "gce-persistent-disk", "gce-gpu" and
            "gce-tpu".
        prediction_interval (google.cloud.capacityplanner_v1beta.types.Forecast.PredictionInterval):
            Optional. The prediction interval to use to select the
            ``Forecast`` values to return.
            PREDICTION_INTERVAL_UNSPECIFIED will return results matching
            all prediction intervals.
        aggregation_method (google.cloud.capacityplanner_v1beta.types.UsageHistory.AggregationMethod):
            Optional. Aggregation Method of the
            historical usage for which the forecast is
            generated.
        start_date (google.type.date_pb2.Date):
            Optional. The start date of forecasts.
        end_date (google.type.date_pb2.Date):
            Optional. The end date of forecasts.
        output_config (google.cloud.capacityplanner_v1beta.types.OutputConfig):
            Required. Output configuration indicating
            where the results will be output to.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    machine_family: str = proto.Field(
        proto.STRING,
        number=2,
    )
    machine_shape: "MachineShape" = proto.Field(
        proto.MESSAGE,
        number=12,
        message="MachineShape",
    )
    disk_type: str = proto.Field(
        proto.STRING,
        number=3,
    )
    gpu_type: str = proto.Field(
        proto.STRING,
        number=10,
    )
    tpu_type: str = proto.Field(
        proto.STRING,
        number=11,
    )
    resource_type: str = proto.Field(
        proto.STRING,
        number=4,
    )
    prediction_interval: "Forecast.PredictionInterval" = proto.Field(
        proto.ENUM,
        number=5,
        enum="Forecast.PredictionInterval",
    )
    aggregation_method: "UsageHistory.AggregationMethod" = proto.Field(
        proto.ENUM,
        number=6,
        enum="UsageHistory.AggregationMethod",
    )
    start_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=7,
        message=date_pb2.Date,
    )
    end_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=8,
        message=date_pb2.Date,
    )
    output_config: "OutputConfig" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="OutputConfig",
    )


class ExportReservationsUsageRequest(proto.Message):
    r"""The ``ExportReservationsUsage`` request

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        machine_family (str):
            Optional. The machine family to query
            reservations and usage by. For example: n1, n2d.

            This field is a member of `oneof`_ ``resource``.
        machine_shape (google.cloud.capacityplanner_v1beta.types.MachineShape):
            Optional. The machine_shape as a filter to select matching
            reservations and its usage.

            This field is a member of `oneof`_ ``resource``.
        gpu_type (str):
            Optional. The GPU type to query reservations
            and usage  by. For example: NVIDIA T4.

            This field is a member of `oneof`_ ``resource``.
        parent (str):
            Required. The compute engine resource and
            location of the reservationsusage. The format
            is:

               projects/{project}/locations/{location} or
            organizations/{organization}/locations/{location}
            or    folders/{folder}/locations/{location}
        location_level (google.cloud.capacityplanner_v1beta.types.TimeSeries.LocationType):
            Optional. The location level of the
            reservations usage timeseries.
        cloud_resource_type (str):
            Required. The resource for the ``ReservationsUsage`` values
            to return. Possible values include "gce-vcpus", "gce-ram",
            "gce-local-ssd", and "gce-gpu".
        usage_aggregation_method (google.cloud.capacityplanner_v1beta.types.UsageHistory.AggregationMethod):
            Required. The method that should be used to
            convert sampled reservations data to daily usage
            values.
        share_type (google.cloud.capacityplanner_v1beta.types.ExportReservationsUsageRequest.ShareType):
            Optional. Type of share settings to filter
            reservations in response. If unspecified, all
            types are included.
        start_date (google.type.date_pb2.Date):
            Optional. The start date of reservations
            usage.
        end_date (google.type.date_pb2.Date):
            Optional. The end date of reservations usage.
        output_config (google.cloud.capacityplanner_v1beta.types.OutputConfig):
            Required. Output configuration indicating
            where the results will be output to.
    """

    class ShareType(proto.Enum):
        r"""Possible scope in which the reservation can be shared.

        Values:
            SHARE_TYPE_UNSPECIFIED (0):
                No share type specified.
            SHARE_TYPE_LOCAL (1):
                Default value, for which reservation is open
                to only owner project.
            SHARE_TYPE_SPECIFIC_PROJECTS (2):
                Shared-reservation is open to specific
                projects.
        """

        SHARE_TYPE_UNSPECIFIED = 0
        SHARE_TYPE_LOCAL = 1
        SHARE_TYPE_SPECIFIC_PROJECTS = 2

    machine_family: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="resource",
    )
    machine_shape: "MachineShape" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="resource",
        message="MachineShape",
    )
    gpu_type: str = proto.Field(
        proto.STRING,
        number=4,
        oneof="resource",
    )
    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    location_level: "TimeSeries.LocationType" = proto.Field(
        proto.ENUM,
        number=11,
        enum="TimeSeries.LocationType",
    )
    cloud_resource_type: str = proto.Field(
        proto.STRING,
        number=5,
    )
    usage_aggregation_method: "UsageHistory.AggregationMethod" = proto.Field(
        proto.ENUM,
        number=6,
        enum="UsageHistory.AggregationMethod",
    )
    share_type: ShareType = proto.Field(
        proto.ENUM,
        number=7,
        enum=ShareType,
    )
    start_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=8,
        message=date_pb2.Date,
    )
    end_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=9,
        message=date_pb2.Date,
    )
    output_config: "OutputConfig" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="OutputConfig",
    )


class OutputConfig(proto.Message):
    r"""Output configuration for export destination.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_destination (google.cloud.capacityplanner_v1beta.types.GcsDestination):
            Destination on Cloud Storage.

            This field is a member of `oneof`_ ``destination``.
        bigquery_destination (google.cloud.capacityplanner_v1beta.types.BigQueryDestination):
            Destination on BigQuery.

            This field is a member of `oneof`_ ``destination``.
    """

    gcs_destination: "GcsDestination" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="destination",
        message="GcsDestination",
    )
    bigquery_destination: "BigQueryDestination" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="destination",
        message="BigQueryDestination",
    )


class GcsDestination(proto.Message):
    r"""A Cloud Storage location.

    Attributes:
        uri (str):
            Optional. The path to the file in Cloud Storage where the
            export will be stored. The URI is in the form
            ``gs://bucketName/fileName``. If the file already exists,
            the request succeeds, but the operation fails.
        bucket (str):
            Required. The bucket name to which the export
            will be stored.
        object_ (str):
            Required. The object name to which the export
            will be stored.
        force (bool):
            Optional. Flag to indicate overwrite in case
            file already exists.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    bucket: str = proto.Field(
        proto.STRING,
        number=3,
    )
    object_: str = proto.Field(
        proto.STRING,
        number=4,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class BigQueryDestination(proto.Message):
    r"""A BigQuery destination for exporting assets to.

    Attributes:
        dataset (str):
            Required. The BigQuery dataset in format
            "projects/{projectId}/datasets/{datasetId}", to which the
            snapshot result should be exported. If this dataset does not
            exist, the export call returns an INVALID_ARGUMENT error.
        table (str):
            Required. The BigQuery table to which the
            snapshot result should be written.
        partition_key (google.cloud.capacityplanner_v1beta.types.BigQueryDestination.PartitionKey):
            Optional. The partition key for BigQuery
            partitioned table.
        write_disposition (google.cloud.capacityplanner_v1beta.types.BigQueryDestination.WriteDisposition):
            Optional. Specifies the action that occurs if
            the destination table or partition already
            exists.
        create_disposition (google.cloud.capacityplanner_v1beta.types.BigQueryDestination.CreateDisposition):
            Optional. Specifies the action that occurs if
            the destination table does not exist
        gcs_location (str):
            Optional. Specifies the Cloud Storage
            location. Users can choose to provide a location
            for Cloud Storage bucket to store the exported
            data. (as it is possible that some locations are
            restricted via org policy for that project)
            Temporary Cloud Storage bucket creation is an
            interim step for BigQuery upload. If no value is
            provided, the default location used will be
            'US'.
    """

    class PartitionKey(proto.Enum):
        r"""This enum determines the partition key column for the
        BigQuery tables. Partitioning can improve query performance and
        reduce query cost by filtering partitions. Refer to
        https://cloud.google.com/bigquery/docs/partitioned-tables for
        details.

        Values:
            PARTITION_KEY_UNSPECIFIED (0):
                Unspecified partition key. Tables won't be
                partitioned using this option.
            REQUEST_TIME (1):
                The time when the request is received. If
                specified as partition key, the result table(s)
                is partitioned by the RequestTime column, an
                additional timestamp column representing when
                the request was received.
        """

        PARTITION_KEY_UNSPECIFIED = 0
        REQUEST_TIME = 1

    class WriteDisposition(proto.Enum):
        r"""Specifies the action that occurs if the destination table or
        partition already exists. By default, the data will be appended
        to the existing table.

        Values:
            WRITE_DISPOSITION_UNSPECIFIED (0):
                Unspecified write disposition.
            WRITE_APPEND (1):
                If the table or partition already exists,
                BigQuery appends the data to the table or the
                latest partition.
            WRITE_TRUNCATE (2):
                If the table or partition already exists,
                BigQuery overwrites the entire table or all the
                partitions data.
            WRITE_EMPTY (3):
                If the table already exists and contains
                data, an error is returned.
        """

        WRITE_DISPOSITION_UNSPECIFIED = 0
        WRITE_APPEND = 1
        WRITE_TRUNCATE = 2
        WRITE_EMPTY = 3

    class CreateDisposition(proto.Enum):
        r"""Specifies the action that occurs if the destination table
        does not exist. By default, a new table will be created.

        Values:
            CREATE_DISPOSITION_UNSPECIFIED (0):
                Unspecified create disposition.
            CREATE_IF_NEEDED (1):
                If the table does not exist, BigQuery creates
                the table.
            CREATE_NEVER (2):
                If the table does not exist, an error will be
                returned.
        """

        CREATE_DISPOSITION_UNSPECIFIED = 0
        CREATE_IF_NEEDED = 1
        CREATE_NEVER = 2

    dataset: str = proto.Field(
        proto.STRING,
        number=1,
    )
    table: str = proto.Field(
        proto.STRING,
        number=2,
    )
    partition_key: PartitionKey = proto.Field(
        proto.ENUM,
        number=3,
        enum=PartitionKey,
    )
    write_disposition: WriteDisposition = proto.Field(
        proto.ENUM,
        number=4,
        enum=WriteDisposition,
    )
    create_disposition: CreateDisposition = proto.Field(
        proto.ENUM,
        number=5,
        enum=CreateDisposition,
    )
    gcs_location: str = proto.Field(
        proto.STRING,
        number=6,
    )


class OperationMetadata(proto.Message):
    r"""Represents the metadata of a long-running operation.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation finished
            running.
    """

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


class ExportUsageHistoriesResponse(proto.Message):
    r"""A response message for [UsageService.ExportUsageHistories].

    Attributes:
        response (str):
            The response message for the usage history
            export. In case of bigquery, it will also
            contain job id.
    """

    response: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ExportForecastsResponse(proto.Message):
    r"""A response message for [UsageService.ExportForecasts].

    Attributes:
        response (str):
            The response message for the forecast export.
            In case of bigquery, it will also contain job
            id.
    """

    response: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ExportReservationsUsageResponse(proto.Message):
    r"""A response message for [UsageService.ExportReservationsUsage].

    Attributes:
        response (str):
            The response message for the reservations
            usage export. In case of bigquery, it will also
            contain job id.
    """

    response: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
