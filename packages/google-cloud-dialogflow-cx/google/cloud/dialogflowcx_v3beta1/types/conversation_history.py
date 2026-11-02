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

from google.cloud.dialogflowcx_v3beta1.types import environment as gcdc_environment
from google.cloud.dialogflowcx_v3beta1.types import flow, intent, page, session

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.cx.v3beta1",
    manifest={
        "GetConversationRequest",
        "DeleteConversationRequest",
        "ListConversationsRequest",
        "ListConversationsResponse",
        "Conversation",
    },
)


class GetConversationRequest(proto.Message):
    r"""The request message for [Conversations.GetConversation][].

    Attributes:
        name (str):
            Required. The name of the conversation. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/conversations/<ConversationID>``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteConversationRequest(proto.Message):
    r"""The request message for [Conversations.DeleteConversation][].

    Attributes:
        name (str):
            Required. The name of the conversation. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/conversations/<ConversationID>``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListConversationsRequest(proto.Message):
    r"""The request message for [Conversations.ListConversations][].

    Attributes:
        parent (str):
            Required. The agent to list all conversations for. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>``.
        filter (str):
            Optional. The filter string. Supports filter by create_time,
            metrics.has_end_interaction, metrics.has_live_agent_handoff,
            intents.display_name, pages.display_name and
            flows.display_name. Timestamps expect an
            [RFC-3339][https://datatracker.ietf.org/doc/html/rfc3339]
            formatted string (e.g. 2012-04-21T11:30:00-04:00). UTC
            offsets are supported. Some examples:

            1. By create time: create_time > "2022-04-21T11:30:00-04:00"
            2. By intent display name: intents.display_name : "billing"
            3. By end interaction signal: metrics.has_end_interaction =
               true
        page_size (int):
            Optional. The maximum number of items to
            return in a single page. By default 100 and at
            most 1000.
        page_token (str):
            Optional. The next_page_token value returned from a previous
            list request.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListConversationsResponse(proto.Message):
    r"""The response message for [Conversations.ListConversations][].

    Attributes:
        conversations (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.Conversation]):
            The list of conversations. There will be a maximum number of
            items returned based on the
            [page_size][google.cloud.dialogflow.cx.v3beta1.ListConversationsRequest.page_size]
            field. The returned conversations will be sorted by
            start_time in descending order (newest conversation first).
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    conversations: MutableSequence["Conversation"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Conversation",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class Conversation(proto.Message):
    r"""Represents a conversation.

    Attributes:
        name (str):
            Identifier. The identifier of the conversation. If
            conversation ID is reused, interactions happened later than
            48 hours of the conversation's create time will be ignored.
            Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/conversations/<ConversationID>``
        type_ (google.cloud.dialogflowcx_v3beta1.types.Conversation.Type):
            The type of the conversation.
        language_code (str):
            The language of the conversation, which is
            the language of the first request in the
            conversation.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Start time of the conversation, which is the
            time of the first request of the conversation.
        duration (google.protobuf.duration_pb2.Duration):
            Duration of the conversation.
        metrics (google.cloud.dialogflowcx_v3beta1.types.Conversation.Metrics):
            Conversation metrics.
        intents (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.Intent]):
            All the matched
            [Intent][google.cloud.dialogflow.cx.v3beta1.Intent] in the
            conversation. Only ``name`` and ``display_name`` are filled
            in this message.
        flows (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.Flow]):
            All the [Flow][google.cloud.dialogflow.cx.v3beta1.Flow] the
            conversation has went through. Only ``name`` and
            ``display_name`` are filled in this message.
        pages (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.Page]):
            All the [Page][google.cloud.dialogflow.cx.v3beta1.Page] the
            conversation has went through. Only ``name`` and
            ``display_name`` are filled in this message.
        interactions (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.Conversation.Interaction]):
            Interactions of the conversation. Only populated for
            ``GetConversation`` and empty for ``ListConversations``.
        environment (google.cloud.dialogflowcx_v3beta1.types.Environment):
            Environment of the conversation. Only ``name`` and
            ``display_name`` are filled in this message.
        flow_versions (MutableMapping[str, int]):
            Flow versions used in the conversation.
    """

    class Type(proto.Enum):
        r"""Represents the type of a conversation.

        Values:
            TYPE_UNSPECIFIED (0):
                Not specified. This value should never be
                used.
            AUDIO (1):
                Audio conversation. A conversation is
                classified as an audio conversation if any
                request has STT input audio or any response has
                TTS output audio.
            TEXT (2):
                Text conversation. A conversation is
                classified as a text conversation if any request
                has text input and no request has STT input
                audio and no response has TTS output audio.
            UNDETERMINED (3):
                Default conversation type for a conversation.
                A conversation is classified as undetermined if
                none of the requests contain text or audio input
                (eg. event or intent input).
        """

        TYPE_UNSPECIFIED = 0
        AUDIO = 1
        TEXT = 2
        UNDETERMINED = 3

    class Metrics(proto.Message):
        r"""Represents metrics for the conversation.

        Attributes:
            interaction_count (int):
                The number of interactions in the
                conversation.
            input_audio_duration (google.protobuf.duration_pb2.Duration):
                Duration of all the input's audio in the
                conversation.
            output_audio_duration (google.protobuf.duration_pb2.Duration):
                Duration of all the output's audio in the
                conversation.
            max_webhook_latency (google.protobuf.duration_pb2.Duration):
                Maximum latency of the
                [Webhook][google.cloud.dialogflow.cx.v3beta1.Webhook] calls
                in the conversation.
            has_end_interaction (bool):
                A signal that indicates the interaction with the Dialogflow
                agent has ended. If any response has the
                [ResponseMessage.end_interaction][google.cloud.dialogflow.cx.v3beta1.ResponseMessage.end_interaction]
                signal, this is set to true.
            has_live_agent_handoff (bool):
                Hands off conversation to a human agent. If any response has
                the
                [ResponseMessage.live_agent_handoff][google.cloud.dialogflow.cx.v3beta1.ResponseMessage.live_agent_handoff]signal,
                this is set to true.
            average_match_confidence (float):
                The average confidence all of the
                [Match][google.cloud.dialogflow.cx.v3beta1.Match] in the
                conversation. Values range from 0.0 (completely uncertain)
                to 1.0 (completely certain).
            query_input_count (google.cloud.dialogflowcx_v3beta1.types.Conversation.Metrics.QueryInputCount):
                Query input counts.
            match_type_count (google.cloud.dialogflowcx_v3beta1.types.Conversation.Metrics.MatchTypeCount):
                Match type counts.
        """

        class QueryInputCount(proto.Message):
            r"""Count by types of
            [QueryInput][google.cloud.dialogflow.cx.v3beta1.QueryInput] of the
            requests in the conversation.

            Attributes:
                text_count (int):
                    The number of
                    [TextInput][google.cloud.dialogflow.cx.v3beta1.TextInput] in
                    the conversation.
                intent_count (int):
                    The number of
                    [IntentInput][google.cloud.dialogflow.cx.v3beta1.IntentInput]
                    in the conversation.
                audio_count (int):
                    The number of
                    [AudioInput][google.cloud.dialogflow.cx.v3beta1.AudioInput]
                    in the conversation.
                event_count (int):
                    The number of
                    [EventInput][google.cloud.dialogflow.cx.v3beta1.EventInput]
                    in the conversation.
                dtmf_count (int):
                    The number of
                    [DtmfInput][google.cloud.dialogflow.cx.v3beta1.DtmfInput] in
                    the conversation.
            """

            text_count: int = proto.Field(
                proto.INT32,
                number=1,
            )
            intent_count: int = proto.Field(
                proto.INT32,
                number=2,
            )
            audio_count: int = proto.Field(
                proto.INT32,
                number=3,
            )
            event_count: int = proto.Field(
                proto.INT32,
                number=4,
            )
            dtmf_count: int = proto.Field(
                proto.INT32,
                number=5,
            )

        class MatchTypeCount(proto.Message):
            r"""Count by
            [Match.MatchType][google.cloud.dialogflow.cx.v3beta1.Match.MatchType]
            of the matches in the conversation.

            Attributes:
                unspecified_count (int):
                    The number of matches with type
                    [Match.MatchType.MATCH_TYPE_UNSPECIFIED][google.cloud.dialogflow.cx.v3beta1.Match.MatchType.MATCH_TYPE_UNSPECIFIED].
                intent_count (int):
                    The number of matches with type
                    [Match.MatchType.INTENT][google.cloud.dialogflow.cx.v3beta1.Match.MatchType.INTENT].
                direct_intent_count (int):
                    The number of matches with type
                    [Match.MatchType.DIRECT_INTENT][google.cloud.dialogflow.cx.v3beta1.Match.MatchType.DIRECT_INTENT].
                parameter_filling_count (int):
                    The number of matches with type
                    [Match.MatchType.PARAMETER_FILLING][google.cloud.dialogflow.cx.v3beta1.Match.MatchType.PARAMETER_FILLING].
                no_match_count (int):
                    The number of matches with type
                    [Match.MatchType.NO_MATCH][google.cloud.dialogflow.cx.v3beta1.Match.MatchType.NO_MATCH].
                no_input_count (int):
                    The number of matches with type
                    [Match.MatchType.NO_INPUT][google.cloud.dialogflow.cx.v3beta1.Match.MatchType.NO_INPUT].
                event_count (int):
                    The number of matches with type
                    [Match.MatchType.EVENT][google.cloud.dialogflow.cx.v3beta1.Match.MatchType.EVENT].
            """

            unspecified_count: int = proto.Field(
                proto.INT32,
                number=1,
            )
            intent_count: int = proto.Field(
                proto.INT32,
                number=2,
            )
            direct_intent_count: int = proto.Field(
                proto.INT32,
                number=3,
            )
            parameter_filling_count: int = proto.Field(
                proto.INT32,
                number=4,
            )
            no_match_count: int = proto.Field(
                proto.INT32,
                number=5,
            )
            no_input_count: int = proto.Field(
                proto.INT32,
                number=6,
            )
            event_count: int = proto.Field(
                proto.INT32,
                number=7,
            )

        interaction_count: int = proto.Field(
            proto.INT32,
            number=1,
        )
        input_audio_duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=2,
            message=duration_pb2.Duration,
        )
        output_audio_duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=3,
            message=duration_pb2.Duration,
        )
        max_webhook_latency: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=4,
            message=duration_pb2.Duration,
        )
        has_end_interaction: bool = proto.Field(
            proto.BOOL,
            number=5,
        )
        has_live_agent_handoff: bool = proto.Field(
            proto.BOOL,
            number=6,
        )
        average_match_confidence: float = proto.Field(
            proto.FLOAT,
            number=7,
        )
        query_input_count: "Conversation.Metrics.QueryInputCount" = proto.Field(
            proto.MESSAGE,
            number=8,
            message="Conversation.Metrics.QueryInputCount",
        )
        match_type_count: "Conversation.Metrics.MatchTypeCount" = proto.Field(
            proto.MESSAGE,
            number=9,
            message="Conversation.Metrics.MatchTypeCount",
        )

    class Interaction(proto.Message):
        r"""Represents an interaction between an end user and a
        Dialogflow CX agent using V3 (Streaming)DetectIntent API, or an
        interaction between an end user and a Dialogflow CX agent using
        V2 (Streaming)AnalyzeContent API.

        Attributes:
            request (google.cloud.dialogflowcx_v3beta1.types.DetectIntentRequest):
                The request of the interaction.
            response (google.cloud.dialogflowcx_v3beta1.types.DetectIntentResponse):
                The final response of the interaction.
            partial_responses (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.DetectIntentResponse]):
                The partial responses of the interaction. Empty if there is
                no partial response in the interaction. See the [partial
                response
                documentation][https://cloud.google.com/dialogflow/cx/docs/concept/fulfillment#queue].
            request_utterances (str):
                The input text or the transcript of the input
                audio in the request.
            response_utterances (str):
                The output text or the transcript of the
                output audio in the responses. If multiple
                output messages are returned, they will be
                concatenated into one.
            create_time (google.protobuf.timestamp_pb2.Timestamp):
                The time that the interaction was created.
            answer_feedback (google.cloud.dialogflowcx_v3beta1.types.AnswerFeedback):
                Answer feedback for the final response.
            missing_transition (google.cloud.dialogflowcx_v3beta1.types.Conversation.Interaction.MissingTransition):
                Missing transition predicted for the
                interaction. This field is set only if the
                interaction match type was no-match.
            step_metrics (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.Conversation.Interaction.StepMetrics]):
                Metrics associated with different processing
                steps. Names and number of steps depend on the
                request and can change without a notice.
        """

        class MissingTransition(proto.Message):
            r"""Information collected for DF CX agents in case NLU predicted
            an intent that was filtered out as being inactive which may
            indicate a missing transition and/or absent functionality.

            Attributes:
                intent_display_name (str):
                    Name of the intent that could have triggered.
                score (float):
                    Score of the above intent. The higher it is
                    the more likely a transition was missed on a
                    given page.
            """

            intent_display_name: str = proto.Field(
                proto.STRING,
                number=1,
            )
            score: float = proto.Field(
                proto.FLOAT,
                number=2,
            )

        class StepMetrics(proto.Message):
            r"""Metrics of each processing step.

            Attributes:
                name (str):
                    Name of the request processing step.
                latency (google.protobuf.duration_pb2.Duration):
                    Processing latency of the step.
            """

            name: str = proto.Field(
                proto.STRING,
                number=1,
            )
            latency: duration_pb2.Duration = proto.Field(
                proto.MESSAGE,
                number=2,
                message=duration_pb2.Duration,
            )

        request: session.DetectIntentRequest = proto.Field(
            proto.MESSAGE,
            number=1,
            message=session.DetectIntentRequest,
        )
        response: session.DetectIntentResponse = proto.Field(
            proto.MESSAGE,
            number=2,
            message=session.DetectIntentResponse,
        )
        partial_responses: MutableSequence[session.DetectIntentResponse] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=3,
                message=session.DetectIntentResponse,
            )
        )
        request_utterances: str = proto.Field(
            proto.STRING,
            number=4,
        )
        response_utterances: str = proto.Field(
            proto.STRING,
            number=5,
        )
        create_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=6,
            message=timestamp_pb2.Timestamp,
        )
        answer_feedback: session.AnswerFeedback = proto.Field(
            proto.MESSAGE,
            number=7,
            message=session.AnswerFeedback,
        )
        missing_transition: "Conversation.Interaction.MissingTransition" = proto.Field(
            proto.MESSAGE,
            number=8,
            message="Conversation.Interaction.MissingTransition",
        )
        step_metrics: MutableSequence["Conversation.Interaction.StepMetrics"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=9,
                message="Conversation.Interaction.StepMetrics",
            )
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=2,
        enum=Type,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=3,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=5,
        message=duration_pb2.Duration,
    )
    metrics: Metrics = proto.Field(
        proto.MESSAGE,
        number=6,
        message=Metrics,
    )
    intents: MutableSequence[intent.Intent] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message=intent.Intent,
    )
    flows: MutableSequence[flow.Flow] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message=flow.Flow,
    )
    pages: MutableSequence[page.Page] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message=page.Page,
    )
    interactions: MutableSequence[Interaction] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message=Interaction,
    )
    environment: gcdc_environment.Environment = proto.Field(
        proto.MESSAGE,
        number=11,
        message=gcdc_environment.Environment,
    )
    flow_versions: MutableMapping[str, int] = proto.MapField(
        proto.STRING,
        proto.INT64,
        number=12,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
