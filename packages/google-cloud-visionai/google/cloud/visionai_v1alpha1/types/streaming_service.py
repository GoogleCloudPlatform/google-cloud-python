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

from google.cloud.visionai_v1alpha1.types import streaming_resources

__protobuf__ = proto.module(
    package="google.cloud.visionai.v1alpha1",
    manifest={
        "LeaseType",
        "ReceiveEventsRequest",
        "EventUpdate",
        "ReceiveEventsControlResponse",
        "ReceiveEventsResponse",
        "Lease",
        "AcquireLeaseRequest",
        "RenewLeaseRequest",
        "ReleaseLeaseRequest",
        "ReleaseLeaseResponse",
        "RequestMetadata",
        "SendPacketsRequest",
        "SendPacketsResponse",
        "ReceivePacketsRequest",
        "ReceivePacketsControlResponse",
        "ReceivePacketsResponse",
        "EagerMode",
        "ControlledMode",
        "CommitRequest",
    },
)


class LeaseType(proto.Enum):
    r"""The lease type.

    Values:
        LEASE_TYPE_UNSPECIFIED (0):
            Lease type unspecified.
        LEASE_TYPE_READER (1):
            Lease for stream reader.
        LEASE_TYPE_WRITER (2):
            Lease for stream writer.
    """

    LEASE_TYPE_UNSPECIFIED = 0
    LEASE_TYPE_READER = 1
    LEASE_TYPE_WRITER = 2


class ReceiveEventsRequest(proto.Message):
    r"""Request message for ReceiveEvents.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        setup_request (google.cloud.visionai_v1alpha1.types.ReceiveEventsRequest.SetupRequest):
            The setup request to setup the RPC
            connection.

            This field is a member of `oneof`_ ``request``.
        commit_request (google.cloud.visionai_v1alpha1.types.CommitRequest):
            This request checkpoints the consumer's read
            progress.

            This field is a member of `oneof`_ ``request``.
    """

    class SetupRequest(proto.Message):
        r"""SetupRequest is the first message sent to the service to
        setup the RPC connection.

        Attributes:
            cluster (str):
                The cluster name.
            stream (str):
                The stream name. The service will return the
                events for the given stream.
            receiver (str):
                A name for the receiver to self-identify.

                This is used to keep track of a receiver's read
                progress.
            controlled_mode (google.cloud.visionai_v1alpha1.types.ControlledMode):
                Controller mode configuration for receiving
                events from the server.
            heartbeat_interval (google.protobuf.duration_pb2.Duration):
                The maximum duration of server silence before the client
                determines the server unreachable.

                The client must either receive an ``Event`` update or a
                heart beat message before this duration expires; otherwise,
                the client will automatically cancel the current connection
                and retry.
            writes_done_grace_period (google.protobuf.duration_pb2.Duration):
                The grace period after which a ``writes_done_request`` is
                issued, that a ``WritesDone`` is expected from the client.

                The server is free to cancel the RPC should this expire.

                A system default will be chosen if unset.
        """

        cluster: str = proto.Field(
            proto.STRING,
            number=1,
        )
        stream: str = proto.Field(
            proto.STRING,
            number=2,
        )
        receiver: str = proto.Field(
            proto.STRING,
            number=3,
        )
        controlled_mode: "ControlledMode" = proto.Field(
            proto.MESSAGE,
            number=4,
            message="ControlledMode",
        )
        heartbeat_interval: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=5,
            message=duration_pb2.Duration,
        )
        writes_done_grace_period: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=6,
            message=duration_pb2.Duration,
        )

    setup_request: SetupRequest = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="request",
        message=SetupRequest,
    )
    commit_request: "CommitRequest" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="request",
        message="CommitRequest",
    )


class EventUpdate(proto.Message):
    r"""The event update message.

    Attributes:
        stream (str):
            The name of the stream that the event is
            attached to.
        event (str):
            The name of the event.
        series (str):
            The name of the series.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            The timestamp when the Event update happens.
        offset (int):
            The offset of the message that will be used
            to acknowledge of the message receiving.
    """

    stream: str = proto.Field(
        proto.STRING,
        number=1,
    )
    event: str = proto.Field(
        proto.STRING,
        number=2,
    )
    series: str = proto.Field(
        proto.STRING,
        number=3,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    offset: int = proto.Field(
        proto.INT64,
        number=5,
    )


class ReceiveEventsControlResponse(proto.Message):
    r"""Control message for a ReceiveEventsResponse.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        heartbeat (bool):
            A server heartbeat.

            This field is a member of `oneof`_ ``control``.
        writes_done_request (bool):
            A request to the receiver to complete any final writes
            followed by a ``WritesDone``; e.g. issue any final
            ``CommitRequest``\ s.

            May be ignored if ``WritesDone`` has already been issued at
            any point prior to receiving this message.

            If ``WritesDone`` does not get issued, then the server will
            forcefully cancel the connection, and the receiver will
            likely receive an uninformative after ``Read`` returns
            ``false`` and ``Finish`` is called.

            This field is a member of `oneof`_ ``control``.
    """

    heartbeat: bool = proto.Field(
        proto.BOOL,
        number=1,
        oneof="control",
    )
    writes_done_request: bool = proto.Field(
        proto.BOOL,
        number=2,
        oneof="control",
    )


class ReceiveEventsResponse(proto.Message):
    r"""Response message for the ReceiveEvents.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        event_update (google.cloud.visionai_v1alpha1.types.EventUpdate):
            The event update message.

            This field is a member of `oneof`_ ``response``.
        control (google.cloud.visionai_v1alpha1.types.ReceiveEventsControlResponse):
            A control message from the server.

            This field is a member of `oneof`_ ``response``.
    """

    event_update: "EventUpdate" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="response",
        message="EventUpdate",
    )
    control: "ReceiveEventsControlResponse" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="response",
        message="ReceiveEventsControlResponse",
    )


class Lease(proto.Message):
    r"""The lease message.

    Attributes:
        id (str):
            The lease id.
        series (str):
            The series name.
        owner (str):
            The owner name.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            The lease expire time.
        lease_type (google.cloud.visionai_v1alpha1.types.LeaseType):
            The lease type.
    """

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    series: str = proto.Field(
        proto.STRING,
        number=2,
    )
    owner: str = proto.Field(
        proto.STRING,
        number=3,
    )
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    lease_type: "LeaseType" = proto.Field(
        proto.ENUM,
        number=5,
        enum="LeaseType",
    )


class AcquireLeaseRequest(proto.Message):
    r"""Request message for acquiring a lease.

    Attributes:
        series (str):
            The series name.
        owner (str):
            The owner name.
        term (google.protobuf.duration_pb2.Duration):
            The lease term.
        lease_type (google.cloud.visionai_v1alpha1.types.LeaseType):
            The lease type.
    """

    series: str = proto.Field(
        proto.STRING,
        number=1,
    )
    owner: str = proto.Field(
        proto.STRING,
        number=2,
    )
    term: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=3,
        message=duration_pb2.Duration,
    )
    lease_type: "LeaseType" = proto.Field(
        proto.ENUM,
        number=4,
        enum="LeaseType",
    )


class RenewLeaseRequest(proto.Message):
    r"""Request message for renewing a lease.

    Attributes:
        id (str):
            Lease id.
        series (str):
            Series name.
        owner (str):
            Lease owner.
        term (google.protobuf.duration_pb2.Duration):
            Lease term.
    """

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    series: str = proto.Field(
        proto.STRING,
        number=2,
    )
    owner: str = proto.Field(
        proto.STRING,
        number=3,
    )
    term: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=4,
        message=duration_pb2.Duration,
    )


class ReleaseLeaseRequest(proto.Message):
    r"""Request message for releasing lease.

    Attributes:
        id (str):
            Lease id.
        series (str):
            Series name.
        owner (str):
            Lease owner.
    """

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    series: str = proto.Field(
        proto.STRING,
        number=2,
    )
    owner: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ReleaseLeaseResponse(proto.Message):
    r"""Response message for release lease."""


class RequestMetadata(proto.Message):
    r"""RequestMetadata is the metadata message for the request.

    Attributes:
        stream (str):
            Stream name.
        event (str):
            Evevt name.
        series (str):
            Series name.
        lease_id (str):
            Lease id.
        owner (str):
            Owner name.
        lease_term (google.protobuf.duration_pb2.Duration):
            Lease term specifies how long the client
            wants the session to be maintained by the server
            after the client leaves. If the lease term is
            not set, the server will release the session
            immediately and the client cannot reconnect to
            the same session later.
    """

    stream: str = proto.Field(
        proto.STRING,
        number=1,
    )
    event: str = proto.Field(
        proto.STRING,
        number=2,
    )
    series: str = proto.Field(
        proto.STRING,
        number=3,
    )
    lease_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    owner: str = proto.Field(
        proto.STRING,
        number=5,
    )
    lease_term: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=6,
        message=duration_pb2.Duration,
    )


class SendPacketsRequest(proto.Message):
    r"""Request message for sending packets.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        packet (google.cloud.visionai_v1alpha1.types.Packet):
            Packets sent over the streaming rpc.

            This field is a member of `oneof`_ ``request``.
        metadata (google.cloud.visionai_v1alpha1.types.RequestMetadata):
            The first message of the streaming rpc
            including the request metadata.

            This field is a member of `oneof`_ ``request``.
    """

    packet: streaming_resources.Packet = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="request",
        message=streaming_resources.Packet,
    )
    metadata: "RequestMetadata" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="request",
        message="RequestMetadata",
    )


class SendPacketsResponse(proto.Message):
    r"""Response message for sending packets."""


class ReceivePacketsRequest(proto.Message):
    r"""Request message for receiving packets.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        setup_request (google.cloud.visionai_v1alpha1.types.ReceivePacketsRequest.SetupRequest):
            The request to setup the initial state of
            session.
            The client must send and only send this as the
            first message.

            This field is a member of `oneof`_ ``request``.
        commit_request (google.cloud.visionai_v1alpha1.types.CommitRequest):
            This request checkpoints the consumer's read
            progress.

            This field is a member of `oneof`_ ``request``.
    """

    class SetupRequest(proto.Message):
        r"""The message specifying the initial settings for the
        ReceivePackets session.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            eager_receive_mode (google.cloud.visionai_v1alpha1.types.EagerMode):
                Options for configuring eager mode.

                This field is a member of `oneof`_ ``consumer_mode``.
            controlled_receive_mode (google.cloud.visionai_v1alpha1.types.ControlledMode):
                Options for configuring controlled mode.

                This field is a member of `oneof`_ ``consumer_mode``.
            metadata (google.cloud.visionai_v1alpha1.types.RequestMetadata):
                The configurations that specify where packets
                are retrieved.
            receiver (str):
                A name for the receiver to self-identify.

                This is used to keep track of a receiver's read
                progress.
            heartbeat_interval (google.protobuf.duration_pb2.Duration):
                The maximum duration of server silence before the client
                determines the server unreachable.

                The client must either receive a ``Packet`` or a heart beat
                message before this duration expires; otherwise, the client
                will automatically cancel the current connection and retry.
            writes_done_grace_period (google.protobuf.duration_pb2.Duration):
                The grace period after which a ``writes_done_request`` is
                issued, that a ``WritesDone`` is expected from the client.

                The server is free to cancel the RPC should this expire.

                A system default will be chosen if unset.
        """

        eager_receive_mode: "EagerMode" = proto.Field(
            proto.MESSAGE,
            number=3,
            oneof="consumer_mode",
            message="EagerMode",
        )
        controlled_receive_mode: "ControlledMode" = proto.Field(
            proto.MESSAGE,
            number=4,
            oneof="consumer_mode",
            message="ControlledMode",
        )
        metadata: "RequestMetadata" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="RequestMetadata",
        )
        receiver: str = proto.Field(
            proto.STRING,
            number=2,
        )
        heartbeat_interval: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=5,
            message=duration_pb2.Duration,
        )
        writes_done_grace_period: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=6,
            message=duration_pb2.Duration,
        )

    setup_request: SetupRequest = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="request",
        message=SetupRequest,
    )
    commit_request: "CommitRequest" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="request",
        message="CommitRequest",
    )


class ReceivePacketsControlResponse(proto.Message):
    r"""Control message for a ReceivePacketsResponse.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        heartbeat (bool):
            A server heartbeat.

            This field is a member of `oneof`_ ``control``.
        writes_done_request (bool):
            A request to the receiver to complete any final writes
            followed by a ``WritesDone``; e.g. issue any final
            ``CommitRequest``\ s.

            May be ignored if ``WritesDone`` has already been issued at
            any point prior to receiving this message.

            If ``WritesDone`` does not get issued, then the server will
            forcefully cancel the connection, and the receiver will
            likely receive an uninformative after ``Read`` returns
            ``false`` and ``Finish`` is called.

            This field is a member of `oneof`_ ``control``.
    """

    heartbeat: bool = proto.Field(
        proto.BOOL,
        number=1,
        oneof="control",
    )
    writes_done_request: bool = proto.Field(
        proto.BOOL,
        number=2,
        oneof="control",
    )


class ReceivePacketsResponse(proto.Message):
    r"""Response message from ReceivePackets.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        packet (google.cloud.visionai_v1alpha1.types.Packet):
            A genuine data payload originating from the
            sender.

            This field is a member of `oneof`_ ``response``.
        control (google.cloud.visionai_v1alpha1.types.ReceivePacketsControlResponse):
            A control message from the server.

            This field is a member of `oneof`_ ``response``.
    """

    packet: streaming_resources.Packet = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="response",
        message=streaming_resources.Packet,
    )
    control: "ReceivePacketsControlResponse" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="response",
        message="ReceivePacketsControlResponse",
    )


class EagerMode(proto.Message):
    r"""The options for receiver under the eager mode."""


class ControlledMode(proto.Message):
    r"""The options for receiver under the controlled mode.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        starting_logical_offset (str):
            This can be set to the following logical
            starting points:
            "begin": This will read from the earliest
            available message.

            "most-recent": This will read from the latest
            available message.

            "end": This will read only future messages.

            "stored": This will resume reads one past the
            last committed offset.           It is the only
            option that resumes progress; all others
            jump unilaterally.

            This field is a member of `oneof`_ ``starting_offset``.
        fallback_starting_offset (str):
            This is the logical starting point to
            fallback upon should the specified starting
            offset be unavailable.

            This can be one of the following values:

            "begin": This will read from the earliest
            available message.

            "end": This will read only future messages.
    """

    starting_logical_offset: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="starting_offset",
    )
    fallback_starting_offset: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CommitRequest(proto.Message):
    r"""The message for explicitly committing the read progress.

    This may only be used when ``ReceivePacketsControlledMode`` is set
    in the initial setup request.

    Attributes:
        offset (int):
            The offset to commit.
    """

    offset: int = proto.Field(
        proto.INT64,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
