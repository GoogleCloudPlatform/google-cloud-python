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
import google.type.date_pb2 as date_pb2  # type: ignore
import google.type.timeofday_pb2 as timeofday_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.devicesandservices.health.v4",
    manifest={
        "CivilDateTime",
        "CivilTimeInterval",
        "ObservationTimeInterval",
        "SessionTimeInterval",
        "ObservationSampleTime",
    },
)


class CivilDateTime(proto.Message):
    r"""Civil time representation similar to
    [google.type.DateTime][google.type.DateTime], but ensures that
    neither the timezone nor the UTC offset can be set to avoid
    confusion between civil and physical time queries.

    Attributes:
        date (google.type.date_pb2.Date):
            Required. Calendar date.
        time (google.type.timeofday_pb2.TimeOfDay):
            Optional. Time of day. Defaults to the start
            of the day, at midnight if omitted.
    """

    date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=1,
        message=date_pb2.Date,
    )
    time: timeofday_pb2.TimeOfDay = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timeofday_pb2.TimeOfDay,
    )


class CivilTimeInterval(proto.Message):
    r"""Counterpart of [google.type.Interval][google.type.Interval], but
    using
    [CivilDateTime][google.devicesandservices.health.v4.CivilDateTime].

    Attributes:
        start (google.devicesandservices.health_v4.types.CivilDateTime):
            Required. The inclusive start of the range.
        end (google.devicesandservices.health_v4.types.CivilDateTime):
            Required. The exclusive end of the range.
    """

    start: "CivilDateTime" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="CivilDateTime",
    )
    end: "CivilDateTime" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="CivilDateTime",
    )


class ObservationTimeInterval(proto.Message):
    r"""Represents a time interval of an observed data point.

    Attributes:
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Required. Observed interval start time.
        start_utc_offset (google.protobuf.duration_pb2.Duration):
            Required. The offset of the user's local time
            at the start of the observation relative to the
            Coordinated Universal Time (UTC).
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Required. Observed interval end time.
        end_utc_offset (google.protobuf.duration_pb2.Duration):
            Required. The offset of the user's local time
            at the end of the observation relative to the
            Coordinated Universal Time (UTC).
        civil_start_time (google.devicesandservices.health_v4.types.CivilDateTime):
            Output only. Observed interval start time in
            civil time in the timezone the subject is in at
            the start of the observed interval
        civil_end_time (google.devicesandservices.health_v4.types.CivilDateTime):
            Output only. Observed interval end time in
            civil time in the timezone the subject is in at
            the end of the observed interval
    """

    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    start_utc_offset: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    end_utc_offset: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=4,
        message=duration_pb2.Duration,
    )
    civil_start_time: "CivilDateTime" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="CivilDateTime",
    )
    civil_end_time: "CivilDateTime" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="CivilDateTime",
    )


class SessionTimeInterval(proto.Message):
    r"""Represents a time interval of session data point, which
    bundles multiple observed metrics together.

    Attributes:
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Required. The start time of the observed
            session.
        start_utc_offset (google.protobuf.duration_pb2.Duration):
            Required. The offset of the user's local time
            at the start of the session relative to the
            Coordinated Universal Time (UTC).
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Required. The end time of the observed
            session.
        end_utc_offset (google.protobuf.duration_pb2.Duration):
            Required. The offset of the user's local time
            at the end of the session relative to the
            Coordinated Universal Time (UTC).
        civil_start_time (google.devicesandservices.health_v4.types.CivilDateTime):
            Output only. Session start time in civil time
            in the timezone the subject is in at the start
            of the session.
        civil_end_time (google.devicesandservices.health_v4.types.CivilDateTime):
            Output only. Session end time in civil time
            in the timezone the subject is in at the end of
            the session.
    """

    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    start_utc_offset: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    end_utc_offset: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=4,
        message=duration_pb2.Duration,
    )
    civil_start_time: "CivilDateTime" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="CivilDateTime",
    )
    civil_end_time: "CivilDateTime" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="CivilDateTime",
    )


class ObservationSampleTime(proto.Message):
    r"""Represents a sample time of an observed data point.

    Attributes:
        physical_time (google.protobuf.timestamp_pb2.Timestamp):
            Required. The time of the observation.
        utc_offset (google.protobuf.duration_pb2.Duration):
            Required. The offset of the user's local time
            during the observation relative to the
            Coordinated Universal Time (UTC).
        civil_time (google.devicesandservices.health_v4.types.CivilDateTime):
            Output only. The civil time in the timezone
            the subject is in at the time of the
            observation.
    """

    physical_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    utc_offset: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )
    civil_time: "CivilDateTime" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="CivilDateTime",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
