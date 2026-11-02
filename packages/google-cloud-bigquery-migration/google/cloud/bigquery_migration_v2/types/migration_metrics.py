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

import google.api.distribution_pb2 as distribution_pb2  # type: ignore
import google.api.metric_pb2 as metric_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.bigquery.migration.v2",
    manifest={
        "TimeSeries",
        "Point",
        "TimeInterval",
        "TypedValue",
    },
)


class TimeSeries(proto.Message):
    r"""The metrics object for a SubTask.

    Attributes:
        metric (str):
            Required. The name of the metric.

            If the metric is not known by the service yet,
            it will be auto-created.
        value_type (google.api.metric_pb2.ValueType):
            Required. The value type of the time series.
        metric_kind (google.api.metric_pb2.MetricKind):
            Optional. The metric kind of the time series.

            If present, it must be the same as the metric kind of the
            associated metric. If the associated metric's descriptor
            must be auto-created, then this field specifies the metric
            kind of the new descriptor and must be either ``GAUGE`` (the
            default) or ``CUMULATIVE``.
        points (MutableSequence[google.cloud.bigquery_migration_v2.types.Point]):
            Required. The data points of this time series. When listing
            time series, points are returned in reverse time order.

            When creating a time series, this field must contain exactly
            one point and the point's type must be the same as the value
            type of the associated metric. If the associated metric's
            descriptor must be auto-created, then the value type of the
            descriptor is determined by the point's type, which must be
            ``BOOL``, ``INT64``, ``DOUBLE``, or ``DISTRIBUTION``.
    """

    metric: str = proto.Field(
        proto.STRING,
        number=1,
    )
    value_type: metric_pb2.MetricDescriptor.ValueType = proto.Field(
        proto.ENUM,
        number=2,
        enum=metric_pb2.MetricDescriptor.ValueType,
    )
    metric_kind: metric_pb2.MetricDescriptor.MetricKind = proto.Field(
        proto.ENUM,
        number=3,
        enum=metric_pb2.MetricDescriptor.MetricKind,
    )
    points: MutableSequence["Point"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="Point",
    )


class Point(proto.Message):
    r"""A single data point in a time series.

    Attributes:
        interval (google.cloud.bigquery_migration_v2.types.TimeInterval):
            The time interval to which the data point applies. For
            ``GAUGE`` metrics, the start time does not need to be
            supplied, but if it is supplied, it must equal the end time.
            For ``DELTA`` metrics, the start and end time should specify
            a non-zero interval, with subsequent points specifying
            contiguous and non-overlapping intervals. For ``CUMULATIVE``
            metrics, the start and end time should specify a non-zero
            interval, with subsequent points specifying the same start
            time and increasing end times, until an event resets the
            cumulative value to zero and sets a new start time for the
            following points.
        value (google.cloud.bigquery_migration_v2.types.TypedValue):
            The value of the data point.
    """

    interval: "TimeInterval" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="TimeInterval",
    )
    value: "TypedValue" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="TypedValue",
    )


class TimeInterval(proto.Message):
    r"""A time interval extending just after a start time through an
    end time. If the start time is the same as the end time, then
    the interval represents a single point in time.

    Attributes:
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. The beginning of the time interval.
            The default value for the start time is the end
            time. The start time must not be later than the
            end time.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Required. The end of the time interval.
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


class TypedValue(proto.Message):
    r"""A single strongly-typed value.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        bool_value (bool):
            A Boolean value: ``true`` or ``false``.

            This field is a member of `oneof`_ ``value``.
        int64_value (int):
            A 64-bit integer. Its range is approximately
            ``+/-9.2x10^18``.

            This field is a member of `oneof`_ ``value``.
        double_value (float):
            A 64-bit double-precision floating-point number. Its
            magnitude is approximately ``+/-10^(+/-300)`` and it has 16
            significant digits of precision.

            This field is a member of `oneof`_ ``value``.
        string_value (str):
            A variable-length string value.

            This field is a member of `oneof`_ ``value``.
        distribution_value (google.api.distribution_pb2.Distribution):
            A distribution value.

            This field is a member of `oneof`_ ``value``.
    """

    bool_value: bool = proto.Field(
        proto.BOOL,
        number=1,
        oneof="value",
    )
    int64_value: int = proto.Field(
        proto.INT64,
        number=2,
        oneof="value",
    )
    double_value: float = proto.Field(
        proto.DOUBLE,
        number=3,
        oneof="value",
    )
    string_value: str = proto.Field(
        proto.STRING,
        number=4,
        oneof="value",
    )
    distribution_value: distribution_pb2.Distribution = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="value",
        message=distribution_pb2.Distribution,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
