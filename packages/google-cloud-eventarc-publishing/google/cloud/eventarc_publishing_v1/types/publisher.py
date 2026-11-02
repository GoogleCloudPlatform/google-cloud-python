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

import google.protobuf.any_pb2 as any_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.eventarc_publishing_v1.types import cloud_event

__protobuf__ = proto.module(
    package="google.cloud.eventarc.publishing.v1",
    manifest={
        "PublishChannelConnectionEventsRequest",
        "PublishChannelConnectionEventsResponse",
        "PublishEventsRequest",
        "PublishEventsResponse",
        "PublishRequest",
        "PublishResponse",
    },
)


class PublishChannelConnectionEventsRequest(proto.Message):
    r"""The request message for the PublishChannelConnectionEvents
    method.

    Attributes:
        channel_connection (str):
            The channel_connection that the events are published from.
            For example:
            ``projects/{partner_project_id}/locations/{location}/channelConnections/{channel_connection_id}``.
        events (MutableSequence[google.protobuf.any_pb2.Any]):
            The CloudEvents v1.0 events to publish. No other types are
            allowed. If this field is set, then the ``text_events``
            fields must not be set.
        text_events (MutableSequence[str]):
            The text representation of events to publish. CloudEvent
            v1.0 in JSON format is the only allowed type. Refer to
            https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/formats/json-format.md
            for specification. If this field is set, then the ``events``
            fields must not be set.
    """

    channel_connection: str = proto.Field(
        proto.STRING,
        number=1,
    )
    events: MutableSequence[any_pb2.Any] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=any_pb2.Any,
    )
    text_events: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class PublishChannelConnectionEventsResponse(proto.Message):
    r"""The response message for the PublishChannelConnectionEvents
    method.

    """


class PublishEventsRequest(proto.Message):
    r"""The request message for the PublishEvents method.

    Attributes:
        channel (str):
            The full name of the channel to publish to. For example:
            ``projects/{project}/locations/{location}/channels/{channel-id}``.
        events (MutableSequence[google.protobuf.any_pb2.Any]):
            The CloudEvents v1.0 events to publish. No other types are
            allowed. If this field is set, then the ``text_events``
            fields must not be set.
        text_events (MutableSequence[str]):
            The text representation of events to publish. CloudEvent
            v1.0 in JSON format is the only allowed type. Refer to
            https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/formats/json-format.md
            for specification. If this field is set, then the ``events``
            fields must not be set.
    """

    channel: str = proto.Field(
        proto.STRING,
        number=1,
    )
    events: MutableSequence[any_pb2.Any] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=any_pb2.Any,
    )
    text_events: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class PublishEventsResponse(proto.Message):
    r"""The response message for the PublishEvents method."""


class PublishRequest(proto.Message):
    r"""The request message for the Publish method.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        message_bus (str):
            Required. The full name of the message bus to publish events
            to. Format:
            ``projects/{project}/locations/{location}/messageBuses/{messageBus}``.
        proto_message (google.cloud.eventarc_publishing_v1.types.CloudEvent):
            The Protobuf format of the CloudEvent being
            published. Specification can be found here:

            https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/formats/protobuf-format.md

            This field is a member of `oneof`_ ``format``.
        json_message (str):
            The JSON format of the CloudEvent being
            published. Specification can be found here:

            https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/formats/json-format.md

            This field is a member of `oneof`_ ``format``.
        avro_message (bytes):
            The Avro format of the CloudEvent being
            published. Specification can be found here:

            https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/formats/avro-format.md

            This field is a member of `oneof`_ ``format``.
    """

    message_bus: str = proto.Field(
        proto.STRING,
        number=1,
    )
    proto_message: cloud_event.CloudEvent = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="format",
        message=cloud_event.CloudEvent,
    )
    json_message: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="format",
    )
    avro_message: bytes = proto.Field(
        proto.BYTES,
        number=4,
        oneof="format",
    )


class PublishResponse(proto.Message):
    r"""The response message for the Publish method."""


__all__ = tuple(sorted(__protobuf__.manifest))
