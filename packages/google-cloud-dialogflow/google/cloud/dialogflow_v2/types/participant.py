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

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.dialogflow_v2.types import audio_config as gcd_audio_config
from google.cloud.dialogflow_v2.types import (
    companion_agent,
    generator,
    grounding,
    session,
)

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.v2",
    manifest={
        "DatastoreResponseReason",
        "Participant",
        "Message",
        "CreateParticipantRequest",
        "GetParticipantRequest",
        "ListParticipantsRequest",
        "ListParticipantsResponse",
        "UpdateParticipantRequest",
        "AnalyzeContentRequest",
        "DtmfParameters",
        "AnalyzeContentResponse",
        "StreamingAnalyzeContentRequest",
        "StreamingAnalyzeContentResponse",
        "SuggestArticlesRequest",
        "SuggestArticlesResponse",
        "SuggestFaqAnswersRequest",
        "SuggestFaqAnswersResponse",
        "GenerateSuggestionsResponse",
        "ToolCallSuggestion",
        "ToolCallEvents",
        "CompanionSuggestion",
        "GenerateCompanionSuggestionsResponse",
        "SuggestSmartRepliesRequest",
        "SuggestSmartRepliesResponse",
        "AudioInput",
        "OutputAudio",
        "AutomatedAgentReply",
        "ArticleAnswer",
        "FaqAnswer",
        "SmartReplyAnswer",
        "IntentSuggestion",
        "DialogflowAssistAnswer",
        "SuggestionResult",
        "InputTextConfig",
        "AnnotatedMessagePart",
        "MessageAnnotation",
        "SuggestionInput",
        "AssistQueryParameters",
        "ResponseMessage",
        "SuggestKnowledgeAssistRequest",
        "SuggestKnowledgeAssistResponse",
        "IngestedContextReferenceDebugInfo",
        "ServiceLatency",
        "KnowledgeAssistDebugInfo",
        "KnowledgeAssistAnswer",
        "StreamingReactiveCompanionSuggestionsRequest",
        "CancelQuery",
        "StreamingReactiveCompanionSuggestionsResponse",
        "BidiStreamingAnalyzeContentRequest",
        "BidiStreamingAnalyzeContentResponse",
    },
)


class DatastoreResponseReason(proto.Enum):
    r"""Response reason from datastore which indicates data serving
    status or answer quality degradation.

    Values:
        DATASTORE_RESPONSE_REASON_UNSPECIFIED (0):
            Default value.
        NONE (1):
            No specific response reason from datastore.
        SEARCH_OUT_OF_QUOTA (2):
            Search is blocked due to out of quota.
        SEARCH_EMPTY_RESULTS (3):
            Search returns empty results.
        ANSWER_GENERATION_GEN_AI_DISABLED (4):
            Generative AI is disabled.
        ANSWER_GENERATION_OUT_OF_QUOTA (5):
            Answer generation is blocked due to out of
            quota.
        ANSWER_GENERATION_ERROR (6):
            Answer generation encounters an error.
        ANSWER_GENERATION_NOT_ENOUGH_INFO (7):
            Answer generation does not have enough
            information to generate answer.
        ANSWER_GENERATION_RAI_FAILED (8):
            Answer generation is blocked by RAI
            (Responsible AI) failure.
        ANSWER_GENERATION_NOT_GROUNDED (9):
            Answer generation is not grounded on reliable
            sources.
    """

    DATASTORE_RESPONSE_REASON_UNSPECIFIED = 0
    NONE = 1
    SEARCH_OUT_OF_QUOTA = 2
    SEARCH_EMPTY_RESULTS = 3
    ANSWER_GENERATION_GEN_AI_DISABLED = 4
    ANSWER_GENERATION_OUT_OF_QUOTA = 5
    ANSWER_GENERATION_ERROR = 6
    ANSWER_GENERATION_NOT_ENOUGH_INFO = 7
    ANSWER_GENERATION_RAI_FAILED = 8
    ANSWER_GENERATION_NOT_GROUNDED = 9


class Participant(proto.Message):
    r"""Represents a conversation participant (human agent, virtual
    agent, end-user).

    Attributes:
        name (str):
            Optional. The unique identifier of this participant. Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>``.
        role (google.cloud.dialogflow_v2.types.Participant.Role):
            Immutable. The role this participant plays in
            the conversation. This field must be set during
            participant creation and is then immutable.
        sip_recording_media_label (str):
            Optional. Label applied to streams
            representing this participant in SIPREC XML
            metadata and SDP. This is used to assign
            transcriptions from that media stream to this
            participant. This field can be updated.
        obfuscated_external_user_id (str):
            Optional. Obfuscated user id that should be associated with
            the created participant.

            You can specify a user id as follows:

            1. If you set this field in
               [CreateParticipantRequest][google.cloud.dialogflow.v2.CreateParticipantRequest.participant]
               or
               [UpdateParticipantRequest][google.cloud.dialogflow.v2.UpdateParticipantRequest.participant],
               Dialogflow adds the obfuscated user id with the
               participant.

            2. If you set this field in
               [AnalyzeContent][google.cloud.dialogflow.v2.AnalyzeContentRequest.obfuscated_external_user_id]
               or [StreamingAnalyzeContent]
               [google.cloud.dialogflow.v2.StreamingAnalyzeContentRequest.obfuscated_external_user_id],
               Dialogflow will update
               [Participant.obfuscated_external_user_id][google.cloud.dialogflow.v2.Participant.obfuscated_external_user_id].

            Dialogflow returns an error if you try to add a user id for
            a
            non-[END_USER][google.cloud.dialogflow.v2.Participant.Role.END_USER]
            participant.

            Dialogflow uses this user id for billing and measurement
            purposes. For example, Dialogflow determines whether a user
            in one conversation returned in a later conversation.

            Additionally, to link an escalated Virtual Agent
            conversation with its corresponding Agent Assist
            conversation for analytics, this field in Agent Assist
            conversations should be populated to indicate the user id of
            the ``END_USER`` participant in the escalated conversation.

            Note:

            - Please never pass raw user ids to Dialogflow. Always
              obfuscate your user id first.
            - Dialogflow only accepts a UTF-8 encoded string, e.g., a
              hex digest of a hash function like SHA-512.
            - The length of the user id must be <= 256 characters.
        documents_metadata_filters (MutableMapping[str, str]):
            Optional. Key-value filters on the metadata of documents
            returned by article suggestion. If specified, article
            suggestion only returns suggested documents that match all
            filters in their
            [Document.metadata][google.cloud.dialogflow.v2.Document.metadata].
            Multiple values for a metadata key should be concatenated by
            comma. For example, filters to match all documents that have
            'US' or 'CA' in their market metadata values and 'agent' in
            their user metadata values will be

            ::

               documents_metadata_filters {
                 key: "market"
                 value: "US,CA"
               }
               documents_metadata_filters {
                 key: "user"
                 value: "agent"
               }
        agent_desktop_source (google.cloud.dialogflow_v2.types.Participant.AgentDesktopSource):
            Optional. For tracking the utilization of prebuilt Agent
            Assist integration modules. This field is only inscope for
            Integration type that include UI Modules, Backend Modules,
            and Agent Desktop connector, it is out of scope for CCaaS
            and Direct Integration. For each human agent, prebuilt UI
            Modules needs to trigger the UpdateParticipant API to update
            this field. Both
            [CreateParticipantRequest][google.cloud.dialogflow.v2.CreateParticipantRequest.participant]
            and
            [UpdateParticipantRequest][google.cloud.dialogflow.v2.UpdateParticipantRequest.participant]
            will be supported.
    """

    class Role(proto.Enum):
        r"""Enumeration of the roles a participant can play in a
        conversation.

        Values:
            ROLE_UNSPECIFIED (0):
                Participant role not set.
            HUMAN_AGENT (1):
                Participant is a human agent.
            AUTOMATED_AGENT (2):
                Participant is an automated agent, such as a
                Dialogflow agent.
            END_USER (3):
                Participant is an end user that has called or
                chatted with Dialogflow services.
        """

        ROLE_UNSPECIFIED = 0
        HUMAN_AGENT = 1
        AUTOMATED_AGENT = 2
        END_USER = 3

    class AgentDesktopSource(proto.Enum):
        r"""Enumeration of the Agent Desktop Source when using prebuilt
        Agent Assist integration modules.

        Values:
            AGENT_DESKTOP_SOURCE_UNSPECIFIED (0):
                Agent Desktop Source is not specified.
            LIVE_PERSON (1):
                Agent Desktop Source is Live Person.
            GENESYS_CLOUD (2):
                Agent Desktop Source is Genesys Cloud.
            TWILIO (3):
                Agent Desktop Source is Twilio.
            SALESFORCE (4):
                Agent Desktop Source is Salesforce.
            OTHER (8):
                UI Modules are in use but the desktop is
                either not currently released or setting this
                field to the applicable desktop.
        """

        AGENT_DESKTOP_SOURCE_UNSPECIFIED = 0
        LIVE_PERSON = 1
        GENESYS_CLOUD = 2
        TWILIO = 3
        SALESFORCE = 4
        OTHER = 8

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    role: Role = proto.Field(
        proto.ENUM,
        number=2,
        enum=Role,
    )
    sip_recording_media_label: str = proto.Field(
        proto.STRING,
        number=6,
    )
    obfuscated_external_user_id: str = proto.Field(
        proto.STRING,
        number=7,
    )
    documents_metadata_filters: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=8,
    )
    agent_desktop_source: AgentDesktopSource = proto.Field(
        proto.ENUM,
        number=10,
        enum=AgentDesktopSource,
    )


class Message(proto.Message):
    r"""Represents a message posted into a conversation.

    Attributes:
        name (str):
            Optional. The unique identifier of the message. Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/messages/<Message ID>``.
        content (str):
            Optional. The message content. Only one of ``content`` and
            ``companion_query`` should be set - not both.
        response_messages (MutableSequence[google.cloud.dialogflow_v2.types.ResponseMessage]):
            Optional. Automated agent responses.
        language_code (str):
            Optional. The message language. This should be a
            `BCP-47 <https://www.rfc-editor.org/rfc/bcp/bcp47.txt>`__
            language tag. Example: "en-US".
        participant (str):
            Output only. The participant that sends this
            message.
        participant_role (google.cloud.dialogflow_v2.types.Participant.Role):
            Output only. The role of the participant.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the message was
            created in Contact Center AI.
        send_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. The time when the message was sent.
            For voice messages, this is the time when an
            utterance started.
        message_annotation (google.cloud.dialogflow_v2.types.MessageAnnotation):
            Output only. The annotation for the message.
        sentiment_analysis (google.cloud.dialogflow_v2.types.SentimentAnalysisResult):
            Output only. The sentiment analysis result
            for the message.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    content: str = proto.Field(
        proto.STRING,
        number=2,
    )
    response_messages: MutableSequence["ResponseMessage"] = proto.RepeatedField(
        proto.MESSAGE,
        number=11,
        message="ResponseMessage",
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=3,
    )
    participant: str = proto.Field(
        proto.STRING,
        number=4,
    )
    participant_role: "Participant.Role" = proto.Field(
        proto.ENUM,
        number=5,
        enum="Participant.Role",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    send_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    message_annotation: "MessageAnnotation" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="MessageAnnotation",
    )
    sentiment_analysis: session.SentimentAnalysisResult = proto.Field(
        proto.MESSAGE,
        number=8,
        message=session.SentimentAnalysisResult,
    )


class CreateParticipantRequest(proto.Message):
    r"""The request message for
    [Participants.CreateParticipant][google.cloud.dialogflow.v2.Participants.CreateParticipant].

    Attributes:
        parent (str):
            Required. Resource identifier of the conversation adding the
            participant. Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>``.
        participant (google.cloud.dialogflow_v2.types.Participant):
            Required. The participant to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    participant: "Participant" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Participant",
    )


class GetParticipantRequest(proto.Message):
    r"""The request message for
    [Participants.GetParticipant][google.cloud.dialogflow.v2.Participants.GetParticipant].

    Attributes:
        name (str):
            Required. The name of the participant. Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListParticipantsRequest(proto.Message):
    r"""The request message for
    [Participants.ListParticipants][google.cloud.dialogflow.v2.Participants.ListParticipants].

    Attributes:
        parent (str):
            Required. The conversation to list all participants from.
            Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>``.
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
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListParticipantsResponse(proto.Message):
    r"""The response message for
    [Participants.ListParticipants][google.cloud.dialogflow.v2.Participants.ListParticipants].

    Attributes:
        participants (MutableSequence[google.cloud.dialogflow_v2.types.Participant]):
            The list of participants. There is a maximum number of items
            returned based on the page_size field in the request.
        next_page_token (str):
            Token to retrieve the next page of results or
            empty if there are no more results in the list.
    """

    @property
    def raw_page(self):
        return self

    participants: MutableSequence["Participant"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Participant",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateParticipantRequest(proto.Message):
    r"""The request message for
    [Participants.UpdateParticipant][google.cloud.dialogflow.v2.Participants.UpdateParticipant].

    Attributes:
        participant (google.cloud.dialogflow_v2.types.Participant):
            Required. The participant to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The mask to specify which fields to
            update.
    """

    participant: "Participant" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Participant",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class AnalyzeContentRequest(proto.Message):
    r"""The request message for
    [Participants.AnalyzeContent][google.cloud.dialogflow.v2.Participants.AnalyzeContent].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        participant (str):
            Required. The name of the participant this text comes from.
            Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>``.
        text_input (google.cloud.dialogflow_v2.types.TextInput):
            The natural language text to be processed.

            This field is a member of `oneof`_ ``input``.
        audio_input (google.cloud.dialogflow_v2.types.AudioInput):
            The natural language speech audio to be
            processed.

            This field is a member of `oneof`_ ``input``.
        event_input (google.cloud.dialogflow_v2.types.EventInput):
            An input event to send to Dialogflow.

            This field is a member of `oneof`_ ``input``.
        suggestion_input (google.cloud.dialogflow_v2.types.SuggestionInput):
            An input representing the selection of a
            suggestion.

            This field is a member of `oneof`_ ``input``.
        reply_audio_config (google.cloud.dialogflow_v2.types.OutputAudioConfig):
            Speech synthesis configuration.
            The speech synthesis settings for a virtual
            agent that may be configured for the associated
            conversation profile are not used when calling
            AnalyzeContent. If this configuration is not
            supplied, speech synthesis is disabled.
        query_params (google.cloud.dialogflow_v2.types.QueryParameters):
            Parameters for a Dialogflow virtual-agent
            query.
        assist_query_params (google.cloud.dialogflow_v2.types.AssistQueryParameters):
            Parameters for a human assist query.
        cx_parameters (google.protobuf.struct_pb2.Struct):
            Additional parameters to be put into
            Dialogflow CX session parameters. To remove a
            parameter from the session, clients should
            explicitly set the parameter value to null.

            Note: this field should only be used if you are
            connecting to a Dialogflow CX agent.
        request_id (str):
            A unique identifier for this request. Restricted to 36 ASCII
            characters. A random UUID is recommended. This request is
            only idempotent if a ``request_id`` is provided.
    """

    participant: str = proto.Field(
        proto.STRING,
        number=1,
    )
    text_input: session.TextInput = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="input",
        message=session.TextInput,
    )
    audio_input: "AudioInput" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="input",
        message="AudioInput",
    )
    event_input: session.EventInput = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="input",
        message=session.EventInput,
    )
    suggestion_input: "SuggestionInput" = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="input",
        message="SuggestionInput",
    )
    reply_audio_config: gcd_audio_config.OutputAudioConfig = proto.Field(
        proto.MESSAGE,
        number=5,
        message=gcd_audio_config.OutputAudioConfig,
    )
    query_params: session.QueryParameters = proto.Field(
        proto.MESSAGE,
        number=9,
        message=session.QueryParameters,
    )
    assist_query_params: "AssistQueryParameters" = proto.Field(
        proto.MESSAGE,
        number=14,
        message="AssistQueryParameters",
    )
    cx_parameters: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=18,
        message=struct_pb2.Struct,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=11,
    )


class DtmfParameters(proto.Message):
    r"""The message in the response that indicates the parameters of
    DTMF.

    Attributes:
        accepts_dtmf_input (bool):
            Indicates whether DTMF input can be handled
            in the next request.
    """

    accepts_dtmf_input: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class AnalyzeContentResponse(proto.Message):
    r"""The response message for
    [Participants.AnalyzeContent][google.cloud.dialogflow.v2.Participants.AnalyzeContent].

    Attributes:
        reply_text (str):
            The output text content.
            This field is set if the automated agent
            responded with text to show to the user.
        reply_audio (google.cloud.dialogflow_v2.types.OutputAudio):
            The audio data bytes encoded as specified in the request.
            This field is set if:

            - ``reply_audio_config`` was specified in the request, or
            - The automated agent responded with audio to play to the
              user. In such case, ``reply_audio.config`` contains
              settings used to synthesize the speech.

            In some scenarios, multiple output audio fields may be
            present in the response structure. In these cases, only the
            top-most-level audio output has content.
        automated_agent_reply (google.cloud.dialogflow_v2.types.AutomatedAgentReply):
            Only set if a Dialogflow automated agent has responded. Note
            that in [AutomatedAgentReply.DetectIntentResponse][],
            [Sessions.DetectIntentResponse.output_audio][] and
            [Sessions.DetectIntentResponse.output_audio_config][] are
            always empty, use
            [reply_audio][google.cloud.dialogflow.v2.AnalyzeContentResponse.reply_audio]
            instead.
        message (google.cloud.dialogflow_v2.types.Message):
            Message analyzed by CCAI.
        human_agent_suggestion_results (MutableSequence[google.cloud.dialogflow_v2.types.SuggestionResult]):
            The suggestions for most recent human agent. The order is
            the same as
            [HumanAgentAssistantConfig.SuggestionConfig.feature_configs][google.cloud.dialogflow.v2.HumanAgentAssistantConfig.SuggestionConfig.feature_configs]
            of
            [HumanAgentAssistantConfig.human_agent_suggestion_config][google.cloud.dialogflow.v2.HumanAgentAssistantConfig.human_agent_suggestion_config].

            Note that any failure of Agent Assist features will not lead
            to the overall failure of an AnalyzeContent API call.
            Instead, the features will fail silently with the error
            field set in the corresponding SuggestionResult.
        end_user_suggestion_results (MutableSequence[google.cloud.dialogflow_v2.types.SuggestionResult]):
            The suggestions for end user. The order is the same as
            [HumanAgentAssistantConfig.SuggestionConfig.feature_configs][google.cloud.dialogflow.v2.HumanAgentAssistantConfig.SuggestionConfig.feature_configs]
            of
            [HumanAgentAssistantConfig.end_user_suggestion_config][google.cloud.dialogflow.v2.HumanAgentAssistantConfig.end_user_suggestion_config].

            Same as human_agent_suggestion_results, any failure of Agent
            Assist features will not lead to the overall failure of an
            AnalyzeContent API call. Instead, the features will fail
            silently with the error field set in the corresponding
            SuggestionResult.
        dtmf_parameters (google.cloud.dialogflow_v2.types.DtmfParameters):
            Indicates the parameters of DTMF.
    """

    reply_text: str = proto.Field(
        proto.STRING,
        number=1,
    )
    reply_audio: "OutputAudio" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="OutputAudio",
    )
    automated_agent_reply: "AutomatedAgentReply" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="AutomatedAgentReply",
    )
    message: "Message" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="Message",
    )
    human_agent_suggestion_results: MutableSequence["SuggestionResult"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=6,
            message="SuggestionResult",
        )
    )
    end_user_suggestion_results: MutableSequence["SuggestionResult"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=7,
            message="SuggestionResult",
        )
    )
    dtmf_parameters: "DtmfParameters" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="DtmfParameters",
    )


class StreamingAnalyzeContentRequest(proto.Message):
    r"""The top-level message sent by the client to the
    [Participants.StreamingAnalyzeContent][google.cloud.dialogflow.v2.Participants.StreamingAnalyzeContent]
    method.

    Multiple request messages should be sent in order:

    1. The first message must contain
       [participant][google.cloud.dialogflow.v2.StreamingAnalyzeContentRequest.participant],
       [config][google.cloud.dialogflow.v2.StreamingAnalyzeContentRequest.config]
       and optionally
       [query_params][google.cloud.dialogflow.v2.StreamingAnalyzeContentRequest.query_params].
       If you want to receive an audio response, it should also contain
       [reply_audio_config][google.cloud.dialogflow.v2.StreamingAnalyzeContentRequest.reply_audio_config].
       The message must not contain
       [input][google.cloud.dialogflow.v2.StreamingAnalyzeContentRequest.input].

    2. If
       [config][google.cloud.dialogflow.v2.StreamingAnalyzeContentRequest.config]
       in the first message was set to
       [audio_config][google.cloud.dialogflow.v2.StreamingAnalyzeContentRequest.audio_config],
       all subsequent messages must contain
       [input_audio][google.cloud.dialogflow.v2.StreamingAnalyzeContentRequest.input_audio]
       to continue with Speech recognition. However, note that:

       - Dialogflow will bill you for the audio so far.
       - Dialogflow discards all Speech recognition results in favor of
         the text input.

    3. If
       [StreamingAnalyzeContentRequest.config][google.cloud.dialogflow.v2.StreamingAnalyzeContentRequest.config]
       in the first message was set to
       [StreamingAnalyzeContentRequest.text_config][google.cloud.dialogflow.v2.StreamingAnalyzeContentRequest.text_config],
       then the second message must contain only
       [input_text][google.cloud.dialogflow.v2.StreamingAnalyzeContentRequest.input_text].
       Moreover, you must not send more than two messages.

    After you sent all input, you must half-close or abort the request
    stream.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        participant (str):
            Required. The name of the participant this text comes from.
            Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>``.
        audio_config (google.cloud.dialogflow_v2.types.InputAudioConfig):
            Instructs the speech recognizer how to
            process the speech audio.

            This field is a member of `oneof`_ ``config``.
        text_config (google.cloud.dialogflow_v2.types.InputTextConfig):
            The natural language text to be processed.

            This field is a member of `oneof`_ ``config``.
        reply_audio_config (google.cloud.dialogflow_v2.types.OutputAudioConfig):
            Speech synthesis configuration.
            The speech synthesis settings for a virtual
            agent that may be configured for the associated
            conversation profile are not used when calling
            StreamingAnalyzeContent. If this configuration
            is not supplied, speech synthesis is disabled.
        input_audio (bytes):
            The input audio content to be recognized. Must be sent if
            ``audio_config`` is set in the first message. The complete
            audio over all streaming messages must not exceed 1 minute.

            This field is a member of `oneof`_ ``input``.
        input_text (str):
            The UTF-8 encoded natural language text to be processed.
            Must be sent if ``text_config`` is set in the first message.
            Text length must not exceed 256 bytes for virtual agent
            interactions. The ``input_text`` field can be only sent
            once, and would cancel the speech recognition if any
            ongoing.

            This field is a member of `oneof`_ ``input``.
        input_dtmf (google.cloud.dialogflow_v2.types.TelephonyDtmfEvents):
            The DTMF digits used to invoke intent and
            fill in parameter value.
            This input is ignored if the previous response
            indicated that DTMF input is not accepted.

            This field is a member of `oneof`_ ``input``.
        suggestion_input (google.cloud.dialogflow_v2.types.SuggestionInput):
            Optional. Input for confirming, revising, or
            canceling a suggestion.

            This field is a member of `oneof`_ ``input``.
        query_params (google.cloud.dialogflow_v2.types.QueryParameters):
            Parameters for a Dialogflow virtual-agent
            query.
        assist_query_params (google.cloud.dialogflow_v2.types.AssistQueryParameters):
            Parameters for a human assist query.
        cx_parameters (google.protobuf.struct_pb2.Struct):
            Additional parameters to be put into
            Dialogflow CX session parameters. To remove a
            parameter from the session, clients should
            explicitly set the parameter value to null.

            Note: this field should only be used if you are
            connecting to a Dialogflow CX agent.
        enable_extended_streaming (bool):
            Optional. Enable full bidirectional streaming. You can keep
            streaming the audio until timeout, and there's no need to
            half close the stream to get the response.

            Restrictions:

            - Timeout: 3 mins.
            - Audio Encoding: only supports
              [AudioEncoding.AUDIO_ENCODING_LINEAR_16][google.cloud.dialogflow.v2.AudioEncoding.AUDIO_ENCODING_LINEAR_16]
              and
              [AudioEncoding.AUDIO_ENCODING_MULAW][google.cloud.dialogflow.v2.AudioEncoding.AUDIO_ENCODING_MULAW]
            - Lifecycle: conversation should be in ``Assist Stage``, go
              to
              [Conversations.CreateConversation][google.cloud.dialogflow.v2.Conversations.CreateConversation]
              for more information.

            InvalidArgument Error will be returned if the one of
            restriction checks failed.

            You can find more details in
            https://cloud.google.com/agent-assist/docs/extended-streaming
        enable_partial_automated_agent_reply (bool):
            Optional. Enable partial responses from Dialogflow CX agent.
            If this flag is not enabled, response stream still contains
            only one final response even if some ``Fulfillment``\ s in
            Dialogflow CX agent have been configured to return partial
            responses.
        output_multiple_utterances (bool):
            Optional. If multiple uttereances are
            detected in the audio stream, process them
            individually instead of stitching them together
            to form a single utterance.
        enable_debugging_info (bool):
            If true, ``StreamingAnalyzeContentResponse.debugging_info``
            will get populated.
    """

    participant: str = proto.Field(
        proto.STRING,
        number=1,
    )
    audio_config: gcd_audio_config.InputAudioConfig = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="config",
        message=gcd_audio_config.InputAudioConfig,
    )
    text_config: "InputTextConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="config",
        message="InputTextConfig",
    )
    reply_audio_config: gcd_audio_config.OutputAudioConfig = proto.Field(
        proto.MESSAGE,
        number=4,
        message=gcd_audio_config.OutputAudioConfig,
    )
    input_audio: bytes = proto.Field(
        proto.BYTES,
        number=5,
        oneof="input",
    )
    input_text: str = proto.Field(
        proto.STRING,
        number=6,
        oneof="input",
    )
    input_dtmf: gcd_audio_config.TelephonyDtmfEvents = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="input",
        message=gcd_audio_config.TelephonyDtmfEvents,
    )
    suggestion_input: "SuggestionInput" = proto.Field(
        proto.MESSAGE,
        number=27,
        oneof="input",
        message="SuggestionInput",
    )
    query_params: session.QueryParameters = proto.Field(
        proto.MESSAGE,
        number=7,
        message=session.QueryParameters,
    )
    assist_query_params: "AssistQueryParameters" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="AssistQueryParameters",
    )
    cx_parameters: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=13,
        message=struct_pb2.Struct,
    )
    enable_extended_streaming: bool = proto.Field(
        proto.BOOL,
        number=11,
    )
    enable_partial_automated_agent_reply: bool = proto.Field(
        proto.BOOL,
        number=12,
    )
    output_multiple_utterances: bool = proto.Field(
        proto.BOOL,
        number=18,
    )
    enable_debugging_info: bool = proto.Field(
        proto.BOOL,
        number=19,
    )


class StreamingAnalyzeContentResponse(proto.Message):
    r"""The top-level message returned from the ``StreamingAnalyzeContent``
    method.

    Multiple response messages can be returned in order:

    1. If the input was set to streaming audio, the first one or more
       messages contain ``recognition_result``. Each
       ``recognition_result`` represents a more complete transcript of
       what the user said. When a user speaks multiple sentences, the
       API will emit multiple messages where ``is_final = true``. Each
       time the system detects a distinct pause or completed thought, it
       locks in that segment, marks it ``is_final = true``, and then
       immediately starts a new recognition cycle for the next sentence
       on the same stream.

    2. In virtual agent stage: if
       ``enable_partial_automated_agent_reply`` is true, the following N
       (currently 1 <= N <= 4) messages contain
       ``automated_agent_reply`` and optionally ``reply_audio`` returned
       by the virtual agent. The first (N-1)
       ``automated_agent_reply``\ s will have
       ``automated_agent_reply_type`` set to ``PARTIAL``. The last
       ``automated_agent_reply`` has ``automated_agent_reply_type`` set
       to ``FINAL``. If ``enable_partial_automated_agent_reply`` is not
       enabled, response stream only contains the final reply.

       In human assist stage: the following N (N >= 1) messages contain
       ``human_agent_suggestion_results``,
       ``end_user_suggestion_results`` or ``message``.

    Attributes:
        recognition_result (google.cloud.dialogflow_v2.types.StreamingRecognitionResult):
            The result of speech recognition.
        reply_text (str):
            The output text content.
            This field is set if an automated agent
            responded with a text for the user.
        reply_audio (google.cloud.dialogflow_v2.types.OutputAudio):
            The audio data bytes encoded as specified in the request.
            This field is set if:

            - The ``reply_audio_config`` field is specified in the
              request.
            - The automated agent, which this output comes from,
              responded with audio. In such case, the
              ``reply_audio.config`` field contains settings used to
              synthesize the speech.

            In some scenarios, multiple output audio fields may be
            present in the response structure. In these cases, only the
            top-most-level audio output has content.
        automated_agent_reply (google.cloud.dialogflow_v2.types.AutomatedAgentReply):
            Note that in [AutomatedAgentReply.DetectIntentResponse][],
            [Sessions.DetectIntentResponse.output_audio][] and
            [Sessions.DetectIntentResponse.output_audio_config][] are
            always empty, use
            [reply_audio][google.cloud.dialogflow.v2.StreamingAnalyzeContentResponse.reply_audio]
            instead.
        message (google.cloud.dialogflow_v2.types.Message):
            Message analyzed by CCAI.
        human_agent_suggestion_results (MutableSequence[google.cloud.dialogflow_v2.types.SuggestionResult]):
            The suggestions for most recent human agent. The order is
            the same as
            [HumanAgentAssistantConfig.SuggestionConfig.feature_configs][google.cloud.dialogflow.v2.HumanAgentAssistantConfig.SuggestionConfig.feature_configs]
            of
            [HumanAgentAssistantConfig.human_agent_suggestion_config][google.cloud.dialogflow.v2.HumanAgentAssistantConfig.human_agent_suggestion_config].
        end_user_suggestion_results (MutableSequence[google.cloud.dialogflow_v2.types.SuggestionResult]):
            The suggestions for end user. The order is the same as
            [HumanAgentAssistantConfig.SuggestionConfig.feature_configs][google.cloud.dialogflow.v2.HumanAgentAssistantConfig.SuggestionConfig.feature_configs]
            of
            [HumanAgentAssistantConfig.end_user_suggestion_config][google.cloud.dialogflow.v2.HumanAgentAssistantConfig.end_user_suggestion_config].
        dtmf_parameters (google.cloud.dialogflow_v2.types.DtmfParameters):
            Indicates the parameters of DTMF.
        debugging_info (google.cloud.dialogflow_v2.types.CloudConversationDebuggingInfo):
            Debugging info that would get populated when
            ``StreamingAnalyzeContentRequest.enable_debugging_info`` is
            set to true.
        speech_model (str):
            The name of the actual Cloud speech model
            used for speech recognition.
    """

    recognition_result: session.StreamingRecognitionResult = proto.Field(
        proto.MESSAGE,
        number=1,
        message=session.StreamingRecognitionResult,
    )
    reply_text: str = proto.Field(
        proto.STRING,
        number=2,
    )
    reply_audio: "OutputAudio" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="OutputAudio",
    )
    automated_agent_reply: "AutomatedAgentReply" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="AutomatedAgentReply",
    )
    message: "Message" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="Message",
    )
    human_agent_suggestion_results: MutableSequence["SuggestionResult"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=7,
            message="SuggestionResult",
        )
    )
    end_user_suggestion_results: MutableSequence["SuggestionResult"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=8,
            message="SuggestionResult",
        )
    )
    dtmf_parameters: "DtmfParameters" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="DtmfParameters",
    )
    debugging_info: session.CloudConversationDebuggingInfo = proto.Field(
        proto.MESSAGE,
        number=11,
        message=session.CloudConversationDebuggingInfo,
    )
    speech_model: str = proto.Field(
        proto.STRING,
        number=13,
    )


class SuggestArticlesRequest(proto.Message):
    r"""The request message for
    [Participants.SuggestArticles][google.cloud.dialogflow.v2.Participants.SuggestArticles].

    Attributes:
        parent (str):
            Required. The name of the participant to fetch suggestion
            for. Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>``.
        latest_message (str):
            Optional. The name of the latest conversation message to
            compile suggestion for. If empty, it will be the latest
            message of the conversation.

            Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/messages/<Message ID>``.
        context_size (int):
            Optional. Max number of messages prior to and including
            [latest_message][google.cloud.dialogflow.v2.SuggestArticlesRequest.latest_message]
            to use as context when compiling the suggestion. By default
            20 and at most 50.
        assist_query_params (google.cloud.dialogflow_v2.types.AssistQueryParameters):
            Parameters for a human assist query.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    latest_message: str = proto.Field(
        proto.STRING,
        number=2,
    )
    context_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    assist_query_params: "AssistQueryParameters" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="AssistQueryParameters",
    )


class SuggestArticlesResponse(proto.Message):
    r"""The response message for
    [Participants.SuggestArticles][google.cloud.dialogflow.v2.Participants.SuggestArticles].

    Attributes:
        article_answers (MutableSequence[google.cloud.dialogflow_v2.types.ArticleAnswer]):
            Articles ordered by score in descending
            order.
        latest_message (str):
            The name of the latest conversation message used to compile
            suggestion for.

            Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/messages/<Message ID>``.
        context_size (int):
            Number of messages prior to and including
            [latest_message][google.cloud.dialogflow.v2.SuggestArticlesResponse.latest_message]
            to compile the suggestion. It may be smaller than the
            [SuggestArticlesRequest.context_size][google.cloud.dialogflow.v2.SuggestArticlesRequest.context_size]
            field in the request if there aren't that many messages in
            the conversation.
    """

    article_answers: MutableSequence["ArticleAnswer"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ArticleAnswer",
    )
    latest_message: str = proto.Field(
        proto.STRING,
        number=2,
    )
    context_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class SuggestFaqAnswersRequest(proto.Message):
    r"""The request message for
    [Participants.SuggestFaqAnswers][google.cloud.dialogflow.v2.Participants.SuggestFaqAnswers].

    Attributes:
        parent (str):
            Required. The name of the participant to fetch suggestion
            for. Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>``.
        latest_message (str):
            Optional. The name of the latest conversation message to
            compile suggestion for. If empty, it will be the latest
            message of the conversation.

            Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/messages/<Message ID>``.
        context_size (int):
            Optional. Max number of messages prior to and including
            [latest_message] to use as context when compiling the
            suggestion. By default 20 and at most 50.
        assist_query_params (google.cloud.dialogflow_v2.types.AssistQueryParameters):
            Parameters for a human assist query.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    latest_message: str = proto.Field(
        proto.STRING,
        number=2,
    )
    context_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    assist_query_params: "AssistQueryParameters" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="AssistQueryParameters",
    )


class SuggestFaqAnswersResponse(proto.Message):
    r"""The request message for
    [Participants.SuggestFaqAnswers][google.cloud.dialogflow.v2.Participants.SuggestFaqAnswers].

    Attributes:
        faq_answers (MutableSequence[google.cloud.dialogflow_v2.types.FaqAnswer]):
            Answers extracted from FAQ documents.
        latest_message (str):
            The name of the latest conversation message used to compile
            suggestion for.

            Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/messages/<Message ID>``.
        context_size (int):
            Number of messages prior to and including
            [latest_message][google.cloud.dialogflow.v2.SuggestFaqAnswersResponse.latest_message]
            to compile the suggestion. It may be smaller than the
            [SuggestFaqAnswersRequest.context_size][google.cloud.dialogflow.v2.SuggestFaqAnswersRequest.context_size]
            field in the request if there aren't that many messages in
            the conversation.
    """

    faq_answers: MutableSequence["FaqAnswer"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="FaqAnswer",
    )
    latest_message: str = proto.Field(
        proto.STRING,
        number=2,
    )
    context_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class GenerateSuggestionsResponse(proto.Message):
    r"""The response message for
    [Conversations.GenerateSuggestions][google.cloud.dialogflow.v2.Conversations.GenerateSuggestions].

    Attributes:
        generator_suggestion_answers (MutableSequence[google.cloud.dialogflow_v2.types.GenerateSuggestionsResponse.GeneratorSuggestionAnswer]):
            The answers generated for the conversation
            based on context.
        latest_message (str):
            The name of the latest conversation message used as context
            for compiling suggestion.

            Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/messages/<Message ID>``.
    """

    class GeneratorSuggestionAnswer(proto.Message):
        r"""A GeneratorSuggestion answer.

        Attributes:
            generator_suggestion (google.cloud.dialogflow_v2.types.GeneratorSuggestion):
                Suggestion details.
            source_generator (str):
                The name of the generator used to generate this suggestion.
                Format:
                ``projects/<Project ID>/locations/<Location ID>/generators/<Generator ID>``.
            answer_record (str):
                Answer record that uniquely identifies the
                suggestion. This can be used to provide
                suggestion feedback.
        """

        generator_suggestion: generator.GeneratorSuggestion = proto.Field(
            proto.MESSAGE,
            number=1,
            message=generator.GeneratorSuggestion,
        )
        source_generator: str = proto.Field(
            proto.STRING,
            number=2,
        )
        answer_record: str = proto.Field(
            proto.STRING,
            number=3,
        )

    generator_suggestion_answers: MutableSequence[GeneratorSuggestionAnswer] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=GeneratorSuggestionAnswer,
        )
    )
    latest_message: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ToolCallSuggestion(proto.Message):
    r"""Structured wrapper that pairs tool execution details with
    strongly-typed citations.

    Attributes:
        tool_call_info (google.cloud.dialogflow_v2.types.GeneratorSuggestion.ToolCallInfo):
            Optional. Tool execution request/response
            details.
        text_update (str):
            Optional. The conversational text update
            generated by the agent accompanying this tool
            call (e.g. "The status of your order 12345 is
            currently being retrieved..."). This is a status
            update emitted alongside in-flight tool
            execution and is not accumulated into the final
            response.
    """

    tool_call_info: generator.GeneratorSuggestion.ToolCallInfo = proto.Field(
        proto.MESSAGE,
        number=1,
        message=generator.GeneratorSuggestion.ToolCallInfo,
    )
    text_update: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ToolCallEvents(proto.Message):
    r"""Represents events containing tool call execution progress.

    Attributes:
        tool_call_suggestions (MutableSequence[google.cloud.dialogflow_v2.types.ToolCallSuggestion]):
            Optional. Tool call suggestions associated
            with these events.
    """

    tool_call_suggestions: MutableSequence["ToolCallSuggestion"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ToolCallSuggestion",
    )


class CompanionSuggestion(proto.Message):
    r"""Represents a companion suggestion answer.

    Attributes:
        guidances (MutableSequence[google.cloud.dialogflow_v2.types.CompanionSuggestion.Guidance]):
            List of guidances generated by the Companion
            Agent.
    """

    class Guidance(proto.Message):
        r"""Represents guidance for companion suggestion.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            suggested_reply (str):
                Suggested reply for the agent to respond to
                the customer.
            suggested_action (str):
                Suggested action to human agent. For example,
                "Ask the customer for their shipping address" or
                "Create a new case for the customer".
            instruction_source (google.cloud.dialogflow_v2.types.GuidanceInstruction):
                Guidance instruction source.
            knowledge_sources (MutableSequence[google.cloud.dialogflow_v2.types.CompanionSuggestion.Guidance.KnowledgeSource]):
                Knowledge sources.
            explanation (str):
                Optional. A brief explanation of why the
                action is suggested.
            grounding_metadata (google.cloud.dialogflow_v2.types.GroundingMetadata):
                Optional. Grounding metadata for the
                generated guidance.

                This field is a member of `oneof`_ ``_grounding_metadata``.
            tool_calls (MutableSequence[google.cloud.dialogflow_v2.types.ToolCallSuggestion]):
                Optional. Rich structured tool calls and
                their associated citations delivered directly as
                suggestions.
            triggering_tool_call_answer_records (MutableSequence[str]):
                Optional. The AnswerRecords of the tool calls that triggered
                this guidance. Format:
                ``projects/<Project ID>/locations/<Location ID>/answerRecords/<Answer Record ID>``.
        """

        class KnowledgeSource(proto.Message):
            r"""Represents a knowledge source for the guidance.

            Attributes:
                knowledge_article_url (str):
                    URL of the knowledge article.
                knowledge_article_title (str):
                    Knowledge article title.
                knowledge_snippet (str):
                    Knowledge snippet.
            """

            knowledge_article_url: str = proto.Field(
                proto.STRING,
                number=1,
            )
            knowledge_article_title: str = proto.Field(
                proto.STRING,
                number=2,
            )
            knowledge_snippet: str = proto.Field(
                proto.STRING,
                number=3,
            )

        suggested_reply: str = proto.Field(
            proto.STRING,
            number=1,
        )
        suggested_action: str = proto.Field(
            proto.STRING,
            number=2,
        )
        instruction_source: companion_agent.GuidanceInstruction = proto.Field(
            proto.MESSAGE,
            number=3,
            message=companion_agent.GuidanceInstruction,
        )
        knowledge_sources: MutableSequence[
            "CompanionSuggestion.Guidance.KnowledgeSource"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message="CompanionSuggestion.Guidance.KnowledgeSource",
        )
        explanation: str = proto.Field(
            proto.STRING,
            number=12,
        )
        grounding_metadata: grounding.GroundingMetadata = proto.Field(
            proto.MESSAGE,
            number=6,
            optional=True,
            message=grounding.GroundingMetadata,
        )
        tool_calls: MutableSequence["ToolCallSuggestion"] = proto.RepeatedField(
            proto.MESSAGE,
            number=7,
            message="ToolCallSuggestion",
        )
        triggering_tool_call_answer_records: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=11,
        )

    guidances: MutableSequence[Guidance] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=Guidance,
    )


class GenerateCompanionSuggestionsResponse(proto.Message):
    r"""Represents the response message for
    GenerateCompanionSuggestions.

    Attributes:
        companion_suggestion (google.cloud.dialogflow_v2.types.CompanionSuggestion):
            Contains the core suggestion generated by the
            Companion Agent.
        answer_record (str):
            Answer record that uniquely identifies the suggestion.
            Format:
            ``projects/<Project ID>/locations/<Location ID>/answerRecords/<Answer Record ID>``.
        latest_message (str):
            The name of the latest conversation message used to compile
            suggestion for. Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/messages/<Message ID>``.
        suggestion_index (int):
            Output only. The 1-based sequential index of
            the suggestion generated in this session.
    """

    companion_suggestion: "CompanionSuggestion" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="CompanionSuggestion",
    )
    answer_record: str = proto.Field(
        proto.STRING,
        number=2,
    )
    latest_message: str = proto.Field(
        proto.STRING,
        number=3,
    )
    suggestion_index: int = proto.Field(
        proto.INT32,
        number=4,
    )


class SuggestSmartRepliesRequest(proto.Message):
    r"""The request message for
    [Participants.SuggestSmartReplies][google.cloud.dialogflow.v2.Participants.SuggestSmartReplies].

    Attributes:
        parent (str):
            Required. The name of the participant to fetch suggestion
            for. Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>``.
        current_text_input (google.cloud.dialogflow_v2.types.TextInput):
            The current natural language text segment to
            compile suggestion for. This provides a way for
            user to get follow up smart reply suggestion
            after a smart reply selection, without sending a
            text message.
        latest_message (str):
            The name of the latest conversation message to compile
            suggestion for. If empty, it will be the latest message of
            the conversation.

            Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/messages/<Message ID>``.
        context_size (int):
            Max number of messages prior to and including
            [latest_message] to use as context when compiling the
            suggestion. By default 20 and at most 50.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    current_text_input: session.TextInput = proto.Field(
        proto.MESSAGE,
        number=4,
        message=session.TextInput,
    )
    latest_message: str = proto.Field(
        proto.STRING,
        number=2,
    )
    context_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class SuggestSmartRepliesResponse(proto.Message):
    r"""The response message for
    [Participants.SuggestSmartReplies][google.cloud.dialogflow.v2.Participants.SuggestSmartReplies].

    Attributes:
        smart_reply_answers (MutableSequence[google.cloud.dialogflow_v2.types.SmartReplyAnswer]):
            Output only. Multiple reply options provided
            by smart reply service. The order is based on
            the rank of the model prediction. The maximum
            number of the returned replies is set in
            SmartReplyConfig.
        latest_message (str):
            The name of the latest conversation message used to compile
            suggestion for.

            Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/messages/<Message ID>``.
        context_size (int):
            Number of messages prior to and including
            [latest_message][google.cloud.dialogflow.v2.SuggestSmartRepliesResponse.latest_message]
            to compile the suggestion. It may be smaller than the
            [SuggestSmartRepliesRequest.context_size][google.cloud.dialogflow.v2.SuggestSmartRepliesRequest.context_size]
            field in the request if there aren't that many messages in
            the conversation.
    """

    smart_reply_answers: MutableSequence["SmartReplyAnswer"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SmartReplyAnswer",
    )
    latest_message: str = proto.Field(
        proto.STRING,
        number=2,
    )
    context_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class AudioInput(proto.Message):
    r"""Represents the natural language speech audio to be processed.

    Attributes:
        config (google.cloud.dialogflow_v2.types.InputAudioConfig):
            Required. Instructs the speech recognizer how
            to process the speech audio.
        audio (bytes):
            Required. The natural language speech audio
            to be processed. A single request can contain up
            to 2 minutes of speech audio data. The
            transcribed text cannot contain more than 256
            bytes for virtual agent interactions.
    """

    config: gcd_audio_config.InputAudioConfig = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcd_audio_config.InputAudioConfig,
    )
    audio: bytes = proto.Field(
        proto.BYTES,
        number=2,
    )


class OutputAudio(proto.Message):
    r"""Represents the natural language speech audio to be played to
    the end user.

    Attributes:
        config (google.cloud.dialogflow_v2.types.OutputAudioConfig):
            Instructs the speech synthesizer how to
            generate the speech audio.
        audio (bytes):
            The natural language speech audio.
    """

    config: gcd_audio_config.OutputAudioConfig = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcd_audio_config.OutputAudioConfig,
    )
    audio: bytes = proto.Field(
        proto.BYTES,
        number=2,
    )


class AutomatedAgentReply(proto.Message):
    r"""Represents a response from an automated agent.

    Attributes:
        detect_intent_response (google.cloud.dialogflow_v2.types.DetectIntentResponse):
            Response of the Dialogflow
            [Sessions.DetectIntent][google.cloud.dialogflow.v2.Sessions.DetectIntent]
            call.
        response_messages (MutableSequence[google.cloud.dialogflow_v2.types.ResponseMessage]):
            Response messages from the automated agent.
        intent (str):
            Name of the intent if an intent is matched for the query.
            For a V2 query, the value format is
            ``projects/<Project ID>/locations/ <Location ID>/agent/intents/<Intent ID>``.
            For a V3 query, the value format is
            ``projects/<Project ID>/locations/ <Location ID>/agents/<Agent ID>/intents/<Intent ID>``.
        event (str):
            Event name if an event is triggered for the
            query.
        match_confidence (float):
            The confidence of the match. Values range
            from 0.0 (completely uncertain) to 1.0
            (completely certain). This value is for
            informational purpose only and is only used to
            help match the best intent within the
            classification threshold. This value may change
            for the same end-user expression at any time due
            to a model retraining or change in
            implementation.
        parameters (google.protobuf.struct_pb2.Struct):
            The collection of current parameters at the
            time of this response.
        automated_agent_reply_type (google.cloud.dialogflow_v2.types.AutomatedAgentReply.AutomatedAgentReplyType):
            AutomatedAgentReply type.
        allow_cancellation (bool):
            Indicates whether the partial automated agent
            reply is interruptible when a later reply
            message arrives. e.g. if the agent specified
            some music as partial response, it can be
            cancelled.
        cx_current_page (str):
            The unique identifier of the current Dialogflow CX
            conversation page. Format:
            ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>/flows/<Flow ID>/pages/<Page ID>``.
        call_companion_auth_code (bytes):
            The auth code for accessing Call Companion
            UI.
    """

    class AutomatedAgentReplyType(proto.Enum):
        r"""Represents different automated agent reply types.

        Values:
            AUTOMATED_AGENT_REPLY_TYPE_UNSPECIFIED (0):
                Not specified. This should never happen.
            PARTIAL (1):
                Partial reply. e.g. Aggregated responses in a
                ``Fulfillment`` that enables ``return_partial_response`` can
                be returned as partial reply. WARNING: partial reply is not
                eligible for barge-in.
            FINAL (2):
                Final reply.
        """

        AUTOMATED_AGENT_REPLY_TYPE_UNSPECIFIED = 0
        PARTIAL = 1
        FINAL = 2

    detect_intent_response: session.DetectIntentResponse = proto.Field(
        proto.MESSAGE,
        number=1,
        message=session.DetectIntentResponse,
    )
    response_messages: MutableSequence["ResponseMessage"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="ResponseMessage",
    )
    intent: str = proto.Field(
        proto.STRING,
        number=4,
    )
    event: str = proto.Field(
        proto.STRING,
        number=5,
    )
    match_confidence: float = proto.Field(
        proto.FLOAT,
        number=9,
    )
    parameters: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=10,
        message=struct_pb2.Struct,
    )
    automated_agent_reply_type: AutomatedAgentReplyType = proto.Field(
        proto.ENUM,
        number=7,
        enum=AutomatedAgentReplyType,
    )
    allow_cancellation: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    cx_current_page: str = proto.Field(
        proto.STRING,
        number=11,
    )
    call_companion_auth_code: bytes = proto.Field(
        proto.BYTES,
        number=12,
    )


class ArticleAnswer(proto.Message):
    r"""Represents article answer.

    Attributes:
        title (str):
            The article title.
        uri (str):
            The article URI.
        snippets (MutableSequence[str]):
            Article snippets.
        confidence (float):
            Article match confidence.
            The system's confidence score that this article
            is a good match for this conversation, as a
            value from 0.0 (completely uncertain) to 1.0
            (completely certain).
        metadata (MutableMapping[str, str]):
            A map that contains metadata about the answer
            and the document from which it originates.
        answer_record (str):
            The name of answer record, in the format of
            "projects/<Project ID>/locations/<Location
            ID>/answerRecords/<Answer Record ID>".
    """

    title: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    snippets: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    confidence: float = proto.Field(
        proto.FLOAT,
        number=4,
    )
    metadata: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    answer_record: str = proto.Field(
        proto.STRING,
        number=6,
    )


class FaqAnswer(proto.Message):
    r"""Represents answer from "frequently asked questions".

    Attributes:
        answer (str):
            The piece of text from the ``source`` knowledge base
            document.
        confidence (float):
            The system's confidence score that this
            Knowledge answer is a good match for this
            conversational query, range from 0.0 (completely
            uncertain) to 1.0 (completely certain).
        question (str):
            The corresponding FAQ question.
        source (str):
            Indicates which Knowledge Document this answer was extracted
            from. Format:
            ``projects/<Project ID>/locations/<Location ID>/agent/knowledgeBases/<Knowledge Base ID>/documents/<Document ID>``.
        metadata (MutableMapping[str, str]):
            A map that contains metadata about the answer
            and the document from which it originates.
        answer_record (str):
            The name of answer record, in the format of
            "projects/<Project ID>/locations/<Location
            ID>/answerRecords/<Answer Record ID>".
    """

    answer: str = proto.Field(
        proto.STRING,
        number=1,
    )
    confidence: float = proto.Field(
        proto.FLOAT,
        number=2,
    )
    question: str = proto.Field(
        proto.STRING,
        number=3,
    )
    source: str = proto.Field(
        proto.STRING,
        number=4,
    )
    metadata: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    answer_record: str = proto.Field(
        proto.STRING,
        number=6,
    )


class SmartReplyAnswer(proto.Message):
    r"""Represents a smart reply answer.

    Attributes:
        reply (str):
            The content of the reply.
        confidence (float):
            Smart reply confidence.
            The system's confidence score that this reply is
            a good match for this conversation, as a value
            from 0.0 (completely uncertain) to 1.0
            (completely certain).
        answer_record (str):
            The name of answer record, in the format of
            "projects/<Project ID>/locations/<Location
            ID>/answerRecords/<Answer Record ID>".
    """

    reply: str = proto.Field(
        proto.STRING,
        number=1,
    )
    confidence: float = proto.Field(
        proto.FLOAT,
        number=2,
    )
    answer_record: str = proto.Field(
        proto.STRING,
        number=3,
    )


class IntentSuggestion(proto.Message):
    r"""Represents an intent suggestion.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        display_name (str):
            The display name of the intent.
        intent_v2 (str):
            The unique identifier of this
            [intent][google.cloud.dialogflow.v2.Intent]. Format:
            ``projects/<Project ID>/locations/<Location ID>/agent/intents/<Intent ID>``.

            This field is a member of `oneof`_ ``intent``.
        description (str):
            Human readable description for better
            understanding an intent like its scope, content,
            result etc. Maximum character limit: 140
            characters.
    """

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    intent_v2: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="intent",
    )
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )


class DialogflowAssistAnswer(proto.Message):
    r"""Represents a Dialogflow assist answer.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        query_result (google.cloud.dialogflow_v2.types.QueryResult):
            Result from v2 agent.

            This field is a member of `oneof`_ ``result``.
        intent_suggestion (google.cloud.dialogflow_v2.types.IntentSuggestion):
            An intent suggestion generated from
            conversation.

            This field is a member of `oneof`_ ``result``.
        answer_record (str):
            The name of answer record, in the format of
            "projects/<Project ID>/locations/<Location
            ID>/answerRecords/<Answer Record ID>".
    """

    query_result: session.QueryResult = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="result",
        message=session.QueryResult,
    )
    intent_suggestion: "IntentSuggestion" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="result",
        message="IntentSuggestion",
    )
    answer_record: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SuggestionResult(proto.Message):
    r"""One response of different type of suggestion response which is used
    in the response of
    [Participants.AnalyzeContent][google.cloud.dialogflow.v2.Participants.AnalyzeContent]
    and
    [Participants.AnalyzeContent][google.cloud.dialogflow.v2.Participants.AnalyzeContent],
    as well as
    [HumanAgentAssistantEvent][google.cloud.dialogflow.v2.HumanAgentAssistantEvent].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        error (google.rpc.status_pb2.Status):
            Error status if the request failed.

            This field is a member of `oneof`_ ``suggestion_response``.
        suggest_articles_response (google.cloud.dialogflow_v2.types.SuggestArticlesResponse):
            SuggestArticlesResponse if request is for
            ARTICLE_SUGGESTION.

            This field is a member of `oneof`_ ``suggestion_response``.
        suggest_knowledge_assist_response (google.cloud.dialogflow_v2.types.SuggestKnowledgeAssistResponse):
            SuggestKnowledgeAssistResponse if request is for
            KNOWLEDGE_ASSIST.

            This field is a member of `oneof`_ ``suggestion_response``.
        suggest_faq_answers_response (google.cloud.dialogflow_v2.types.SuggestFaqAnswersResponse):
            SuggestFaqAnswersResponse if request is for FAQ_ANSWER.

            This field is a member of `oneof`_ ``suggestion_response``.
        suggest_smart_replies_response (google.cloud.dialogflow_v2.types.SuggestSmartRepliesResponse):
            SuggestSmartRepliesResponse if request is for SMART_REPLY.

            This field is a member of `oneof`_ ``suggestion_response``.
        generate_suggestions_response (google.cloud.dialogflow_v2.types.GenerateSuggestionsResponse):
            Suggestions generated using generators
            triggered by customer or agent messages.

            This field is a member of `oneof`_ ``suggestion_response``.
        generate_companion_suggestions_response (google.cloud.dialogflow_v2.types.GenerateCompanionSuggestionsResponse):
            Suggestions generated by companion agent.

            This field is a member of `oneof`_ ``suggestion_response``.
    """

    error: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="suggestion_response",
        message=status_pb2.Status,
    )
    suggest_articles_response: "SuggestArticlesResponse" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="suggestion_response",
        message="SuggestArticlesResponse",
    )
    suggest_knowledge_assist_response: "SuggestKnowledgeAssistResponse" = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="suggestion_response",
        message="SuggestKnowledgeAssistResponse",
    )
    suggest_faq_answers_response: "SuggestFaqAnswersResponse" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="suggestion_response",
        message="SuggestFaqAnswersResponse",
    )
    suggest_smart_replies_response: "SuggestSmartRepliesResponse" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="suggestion_response",
        message="SuggestSmartRepliesResponse",
    )
    generate_suggestions_response: "GenerateSuggestionsResponse" = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="suggestion_response",
        message="GenerateSuggestionsResponse",
    )
    generate_companion_suggestions_response: "GenerateCompanionSuggestionsResponse" = (
        proto.Field(
            proto.MESSAGE,
            number=10,
            oneof="suggestion_response",
            message="GenerateCompanionSuggestionsResponse",
        )
    )


class InputTextConfig(proto.Message):
    r"""Defines the language used in the input text.

    Attributes:
        language_code (str):
            Required. The language of this conversational query. See
            `Language
            Support <https://cloud.google.com/dialogflow/docs/reference/language>`__
            for a list of the currently supported language codes.
    """

    language_code: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AnnotatedMessagePart(proto.Message):
    r"""Represents a part of a message possibly annotated with an
    entity. The part can be an entity or purely a part of the
    message between two entities or message start/end.

    Attributes:
        text (str):
            A part of a message possibly annotated with
            an entity.
        entity_type (str):
            The `Dialogflow system entity
            type <https://cloud.google.com/dialogflow/docs/reference/system-entities>`__
            of this message part. If this is empty, Dialogflow could not
            annotate the phrase part with a system entity.
        formatted_value (google.protobuf.struct_pb2.Value):
            The `Dialogflow system entity formatted
            value <https://cloud.google.com/dialogflow/docs/reference/system-entities>`__
            of this message part. For example for a system entity of
            type ``@sys.unit-currency``, this may contain:

            .. raw:: html

                <pre>
                {
                  "amount": 5,
                  "currency": "USD"
                }
                </pre>
    """

    text: str = proto.Field(
        proto.STRING,
        number=1,
    )
    entity_type: str = proto.Field(
        proto.STRING,
        number=2,
    )
    formatted_value: struct_pb2.Value = proto.Field(
        proto.MESSAGE,
        number=3,
        message=struct_pb2.Value,
    )


class MessageAnnotation(proto.Message):
    r"""Represents the result of annotation for the message.

    Attributes:
        parts (MutableSequence[google.cloud.dialogflow_v2.types.AnnotatedMessagePart]):
            The collection of annotated message parts ordered by their
            position in the message. You can recover the annotated
            message by concatenating [AnnotatedMessagePart.text].
        contain_entities (bool):
            Indicates whether the text message contains
            entities.
    """

    parts: MutableSequence["AnnotatedMessagePart"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AnnotatedMessagePart",
    )
    contain_entities: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class SuggestionInput(proto.Message):
    r"""Represents the action to take for a tool call that requires
    confirmation.

    Attributes:
        answer_record (str):
            Required. Format:
            ``projects/<Project ID>/locations/<Location ID>/answerRecords/<Answer Record ID>``
            The answer record associated with the tool call.
        parameters (google.protobuf.struct_pb2.Struct):
            Optional. Parameters to be used for the tool
            call.  If not provided, the tool will be called
            without any parameters.
        action (google.cloud.dialogflow_v2.types.SuggestionInput.Action):
            Optional. The type of action to take with the
            tool.
        send_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. Time when the current suggest input
            is sent. For tool calls, this timestamp (along
            with the answer record) will be included in the
            corresponding tool call result so that it can be
            identified.
    """

    class Action(proto.Enum):
        r"""Indicate what type of action to take with the tool call.

        Values:
            ACTION_UNSPECIFIED (0):
                Action not specified.
            CANCEL (1):
                Indicates the user chooses to not make the
                tool call. It is only applicable to tool calls
                that are waiting for user confirmation.
            REVISE (2):
                Makes the tool call with provided parameters.
                This action is intended for tool calls that only
                read but not write data.
            CONFIRM (3):
                Makes the tool call with provided parameters.
                This action is intended for tool calls that may
                write data.
        """

        ACTION_UNSPECIFIED = 0
        CANCEL = 1
        REVISE = 2
        CONFIRM = 3

    answer_record: str = proto.Field(
        proto.STRING,
        number=1,
    )
    parameters: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=4,
        message=struct_pb2.Struct,
    )
    action: Action = proto.Field(
        proto.ENUM,
        number=5,
        enum=Action,
    )
    send_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )


class AssistQueryParameters(proto.Message):
    r"""Represents the parameters of human assist query.

    Attributes:
        documents_metadata_filters (MutableMapping[str, str]):
            Key-value filters on the metadata of documents returned by
            article suggestion. If specified, article suggestion only
            returns suggested documents that match all filters in their
            [Document.metadata][google.cloud.dialogflow.v2.Document.metadata].
            Multiple values for a metadata key should be concatenated by
            comma. For example, filters to match all documents that have
            'US' or 'CA' in their market metadata values and 'agent' in
            their user metadata values will be

            ::

               documents_metadata_filters {
                 key: "market"
                 value: "US,CA"
               }
               documents_metadata_filters {
                 key: "user"
                 value: "agent"
               }
    """

    documents_metadata_filters: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=1,
    )


class ResponseMessage(proto.Message):
    r"""Response messages from an automated agent.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        text (google.cloud.dialogflow_v2.types.ResponseMessage.Text):
            Returns a text response.

            This field is a member of `oneof`_ ``message``.
        payload (google.protobuf.struct_pb2.Struct):
            Returns a response containing a custom,
            platform-specific payload.

            This field is a member of `oneof`_ ``message``.
        live_agent_handoff (google.cloud.dialogflow_v2.types.ResponseMessage.LiveAgentHandoff):
            Hands off conversation to a live agent.

            This field is a member of `oneof`_ ``message``.
        end_interaction (google.cloud.dialogflow_v2.types.ResponseMessage.EndInteraction):
            A signal that indicates the interaction with
            the Dialogflow agent has ended.

            This field is a member of `oneof`_ ``message``.
        mixed_audio (google.cloud.dialogflow_v2.types.ResponseMessage.MixedAudio):
            An audio response message composed of both
            the synthesized Dialogflow agent responses and
            the audios hosted in places known to the client.

            This field is a member of `oneof`_ ``message``.
        telephony_transfer_call (google.cloud.dialogflow_v2.types.ResponseMessage.TelephonyTransferCall):
            A signal that the client should transfer the
            phone call connected to this agent to a
            third-party endpoint.

            This field is a member of `oneof`_ ``message``.
    """

    class Text(proto.Message):
        r"""The text response message.

        Attributes:
            text (MutableSequence[str]):
                A collection of text response variants. If
                multiple variants are defined, only one text
                response variant is returned at runtime.
        """

        text: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )

    class LiveAgentHandoff(proto.Message):
        r"""Indicates that the conversation should be handed off to a human
        agent.

        Dialogflow only uses this to determine which conversations were
        handed off to a human agent for measurement purposes. What else to
        do with this signal is up to you and your handoff procedures.

        You may set this, for example:

        - In the entry fulfillment of a CX Page if entering the page
          indicates something went extremely wrong in the conversation.
        - In a webhook response when you determine that the customer issue
          can only be handled by a human.

        Attributes:
            metadata (google.protobuf.struct_pb2.Struct):
                Custom metadata for your handoff procedure.
                Dialogflow doesn't impose any structure on this.
        """

        metadata: struct_pb2.Struct = proto.Field(
            proto.MESSAGE,
            number=1,
            message=struct_pb2.Struct,
        )

    class EndInteraction(proto.Message):
        r"""Indicates that interaction with the Dialogflow agent has
        ended.

        """

    class MixedAudio(proto.Message):
        r"""Represents an audio message that is composed of both segments
        synthesized from the Dialogflow agent prompts and ones hosted
        externally at the specified URIs.

        Attributes:
            segments (MutableSequence[google.cloud.dialogflow_v2.types.ResponseMessage.MixedAudio.Segment]):
                Segments this audio response is composed of.
        """

        class Segment(proto.Message):
            r"""Represents one segment of audio.

            This message has `oneof`_ fields (mutually exclusive fields).
            For each oneof, at most one member field can be set at the same time.
            Setting any member of the oneof automatically clears all other
            members.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                audio (bytes):
                    Raw audio synthesized from the Dialogflow
                    agent's response using the output config
                    specified in the request.

                    This field is a member of `oneof`_ ``content``.
                uri (str):
                    Client-specific URI that points to an audio
                    clip accessible to the client.

                    This field is a member of `oneof`_ ``content``.
                allow_playback_interruption (bool):
                    Whether the playback of this segment can be
                    interrupted by the end user's speech and the
                    client should then start the next Dialogflow
                    request.
            """

            audio: bytes = proto.Field(
                proto.BYTES,
                number=1,
                oneof="content",
            )
            uri: str = proto.Field(
                proto.STRING,
                number=2,
                oneof="content",
            )
            allow_playback_interruption: bool = proto.Field(
                proto.BOOL,
                number=3,
            )

        segments: MutableSequence["ResponseMessage.MixedAudio.Segment"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=1,
                message="ResponseMessage.MixedAudio.Segment",
            )
        )

    class TelephonyTransferCall(proto.Message):
        r"""Represents the signal that telles the client to transfer the
        phone call connected to the agent to a third-party endpoint.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            phone_number (str):
                Transfer the call to a phone number in `E.164
                format <https://en.wikipedia.org/wiki/E.164>`__.

                This field is a member of `oneof`_ ``endpoint``.
            sip_uri (str):
                Transfer the call to a SIP endpoint.

                This field is a member of `oneof`_ ``endpoint``.
        """

        phone_number: str = proto.Field(
            proto.STRING,
            number=1,
            oneof="endpoint",
        )
        sip_uri: str = proto.Field(
            proto.STRING,
            number=2,
            oneof="endpoint",
        )

    text: Text = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="message",
        message=Text,
    )
    payload: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="message",
        message=struct_pb2.Struct,
    )
    live_agent_handoff: LiveAgentHandoff = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="message",
        message=LiveAgentHandoff,
    )
    end_interaction: EndInteraction = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="message",
        message=EndInteraction,
    )
    mixed_audio: MixedAudio = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="message",
        message=MixedAudio,
    )
    telephony_transfer_call: TelephonyTransferCall = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="message",
        message=TelephonyTransferCall,
    )


class SuggestKnowledgeAssistRequest(proto.Message):
    r"""The request message for
    [Participants.SuggestKnowledgeAssist][google.cloud.dialogflow.v2.Participants.SuggestKnowledgeAssist].

    Attributes:
        parent (str):
            Required. The name of the participant to fetch suggestions
            for. Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>``.
        latest_message (str):
            Optional. The name of the latest conversation message to
            compile suggestions for. If empty, it will be the latest
            message of the conversation. Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/messages/<Message ID>``.
        context_size (int):
            Optional. Max number of messages prior to and including
            [latest_message][google.cloud.dialogflow.v2.SuggestKnowledgeAssistRequest.latest_message]
            to use as context when compiling the suggestion. The context
            size is by default 100 and at most 100.
        previous_suggested_query (str):
            Optional. The previously suggested query for
            the given conversation. This helps identify
            whether the next suggestion we generate is
            reasonably different from the previous one. This
            is useful to avoid similar suggestions within
            the conversation.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    latest_message: str = proto.Field(
        proto.STRING,
        number=2,
    )
    context_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    previous_suggested_query: str = proto.Field(
        proto.STRING,
        number=4,
    )


class SuggestKnowledgeAssistResponse(proto.Message):
    r"""The response message for
    [Participants.SuggestKnowledgeAssist][google.cloud.dialogflow.v2.Participants.SuggestKnowledgeAssist].

    Attributes:
        knowledge_assist_answer (google.cloud.dialogflow_v2.types.KnowledgeAssistAnswer):
            Output only. Knowledge Assist suggestion.
        latest_message (str):
            The name of the latest conversation message used to compile
            suggestion for. Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/messages/<Message ID>``.
        context_size (int):
            Number of messages prior to and including
            [latest_message][google.cloud.dialogflow.v2.SuggestKnowledgeAssistResponse.latest_message]
            to compile the suggestion. It may be smaller than the
            [SuggestKnowledgeAssistRequest.context_size][google.cloud.dialogflow.v2.SuggestKnowledgeAssistRequest.context_size]
            field in the request if there are fewer messages in the
            conversation.
        additional_suggested_query_results (MutableSequence[google.cloud.dialogflow_v2.types.KnowledgeAssistAnswer.AdditionalSuggestedQueryResult]):
            Optional. The list of additional suggested
            queries based on the context. This is used for
            the cases when we want to generate multiple
            queries for a single request.
    """

    knowledge_assist_answer: "KnowledgeAssistAnswer" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="KnowledgeAssistAnswer",
    )
    latest_message: str = proto.Field(
        proto.STRING,
        number=2,
    )
    context_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    additional_suggested_query_results: MutableSequence[
        "KnowledgeAssistAnswer.AdditionalSuggestedQueryResult"
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="KnowledgeAssistAnswer.AdditionalSuggestedQueryResult",
    )


class IngestedContextReferenceDebugInfo(proto.Message):
    r"""Debug information related to ingested context reference.

    Attributes:
        project_not_allowlisted (bool):
            Indicates if the project is allowlisted to
            use ingested context reference.
        context_reference_retrieved (bool):
            The status of context_reference retrieval from database.
        ingested_parameters_debug_info (MutableSequence[google.cloud.dialogflow_v2.types.IngestedContextReferenceDebugInfo.IngestedParameterDebugInfo]):
            Parameters ingested from the context
            reference.
    """

    class IngestedParameterDebugInfo(proto.Message):
        r"""Debug information related to ingested parameters from context
        reference.

        Attributes:
            parameter (str):
                The name of the parameter in the context
                reference.
            ingestion_status (google.cloud.dialogflow_v2.types.IngestedContextReferenceDebugInfo.IngestedParameterDebugInfo.IngestionStatus):
                The ingestion status for this specific
                parameter.
        """

        class IngestionStatus(proto.Enum):
            r"""Enum representing the various states of parameter ingestion.

            Values:
                INGESTION_STATUS_UNSPECIFIED (0):
                    Default value, indicates that the ingestion
                    status is not specified.
                INGESTION_STATUS_SUCCEEDED (1):
                    Indicates that the parameter was successfully
                    ingested.
                INGESTION_STATUS_CONTEXT_NOT_AVAILABLE (2):
                    Indicates that the parameter was not
                    available for ingestion.
                INGESTION_STATUS_PARSE_FAILED (3):
                    Indicates that there was a failure parsing
                    the parameter content.
                INGESTION_STATUS_INVALID_ENTRY (4):
                    Indicates that the context reference had an
                    unexpected number of content entries as Context
                    reference should only have one entry.
                INGESTION_STATUS_INVALID_FORMAT (5):
                    Indicates that the context reference content
                    was not in the expected format (e.g., JSON).
                INGESTION_STATUS_LANGUAGE_MISMATCH (6):
                    Indicates that the context reference language
                    does not match the conversation language.
            """

            INGESTION_STATUS_UNSPECIFIED = 0
            INGESTION_STATUS_SUCCEEDED = 1
            INGESTION_STATUS_CONTEXT_NOT_AVAILABLE = 2
            INGESTION_STATUS_PARSE_FAILED = 3
            INGESTION_STATUS_INVALID_ENTRY = 4
            INGESTION_STATUS_INVALID_FORMAT = 5
            INGESTION_STATUS_LANGUAGE_MISMATCH = 6

        parameter: str = proto.Field(
            proto.STRING,
            number=1,
        )
        ingestion_status: "IngestedContextReferenceDebugInfo.IngestedParameterDebugInfo.IngestionStatus" = proto.Field(
            proto.ENUM,
            number=2,
            enum="IngestedContextReferenceDebugInfo.IngestedParameterDebugInfo.IngestionStatus",
        )

    project_not_allowlisted: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    context_reference_retrieved: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    ingested_parameters_debug_info: MutableSequence[IngestedParameterDebugInfo] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message=IngestedParameterDebugInfo,
        )
    )


class ServiceLatency(proto.Message):
    r"""Message to represent the latency of the service.

    Attributes:
        internal_service_latencies (MutableSequence[google.cloud.dialogflow_v2.types.ServiceLatency.InternalServiceLatency]):
            A list of internal service latencies.
    """

    class InternalServiceLatency(proto.Message):
        r"""Message to represent the latency of an internal service.

        Attributes:
            step (str):
                The name of the internal service.
            latency_ms (float):
                The latency of the internal service in
                milliseconds.
            start_time (google.protobuf.timestamp_pb2.Timestamp):
                The start time of the internal service.
            complete_time (google.protobuf.timestamp_pb2.Timestamp):
                The completion time of the internal service.
        """

        step: str = proto.Field(
            proto.STRING,
            number=1,
        )
        latency_ms: float = proto.Field(
            proto.FLOAT,
            number=2,
        )
        start_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=3,
            message=timestamp_pb2.Timestamp,
        )
        complete_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=4,
            message=timestamp_pb2.Timestamp,
        )

    internal_service_latencies: MutableSequence[InternalServiceLatency] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=InternalServiceLatency,
        )
    )


class KnowledgeAssistDebugInfo(proto.Message):
    r"""Debug information related to Knowledge Assist feature.

    Attributes:
        query_generation_failure_reason (google.cloud.dialogflow_v2.types.KnowledgeAssistDebugInfo.QueryGenerationFailureReason):
            Reason for query generation.
        query_categorization_failure_reason (google.cloud.dialogflow_v2.types.KnowledgeAssistDebugInfo.QueryCategorizationFailureReason):
            Reason for query categorization.
        datastore_response_reason (google.cloud.dialogflow_v2.types.DatastoreResponseReason):
            Response reason from datastore which
            indicates data serving status or answer quality
            degradation.
        knowledge_assist_behavior (google.cloud.dialogflow_v2.types.KnowledgeAssistDebugInfo.KnowledgeAssistBehavior):
            Configured behaviors for Knowedge Assist.
        ingested_context_reference_debug_info (google.cloud.dialogflow_v2.types.IngestedContextReferenceDebugInfo):
            Information about parameters ingested for
            search knowledge.
        service_latency (google.cloud.dialogflow_v2.types.ServiceLatency):
            The latency of the service.
        query_generation_debug_info (google.cloud.dialogflow_v2.types.KnowledgeAssistDebugInfo.QueryGenerationDebugInfo):
            Debug information and model metadata for
            query generation.
        ces_debug_info (google.protobuf.struct_pb2.Struct):
            Debug information from CES runtime API.
    """

    class QueryGenerationFailureReason(proto.Enum):
        r"""Reason for query generation failure.

        Values:
            QUERY_GENERATION_FAILURE_REASON_UNSPECIFIED (0):
                Default value.
            QUERY_GENERATION_OUT_OF_QUOTA (1):
                Query generation is blocked due to out of
                quota.
            QUERY_GENERATION_FAILED (2):
                Call to Knowedge Assist query generation
                model fails.
            QUERY_GENERATION_NO_QUERY_GENERATED (3):
                Query generation model decides that there is
                no new topic change or there has been similar
                queries generated in the previous turns.
            QUERY_GENERATION_RAI_FAILED (4):
                Knowedge Assist generated query is blocked by
                RAI (Responsible AI).
            NOT_IN_ALLOWLIST (5):
                Query generation is blocked by Knowledge
                Assist conversation profile level / agent id
                level filtering.
            QUERY_GENERATION_QUERY_REDACTED (6):
                The generated query is blocked due to
                redaction.
            QUERY_GENERATION_LLM_RESPONSE_PARSE_FAILED (10):
                Query generation failed due to LLM response
                parse failure.
            QUERY_GENERATION_EMPTY_CONVERSATION (11):
                The conversation has no messages.
            QUERY_GENERATION_EMPTY_LAST_MESSAGE (12):
                The last message in the conversation is
                empty.
            QUERY_GENERATION_TRIGGERING_EVENT_CONDITION_NOT_MET (13):
                The trigger event condition is not met. This occurs in the
                following scenarios:

                1. The trigger_event is CUSTOMER_MESSAGE or UNSPECIFIED, but
                   the last message is not from the customer.
                2. The trigger_event is AGENT_MESSAGE, but the last message
                   is not from the agent.
        """

        QUERY_GENERATION_FAILURE_REASON_UNSPECIFIED = 0
        QUERY_GENERATION_OUT_OF_QUOTA = 1
        QUERY_GENERATION_FAILED = 2
        QUERY_GENERATION_NO_QUERY_GENERATED = 3
        QUERY_GENERATION_RAI_FAILED = 4
        NOT_IN_ALLOWLIST = 5
        QUERY_GENERATION_QUERY_REDACTED = 6
        QUERY_GENERATION_LLM_RESPONSE_PARSE_FAILED = 10
        QUERY_GENERATION_EMPTY_CONVERSATION = 11
        QUERY_GENERATION_EMPTY_LAST_MESSAGE = 12
        QUERY_GENERATION_TRIGGERING_EVENT_CONDITION_NOT_MET = 13

    class QueryCategorizationFailureReason(proto.Enum):
        r"""Reason for query categorization failure.

        Values:
            QUERY_CATEGORIZATION_FAILURE_REASON_UNSPECIFIED (0):
                Default value.
            QUERY_CATEGORIZATION_INVALID_CONFIG (1):
                Vertex AI Search config supplied for query
                categorization is invalid.
            QUERY_CATEGORIZATION_RESULT_NOT_FOUND (2):
                Vertex AI Search result does not contain a
                query categorization result.
            QUERY_CATEGORIZATION_FAILED (3):
                Vertex AI Search call fails.
        """

        QUERY_CATEGORIZATION_FAILURE_REASON_UNSPECIFIED = 0
        QUERY_CATEGORIZATION_INVALID_CONFIG = 1
        QUERY_CATEGORIZATION_RESULT_NOT_FOUND = 2
        QUERY_CATEGORIZATION_FAILED = 3

    class KnowledgeAssistBehavior(proto.Message):
        r"""Configured behaviors for Knowedge Assist.

        Attributes:
            answer_generation_rewriter_on (bool):
                Whether data store agent rewriter was turned
                off for the request.
            end_user_metadata_included (bool):
                Whether end_user_metadata is included in the data store
                agent call.
            return_query_only (bool):
                Whether customers configured to return query
                only in the conversation profile.
            use_pubsub_delivery (bool):
                Whether customers configured to use pubsub to
                deliver.
            disable_sync_delivery (bool):
                Whether customers configured to disable the
                synchronous delivery of Knowedge Assist
                response.
            previous_queries_included (bool):
                Whether previously suggested queries are
                included in the query generation process.
            use_translated_message (bool):
                Translated message is included in query
                generation process.
            use_custom_safety_filter_level (bool):
                Safety filter is adjusted by user.
            conversation_transcript_has_mixed_languages (bool):
                Conversation transcript has mixed languages.
            query_generation_agent_language_mismatch (bool):
                Whether the agent language from the
                translation generator mismatches the end-user
                language.
            query_generation_end_user_language_mismatch (bool):
                Whether the end-user language from the
                translation generator mismatches the end-user
                language.
            third_party_connector_allowed (bool):
                This field indicates whether third party
                connectors are enabled for the project
            multiple_queries_generated (bool):
                Indicates that the query generation model
                generated multiple queries.
            query_contained_search_context (bool):
                Indicates that the generated query contains
                search context.
            invalid_items_query_suggestion_skipped (bool):
                Indicates that invalid items were skipped
                when parsing the LLM response.
            primary_query_redacted_and_replaced (bool):
                True if the primary suggested query was
                redacted and replaced by an additional query.
            appended_search_context_count (int):
                The number of search contexts appended to the
                query.
        """

        answer_generation_rewriter_on: bool = proto.Field(
            proto.BOOL,
            number=1,
        )
        end_user_metadata_included: bool = proto.Field(
            proto.BOOL,
            number=2,
        )
        return_query_only: bool = proto.Field(
            proto.BOOL,
            number=4,
        )
        use_pubsub_delivery: bool = proto.Field(
            proto.BOOL,
            number=5,
        )
        disable_sync_delivery: bool = proto.Field(
            proto.BOOL,
            number=6,
        )
        previous_queries_included: bool = proto.Field(
            proto.BOOL,
            number=7,
        )
        use_translated_message: bool = proto.Field(
            proto.BOOL,
            number=8,
        )
        use_custom_safety_filter_level: bool = proto.Field(
            proto.BOOL,
            number=9,
        )
        conversation_transcript_has_mixed_languages: bool = proto.Field(
            proto.BOOL,
            number=10,
        )
        query_generation_agent_language_mismatch: bool = proto.Field(
            proto.BOOL,
            number=11,
        )
        query_generation_end_user_language_mismatch: bool = proto.Field(
            proto.BOOL,
            number=12,
        )
        third_party_connector_allowed: bool = proto.Field(
            proto.BOOL,
            number=13,
        )
        multiple_queries_generated: bool = proto.Field(
            proto.BOOL,
            number=14,
        )
        query_contained_search_context: bool = proto.Field(
            proto.BOOL,
            number=15,
        )
        invalid_items_query_suggestion_skipped: bool = proto.Field(
            proto.BOOL,
            number=16,
        )
        primary_query_redacted_and_replaced: bool = proto.Field(
            proto.BOOL,
            number=17,
        )
        appended_search_context_count: int = proto.Field(
            proto.INT32,
            number=18,
        )

    class QueryGenerationDebugInfo(proto.Message):
        r"""Debug information and model metadata for query generation.

        Attributes:
            prompt_token_count (int):
                The total number of tokens in the prompt.
            candidates_token_count (int):
                The total number of tokens in the generated
                candidates.
            total_token_count (int):
                The total number of tokens for the entire
                request.
            thinking_level (str):
                The thinking level configured for the Gemini
                model.
            thinking_budget_tokens (int):
                The thinking budget (in number of tokens)
                configured for the Gemini model.
            similarity_to_last_query (float):
                The similarity score of the suggested query
                to the last suggested query.
            similarity_to_last_query_threshold (float):
                The similarity threshold used to filter out
                queries similar to the last suggestion.
        """

        prompt_token_count: int = proto.Field(
            proto.INT32,
            number=1,
        )
        candidates_token_count: int = proto.Field(
            proto.INT32,
            number=2,
        )
        total_token_count: int = proto.Field(
            proto.INT32,
            number=3,
        )
        thinking_level: str = proto.Field(
            proto.STRING,
            number=4,
        )
        thinking_budget_tokens: int = proto.Field(
            proto.INT32,
            number=5,
        )
        similarity_to_last_query: float = proto.Field(
            proto.FLOAT,
            number=6,
        )
        similarity_to_last_query_threshold: float = proto.Field(
            proto.FLOAT,
            number=7,
        )

    query_generation_failure_reason: QueryGenerationFailureReason = proto.Field(
        proto.ENUM,
        number=1,
        enum=QueryGenerationFailureReason,
    )
    query_categorization_failure_reason: QueryCategorizationFailureReason = proto.Field(
        proto.ENUM,
        number=2,
        enum=QueryCategorizationFailureReason,
    )
    datastore_response_reason: "DatastoreResponseReason" = proto.Field(
        proto.ENUM,
        number=3,
        enum="DatastoreResponseReason",
    )
    knowledge_assist_behavior: KnowledgeAssistBehavior = proto.Field(
        proto.MESSAGE,
        number=4,
        message=KnowledgeAssistBehavior,
    )
    ingested_context_reference_debug_info: "IngestedContextReferenceDebugInfo" = (
        proto.Field(
            proto.MESSAGE,
            number=5,
            message="IngestedContextReferenceDebugInfo",
        )
    )
    service_latency: "ServiceLatency" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="ServiceLatency",
    )
    query_generation_debug_info: QueryGenerationDebugInfo = proto.Field(
        proto.MESSAGE,
        number=7,
        message=QueryGenerationDebugInfo,
    )
    ces_debug_info: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=8,
        message=struct_pb2.Struct,
    )


class KnowledgeAssistAnswer(proto.Message):
    r"""Represents a Knowledge Assist answer.

    Attributes:
        suggested_query (google.cloud.dialogflow_v2.types.KnowledgeAssistAnswer.SuggestedQuery):
            The query suggested based on the context.
            Suggestion is made only if it is different from
            the previous suggestion.
        suggested_query_answer (google.cloud.dialogflow_v2.types.KnowledgeAssistAnswer.KnowledgeAnswer):
            The answer generated for the suggested query.
            Whether or not an answer is generated depends on
            how confident we are about the generated query.
        answer_record (str):
            The name of the answer record. Format:
            ``projects/<Project ID>/locations/<location ID>/answer Records/<Answer Record ID>``.
        knowledge_assist_debug_info (google.cloud.dialogflow_v2.types.KnowledgeAssistDebugInfo):
            Debug information related to Knowledge Assist
            feature.
    """

    class SuggestedQuery(proto.Message):
        r"""Represents a suggested query.

        Attributes:
            query_text (str):
                Suggested query text.
            search_contexts (MutableSequence[google.cloud.dialogflow_v2.types.KnowledgeAssistAnswer.SuggestedQuery.SearchContext]):
                Optional. The search contexts for the query.
        """

        class SearchContext(proto.Message):
            r"""Search context is information useful for knowledge search that helps
            enrich the query. Example: search_context { key: "application name"
            value: "DesignApp" }

            Attributes:
                key (str):
                    Optional. The key of the search context, e.g.
                    "application name".
                value (str):
                    Optional. The value of the search context,
                    e.g. "DesignApp".
            """

            key: str = proto.Field(
                proto.STRING,
                number=1,
            )
            value: str = proto.Field(
                proto.STRING,
                number=2,
            )

        query_text: str = proto.Field(
            proto.STRING,
            number=1,
        )
        search_contexts: MutableSequence[
            "KnowledgeAssistAnswer.SuggestedQuery.SearchContext"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message="KnowledgeAssistAnswer.SuggestedQuery.SearchContext",
        )

    class AdditionalSuggestedQueryResult(proto.Message):
        r"""Represents a single suggested query result.

        Attributes:
            suggested_query (google.cloud.dialogflow_v2.types.KnowledgeAssistAnswer.SuggestedQuery):
                Output only. The suggested query based on the
                context.
            answer_record (str):
                Output only. The name of the answer record. Format:
                ``projects/<Project ID>/locations/<Location ID>/answerRecords/<Answer Record ID>``
        """

        suggested_query: "KnowledgeAssistAnswer.SuggestedQuery" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="KnowledgeAssistAnswer.SuggestedQuery",
        )
        answer_record: str = proto.Field(
            proto.STRING,
            number=5,
        )

    class KnowledgeAnswer(proto.Message):
        r"""Represents an answer from Knowledge. Currently supports FAQ
        and Generative answers.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            answer_text (str):
                The piece of text from the ``source`` that answers this
                suggested query.
            faq_source (google.cloud.dialogflow_v2.types.KnowledgeAssistAnswer.KnowledgeAnswer.FaqSource):
                Populated if the prediction came from FAQ.

                This field is a member of `oneof`_ ``source``.
            generative_source (google.cloud.dialogflow_v2.types.KnowledgeAssistAnswer.KnowledgeAnswer.GenerativeSource):
                Populated if the prediction was Generative.

                This field is a member of `oneof`_ ``source``.
            playbook_source (google.cloud.dialogflow_v2.types.KnowledgeAssistAnswer.KnowledgeAnswer.GenerativeSource):
                Populated if the prediction was from
                Playbook.

                This field is a member of `oneof`_ ``source``.
            event_source (google.cloud.dialogflow_v2.types.KnowledgeAssistAnswer.KnowledgeAnswer.EventSource):
                Populated if the prediction was from an
                event.

                This field is a member of `oneof`_ ``source``.
        """

        class FaqSource(proto.Message):
            r"""Details about source of FAQ answer.

            Attributes:
                question (str):
                    The corresponding FAQ question.
            """

            question: str = proto.Field(
                proto.STRING,
                number=2,
            )

        class GenerativeSource(proto.Message):
            r"""Details about source of Generative answer.

            Attributes:
                snippets (MutableSequence[google.cloud.dialogflow_v2.types.KnowledgeAssistAnswer.KnowledgeAnswer.GenerativeSource.Snippet]):
                    All snippets used for this Generative
                    Prediction, with their source URI and data.
            """

            class Snippet(proto.Message):
                r"""Snippet Source for a Generative Prediction.

                Attributes:
                    uri (str):
                        URI the data is sourced from.
                    text (str):
                        Text taken from that URI.
                    title (str):
                        Title of the document.
                    metadata (google.protobuf.struct_pb2.Struct):
                        Metadata of the document.
                """

                uri: str = proto.Field(
                    proto.STRING,
                    number=2,
                )
                text: str = proto.Field(
                    proto.STRING,
                    number=3,
                )
                title: str = proto.Field(
                    proto.STRING,
                    number=4,
                )
                metadata: struct_pb2.Struct = proto.Field(
                    proto.MESSAGE,
                    number=5,
                    message=struct_pb2.Struct,
                )

            snippets: MutableSequence[
                "KnowledgeAssistAnswer.KnowledgeAnswer.GenerativeSource.Snippet"
            ] = proto.RepeatedField(
                proto.MESSAGE,
                number=1,
                message="KnowledgeAssistAnswer.KnowledgeAnswer.GenerativeSource.Snippet",
            )

        class EventSource(proto.Message):
            r"""Details about source of Event answer.

            Attributes:
                event (str):
                    Name of the triggered event.
                snippets (google.cloud.dialogflow_v2.types.KnowledgeAssistAnswer.KnowledgeAnswer.GenerativeSource):
                    Sources used in event fulfillment.
            """

            event: str = proto.Field(
                proto.STRING,
                number=1,
            )
            snippets: "KnowledgeAssistAnswer.KnowledgeAnswer.GenerativeSource" = (
                proto.Field(
                    proto.MESSAGE,
                    number=2,
                    message="KnowledgeAssistAnswer.KnowledgeAnswer.GenerativeSource",
                )
            )

        answer_text: str = proto.Field(
            proto.STRING,
            number=1,
        )
        faq_source: "KnowledgeAssistAnswer.KnowledgeAnswer.FaqSource" = proto.Field(
            proto.MESSAGE,
            number=3,
            oneof="source",
            message="KnowledgeAssistAnswer.KnowledgeAnswer.FaqSource",
        )
        generative_source: "KnowledgeAssistAnswer.KnowledgeAnswer.GenerativeSource" = (
            proto.Field(
                proto.MESSAGE,
                number=4,
                oneof="source",
                message="KnowledgeAssistAnswer.KnowledgeAnswer.GenerativeSource",
            )
        )
        playbook_source: "KnowledgeAssistAnswer.KnowledgeAnswer.GenerativeSource" = (
            proto.Field(
                proto.MESSAGE,
                number=7,
                oneof="source",
                message="KnowledgeAssistAnswer.KnowledgeAnswer.GenerativeSource",
            )
        )
        event_source: "KnowledgeAssistAnswer.KnowledgeAnswer.EventSource" = proto.Field(
            proto.MESSAGE,
            number=8,
            oneof="source",
            message="KnowledgeAssistAnswer.KnowledgeAnswer.EventSource",
        )

    suggested_query: SuggestedQuery = proto.Field(
        proto.MESSAGE,
        number=1,
        message=SuggestedQuery,
    )
    suggested_query_answer: KnowledgeAnswer = proto.Field(
        proto.MESSAGE,
        number=2,
        message=KnowledgeAnswer,
    )
    answer_record: str = proto.Field(
        proto.STRING,
        number=3,
    )
    knowledge_assist_debug_info: "KnowledgeAssistDebugInfo" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="KnowledgeAssistDebugInfo",
    )


class StreamingReactiveCompanionSuggestionsRequest(proto.Message):
    r"""The request message for
    [Participants.StreamingReactiveCompanionSuggestions][google.cloud.dialogflow.v2.Participants.StreamingReactiveCompanionSuggestions].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        participant (str):
            Required. The human-agent participant name. Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>``.
        text_input (str):
            The natural language text to be processed.

            This field is a member of `oneof`_ ``input``.
        cancel_reactive_query (google.cloud.dialogflow_v2.types.CancelQuery):
            Signals to cancel the current ongoing
            reactive query processing.

            This field is a member of `oneof`_ ``input``.
        suggestion_input (google.cloud.dialogflow_v2.types.SuggestionInput):
            An input representing the selection of a
            suggestion.

            This field is a member of `oneof`_ ``input``.
    """

    participant: str = proto.Field(
        proto.STRING,
        number=1,
    )
    text_input: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="input",
    )
    cancel_reactive_query: "CancelQuery" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="input",
        message="CancelQuery",
    )
    suggestion_input: "SuggestionInput" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="input",
        message="SuggestionInput",
    )


class CancelQuery(proto.Message):
    r"""Message to signal cancellation of the current query turn.
    Cancels the currently active interactive query, not any query
    running in the background.

    """


class StreamingReactiveCompanionSuggestionsResponse(proto.Message):
    r"""The response message for
    [Participants.StreamingReactiveCompanionSuggestions][google.cloud.dialogflow.v2.Participants.StreamingReactiveCompanionSuggestions].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        response_chunk (str):
            Streamed response text chunks.

            This field is a member of `oneof`_ ``response``.
        status (google.rpc.status_pb2.Status):
            Status of the response for the current query.
            If set and non-ok, indicates an error occurred
            during processing of the current query, or
            confirms that a requested cancellation has
            successfully completed (status code CANCELLED).

            This field is a member of `oneof`_ ``response``.
        reactive_mode_final_response (google.cloud.dialogflow_v2.types.StreamingReactiveCompanionSuggestionsResponse.ReactiveModeResponse):
            Output only. The final response from the reactive mode
            capturing the entire accumulated streaming response,
            grounding metadata, and tool calls. Only set when
            ``is_final`` is ``true`` and conversational processing for
            the query turn completes.

            This field is a member of `oneof`_ ``response``.
        intermediate_tool_call_events (google.cloud.dialogflow_v2.types.ToolCallEvents):
            Output only. Captures intermediate tool call events that
            occur during the execution of the reactive query turn. Note
            that conversational messages within tool calls are displayed
            within the tool cards and hence are not accumulated within
            the ``reactive_mode_final_response.response`` string.

            This field is a member of `oneof`_ ``response``.
        is_final (bool):
            Output only. Indicates whether the client/UI can accept a
            new query for reactive chat. When ``is_final`` is ``true``,
            the reactive chat interface is unblocked and ready to
            receive new human agent queries. For synchronous turns, this
            is set to ``true`` on the final response chunk. For
            asynchronous tool calls running in the background, this is
            set to ``true`` on the intermediate trigger chunk to unblock
            the UI while the background tool execution is in progress.
        answer_record (str):
            Output only. Only set when ``is_final`` is ``true`` and
            conversational turn processing completes. The final answer
            record representing the completed suggestion. Only present
            in the last chunk of the completed response.
        text_message_id (str):
            Required. The unique message identifier
            corresponding to the human agent query that
            generated this response chunk.
        send_time (google.protobuf.timestamp_pb2.Timestamp):
            The timestamp when the response chunk was
            sent by the service.
    """

    class ReactiveModeResponse(proto.Message):
        r"""The complete response generated by the reactive mode
        capturing the entire accumulated streaming response, grounding
        metadata, and tool calls.

        Attributes:
            response (str):
                Optional. The full reactive suggestion
                generated by the Companion Agent. After the last
                streaming chunk is sent, this is the final
                response concatenating all the streaming
                response chunks together to represent the full
                reactive suggestion.
            grounding_metadata (google.cloud.dialogflow_v2.types.GroundingMetadata):
                Optional. Grounding metadata for the
                generated response.
            tool_calls (MutableSequence[google.cloud.dialogflow_v2.types.ToolCallSuggestion]):
                Optional. Captures all the rich structured
                tool calls and their associated citations used
                by the reactive agent to generate the reactive
                suggestion.
        """

        response: str = proto.Field(
            proto.STRING,
            number=1,
        )
        grounding_metadata: grounding.GroundingMetadata = proto.Field(
            proto.MESSAGE,
            number=2,
            message=grounding.GroundingMetadata,
        )
        tool_calls: MutableSequence["ToolCallSuggestion"] = proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message="ToolCallSuggestion",
        )

    response_chunk: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="response",
    )
    status: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="response",
        message=status_pb2.Status,
    )
    reactive_mode_final_response: ReactiveModeResponse = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="response",
        message=ReactiveModeResponse,
    )
    intermediate_tool_call_events: "ToolCallEvents" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="response",
        message="ToolCallEvents",
    )
    is_final: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    answer_record: str = proto.Field(
        proto.STRING,
        number=5,
    )
    text_message_id: str = proto.Field(
        proto.STRING,
        number=8,
    )
    send_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )


class BidiStreamingAnalyzeContentRequest(proto.Message):
    r"""The request message for
    [Participants.BidiStreamingAnalyzeContent][google.cloud.dialogflow.v2.Participants.BidiStreamingAnalyzeContent].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        config (google.cloud.dialogflow_v2.types.BidiStreamingAnalyzeContentRequest.Config):
            The config message for this conversation.

            This field is a member of `oneof`_ ``request``.
        input (google.cloud.dialogflow_v2.types.BidiStreamingAnalyzeContentRequest.Input):
            Text, audio or other multi-modality inputs.
            This is the second and following messages sent
            by the client.

            This field is a member of `oneof`_ ``request``.
    """

    class Config(proto.Message):
        r"""The config of the session.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            participant (str):
                Required. The name of the participant to fetch response for.
                Format:
                ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>``.
            voice_session_config (google.cloud.dialogflow_v2.types.BidiStreamingAnalyzeContentRequest.Config.VoiceSessionConfig):
                Configure a voice-based session.

                This field is a member of `oneof`_ ``config``.
            initial_virtual_agent_parameters (google.protobuf.struct_pb2.Struct):
                Optional. Parameters to be passed to the
                virtual agent at the beginning.
            initial_virtual_agent_query_params (google.cloud.dialogflow_v2.types.QueryParameters):
                Optional. Initial parameters for the
                virtual-agent.
        """

        class VoiceSessionConfig(proto.Message):
            r"""The config about how to process the audio for a voice-based
            session.


            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                input_audio_encoding (google.cloud.dialogflow_v2.types.AudioEncoding):
                    Required. The encoding of input audio.
                input_audio_sample_rate_hertz (int):
                    Required. The sample rate of input audio.
                output_audio_encoding (google.cloud.dialogflow_v2.types.OutputAudioEncoding):
                    Required. The encoding of output audio.
                output_audio_sample_rate_hertz (int):
                    Required. The sample rate of output audio.
                enable_cx_proactive_processing (bool):
                    Optional. Whether to enable CX proactive
                    processing.
                enable_streaming_synthesize (bool):
                    Optional. If true, Dialogflow will stream the
                    audio bytes from Cloud TTS for speech synthesis
                    using the StreamingSynthesize api.
                gemini_asr_config (google.cloud.dialogflow_v2.types.SpeechToTextConfig.GeminiAsrConfig):
                    Optional. Configuration for using Gemini ASR models served
                    via Vertex AI. This field is only used when
                    ``use_gemini_asr`` is true.
                use_gemini_asr (bool):
                    Optional. If true, Gemini ASR will be used
                    for transcription instead of Cloud
                    Speech-to-Text. If false, Cloud Speech-to-Text
                    will be used. If unset, this setting is
                    inherited from the ConversationProfile.

                    This field is a member of `oneof`_ ``_use_gemini_asr``.
                disable_interim_input_transcripts (bool):
                    Optional. Disables emission of interim input transcriptions
                    when set to ``true``.

                    This field is a member of `oneof`_ ``_disable_interim_input_transcripts``.
            """

            input_audio_encoding: gcd_audio_config.AudioEncoding = proto.Field(
                proto.ENUM,
                number=1,
                enum=gcd_audio_config.AudioEncoding,
            )
            input_audio_sample_rate_hertz: int = proto.Field(
                proto.INT32,
                number=2,
            )
            output_audio_encoding: gcd_audio_config.OutputAudioEncoding = proto.Field(
                proto.ENUM,
                number=3,
                enum=gcd_audio_config.OutputAudioEncoding,
            )
            output_audio_sample_rate_hertz: int = proto.Field(
                proto.INT32,
                number=4,
            )
            enable_cx_proactive_processing: bool = proto.Field(
                proto.BOOL,
                number=5,
            )
            enable_streaming_synthesize: bool = proto.Field(
                proto.BOOL,
                number=23,
            )
            gemini_asr_config: gcd_audio_config.SpeechToTextConfig.GeminiAsrConfig = (
                proto.Field(
                    proto.MESSAGE,
                    number=24,
                    message=gcd_audio_config.SpeechToTextConfig.GeminiAsrConfig,
                )
            )
            use_gemini_asr: bool = proto.Field(
                proto.BOOL,
                number=25,
                optional=True,
            )
            disable_interim_input_transcripts: bool = proto.Field(
                proto.BOOL,
                number=26,
                optional=True,
            )

        participant: str = proto.Field(
            proto.STRING,
            number=1,
        )
        voice_session_config: "BidiStreamingAnalyzeContentRequest.Config.VoiceSessionConfig" = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="config",
            message="BidiStreamingAnalyzeContentRequest.Config.VoiceSessionConfig",
        )
        initial_virtual_agent_parameters: struct_pb2.Struct = proto.Field(
            proto.MESSAGE,
            number=3,
            message=struct_pb2.Struct,
        )
        initial_virtual_agent_query_params: session.QueryParameters = proto.Field(
            proto.MESSAGE,
            number=4,
            message=session.QueryParameters,
        )

    class TurnInput(proto.Message):
        r"""Input that forms data for a single turn.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            text (str):
                The UTF-8 encoded natural language text to be
                processed.

                This field is a member of `oneof`_ ``main_content``.
            intent (str):
                The intent to be triggered on V3 agent. Format:
                ``projects/<Project ID>/locations/<Location ID>/locations/ <Location ID>/agents/<Agent ID>/intents/<Intent ID>``.
                This can only be used to trigger the Welcome intent id if
                the modality is text.

                This field is a member of `oneof`_ ``main_content``.
            event (str):
                The input event name.
                This can only be sent once and would cancel the
                ongoing speech recognition if any. To trigger
                the Welcome intent use the event "WELCOME".

                This field is a member of `oneof`_ ``main_content``.
            suggestion_input (google.cloud.dialogflow_v2.types.SuggestionInput):
                Optional. Input for confirming, revising, or
                canceling a suggestion.

                This field is a member of `oneof`_ ``main_content``.
            virtual_agent_parameters (google.protobuf.struct_pb2.Struct):
                Optional. Parameters to be passed to the
                virtual agent.
        """

        text: str = proto.Field(
            proto.STRING,
            number=1,
            oneof="main_content",
        )
        intent: str = proto.Field(
            proto.STRING,
            number=2,
            oneof="main_content",
        )
        event: str = proto.Field(
            proto.STRING,
            number=3,
            oneof="main_content",
        )
        suggestion_input: "SuggestionInput" = proto.Field(
            proto.MESSAGE,
            number=6,
            oneof="main_content",
            message="SuggestionInput",
        )
        virtual_agent_parameters: struct_pb2.Struct = proto.Field(
            proto.MESSAGE,
            number=4,
            message=struct_pb2.Struct,
        )

    class Input(proto.Message):
        r"""Input for the conversation.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            audio (bytes):
                The content of audio stream to be recognized.

                This field is a member of `oneof`_ ``input``.
            dtmf (google.cloud.dialogflow_v2.types.TelephonyDtmfEvents):
                The DTMF digits used to invoke intent and
                fill in parameter value.
                This input is ignored if the previous response
                indicated that DTMF input is not accepted.

                This field is a member of `oneof`_ ``input``.
            turn (google.cloud.dialogflow_v2.types.BidiStreamingAnalyzeContentRequest.TurnInput):
                Turn input.

                This field is a member of `oneof`_ ``input``.
        """

        audio: bytes = proto.Field(
            proto.BYTES,
            number=1,
            oneof="input",
        )
        dtmf: gcd_audio_config.TelephonyDtmfEvents = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="input",
            message=gcd_audio_config.TelephonyDtmfEvents,
        )
        turn: "BidiStreamingAnalyzeContentRequest.TurnInput" = proto.Field(
            proto.MESSAGE,
            number=3,
            oneof="input",
            message="BidiStreamingAnalyzeContentRequest.TurnInput",
        )

    config: Config = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="request",
        message=Config,
    )
    input: Input = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="request",
        message=Input,
    )


class BidiStreamingAnalyzeContentResponse(proto.Message):
    r"""The response message for
    [Participants.BidiStreamingAnalyzeContent][google.cloud.dialogflow.v2.Participants.BidiStreamingAnalyzeContent].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        recognition_result (google.cloud.dialogflow_v2.types.StreamingRecognitionResult):
            The result of speech recognition.

            This field is a member of `oneof`_ ``response``.
        barge_in_signal (google.cloud.dialogflow_v2.types.BidiStreamingAnalyzeContentResponse.BargeInSignal):
            Indicate the user barge-in has been detected,
            and client should stop playing back the audio.

            This field is a member of `oneof`_ ``response``.
        analyze_content_response (google.cloud.dialogflow_v2.types.AnalyzeContentResponse):
            The agent response from analyze content.

            This field is a member of `oneof`_ ``response``.
        turn_complete (google.cloud.dialogflow_v2.types.BidiStreamingAnalyzeContentResponse.TurnComplete):
            Indicate that the turn is complete.

            This field is a member of `oneof`_ ``response``.
    """

    class BargeInSignal(proto.Message):
        r"""Indicate the user barge-in has been detected."""

    class TurnComplete(proto.Message):
        r"""Indicate that the turn is complete."""

    recognition_result: session.StreamingRecognitionResult = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="response",
        message=session.StreamingRecognitionResult,
    )
    barge_in_signal: BargeInSignal = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="response",
        message=BargeInSignal,
    )
    analyze_content_response: "AnalyzeContentResponse" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="response",
        message="AnalyzeContentResponse",
    )
    turn_complete: TurnComplete = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="response",
        message=TurnComplete,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
