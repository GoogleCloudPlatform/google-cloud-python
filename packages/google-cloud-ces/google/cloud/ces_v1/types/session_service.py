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
import proto  # type: ignore

from google.cloud.ces_v1.types import common, example, mocks, search_suggestions

__protobuf__ = proto.module(
    package="google.cloud.ces.v1",
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
        mocked_tool_calls (MutableSequence[google.cloud.ces_v1.types.MockedToolCall]):
            Optional. All tool calls to mock for the
            duration of the session.
        unmatched_tool_call_behavior (google.cloud.ces_v1.types.MockConfig.UnmatchedToolCallBehavior):
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
        audio_encoding (google.cloud.ces_v1.types.AudioEncoding):
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
        audio_encoding (google.cloud.ces_v1.types.AudioEncoding):
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
        input_audio_config (google.cloud.ces_v1.types.InputAudioConfig):
            Optional. Configuration for processing the
            input audio.
        output_audio_config (google.cloud.ces_v1.types.OutputAudioConfig):
            Optional. Configuration for generating the
            output audio.
        historical_contexts (MutableSequence[google.cloud.ces_v1.types.Message]):
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
            agent][google.cloud.ces.v1.App.root_agent] of the app.
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
        remote_dialogflow_query_parameters (google.cloud.ces_v1.types.SessionConfig.RemoteDialogflowQueryParameters):
            Optional.
            `QueryParameters <https://cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#queryparameters>`__
            to send to the remote
            `Dialogflow <https://cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents>`__
            agent when the session control is transferred to the remote
            agent.
        enable_text_streaming (bool):
            Optional. Whether to enable streaming text outputs from the
            model. By default, text outputs from the model are collected
            before sending to the client. NOTE: This is only supported
            for text (non-voice) sessions via
            [StreamRunSession][google.cloud.ces.v1.SessionService.StreamRunSession]
            or
            [BidiRunSession][google.cloud.ces.v1.SessionService.BidiRunSession].
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


class ToolCalls(proto.Message):
    r"""Request for the client to execute the tools and return the
    execution results before continuing the session.

    Attributes:
        tool_calls (MutableSequence[google.cloud.ces_v1.types.ToolCall]):
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
        tool_responses (MutableSequence[google.cloud.ces_v1.types.ToolResponse]):
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
        cited_chunks (MutableSequence[google.cloud.ces_v1.types.Citations.CitedChunk]):
            List of cited pieces of information.
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

    cited_chunks: MutableSequence[CitedChunk] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=CitedChunk,
    )


class Event(proto.Message):
    r"""Event input.

    Attributes:
        event (str):
            Required. The name of the event.
    """

    event: str = proto.Field(
        proto.STRING,
        number=1,
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
        tool_responses (google.cloud.ces_v1.types.ToolResponses):
            Optional. Execution results for the tool
            calls from the client.

            This field is a member of `oneof`_ ``input_type``.
        image (google.cloud.ces_v1.types.Image):
            Optional. Image data from the end user.

            This field is a member of `oneof`_ ``input_type``.
        blob (google.cloud.ces_v1.types.Blob):
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
        event (google.cloud.ces_v1.types.Event):
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
    """

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
        tool_calls (google.cloud.ces_v1.types.ToolCalls):
            Request for the client to execute the tools.

            This field is a member of `oneof`_ ``output_type``.
        citations (google.cloud.ces_v1.types.Citations):
            Citations that provide the source information
            for the agent's generated text.

            This field is a member of `oneof`_ ``output_type``.
        google_search_suggestions (google.cloud.ces_v1.types.GoogleSearchSuggestions):
            The suggestions returned from Google Search as a result of
            invoking the
            [GoogleSearchTool][google.cloud.ces.v1.GoogleSearchTool].

            This field is a member of `oneof`_ ``output_type``.
        end_session (google.cloud.ces_v1.types.EndSession):
            Indicates the session has ended.

            This field is a member of `oneof`_ ``output_type``.
        payload (google.protobuf.struct_pb2.Struct):
            Custom payload with structured output from
            the CES agent.

            This field is a member of `oneof`_ ``output_type``.
        turn_index (int):
            Indicates the sequential order of
            conversation turn to which this output belongs
            to, starting from 1.
        turn_completed (bool):
            If true, the CES agent has detected the end
            of the current conversation turn and will
            provide no further output for this turn.
        diagnostic_info (google.cloud.ces_v1.types.SessionOutput.DiagnosticInfo):
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
            messages (MutableSequence[google.cloud.ces_v1.types.Message]):
                List of the messages that happened during the
                processing.
            root_span (google.cloud.ces_v1.types.Span):
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
    [SessionService.RunSession][google.cloud.ces.v1.SessionService.RunSession].

    Attributes:
        config (google.cloud.ces_v1.types.SessionConfig):
            Required. The configuration for the session.
        inputs (MutableSequence[google.cloud.ces_v1.types.SessionInput]):
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
    [SessionService.RunSession][google.cloud.ces.v1.SessionService.RunSession].

    Attributes:
        outputs (MutableSequence[google.cloud.ces_v1.types.SessionOutput]):
            Outputs for the session.
    """

    outputs: MutableSequence["SessionOutput"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SessionOutput",
    )


class BidiSessionClientMessage(proto.Message):
    r"""The top-level message sent by the client for the
    [SessionService.BidiRunSession][google.cloud.ces.v1.SessionService.BidiRunSession]
    method.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        config (google.cloud.ces_v1.types.SessionConfig):
            Optional. The initial config message for the
            session.

            This field is a member of `oneof`_ ``message_type``.
        realtime_input (google.cloud.ces_v1.types.SessionInput):
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
    [SessionService.BidiRunSession][google.cloud.ces.v1.SessionService.BidiRunSession]
    method.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        session_output (google.cloud.ces_v1.types.SessionOutput):
            Optional. Processing result from the CES
            agent.

            This field is a member of `oneof`_ ``message_type``.
        recognition_result (google.cloud.ces_v1.types.RecognitionResult):
            Optional. Realtime speech recognition result
            for the audio input.

            This field is a member of `oneof`_ ``message_type``.
        interruption_signal (google.cloud.ces_v1.types.InterruptionSignal):
            Optional. Indicates the agent's audio
            response has been interrupted.

            This field is a member of `oneof`_ ``message_type``.
        end_session (google.cloud.ces_v1.types.EndSession):
            Optional. Indicates that the session has
            ended.

            This field is a member of `oneof`_ ``message_type``.
        go_away (google.cloud.ces_v1.types.GoAway):
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


__all__ = tuple(sorted(__protobuf__.manifest))
