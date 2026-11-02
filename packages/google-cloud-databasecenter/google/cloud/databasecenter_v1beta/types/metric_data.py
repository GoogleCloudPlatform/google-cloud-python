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

__protobuf__ = proto.module(
    package="google.cloud.databasecenter.v1beta",
    manifest={
        "Metrics",
        "MetricData",
        "TypedValue",
    },
)


class Metrics(proto.Message):
    r"""Metrics represents the metrics for a database resource.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        p99_cpu_utilization (google.cloud.databasecenter_v1beta.types.MetricData):
            P99 CPU utilization observed for the
            resource. The value is a fraction between 0.0
            and 1.0 (may momentarily exceed 1.0 in some
            cases).

            This field is a member of `oneof`_ ``_p99_cpu_utilization``.
        p95_cpu_utilization (google.cloud.databasecenter_v1beta.types.MetricData):
            P95 CPU utilization observed for the
            resource. The value is a fraction between 0.0
            and 1.0 (may momentarily exceed 1.0 in some
            cases).

            This field is a member of `oneof`_ ``_p95_cpu_utilization``.
        current_storage_used_bytes (google.cloud.databasecenter_v1beta.types.MetricData):
            Current storage used by the resource in
            bytes.

            This field is a member of `oneof`_ ``_current_storage_used_bytes``.
        peak_storage_utilization (google.cloud.databasecenter_v1beta.types.MetricData):
            Peak storage utilization observed for the
            resource. The value is a fraction between 0.0
            and 1.0 (may momentarily exceed 1.0 in some
            cases).

            This field is a member of `oneof`_ ``_peak_storage_utilization``.
        peak_memory_utilization (google.cloud.databasecenter_v1beta.types.MetricData):
            Peak memory utilization observed for the
            resource. The value is a fraction between 0.0
            and 1.0 (may momentarily exceed 1.0 in some
            cases).

            This field is a member of `oneof`_ ``_peak_memory_utilization``.
        peak_number_connections (google.cloud.databasecenter_v1beta.types.MetricData):
            Peak number of connections observed for the
            resource. The value is a positive integer.

            This field is a member of `oneof`_ ``_peak_number_connections``.
        node_count (google.cloud.databasecenter_v1beta.types.MetricData):
            Number of nodes in instance for spanner or
            bigtable.

            This field is a member of `oneof`_ ``_node_count``.
        processing_unit_count (google.cloud.databasecenter_v1beta.types.MetricData):
            Number of processing units in spanner.

            This field is a member of `oneof`_ ``_processing_unit_count``.
        current_memory_used_bytes (google.cloud.databasecenter_v1beta.types.MetricData):
            Current memory used by the resource in bytes.

            This field is a member of `oneof`_ ``_current_memory_used_bytes``.
    """

    p99_cpu_utilization: "MetricData" = proto.Field(
        proto.MESSAGE,
        number=1,
        optional=True,
        message="MetricData",
    )
    p95_cpu_utilization: "MetricData" = proto.Field(
        proto.MESSAGE,
        number=2,
        optional=True,
        message="MetricData",
    )
    current_storage_used_bytes: "MetricData" = proto.Field(
        proto.MESSAGE,
        number=3,
        optional=True,
        message="MetricData",
    )
    peak_storage_utilization: "MetricData" = proto.Field(
        proto.MESSAGE,
        number=4,
        optional=True,
        message="MetricData",
    )
    peak_memory_utilization: "MetricData" = proto.Field(
        proto.MESSAGE,
        number=5,
        optional=True,
        message="MetricData",
    )
    peak_number_connections: "MetricData" = proto.Field(
        proto.MESSAGE,
        number=6,
        optional=True,
        message="MetricData",
    )
    node_count: "MetricData" = proto.Field(
        proto.MESSAGE,
        number=7,
        optional=True,
        message="MetricData",
    )
    processing_unit_count: "MetricData" = proto.Field(
        proto.MESSAGE,
        number=8,
        optional=True,
        message="MetricData",
    )
    current_memory_used_bytes: "MetricData" = proto.Field(
        proto.MESSAGE,
        number=9,
        optional=True,
        message="MetricData",
    )


class MetricData(proto.Message):
    r"""MetricData represents the metric data for a database
    resource.

    Attributes:
        value (google.cloud.databasecenter_v1beta.types.TypedValue):
            The value associated with the metric.
        observation_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the metric was observed in the
            metric source service.
    """

    value: "TypedValue" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="TypedValue",
    )
    observation_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


class TypedValue(proto.Message):
    r"""TypedValue represents the value of the metric based on data
    type.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        double_value (float):
            The value of the metric as double.

            This field is a member of `oneof`_ ``value``.
        int64_value (int):
            The value of the metric as int.

            This field is a member of `oneof`_ ``value``.
    """

    double_value: float = proto.Field(
        proto.DOUBLE,
        number=1,
        oneof="value",
    )
    int64_value: int = proto.Field(
        proto.INT64,
        number=2,
        oneof="value",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
