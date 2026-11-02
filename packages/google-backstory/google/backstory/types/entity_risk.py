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
import google.type.interval_pb2 as interval_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.backstory",
    manifest={
        "EntityRisk",
        "RiskDelta",
    },
)


class EntityRisk(proto.Message):
    r"""Stores information related to the risk score of an entity.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        risk_version (str):
            Version of the risk score calculation
            algorithm.
        risk_window (google.type.interval_pb2.Interval):
            Time window used when computing the risk
            score for an entity, for example 24 hours or 7
            days.
        DEPRECATED_risk_score (int):
            Deprecated risk score.
        risk_delta (google.backstory.types.RiskDelta):
            Represents the change in risk score for an
            entity between the end of the previous time
            window and the end of the current time window.

            This field is a member of `oneof`_ ``_risk_delta``.
        detections_count (int):
            Number of detections that make up the risk
            score within the time window.
        first_detection_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp of the first detection within the
            specified time window. This field is empty when
            there are no detections.
        last_detection_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp of the last detection within the
            specified time window. This field is empty when
            there are no detections.
        risk_score (float):
            Raw risk score for the entity.
        normalized_risk_score (int):
            Normalized risk score for the entity. This
            value is between 0-1000.
        risk_window_size (google.protobuf.duration_pb2.Duration):
            Risk window duration for the entity.
        raw_risk_delta (google.backstory.types.RiskDelta):
            Represents the change in raw risk score for
            an entity between the end of the previous time
            window and the end of the current time window.

            This field is a member of `oneof`_ ``_raw_risk_delta``.
        last_reset_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp for UEBA risk score reset based
            deduplication. Used specifically for risk based
            meta rules.
        detail_uri (str):
            Link to the Google Security Operations UI
            with information about the entity risk score. If
            the SecOps instance has multiple frontend paths
            configured, this will be a relative path that
            can be used to construct the full URL.
        risk_window_has_new_detections (bool):
            Whether there are new detections for the risk
            window.
    """

    risk_version: str = proto.Field(
        proto.STRING,
        number=1,
    )
    risk_window: interval_pb2.Interval = proto.Field(
        proto.MESSAGE,
        number=2,
        message=interval_pb2.Interval,
    )
    DEPRECATED_risk_score: int = proto.Field(
        proto.INT32,
        number=3,
    )
    risk_delta: "RiskDelta" = proto.Field(
        proto.MESSAGE,
        number=4,
        optional=True,
        message="RiskDelta",
    )
    detections_count: int = proto.Field(
        proto.INT32,
        number=5,
    )
    first_detection_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    last_detection_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    risk_score: float = proto.Field(
        proto.FLOAT,
        number=8,
    )
    normalized_risk_score: int = proto.Field(
        proto.INT32,
        number=9,
    )
    risk_window_size: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=10,
        message=duration_pb2.Duration,
    )
    raw_risk_delta: "RiskDelta" = proto.Field(
        proto.MESSAGE,
        number=11,
        optional=True,
        message="RiskDelta",
    )
    last_reset_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=12,
        message=timestamp_pb2.Timestamp,
    )
    detail_uri: str = proto.Field(
        proto.STRING,
        number=13,
    )
    risk_window_has_new_detections: bool = proto.Field(
        proto.BOOL,
        number=14,
    )


class RiskDelta(proto.Message):
    r"""Describes the difference in risk score between two points in
    time.

    Attributes:
        previous_range_end_time (google.protobuf.timestamp_pb2.Timestamp):
            End time of the previous time window.
        risk_score_delta (int):
            Difference in the normalized risk score from
            the previous recorded value.
        previous_risk_score (int):
            Risk score from previous risk window
        risk_score_numeric_delta (int):
            Numeric change between current and previous
            risk score
    """

    previous_range_end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    risk_score_delta: int = proto.Field(
        proto.INT32,
        number=2,
    )
    previous_risk_score: int = proto.Field(
        proto.INT32,
        number=3,
    )
    risk_score_numeric_delta: int = proto.Field(
        proto.INT32,
        number=4,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
