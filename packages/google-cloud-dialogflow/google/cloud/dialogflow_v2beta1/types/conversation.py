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

from google.cloud.dialogflow_v2beta1.types import (
    conversation_profile as gcd_conversation_profile,
)
from google.cloud.dialogflow_v2beta1.types import generator as gcd_generator
from google.cloud.dialogflow_v2beta1.types import participant, session

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.v2beta1",
    manifest={
        "Conversation",
        "ConversationPhoneNumber",
        "CreateConversationRequest",
        "ListConversationsRequest",
        "ListConversationsResponse",
        "GetConversationRequest",
        "CompleteConversationRequest",
        "CreateMessageRequest",
        "BatchCreateMessagesRequest",
        "BatchCreateMessagesResponse",
        "ListMessagesRequest",
        "ListMessagesResponse",
        "IngestContextReferencesRequest",
        "IngestContextReferencesResponse",
        "SuggestConversationSummaryRequest",
        "SuggestConversationSummaryResponse",
        "GenerateStatelessSummaryRequest",
        "GenerateStatelessSummaryResponse",
        "GenerateStatelessSuggestionRequest",
        "GenerateStatelessSuggestionResponse",
        "SearchKnowledgeRequest",
        "SearchKnowledgeDebugInfo",
        "SearchKnowledgeResponse",
        "SearchKnowledgeAnswer",
        "GenerateSuggestionsRequest",
    },
)


class Conversation(proto.Message):
    r"""Represents a conversation.
    A conversation is an interaction between an agent, including
    live agents and Dialogflow agents, and a support customer.
    Conversations can include phone calls and text-based chat
    sessions.

    Attributes:
        name (str):
            Output only. Identifier. The unique identifier of this
            conversation. Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>``.
        lifecycle_state (google.cloud.dialogflow_v2beta1.types.Conversation.LifecycleState):
            Output only. The current state of the
            Conversation.
        conversation_profile (str):
            Required. The Conversation Profile to be used to configure
            this Conversation. This field cannot be updated. Format:
            ``projects/<Project ID>/locations/<Location ID>/conversationProfiles/<Conversation Profile ID>``.
        phone_number (google.cloud.dialogflow_v2beta1.types.ConversationPhoneNumber):
            Output only. Required if the conversation is
            to be connected over telephony.
        conversation_stage (google.cloud.dialogflow_v2beta1.types.Conversation.ConversationStage):
            Optional. The stage of a conversation. It indicates whether
            the virtual agent or a human agent is handling the
            conversation.

            If the conversation is created with the conversation profile
            that has Dialogflow config set, defaults to
            [ConversationStage.VIRTUAL_AGENT_STAGE][google.cloud.dialogflow.v2beta1.Conversation.ConversationStage.VIRTUAL_AGENT_STAGE];
            Otherwise, defaults to
            [ConversationStage.HUMAN_ASSIST_STAGE][google.cloud.dialogflow.v2beta1.Conversation.ConversationStage.HUMAN_ASSIST_STAGE].

            If the conversation is created with the conversation profile
            that has Dialogflow config set but explicitly sets
            conversation_stage to
            [ConversationStage.HUMAN_ASSIST_STAGE][google.cloud.dialogflow.v2beta1.Conversation.ConversationStage.HUMAN_ASSIST_STAGE],
            it skips
            [ConversationStage.VIRTUAL_AGENT_STAGE][google.cloud.dialogflow.v2beta1.Conversation.ConversationStage.VIRTUAL_AGENT_STAGE]
            stage and directly goes to
            [ConversationStage.HUMAN_ASSIST_STAGE][google.cloud.dialogflow.v2beta1.Conversation.ConversationStage.HUMAN_ASSIST_STAGE].
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the conversation was
            started.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the conversation was
            finished.
        telephony_connection_info (google.cloud.dialogflow_v2beta1.types.Conversation.TelephonyConnectionInfo):
            Output only. The telephony connection
            information.
        initial_conversation_profile (google.cloud.dialogflow_v2beta1.types.ConversationProfile):
            Optional. Output only. The initial
            conversation profile to be used to configure
            this conversation, which is a copy of the
            conversation profile config read at conversation
            creation time.
        ingested_context_references (MutableMapping[str, google.cloud.dialogflow_v2beta1.types.Conversation.ContextReference]):
            Output only. The context reference updates
            provided by external systems.
        initial_generator_contexts (MutableMapping[str, google.cloud.dialogflow_v2beta1.types.Conversation.GeneratorContext]):
            Output only. A map with generator name as key
            and generator context as value.
    """

    class LifecycleState(proto.Enum):
        r"""Enumeration of the completion status of the conversation.

        Values:
            LIFECYCLE_STATE_UNSPECIFIED (0):
                Unknown.
            IN_PROGRESS (1):
                Conversation is currently open for media
                analysis.
            COMPLETED (2):
                Conversation has been completed.
        """

        LIFECYCLE_STATE_UNSPECIFIED = 0
        IN_PROGRESS = 1
        COMPLETED = 2

    class ConversationStage(proto.Enum):
        r"""Enumeration of the different conversation stages a conversation can
        be in. Reference:
        https://cloud.google.com/agent-assist/docs/basics#conversation_stages

        Values:
            CONVERSATION_STAGE_UNSPECIFIED (0):
                Unknown. Should never be used after a
                conversation is successfully created.
            VIRTUAL_AGENT_STAGE (1):
                The conversation should return virtual agent
                responses into the conversation.
            HUMAN_ASSIST_STAGE (2):
                The conversation should not provide
                responses, just listen and provide suggestions.
        """

        CONVERSATION_STAGE_UNSPECIFIED = 0
        VIRTUAL_AGENT_STAGE = 1
        HUMAN_ASSIST_STAGE = 2

    class TelephonyConnectionInfo(proto.Message):
        r"""The information about phone calls connected via phone gateway
        to the conversation.

        Attributes:
            dialed_number (str):
                Output only. The number dialed to connect
                this call in E.164 format.
            sdp (str):
                Optional. SDP of the call. It's initially the
                SDP answer to the incoming call, but maybe later
                updated for the purpose of making the link
                active, etc.
            sip_headers (MutableSequence[google.cloud.dialogflow_v2beta1.types.Conversation.TelephonyConnectionInfo.SipHeader]):
                Output only. The SIP headers from the initial
                SIP INVITE.
            extra_mime_contents (MutableSequence[google.cloud.dialogflow_v2beta1.types.Conversation.TelephonyConnectionInfo.MimeContent]):
                Output only. The mime content from the
                initial SIP INVITE.
        """

        class SipHeader(proto.Message):
            r"""The SIP headers from the initial SIP INVITE.

            Attributes:
                name (str):
                    Optional. The name of the header.
                value (str):
                    Optional. The value of the header.
            """

            name: str = proto.Field(
                proto.STRING,
                number=1,
            )
            value: str = proto.Field(
                proto.STRING,
                number=2,
            )

        class MimeContent(proto.Message):
            r"""The mime content from the initial SIP INVITE.

            Attributes:
                mime_type (str):
                    Optional. The mime type of the content.
                content (bytes):
                    Optional. The content payload.
            """

            mime_type: str = proto.Field(
                proto.STRING,
                number=1,
            )
            content: bytes = proto.Field(
                proto.BYTES,
                number=2,
            )

        dialed_number: str = proto.Field(
            proto.STRING,
            number=2,
        )
        sdp: str = proto.Field(
            proto.STRING,
            number=5,
        )
        sip_headers: MutableSequence[
            "Conversation.TelephonyConnectionInfo.SipHeader"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=12,
            message="Conversation.TelephonyConnectionInfo.SipHeader",
        )
        extra_mime_contents: MutableSequence[
            "Conversation.TelephonyConnectionInfo.MimeContent"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=13,
            message="Conversation.TelephonyConnectionInfo.MimeContent",
        )

    class ContextReference(proto.Message):
        r"""Represents a piece of ingested context information.

        Attributes:
            context_contents (MutableSequence[google.cloud.dialogflow_v2beta1.types.Conversation.ContextReference.ContextContent]):
                Required. The list of content updates for a
                context reference.
            update_mode (google.cloud.dialogflow_v2beta1.types.Conversation.ContextReference.UpdateMode):
                Required. The mode in which context reference
                contents are updated.
            language_code (str):
                Optional. The language of the information
                ingested, defaults to "en-US" if not set.
            create_time (google.protobuf.timestamp_pb2.Timestamp):
                Output only. The time the context reference
                was first created.
        """

        class UpdateMode(proto.Enum):
            r"""Represents the mode in which context reference contents are
            updated.

            Values:
                UPDATE_MODE_UNSPECIFIED (0):
                    Unspecified update mode.
                APPEND (1):
                    Context content updates are applied in append
                    mode.
                OVERWRITE (2):
                    Context content updates are applied in
                    overwrite mode.
            """

            UPDATE_MODE_UNSPECIFIED = 0
            APPEND = 1
            OVERWRITE = 2

        class ContextContent(proto.Message):
            r"""Contents ingested.

            Attributes:
                content (str):
                    Required. The information ingested in a
                    single request.
                content_format (google.cloud.dialogflow_v2beta1.types.Conversation.ContextReference.ContextContent.ContentFormat):
                    Required. The format of the ingested string.
                ingestion_time (google.protobuf.timestamp_pb2.Timestamp):
                    Output only. The time when this information
                    was incorporated into the relevant context
                    reference.
                answer_record (str):
                    Optional. The answer record of the tool execution result.
                    Format:
                    ``projects/<Project ID>/locations/<Location ID>/answerRecords/<Answer Record ID>``.
            """

            class ContentFormat(proto.Enum):
                r"""Represents the format of the ingested string.

                Values:
                    CONTENT_FORMAT_UNSPECIFIED (0):
                        Unspecified content format.
                    JSON (1):
                        Content was provided in JSON format.
                    PLAIN_TEXT (2):
                        Content was provided as plain text.
                """

                CONTENT_FORMAT_UNSPECIFIED = 0
                JSON = 1
                PLAIN_TEXT = 2

            content: str = proto.Field(
                proto.STRING,
                number=1,
            )
            content_format: "Conversation.ContextReference.ContextContent.ContentFormat" = proto.Field(
                proto.ENUM,
                number=2,
                enum="Conversation.ContextReference.ContextContent.ContentFormat",
            )
            ingestion_time: timestamp_pb2.Timestamp = proto.Field(
                proto.MESSAGE,
                number=3,
                message=timestamp_pb2.Timestamp,
            )
            answer_record: str = proto.Field(
                proto.STRING,
                number=4,
            )

        context_contents: MutableSequence[
            "Conversation.ContextReference.ContextContent"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="Conversation.ContextReference.ContextContent",
        )
        update_mode: "Conversation.ContextReference.UpdateMode" = proto.Field(
            proto.ENUM,
            number=2,
            enum="Conversation.ContextReference.UpdateMode",
        )
        language_code: str = proto.Field(
            proto.STRING,
            number=3,
        )
        create_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=4,
            message=timestamp_pb2.Timestamp,
        )

    class GeneratorContext(proto.Message):
        r"""Represents the context of a generator.

        Attributes:
            generator_type (google.cloud.dialogflow_v2beta1.types.Conversation.GeneratorContext.GeneratorType):
                Output only. The type of the generator.
        """

        class GeneratorType(proto.Enum):
            r"""The available generator types.

            Values:
                GENERATOR_TYPE_UNSPECIFIED (0):
                    Unspecified generator type.
                FREE_FORM (1):
                    Free form generator type.
                AGENT_COACHING (2):
                    Agent coaching generator type.
                SUMMARIZATION (3):
                    Summarization generator type.
                TRANSLATION (4):
                    Translation generator type.
                AGENT_FEEDBACK (5):
                    Agent feedback generator type.
                CUSTOMER_MESSAGE_GENERATION (6):
                    Customer message generation generator type.
            """

            GENERATOR_TYPE_UNSPECIFIED = 0
            FREE_FORM = 1
            AGENT_COACHING = 2
            SUMMARIZATION = 3
            TRANSLATION = 4
            AGENT_FEEDBACK = 5
            CUSTOMER_MESSAGE_GENERATION = 6

        generator_type: "Conversation.GeneratorContext.GeneratorType" = proto.Field(
            proto.ENUM,
            number=1,
            enum="Conversation.GeneratorContext.GeneratorType",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    lifecycle_state: LifecycleState = proto.Field(
        proto.ENUM,
        number=2,
        enum=LifecycleState,
    )
    conversation_profile: str = proto.Field(
        proto.STRING,
        number=3,
    )
    phone_number: "ConversationPhoneNumber" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="ConversationPhoneNumber",
    )
    conversation_stage: ConversationStage = proto.Field(
        proto.ENUM,
        number=7,
        enum=ConversationStage,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    telephony_connection_info: TelephonyConnectionInfo = proto.Field(
        proto.MESSAGE,
        number=10,
        message=TelephonyConnectionInfo,
    )
    initial_conversation_profile: gcd_conversation_profile.ConversationProfile = (
        proto.Field(
            proto.MESSAGE,
            number=15,
            message=gcd_conversation_profile.ConversationProfile,
        )
    )
    ingested_context_references: MutableMapping[str, ContextReference] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=17,
        message=ContextReference,
    )
    initial_generator_contexts: MutableMapping[str, GeneratorContext] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=18,
        message=GeneratorContext,
    )


class ConversationPhoneNumber(proto.Message):
    r"""Represents a phone number for telephony integration. It
    allows for connecting a particular conversation over telephony.

    Attributes:
        country_code (int):
            Output only. Desired country code for the
            phone number.
        phone_number (str):
            Output only. The phone number to connect to
            this conversation.
    """

    country_code: int = proto.Field(
        proto.INT32,
        number=2,
    )
    phone_number: str = proto.Field(
        proto.STRING,
        number=3,
    )


class CreateConversationRequest(proto.Message):
    r"""The request message for
    [Conversations.CreateConversation][google.cloud.dialogflow.v2beta1.Conversations.CreateConversation].

    Attributes:
        parent (str):
            Required. Resource identifier of the project creating the
            conversation. Format:
            ``projects/<Project ID>/locations/<Location ID>``.
        conversation (google.cloud.dialogflow_v2beta1.types.Conversation):
            Required. The conversation to create.
        conversation_id (str):
            Optional. Identifier of the conversation. Generally it's
            auto generated by Google. Only set it if you cannot wait for
            the response to return a auto-generated one to you.

            The conversation ID must be compliant with the regression
            formula ``[a-zA-Z][a-zA-Z0-9_-]*`` with the characters
            length in range of [3,64]. If the field is provided, the
            caller is responsible for

            1. the uniqueness of the ID, otherwise the request will be
               rejected.
            2. the consistency for whether to use custom ID or not under
               a project to better ensure uniqueness.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    conversation: "Conversation" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Conversation",
    )
    conversation_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListConversationsRequest(proto.Message):
    r"""The request message for
    [Conversations.ListConversations][google.cloud.dialogflow.v2beta1.Conversations.ListConversations].

    Attributes:
        parent (str):
            Required. The project from which to list all conversation.
            Format: ``projects/<Project ID>/locations/<Location ID>``.
        page_size (int):
            Optional. The maximum number of items to
            return in a single page. By default 100 and at
            most 1000.
        page_token (str):
            Optional. The next_page_token value returned from a previous
            list request.
        filter (str):
            Optional. A filter expression that filters conversations
            listed in the response. Only ``lifecycle_state`` can be
            filtered on in this way. For example, the following
            expression only returns ``COMPLETED`` conversations:

            ``lifecycle_state = "COMPLETED"``

            For more information about filtering, see `API
            Filtering <https://aip.dev/160>`__.
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


class ListConversationsResponse(proto.Message):
    r"""The response message for
    [Conversations.ListConversations][google.cloud.dialogflow.v2beta1.Conversations.ListConversations].

    Attributes:
        conversations (MutableSequence[google.cloud.dialogflow_v2beta1.types.Conversation]):
            The list of conversations. There will be a maximum number of
            items returned based on the page_size field in the request.
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


class GetConversationRequest(proto.Message):
    r"""The request message for
    [Conversations.GetConversation][google.cloud.dialogflow.v2beta1.Conversations.GetConversation].

    Attributes:
        name (str):
            Required. The name of the conversation. Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CompleteConversationRequest(proto.Message):
    r"""The request message for
    [Conversations.CompleteConversation][google.cloud.dialogflow.v2beta1.Conversations.CompleteConversation].

    Attributes:
        name (str):
            Required. Resource identifier of the conversation to close.
            Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateMessageRequest(proto.Message):
    r"""The request message to create one Message. Currently it is
    only used in BatchCreateMessagesRequest.

    Attributes:
        parent (str):
            Required. Resource identifier of the conversation to create
            message. Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>``.
        message (google.cloud.dialogflow_v2beta1.types.Message):
            Required. The message to create.
            [Message.participant][google.cloud.dialogflow.v2beta1.Message.participant]
            is required.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    message: participant.Message = proto.Field(
        proto.MESSAGE,
        number=2,
        message=participant.Message,
    )


class BatchCreateMessagesRequest(proto.Message):
    r"""The request message for
    [Conversations.BatchCreateMessagesRequest][].

    Attributes:
        parent (str):
            Required. Resource identifier of the conversation to create
            message. Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>``.
        requests (MutableSequence[google.cloud.dialogflow_v2beta1.types.CreateMessageRequest]):
            Required. A maximum of 300 messages can be created in a
            batch. [CreateMessageRequest.message.send_time][] is
            required. All created messages will have identical
            [Message.create_time][google.cloud.dialogflow.v2beta1.Message.create_time].
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["CreateMessageRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="CreateMessageRequest",
    )


class BatchCreateMessagesResponse(proto.Message):
    r"""The request message for
    [Conversations.BatchCreateMessagesResponse][].

    Attributes:
        messages (MutableSequence[google.cloud.dialogflow_v2beta1.types.Message]):
            Messages created.
    """

    messages: MutableSequence[participant.Message] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=participant.Message,
    )


class ListMessagesRequest(proto.Message):
    r"""The request message for
    [Conversations.ListMessages][google.cloud.dialogflow.v2beta1.Conversations.ListMessages].

    Attributes:
        parent (str):
            Required. The name of the conversation to list messages for.
            Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>``
        filter (str):
            Optional. Filter on message fields. Currently predicates on
            ``create_time`` and ``create_time_epoch_microseconds`` are
            supported. ``create_time`` only support milliseconds
            accuracy. E.g.,
            ``create_time_epoch_microseconds > 1551790877964485`` or
            ``create_time > "2017-01-15T01:30:15.01Z"``.

            For more information about filtering, see `API
            Filtering <https://aip.dev/160>`__.
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
        number=4,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListMessagesResponse(proto.Message):
    r"""The response message for
    [Conversations.ListMessages][google.cloud.dialogflow.v2beta1.Conversations.ListMessages].

    Attributes:
        messages (MutableSequence[google.cloud.dialogflow_v2beta1.types.Message]):
            Required. The list of messages. There will be a maximum
            number of items returned based on the page_size field in the
            request. ``messages`` is sorted by ``create_time`` in
            descending order.
        next_page_token (str):
            Optional. Token to retrieve the next page of
            results, or empty if there are no more results
            in the list.
    """

    @property
    def raw_page(self):
        return self

    messages: MutableSequence[participant.Message] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=participant.Message,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class IngestContextReferencesRequest(proto.Message):
    r"""The request message for
    [ConversationsService.IngestContextReferences][].

    Attributes:
        conversation (str):
            Required. Resource identifier of the conversation to ingest
            context information for. Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>``.
        context_references (MutableMapping[str, google.cloud.dialogflow_v2beta1.types.Conversation.ContextReference]):
            Required. The context references to ingest.
            The key is the name of the context reference and
            the value contains the contents of the context
            reference. The key is used to incorporate
            ingested context references to enhance the
            generator.
    """

    conversation: str = proto.Field(
        proto.STRING,
        number=1,
    )
    context_references: MutableMapping[str, "Conversation.ContextReference"] = (
        proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=2,
            message="Conversation.ContextReference",
        )
    )


class IngestContextReferencesResponse(proto.Message):
    r"""The response message for
    [ConversationsService.IngestContextReferences][].

    Attributes:
        ingested_context_references (MutableMapping[str, google.cloud.dialogflow_v2beta1.types.Conversation.ContextReference]):
            All context references ingested.
    """

    ingested_context_references: MutableMapping[
        str, "Conversation.ContextReference"
    ] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=1,
        message="Conversation.ContextReference",
    )


class SuggestConversationSummaryRequest(proto.Message):
    r"""The request message for
    [Conversations.SuggestConversationSummary][google.cloud.dialogflow.v2beta1.Conversations.SuggestConversationSummary].

    Attributes:
        conversation (str):
            Required. The conversation to fetch suggestion for. Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>``.
        latest_message (str):
            Optional. The name of the latest conversation message used
            as context for compiling suggestion. If empty, the latest
            message of the conversation will be used.

            Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/messages/<Message ID>``.
        context_size (int):
            Optional. Max number of messages prior to and including
            [latest_message] to use as context when compiling the
            suggestion. By default 500 and at most 1000.
        assist_query_params (google.cloud.dialogflow_v2beta1.types.AssistQueryParameters):
            Optional. Parameters for a human assist
            query. Only used for POC/demo purpose.
    """

    conversation: str = proto.Field(
        proto.STRING,
        number=1,
    )
    latest_message: str = proto.Field(
        proto.STRING,
        number=3,
    )
    context_size: int = proto.Field(
        proto.INT32,
        number=4,
    )
    assist_query_params: participant.AssistQueryParameters = proto.Field(
        proto.MESSAGE,
        number=5,
        message=participant.AssistQueryParameters,
    )


class SuggestConversationSummaryResponse(proto.Message):
    r"""The response message for
    [Conversations.SuggestConversationSummary][google.cloud.dialogflow.v2beta1.Conversations.SuggestConversationSummary].

    Attributes:
        summary (google.cloud.dialogflow_v2beta1.types.SuggestConversationSummaryResponse.Summary):
            Generated summary.
        latest_message (str):
            The name of the latest conversation message used as context
            for compiling suggestion.

            Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/messages/<Message ID>``.
        context_size (int):
            Number of messages prior to and including
            [last_conversation_message][] used to compile the
            suggestion. It may be smaller than the
            [SuggestSummaryRequest.context_size][] field in the request
            if there weren't that many messages in the conversation.
    """

    class Summary(proto.Message):
        r"""Generated summary for a conversation.

        Attributes:
            text (str):
                The summary content that is concatenated into
                one string.
            text_sections (MutableMapping[str, str]):
                The summary content that is divided into
                sections. The key is the section's name and the
                value is the section's content. There is no
                specific format for the key or value.
            sorted_text_sections (MutableSequence[google.cloud.dialogflow_v2beta1.types.SuggestConversationSummaryResponse.Summary.SummarySection]):
                Same as text_sections, but in an order that is consistent
                with the order of the sections in the generator.
            answer_record (str):
                The name of the answer record. Format:

                "projects/<Project ID>/answerRecords/<Answer
                Record ID>".
            baseline_model_version (str):
                The baseline model version used to generate
                this summary. It is empty if a baseline model
                was not used to generate this summary.
        """

        class SummarySection(proto.Message):
            r"""A component of the generated summary.

            Attributes:
                section (str):
                    Output only. Name of the section.
                summary (str):
                    Output only. Summary text for the section.
            """

            section: str = proto.Field(
                proto.STRING,
                number=1,
            )
            summary: str = proto.Field(
                proto.STRING,
                number=2,
            )

        text: str = proto.Field(
            proto.STRING,
            number=1,
        )
        text_sections: MutableMapping[str, str] = proto.MapField(
            proto.STRING,
            proto.STRING,
            number=4,
        )
        sorted_text_sections: MutableSequence[
            "SuggestConversationSummaryResponse.Summary.SummarySection"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=6,
            message="SuggestConversationSummaryResponse.Summary.SummarySection",
        )
        answer_record: str = proto.Field(
            proto.STRING,
            number=3,
        )
        baseline_model_version: str = proto.Field(
            proto.STRING,
            number=5,
        )

    summary: Summary = proto.Field(
        proto.MESSAGE,
        number=1,
        message=Summary,
    )
    latest_message: str = proto.Field(
        proto.STRING,
        number=2,
    )
    context_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class GenerateStatelessSummaryRequest(proto.Message):
    r"""The request message for
    [Conversations.GenerateStatelessSummary][google.cloud.dialogflow.v2beta1.Conversations.GenerateStatelessSummary].

    Attributes:
        stateless_conversation (google.cloud.dialogflow_v2beta1.types.GenerateStatelessSummaryRequest.MinimalConversation):
            Required. The conversation to suggest a
            summary for.
        conversation_profile (google.cloud.dialogflow_v2beta1.types.ConversationProfile):
            Required. A ConversationProfile containing information
            required for Summary generation. Required fields:
            {language_code, security_settings} Optional fields:
            {agent_assistant_config}
        latest_message (str):
            Optional. The name of the latest conversation
            message used as context for generating a
            Summary. If empty, the latest message of the
            conversation will be used. The format is
            specific to the user and the names of the
            messages provided.
        max_context_size (int):
            Optional. Max number of messages prior to and including
            [latest_message] to use as context when compiling the
            suggestion. By default 500 and at most 1000.
    """

    class MinimalConversation(proto.Message):
        r"""The minimum amount of information required to generate a
        Summary without having a Conversation resource created.

        Attributes:
            messages (MutableSequence[google.cloud.dialogflow_v2beta1.types.Message]):
                Required. The messages that the Summary will be generated
                from. It is expected that this message content is already
                redacted and does not contain any PII. Required fields:
                {content, language_code, participant, participant_role}
                Optional fields: {send_time} If send_time is not provided,
                then the messages must be provided in chronological order.
            parent (str):
                Required. The parent resource to charge for the Summary's
                generation. Format:
                ``projects/<Project ID>/locations/<Location ID>``.
        """

        messages: MutableSequence[participant.Message] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=participant.Message,
        )
        parent: str = proto.Field(
            proto.STRING,
            number=2,
        )

    stateless_conversation: MinimalConversation = proto.Field(
        proto.MESSAGE,
        number=1,
        message=MinimalConversation,
    )
    conversation_profile: gcd_conversation_profile.ConversationProfile = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcd_conversation_profile.ConversationProfile,
    )
    latest_message: str = proto.Field(
        proto.STRING,
        number=3,
    )
    max_context_size: int = proto.Field(
        proto.INT32,
        number=4,
    )


class GenerateStatelessSummaryResponse(proto.Message):
    r"""The response message for
    [Conversations.GenerateStatelessSummary][google.cloud.dialogflow.v2beta1.Conversations.GenerateStatelessSummary].

    Attributes:
        summary (google.cloud.dialogflow_v2beta1.types.GenerateStatelessSummaryResponse.Summary):
            Generated summary.
        latest_message (str):
            The name of the latest conversation message
            used as context for compiling suggestion. The
            format is specific to the user and the names of
            the messages provided.
        context_size (int):
            Number of messages prior to and including
            [last_conversation_message][] used to compile the
            suggestion. It may be smaller than the
            [GenerateStatelessSummaryRequest.context_size][] field in
            the request if there weren't that many messages in the
            conversation.
    """

    class Summary(proto.Message):
        r"""Generated summary for a conversation.

        Attributes:
            text (str):
                The summary content that is concatenated into
                one string.
            text_sections (MutableMapping[str, str]):
                The summary content that is divided into
                sections. The key is the section's name and the
                value is the section's content. There is no
                specific format for the key or value.
            baseline_model_version (str):
                The baseline model version used to generate
                this summary. It is empty if a baseline model
                was not used to generate this summary.
        """

        text: str = proto.Field(
            proto.STRING,
            number=1,
        )
        text_sections: MutableMapping[str, str] = proto.MapField(
            proto.STRING,
            proto.STRING,
            number=2,
        )
        baseline_model_version: str = proto.Field(
            proto.STRING,
            number=4,
        )

    summary: Summary = proto.Field(
        proto.MESSAGE,
        number=1,
        message=Summary,
    )
    latest_message: str = proto.Field(
        proto.STRING,
        number=2,
    )
    context_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class GenerateStatelessSuggestionRequest(proto.Message):
    r"""The request message for
    [Conversations.GenerateStatelessSuggestion][google.cloud.dialogflow.v2beta1.Conversations.GenerateStatelessSuggestion].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        parent (str):
            Required. The parent resource to charge for the Suggestion's
            generation. Format:
            ``projects/<Project ID>/locations/<Location ID>``.
        generator (google.cloud.dialogflow_v2beta1.types.Generator):
            Uncreated generator. It should be a complete
            generator that includes all information about
            the generator.

            This field is a member of `oneof`_ ``generator_resource``.
        generator_name (str):
            The resource name of the existing created generator. Format:
            ``projects/<Project ID>/locations/<Location ID>/generators/<Generator ID>``

            This field is a member of `oneof`_ ``generator_resource``.
        context_references (MutableMapping[str, google.cloud.dialogflow_v2beta1.types.Conversation.ContextReference]):
            Optional. A section of ingested context
            information. The key is the name of the context
            reference and the value contains the contents of
            the context reference. The key is used to
            incorporate ingested context references to
            enhance the generator.
        conversation_context (google.cloud.dialogflow_v2beta1.types.ConversationContext):
            Optional. Context of the conversation,
            including transcripts.
        trigger_events (MutableSequence[google.cloud.dialogflow_v2beta1.types.TriggerEvent]):
            Optional. A list of trigger events. Generator
            will be triggered only if it's trigger event is
            included here.
        security_settings (str):
            Optional. Name of the CX SecuritySettings which is used to
            redact generated response. If this field is empty, try to
            fetch v2 security_settings, which is a project level
            setting. If this field is empty and no v2 security_settings
            set up in this project, no redaction will be done.

            Format:
            ``projects/<Project ID>/locations/<Location ID>/securitySettings/<Security Settings ID>``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    generator: gcd_generator.Generator = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="generator_resource",
        message=gcd_generator.Generator,
    )
    generator_name: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="generator_resource",
    )
    context_references: MutableMapping[str, "Conversation.ContextReference"] = (
        proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=4,
            message="Conversation.ContextReference",
        )
    )
    conversation_context: gcd_generator.ConversationContext = proto.Field(
        proto.MESSAGE,
        number=5,
        message=gcd_generator.ConversationContext,
    )
    trigger_events: MutableSequence[gcd_generator.TriggerEvent] = proto.RepeatedField(
        proto.ENUM,
        number=6,
        enum=gcd_generator.TriggerEvent,
    )
    security_settings: str = proto.Field(
        proto.STRING,
        number=8,
    )


class GenerateStatelessSuggestionResponse(proto.Message):
    r"""The response message for
    [Conversations.GenerateStatelessSuggestion][google.cloud.dialogflow.v2beta1.Conversations.GenerateStatelessSuggestion].

    Attributes:
        generator_suggestion (google.cloud.dialogflow_v2beta1.types.GeneratorSuggestion):
            Required. Generated suggestion for a
            conversation.
    """

    generator_suggestion: gcd_generator.GeneratorSuggestion = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcd_generator.GeneratorSuggestion,
    )


class SearchKnowledgeRequest(proto.Message):
    r"""The request message for
    [Conversations.SearchKnowledge][google.cloud.dialogflow.v2beta1.Conversations.SearchKnowledge].

    Attributes:
        parent (str):
            Required. The parent resource contains the conversation
            profile Format: 'projects/' or
            ``projects/<Project ID>/locations/<Location ID>``.
        query (google.cloud.dialogflow_v2beta1.types.TextInput):
            Required. The natural language text query for
            knowledge search.
        conversation_profile (str):
            Required. The conversation profile used to configure the
            search. Format:
            ``projects/<Project ID>/locations/<Location ID>/conversationProfiles/<Conversation Profile ID>``.
        session_id (str):
            Required. The ID of the search session. The session_id can
            be combined with Dialogflow V3 Agent ID retrieved from
            conversation profile or on its own to identify a search
            session. The search history of the same session will impact
            the search result. It's up to the API caller to choose an
            appropriate ``Session ID``. It can be a random number or
            some type of session identifiers (preferably hashed). The
            length must not exceed 36 characters.
        conversation (str):
            Optional. The conversation (between human agent and end
            user) where the search request is triggered. Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>``.
        latest_message (str):
            Optional. The name of the latest conversation message when
            the request is triggered. Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/messages/<Message ID>``.
        query_source (google.cloud.dialogflow_v2beta1.types.SearchKnowledgeRequest.QuerySource):
            Optional. The source of the query in the
            request.
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
        search_config (google.cloud.dialogflow_v2beta1.types.SearchKnowledgeRequest.SearchConfig):
            Optional. Configuration specific to search
            queries with data stores.
        exact_search (bool):
            Optional. Whether to search the query exactly
            without query rewrite.
    """

    class QuerySource(proto.Enum):
        r"""The source of the query. We use QuerySource to distinguish queries
        directly entered by agents and suggested queries from
        [Participants.SuggestKnowledgeAssist][google.cloud.dialogflow.v2beta1.Participants.SuggestKnowledgeAssist].
        If SUGGESTED_QUERY source is specified, we will treat it as a
        continuation of a SuggestKnowledgeAssist call.

        Values:
            QUERY_SOURCE_UNSPECIFIED (0):
                Unknown query source.
            AGENT_QUERY (1):
                The query is from agents.
            SUGGESTED_QUERY (2):
                The query is a suggested query from
                [Participants.SuggestKnowledgeAssist][google.cloud.dialogflow.v2beta1.Participants.SuggestKnowledgeAssist].
        """

        QUERY_SOURCE_UNSPECIFIED = 0
        AGENT_QUERY = 1
        SUGGESTED_QUERY = 2

    class SearchConfig(proto.Message):
        r"""Configuration specific to search queries with data stores.

        Attributes:
            boost_specs (MutableSequence[google.cloud.dialogflow_v2beta1.types.SearchKnowledgeRequest.SearchConfig.BoostSpecs]):
                Optional. Boost specifications for data
                stores.
            filter_specs (MutableSequence[google.cloud.dialogflow_v2beta1.types.SearchKnowledgeRequest.SearchConfig.FilterSpecs]):
                Optional. Filter specification for data store
                queries.
                Maps from datastore name to the filter
                expression for that datastore. Do not specify
                more than one FilterSpecs for each datastore
                name. If multiple FilterSpecs are provided for
                the same datastore name, the behavior is
                undefined.
        """

        class BoostSpecs(proto.Message):
            r"""Boost specifications for data stores.

            Maps from datastore name to their boost configuration. Do not
            specify more than one BoostSpecs for each datastore name. If
            multiple BoostSpecs are provided for the same datastore name,
            the behavior is undefined.

            Attributes:
                data_stores (MutableSequence[str]):
                    Optional. Data Stores where the boosting configuration is
                    applied. The full names of the referenced data stores.
                    Formats:
                    ``projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}``
                    ``projects/{project}/locations/{location}/dataStores/{data_store}``
                spec (MutableSequence[google.cloud.dialogflow_v2beta1.types.SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec]):
                    Optional. A list of boosting specifications.
            """

            class BoostSpec(proto.Message):
                r"""Boost specification to boost certain documents.
                A copy of google.cloud.discoveryengine.v1main.BoostSpec, field
                documentation is available at
                https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/BoostSpec

                Attributes:
                    condition_boost_specs (MutableSequence[google.cloud.dialogflow_v2beta1.types.SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.ConditionBoostSpec]):
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
                        boost_control_spec (google.cloud.dialogflow_v2beta1.types.SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.ConditionBoostSpec.BoostControlSpec):
                            Optional. Complex specification for custom
                            ranking based on customer defined attribute
                            value.
                    """

                    class BoostControlSpec(proto.Message):
                        r"""Specification for custom ranking based on customer specified
                        attribute
                        value. It provides more controls for customized ranking than the
                        simple (condition, boost) combination above.

                        Attributes:
                            field_name (str):
                                Optional. The name of the field whose value
                                will be used to determine the boost amount.
                            attribute_type (google.cloud.dialogflow_v2beta1.types.SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType):
                                Optional. The attribute type to be used to determine the
                                boost amount. The attribute value can be derived from the
                                field value of the specified field_name. In the case of
                                numerical it is straightforward i.e. attribute_value =
                                numerical_field_value. In the case of freshness however,
                                attribute_value = (time.now() - datetime_field_value).
                            interpolation_type (google.cloud.dialogflow_v2beta1.types.SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType):
                                Optional. The interpolation type to be
                                applied to connect the control points listed
                                below.
                            control_points (MutableSequence[google.cloud.dialogflow_v2beta1.types.SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.ConditionBoostSpec.BoostControlSpec.ControlPoint]):
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
                        attribute_type: "SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType" = proto.Field(
                            proto.ENUM,
                            number=2,
                            enum="SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.ConditionBoostSpec.BoostControlSpec.AttributeType",
                        )
                        interpolation_type: "SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType" = proto.Field(
                            proto.ENUM,
                            number=3,
                            enum="SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.ConditionBoostSpec.BoostControlSpec.InterpolationType",
                        )
                        control_points: MutableSequence[
                            "SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.ConditionBoostSpec.BoostControlSpec.ControlPoint"
                        ] = proto.RepeatedField(
                            proto.MESSAGE,
                            number=4,
                            message="SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.ConditionBoostSpec.BoostControlSpec.ControlPoint",
                        )

                    condition: str = proto.Field(
                        proto.STRING,
                        number=1,
                    )
                    boost: float = proto.Field(
                        proto.FLOAT,
                        number=2,
                    )
                    boost_control_spec: "SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.ConditionBoostSpec.BoostControlSpec" = proto.Field(
                        proto.MESSAGE,
                        number=4,
                        message="SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.ConditionBoostSpec.BoostControlSpec",
                    )

                condition_boost_specs: MutableSequence[
                    "SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.ConditionBoostSpec"
                ] = proto.RepeatedField(
                    proto.MESSAGE,
                    number=1,
                    message="SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec.ConditionBoostSpec",
                )

            data_stores: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=1,
            )
            spec: MutableSequence[
                "SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec"
            ] = proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message="SearchKnowledgeRequest.SearchConfig.BoostSpecs.BoostSpec",
            )

        class FilterSpecs(proto.Message):
            r"""Filter specification for data store queries.

            Attributes:
                data_stores (MutableSequence[str]):
                    Optional. The data store where the filter
                    configuration is applied. Full resource name of
                    data store, such as
                    projects/{project}/locations/{location}/collections/{collectionId}/
                    dataStores/{dataStoreId}.
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

        boost_specs: MutableSequence[
            "SearchKnowledgeRequest.SearchConfig.BoostSpecs"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="SearchKnowledgeRequest.SearchConfig.BoostSpecs",
        )
        filter_specs: MutableSequence[
            "SearchKnowledgeRequest.SearchConfig.FilterSpecs"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="SearchKnowledgeRequest.SearchConfig.FilterSpecs",
        )

    parent: str = proto.Field(
        proto.STRING,
        number=6,
    )
    query: session.TextInput = proto.Field(
        proto.MESSAGE,
        number=1,
        message=session.TextInput,
    )
    conversation_profile: str = proto.Field(
        proto.STRING,
        number=2,
    )
    session_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    conversation: str = proto.Field(
        proto.STRING,
        number=4,
    )
    latest_message: str = proto.Field(
        proto.STRING,
        number=5,
    )
    query_source: QuerySource = proto.Field(
        proto.ENUM,
        number=7,
        enum=QuerySource,
    )
    end_user_metadata: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=9,
        message=struct_pb2.Struct,
    )
    search_config: SearchConfig = proto.Field(
        proto.MESSAGE,
        number=11,
        message=SearchConfig,
    )
    exact_search: bool = proto.Field(
        proto.BOOL,
        number=14,
    )


class SearchKnowledgeDebugInfo(proto.Message):
    r"""Debug information related to SearchKnowledge feature.

    Attributes:
        datastore_response_reason (google.cloud.dialogflow_v2beta1.types.DatastoreResponseReason):
            Response reason from datastore which
            indicates data serving status or answer quality
            degradation.
        search_knowledge_behavior (google.cloud.dialogflow_v2beta1.types.SearchKnowledgeDebugInfo.SearchKnowledgeBehavior):
            Configured behaviors for SearchKnowledge.
        ingested_context_reference_debug_info (google.cloud.dialogflow_v2beta1.types.IngestedContextReferenceDebugInfo):
            Information about parameters ingested for
            search knowledge.
        service_latency (google.cloud.dialogflow_v2beta1.types.ServiceLatency):
            The latency of the service.
        ces_debug_info (google.protobuf.struct_pb2.Struct):
            Optional. Debug info from the Customer
            Engagement Suite (CES) execution.
    """

    class SearchKnowledgeBehavior(proto.Message):
        r"""Configured behaviors for SearchKnowledge.

        Attributes:
            answer_generation_rewriter_on (bool):
                Whether data store agent rewriter was turned
                on for the request.
            end_user_metadata_included (bool):
                Whether end_user_metadata is included in the data store
                agent call.
            third_party_connector_allowed (bool):
                This field indicates whether third party
                connectors are enabled for the project. Note
                that this field only indicates if the project is
                allowlisted for connectors.
        """

        answer_generation_rewriter_on: bool = proto.Field(
            proto.BOOL,
            number=1,
        )
        end_user_metadata_included: bool = proto.Field(
            proto.BOOL,
            number=2,
        )
        third_party_connector_allowed: bool = proto.Field(
            proto.BOOL,
            number=4,
        )

    datastore_response_reason: participant.DatastoreResponseReason = proto.Field(
        proto.ENUM,
        number=1,
        enum=participant.DatastoreResponseReason,
    )
    search_knowledge_behavior: SearchKnowledgeBehavior = proto.Field(
        proto.MESSAGE,
        number=2,
        message=SearchKnowledgeBehavior,
    )
    ingested_context_reference_debug_info: participant.IngestedContextReferenceDebugInfo = proto.Field(
        proto.MESSAGE,
        number=3,
        message=participant.IngestedContextReferenceDebugInfo,
    )
    service_latency: participant.ServiceLatency = proto.Field(
        proto.MESSAGE,
        number=4,
        message=participant.ServiceLatency,
    )
    ces_debug_info: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=5,
        message=struct_pb2.Struct,
    )


class SearchKnowledgeResponse(proto.Message):
    r"""The response message for
    [Conversations.SearchKnowledge][google.cloud.dialogflow.v2beta1.Conversations.SearchKnowledge].

    Attributes:
        answers (MutableSequence[google.cloud.dialogflow_v2beta1.types.SearchKnowledgeAnswer]):
            Most relevant snippets extracted from
            articles in the given knowledge base, ordered by
            confidence.
        rewritten_query (str):
            The rewritten query used to search knowledge.
        search_knowledge_debug_info (google.cloud.dialogflow_v2beta1.types.SearchKnowledgeDebugInfo):
            Debug info for SearchKnowledge.
    """

    answers: MutableSequence["SearchKnowledgeAnswer"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="SearchKnowledgeAnswer",
    )
    rewritten_query: str = proto.Field(
        proto.STRING,
        number=3,
    )
    search_knowledge_debug_info: "SearchKnowledgeDebugInfo" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="SearchKnowledgeDebugInfo",
    )


class SearchKnowledgeAnswer(proto.Message):
    r"""Represents a SearchKnowledge answer.

    Attributes:
        answer (str):
            The piece of text from the knowledge base
            documents that answers the search query
        answer_type (google.cloud.dialogflow_v2beta1.types.SearchKnowledgeAnswer.AnswerType):
            The type of the answer.
        answer_sources (MutableSequence[google.cloud.dialogflow_v2beta1.types.SearchKnowledgeAnswer.AnswerSource]):
            All sources used to generate the answer.
        answer_record (str):
            The name of the answer record. Format:
            ``projects/<Project ID>/locations/<location ID>/answer Records/<Answer Record ID>``
    """

    class AnswerType(proto.Enum):
        r"""The type of the answer.

        Values:
            ANSWER_TYPE_UNSPECIFIED (0):
                The answer has a unspecified type.
            FAQ (1):
                The answer is from FAQ documents.
            GENERATIVE (2):
                The answer is from generative model.
            INTENT (3):
                The answer is from intent matching.
            PLAYBOOK (4):
                The answer is from Playbook.
            EVENT (5):
                The answer is from event.
        """

        ANSWER_TYPE_UNSPECIFIED = 0
        FAQ = 1
        GENERATIVE = 2
        INTENT = 3
        PLAYBOOK = 4
        EVENT = 5

    class AnswerSource(proto.Message):
        r"""The sources of the answers.

        Attributes:
            title (str):
                The title of the article.
            uri (str):
                The URI of the article.
            snippet (str):
                The relevant snippet of the article.
            metadata (google.protobuf.struct_pb2.Struct):
                Metadata associated with the article.
        """

        title: str = proto.Field(
            proto.STRING,
            number=1,
        )
        uri: str = proto.Field(
            proto.STRING,
            number=2,
        )
        snippet: str = proto.Field(
            proto.STRING,
            number=3,
        )
        metadata: struct_pb2.Struct = proto.Field(
            proto.MESSAGE,
            number=5,
            message=struct_pb2.Struct,
        )

    answer: str = proto.Field(
        proto.STRING,
        number=1,
    )
    answer_type: AnswerType = proto.Field(
        proto.ENUM,
        number=2,
        enum=AnswerType,
    )
    answer_sources: MutableSequence[AnswerSource] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=AnswerSource,
    )
    answer_record: str = proto.Field(
        proto.STRING,
        number=5,
    )


class GenerateSuggestionsRequest(proto.Message):
    r"""The request message for
    [Conversations.GenerateSuggestions][google.cloud.dialogflow.v2beta1.Conversations.GenerateSuggestions].

    Attributes:
        conversation (str):
            Required. The conversation for which the suggestions are
            generated. Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>``.

            The conversation must be created with a conversation profile
            which has generators configured in it to be able to get
            suggestions.
        latest_message (str):
            Optional. The name of the latest conversation message for
            which the request is triggered. Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/messages/<Message ID>``.
        trigger_events (MutableSequence[google.cloud.dialogflow_v2beta1.types.TriggerEvent]):
            Optional. A list of trigger events. Only generators
            configured in the conversation_profile whose trigger_event
            is listed here will be triggered.
    """

    conversation: str = proto.Field(
        proto.STRING,
        number=1,
    )
    latest_message: str = proto.Field(
        proto.STRING,
        number=2,
    )
    trigger_events: MutableSequence[gcd_generator.TriggerEvent] = proto.RepeatedField(
        proto.ENUM,
        number=3,
        enum=gcd_generator.TriggerEvent,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
