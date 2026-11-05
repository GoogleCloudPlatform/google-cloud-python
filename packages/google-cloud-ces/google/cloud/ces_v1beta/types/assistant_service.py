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

import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.ces_v1beta.types import common

__protobuf__ = proto.module(
    package="google.cloud.ces.v1beta",
    manifest={
        "AssistantSessionState",
        "ListAssistantSessionsRequest",
        "ListAssistantSessionsResponse",
        "GetAssistantSessionRequest",
        "CreateAssistantSessionRequest",
        "DeleteAssistantSessionRequest",
        "RunAssistantRequest",
        "RunAssistantResponse",
        "AssistantSession",
        "ActiveTurnInfo",
        "AssistantSessionArtifact",
        "AssistantChunk",
        "AssistantOutput",
        "AssistantMessage",
        "TypedPayload",
        "UserResponseSuggestions",
        "ChatAiAssistantRequest",
        "ChatAiAssistantResponse",
    },
)


class AssistantSessionState(proto.Enum):
    r"""The status of the assistant session.

    Values:
        ASSISTANT_SESSION_STATE_UNSPECIFIED (0):
            The default value. This value is used if the
            status is not specified.
        PROCESSING (1):
            The assistant agent is processing the request
            as a long running task.
        IDLE (2):
            The assistant agent is idle and does not have
            any pending requests or response.
        PENDING_REVIEW (3):
            The assistant agent is done processing a long
            running task and has a response ready for the
            user.
    """

    ASSISTANT_SESSION_STATE_UNSPECIFIED = 0
    PROCESSING = 1
    IDLE = 2
    PENDING_REVIEW = 3


class ListAssistantSessionsRequest(proto.Message):
    r"""Request message for
    [AssistantService.ListAssistantSessions][google.cloud.ces.v1beta.AssistantService.ListAssistantSessions].

    Attributes:
        parent (str):
            Required. The app to list assistant sessions from. Format:
            ``projects/{project}/locations/{location}/apps/{app}``
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. The
            [next_page_token][google.cloud.ces.v1beta.ListAssistantSessionsResponse.next_page_token]
            value returned from a previous list
            [AssistantService.ListAssistantSessions][google.cloud.ces.v1beta.AssistantService.ListAssistantSessions]
            call.
        filter (str):
            Optional. Filter to be applied when listing
            the assistant sessions. See
            https://google.aip.dev/160 for more details.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListAssistantSessionsResponse(proto.Message):
    r"""Response message for
    [AssistantService.ListAssistantSessions][google.cloud.ces.v1beta.AssistantService.ListAssistantSessions].

    Attributes:
        assistant_sessions (MutableSequence[google.cloud.ces_v1beta.types.AssistantSession]):
            The list of assistant sessions.
        next_page_token (str):
            Optional. A token that can be sent as
            [ListAssistantSessionsRequest.page_token][google.cloud.ces.v1beta.ListAssistantSessionsRequest.page_token]
            to retrieve the next page. Absence of this field indicates
            there are no subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    assistant_sessions: MutableSequence["AssistantSession"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AssistantSession",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetAssistantSessionRequest(proto.Message):
    r"""Request message for
    [AssistantService.GetAssistantSession][google.cloud.ces.v1beta.AssistantService.GetAssistantSession].

    Attributes:
        name (str):
            Required. The name of the assistant session to retrieve.
            Format:
            ``projects/{project}/locations/{location}/apps/{app}/assistantSessions/{assistant_session}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateAssistantSessionRequest(proto.Message):
    r"""Request message for
    [AssistantService.CreateAssistantSession][google.cloud.ces.v1beta.AssistantService.CreateAssistantSession].

    Attributes:
        parent (str):
            Required. The app to create the assistant session in Format:
            ``projects/{project}/locations/{location}/apps/{app}``
        assistant_session_id (str):
            Optional. The ID to use for the assistant
            session, which will become the final component
            of the assistant session's resource name. If not
            provided, a unique ID will be automatically
            assigned for the assistant session.
        assistant_session_messages (MutableSequence[google.cloud.ces_v1beta.types.AssistantMessage]):
            Optional. The messages to seed the assistant
            session with.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    assistant_session_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    assistant_session_messages: MutableSequence["AssistantMessage"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message="AssistantMessage",
        )
    )


class DeleteAssistantSessionRequest(proto.Message):
    r"""Request message for
    [AssistantService.DeleteAssistantSession][google.cloud.ces.v1beta.AssistantService.DeleteAssistantSession].

    Attributes:
        name (str):
            Required. The name of the assistant session to delete.
            Format:
            ``projects/{project}/locations/{location}/apps/{app}/assistantSessions/{assistant_session}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class RunAssistantRequest(proto.Message):
    r"""Request message for
    [AssistantService.RunAssistant][google.cloud.ces.v1beta.AssistantService.RunAssistant].

    Attributes:
        app (str):
            Required. The app to run assistant for. Format:
            ``projects/{project}/locations/{location}/apps/{app}``
        assistant_session (str):
            Required. The assistant session to be used to run the
            assistant. Format:
            ``projects/{project}/locations/{location}/apps/{app}/assistantSessions/{assistant_session}``
        message (google.cloud.ces_v1beta.types.AssistantMessage):
            Required. The message to send to the
            assistant agent.
        interaction_type (google.cloud.ces_v1beta.types.RunAssistantRequest.InteractionType):
            Optional. Different interaction types for the
            assistant message.
    """

    class InteractionType(proto.Enum):
        r"""The type of interaction for the message sent to the
        assistant.

        Values:
            INTERACTION_TYPE_UNSPECIFIED (0):
                The default value. This value is used if the
                type is not specified.
            NEW_MESSAGE (1):
                The message is a user input. User input is
                provided in the chunk list.
            POLL (2):
                The message is for polling the state of the
                assistant session.
            DISMISS (3):
                The message is to dismiss the assistant
                session pending review. This will change the
                state of the assistant session to idle.
        """

        INTERACTION_TYPE_UNSPECIFIED = 0
        NEW_MESSAGE = 1
        POLL = 2
        DISMISS = 3

    app: str = proto.Field(
        proto.STRING,
        number=1,
    )
    assistant_session: str = proto.Field(
        proto.STRING,
        number=2,
    )
    message: "AssistantMessage" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="AssistantMessage",
    )
    interaction_type: InteractionType = proto.Field(
        proto.ENUM,
        number=4,
        enum=InteractionType,
    )


class RunAssistantResponse(proto.Message):
    r"""Response message for
    [AssistantService.RunAssistant][google.cloud.ces.v1beta.AssistantService.RunAssistant].

    Attributes:
        output (google.cloud.ces_v1beta.types.AssistantOutput):
            Required. The output from the assistant
            agent.
        state (google.cloud.ces_v1beta.types.AssistantSessionState):
            Output only. The status of the assistant
            session.
    """

    output: "AssistantOutput" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="AssistantOutput",
    )
    state: "AssistantSessionState" = proto.Field(
        proto.ENUM,
        number=3,
        enum="AssistantSessionState",
    )


class AssistantSession(proto.Message):
    r"""An assistant session represents a conversation between a user
    and the assistant agent.

    Attributes:
        name (str):
            Required. Identifier. The unique identifier of the session.
            Format:
            ``projects/{project}/locations/{location}/apps/{app}/assistantSessions/{session}``
        requestor (str):
            Output only. The user who initiated the
            session.
        messages (MutableSequence[google.cloud.ces_v1beta.types.AssistantMessage]):
            Optional. History of messages in the session.
        state (google.cloud.ces_v1beta.types.AssistantSessionState):
            Output only. The status of the assistant
            session.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the assistant session
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the assistant session
            was last updated.
        user_response_suggestions (google.cloud.ces_v1beta.types.UserResponseSuggestions):
            Output only. Suggested user responses from
            the assistant agent.
        display_name (str):
            Optional. The display name of the assistant
            session.
        artifacts (MutableSequence[google.cloud.ces_v1beta.types.AssistantSessionArtifact]):
            Output only. Document artifacts (e.g.
            generated TDDs in markdown) produced by the
            assistant in this session. Pointers only; the
            file content lives in the customer's Cloud
            Storage bucket.
        session_checkpoint (google.cloud.ces_v1beta.types.SessionCheckpoint):
            Output only. Session checkpoint containing
            user intent and rolling history summary.
        active_turn (google.cloud.ces_v1beta.types.ActiveTurnInfo):
            Output only. Attachment info for this
            session's currently running turn. Unset when no
            turn is running.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requestor: str = proto.Field(
        proto.STRING,
        number=2,
    )
    messages: MutableSequence["AssistantMessage"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="AssistantMessage",
    )
    state: "AssistantSessionState" = proto.Field(
        proto.ENUM,
        number=4,
        enum="AssistantSessionState",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    user_response_suggestions: "UserResponseSuggestions" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="UserResponseSuggestions",
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=8,
    )
    artifacts: MutableSequence["AssistantSessionArtifact"] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message="AssistantSessionArtifact",
    )
    session_checkpoint: common.SessionCheckpoint = proto.Field(
        proto.MESSAGE,
        number=10,
        message=common.SessionCheckpoint,
    )
    active_turn: "ActiveTurnInfo" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="ActiveTurnInfo",
    )


class ActiveTurnInfo(proto.Message):
    r"""Live-attachment info for a session turn that is currently
    running, disconnected from its client, or parked for pickup by
    another server task.

    Attributes:
        turn_id (str):
            Identifies the turn; echoed by resume
            snapshots on the streaming API.
        status (google.cloud.ces_v1beta.types.ActiveTurnInfo.Status):
            Current attachment status.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. When the turn started.
        last_progress_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. When the turn last persisted
            progress.
        orphan_deadline_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. When the turn will be wound down
            if no client attaches.
    """

    class Status(proto.Enum):
        r"""How the running turn currently relates to clients and server
        tasks.

        Values:
            STATUS_UNSPECIFIED (0):
                Unspecified.
            RUNNING (1):
                The turn is executing with at least one
                client attached.
            DISCONNECTED (2):
                The turn is executing with no client
                attached.
            RESUMING (3):
                The turn is parked for pickup: the next
                attach continues it.
            ABANDONED (4):
                The turn's server lease has lapsed and no
                task is driving it; the next read seals it to a
                committed partial. Not attachable.
        """

        STATUS_UNSPECIFIED = 0
        RUNNING = 1
        DISCONNECTED = 2
        RESUMING = 3
        ABANDONED = 4

    turn_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    status: Status = proto.Field(
        proto.ENUM,
        number=2,
        enum=Status,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    last_progress_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    orphan_deadline_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )


class AssistantSessionArtifact(proto.Message):
    r"""A document artifact generated by the assistant within a
    session, stored as a file in the customer's Cloud Storage
    bucket.

    Attributes:
        id (str):
            Output only. The unique identifier of the
            artifact within the session.
        display_name (str):
            Output only. The file name shown to the user, e.g.
            "hotel_booking_tdd.md".
        gcs_uri (str):
            Output only. The Cloud Storage object holding the artifact
            content. Example:
            "gs://{project}-agent-assist-artifacts/agent-assist-generated/1_tdd.md".
        mime_type (str):
            Output only. The IANA media type of the
            artifact content, e.g. "text/markdown".
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. When the artifact was persisted.
        turn_index (int):
            Output only. Index of the message in
            [AssistantSession.messages] whose turn produced the
            artifact, for placing the artifact chip when history is
            restored.
    """

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    gcs_uri: str = proto.Field(
        proto.STRING,
        number=3,
    )
    mime_type: str = proto.Field(
        proto.STRING,
        number=4,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    turn_index: int = proto.Field(
        proto.INT32,
        number=6,
    )


class AssistantChunk(proto.Message):
    r"""A chunk of data in an assistant message.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        text (str):
            Optional. Text data.

            This field is a member of `oneof`_ ``data``.
        thought (str):
            Optional. Thought generated by the model.

            This field is a member of `oneof`_ ``data``.
        payload (google.protobuf.struct_pb2.Struct):
            Optional. Payload which contains structured
            responses like the quality report, agent version
            name, suggested responses etc.

            This field is a member of `oneof`_ ``data``.
        typed_payload (google.cloud.ces_v1beta.types.TypedPayload):
            Optional. Typed payload which contains
            structured responses.

            This field is a member of `oneof`_ ``data``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. Timestamp when the chunk was
            created or emitted.
    """

    text: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="data",
    )
    thought: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="data",
    )
    payload: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="data",
        message=struct_pb2.Struct,
    )
    typed_payload: "TypedPayload" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="data",
        message="TypedPayload",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )


class AssistantOutput(proto.Message):
    r"""The output from the assistant agent.

    Attributes:
        message (google.cloud.ces_v1beta.types.AssistantMessage):
            Required. The response from the assistant
            agent.
        user_response_suggestions (google.cloud.ces_v1beta.types.UserResponseSuggestions):
            Output only. Suggested user responses from
            the assistant agent.
    """

    message: "AssistantMessage" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="AssistantMessage",
    )
    user_response_suggestions: "UserResponseSuggestions" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="UserResponseSuggestions",
    )


class AssistantMessage(proto.Message):
    r"""A message in an assistant session.

    Attributes:
        role (str):
            Required. Role within the conversation "user"
            or  "model".
        chunks (MutableSequence[google.cloud.ces_v1beta.types.AssistantChunk]):
            Optional. Content of the message as chunks.
        event_time (google.protobuf.timestamp_pb2.Timestamp):
            Required. Timestamp when the message was sent
            or received.
        attached_gcs_uris (MutableSequence[str]):
            Optional. Cloud Storage URIs for files
            uploaded by the user during this turn. This
            allows attachments to be persisted and rendered
            in the session history UI. Example:
            "gs://cxas-transient-uploads/uuid/prd.pdf".
    """

    role: str = proto.Field(
        proto.STRING,
        number=1,
    )
    chunks: MutableSequence["AssistantChunk"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="AssistantChunk",
    )
    event_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    attached_gcs_uris: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )


class TypedPayload(proto.Message):
    r"""Payload with a type.

    Attributes:
        display_name (str):
            Required. The display name of the payload.
        type_ (str):
            Required. The type of the payload.
        value (google.protobuf.struct_pb2.Struct):
            Required. The value of the payload.
        metadata (google.protobuf.struct_pb2.Struct):
            Optional. The metadata of the payload.
    """

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=2,
    )
    value: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=3,
        message=struct_pb2.Struct,
    )
    metadata: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=4,
        message=struct_pb2.Struct,
    )


class UserResponseSuggestions(proto.Message):
    r"""Suggested user responses from the assistant agent.

    Attributes:
        suggestions (MutableSequence[str]):
            Required. The assistant suggested user
            responses. These are suggestions for the user on
            how to interact with the assistant.
    """

    suggestions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class ChatAiAssistantRequest(proto.Message):
    r"""Request message for
    [AssistantService.ChatAiAssistant][google.cloud.ces.v1beta.AssistantService.ChatAiAssistant].

    Attributes:
        app (str):
            Required. The app to run assistant for. Format:
            ``projects/{project}/locations/{location}/apps/{app}``
        assistant_session (str):
            Required. The assistant session to be used to run the
            assistant. Format:
            ``projects/{project}/locations/{location}/apps/{app}/assistantSessions/{assistant_session}``
        message (str):
            Required. The message to send to the
            assistant agent.
        attached_gcs_uris (MutableSequence[str]):
            Optional. Cloud Storage URIs for files
            uploaded by the user during this turn. Example:
            "gs://cxas-transient-uploads/uuid/prd.pdf".
        context_token (str):
            Optional. Opaque onboarding context token returned by
            [SessionService.GenerateOnboardingSuggestions][google.cloud.ces.v1beta.SessionService.GenerateOnboardingSuggestions].
            When set and still fresh, the server reuses the onboarding
            snapshot computed for the zero state instead of recomputing
            it for the first conversation turn.
    """

    app: str = proto.Field(
        proto.STRING,
        number=1,
    )
    assistant_session: str = proto.Field(
        proto.STRING,
        number=2,
    )
    message: str = proto.Field(
        proto.STRING,
        number=3,
    )
    attached_gcs_uris: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    context_token: str = proto.Field(
        proto.STRING,
        number=6,
    )


class ChatAiAssistantResponse(proto.Message):
    r"""Response message for
    [AssistantService.ChatAiAssistant][google.cloud.ces.v1beta.AssistantService.ChatAiAssistant].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        text_chunk (str):
            Text Token (for streaming Gemini responses
            word-by-word)

            This field is a member of `oneof`_ ``event``.
        status_message (str):
            Simple status update

            This field is a member of `oneof`_ ``event``.
        session_checkpoint (google.cloud.ces_v1beta.types.SessionCheckpoint):
            Session checkpoint/compaction recap event
            containing user intent and rolling summary.

            This field is a member of `oneof`_ ``event``.
        event_id (str):
            Unique identifier for the event.
        event_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp when the event occurred.
        ui_event (google.cloud.ces_v1beta.types.UiEvent):
            Optional. UI event payload.
    """

    text_chunk: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="event",
    )
    status_message: str = proto.Field(
        proto.STRING,
        number=4,
        oneof="event",
    )
    session_checkpoint: common.SessionCheckpoint = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="event",
        message=common.SessionCheckpoint,
    )
    event_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    event_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    ui_event: common.UiEvent = proto.Field(
        proto.MESSAGE,
        number=5,
        message=common.UiEvent,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
