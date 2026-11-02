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
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.visionai.v1alpha1",
    manifest={
        "Stream",
        "Event",
        "Series",
        "Channel",
    },
)


class Stream(proto.Message):
    r"""Message describing the Stream object. The Stream and the
    Event resources are many to many; i.e., each Stream resource can
    associate to many Event resources and each Event resource can
    associate to many Stream resources.

    Attributes:
        name (str):
            Name of the resource.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The create timestamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The update timestamp.
        labels (MutableMapping[str, str]):
            Labels as key value pairs.
        annotations (MutableMapping[str, str]):
            Annotations to allow clients to store small
            amounts of arbitrary data.
        display_name (str):
            The display name for the stream resource.
        enable_hls_playback (bool):
            Whether to enable the HLS playback service on
            this stream.
        media_warehouse_asset (str):
            The name of the media warehouse asset for long term storage
            of stream data. Format:
            projects/${p_id}/locations/${l_id}/corpora/${c_id}/assets/${a_id}
            Remain empty if the media warehouse storage is not needed
            for the stream.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=6,
    )
    enable_hls_playback: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    media_warehouse_asset: str = proto.Field(
        proto.STRING,
        number=8,
    )


class Event(proto.Message):
    r"""Message describing the Event object.

    Attributes:
        name (str):
            Name of the resource.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The create timestamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The update timestamp.
        labels (MutableMapping[str, str]):
            Labels as key value pairs.
        annotations (MutableMapping[str, str]):
            Annotations to allow clients to store small
            amounts of arbitrary data.
        alignment_clock (google.cloud.visionai_v1alpha1.types.Event.Clock):
            The clock used for joining streams.
        grace_period (google.protobuf.duration_pb2.Duration):
            Grace period for cleaning up the event. This is the time the
            controller waits for before deleting the event. During this
            period, if there is any active channel on the event. The
            deletion of the event after grace_period will be ignored.
    """

    class Clock(proto.Enum):
        r"""Clock that will be used for joining streams.

        Values:
            CLOCK_UNSPECIFIED (0):
                Clock is not specified.
            CAPTURE (1):
                Use the timestamp when the data is captured.
                Clients need to sync the clock.
            INGEST (2):
                Use the timestamp when the data is received.
        """

        CLOCK_UNSPECIFIED = 0
        CAPTURE = 1
        INGEST = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    alignment_clock: Clock = proto.Field(
        proto.ENUM,
        number=6,
        enum=Clock,
    )
    grace_period: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=7,
        message=duration_pb2.Duration,
    )


class Series(proto.Message):
    r"""Message describing the Series object.

    Attributes:
        name (str):
            Name of the resource.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The create timestamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The update timestamp.
        labels (MutableMapping[str, str]):
            Labels as key value pairs.
        annotations (MutableMapping[str, str]):
            Annotations to allow clients to store small
            amounts of arbitrary data.
        stream (str):
            Required. Stream that is associated with this
            series.
        event (str):
            Required. Event that is associated with this
            series.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    stream: str = proto.Field(
        proto.STRING,
        number=6,
    )
    event: str = proto.Field(
        proto.STRING,
        number=7,
    )


class Channel(proto.Message):
    r"""Message describing the Channel object.

    Attributes:
        name (str):
            Name of the resource.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The create timestamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The update timestamp.
        labels (MutableMapping[str, str]):
            Labels as key value pairs.
        annotations (MutableMapping[str, str]):
            Annotations to allow clients to store small
            amounts of arbitrary data.
        stream (str):
            Required. Stream that is associated with this
            series.
        event (str):
            Required. Event that is associated with this
            series.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    stream: str = proto.Field(
        proto.STRING,
        number=6,
    )
    event: str = proto.Field(
        proto.STRING,
        number=7,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
