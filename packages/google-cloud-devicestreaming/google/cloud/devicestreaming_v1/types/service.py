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
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.devicestreaming.v1",
    manifest={
        "CreateDeviceSessionRequest",
        "ListDeviceSessionsRequest",
        "ListDeviceSessionsResponse",
        "GetDeviceSessionRequest",
        "CancelDeviceSessionRequest",
        "UpdateDeviceSessionRequest",
        "DeviceSession",
        "ClientInfo",
        "AndroidDevice",
    },
)


class CreateDeviceSessionRequest(proto.Message):
    r"""Request message for DirectAccessService.CreateDeviceSession.

    Attributes:
        parent (str):
            Required. The Compute Engine project under which this device
            will be allocated. "projects/{project_id}".
        device_session (google.cloud.devicestreaming_v1.types.DeviceSession):
            Required. A DeviceSession to create.
        device_session_id (str):
            Optional. The ID to use for the DeviceSession, which will
            become the final component of the DeviceSession's resource
            name.

            This value should be 4-63 characters, and valid characters
            are /[a-z][0-9]-/.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    device_session: "DeviceSession" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DeviceSession",
    )
    device_session_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListDeviceSessionsRequest(proto.Message):
    r"""Request message for DirectAccessService.ListDeviceSessions.

    Attributes:
        parent (str):
            Required. The name of the parent to request, e.g.
            "projects/{project_id}".
        page_size (int):
            Optional. The maximum number of
            DeviceSessions to return.
        page_token (str):
            Optional. A continuation token for paging.
        filter (str):
            Optional. If specified, responses will be filtered by the
            given filter. Allowed fields are: session_state.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=4,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=1,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListDeviceSessionsResponse(proto.Message):
    r"""Response message for DirectAccessService.ListDeviceSessions.

    Attributes:
        device_sessions (MutableSequence[google.cloud.devicestreaming_v1.types.DeviceSession]):
            The sessions matching the specified filter in
            the given cloud project.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    device_sessions: MutableSequence["DeviceSession"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DeviceSession",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetDeviceSessionRequest(proto.Message):
    r"""Request message for DirectAccessService.GetDeviceSession.

    Attributes:
        name (str):
            Required. Name of the DeviceSession, e.g.
            "projects/{project_id}/deviceSessions/{session_id}".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CancelDeviceSessionRequest(proto.Message):
    r"""Request message for DirectAccessService.CancelDeviceSession.

    Attributes:
        name (str):
            Required. Name of the DeviceSession, e.g.
            "projects/{project_id}/deviceSessions/{session_id}".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateDeviceSessionRequest(proto.Message):
    r"""Request message for DirectAccessService.UpdateDeviceSession.

    Attributes:
        device_session (google.cloud.devicestreaming_v1.types.DeviceSession):
            Required. DeviceSession to update. The DeviceSession's
            ``name`` field is used to identify the session to update
            "projects/{project_id}/deviceSessions/{session_id}".
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    device_session: "DeviceSession" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="DeviceSession",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeviceSession(proto.Message):
    r"""Protobuf message describing the device message, used from
    several RPCs.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Optional. Name of the DeviceSession, e.g.
            "projects/{project_id}/deviceSessions/{session_id}".
        display_name (str):
            Output only. The title of the DeviceSession
            to be presented in the UI.
        state (google.cloud.devicestreaming_v1.types.DeviceSession.SessionState):
            Output only. Current state of the
            DeviceSession.
        state_histories (MutableSequence[google.cloud.devicestreaming_v1.types.DeviceSession.SessionStateEvent]):
            Output only. The historical state transitions of the
            session_state message including the current session state.
        ttl (google.protobuf.duration_pb2.Duration):
            Optional. The amount of time that a device
            will be initially allocated for. This can
            eventually be extended with the
            UpdateDeviceSession RPC. Default: 15 minutes.

            This field is a member of `oneof`_ ``expiration``.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. If the device is still in use at
            this time, any connections will be ended and the
            SessionState will transition from ACTIVE to
            FINISHED.

            This field is a member of `oneof`_ ``expiration``.
        inactivity_timeout (google.protobuf.duration_pb2.Duration):
            Output only. The interval of time that this device must be
            interacted with before it transitions from ACTIVE to
            TIMEOUT_INACTIVITY.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time that the Session was
            created.
        active_start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp that the session
            first became ACTIVE.
        android_device (google.cloud.devicestreaming_v1.types.AndroidDevice):
            Required. The requested device.
        client_info (google.cloud.devicestreaming_v1.types.ClientInfo):
            Optional. Information about the client which
            invoked the device session.
    """

    class SessionState(proto.Enum):
        r"""The state that the DeviceSession resides.

        Values:
            SESSION_STATE_UNSPECIFIED (0):
                Default value. This value is unused.
            REQUESTED (1):
                Initial state of a session request. The
                session is being validated for correctness and a
                device is not yet requested.
            PENDING (2):
                The session has been validated and is in the
                queue for a device.
            ACTIVE (3):
                The session has been granted and the device
                is accepting connections.
            EXPIRED (4):
                The session duration exceeded the device's
                reservation time period and timed out
                automatically.
            FINISHED (5):
                The user is finished with the session and it
                was canceled by the user while the request was
                still getting allocated or after allocation and
                during device usage period.
            UNAVAILABLE (6):
                Unable to complete the session because the
                device was unavailable and it failed to allocate
                through the scheduler. For example, a device not
                in the catalog was requested or the request
                expired in the allocation queue.
            ERROR (7):
                Unable to complete the session for an
                internal reason, such as an infrastructure
                failure.
        """

        SESSION_STATE_UNSPECIFIED = 0
        REQUESTED = 1
        PENDING = 2
        ACTIVE = 3
        EXPIRED = 4
        FINISHED = 5
        UNAVAILABLE = 6
        ERROR = 7

    class SessionStateEvent(proto.Message):
        r"""A message encapsulating a series of Session states and the
        time that the DeviceSession first entered those states.

        Attributes:
            session_state (google.cloud.devicestreaming_v1.types.DeviceSession.SessionState):
                Output only. The session_state tracked by this event
            event_time (google.protobuf.timestamp_pb2.Timestamp):
                Output only. The time that the session_state first
                encountered that state.
            state_message (str):
                Output only. A human-readable message to
                explain the state.
        """

        session_state: "DeviceSession.SessionState" = proto.Field(
            proto.ENUM,
            number=1,
            enum="DeviceSession.SessionState",
        )
        event_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=2,
            message=timestamp_pb2.Timestamp,
        )
        state_message: str = proto.Field(
            proto.STRING,
            number=3,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    state: SessionState = proto.Field(
        proto.ENUM,
        number=3,
        enum=SessionState,
    )
    state_histories: MutableSequence[SessionStateEvent] = proto.RepeatedField(
        proto.MESSAGE,
        number=14,
        message=SessionStateEvent,
    )
    ttl: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="expiration",
        message=duration_pb2.Duration,
    )
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="expiration",
        message=timestamp_pb2.Timestamp,
    )
    inactivity_timeout: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=7,
        message=duration_pb2.Duration,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    active_start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    android_device: "AndroidDevice" = proto.Field(
        proto.MESSAGE,
        number=15,
        message="AndroidDevice",
    )
    client_info: "ClientInfo" = proto.Field(
        proto.MESSAGE,
        number=21,
        message="ClientInfo",
    )


class ClientInfo(proto.Message):
    r"""Information about the client which invoked the device
    session.

    Attributes:
        client (str):
            Required. Client name, such as gcloud. The
            maximum length is 64 characters.
        version (str):
            Optional. Client version. The maximum length
            is 64 characters.
    """

    client: str = proto.Field(
        proto.STRING,
        number=1,
    )
    version: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AndroidDevice(proto.Message):
    r"""A single Android device.

    Attributes:
        android_model_id (str):
            Required. The id of the Android device to be
            used. Use the TestEnvironmentDiscoveryService to
            get supported options.
        android_version_id (str):
            Required. The id of the Android OS version to
            be used. Use the TestEnvironmentDiscoveryService
            to get supported options.
        locale (str):
            Optional. The locale the test device used for
            testing. Use the TestEnvironmentDiscoveryService
            to get supported options.
        orientation (str):
            Optional. How the device is oriented during
            the test. Use the
            TestEnvironmentDiscoveryService to get supported
            options.
    """

    android_model_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    android_version_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    locale: str = proto.Field(
        proto.STRING,
        number=3,
    )
    orientation: str = proto.Field(
        proto.STRING,
        number=4,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
