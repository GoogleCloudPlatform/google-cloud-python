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

__protobuf__ = proto.module(
    package="google.cloud.devicestreaming.v1",
    manifest={
        "DeviceMessage",
        "AdbMessage",
        "StatusUpdate",
        "StreamStatus",
        "Open",
        "StreamData",
        "Okay",
        "Fail",
        "Close",
    },
)


class DeviceMessage(proto.Message):
    r"""A message returned from a device.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        status_update (google.cloud.devicestreaming_v1.types.StatusUpdate):
            Information about the device's state.

            This field is a member of `oneof`_ ``contents``.
        stream_status (google.cloud.devicestreaming_v1.types.StreamStatus):
            The result of a device stream from ADB.

            This field is a member of `oneof`_ ``contents``.
        stream_data (google.cloud.devicestreaming_v1.types.StreamData):
            Data from an open stream.

            This field is a member of `oneof`_ ``contents``.
    """

    status_update: "StatusUpdate" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="contents",
        message="StatusUpdate",
    )
    stream_status: "StreamStatus" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="contents",
        message="StreamStatus",
    )
    stream_data: "StreamData" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="contents",
        message="StreamData",
    )


class AdbMessage(proto.Message):
    r"""A message to an ADB server.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        open_ (google.cloud.devicestreaming_v1.types.Open):
            Open a new stream.

            This field is a member of `oneof`_ ``contents``.
        stream_data (google.cloud.devicestreaming_v1.types.StreamData):
            Send data to a stream.

            This field is a member of `oneof`_ ``contents``.
    """

    open_: "Open" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="contents",
        message="Open",
    )
    stream_data: "StreamData" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="contents",
        message="StreamData",
    )


class StatusUpdate(proto.Message):
    r"""A StatusUpdate message given over the ADB protocol for the
    device state.

    Attributes:
        state (google.cloud.devicestreaming_v1.types.StatusUpdate.DeviceState):
            The device's state
        properties (MutableMapping[str, str]):
            A map of properties with information about
            this device.
        features (str):
            A comma-separated list of "features" that
            this device supports.
    """

    class DeviceState(proto.Enum):
        r"""The state displayed with the ADB Device when running "adb
        devices"

        Values:
            DEVICE_STATE_UNSPECIFIED (0):
                The device state is unknown.
            DEVICE (1):
                The ADB device is in the "device" status.
            RECOVERY (2):
                The ADB device is in the "recovery" status.
            RESCUE (3):
                The ADB device is in the "rescue" status.
            SIDELOAD (4):
                The ADB device is in the "sideload" status.
            MISSING (10):
                The ADB device is in the "missing" status.
            OFFLINE (11):
                The ADB device is in the "offline" status.
            UNAUTHORIZED (12):
                The ADB device is in the "unauthorized"
                status.
            AUTHORIZING (13):
                The ADB device is in the "authorizing"
                status.
            CONNECTING (14):
                The ADB device is in the "connecting" status.
        """

        DEVICE_STATE_UNSPECIFIED = 0
        DEVICE = 1
        RECOVERY = 2
        RESCUE = 3
        SIDELOAD = 4
        MISSING = 10
        OFFLINE = 11
        UNAUTHORIZED = 12
        AUTHORIZING = 13
        CONNECTING = 14

    state: DeviceState = proto.Field(
        proto.ENUM,
        number=1,
        enum=DeviceState,
    )
    properties: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )
    features: str = proto.Field(
        proto.STRING,
        number=3,
    )


class StreamStatus(proto.Message):
    r"""The result of a stream.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        stream_id (int):
            The unique ID of this stream, assigned by the
            client.
        okay (google.cloud.devicestreaming_v1.types.Okay):
            Okay for success.

            This field is a member of `oneof`_ ``status``.
        fail (google.cloud.devicestreaming_v1.types.Fail):
            Fail for failure.

            This field is a member of `oneof`_ ``status``.
    """

    stream_id: int = proto.Field(
        proto.INT32,
        number=1,
    )
    okay: "Okay" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="status",
        message="Okay",
    )
    fail: "Fail" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="status",
        message="Fail",
    )


class Open(proto.Message):
    r"""Message for opening a new stream.

    Attributes:
        stream_id (int):
            Required. The unique ID that will be used to
            talk to this stream. This should probably just
            be a number that increments for each new Open
            request.
        service (str):
            Optional. An ADB service to use in the new
            stream.
    """

    stream_id: int = proto.Field(
        proto.INT32,
        number=1,
    )
    service: str = proto.Field(
        proto.STRING,
        number=2,
    )


class StreamData(proto.Message):
    r"""Data for a stream.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        stream_id (int):
            Required. The unique ID of this stream,
            assigned by the client.
        data (bytes):
            Data in the stream.

            This field is a member of `oneof`_ ``contents``.
        close (google.cloud.devicestreaming_v1.types.Close):
            The stream is closing. EOF.

            This field is a member of `oneof`_ ``contents``.
    """

    stream_id: int = proto.Field(
        proto.INT32,
        number=1,
    )
    data: bytes = proto.Field(
        proto.BYTES,
        number=2,
        oneof="contents",
    )
    close: "Close" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="contents",
        message="Close",
    )


class Okay(proto.Message):
    r"""Message signifying that the stream is open"""


class Fail(proto.Message):
    r"""Message signifying that the stream failed to open

    Attributes:
        reason (str):
            A user-displayable failure reason.
    """

    reason: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Close(proto.Message):
    r"""Message signifying that the stream closed."""


__all__ = tuple(sorted(__protobuf__.manifest))
