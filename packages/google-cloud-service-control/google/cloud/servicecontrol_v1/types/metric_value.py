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

from google.cloud.servicecontrol_v1.types import distribution as gas_distribution

__protobuf__ = proto.module(
    package="google.api.servicecontrol.v1",
    manifest={
        "MetricValue",
        "MetricValueSet",
    },
)


class MetricValue(proto.Message):
    r"""Represents a single metric value.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        labels (MutableMapping[str, str]):
            The labels describing the metric value. See comments on
            [google.api.servicecontrol.v1.Operation.labels][google.api.servicecontrol.v1.Operation.labels]
            for the overriding relationship. Note that this map must not
            contain monitored resource labels.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            The start of the time period over which this metric value's
            measurement applies. The time period has different semantics
            for different metric types (cumulative, delta, and gauge).
            See the metric definition documentation in the service
            configuration for details. If not specified,
            [google.api.servicecontrol.v1.Operation.start_time][google.api.servicecontrol.v1.Operation.start_time]
            will be used.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            The end of the time period over which this metric value's
            measurement applies. If not specified,
            [google.api.servicecontrol.v1.Operation.end_time][google.api.servicecontrol.v1.Operation.end_time]
            will be used.
        bool_value (bool):
            A boolean value.

            This field is a member of `oneof`_ ``value``.
        int64_value (int):
            A signed 64-bit integer value.

            This field is a member of `oneof`_ ``value``.
        double_value (float):
            A double precision floating point value.

            This field is a member of `oneof`_ ``value``.
        string_value (str):
            A text string value.

            This field is a member of `oneof`_ ``value``.
        distribution_value (google.cloud.servicecontrol_v1.types.Distribution):
            A distribution value.

            This field is a member of `oneof`_ ``value``.
    """

    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=1,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    bool_value: bool = proto.Field(
        proto.BOOL,
        number=4,
        oneof="value",
    )
    int64_value: int = proto.Field(
        proto.INT64,
        number=5,
        oneof="value",
    )
    double_value: float = proto.Field(
        proto.DOUBLE,
        number=6,
        oneof="value",
    )
    string_value: str = proto.Field(
        proto.STRING,
        number=7,
        oneof="value",
    )
    distribution_value: gas_distribution.Distribution = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="value",
        message=gas_distribution.Distribution,
    )


class MetricValueSet(proto.Message):
    r"""Represents a set of metric values in the same metric.
    Each metric value in the set should have a unique combination of
    start time, end time, and label values.

    Attributes:
        metric_name (str):
            The metric name defined in the service
            configuration.
        metric_values (MutableSequence[google.cloud.servicecontrol_v1.types.MetricValue]):
            The values in this metric.
    """

    metric_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    metric_values: MutableSequence["MetricValue"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="MetricValue",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
