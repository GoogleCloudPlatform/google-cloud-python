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
import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.rpc.status_pb2 as status_pb2  # type: ignore
import google.type.latlng_pb2 as latlng_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.dialogflowcx_v3beta1.types import (
    advanced_settings as gcdc_advanced_settings,
)
from google.cloud.dialogflowcx_v3beta1.types import (
    audio_config,
    data_store_connection,
    example,
    flow,
    generative_settings,
    page,
    response_message,
    session_entity_type,
    tool_call,
    trace,
)
from google.cloud.dialogflowcx_v3beta1.types import intent as gcdc_intent

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.cx.v3beta1",
    manifest={
        "DetectIntentResponseView",
        "AnswerFeedback",
        "SubmitAnswerFeedbackRequest",
        "DetectIntentRequest",
        "DetectIntentResponse",
        "StreamingDetectIntentRequest",
        "CloudConversationDebuggingInfo",
        "StreamingDetectIntentResponse",
        "StreamingRecognitionResult",
        "QueryParameters",
        "SearchConfig",
        "BoostSpec",
        "BoostSpecs",
        "FilterSpecs",
        "QueryInput",
        "GenerativeInfo",
        "QueryResult",
        "TextInput",
        "IntentInput",
        "AudioInput",
        "EventInput",
        "DtmfInput",
        "Match",
        "MatchIntentRequest",
        "MatchIntentResponse",
        "FulfillIntentRequest",
        "FulfillIntentResponse",
        "SentimentAnalysisResult",
    },
)


class DetectIntentResponseView(proto.Enum):
    r"""The response view specifies which fields in the
    [QueryResult][google.cloud.dialogflow.cx.v3beta1.QueryResult] to
    return.

    Values:
        DETECT_INTENT_RESPONSE_VIEW_UNSPECIFIED (0):
            Not specified. ``DETECT_INTENT_RESPONSE_VIEW_DEFAULT`` will
            be used.
        DETECT_INTENT_RESPONSE_VIEW_FULL (1):
            Full response view includes all fields.
        DETECT_INTENT_RESPONSE_VIEW_BASIC (2):
            Basic response view omits the following fields:
            -----------------------------------------------

            [QueryResult.diagnostic_info][google.cloud.dialogflow.cx.v3beta1.QueryResult.diagnostic_info]
            ---------------------------------------------------------------------------------------------

            [QueryResult.generative_info][google.cloud.dialogflow.cx.v3beta1.QueryResult.generative_info]
            ---------------------------------------------------------------------------------------------

            [QueryResult.trace_blocks][google.cloud.dialogflow.cx.v3beta1.QueryResult.trace_blocks]
            ---------------------------------------------------------------------------------------

            [QueryResult.data_store_connection_signals][google.cloud.dialogflow.cx.v3beta1.QueryResult.data_store_connection_signals]
        DETECT_INTENT_RESPONSE_VIEW_DEFAULT (3):
            Default response view omits the following fields:
            -------------------------------------------------

            [QueryResult.trace_blocks][google.cloud.dialogflow.cx.v3beta1.QueryResult.trace_blocks]
    """

    DETECT_INTENT_RESPONSE_VIEW_UNSPECIFIED = 0
    DETECT_INTENT_RESPONSE_VIEW_FULL = 1
    DETECT_INTENT_RESPONSE_VIEW_BASIC = 2
    DETECT_INTENT_RESPONSE_VIEW_DEFAULT = 3


class AnswerFeedback(proto.Message):
    r"""Stores information about feedback provided by users about a
    response.

    Attributes:
        rating (google.cloud.dialogflowcx_v3beta1.types.AnswerFeedback.Rating):
            Optional. Rating from user for the specific
            Dialogflow response.
        rating_reason (google.cloud.dialogflowcx_v3beta1.types.AnswerFeedback.RatingReason):
            Optional. In case of thumbs down rating
            provided, users can optionally provide context
            about the rating.
        custom_rating (str):
            Optional. Custom rating from the user about
            the provided answer, with maximum length of 1024
            characters. For example, client could use a
            customized JSON object to indicate the rating.
    """

    class Rating(proto.Enum):
        r"""Represents thumbs up/down rating provided by user about a
        response.

        Values:
            RATING_UNSPECIFIED (0):
                Rating not specified.
            THUMBS_UP (1):
                Thumbs up feedback from user.
            THUMBS_DOWN (2):
                Thumbs down feedback from user.
        """

        RATING_UNSPECIFIED = 0
        THUMBS_UP = 1
        THUMBS_DOWN = 2

    class RatingReason(proto.Message):
        r"""Stores extra information about why users provided thumbs down
        rating.

        Attributes:
            reason_labels (MutableSequence[str]):
                Optional. Custom reason labels for thumbs
                down rating provided by the user. The maximum
                number of labels allowed is 10 and the maximum
                length of a single label is 128 characters.
            feedback (str):
                Optional. Additional feedback about the rating. This field
                can be populated without choosing a predefined ``reason``.
        """

        reason_labels: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=3,
        )
        feedback: str = proto.Field(
            proto.STRING,
            number=2,
        )

    rating: Rating = proto.Field(
        proto.ENUM,
        number=1,
        enum=Rating,
    )
    rating_reason: RatingReason = proto.Field(
        proto.MESSAGE,
        number=2,
        message=RatingReason,
    )
    custom_rating: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SubmitAnswerFeedbackRequest(proto.Message):
    r"""The request to set the feedback for a bot answer.

    Attributes:
        session (str):
            Required. The name of the session the
            feedback was sent to.
        response_id (str):
            Required. ID of the response to update its feedback. This is
            the same as DetectIntentResponse.response_id.
        answer_feedback (google.cloud.dialogflowcx_v3beta1.types.AnswerFeedback):
            Required. Feedback provided for a bot answer.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The mask to control which fields to
            update. If the mask is not present, all fields
            will be updated.
    """

    session: str = proto.Field(
        proto.STRING,
        number=1,
    )
    response_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    answer_feedback: "AnswerFeedback" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="AnswerFeedback",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=4,
        message=field_mask_pb2.FieldMask,
    )


class DetectIntentRequest(proto.Message):
    r"""The request to detect user's intent.

    Attributes:
        session (str):
            Required. The name of the session this query is sent to.
            Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/sessions/<SessionID>``
            or
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>/sessions/<SessionID>``.
            If ``Environment ID`` is not specified, we assume default
            'draft' environment. It's up to the API caller to choose an
            appropriate ``Session ID``. It can be a random number or
            some type of session identifiers (preferably hashed). The
            length of the ``Session ID`` must not exceed 36 characters.

            For more information, see the `sessions
            guide <https://cloud.google.com/dialogflow/cx/docs/concept/session>`__.

            Note: Always use agent versions for production traffic. See
            `Versions and
            environments <https://cloud.google.com/dialogflow/cx/docs/concept/version>`__.
        query_params (google.cloud.dialogflowcx_v3beta1.types.QueryParameters):
            The parameters of this query.
        query_input (google.cloud.dialogflowcx_v3beta1.types.QueryInput):
            Required. The input specification.
        output_audio_config (google.cloud.dialogflowcx_v3beta1.types.OutputAudioConfig):
            Instructs the speech synthesizer how to
            generate the output audio.
        response_view (google.cloud.dialogflowcx_v3beta1.types.DetectIntentResponseView):
            Optional. Specifies which fields in the
            [QueryResult][google.cloud.dialogflow.cx.v3beta1.QueryResult]
            to return. If not set, the default is
            DETECT_INTENT_RESPONSE_VIEW_FULL.
    """

    session: str = proto.Field(
        proto.STRING,
        number=1,
    )
    query_params: "QueryParameters" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="QueryParameters",
    )
    query_input: "QueryInput" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="QueryInput",
    )
    output_audio_config: audio_config.OutputAudioConfig = proto.Field(
        proto.MESSAGE,
        number=4,
        message=audio_config.OutputAudioConfig,
    )
    response_view: "DetectIntentResponseView" = proto.Field(
        proto.ENUM,
        number=9,
        enum="DetectIntentResponseView",
    )


class DetectIntentResponse(proto.Message):
    r"""The message returned from the DetectIntent method.

    Attributes:
        response_id (str):
            Output only. The unique identifier of the
            response. It can be used to locate a response in
            the training example set or for reporting
            issues.
        query_result (google.cloud.dialogflowcx_v3beta1.types.QueryResult):
            The result of the conversational query.
        output_audio (bytes):
            The audio data bytes encoded as specified in the request.
            Note: The output audio is generated based on the values of
            default platform text responses found in the
            [``query_result.response_messages``][google.cloud.dialogflow.cx.v3beta1.QueryResult.response_messages]
            field. If multiple default text responses exist, they will
            be concatenated when generating audio. If no default
            platform text responses exist, the generated audio content
            will be empty.

            In some scenarios, multiple output audio fields may be
            present in the response structure. In these cases, only the
            top-most-level audio output has content.
        output_audio_config (google.cloud.dialogflowcx_v3beta1.types.OutputAudioConfig):
            The config used by the speech synthesizer to
            generate the output audio.
        response_type (google.cloud.dialogflowcx_v3beta1.types.DetectIntentResponse.ResponseType):
            Response type.
        allow_cancellation (bool):
            Indicates whether the partial response can be
            cancelled when a later response arrives. e.g. if
            the agent specified some music as partial
            response, it can be cancelled.
    """

    class ResponseType(proto.Enum):
        r"""Represents different DetectIntentResponse types.

        Values:
            RESPONSE_TYPE_UNSPECIFIED (0):
                Not specified. This should never happen.
            PARTIAL (1):
                Partial response. e.g. Aggregated responses in a Fulfillment
                that enables ``return_partial_response`` can be returned as
                partial response. WARNING: partial response is not eligible
                for barge-in.
            FINAL (2):
                Final response.
        """

        RESPONSE_TYPE_UNSPECIFIED = 0
        PARTIAL = 1
        FINAL = 2

    response_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    query_result: "QueryResult" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="QueryResult",
    )
    output_audio: bytes = proto.Field(
        proto.BYTES,
        number=4,
    )
    output_audio_config: audio_config.OutputAudioConfig = proto.Field(
        proto.MESSAGE,
        number=5,
        message=audio_config.OutputAudioConfig,
    )
    response_type: ResponseType = proto.Field(
        proto.ENUM,
        number=6,
        enum=ResponseType,
    )
    allow_cancellation: bool = proto.Field(
        proto.BOOL,
        number=7,
    )


class StreamingDetectIntentRequest(proto.Message):
    r"""The top-level message sent by the client to the
    [Sessions.StreamingDetectIntent][google.cloud.dialogflow.cx.v3beta1.Sessions.StreamingDetectIntent]
    method.

    Multiple request messages should be sent in order:

    1. The first message must contain
       [session][google.cloud.dialogflow.cx.v3beta1.StreamingDetectIntentRequest.session],
       [query_input][google.cloud.dialogflow.cx.v3beta1.StreamingDetectIntentRequest.query_input]
       plus optionally
       [query_params][google.cloud.dialogflow.cx.v3beta1.StreamingDetectIntentRequest.query_params].
       If the client wants to receive an audio response, it should also
       contain
       [output_audio_config][google.cloud.dialogflow.cx.v3beta1.StreamingDetectIntentRequest.output_audio_config].

    2. If
       [query_input][google.cloud.dialogflow.cx.v3beta1.StreamingDetectIntentRequest.query_input]
       was set to
       [query_input.audio.config][google.cloud.dialogflow.cx.v3beta1.AudioInput.config],
       all subsequent messages must contain
       [query_input.audio.audio][google.cloud.dialogflow.cx.v3beta1.AudioInput.audio]
       to continue with Speech recognition. If you decide to rather
       detect an intent from text input after you already started Speech
       recognition, please send a message with
       [query_input.text][google.cloud.dialogflow.cx.v3beta1.QueryInput.text].

       However, note that:

       - Dialogflow will bill you for the audio duration so far.
       - Dialogflow discards all Speech recognition results in favor of
         the input text.
       - Dialogflow will use the language code from the first message.

    After you sent all input, you must half-close or abort the request
    stream.

    Attributes:
        session (str):
            The name of the session this query is sent to. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/sessions/<SessionID>``
            or
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>/sessions/<SessionID>``.
            If ``Environment ID`` is not specified, we assume default
            'draft' environment. It's up to the API caller to choose an
            appropriate ``Session ID``. It can be a random number or
            some type of session identifiers (preferably hashed). The
            length of the ``Session ID`` must not exceed 36 characters.
            Note: session must be set in the first request.

            For more information, see the `sessions
            guide <https://cloud.google.com/dialogflow/cx/docs/concept/session>`__.

            Note: Always use agent versions for production traffic. See
            `Versions and
            environments <https://cloud.google.com/dialogflow/cx/docs/concept/version>`__.
        query_params (google.cloud.dialogflowcx_v3beta1.types.QueryParameters):
            The parameters of this query.
        query_input (google.cloud.dialogflowcx_v3beta1.types.QueryInput):
            Required. The input specification.
        output_audio_config (google.cloud.dialogflowcx_v3beta1.types.OutputAudioConfig):
            Instructs the speech synthesizer how to
            generate the output audio.
        enable_partial_response (bool):
            Enable partial detect intent response. If this flag is not
            enabled, response stream still contains only one final
            ``DetectIntentResponse`` even if some ``Fulfillment``\ s in
            the agent have been configured to return partial responses.
        enable_debugging_info (bool):
            If true, ``StreamingDetectIntentResponse.debugging_info``
            will get populated.
        response_view (google.cloud.dialogflowcx_v3beta1.types.DetectIntentResponseView):
            Optional. Specifies which fields in the
            [QueryResult][google.cloud.dialogflow.cx.v3beta1.QueryResult]
            to return. If not set, the default is
            DETECT_INTENT_RESPONSE_VIEW_FULL.
    """

    session: str = proto.Field(
        proto.STRING,
        number=1,
    )
    query_params: "QueryParameters" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="QueryParameters",
    )
    query_input: "QueryInput" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="QueryInput",
    )
    output_audio_config: audio_config.OutputAudioConfig = proto.Field(
        proto.MESSAGE,
        number=4,
        message=audio_config.OutputAudioConfig,
    )
    enable_partial_response: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    enable_debugging_info: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    response_view: "DetectIntentResponseView" = proto.Field(
        proto.ENUM,
        number=16,
        enum="DetectIntentResponseView",
    )


class CloudConversationDebuggingInfo(proto.Message):
    r"""Cloud conversation info for easier debugging. It will get populated
    in ``StreamingDetectIntentResponse`` or
    ``StreamingAnalyzeContentResponse`` when the flag
    ``enable_debugging_info`` is set to true in corresponding requests.

    Attributes:
        audio_data_chunks (int):
            Number of input audio data chunks in
            streaming requests.
        result_end_time_offset (google.protobuf.duration_pb2.Duration):
            Time offset of the end of speech utterance
            relative to the beginning of the first audio
            chunk.
        first_audio_duration (google.protobuf.duration_pb2.Duration):
            Duration of first audio chunk.
        single_utterance (bool):
            Whether client used single utterance mode.
        speech_partial_results_end_times (MutableSequence[google.protobuf.duration_pb2.Duration]):
            Time offsets of the speech partial results
            relative to the beginning of the stream.
        speech_final_results_end_times (MutableSequence[google.protobuf.duration_pb2.Duration]):
            Time offsets of the speech final results (is_final=true)
            relative to the beginning of the stream.
        partial_responses (int):
            Total number of partial responses.
        speaker_id_passive_latency_ms_offset (int):
            Time offset of Speaker ID stream close time
            relative to the Speech stream close time in
            milliseconds. Only meaningful for conversations
            involving passive verification.
        bargein_event_triggered (bool):
            Whether a barge-in event is triggered in this
            request.
        speech_single_utterance (bool):
            Whether speech uses single utterance mode.
        dtmf_partial_results_times (MutableSequence[google.protobuf.duration_pb2.Duration]):
            Time offsets of the DTMF partial results
            relative to the beginning of the stream.
        dtmf_final_results_times (MutableSequence[google.protobuf.duration_pb2.Duration]):
            Time offsets of the DTMF final results
            relative to the beginning of the stream.
        single_utterance_end_time_offset (google.protobuf.duration_pb2.Duration):
            Time offset of the end-of-single-utterance
            signal relative to the beginning of the stream.
        no_speech_timeout (google.protobuf.duration_pb2.Duration):
            No speech timeout settings for the stream.
        endpointing_timeout (google.protobuf.duration_pb2.Duration):
            Speech endpointing timeout settings for the
            stream.
        is_input_text (bool):
            Whether the streaming terminates with an
            injected text query.
        client_half_close_time_offset (google.protobuf.duration_pb2.Duration):
            Client half close time in terms of input
            audio duration.
        client_half_close_streaming_time_offset (google.protobuf.duration_pb2.Duration):
            Client half close time in terms of API
            streaming duration.
    """

    audio_data_chunks: int = proto.Field(
        proto.INT32,
        number=1,
    )
    result_end_time_offset: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )
    first_audio_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=3,
        message=duration_pb2.Duration,
    )
    single_utterance: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    speech_partial_results_end_times: MutableSequence[duration_pb2.Duration] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=6,
            message=duration_pb2.Duration,
        )
    )
    speech_final_results_end_times: MutableSequence[duration_pb2.Duration] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=7,
            message=duration_pb2.Duration,
        )
    )
    partial_responses: int = proto.Field(
        proto.INT32,
        number=8,
    )
    speaker_id_passive_latency_ms_offset: int = proto.Field(
        proto.INT32,
        number=9,
    )
    bargein_event_triggered: bool = proto.Field(
        proto.BOOL,
        number=10,
    )
    speech_single_utterance: bool = proto.Field(
        proto.BOOL,
        number=11,
    )
    dtmf_partial_results_times: MutableSequence[duration_pb2.Duration] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=12,
            message=duration_pb2.Duration,
        )
    )
    dtmf_final_results_times: MutableSequence[duration_pb2.Duration] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=13,
            message=duration_pb2.Duration,
        )
    )
    single_utterance_end_time_offset: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=14,
        message=duration_pb2.Duration,
    )
    no_speech_timeout: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=15,
        message=duration_pb2.Duration,
    )
    endpointing_timeout: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=19,
        message=duration_pb2.Duration,
    )
    is_input_text: bool = proto.Field(
        proto.BOOL,
        number=16,
    )
    client_half_close_time_offset: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=17,
        message=duration_pb2.Duration,
    )
    client_half_close_streaming_time_offset: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=18,
        message=duration_pb2.Duration,
    )


class StreamingDetectIntentResponse(proto.Message):
    r"""The top-level message returned from the
    [StreamingDetectIntent][google.cloud.dialogflow.cx.v3beta1.Sessions.StreamingDetectIntent]
    method.

    Multiple response messages can be returned in order:

    - If the ``StreamingDetectIntentRequest.query_input.audio`` field
      was set, the first M messages contain ``recognition_result``. Each
      ``recognition_result`` represents a more complete transcript of
      what the user said. The last ``recognition_result`` has
      ``is_final`` set to ``true``.

    - If the ``StreamingDetectIntentRequest.enable_partial_response``
      field was true, the ``detect_intent_response`` field is populated
      for each of the following N responses, where 0 <= N <= 5. These
      responses set the
      [DetectIntentResponse.response_type][google.cloud.dialogflow.cx.v3beta1.DetectIntentResponse.response_type]
      field to ``PARTIAL``.

    For the last response message, the ``detect_intent_response`` is
    fully populated, and
    [DetectIntentResponse.response_type][google.cloud.dialogflow.cx.v3beta1.DetectIntentResponse.response_type]
    is set to ``FINAL``.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        recognition_result (google.cloud.dialogflowcx_v3beta1.types.StreamingRecognitionResult):
            The result of speech recognition.

            This field is a member of `oneof`_ ``response``.
        detect_intent_response (google.cloud.dialogflowcx_v3beta1.types.DetectIntentResponse):
            The response from detect intent.

            This field is a member of `oneof`_ ``response``.
        debugging_info (google.cloud.dialogflowcx_v3beta1.types.CloudConversationDebuggingInfo):
            Debugging info that would get populated when
            ``StreamingDetectIntentRequest.enable_debugging_info`` is
            set to true.
    """

    recognition_result: "StreamingRecognitionResult" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="response",
        message="StreamingRecognitionResult",
    )
    detect_intent_response: "DetectIntentResponse" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="response",
        message="DetectIntentResponse",
    )
    debugging_info: "CloudConversationDebuggingInfo" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="CloudConversationDebuggingInfo",
    )


class StreamingRecognitionResult(proto.Message):
    r"""Contains a speech recognition result corresponding to a portion of
    the audio that is currently being processed or an indication that
    this is the end of the single requested utterance.

    While end-user audio is being processed, Dialogflow sends a series
    of results. Each result may contain a ``transcript`` value. A
    transcript represents a portion of the utterance. While the
    recognizer is processing audio, transcript values may be interim
    values or finalized values. Once a transcript is finalized, the
    ``is_final`` value is set to true and processing continues for the
    next transcript.

    If
    ``StreamingDetectIntentRequest.query_input.audio.config.single_utterance``
    was true, and the recognizer has completed processing audio, the
    ``message_type`` value is set to \`END_OF_SINGLE_UTTERANCE and the
    following (last) result contains the last finalized transcript.

    The complete end-user utterance is determined by concatenating the
    finalized transcript values received for the series of results.

    In the following example, single utterance is enabled. In the case
    where single utterance is not enabled, result 7 would not occur.

    ::

       Num | transcript              | message_type            | is_final
       --- | ----------------------- | ----------------------- | --------
       1   | "tube"                  | TRANSCRIPT              | false
       2   | "to be a"               | TRANSCRIPT              | false
       3   | "to be"                 | TRANSCRIPT              | false
       4   | "to be or not to be"    | TRANSCRIPT              | true
       5   | "that's"                | TRANSCRIPT              | false
       6   | "that is                | TRANSCRIPT              | false
       7   | unset                   | END_OF_SINGLE_UTTERANCE | unset
       8   | " that is the question" | TRANSCRIPT              | true

    Concatenating the finalized transcripts with ``is_final`` set to
    true, the complete utterance becomes "to be or not to be that is the
    question".

    Attributes:
        message_type (google.cloud.dialogflowcx_v3beta1.types.StreamingRecognitionResult.MessageType):
            Type of the result message.
        transcript (str):
            Transcript text representing the words that the user spoke.
            Populated if and only if ``message_type`` = ``TRANSCRIPT``.
        is_final (bool):
            If ``false``, the ``StreamingRecognitionResult`` represents
            an interim result that may change. If ``true``, the
            recognizer will not return any further hypotheses about this
            piece of the audio. May only be populated for
            ``message_type`` = ``TRANSCRIPT``.
        confidence (float):
            The Speech confidence between 0.0 and 1.0 for the current
            portion of audio. A higher number indicates an estimated
            greater likelihood that the recognized words are correct.
            The default of 0.0 is a sentinel value indicating that
            confidence was not set.

            This field is typically only provided if ``is_final`` is
            true and you should not rely on it being accurate or even
            set.
        stability (float):
            An estimate of the likelihood that the speech recognizer
            will not change its guess about this interim recognition
            result:

            - If the value is unspecified or 0.0, Dialogflow didn't
              compute the stability. In particular, Dialogflow will only
              provide stability for ``TRANSCRIPT`` results with
              ``is_final = false``.
            - Otherwise, the value is in (0.0, 1.0] where 0.0 means
              completely unstable and 1.0 means completely stable.
        speech_word_info (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.SpeechWordInfo]):
            Word-specific information for the words recognized by Speech
            in
            [transcript][google.cloud.dialogflow.cx.v3beta1.StreamingRecognitionResult.transcript].
            Populated if and only if ``message_type`` = ``TRANSCRIPT``
            and [InputAudioConfig.enable_word_info] is set.
        speech_end_offset (google.protobuf.duration_pb2.Duration):
            Time offset of the end of this Speech recognition result
            relative to the beginning of the audio. Only populated for
            ``message_type`` = ``TRANSCRIPT``.
        language_code (str):
            Detected language code for the transcript.
    """

    class MessageType(proto.Enum):
        r"""Type of the response message.

        Values:
            MESSAGE_TYPE_UNSPECIFIED (0):
                Not specified. Should never be used.
            TRANSCRIPT (1):
                Message contains a (possibly partial)
                transcript.
            END_OF_SINGLE_UTTERANCE (2):
                This event indicates that the server has detected the end of
                the user's speech utterance and expects no additional
                speech. Therefore, the server will not process additional
                audio (although it may subsequently return additional
                results). The client should stop sending additional audio
                data, half-close the gRPC connection, and wait for any
                additional results until the server closes the gRPC
                connection. This message is only sent if
                [``single_utterance``][google.cloud.dialogflow.cx.v3beta1.InputAudioConfig.single_utterance]
                was set to ``true``, and is not used otherwise.
        """

        MESSAGE_TYPE_UNSPECIFIED = 0
        TRANSCRIPT = 1
        END_OF_SINGLE_UTTERANCE = 2

    message_type: MessageType = proto.Field(
        proto.ENUM,
        number=1,
        enum=MessageType,
    )
    transcript: str = proto.Field(
        proto.STRING,
        number=2,
    )
    is_final: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    confidence: float = proto.Field(
        proto.FLOAT,
        number=4,
    )
    stability: float = proto.Field(
        proto.FLOAT,
        number=6,
    )
    speech_word_info: MutableSequence[audio_config.SpeechWordInfo] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=7,
            message=audio_config.SpeechWordInfo,
        )
    )
    speech_end_offset: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=8,
        message=duration_pb2.Duration,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=10,
    )


class QueryParameters(proto.Message):
    r"""Represents the parameters of a conversational query.

    Attributes:
        time_zone (str):
            The time zone of this conversational query from the `time
            zone database <https://www.iana.org/time-zones>`__, e.g.,
            America/New_York, Europe/Paris. If not provided, the time
            zone specified in the agent is used.
        geo_location (google.type.latlng_pb2.LatLng):
            The geo location of this conversational
            query.
        session_entity_types (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.SessionEntityType]):
            Additional session entity types to replace or
            extend developer entity types with. The entity
            synonyms apply to all languages and persist for
            the session of this query.
        payload (google.protobuf.struct_pb2.Struct):
            This field can be used to pass custom data into the webhook
            associated with the agent. Arbitrary JSON objects are
            supported. Some integrations that query a Dialogflow agent
            may provide additional information in the payload. In
            particular, for the Dialogflow Phone Gateway integration,
            this field has the form:

            ::

               {
                "telephony": {
                  "caller_id": "+18558363987"
                }
               }
        parameters (google.protobuf.struct_pb2.Struct):
            Additional parameters to be put into [session
            parameters][SessionInfo.parameters]. To remove a parameter
            from the session, clients should explicitly set the
            parameter value to null.

            You can reference the session parameters in the agent with
            the following format: $session.params.parameter-id.

            Depending on your protocol or client library language, this
            is a map, associative array, symbol table, dictionary, or
            JSON object composed of a collection of (MapKey, MapValue)
            pairs:

            - MapKey type: string
            - MapKey value: parameter name
            - MapValue type: If parameter's entity type is a composite
              entity then use map, otherwise, depending on the parameter
              value type, it could be one of string, number, boolean,
              null, list or map.
            - MapValue value: If parameter's entity type is a composite
              entity then use map from composite entity property names
              to property values, otherwise, use parameter value.
        parameter_scope (str):
            Scope for the parameters. If not specified, parameters will
            be treated as session parameters. Parameters with custom
            scope will not be put into [session
            parameters][google.cloud.dialogflow.cx.v3beta1.SessionInfo.parameters].

            You can reference the parameters with custom scope in the
            agent with the following format:
            $parameter-scope.params.parameter-id.
        current_page (str):
            The unique identifier of the
            [page][google.cloud.dialogflow.cx.v3beta1.Page] to override
            the [current page][QueryResult.current_page] in the session.
            Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/pages/<PageID>``.

            If ``current_page`` is specified, the previous state of the
            session will be ignored by Dialogflow, including the
            [previous page][QueryResult.current_page] and the [previous
            session parameters][QueryResult.parameters]. In most cases,
            [current_page][google.cloud.dialogflow.cx.v3beta1.QueryParameters.current_page]
            and
            [parameters][google.cloud.dialogflow.cx.v3beta1.QueryParameters.parameters]
            should be configured together to direct a session to a
            specific state.
        disable_webhook (bool):
            Whether to disable webhook calls for this
            request.
        analyze_query_text_sentiment (bool):
            Configures whether sentiment analysis should
            be performed. If not provided, sentiment
            analysis is not performed.
        webhook_headers (MutableMapping[str, str]):
            This field can be used to pass HTTP headers
            for a webhook call. These headers will be sent
            to webhook along with the headers that have been
            configured through Dialogflow web console. The
            headers defined within this field will overwrite
            the headers configured through Dialogflow
            console if there is a conflict. Header names are
            case-insensitive. Google's specified headers are
            not allowed. Including: "Host",
            "Content-Length", "Connection", "From",
            "User-Agent", "Accept-Encoding",
            "If-Modified-Since", "If-None-Match",
            "X-Forwarded-For", etc.
        flow_versions (MutableSequence[str]):
            A list of flow versions to override for the request. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/versions/<VersionID>``.

            If version 1 of flow X is included in this list, the traffic
            of flow X will go through version 1 regardless of the
            version configuration in the environment. Each flow can have
            at most one version specified in this list.
        current_playbook (str):
            Optional. The unique identifier of the
            [playbook][google.cloud.dialogflow.cx.v3beta1.Playbook] to
            start or continue the session with. If ``current_playbook``
            is specified, the previous state of the session will be
            ignored by Dialogflow.

            Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>``.
        llm_model_settings (google.cloud.dialogflowcx_v3beta1.types.LlmModelSettings):
            Optional. Use the specified LLM model
            settings for processing the request.
        channel (str):
            The channel which this query is for.

            If specified, only the
            [ResponseMessage][google.cloud.dialogflow.cx.v3beta1.ResponseMessage]
            associated with the channel will be returned. If no
            [ResponseMessage][google.cloud.dialogflow.cx.v3beta1.ResponseMessage]
            is associated with the channel, it falls back to the
            [ResponseMessage][google.cloud.dialogflow.cx.v3beta1.ResponseMessage]
            with unspecified channel.

            If unspecified, the
            [ResponseMessage][google.cloud.dialogflow.cx.v3beta1.ResponseMessage]
            with unspecified channel will be returned.
        session_ttl (google.protobuf.duration_pb2.Duration):
            Optional. Configure lifetime of the
            Dialogflow session. By default, a Dialogflow
            session remains active and its data is stored
            for 30 minutes after the last request is sent
            for the session. This value should be no longer
            than 1 day.
        end_user_metadata (google.protobuf.struct_pb2.Struct):
            Optional. Information about the end-user to improve the
            relevance and accuracy of generative answers.

            This will be interpreted and used by a language model, so,
            for good results, the data should be self-descriptive, and
            in a simple structure.

            Example:

            .. code:: json

               {
                 "subscription plan": "Business Premium Plus",
                 "devices owned": [
                   {"model": "Google Pixel 7"},
                   {"model": "Google Pixel Tablet"}
                 ]
               }
        search_config (google.cloud.dialogflowcx_v3beta1.types.SearchConfig):
            Optional. Search configuration for UCS search
            queries.
        populate_data_store_connection_signals (bool):
            Optional. If set to true and data stores are involved in
            serving the request then
            DetectIntentResponse.query_result.data_store_connection_signals
            will be filled with data that can help evaluations.
    """

    time_zone: str = proto.Field(
        proto.STRING,
        number=1,
    )
    geo_location: latlng_pb2.LatLng = proto.Field(
        proto.MESSAGE,
        number=2,
        message=latlng_pb2.LatLng,
    )
    session_entity_types: MutableSequence[session_entity_type.SessionEntityType] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message=session_entity_type.SessionEntityType,
        )
    )
    payload: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=4,
        message=struct_pb2.Struct,
    )
    parameters: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=5,
        message=struct_pb2.Struct,
    )
    parameter_scope: str = proto.Field(
        proto.STRING,
        number=12,
    )
    current_page: str = proto.Field(
        proto.STRING,
        number=6,
    )
    disable_webhook: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    analyze_query_text_sentiment: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    webhook_headers: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=10,
    )
    flow_versions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=14,
    )
    current_playbook: str = proto.Field(
        proto.STRING,
        number=19,
    )
    llm_model_settings: generative_settings.LlmModelSettings = proto.Field(
        proto.MESSAGE,
        number=21,
        message=generative_settings.LlmModelSettings,
    )
    channel: str = proto.Field(
        proto.STRING,
        number=15,
    )
    session_ttl: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=16,
        message=duration_pb2.Duration,
    )
    end_user_metadata: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=18,
        message=struct_pb2.Struct,
    )
    search_config: "SearchConfig" = proto.Field(
        proto.MESSAGE,
        number=20,
        message="SearchConfig",
    )
    populate_data_store_connection_signals: bool = proto.Field(
        proto.BOOL,
        number=25,
    )


class SearchConfig(proto.Message):
    r"""Search configuration for UCS search queries.

    Attributes:
        boost_specs (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.BoostSpecs]):
            Optional. Boosting configuration for the
            datastores.
            Maps from datastore name to their boost
            configuration. Do not specify more than one
            BoostSpecs for each datastore name. If multiple
            BoostSpecs are provided for the same datastore
            name, the behavior is undefined.
        filter_specs (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.FilterSpecs]):
            Optional. Filter configuration for the
            datastores.
            Maps from datastore name to the filter
            expression for that datastore. Do not specify
            more than one FilterSpecs for each datastore
            name. If multiple FilterSpecs are provided for
            the same datastore name, the behavior is
            undefined.
    """

    boost_specs: MutableSequence["BoostSpecs"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="BoostSpecs",
    )
    filter_specs: MutableSequence["FilterSpecs"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="FilterSpecs",
    )


class BoostSpec(proto.Message):
    r"""Boost specification to boost certain documents.
    A copy of google.cloud.discoveryengine.v1main.BoostSpec, field
    documentation is available at
    https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/BoostSpec

    Attributes:
        condition_boost_specs (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.BoostSpec.ConditionBoostSpec]):
            Optional. Condition boost specifications. If
            a document matches multiple conditions in the
            specifications, boost scores from these
            specifications are all applied and combined in a
            non-linear way. Maximum number of specifications
            is 20.
    """

    class ConditionBoostSpec(proto.Message):
        r"""Boost applies to documents which match a condition.

        Attributes:
            condition (str):
                Optional. An expression which specifies a boost condition.
                The syntax and supported fields are the same as a filter
                expression. Examples:

                - To boost documents with document ID "doc_1" or "doc_2",
                  and color "Red" or "Blue":

                  - (id: ANY("doc_1", "doc_2")) AND (color:
                    ANY("Red","Blue"))
            boost (float):
                Optional. Strength of the condition boost, which should be
                in [-1, 1]. Negative boost means demotion. Default is 0.0.

                Setting to 1.0 gives the document a big promotion. However,
                it does not necessarily mean that the boosted document will
                be the top result at all times, nor that other documents
                will be excluded. Results could still be shown even when
                none of them matches the condition. And results that are
                significantly more relevant to the search query can still
                trump your heavily favored but irrelevant documents.

                Setting to -1.0 gives the document a big demotion. However,
                results that are deeply relevant might still be shown. The
                document will have an upstream battle to get a fairly high
                ranking, but it is not blocked out completely.

                Setting to 0.0 means no boost applied. The boosting
                condition is ignored.
            boost_control_spec (google.cloud.dialogflowcx_v3beta1.types.BoostSpec.ConditionBoostSpec.BoostControlSpec):
                Optional. Complex specification for custom
                ranking based on customer defined attribute
                value.
        """

        class BoostControlSpec(proto.Message):
            r"""Specification for custom ranking based on customer specified
            attribute value. It provides more controls for customized
            ranking than the simple (condition, boost) combination above.

            Attributes:
                field_name (str):
                    Optional. The name of the field whose value
                    will be used to determine the boost amount.
                attribute_type (google.cloud.dialogflowcx_v3beta1.types.BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType):
                    Optional. The attribute type to be used to determine the
                    boost amount. The attribute value can be derived from the
                    field value of the specified field_name. In the case of
                    numerical it is straightforward i.e. attribute_value =
                    numerical_field_value. In the case of freshness however,
                    attribute_value = (time.now() - datetime_field_value).
                interpolation_type (google.cloud.dialogflowcx_v3beta1.types.BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType):
                    Optional. The interpolation type to be
                    applied to connect the control points listed
                    below.
                control_points (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.BoostSpec.ConditionBoostSpec.BoostControlSpec.ControlPoint]):
                    Optional. The control points used to define the curve. The
                    monotonic function (defined through the interpolation_type
                    above) passes through the control points listed here.
            """

            class AttributeType(proto.Enum):
                r"""The attribute(or function) for which the custom ranking is to
                be applied.

                Values:
                    ATTRIBUTE_TYPE_UNSPECIFIED (0):
                        Unspecified AttributeType.
                    NUMERICAL (1):
                        The value of the numerical field will be used to dynamically
                        update the boost amount. In this case, the attribute_value
                        (the x value) of the control point will be the actual value
                        of the numerical field for which the boost_amount is
                        specified.
                    FRESHNESS (2):
                        For the freshness use case the attribute value will be the
                        duration between the current time and the date in the
                        datetime field specified. The value must be formatted as an
                        XSD ``dayTimeDuration`` value (a restricted subset of an ISO
                        8601 duration value). The pattern for this is:
                        ``[nD][T[nH][nM][nS]]``. E.g. ``5D``, ``3DT12H30M``,
                        ``T24H``.
                """

                ATTRIBUTE_TYPE_UNSPECIFIED = 0
                NUMERICAL = 1
                FRESHNESS = 2

            class InterpolationType(proto.Enum):
                r"""The interpolation type to be applied. Default will be linear
                (Piecewise Linear).

                Values:
                    INTERPOLATION_TYPE_UNSPECIFIED (0):
                        Interpolation type is unspecified. In this
                        case, it defaults to Linear.
                    LINEAR (1):
                        Piecewise linear interpolation will be
                        applied.
                """

                INTERPOLATION_TYPE_UNSPECIFIED = 0
                LINEAR = 1

            class ControlPoint(proto.Message):
                r"""The control points used to define the curve. The curve
                defined through these control points can only be monotonically
                increasing or decreasing(constant values are acceptable).

                Attributes:
                    attribute_value (str):
                        Optional. Can be one of:

                        1. The numerical field value.
                        2. The duration spec for freshness: The value must be
                           formatted as an XSD ``dayTimeDuration`` value (a
                           restricted subset of an ISO 8601 duration value). The
                           pattern for this is: ``[nD][T[nH][nM][nS]]``.
                    boost_amount (float):
                        Optional. The value between -1 to 1 by which to boost the
                        score if the attribute_value evaluates to the value
                        specified above.
                """

                attribute_value: str = proto.Field(
                    proto.STRING,
                    number=1,
                )
                boost_amount: float = proto.Field(
                    proto.FLOAT,
                    number=2,
                )

            field_name: str = proto.Field(
                proto.STRING,
                number=1,
            )
            attribute_type: "BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType" = proto.Field(
                proto.ENUM,
                number=2,
                enum="BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType",
            )
            interpolation_type: "BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType" = proto.Field(
                proto.ENUM,
                number=3,
                enum="BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType",
            )
            control_points: MutableSequence[
                "BoostSpec.ConditionBoostSpec.BoostControlSpec.ControlPoint"
            ] = proto.RepeatedField(
                proto.MESSAGE,
                number=4,
                message="BoostSpec.ConditionBoostSpec.BoostControlSpec.ControlPoint",
            )

        condition: str = proto.Field(
            proto.STRING,
            number=1,
        )
        boost: float = proto.Field(
            proto.FLOAT,
            number=2,
        )
        boost_control_spec: "BoostSpec.ConditionBoostSpec.BoostControlSpec" = (
            proto.Field(
                proto.MESSAGE,
                number=4,
                message="BoostSpec.ConditionBoostSpec.BoostControlSpec",
            )
        )

    condition_boost_specs: MutableSequence[ConditionBoostSpec] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=ConditionBoostSpec,
    )


class BoostSpecs(proto.Message):
    r"""Boost specifications for data stores.

    Attributes:
        data_stores (MutableSequence[str]):
            Optional. Data Stores where the boosting configuration is
            applied. The full names of the referenced data stores.
            Formats:
            ``projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}``
            \`projects/{project}/locations/{location}/dataStores/{data_store}
        spec (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.BoostSpec]):
            Optional. A list of boosting specifications.
    """

    data_stores: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    spec: MutableSequence["BoostSpec"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="BoostSpec",
    )


class FilterSpecs(proto.Message):
    r"""Filter specifications for data stores.

    Attributes:
        data_stores (MutableSequence[str]):
            Optional. Data Stores where the boosting configuration is
            applied. The full names of the referenced data stores.
            Formats:
            ``projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}``
            \`projects/{project}/locations/{location}/dataStores/{data_store}
        filter (str):
            Optional. The filter expression to be
            applied. Expression syntax is documented at
            https://cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata#filter-expression-syntax
    """

    data_stores: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )


class QueryInput(proto.Message):
    r"""Represents the query input. It can contain one of:

    1. A conversational query in the form of text.

    2. An intent query that specifies which intent to trigger.

    3. Natural language speech audio to be processed.

    4. An event to be triggered.

    5. DTMF digits to invoke an intent and fill in parameter value.

    6. The results of a tool executed by the client.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        text (google.cloud.dialogflowcx_v3beta1.types.TextInput):
            The natural language text to be processed.

            This field is a member of `oneof`_ ``input``.
        intent (google.cloud.dialogflowcx_v3beta1.types.IntentInput):
            The intent to be triggered.

            This field is a member of `oneof`_ ``input``.
        audio (google.cloud.dialogflowcx_v3beta1.types.AudioInput):
            The natural language speech audio to be
            processed.

            This field is a member of `oneof`_ ``input``.
        event (google.cloud.dialogflowcx_v3beta1.types.EventInput):
            The event to be triggered.

            This field is a member of `oneof`_ ``input``.
        dtmf (google.cloud.dialogflowcx_v3beta1.types.DtmfInput):
            The DTMF event to be handled.

            This field is a member of `oneof`_ ``input``.
        tool_call_result (google.cloud.dialogflowcx_v3beta1.types.ToolCallResult):
            The results of a tool executed by the client.

            This field is a member of `oneof`_ ``input``.
        language_code (str):
            Required. The language of the input. See `Language
            Support <https://cloud.google.com/dialogflow/cx/docs/reference/language>`__
            for a list of the currently supported language codes. Note
            that queries in the same session do not necessarily need to
            specify the same language.
    """

    text: "TextInput" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="input",
        message="TextInput",
    )
    intent: "IntentInput" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="input",
        message="IntentInput",
    )
    audio: "AudioInput" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="input",
        message="AudioInput",
    )
    event: "EventInput" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="input",
        message="EventInput",
    )
    dtmf: "DtmfInput" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="input",
        message="DtmfInput",
    )
    tool_call_result: tool_call.ToolCallResult = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="input",
        message=tool_call.ToolCallResult,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=4,
    )


class GenerativeInfo(proto.Message):
    r"""Represents the information of a query if handled by
    generative agent resources.

    Attributes:
        current_playbooks (MutableSequence[str]):
            The stack of
            [playbooks][google.cloud.dialogflow.cx.v3beta1.Playbook]
            that the conversation has currently entered, with the most
            recent one on the top.
        action_tracing_info (google.cloud.dialogflowcx_v3beta1.types.Example):
            The actions performed by the generative
            playbook for the current agent response.
    """

    current_playbooks: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    action_tracing_info: example.Example = proto.Field(
        proto.MESSAGE,
        number=2,
        message=example.Example,
    )


class QueryResult(proto.Message):
    r"""Represents the result of a conversational query.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        text (str):
            If [natural language
            text][google.cloud.dialogflow.cx.v3beta1.TextInput] was
            provided as input, this field will contain a copy of the
            text.

            This field is a member of `oneof`_ ``query``.
        trigger_intent (str):
            If an
            [intent][google.cloud.dialogflow.cx.v3beta1.IntentInput] was
            provided as input, this field will contain a copy of the
            intent identifier. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/intents/<IntentID>``.

            This field is a member of `oneof`_ ``query``.
        transcript (str):
            If [natural language speech
            audio][google.cloud.dialogflow.cx.v3beta1.AudioInput] was
            provided as input, this field will contain the transcript
            for the audio.

            This field is a member of `oneof`_ ``query``.
        trigger_event (str):
            If an [event][google.cloud.dialogflow.cx.v3beta1.EventInput]
            was provided as input, this field will contain the name of
            the event.

            This field is a member of `oneof`_ ``query``.
        dtmf (google.cloud.dialogflowcx_v3beta1.types.DtmfInput):
            If a [DTMF][google.cloud.dialogflow.cx.v3beta1.DtmfInput]
            was provided as input, this field will contain a copy of the
            [DtmfInput][google.cloud.dialogflow.cx.v3beta1.DtmfInput].

            This field is a member of `oneof`_ ``query``.
        language_code (str):
            The language that was triggered during intent detection. See
            `Language
            Support <https://cloud.google.com/dialogflow/cx/docs/reference/language>`__
            for a list of the currently supported language codes.
        parameters (google.protobuf.struct_pb2.Struct):
            The collected [session
            parameters][google.cloud.dialogflow.cx.v3beta1.SessionInfo.parameters].

            Depending on your protocol or client library language, this
            is a map, associative array, symbol table, dictionary, or
            JSON object composed of a collection of (MapKey, MapValue)
            pairs:

            - MapKey type: string
            - MapKey value: parameter name
            - MapValue type: If parameter's entity type is a composite
              entity then use map, otherwise, depending on the parameter
              value type, it could be one of string, number, boolean,
              null, list or map.
            - MapValue value: If parameter's entity type is a composite
              entity then use map from composite entity property names
              to property values, otherwise, use parameter value.
        response_messages (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.ResponseMessage]):
            The list of rich messages returned to the
            client. Responses vary from simple text messages
            to more sophisticated, structured payloads used
            to drive complex logic.
        webhook_ids (MutableSequence[str]):
            The list of webhook ids in the order of call
            sequence.
        webhook_display_names (MutableSequence[str]):
            The list of webhook display names in the
            order of call sequence.
        webhook_latencies (MutableSequence[google.protobuf.duration_pb2.Duration]):
            The list of webhook latencies in the order of
            call sequence.
        webhook_tags (MutableSequence[str]):
            The list of webhook tags in the order of call
            sequence.
        webhook_statuses (MutableSequence[google.rpc.status_pb2.Status]):
            The list of webhook call status in the order
            of call sequence.
        webhook_payloads (MutableSequence[google.protobuf.struct_pb2.Struct]):
            The list of webhook payload in
            [WebhookResponse.payload][google.cloud.dialogflow.cx.v3beta1.WebhookResponse.payload],
            in the order of call sequence. If some webhook call fails or
            doesn't return any payload, an empty ``Struct`` would be
            used instead.
        current_page (google.cloud.dialogflowcx_v3beta1.types.Page):
            The current [Page][google.cloud.dialogflow.cx.v3beta1.Page].
            Some, not all fields are filled in this message, including
            but not limited to ``name`` and ``display_name``.
        current_flow (google.cloud.dialogflowcx_v3beta1.types.Flow):
            The current [Flow][google.cloud.dialogflow.cx.v3beta1.Flow].
            Some, not all fields are filled in this message, including
            but not limited to ``name`` and ``display_name``.
        intent (google.cloud.dialogflowcx_v3beta1.types.Intent):
            The [Intent][google.cloud.dialogflow.cx.v3beta1.Intent] that
            matched the conversational query. Some, not all fields are
            filled in this message, including but not limited to:
            ``name`` and ``display_name``. This field is deprecated,
            please use
            [QueryResult.match][google.cloud.dialogflow.cx.v3beta1.QueryResult.match]
            instead.
        intent_detection_confidence (float):
            The intent detection confidence. Values range from 0.0
            (completely uncertain) to 1.0 (completely certain). This
            value is for informational purpose only and is only used to
            help match the best intent within the classification
            threshold. This value may change for the same end-user
            expression at any time due to a model retraining or change
            in implementation. This field is deprecated, please use
            [QueryResult.match][google.cloud.dialogflow.cx.v3beta1.QueryResult.match]
            instead.
        match (google.cloud.dialogflowcx_v3beta1.types.Match):
            Intent match result, could be an intent or an
            event.
        diagnostic_info (google.protobuf.struct_pb2.Struct):
            The free-form diagnostic info. For example, this field could
            contain webhook call latency. The fields of this data can
            change without notice, so you should not write code that
            depends on its structure.

            One of the fields is called "Alternative Matched Intents",
            which may aid with debugging. The following describes these
            intent results:

            - The list is empty if no intent was matched to end-user
              input.
            - Only intents that are referenced in the currently active
              flow are included.
            - The matched intent is included.
            - Other intents that could have matched end-user input, but
              did not match because they are referenced by intent routes
              that are out of
              `scope <https://cloud.google.com/dialogflow/cx/docs/concept/handler#scope>`__,
              are included.
            - Other intents referenced by intent routes in scope that
              matched end-user input, but had a lower confidence score.
        generative_info (google.cloud.dialogflowcx_v3beta1.types.GenerativeInfo):
            The information of a query if handled by
            generative agent resources.
        sentiment_analysis_result (google.cloud.dialogflowcx_v3beta1.types.SentimentAnalysisResult):
            The sentiment analyss result, which depends on
            [``analyze_query_text_sentiment``]
            [google.cloud.dialogflow.cx.v3beta1.QueryParameters.analyze_query_text_sentiment],
            specified in the request.
        advanced_settings (google.cloud.dialogflowcx_v3beta1.types.AdvancedSettings):
            Returns the current advanced settings
            including IVR settings. Even though the
            operations configured by these settings are
            performed by Dialogflow, the client may need to
            perform special logic at the moment. For
            example, if Dialogflow exports audio to Google
            Cloud Storage, then the client may need to wait
            for the resulting object to appear in the bucket
            before proceeding.
        allow_answer_feedback (bool):
            Indicates whether the Thumbs up/Thumbs down
            rating controls are need to be shown for the
            response in the Dialogflow Messenger widget.
        data_store_connection_signals (google.cloud.dialogflowcx_v3beta1.types.DataStoreConnectionSignals):
            Optional. Data store connection feature
            output signals. Filled only when data stores are
            involved in serving the query.
        trace_blocks (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.TraceBlock]):
            Optional. Contains the sequence of trace
            blocks from the current conversation turn. Trace
            blocks are ordered chronologically and contain
            detailed traces of runtime behavior such as tool
            calls, LLM calls, flow and playbook invocations,
            agent utterances and user utterances.
    """

    text: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="query",
    )
    trigger_intent: str = proto.Field(
        proto.STRING,
        number=11,
        oneof="query",
    )
    transcript: str = proto.Field(
        proto.STRING,
        number=12,
        oneof="query",
    )
    trigger_event: str = proto.Field(
        proto.STRING,
        number=14,
        oneof="query",
    )
    dtmf: "DtmfInput" = proto.Field(
        proto.MESSAGE,
        number=23,
        oneof="query",
        message="DtmfInput",
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=2,
    )
    parameters: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=3,
        message=struct_pb2.Struct,
    )
    response_messages: MutableSequence[response_message.ResponseMessage] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message=response_message.ResponseMessage,
        )
    )
    webhook_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=25,
    )
    webhook_display_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=26,
    )
    webhook_latencies: MutableSequence[duration_pb2.Duration] = proto.RepeatedField(
        proto.MESSAGE,
        number=27,
        message=duration_pb2.Duration,
    )
    webhook_tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=29,
    )
    webhook_statuses: MutableSequence[status_pb2.Status] = proto.RepeatedField(
        proto.MESSAGE,
        number=13,
        message=status_pb2.Status,
    )
    webhook_payloads: MutableSequence[struct_pb2.Struct] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message=struct_pb2.Struct,
    )
    current_page: page.Page = proto.Field(
        proto.MESSAGE,
        number=7,
        message=page.Page,
    )
    current_flow: flow.Flow = proto.Field(
        proto.MESSAGE,
        number=31,
        message=flow.Flow,
    )
    intent: gcdc_intent.Intent = proto.Field(
        proto.MESSAGE,
        number=8,
        message=gcdc_intent.Intent,
    )
    intent_detection_confidence: float = proto.Field(
        proto.FLOAT,
        number=9,
    )
    match: "Match" = proto.Field(
        proto.MESSAGE,
        number=15,
        message="Match",
    )
    diagnostic_info: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=10,
        message=struct_pb2.Struct,
    )
    generative_info: "GenerativeInfo" = proto.Field(
        proto.MESSAGE,
        number=33,
        message="GenerativeInfo",
    )
    sentiment_analysis_result: "SentimentAnalysisResult" = proto.Field(
        proto.MESSAGE,
        number=17,
        message="SentimentAnalysisResult",
    )
    advanced_settings: gcdc_advanced_settings.AdvancedSettings = proto.Field(
        proto.MESSAGE,
        number=21,
        message=gcdc_advanced_settings.AdvancedSettings,
    )
    allow_answer_feedback: bool = proto.Field(
        proto.BOOL,
        number=32,
    )
    data_store_connection_signals: data_store_connection.DataStoreConnectionSignals = (
        proto.Field(
            proto.MESSAGE,
            number=35,
            message=data_store_connection.DataStoreConnectionSignals,
        )
    )
    trace_blocks: MutableSequence[trace.TraceBlock] = proto.RepeatedField(
        proto.MESSAGE,
        number=37,
        message=trace.TraceBlock,
    )


class TextInput(proto.Message):
    r"""Represents the natural language text to be processed.

    Attributes:
        text (str):
            Required. The UTF-8 encoded natural language
            text to be processed.
    """

    text: str = proto.Field(
        proto.STRING,
        number=1,
    )


class IntentInput(proto.Message):
    r"""Represents the intent to trigger programmatically rather than
    as a result of natural language processing.

    Attributes:
        intent (str):
            Required. The unique identifier of the intent. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/intents/<IntentID>``.
    """

    intent: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AudioInput(proto.Message):
    r"""Represents the natural speech audio to be processed.

    Attributes:
        config (google.cloud.dialogflowcx_v3beta1.types.InputAudioConfig):
            Required. Instructs the speech recognizer how
            to process the speech audio.
        audio (bytes):
            The natural language speech audio to be processed. A single
            request can contain up to 2 minutes of speech audio data.
            The [transcribed
            text][google.cloud.dialogflow.cx.v3beta1.QueryResult.transcript]
            cannot contain more than 256 bytes.

            For non-streaming audio detect intent, both ``config`` and
            ``audio`` must be provided. For streaming audio detect
            intent, ``config`` must be provided in the first request and
            ``audio`` must be provided in all following requests.
    """

    config: audio_config.InputAudioConfig = proto.Field(
        proto.MESSAGE,
        number=1,
        message=audio_config.InputAudioConfig,
    )
    audio: bytes = proto.Field(
        proto.BYTES,
        number=2,
    )


class EventInput(proto.Message):
    r"""Represents the event to trigger.

    Attributes:
        event (str):
            Name of the event.
    """

    event: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DtmfInput(proto.Message):
    r"""Represents the input for dtmf event.

    Attributes:
        digits (str):
            The dtmf digits.
        finish_digit (str):
            The finish digit (if any).
    """

    digits: str = proto.Field(
        proto.STRING,
        number=1,
    )
    finish_digit: str = proto.Field(
        proto.STRING,
        number=2,
    )


class Match(proto.Message):
    r"""Represents one match result of [MatchIntent][].

    Attributes:
        intent (google.cloud.dialogflowcx_v3beta1.types.Intent):
            The [Intent][google.cloud.dialogflow.cx.v3beta1.Intent] that
            matched the query. Some, not all fields are filled in this
            message, including but not limited to: ``name`` and
            ``display_name``. Only filled for
            [``INTENT``][google.cloud.dialogflow.cx.v3beta1.Match.MatchType]
            match type.
        event (str):
            The event that matched the query. Filled for
            [``EVENT``][google.cloud.dialogflow.cx.v3beta1.Match.MatchType],
            [``NO_MATCH``][google.cloud.dialogflow.cx.v3beta1.Match.MatchType]
            and
            [``NO_INPUT``][google.cloud.dialogflow.cx.v3beta1.Match.MatchType]
            match types.
        parameters (google.protobuf.struct_pb2.Struct):
            The collection of parameters extracted from the query.

            Depending on your protocol or client library language, this
            is a map, associative array, symbol table, dictionary, or
            JSON object composed of a collection of (MapKey, MapValue)
            pairs:

            - MapKey type: string
            - MapKey value: parameter name
            - MapValue type: If parameter's entity type is a composite
              entity then use map, otherwise, depending on the parameter
              value type, it could be one of string, number, boolean,
              null, list or map.
            - MapValue value: If parameter's entity type is a composite
              entity then use map from composite entity property names
              to property values, otherwise, use parameter value.
        resolved_input (str):
            Final text input which was matched during
            MatchIntent. This value can be different from
            original input sent in request because of
            spelling correction or other processing.
        match_type (google.cloud.dialogflowcx_v3beta1.types.Match.MatchType):
            Type of this
            [Match][google.cloud.dialogflow.cx.v3beta1.Match].
        confidence (float):
            The confidence of this match. Values range
            from 0.0 (completely uncertain) to 1.0
            (completely certain). This value is for
            informational purpose only and is only used to
            help match the best intent within the
            classification threshold. This value may change
            for the same end-user expression at any time due
            to a model retraining or change in
            implementation.
    """

    class MatchType(proto.Enum):
        r"""Type of a Match.

        Values:
            MATCH_TYPE_UNSPECIFIED (0):
                Not specified. Should never be used.
            INTENT (1):
                The query was matched to an intent.
            DIRECT_INTENT (2):
                The query directly triggered an intent.
            PARAMETER_FILLING (3):
                The query was used for parameter filling.
            NO_MATCH (4):
                No match was found for the query.
            NO_INPUT (5):
                Indicates an empty query.
            EVENT (6):
                The query directly triggered an event.
            KNOWLEDGE_CONNECTOR (8):
                The query was matched to a Knowledge
                Connector answer.
            PLAYBOOK (9):
                The query was handled by a
                [``Playbook``][google.cloud.dialogflow.cx.v3beta1.Playbook].
        """

        MATCH_TYPE_UNSPECIFIED = 0
        INTENT = 1
        DIRECT_INTENT = 2
        PARAMETER_FILLING = 3
        NO_MATCH = 4
        NO_INPUT = 5
        EVENT = 6
        KNOWLEDGE_CONNECTOR = 8
        PLAYBOOK = 9

    intent: gcdc_intent.Intent = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcdc_intent.Intent,
    )
    event: str = proto.Field(
        proto.STRING,
        number=6,
    )
    parameters: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=2,
        message=struct_pb2.Struct,
    )
    resolved_input: str = proto.Field(
        proto.STRING,
        number=3,
    )
    match_type: MatchType = proto.Field(
        proto.ENUM,
        number=4,
        enum=MatchType,
    )
    confidence: float = proto.Field(
        proto.FLOAT,
        number=5,
    )


class MatchIntentRequest(proto.Message):
    r"""Request of [MatchIntent][].

    Attributes:
        session (str):
            Required. The name of the session this query is sent to.
            Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/sessions/<SessionID>``
            or
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>/sessions/<SessionID>``.
            If ``Environment ID`` is not specified, we assume default
            'draft' environment. It's up to the API caller to choose an
            appropriate ``Session ID``. It can be a random number or
            some type of session identifiers (preferably hashed). The
            length of the ``Session ID`` must not exceed 36 characters.

            For more information, see the `sessions
            guide <https://cloud.google.com/dialogflow/cx/docs/concept/session>`__.
        query_params (google.cloud.dialogflowcx_v3beta1.types.QueryParameters):
            The parameters of this query.
        query_input (google.cloud.dialogflowcx_v3beta1.types.QueryInput):
            Required. The input specification.
        persist_parameter_changes (bool):
            Persist session parameter changes from ``query_params``.
    """

    session: str = proto.Field(
        proto.STRING,
        number=1,
    )
    query_params: "QueryParameters" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="QueryParameters",
    )
    query_input: "QueryInput" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="QueryInput",
    )
    persist_parameter_changes: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class MatchIntentResponse(proto.Message):
    r"""Response of [MatchIntent][].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        text (str):
            If [natural language
            text][google.cloud.dialogflow.cx.v3beta1.TextInput] was
            provided as input, this field will contain a copy of the
            text.

            This field is a member of `oneof`_ ``query``.
        trigger_intent (str):
            If an
            [intent][google.cloud.dialogflow.cx.v3beta1.IntentInput] was
            provided as input, this field will contain a copy of the
            intent identifier. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/intents/<IntentID>``.

            This field is a member of `oneof`_ ``query``.
        transcript (str):
            If [natural language speech
            audio][google.cloud.dialogflow.cx.v3beta1.AudioInput] was
            provided as input, this field will contain the transcript
            for the audio.

            This field is a member of `oneof`_ ``query``.
        trigger_event (str):
            If an [event][google.cloud.dialogflow.cx.v3beta1.EventInput]
            was provided as input, this field will contain a copy of the
            event name.

            This field is a member of `oneof`_ ``query``.
        matches (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.Match]):
            Match results, if more than one, ordered
            descendingly by the confidence we have that the
            particular intent matches the query.
        current_page (google.cloud.dialogflowcx_v3beta1.types.Page):
            The current [Page][google.cloud.dialogflow.cx.v3beta1.Page].
            Some, not all fields are filled in this message, including
            but not limited to ``name`` and ``display_name``.
    """

    text: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="query",
    )
    trigger_intent: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="query",
    )
    transcript: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="query",
    )
    trigger_event: str = proto.Field(
        proto.STRING,
        number=6,
        oneof="query",
    )
    matches: MutableSequence["Match"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="Match",
    )
    current_page: page.Page = proto.Field(
        proto.MESSAGE,
        number=5,
        message=page.Page,
    )


class FulfillIntentRequest(proto.Message):
    r"""Request of [FulfillIntent][]

    Attributes:
        match_intent_request (google.cloud.dialogflowcx_v3beta1.types.MatchIntentRequest):
            Must be same as the corresponding MatchIntent
            request, otherwise the behavior is undefined.
        match (google.cloud.dialogflowcx_v3beta1.types.Match):
            The matched intent/event to fulfill.
        output_audio_config (google.cloud.dialogflowcx_v3beta1.types.OutputAudioConfig):
            Instructs the speech synthesizer how to
            generate output audio.
    """

    match_intent_request: "MatchIntentRequest" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="MatchIntentRequest",
    )
    match: "Match" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Match",
    )
    output_audio_config: audio_config.OutputAudioConfig = proto.Field(
        proto.MESSAGE,
        number=3,
        message=audio_config.OutputAudioConfig,
    )


class FulfillIntentResponse(proto.Message):
    r"""Response of [FulfillIntent][]

    Attributes:
        response_id (str):
            Output only. The unique identifier of the
            response. It can be used to locate a response in
            the training example set or for reporting
            issues.
        query_result (google.cloud.dialogflowcx_v3beta1.types.QueryResult):
            The result of the conversational query.
        output_audio (bytes):
            The audio data bytes encoded as specified in the request.
            Note: The output audio is generated based on the values of
            default platform text responses found in the
            [``query_result.response_messages``][google.cloud.dialogflow.cx.v3beta1.QueryResult.response_messages]
            field. If multiple default text responses exist, they will
            be concatenated when generating audio. If no default
            platform text responses exist, the generated audio content
            will be empty.

            In some scenarios, multiple output audio fields may be
            present in the response structure. In these cases, only the
            top-most-level audio output has content.
        output_audio_config (google.cloud.dialogflowcx_v3beta1.types.OutputAudioConfig):
            The config used by the speech synthesizer to
            generate the output audio.
    """

    response_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    query_result: "QueryResult" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="QueryResult",
    )
    output_audio: bytes = proto.Field(
        proto.BYTES,
        number=3,
    )
    output_audio_config: audio_config.OutputAudioConfig = proto.Field(
        proto.MESSAGE,
        number=4,
        message=audio_config.OutputAudioConfig,
    )


class SentimentAnalysisResult(proto.Message):
    r"""The result of sentiment analysis. Sentiment analysis inspects
    user input and identifies the prevailing subjective opinion,
    especially to determine a user's attitude as positive, negative,
    or neutral.

    Attributes:
        score (float):
            Sentiment score between -1.0 (negative
            sentiment) and 1.0 (positive  sentiment).
        magnitude (float):
            A non-negative number in the [0, +inf) range, which
            represents the absolute magnitude of sentiment, regardless
            of score (positive or negative).
    """

    score: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    magnitude: float = proto.Field(
        proto.FLOAT,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
