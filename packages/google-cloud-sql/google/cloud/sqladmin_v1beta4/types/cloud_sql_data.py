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

import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.sql.v1beta4",
    manifest={
        "SqlDataFeature",
        "StreamSqlDataRequest",
        "StartSession",
        "ContinueSession",
        "StreamSqlDataResponse",
        "SessionMetadata",
        "DataPacket",
        "Ack",
        "TerminateSession",
    },
)


class SqlDataFeature(proto.Enum):
    r"""The session features. The server must send the supported
    features in its first message to the client.

    Values:
        SQL_DATA_FEATURE_UNSPECIFIED (0):
            The feature is not specified. This value
            should not be used.
        SQL_DATA_FEATURE_RECONNECT (1):
            The server supports reconnecting to the
            session. If this feature is not present, the
            client should not attempt to reconnect to the
            session.
    """

    SQL_DATA_FEATURE_UNSPECIFIED = 0
    SQL_DATA_FEATURE_RECONNECT = 1


class StreamSqlDataRequest(proto.Message):
    r"""Message sent from the client to ``SqlDataService``.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        ack (google.cloud.sqladmin_v1beta4.types.Ack):
            Optional. Acknowledges data received by the
            client.
        start_session (google.cloud.sqladmin_v1beta4.types.StartSession):
            Starts a new session. When starting a new
            session, this is the first message the client
            sends.

            This field is a member of `oneof`_ ``message``.
        continue_session (google.cloud.sqladmin_v1beta4.types.ContinueSession):
            Continues an existing session. When
            continuing an existing session, this is the
            first message the client sends.

            This field is a member of `oneof`_ ``message``.
        data (google.cloud.sqladmin_v1beta4.types.DataPacket):
            Database data.

            This field is a member of `oneof`_ ``message``.
        terminate_session (google.cloud.sqladmin_v1beta4.types.TerminateSession):
            Terminates the session. This closes the
            connection to the database.

            This field is a member of `oneof`_ ``message``.
        instance_id (str):
            Optional. Deprecated: Use ``StartSession.instance_id`` or
            ``ContinueSession.instance_id`` instead. The Cloud SQL
            instance resource name, for example:
            projects/example-project/instances/example-instance
    """

    ack: "Ack" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="Ack",
    )
    start_session: "StartSession" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="message",
        message="StartSession",
    )
    continue_session: "ContinueSession" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="message",
        message="ContinueSession",
    )
    data: "DataPacket" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="message",
        message="DataPacket",
    )
    terminate_session: "TerminateSession" = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="message",
        message="TerminateSession",
    )
    instance_id: str = proto.Field(
        proto.STRING,
        number=9,
    )


class StartSession(proto.Message):
    r"""Start a new session. The client must send this as the first
    message to the server to start a new session. The client may
    immediately send Data messages without waiting for a reply from
    the server.

    Attributes:
        location_id (str):
            Required. ``location_id`` is used to route the request to a
            specific region. Use the same region which was used to
            create the instance. Use the format
            ``locations/{location}``, for example:
            ``locations/us-central1``.
        instance_id (str):
            Required. The Cloud SQL instance resource
            name, for example:
            projects/example-project/instances/example-instance
        session_id (str):
            Optional. The session id, chosen by the client. This should
            be an unguessable string. If the client does not intend to
            reconnect to this session, the client may leave session_id
            unset.
    """

    location_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    session_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ContinueSession(proto.Message):
    r"""Reconnects to an existing session. The client must send this
    as the first message to the server to reconnect to an existing
    session. The client may immediately send Data messages without
    waiting for a reply from the server.

    Attributes:
        location_id (str):
            Required. ``location_id`` is used to route the request to a
            specific region. Use the same region which was used to
            create the instance. Use the format
            ``locations/{location}``, for example:
            ``locations/us-central1``.
        instance_id (str):
            Required. The Cloud SQL instance resource
            name, for example:
            projects/example-project/instances/example-instance
        session_id (str):
            Required. The id of the session to reconnect.
    """

    location_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    session_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class StreamSqlDataResponse(proto.Message):
    r"""Message sent from SqlDataService back to the client.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        ack (google.cloud.sqladmin_v1beta4.types.Ack):
            Acknowledges data received by the server.
        session_metadata (google.cloud.sqladmin_v1beta4.types.SessionMetadata):
            The first message from the server to the
            client, containing metadata about this session.

            This field is a member of `oneof`_ ``message``.
        data (google.cloud.sqladmin_v1beta4.types.DataPacket):
            Data from the database.

            This field is a member of `oneof`_ ``message``.
        terminate_session (google.cloud.sqladmin_v1beta4.types.TerminateSession):
            Terminates the session. This indicates that
            the database connection is closed. When the
            client receives this message, it should not
            attempt to reconnect.

            This field is a member of `oneof`_ ``message``.
    """

    ack: "Ack" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Ack",
    )
    session_metadata: "SessionMetadata" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="message",
        message="SessionMetadata",
    )
    data: "DataPacket" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="message",
        message="DataPacket",
    )
    terminate_session: "TerminateSession" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="message",
        message="TerminateSession",
    )


class SessionMetadata(proto.Message):
    r"""Metadata from the server to the client about the session. The
    server will always send this as the first message

    Attributes:
        supported_features (MutableSequence[google.cloud.sqladmin_v1beta4.types.SqlDataFeature]):
            The features supported by the server for this
            session. This field is used by the client to
            determine which features are available on the
            server. The features supported by the server for
            this session.
    """

    supported_features: MutableSequence["SqlDataFeature"] = proto.RepeatedField(
        proto.ENUM,
        number=1,
        enum="SqlDataFeature",
    )


class DataPacket(proto.Message):
    r"""Contains data being sent or received by the database.

    Attributes:
        first_byte_offset (int):
            Optional. The absolute byte offset of the
            first byte in this payload. 0 for new
            connections or resumed connections that hasn't
            acked any bytes from server. Non-zero for
            resumed connections
        data (bytes):
            Required. Raw data being sent or received by
            the database.
    """

    first_byte_offset: int = proto.Field(
        proto.INT64,
        number=1,
    )
    data: bytes = proto.Field(
        proto.BYTES,
        number=2,
    )


class Ack(proto.Message):
    r"""Acknowledges data received by the client or server.

    Attributes:
        received_offset (int):
            Required. The absolute number of bytes
            processed in the session.
    """

    received_offset: int = proto.Field(
        proto.INT64,
        number=1,
    )


class TerminateSession(proto.Message):
    r"""Indicates that the session is permanently ended.

    Attributes:
        status (google.rpc.status_pb2.Status):
            Required. The session termination status.
    """

    status: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=1,
        message=status_pb2.Status,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
