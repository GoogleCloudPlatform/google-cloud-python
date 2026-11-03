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
import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.ces_v1beta.types import common, example, mocks, search_suggestions

__protobuf__ = proto.module(
    package="google.cloud.ces.v1beta",
    manifest={
        "AudioEncoding",
        "MockConfig",
        "InputAudioConfig",
        "OutputAudioConfig",
        "SessionConfig",
        "ToolCalls",
        "ToolResponses",
        "Citations",
        "Event",
        "SessionInput",
        "SessionOutput",
        "RecognitionResult",
        "InterruptionSignal",
        "EndSession",
        "GoAway",
        "RunSessionRequest",
        "RunSessionResponse",
        "BidiSessionClientMessage",
        "BidiSessionServerMessage",
        "StreamChatAiAssistantRequest",
        "AssistantSuggestion",
        "GenerateOnboardingSuggestionsRequest",
        "GenerateOnboardingSuggestionsResponse",
        "ArtifactChunk",
        "OptionQuestionsChunk",
        "AssistantConfirmationRequest",
        "AssistantConfirmationResponse",
        "OperationCompletedEvent",
        "TurnMetadata",
        "StreamChatAiAssistantResponse",
        "CancelAssistantTurnRequest",
        "CancelAssistantTurnResponse",
        "TurnResumeSnapshot",
        "TurnHandoffEvent",
        "TurnCompletedEvent",
    },
)


class AudioEncoding(proto.Enum):
    r"""AudioEncoding specifies the encoding format for audio data.

    Values:
        AUDIO_ENCODING_UNSPECIFIED (0):
            Unspecified audio encoding.
        LINEAR16 (1):
            16-bit linear PCM audio encoding.
        MULAW (2):
            8-bit samples that compand 14-bit audio
            samples using G.711 PCMU/mu-law.
        ALAW (3):
            8-bit samples that compand 14-bit audio
            samples using G.711 PCMU/A-law.
    """

    AUDIO_ENCODING_UNSPECIFIED = 0
    LINEAR16 = 1
    MULAW = 2
    ALAW = 3


class MockConfig(proto.Message):
    r"""Mock tool calls configuration for the session.

    Attributes:
        mocked_tool_calls (MutableSequence[google.cloud.ces_v1beta.types.MockedToolCall]):
            Optional. All tool calls to mock for the
            duration of the session.
        unmatched_tool_call_behavior (google.cloud.ces_v1beta.types.MockConfig.UnmatchedToolCallBehavior):
            Required. Beavhior for tool calls that don't match any args
            patterns in mocked_tool_calls.
    """

    class UnmatchedToolCallBehavior(proto.Enum):
        r"""What to do when a tool call doesn't match any mocked tool
        calls.

        Values:
            UNMATCHED_TOOL_CALL_BEHAVIOR_UNSPECIFIED (0):
                Default value. This value is unused.
            FAIL (1):
                Throw an error for any tool calls that don't
                match a mock expected input pattern.
            PASS_THROUGH (2):
                For unmatched tool calls, pass the tool call
                through to real tool.
        """

        UNMATCHED_TOOL_CALL_BEHAVIOR_UNSPECIFIED = 0
        FAIL = 1
        PASS_THROUGH = 2

    mocked_tool_calls: MutableSequence[mocks.MockedToolCall] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=mocks.MockedToolCall,
    )
    unmatched_tool_call_behavior: UnmatchedToolCallBehavior = proto.Field(
        proto.ENUM,
        number=2,
        enum=UnmatchedToolCallBehavior,
    )


class InputAudioConfig(proto.Message):
    r"""InputAudioConfig configures how the CES agent should
    interpret the incoming audio data.

    Attributes:
        audio_encoding (google.cloud.ces_v1beta.types.AudioEncoding):
            Required. The encoding of the input audio
            data.
        sample_rate_hertz (int):
            Required. The sample rate (in Hertz) of the
            input audio data.
        noise_suppression_level (str):
            Optional. Whether to enable noise suppression on the input
            audio. Available values are "low", "moderate", "high",
            "very_high".
    """

    audio_encoding: "AudioEncoding" = proto.Field(
        proto.ENUM,
        number=1,
        enum="AudioEncoding",
    )
    sample_rate_hertz: int = proto.Field(
        proto.INT32,
        number=2,
    )
    noise_suppression_level: str = proto.Field(
        proto.STRING,
        number=6,
    )


class OutputAudioConfig(proto.Message):
    r"""OutputAudioConfig configures how the CES agent should
    synthesize outgoing audio responses.

    Attributes:
        audio_encoding (google.cloud.ces_v1beta.types.AudioEncoding):
            Required. The encoding of the output audio
            data.
        sample_rate_hertz (int):
            Required. The sample rate (in Hertz) of the
            output audio data.
    """

    audio_encoding: "AudioEncoding" = proto.Field(
        proto.ENUM,
        number=1,
        enum="AudioEncoding",
    )
    sample_rate_hertz: int = proto.Field(
        proto.INT32,
        number=2,
    )


class SessionConfig(proto.Message):
    r"""The configuration for the session.

    Attributes:
        session (str):
            Required. The unique identifier of the session. Format:
            ``projects/{project}/locations/{location}/apps/{app}/sessions/{session}``
        input_audio_config (google.cloud.ces_v1beta.types.InputAudioConfig):
            Optional. Configuration for processing the
            input audio.
        output_audio_config (google.cloud.ces_v1beta.types.OutputAudioConfig):
            Optional. Configuration for generating the
            output audio.
        historical_contexts (MutableSequence[google.cloud.ces_v1beta.types.Message]):
            Optional. The historical context of the
            session, including user inputs, agent responses,
            and other messages. Typically, CES agent would
            manage session automatically so client doesn't
            need to explicitly populate this field. However,
            client can optionally override the historical
            contexts to force the session start from certain
            state.
        entry_agent (str):
            Optional. The entry agent to handle the session. If not
            specified, the session will be handled by the [root
            agent][google.cloud.ces.v1beta.App.root_agent] of the app.
            Format:
            ``projects/{project}/locations/{location}/apps/{app}/agents/{agent}``
        deployment (str):
            Optional. The deployment of the app to use for the session.
            Format:
            ``projects/{project}/locations/{location}/apps/{app}/deployments/{deployment}``
        time_zone (str):
            Optional. The time zone of the user. If provided, the agent
            will use the time zone for date and time related variables.
            Otherwise, the agent will use the time zone specified in the
            App.time_zone_settings.

            The format is the IANA Time Zone Database time zone, e.g.
            "America/Los_Angeles".
        use_tool_fakes (bool):
            Optional. Whether to use tool fakes for the
            session. If this field is set, the agent will
            attempt use tool fakes instead of calling the
            real tools.
        remote_dialogflow_query_parameters (google.cloud.ces_v1beta.types.SessionConfig.RemoteDialogflowQueryParameters):
            Optional.
            `QueryParameters <https://cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#queryparameters>`__
            to send to the remote
            `Dialogflow <https://cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents>`__
            agent when the session control is transferred to the remote
            agent.
        enable_text_streaming (bool):
            Optional. Whether to stream text output from the model to
            the client incrementally as it is generated. Defaults to
            ``false``.

            - When disabled, the model's text output is buffered, and
              each text output sent to the client is a complete
              sentence. Clients can render each text output on a new
              line.
            - When enabled, each text output may contain only part of a
              sentence. Clients should concatenate consecutive text
              outputs to render the complete response.

            NOTE: This is only supported for text (non-voice) sessions
            using
            [StreamRunSession][google.cloud.ces.v1beta.SessionService.StreamRunSession]
            or
            [BidiRunSession][google.cloud.ces.v1beta.SessionService.BidiRunSession].
        include_llm_thought_summary (bool):
            Optional. Whether to include LLM thought
            summaries in the session outputs.
        exclude_diagnostic_info (bool):
            Optional. Whether to exclude diagnostic info
            from the session output.
        include_progress_update (bool):
            Optional. Whether to include intermediate processing update
            to the client. If enabled, the update will be sent back in
            [SessionOutput.progress][google.cloud.ces.v1beta.SessionOutput.progress].
    """

    class RemoteDialogflowQueryParameters(proto.Message):
        r"""`QueryParameters <https://cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#queryparameters>`__
        to send to the remote
        `Dialogflow <https://cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents>`__
        agent when the session control is transferred to the remote agent.

        Attributes:
            webhook_headers (MutableMapping[str, str]):
                Optional. The HTTP headers to be sent as webhook_headers in
                `QueryParameters <https://cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#queryparameters>`__.
            payload (google.protobuf.struct_pb2.Struct):
                Optional. The payload to be sent in
                `QueryParameters <https://cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#queryparameters>`__.
            end_user_metadata (google.protobuf.struct_pb2.Struct):
                Optional. The end user metadata to be sent in
                `QueryParameters <https://cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#queryparameters>`__.
        """

        webhook_headers: MutableMapping[str, str] = proto.MapField(
            proto.STRING,
            proto.STRING,
            number=1,
        )
        payload: struct_pb2.Struct = proto.Field(
            proto.MESSAGE,
            number=2,
            message=struct_pb2.Struct,
        )
        end_user_metadata: struct_pb2.Struct = proto.Field(
            proto.MESSAGE,
            number=3,
            message=struct_pb2.Struct,
        )

    session: str = proto.Field(
        proto.STRING,
        number=1,
    )
    input_audio_config: "InputAudioConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="InputAudioConfig",
    )
    output_audio_config: "OutputAudioConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="OutputAudioConfig",
    )
    historical_contexts: MutableSequence[example.Message] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message=example.Message,
    )
    entry_agent: str = proto.Field(
        proto.STRING,
        number=12,
    )
    deployment: str = proto.Field(
        proto.STRING,
        number=8,
    )
    time_zone: str = proto.Field(
        proto.STRING,
        number=11,
    )
    use_tool_fakes: bool = proto.Field(
        proto.BOOL,
        number=14,
    )
    remote_dialogflow_query_parameters: RemoteDialogflowQueryParameters = proto.Field(
        proto.MESSAGE,
        number=15,
        message=RemoteDialogflowQueryParameters,
    )
    enable_text_streaming: bool = proto.Field(
        proto.BOOL,
        number=18,
    )
    include_llm_thought_summary: bool = proto.Field(
        proto.BOOL,
        number=21,
    )
    exclude_diagnostic_info: bool = proto.Field(
        proto.BOOL,
        number=24,
    )
    include_progress_update: bool = proto.Field(
        proto.BOOL,
        number=28,
    )


class ToolCalls(proto.Message):
    r"""Request for the client to execute the tools and return the
    execution results before continuing the session.

    Attributes:
        tool_calls (MutableSequence[google.cloud.ces_v1beta.types.ToolCall]):
            Optional. The list of tool calls to execute.
    """

    tool_calls: MutableSequence[example.ToolCall] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=example.ToolCall,
    )


class ToolResponses(proto.Message):
    r"""Execution results for the requested tool calls from the
    client.

    Attributes:
        tool_responses (MutableSequence[google.cloud.ces_v1beta.types.ToolResponse]):
            Optional. The list of tool execution results.
    """

    tool_responses: MutableSequence[example.ToolResponse] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=example.ToolResponse,
    )


class Citations(proto.Message):
    r"""Citations associated with the agent response.

    Attributes:
        cited_chunks (MutableSequence[google.cloud.ces_v1beta.types.Citations.CitedChunk]):
            List of cited pieces of information.
        inline_citations (MutableSequence[google.cloud.ces_v1beta.types.Citations.InlineCitation]):
            Optional. List of inline citations in the
            agent response.
    """

    class CitedChunk(proto.Message):
        r"""Piece of cited information.

        Attributes:
            uri (str):
                URI used for citation.
            title (str):
                Title of the cited document.
            text (str):
                Text used for citation.
            requires_attribution (bool):
                Whether this citation requires attribution to
                be shown to the end users.
        """

        uri: str = proto.Field(
            proto.STRING,
            number=1,
        )
        title: str = proto.Field(
            proto.STRING,
            number=2,
        )
        text: str = proto.Field(
            proto.STRING,
            number=3,
        )
        requires_attribution: bool = proto.Field(
            proto.BOOL,
            number=4,
        )

    class InlineCitation(proto.Message):
        r"""An inline citation in the response text.

        Attributes:
            start_index (int):
                The starting index (in bytes) of the text
                segment in the agent response.
            end_index (int):
                The ending index (in bytes) of the text
                segment in the agent response.
            cited_chunk_indices (MutableSequence[int]):
                The indices of the cited chunks that back this text segment.
                Indices refer to the elements in ``cited_chunks``.
        """

        start_index: int = proto.Field(
            proto.INT32,
            number=1,
        )
        end_index: int = proto.Field(
            proto.INT32,
            number=2,
        )
        cited_chunk_indices: MutableSequence[int] = proto.RepeatedField(
            proto.INT32,
            number=3,
        )

    cited_chunks: MutableSequence[CitedChunk] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=CitedChunk,
    )
    inline_citations: MutableSequence[InlineCitation] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=InlineCitation,
    )


class Event(proto.Message):
    r"""Event input.

    Attributes:
        event (str):
            Required. The name of the event.
        variables (google.protobuf.struct_pb2.Struct):
            Optional. Additional variables associated
            with the event.
    """

    event: str = proto.Field(
        proto.STRING,
        number=1,
    )
    variables: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=2,
        message=struct_pb2.Struct,
    )


class SessionInput(proto.Message):
    r"""Input for the session.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        text (str):
            Optional. Text data from the end user.

            This field is a member of `oneof`_ ``input_type``.
        dtmf (str):
            Optional. DTMF digits from the end user.

            This field is a member of `oneof`_ ``input_type``.
        audio (bytes):
            Optional. Audio data from the end user.

            This field is a member of `oneof`_ ``input_type``.
        tool_responses (google.cloud.ces_v1beta.types.ToolResponses):
            Optional. Execution results for the tool
            calls from the client.

            This field is a member of `oneof`_ ``input_type``.
        image (google.cloud.ces_v1beta.types.Image):
            Optional. Image data from the end user.

            This field is a member of `oneof`_ ``input_type``.
        blob (google.cloud.ces_v1beta.types.Blob):
            Optional. Blob data from the end user.

            This field is a member of `oneof`_ ``input_type``.
        variables (google.protobuf.struct_pb2.Struct):
            Optional. Contextual variables for the session, keyed by
            name. Only variables declared in the app will be used by the
            CES agent.

            Unrecognized variables will still be sent to the [Dialogflow
            agent][Agent.RemoteDialogflowAgent] as additional session
            parameters.

            This field is a member of `oneof`_ ``input_type``.
        event (google.cloud.ces_v1beta.types.Event):
            Optional. Event input.

            This field is a member of `oneof`_ ``input_type``.
        will_continue (bool):
            Optional. A flag to indicate if the current message is a
            fragment of a larger input in the bidi streaming session.

            When set to ``true``, the agent defers processing until it
            receives a subsequent message where ``will_continue`` is
            ``false``, or until the system detects an endpoint in the
            audio input.

            NOTE: This field does not apply to audio and DTMF inputs, as
            they are always processed automatically based on the
            endpointing signal.
        recording_control (google.cloud.ces_v1beta.types.SessionInput.RecordingControl):
            Optional. Whether the conversation may be
            recorded and logged from here on.
            Use this when the app, rather than the agent,
            decides what may be kept:

            for example when the end user has to consent to
            being recorded before anything about the call
            can be stored.

            The value stays in effect until the client sends
            a different one, so it only needs to be sent
            when the answer changes. Whatever is in effect
            when a turn completes decides that turn, both
            whether its audio reaches the recording bucket
            and whether its transcript reaches conversation
            history, BigQuery and Cloud Logging. It covers
            the agent's side of the turn as well as the end
            user's.

            Turns that complete before the client first
            sends this are recorded according to the app's
            logging settings, as though the field did not
            exist.

            If more than one input in the same request sets
            it, the last one wins.
    """

    class RecordingControl(proto.Enum):
        r"""What the app has decided may be recorded and logged.

        This enum is extensible; new values may be added in the future.

        Values:
            RECORDING_CONTROL_UNSPECIFIED (0):
                The app is not controlling recording. The
                app's logging settings decide, as they do for
                every session that never sets this field.
            RECORDING_ENABLED (1):
                The conversation may be recorded and logged
                from here on.
            RECORDING_DISABLED (2):
                The conversation may not be recorded or
                logged from here on.
        """

        RECORDING_CONTROL_UNSPECIFIED = 0
        RECORDING_ENABLED = 1
        RECORDING_DISABLED = 2

    text: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="input_type",
    )
    dtmf: str = proto.Field(
        proto.STRING,
        number=6,
        oneof="input_type",
    )
    audio: bytes = proto.Field(
        proto.BYTES,
        number=2,
        oneof="input_type",
    )
    tool_responses: "ToolResponses" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="input_type",
        message="ToolResponses",
    )
    image: example.Image = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="input_type",
        message=example.Image,
    )
    blob: example.Blob = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="input_type",
        message=example.Blob,
    )
    variables: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="input_type",
        message=struct_pb2.Struct,
    )
    event: "Event" = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="input_type",
        message="Event",
    )
    will_continue: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    recording_control: RecordingControl = proto.Field(
        proto.ENUM,
        number=10,
        enum=RecordingControl,
    )


class SessionOutput(proto.Message):
    r"""Output for the session.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        text (str):
            Output text from the CES agent.

            This field is a member of `oneof`_ ``output_type``.
        audio (bytes):
            Output audio from the CES agent.

            This field is a member of `oneof`_ ``output_type``.
        tool_calls (google.cloud.ces_v1beta.types.ToolCalls):
            Request for the client to execute the tools.

            This field is a member of `oneof`_ ``output_type``.
        citations (google.cloud.ces_v1beta.types.Citations):
            Citations that provide the source information
            for the agent's generated text.

            This field is a member of `oneof`_ ``output_type``.
        google_search_suggestions (google.cloud.ces_v1beta.types.GoogleSearchSuggestions):
            The suggestions returned from Google Search as a result of
            invoking the
            [GoogleSearchTool][google.cloud.ces.v1beta.GoogleSearchTool].

            This field is a member of `oneof`_ ``output_type``.
        end_session (google.cloud.ces_v1beta.types.EndSession):
            Indicates the session has ended.

            This field is a member of `oneof`_ ``output_type``.
        payload (google.protobuf.struct_pb2.Struct):
            Custom payload with structured output from
            the CES agent.

            This field is a member of `oneof`_ ``output_type``.
        image (google.cloud.ces_v1beta.types.Image):
            Output image from the CES agent.

            This field is a member of `oneof`_ ``output_type``.
        progress (str):
            Intermediate progress update from the CES
            agent.

            This field is a member of `oneof`_ ``output_type``.
        turn_index (int):
            Indicates the sequential order of
            conversation turn to which this output belongs
            to, starting from 1.
        turn_completed (bool):
            If true, the CES agent has detected the end
            of the current conversation turn and will
            provide no further output for this turn.
        diagnostic_info (google.cloud.ces_v1beta.types.SessionOutput.DiagnosticInfo):
            Optional. Diagnostic information contains execution details
            during the processing of the input. Only populated in the
            last SessionOutput (with ``turn_completed=true``) for each
            turn.
        context (MutableSequence[google.protobuf.any_pb2.Any]):
            Context messages for external supervision
            guardrails.
    """

    class DiagnosticInfo(proto.Message):
        r"""Contains execution details during the processing.

        Attributes:
            messages (MutableSequence[google.cloud.ces_v1beta.types.Message]):
                List of the messages that happened during the
                processing.
            root_span (google.cloud.ces_v1beta.types.Span):
                A trace of the entire request processing,
                represented as a root span. This span can
                contain nested child spans for specific
                operations.
        """

        messages: MutableSequence[example.Message] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=example.Message,
        )
        root_span: common.Span = proto.Field(
            proto.MESSAGE,
            number=3,
            message=common.Span,
        )

    text: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="output_type",
    )
    audio: bytes = proto.Field(
        proto.BYTES,
        number=2,
        oneof="output_type",
    )
    tool_calls: "ToolCalls" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="output_type",
        message="ToolCalls",
    )
    citations: "Citations" = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="output_type",
        message="Citations",
    )
    google_search_suggestions: search_suggestions.GoogleSearchSuggestions = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="output_type",
        message=search_suggestions.GoogleSearchSuggestions,
    )
    end_session: "EndSession" = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="output_type",
        message="EndSession",
    )
    payload: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="output_type",
        message=struct_pb2.Struct,
    )
    image: example.Image = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="output_type",
        message=example.Image,
    )
    progress: str = proto.Field(
        proto.STRING,
        number=14,
        oneof="output_type",
    )
    turn_index: int = proto.Field(
        proto.INT32,
        number=6,
    )
    turn_completed: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    diagnostic_info: DiagnosticInfo = proto.Field(
        proto.MESSAGE,
        number=7,
        message=DiagnosticInfo,
    )
    context: MutableSequence[any_pb2.Any] = proto.RepeatedField(
        proto.MESSAGE,
        number=12,
        message=any_pb2.Any,
    )


class RecognitionResult(proto.Message):
    r"""Speech recognition result for the audio input.

    Attributes:
        transcript (str):
            Optional. Concatenated user speech segments
            captured during the current turn.
    """

    transcript: str = proto.Field(
        proto.STRING,
        number=1,
    )


class InterruptionSignal(proto.Message):
    r"""Indicates the agent's audio response has been interrupted.
    The client should immediately stop any current audio playback
    (e.g., due to user barge-in or a new agent response being
    generated).

    Attributes:
        barge_in (bool):
            Whether the interruption is caused by a user
            barge-in event.
    """

    barge_in: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class EndSession(proto.Message):
    r"""Indicates the session has terminated, due to either
    successful completion (e.g. user says "Good bye!" ) or an agent
    escalation.

    The agent will not process any further inputs after session is
    terminated and the client should half-close and disconnect after
    receiving all remaining responses from the agent.

    Attributes:
        metadata (google.protobuf.struct_pb2.Struct):
            Optional. Provides additional information
            about the end session signal, such as the reason
            for ending the session.
    """

    metadata: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=1,
        message=struct_pb2.Struct,
    )


class GoAway(proto.Message):
    r"""Indicates that the server will disconnect soon and the client
    should half-close and restart the connection.

    """


class RunSessionRequest(proto.Message):
    r"""Request message for
    [SessionService.RunSession][google.cloud.ces.v1beta.SessionService.RunSession].

    Attributes:
        config (google.cloud.ces_v1beta.types.SessionConfig):
            Required. The configuration for the session.
        inputs (MutableSequence[google.cloud.ces_v1beta.types.SessionInput]):
            Required. Inputs for the session.
    """

    config: "SessionConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="SessionConfig",
    )
    inputs: MutableSequence["SessionInput"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="SessionInput",
    )


class RunSessionResponse(proto.Message):
    r"""Response message for
    [SessionService.RunSession][google.cloud.ces.v1beta.SessionService.RunSession].

    Attributes:
        outputs (MutableSequence[google.cloud.ces_v1beta.types.SessionOutput]):
            Outputs for the session.
    """

    outputs: MutableSequence["SessionOutput"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SessionOutput",
    )


class BidiSessionClientMessage(proto.Message):
    r"""The top-level message sent by the client for the
    [SessionService.BidiRunSession][google.cloud.ces.v1beta.SessionService.BidiRunSession]
    method.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        config (google.cloud.ces_v1beta.types.SessionConfig):
            Optional. The initial config message for the
            session.

            This field is a member of `oneof`_ ``message_type``.
        realtime_input (google.cloud.ces_v1beta.types.SessionInput):
            Optional. Realtime input for the session.

            This field is a member of `oneof`_ ``message_type``.
    """

    config: "SessionConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="message_type",
        message="SessionConfig",
    )
    realtime_input: "SessionInput" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="message_type",
        message="SessionInput",
    )


class BidiSessionServerMessage(proto.Message):
    r"""The top-level message returned from
    [SessionService.BidiRunSession][google.cloud.ces.v1beta.SessionService.BidiRunSession]
    method.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        session_output (google.cloud.ces_v1beta.types.SessionOutput):
            Optional. Processing result from the CES
            agent.

            This field is a member of `oneof`_ ``message_type``.
        recognition_result (google.cloud.ces_v1beta.types.RecognitionResult):
            Optional. Realtime speech recognition result
            for the audio input.

            This field is a member of `oneof`_ ``message_type``.
        interruption_signal (google.cloud.ces_v1beta.types.InterruptionSignal):
            Optional. Indicates the agent's audio
            response has been interrupted.

            This field is a member of `oneof`_ ``message_type``.
        end_session (google.cloud.ces_v1beta.types.EndSession):
            Optional. Indicates that the session has
            ended.

            This field is a member of `oneof`_ ``message_type``.
        go_away (google.cloud.ces_v1beta.types.GoAway):
            Optional. Indicates that the server will
            disconnect soon and the client should half-close
            and restart the connection.

            This field is a member of `oneof`_ ``message_type``.
    """

    session_output: "SessionOutput" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="message_type",
        message="SessionOutput",
    )
    recognition_result: "RecognitionResult" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="message_type",
        message="RecognitionResult",
    )
    interruption_signal: "InterruptionSignal" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="message_type",
        message="InterruptionSignal",
    )
    end_session: "EndSession" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="message_type",
        message="EndSession",
    )
    go_away: "GoAway" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="message_type",
        message="GoAway",
    )


class StreamChatAiAssistantRequest(proto.Message):
    r"""Request message for
    [SessionService.StreamChatAiAssistant][google.cloud.ces.v1beta.SessionService.StreamChatAiAssistant].

    Attributes:
        name (str):
            Required. The assistant session to be used to run the
            assistant. Format:
            ``projects/{project}/locations/{location}/apps/{app}/assistantSessions/{assistant_session}``
        message (str):
            Optional. The message to send to the assistant agent. May be
            empty when ``confirmation_response`` is set (answering a
            pending confirmation without adding a new message); at least
            one of the two must be provided.
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
        confirmation_response (google.cloud.ces_v1beta.types.AssistantConfirmationResponse):
            Optional. The user's answer to a pending
            [AssistantConfirmationRequest][google.cloud.ces.v1beta.AssistantConfirmationRequest].
            When set, the server resumes the paused agent with this
            answer instead of (or in addition to) starting a new prompt
            turn.
        client_capabilities (MutableSequence[google.cloud.ces_v1beta.types.StreamChatAiAssistantRequest.ClientCapability]):
            Optional. Response features this client can render. The
            server only emits events that need a capability (e.g.
            ``confirmation_request``) when the capability is declared,
            so older clients never receive events they would silently
            drop.
        operation_completed_event (google.cloud.ces_v1beta.types.OperationCompletedEvent):
            Optional. Resumes an assistant session paused
            waiting for a client-managed long-running
            operation to complete.
        resume_from_sequence_number (int):
            Optional. Optional cursor to resume and
            replay events from an in-flight or completed
            turn.
        attach_only (bool):
            Optional. Optional flag to attach to an
            existing in-flight turn without submitting a new
            message.
    """

    class ClientCapability(proto.Enum):
        r"""Response features a client can declare.

        Values:
            CLIENT_CAPABILITY_UNSPECIFIED (0):
                Unspecified capability; ignored.
            CONFIRMATION_CARDS (1):
                The client renders
                [AssistantConfirmationRequest][google.cloud.ces.v1beta.AssistantConfirmationRequest]
                cards and answers them via ``confirmation_response``.
            CLIENT_MANAGED_LRO (2):
                The client manages long-running operations out-of-band by
                polling the operation and sending
                ``operation_completed_event`` to resume the turn. If not
                declared, the server manages LRO polling and completes the
                turn inline.
        """

        CLIENT_CAPABILITY_UNSPECIFIED = 0
        CONFIRMATION_CARDS = 1
        CLIENT_MANAGED_LRO = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
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
    confirmation_response: "AssistantConfirmationResponse" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="AssistantConfirmationResponse",
    )
    client_capabilities: MutableSequence[ClientCapability] = proto.RepeatedField(
        proto.ENUM,
        number=8,
        enum=ClientCapability,
    )
    operation_completed_event: "OperationCompletedEvent" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="OperationCompletedEvent",
    )
    resume_from_sequence_number: int = proto.Field(
        proto.INT64,
        number=11,
    )
    attach_only: bool = proto.Field(
        proto.BOOL,
        number=12,
    )


class AssistantSuggestion(proto.Message):
    r"""A single personalized onboarding suggestion chip for Arc's
    zero state.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        seed_prompt (str):
            Prefill the composer with this text; the user
            reviews and sends.

            This field is a member of `oneof`_ ``action``.
        load_session (google.cloud.ces_v1beta.types.AssistantSuggestion.LoadSession):
            Open an existing assistant session.

            This field is a member of `oneof`_ ``action``.
        send_message (str):
            Prefill the composer with this text and
            submit immediately. Only used for quick-reply
            chips inside an active onboarding conversation.

            This field is a member of `oneof`_ ``action``.
        suggestion_id (str):
            Stable identifier for this suggestion,
            round-tripped by clients in interaction logging.
        label (str):
            Chip label shown to the user (at most 60
            characters).
        rationale (str):
            Optional short explanation of why this
            suggestion is shown (tooltip / rationale
            popover).
        icon (google.cloud.ces_v1beta.types.AssistantSuggestion.Icon):
            Icon hint for the chip.
        source (google.cloud.ces_v1beta.types.AssistantSuggestion.Source):
            How this suggestion was produced.
        candidate_type (str):
            Rule-table candidate type in kebab-case (e.g.
            "resume-pending-review"), for metrics.
    """

    class Icon(proto.Enum):
        r"""Icon hint for the chip.

        Values:
            ICON_UNSPECIFIED (0):
                Unspecified icon.
            RESUME (1):
                Resume a previous session.
            BUILD (2):
                Build something new.
            EVALUATE (3):
                Evaluation-related suggestion.
            DEPLOY (4):
                Deployment-related suggestion.
            EXPLORE (5):
                Exploration / discovery suggestion.
            FIX (6):
                Fix an error or failing state.
        """

        ICON_UNSPECIFIED = 0
        RESUME = 1
        BUILD = 2
        EVALUATE = 3
        DEPLOY = 4
        EXPLORE = 5
        FIX = 6

    class Source(proto.Enum):
        r"""How this suggestion was produced.

        Values:
            SOURCE_UNSPECIFIED (0):
                Unspecified source.
            RULE (1):
                Deterministic rule-table candidate with
                template phrasing.
            LLM_RANKED (2):
                Rule-table candidate re-ranked and phrased by
                the LLM phrasing step.
        """

        SOURCE_UNSPECIFIED = 0
        RULE = 1
        LLM_RANKED = 2

    class LoadSession(proto.Message):
        r"""Parameters for the load_session action.

        Attributes:
            assistant_session_id (str):
                Identifier of the assistant session to open
                (the final segment of the AssistantSession
                resource name).
        """

        assistant_session_id: str = proto.Field(
            proto.STRING,
            number=1,
        )

    seed_prompt: str = proto.Field(
        proto.STRING,
        number=5,
        oneof="action",
    )
    load_session: LoadSession = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="action",
        message=LoadSession,
    )
    send_message: str = proto.Field(
        proto.STRING,
        number=7,
        oneof="action",
    )
    suggestion_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    label: str = proto.Field(
        proto.STRING,
        number=2,
    )
    rationale: str = proto.Field(
        proto.STRING,
        number=3,
    )
    icon: Icon = proto.Field(
        proto.ENUM,
        number=4,
        enum=Icon,
    )
    source: Source = proto.Field(
        proto.ENUM,
        number=8,
        enum=Source,
    )
    candidate_type: str = proto.Field(
        proto.STRING,
        number=9,
    )


class GenerateOnboardingSuggestionsRequest(proto.Message):
    r"""Request message for
    [SessionService.GenerateOnboardingSuggestions][google.cloud.ces.v1beta.SessionService.GenerateOnboardingSuggestions].

    Attributes:
        name (str):
            Required. The app whose zero state is being rendered.
            Format:
            ``projects/{project}/locations/{location}/apps/{app}``
        max_suggestions (int):
            Optional. Maximum number of suggestions to
            return. Defaults to 4 when unset.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    max_suggestions: int = proto.Field(
        proto.INT32,
        number=2,
    )


class GenerateOnboardingSuggestionsResponse(proto.Message):
    r"""Response message for
    [SessionService.GenerateOnboardingSuggestions][google.cloud.ces.v1beta.SessionService.GenerateOnboardingSuggestions].

    Attributes:
        user_profile (google.cloud.ces_v1beta.types.GenerateOnboardingSuggestionsResponse.UserProfile):
            Classification of the requesting user's
            history.
        suggestions (MutableSequence[google.cloud.ces_v1beta.types.AssistantSuggestion]):
            Personalized suggestions, ranked most
            relevant first.
        context_token (str):
            Opaque token capturing the onboarding snapshot used to
            generate these suggestions. Clients echo it on the first
            [StreamChatAiAssistantRequest][google.cloud.ces.v1beta.StreamChatAiAssistantRequest]
            so the server can reuse the snapshot.
    """

    class UserProfile(proto.Enum):
        r"""Classification of the requesting user's history with the
        assistant in this app.

        Values:
            USER_PROFILE_UNSPECIFIED (0):
                Unspecified profile.
            NEW (1):
                No assistant sessions containing messages.
            EXPLORING (2):
                One or two assistant sessions containing
                messages.
            RETURNING (3):
                More than two assistant sessions containing
                messages.
        """

        USER_PROFILE_UNSPECIFIED = 0
        NEW = 1
        EXPLORING = 2
        RETURNING = 3

    user_profile: UserProfile = proto.Field(
        proto.ENUM,
        number=1,
        enum=UserProfile,
    )
    suggestions: MutableSequence["AssistantSuggestion"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="AssistantSuggestion",
    )
    context_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ArtifactChunk(proto.Message):
    r"""A streamed fragment of a document artifact (e.g. a markdown
    TDD) that the assistant is generating. Content deltas stream
    while the document is being written so clients can render a live
    preview; the FINALIZED chunk carries the GCS URI once the file
    has been persisted.

    Attributes:
        artifact_id (str):
            Identifier of the artifact, stable across all
            chunks of one artifact within the stream.
        display_name (str):
            The file name shown to the user, e.g.
            "hotel_booking_tdd.md". Set on STARTED (and repeated on
            FINALIZED).
        mime_type (str):
            The IANA media type of the artifact content,
            e.g. "text/markdown".
        content_delta (str):
            Incremental artifact content. Set on DELTA
            chunks.
        gcs_uri (str):
            The GCS object the artifact was persisted to.
            Set on FINALIZED chunks.
        state (google.cloud.ces_v1beta.types.ArtifactChunk.State):
            Lifecycle position of this chunk.
    """

    class State(proto.Enum):
        r"""Lifecycle position of this chunk within the artifact's
        stream.

        Values:
            STATE_UNSPECIFIED (0):
                Unused default.
            STARTED (1):
                The assistant started generating the
                artifact.
            DELTA (2):
                A content increment; content_delta is set.
            FINALIZED (3):
                The artifact was persisted; gcs_uri is set.
            FAILED (4):
                Generation or persistence failed; the
                artifact was not saved.
            CLOSED (5):
                The document finished streaming: its content was fully
                delivered via content_delta chunks. Persistence may still
                follow; a FINALIZED chunk with a gcs_uri is sent if and when
                the artifact is saved.
        """

        STATE_UNSPECIFIED = 0
        STARTED = 1
        DELTA = 2
        FINALIZED = 3
        FAILED = 4
        CLOSED = 5

    artifact_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    mime_type: str = proto.Field(
        proto.STRING,
        number=3,
    )
    content_delta: str = proto.Field(
        proto.STRING,
        number=4,
    )
    gcs_uri: str = proto.Field(
        proto.STRING,
        number=5,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=6,
        enum=State,
    )


class OptionQuestionsChunk(proto.Message):
    r"""Structured clarification options the assistant asks the user
    to choose among, transduced server-side out of the model's turn
    (the option block is stripped from the streamed and persisted
    text). The console renders a keyboard-navigable option list
    docked above the composer.

    Attributes:
        questions (MutableSequence[google.cloud.ces_v1beta.types.OptionQuestionsChunk.Question]):
            The questions asked this turn. More than one
            entry drives the console's "1 of N" pager.
    """

    class Option(proto.Message):
        r"""A single selectable option.

        Attributes:
            title (str):
                Short plain-text option title (no markdown,
                no numbering).
            details (str):
                Optional trade-off details shown as secondary
                text.
            submit_text (str):
                Optional message text to send when the option is chosen;
                defaults to ``title`` when empty.
        """

        title: str = proto.Field(
            proto.STRING,
            number=1,
        )
        details: str = proto.Field(
            proto.STRING,
            number=2,
        )
        submit_text: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class Question(proto.Message):
        r"""One question with its options.

        Attributes:
            question (str):
                The question header text.
            options (MutableSequence[google.cloud.ces_v1beta.types.OptionQuestionsChunk.Option]):
                The selectable options, in presentation
                order.
        """

        question: str = proto.Field(
            proto.STRING,
            number=1,
        )
        options: MutableSequence["OptionQuestionsChunk.Option"] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="OptionQuestionsChunk.Option",
        )

    questions: MutableSequence[Question] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=Question,
    )


class AssistantConfirmationRequest(proto.Message):
    r"""A blocking question or confirmation the assistant needs answered
    before an agent action can proceed. The requesting agent is paused
    and resumes only when the answer arrives on a later
    [StreamChatAiAssistantRequest.confirmation_response][google.cloud.ces.v1beta.StreamChatAiAssistantRequest.confirmation_response].

    Attributes:
        confirmation_id (str):
            Identifier correlating this request with its
            response. Opaque to clients; must be echoed
            verbatim on the answering request.
        context (str):
            Context describing what is being confirmed
            (e.g. the action the agent wants to take, or the
            question it needs answered). Rendered as plain
            text, not Markdown.
        positive_label (str):
            Label for the approving action of a binary confirmation
            (e.g. "Publish"). Unset when ``questions`` is populated.
        negative_label (str):
            Label for the declining action of a binary confirmation
            (e.g. "Not yet"). Unset when ``questions`` is populated.
        questions (MutableSequence[google.cloud.ces_v1beta.types.OptionQuestionsChunk.Question]):
            Multi-choice form of the confirmation. When populated, the
            card renders a selectable option list and the chosen
            option's submit_text (or free-form user text) is returned as
            [AssistantConfirmationResponse.answer_text][google.cloud.ces.v1beta.AssistantConfirmationResponse.answer_text].
        tool (str):
            Name of the tool call the agent paused on (e.g.
            "update_app"), for the card header. Unset for pure
            questions.
        agent_name (str):
            Display label of the agent that raised the confirmation
            (e.g. ``"Contract Architect"``), for the card header.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            Time after which this confirmation can no
            longer be answered. An expired card renders as
            inactive, and the server declines the
            confirmation on the next turn so the paused
            agent does not wait indefinitely.
    """

    confirmation_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    context: str = proto.Field(
        proto.STRING,
        number=2,
    )
    positive_label: str = proto.Field(
        proto.STRING,
        number=3,
    )
    negative_label: str = proto.Field(
        proto.STRING,
        number=4,
    )
    questions: MutableSequence["OptionQuestionsChunk.Question"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="OptionQuestionsChunk.Question",
    )
    tool: str = proto.Field(
        proto.STRING,
        number=6,
    )
    agent_name: str = proto.Field(
        proto.STRING,
        number=7,
    )
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )


class AssistantConfirmationResponse(proto.Message):
    r"""The user's answer to an
    [AssistantConfirmationRequest][google.cloud.ces.v1beta.AssistantConfirmationRequest],
    sent on the next
    [SessionService.StreamChatAiAssistant][google.cloud.ces.v1beta.SessionService.StreamChatAiAssistant]
    call to resume the paused agent.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        confirmed (bool):
            Binary answer: true approves the paused
            action, false declines it.

            This field is a member of `oneof`_ ``response``.
        answer_text (str):
            The chosen option's submit_text, or free-form user text. The
            paused action is cancelled and the text is handed to the
            agent to act on.

            This field is a member of `oneof`_ ``response``.
        confirmation_id (str):
            The
            [AssistantConfirmationRequest.confirmation_id][google.cloud.ces.v1beta.AssistantConfirmationRequest.confirmation_id]
            being answered.
    """

    confirmed: bool = proto.Field(
        proto.BOOL,
        number=2,
        oneof="response",
    )
    answer_text: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="response",
    )
    confirmation_id: str = proto.Field(
        proto.STRING,
        number=1,
    )


class OperationCompletedEvent(proto.Message):
    r"""Event sent by the client or background worker to resume an
    assistant session after an asynchronous Long-Running Operation
    (LRO) completes.

    Attributes:
        operation_name (str):
            The operation resource name (e.g. ``operations/{op}``).
        target_resource_name (str):
            The primary resource targeted or produced by
            the operation (e.g. evaluation run ID, app ID,
            dataset ID).
        operation_type (str):
            The operation type or tool name (e.g. "run_evaluation",
            "copy_app", "export_app").
        status (str):
            Status of the operation run (e.g.
            "SUCCEEDED", "FAILED", "CANCELLED").
        deduplication_token (str):
            Optional deduplication token (e.g. UUID) to
            prevent duplicate turn execution from concurrent
            browser tabs.
        error (google.rpc.status_pb2.Status):
            Optional canonical error status if the
            operation failed.
        metadata (google.protobuf.struct_pb2.Struct):
            Optional structured result metadata (e.g. pass_rate,
            total_examples, export_uri).
    """

    operation_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    target_resource_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    operation_type: str = proto.Field(
        proto.STRING,
        number=3,
    )
    status: str = proto.Field(
        proto.STRING,
        number=4,
    )
    deduplication_token: str = proto.Field(
        proto.STRING,
        number=5,
    )
    error: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=6,
        message=status_pb2.Status,
    )
    metadata: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=7,
        message=struct_pb2.Struct,
    )


class TurnMetadata(proto.Message):
    r"""Turn-level metadata and intent categorization.

    Attributes:
        contract_related (bool):
            Indicates whether this assistant turn was
            contract-related (e.g. contract drafting,
            alignment, extraction, or revision).
        contract_finalized (bool):
            Set on the final artifact event of a turn whose contract
            draft was published (a revision was activated). Terminal for
            the clarification flow of this draft: contract_progress is
            authoritative and complete.
        contract_streaming_phase (google.cloud.ces_v1beta.types.TurnMetadata.ContractStreamingPhase):
            Set only on in-flight progress estimates
            emitted while a contract artifact fence is
            streaming, and on the revision-turn-start event.
            Unset on authoritative payloads.
        contract_draft_complete (bool):
            Set on the terminal event of a contract draft whose every
            placeholder is resolved (contract_progress is 100%), whether
            or not the draft was published. Clients complete and dismiss
            the contract progress display on it; publication is reported
            separately by contract_finalized.
    """

    class ContractStreamingPhase(proto.Enum):
        r"""Streaming phase of the contract progress payload.

        Values:
            CONTRACT_STREAMING_PHASE_UNSPECIFIED (0):
                The payload is authoritative (computed from a
                complete contract document, a persisted
                snapshot, or the pre-draft state). Clients must
                replace any previously received progress with
                it.
            DRAFTING (1):
                An initial contract draft is streaming. contract_progress is
                an in-flight estimate: non-decreasing within one artifact
                fence, capped below the authoritative range, with
                pillar_breakdowns carrying total_item_count == 0 to mark
                estimated pillar states.
            REVISING (2):
                A revision of an existing contract is
                streaming (for example after an annotation
                submission). Same estimate semantics as
                DRAFTING.
        """

        CONTRACT_STREAMING_PHASE_UNSPECIFIED = 0
        DRAFTING = 1
        REVISING = 2

    contract_related: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    contract_finalized: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    contract_streaming_phase: ContractStreamingPhase = proto.Field(
        proto.ENUM,
        number=4,
        enum=ContractStreamingPhase,
    )
    contract_draft_complete: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class StreamChatAiAssistantResponse(proto.Message):
    r"""Response message for
    [SessionService.StreamChatAiAssistant][google.cloud.ces.v1beta.SessionService.StreamChatAiAssistant].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        text_chunk (str):
            Text Token (for streaming Gemini responses
            word-by-word).

            This field is a member of `oneof`_ ``event``.
        status (google.rpc.status_pb2.Status):
            Simple status update.

            This field is a member of `oneof`_ ``event``.
        thought_chunk (str):
            Thought text chunk (agent's reasoning before
            generating response).

            This field is a member of `oneof`_ ``event``.
        tool_call (google.cloud.ces_v1beta.types.ToolCall):
            Tool call execution event.

            This field is a member of `oneof`_ ``event``.
        tool_response (google.cloud.ces_v1beta.types.ToolResponse):
            Tool call response event.

            This field is a member of `oneof`_ ``event``.
        artifact_chunk (google.cloud.ces_v1beta.types.ArtifactChunk):
            Generated-document artifact event (live
            preview deltas + final GCS pointer).

            This field is a member of `oneof`_ ``event``.
        option_questions_chunk (google.cloud.ces_v1beta.types.OptionQuestionsChunk):
            Structured clarification options parsed out
            of the model turn. The console renders these as
            a selectable option list instead of raw text.

            This field is a member of `oneof`_ ``event``.
        confirmation_request (google.cloud.ces_v1beta.types.AssistantConfirmationRequest):
            A blocking confirmation the agent paused on. The agent
            resumes when the answer arrives on a later request's
            ``confirmation_response``. Only sent to clients that
            declared the CONFIRMATION_CARDS capability on the request.

            This field is a member of `oneof`_ ``event``.
        session_checkpoint (google.cloud.ces_v1beta.types.SessionCheckpoint):
            Session checkpoint/compaction recap event
            containing user intent and rolling summary.

            This field is a member of `oneof`_ ``event``.
        resume_snapshot (google.cloud.ces_v1beta.types.TurnResumeSnapshot):
            A compacted replay of an in-flight turn, sent
            as the first event of every attach or resume
            before any live event. The client replaces any
            locally rendered state for this turn with the
            snapshot's contents.

            This field is a member of `oneof`_ ``event``.
        handoff (google.cloud.ces_v1beta.types.TurnHandoffEvent):
            Tells the client to silently reconnect with
            resume_from_sequence_number: the task serving this stream is
            going away and the turn will continue elsewhere. Not an
            error; the stream completes normally after this event.

            This field is a member of `oneof`_ ``event``.
        turn_completed (google.cloud.ces_v1beta.types.TurnCompletedEvent):
            The turn has ended. Sent as the last event of
            every turn, on the original stream and on every
            attached or resumed stream, so clients can end
            the turn on an explicit signal instead of
            inferring it from stream closure.

            This field is a member of `oneof`_ ``event``.
        event_id (str):
            Unique identifier for the event.
        event_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp when the event occurred.
        ui_event (google.cloud.ces_v1beta.types.UiEvent):
            Optional. UI event payload.
        turn_metadata (google.cloud.ces_v1beta.types.TurnMetadata):
            Optional. Turn-level metadata and intent
            categorization.
        sequence_number (int):
            Optional. Monotonically increasing sequence
            number for this session turn.
        turn_in_progress (bool):
            Optional. Indicates whether the turn is still
            actively running in the background.
    """

    text_chunk: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="event",
    )
    status: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="event",
        message=status_pb2.Status,
    )
    thought_chunk: str = proto.Field(
        proto.STRING,
        number=6,
        oneof="event",
    )
    tool_call: example.ToolCall = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="event",
        message=example.ToolCall,
    )
    tool_response: example.ToolResponse = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="event",
        message=example.ToolResponse,
    )
    artifact_chunk: "ArtifactChunk" = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="event",
        message="ArtifactChunk",
    )
    option_questions_chunk: "OptionQuestionsChunk" = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="event",
        message="OptionQuestionsChunk",
    )
    confirmation_request: "AssistantConfirmationRequest" = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="event",
        message="AssistantConfirmationRequest",
    )
    session_checkpoint: common.SessionCheckpoint = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="event",
        message=common.SessionCheckpoint,
    )
    resume_snapshot: "TurnResumeSnapshot" = proto.Field(
        proto.MESSAGE,
        number=17,
        oneof="event",
        message="TurnResumeSnapshot",
    )
    handoff: "TurnHandoffEvent" = proto.Field(
        proto.MESSAGE,
        number=18,
        oneof="event",
        message="TurnHandoffEvent",
    )
    turn_completed: "TurnCompletedEvent" = proto.Field(
        proto.MESSAGE,
        number=19,
        oneof="event",
        message="TurnCompletedEvent",
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
    turn_metadata: "TurnMetadata" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="TurnMetadata",
    )
    sequence_number: int = proto.Field(
        proto.INT64,
        number=15,
    )
    turn_in_progress: bool = proto.Field(
        proto.BOOL,
        number=16,
    )


class CancelAssistantTurnRequest(proto.Message):
    r"""Request to cancel an assistant session's in-flight turn.

    Attributes:
        name (str):
            Required. The assistant session whose
            in-flight turn to cancel.
        turn_id (str):
            Optional. The turn to cancel; empty cancels
            whichever turn is running. A cancel naming a
            turn that is no longer the running one is a
            no-op.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    turn_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CancelAssistantTurnResponse(proto.Message):
    r"""Response for CancelAssistantTurn.

    Attributes:
        cancelled (bool):
            Whether an in-flight turn was found and asked
            to stop (directly on this task, or through an
            epoch preemption for a turn hosted elsewhere).
    """

    cancelled: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class TurnResumeSnapshot(proto.Message):
    r"""A compacted replay of an in-flight turn: everything needed to
    render the turn's visible output so far, plus the position live
    events continue from.

    Attributes:
        turn_id (str):
            Identifies the turn being attached to.
        resolved_sequence_number (int):
            The position this snapshot represents. Live events follow
            with sequence_number strictly greater than this. When lower
            than the resume_from_sequence_number the client requested,
            flushed progress lags what the client already rendered: the
            client must discard its rendered content of this turn beyond
            this position before applying the snapshot.
        events (MutableSequence[google.cloud.ces_v1beta.types.StreamChatAiAssistantResponse]):
            Compacted events reconstructing the turn's
            visible output, in render order, using the same
            event shapes as live streaming.
        orphan_deadline_time (google.protobuf.timestamp_pb2.Timestamp):
            When the turn will be wound down if no client
            remains attached.
    """

    turn_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    resolved_sequence_number: int = proto.Field(
        proto.INT64,
        number=2,
    )
    events: MutableSequence["StreamChatAiAssistantResponse"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="StreamChatAiAssistantResponse",
    )
    orphan_deadline_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


class TurnHandoffEvent(proto.Message):
    r"""Emitted before this task stops serving the stream mid-turn (e.g. a
    server restart). The turn's state is persisted; a reconnect carrying
    resume_from_sequence_number continues it on another task.

    Attributes:
        turn_id (str):
            Identifies the turn to resume.
        reason (google.cloud.ces_v1beta.types.TurnHandoffEvent.Reason):
            Why the stream is handing off.
    """

    class Reason(proto.Enum):
        r"""Why the stream is handing off.

        Values:
            REASON_UNSPECIFIED (0):
                Unspecified.
            SERVER_RESTART (1):
                The serving task is shutting down (release
                push or rescheduling).
        """

        REASON_UNSPECIFIED = 0
        SERVER_RESTART = 1

    turn_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    reason: Reason = proto.Field(
        proto.ENUM,
        number=2,
        enum=Reason,
    )


class TurnCompletedEvent(proto.Message):
    r"""Terminal event of a turn (see
    StreamChatAiAssistantResponse.turn_completed).

    Attributes:
        turn_id (str):
            Identifier of the turn that ended; matches
            TurnResumeSnapshot.turn_id and ActiveTurnInfo.turn_id.
        reason (google.cloud.ces_v1beta.types.TurnCompletedEvent.Reason):
            Why the turn ended.
        final_sequence_number (int):
            Sequence number of the last event the turn
            produced. A client whose cursor is lower missed
            content and should reload the session to see it.
    """

    class Reason(proto.Enum):
        r"""Why the turn ended, so a client that attached late can word
        the outcome instead of guessing from an empty stream.

        Values:
            REASON_UNSPECIFIED (0):
                Unspecified.
            COMPLETED (1):
                The turn ran to completion; the session holds
                its committed output.
            ABANDONED (2):
                No task was driving the turn any more; it was
                sealed to a committed partial and cannot be
                continued.
            RESUME_UNAVAILABLE (3):
                This server does not serve attach or resume
                for the session, so nothing was tailed; the
                client should reload the session instead.
        """

        REASON_UNSPECIFIED = 0
        COMPLETED = 1
        ABANDONED = 2
        RESUME_UNAVAILABLE = 3

    turn_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    reason: Reason = proto.Field(
        proto.ENUM,
        number=2,
        enum=Reason,
    )
    final_sequence_number: int = proto.Field(
        proto.INT64,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
