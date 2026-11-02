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

from google.cloud.dialogflow_v2beta1.types import participant, session

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.v2beta1",
    manifest={
        "ConversationEvent",
    },
)


class ConversationEvent(proto.Message):
    r"""Represents a notification sent to Pub/Sub subscribers for
    conversation lifecycle events.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        conversation (str):
            Required. The unique identifier of the conversation this
            notification refers to. Format:
            ``projects/<Project ID>/conversations/<Conversation ID>``.
        type_ (google.cloud.dialogflow_v2beta1.types.ConversationEvent.Type):
            Required. The type of the event that this
            notification refers to.
        error_status (google.rpc.status_pb2.Status):
            Optional. More detailed information about an error. Only set
            for type UNRECOVERABLE_ERROR_IN_PHONE_CALL.
        new_message_payload (google.cloud.dialogflow_v2beta1.types.Message):
            Payload of NEW_MESSAGE event.

            This field is a member of `oneof`_ ``payload``.
        new_recognition_result_payload (google.cloud.dialogflow_v2beta1.types.StreamingRecognitionResult):
            Payload of NEW_RECOGNITION_RESULT event.

            This field is a member of `oneof`_ ``payload``.
    """

    class Type(proto.Enum):
        r"""Enumeration of the types of events available.

        Values:
            TYPE_UNSPECIFIED (0):
                Type not set.
            CONVERSATION_STARTED (1):
                A new conversation has been opened. This is
                fired when a telephone call is answered, or a
                conversation is created via the API.
            CONVERSATION_FINISHED (2):
                An existing conversation has closed. This is
                fired when a telephone call is terminated, or a
                conversation is closed via the API. The event is
                fired for every CompleteConversation call, even
                if the conversation is already closed.
            HUMAN_INTERVENTION_NEEDED (3):
                An existing conversation has received
                notification from Dialogflow that human
                intervention is required.
            NEW_MESSAGE (5):
                An existing conversation has received a new message, either
                from API or telephony. It is configured in
                [ConversationProfile.new_message_event_notification_config][google.cloud.dialogflow.v2beta1.ConversationProfile.new_message_event_notification_config]
            NEW_RECOGNITION_RESULT (7):
                An existing conversation has received a new speech
                recognition result. This is mainly for delivering
                intermediate transcripts. The notification is configured in
                [ConversationProfile.new_recognition_event_notification_config][].
            UNRECOVERABLE_ERROR (4):
                Unrecoverable error during a telephone call.

                In general non-recoverable errors only occur if something
                was misconfigured in the ConversationProfile corresponding
                to the call. After a non-recoverable error, Dialogflow may
                stop responding.

                We don't fire this event:

                - in an API call because we can directly return the error,
                  or,
                - when we can recover from an error.
        """

        TYPE_UNSPECIFIED = 0
        CONVERSATION_STARTED = 1
        CONVERSATION_FINISHED = 2
        HUMAN_INTERVENTION_NEEDED = 3
        NEW_MESSAGE = 5
        NEW_RECOGNITION_RESULT = 7
        UNRECOVERABLE_ERROR = 4

    conversation: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=2,
        enum=Type,
    )
    error_status: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=3,
        message=status_pb2.Status,
    )
    new_message_payload: participant.Message = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="payload",
        message=participant.Message,
    )
    new_recognition_result_payload: session.StreamingRecognitionResult = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="payload",
        message=session.StreamingRecognitionResult,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
