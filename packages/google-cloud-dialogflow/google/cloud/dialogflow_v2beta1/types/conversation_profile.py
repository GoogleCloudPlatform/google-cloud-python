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
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.dialogflow_v2beta1.types import audio_config, generator, participant

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.v2beta1",
    manifest={
        "ConversationProfile",
        "AutomatedAgentConfig",
        "HumanAgentAssistantConfig",
        "HumanAgentHandoffConfig",
        "NotificationConfig",
        "LoggingConfig",
        "SipConfig",
        "ListConversationProfilesRequest",
        "ListConversationProfilesResponse",
        "GetConversationProfileRequest",
        "CreateConversationProfileRequest",
        "UpdateConversationProfileRequest",
        "DeleteConversationProfileRequest",
        "SetSuggestionFeatureConfigRequest",
        "ClearSuggestionFeatureConfigRequest",
        "SetSuggestionFeatureConfigOperationMetadata",
        "ClearSuggestionFeatureConfigOperationMetadata",
    },
)


class ConversationProfile(proto.Message):
    r"""Defines the services to connect to incoming Dialogflow
    conversations.

    Attributes:
        name (str):
            The unique identifier of this conversation profile. Format:
            ``projects/<Project ID>/locations/<Location ID>/conversationProfiles/<Conversation Profile ID>``.
        display_name (str):
            Required. Human readable name for this
            profile. Max length 1024 bytes.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create time of the conversation
            profile.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Update time of the conversation
            profile.
        use_bidi_streaming (bool):
            Optional. Whether to use the bidi streaming
            API in telephony integration for the
            conversation profile.
        automated_agent_config (google.cloud.dialogflow_v2beta1.types.AutomatedAgentConfig):
            Configuration for an automated agent to use
            with this profile.
        human_agent_assistant_config (google.cloud.dialogflow_v2beta1.types.HumanAgentAssistantConfig):
            Configuration for agent assistance to use
            with this profile.
        human_agent_handoff_config (google.cloud.dialogflow_v2beta1.types.HumanAgentHandoffConfig):
            Configuration for connecting to a live agent.

            Currently, this feature is not general
            available, please contact Google to get access.
        notification_config (google.cloud.dialogflow_v2beta1.types.NotificationConfig):
            Configuration for publishing conversation
            lifecycle events.
        logging_config (google.cloud.dialogflow_v2beta1.types.LoggingConfig):
            Configuration for logging conversation
            lifecycle events.
        new_message_event_notification_config (google.cloud.dialogflow_v2beta1.types.NotificationConfig):
            Configuration for publishing new message events. Event will
            be sent in format of
            [ConversationEvent][google.cloud.dialogflow.v2beta1.ConversationEvent]
        new_recognition_result_notification_config (google.cloud.dialogflow_v2beta1.types.NotificationConfig):
            Optional. Configuration for publishing transcription
            intermediate results. Event will be sent in format of
            [ConversationEvent][google.cloud.dialogflow.v2beta1.ConversationEvent].
            If configured, the following information will be populated
            as
            [ConversationEvent][google.cloud.dialogflow.v2beta1.ConversationEvent]
            Pub/Sub message attributes:

            - "participant_id"
            - "participant_role"
            - "message_id".
        stt_config (google.cloud.dialogflow_v2beta1.types.SpeechToTextConfig):
            Settings for speech transcription.
        language_code (str):
            Language code for the conversation profile. If not
            specified, the language is en-US. Language at
            ConversationProfile should be set for all non en-us
            languages. This should be a
            `BCP-47 <https://www.rfc-editor.org/rfc/bcp/bcp47.txt>`__
            language tag. Example: "en-US".
        sip_config (google.cloud.dialogflow_v2beta1.types.SipConfig):
            Optional. Configuration for SIP connections.
        time_zone (str):
            The time zone of this conversational profile from the `time
            zone database <https://www.iana.org/time-zones>`__, e.g.,
            America/New_York, Europe/Paris. Defaults to
            America/New_York.
        security_settings (str):
            Name of the CX SecuritySettings reference for the agent.
            Format:
            ``projects/<Project ID>/locations/<Location ID>/securitySettings/<Security Settings ID>``.
        tts_config (google.cloud.dialogflow_v2beta1.types.SynthesizeSpeechConfig):
            Configuration for Text-to-Speech
            synthesization.
            Used by Phone Gateway to specify synthesization
            options. If agent defines synthesization options
            as well, agent settings overrides the option
            here.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=11,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=12,
        message=timestamp_pb2.Timestamp,
    )
    use_bidi_streaming: bool = proto.Field(
        proto.BOOL,
        number=23,
    )
    automated_agent_config: "AutomatedAgentConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="AutomatedAgentConfig",
    )
    human_agent_assistant_config: "HumanAgentAssistantConfig" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="HumanAgentAssistantConfig",
    )
    human_agent_handoff_config: "HumanAgentHandoffConfig" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="HumanAgentHandoffConfig",
    )
    notification_config: "NotificationConfig" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="NotificationConfig",
    )
    logging_config: "LoggingConfig" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="LoggingConfig",
    )
    new_message_event_notification_config: "NotificationConfig" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="NotificationConfig",
    )
    new_recognition_result_notification_config: "NotificationConfig" = proto.Field(
        proto.MESSAGE,
        number=21,
        message="NotificationConfig",
    )
    stt_config: audio_config.SpeechToTextConfig = proto.Field(
        proto.MESSAGE,
        number=9,
        message=audio_config.SpeechToTextConfig,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=10,
    )
    sip_config: "SipConfig" = proto.Field(
        proto.MESSAGE,
        number=16,
        message="SipConfig",
    )
    time_zone: str = proto.Field(
        proto.STRING,
        number=14,
    )
    security_settings: str = proto.Field(
        proto.STRING,
        number=13,
    )
    tts_config: audio_config.SynthesizeSpeechConfig = proto.Field(
        proto.MESSAGE,
        number=18,
        message=audio_config.SynthesizeSpeechConfig,
    )


class AutomatedAgentConfig(proto.Message):
    r"""Defines the Automated Agent to connect to a conversation.

    Attributes:
        agent (str):
            Required. The resource name of the Dialogflow agent
            environment to use.

            This project needs to either be the same project as the
            conversation or you need to grant
            ``service-<Conversation Project Number>@gcp-sa-dialogflow.iam.gserviceaccount.com``
            the ``Dialogflow API Service Agent`` role in this project.

            - For ES agents, use format:
              ``projects/<Project ID>/locations/<Location ID>/agent/environments/<Environment ID or '-'>``.
              If environment is not specified, the default ``draft``
              environment is used. Refer to
              `DetectIntentRequest </dialogflow/docs/reference/rpc/google.cloud.dialogflow.v2beta1#google.cloud.dialogflow.v2beta1.DetectIntentRequest>`__
              for more details.

            - For CX agents, use format
              ``projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>/environments/<Environment ID or '-'>``.
              If environment is not specified, the default ``draft``
              environment is used.
        session_ttl (google.protobuf.duration_pb2.Duration):
            Optional. Configure lifetime of the
            Dialogflow session. By default, a Dialogflow CX
            session remains active and its data is stored
            for 30 minutes after the last request is sent
            for the session. This value should be no longer
            than 1 day.
    """

    agent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    session_ttl: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=3,
        message=duration_pb2.Duration,
    )


class HumanAgentAssistantConfig(proto.Message):
    r"""Defines the Human Agent Assistant to connect to a
    conversation.

    Attributes:
        notification_config (google.cloud.dialogflow_v2beta1.types.NotificationConfig):
            Pub/Sub topic on which to publish new agent
            assistant events.
        human_agent_suggestion_config (google.cloud.dialogflow_v2beta1.types.HumanAgentAssistantConfig.SuggestionConfig):
            Configuration for agent assistance of human
            agent participant.
        end_user_suggestion_config (google.cloud.dialogflow_v2beta1.types.HumanAgentAssistantConfig.SuggestionConfig):
            Configuration for agent assistance of end
            user participant.
            Currently, this feature is not general
            available, please contact Google to get access.
        message_analysis_config (google.cloud.dialogflow_v2beta1.types.HumanAgentAssistantConfig.MessageAnalysisConfig):
            Configuration for message analysis.
    """

    class SuggestionTriggerSettings(proto.Message):
        r"""Settings of suggestion trigger.

        Attributes:
            no_small_talk (bool):
                Do not trigger if last utterance is small
                talk.
            only_end_user (bool):
                Only trigger suggestion if participant role of last
                utterance is END_USER.
        """

        no_small_talk: bool = proto.Field(
            proto.BOOL,
            number=1,
        )
        only_end_user: bool = proto.Field(
            proto.BOOL,
            number=2,
        )

    class SuggestionFeatureConfig(proto.Message):
        r"""Config for suggestion features.

        Attributes:
            suggestion_feature (google.cloud.dialogflow_v2beta1.types.SuggestionFeature):
                The suggestion feature.
            enable_event_based_suggestion (bool):
                Automatically iterates all participants and tries to compile
                suggestions.

                Supported features: ARTICLE_SUGGESTION, FAQ,
                DIALOGFLOW_ASSIST, ENTITY_EXTRACTION, KNOWLEDGE_ASSIST.
            disable_agent_query_logging (bool):
                Optional. Disable the logging of search queries sent by
                human agents. It can prevent those queries from being stored
                at answer records.

                Supported features: KNOWLEDGE_SEARCH.
            enable_query_suggestion_when_no_answer (bool):
                Optional. Enable query suggestion even if we can't find its
                answer. By default, queries are suggested only if we find
                its answer. Supported features: KNOWLEDGE_ASSIST
            enable_conversation_augmented_query (bool):
                Optional. Enable including conversation context during query
                answer generation. Supported features: KNOWLEDGE_SEARCH.
            enable_query_suggestion_only (bool):
                Optional. Enable query suggestion only. Supported features:
                KNOWLEDGE_ASSIST
            enable_response_debug_info (bool):
                Optional. Enable returning detailed reasons for suggestion
                results.

                For example, with this field disabled, Knowledge Search
                feature returns NotFound error when no answer is found for
                the input query. Enabling this field will change the
                behavior to return an OK response with detailed information
                indicating the lack of results.

                Supported features: KNOWLEDGE_SEARCH, KNOWLEDGE_ASSIST
            rai_settings (google.cloud.dialogflow_v2beta1.types.RaiSettings):
                Optional. Settings for Responsible AI checks. Supported
                features: KNOWLEDGE_ASSIST
            suggestion_trigger_event (google.cloud.dialogflow_v2beta1.types.TriggerEvent):
                Optional. The trigger event for suggestion. If unspecified,
                it will be ``CUSTOMER_MESSAGE``. Supported features:
                KNOWLEDGE_ASSIST For KNOWLEDGE_ASSIST, these four trigger
                events are supported:

                1. TRIGGER_EVENT_UNSPECIFIED
                2. END_OF_UTTERANCE
                3. CUSTOMER_MESSAGE
                4. AGENT_MESSAGE
            disable_query_search_context (bool):
                Optional. If true, disable appending available search
                context to the search query. Supported features:
                KNOWLEDGE_ASSIST
            suggestion_trigger_settings (google.cloud.dialogflow_v2beta1.types.HumanAgentAssistantConfig.SuggestionTriggerSettings):
                Settings of suggestion trigger.

                Currently, only ARTICLE_SUGGESTION, FAQ, and
                DIALOGFLOW_ASSIST will use this field.
            query_config (google.cloud.dialogflow_v2beta1.types.HumanAgentAssistantConfig.SuggestionQueryConfig):
                Configs of query.
            conversation_process_config (google.cloud.dialogflow_v2beta1.types.HumanAgentAssistantConfig.ConversationProcessConfig):
                Configs for processing conversation.
        """

        suggestion_feature: participant.SuggestionFeature = proto.Field(
            proto.MESSAGE,
            number=5,
            message=participant.SuggestionFeature,
        )
        enable_event_based_suggestion: bool = proto.Field(
            proto.BOOL,
            number=3,
        )
        disable_agent_query_logging: bool = proto.Field(
            proto.BOOL,
            number=14,
        )
        enable_query_suggestion_when_no_answer: bool = proto.Field(
            proto.BOOL,
            number=15,
        )
        enable_conversation_augmented_query: bool = proto.Field(
            proto.BOOL,
            number=16,
        )
        enable_query_suggestion_only: bool = proto.Field(
            proto.BOOL,
            number=17,
        )
        enable_response_debug_info: bool = proto.Field(
            proto.BOOL,
            number=18,
        )
        rai_settings: generator.RaiSettings = proto.Field(
            proto.MESSAGE,
            number=19,
            message=generator.RaiSettings,
        )
        suggestion_trigger_event: generator.TriggerEvent = proto.Field(
            proto.ENUM,
            number=20,
            enum=generator.TriggerEvent,
        )
        disable_query_search_context: bool = proto.Field(
            proto.BOOL,
            number=21,
        )
        suggestion_trigger_settings: "HumanAgentAssistantConfig.SuggestionTriggerSettings" = proto.Field(
            proto.MESSAGE,
            number=10,
            message="HumanAgentAssistantConfig.SuggestionTriggerSettings",
        )
        query_config: "HumanAgentAssistantConfig.SuggestionQueryConfig" = proto.Field(
            proto.MESSAGE,
            number=6,
            message="HumanAgentAssistantConfig.SuggestionQueryConfig",
        )
        conversation_process_config: "HumanAgentAssistantConfig.ConversationProcessConfig" = proto.Field(
            proto.MESSAGE,
            number=8,
            message="HumanAgentAssistantConfig.ConversationProcessConfig",
        )

    class SuggestionConfig(proto.Message):
        r"""Detail human agent assistant config.

        Attributes:
            feature_configs (MutableSequence[google.cloud.dialogflow_v2beta1.types.HumanAgentAssistantConfig.SuggestionFeatureConfig]):
                Configuration of different suggestion
                features. One feature can have only one config.
            group_suggestion_responses (bool):
                If ``group_suggestion_responses`` is false, and there are
                multiple ``feature_configs`` in ``event based suggestion``
                or StreamingAnalyzeContent, we will try to deliver
                suggestions to customers as soon as we get new suggestion.
                Different type of suggestions based on the same context will
                be in separate Pub/Sub event or
                ``StreamingAnalyzeContentResponse``.

                If ``group_suggestion_responses`` set to true. All the
                suggestions to the same participant based on the same
                context will be grouped into a single Pub/Sub event or
                StreamingAnalyzeContentResponse.
            generators (MutableSequence[str]):
                Optional. List of various generator resource
                names used in the conversation profile.
            disable_high_latency_features_sync_delivery (bool):
                Optional. When disable_high_latency_features_sync_delivery
                is true and using the AnalyzeContent API, we will not
                deliver the responses from high latency features in the API
                response. The
                human_agent_assistant_config.notification_config must be
                configured and enable_event_based_suggestion must be set to
                true to receive the responses from high latency features in
                Pub/Sub. High latency feature(s): KNOWLEDGE_ASSIST
            skip_empty_event_based_suggestion (bool):
                Optional. Enable skipping event based
                suggestion if the suggestion is empty.

                For example, with this field disabled, Knowledge
                Assist feature sends a Pub/Sub message when
                there are no suggestions. Enabling this field
                will change the behavior to skip the Pub/Sub
                message in this situation.
            use_unredacted_conversation_data (bool):
                Optional. If true, use unredacted transcript data (Supported
                features: AI_COACH) and use unredacted ingested context
                (Supported features: All Agent Assist features)
            enable_async_tool_call (bool):
                Optional. Deprecated: This field is not consulted for tool
                execution. Configure asynchronous execution per tool using
                [CesToolSpec.async_execution][google.cloud.dialogflow.v2beta1.CesToolSpec.async_execution]
                or
                [ToolsetTool.async_execution][google.cloud.dialogflow.v2beta1.ToolsetTool.async_execution]
                instead.
            companion_agent (str):
                Optional. The resource name of the companion agent to link.
                This is only supported for
                ``human_agent_suggestion_config``. Format:
                ``projects/{project}/locations/{location}/companionAgents/{companion_agent}``
        """

        feature_configs: MutableSequence[
            "HumanAgentAssistantConfig.SuggestionFeatureConfig"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="HumanAgentAssistantConfig.SuggestionFeatureConfig",
        )
        group_suggestion_responses: bool = proto.Field(
            proto.BOOL,
            number=3,
        )
        generators: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=4,
        )
        disable_high_latency_features_sync_delivery: bool = proto.Field(
            proto.BOOL,
            number=5,
        )
        skip_empty_event_based_suggestion: bool = proto.Field(
            proto.BOOL,
            number=6,
        )
        use_unredacted_conversation_data: bool = proto.Field(
            proto.BOOL,
            number=8,
        )
        enable_async_tool_call: bool = proto.Field(
            proto.BOOL,
            number=9,
        )
        companion_agent: str = proto.Field(
            proto.STRING,
            number=11,
        )

    class SuggestionQueryConfig(proto.Message):
        r"""Config for suggestion query.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            knowledge_base_query_source (google.cloud.dialogflow_v2beta1.types.HumanAgentAssistantConfig.SuggestionQueryConfig.KnowledgeBaseQuerySource):
                Query from knowledgebase. It is used by: ARTICLE_SUGGESTION,
                FAQ.

                This field is a member of `oneof`_ ``query_source``.
            document_query_source (google.cloud.dialogflow_v2beta1.types.HumanAgentAssistantConfig.SuggestionQueryConfig.DocumentQuerySource):
                Query from knowledge base document. It is used by:
                SMART_REPLY, SMART_COMPOSE.

                This field is a member of `oneof`_ ``query_source``.
            dialogflow_query_source (google.cloud.dialogflow_v2beta1.types.HumanAgentAssistantConfig.SuggestionQueryConfig.DialogflowQuerySource):
                Query from Dialogflow agent. It is used by
                DIALOGFLOW_ASSIST, ENTITY_EXTRACTION.

                This field is a member of `oneof`_ ``query_source``.
            max_results (int):
                Maximum number of results to return.
                Currently, if unset, defaults to 10. And the max
                number is 20.
            confidence_threshold (float):
                Confidence threshold of query result.

                Agent Assist gives each suggestion a score in the range
                [0.0, 1.0], based on the relevance between the suggestion
                and the current conversation context. A score of 0.0 has no
                relevance, while a score of 1.0 has high relevance. Only
                suggestions with a score greater than or equal to the value
                of this field are included in the results.

                For a baseline model (the default), the recommended value is
                in the range [0.05, 0.1].

                For a custom model, there is no recommended value. Tune this
                value by starting from a very low value and slowly
                increasing until you have desired results.

                If this field is not set, it is default to 0.0, which means
                that all suggestions are returned.

                Supported features: ARTICLE_SUGGESTION, FAQ, SMART_REPLY,
                SMART_COMPOSE, KNOWLEDGE_SEARCH, KNOWLEDGE_ASSIST,
                ENTITY_EXTRACTION.
            context_filter_settings (google.cloud.dialogflow_v2beta1.types.HumanAgentAssistantConfig.SuggestionQueryConfig.ContextFilterSettings):
                Determines how recent conversation context is
                filtered when generating suggestions. If
                unspecified, no messages will be dropped.
            sections (google.cloud.dialogflow_v2beta1.types.HumanAgentAssistantConfig.SuggestionQueryConfig.Sections):
                Optional. The customized sections chosen to
                return when requesting a summary of a
                conversation.
            context_size (int):
                Optional. The number of recent messages to include in the
                context. Supported features: KNOWLEDGE_ASSIST.
        """

        class KnowledgeBaseQuerySource(proto.Message):
            r"""Knowledge base source settings.

            Supported features: ARTICLE_SUGGESTION, FAQ.

            Attributes:
                knowledge_bases (MutableSequence[str]):
                    Required. Knowledge bases to query. Format:
                    ``projects/<Project ID>/locations/<Location ID>/knowledgeBases/<Knowledge Base ID>``.
                    Currently, only one knowledge base is supported.
            """

            knowledge_bases: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=1,
            )

        class DocumentQuerySource(proto.Message):
            r"""Document source settings.

            Supported features: SMART_REPLY, SMART_COMPOSE.

            Attributes:
                documents (MutableSequence[str]):
                    Required. Knowledge documents to query from. Format:
                    ``projects/<Project ID>/locations/<Location ID>/knowledgeBases/<KnowledgeBase ID>/documents/<Document ID>``.
                    Currently, only one document is supported.
            """

            documents: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=1,
            )

        class DialogflowQuerySource(proto.Message):
            r"""Dialogflow source setting.

            Supported feature: DIALOGFLOW_ASSIST, ENTITY_EXTRACTION.

            Attributes:
                agent (str):
                    Required. The name of a dialogflow virtual agent used for
                    end user side intent detection and suggestion. Format:
                    ``projects/<Project ID>/locations/<Location ID>/agent``.
                    When multiple agents are allowed in the same Dialogflow
                    project.
                human_agent_side_config (google.cloud.dialogflow_v2beta1.types.HumanAgentAssistantConfig.SuggestionQueryConfig.DialogflowQuerySource.HumanAgentSideConfig):
                    The Dialogflow assist configuration for human
                    agent.
            """

            class HumanAgentSideConfig(proto.Message):
                r"""The configuration used for human agent side Dialogflow assist
                suggestion.

                Attributes:
                    agent (str):
                        Optional. The name of a dialogflow virtual agent used for
                        intent detection and suggestion triggered by human agent.
                        Format:
                        ``projects/<Project ID>/locations/<Location ID>/agent``.
                """

                agent: str = proto.Field(
                    proto.STRING,
                    number=1,
                )

            agent: str = proto.Field(
                proto.STRING,
                number=1,
            )
            human_agent_side_config: "HumanAgentAssistantConfig.SuggestionQueryConfig.DialogflowQuerySource.HumanAgentSideConfig" = proto.Field(
                proto.MESSAGE,
                number=3,
                message="HumanAgentAssistantConfig.SuggestionQueryConfig.DialogflowQuerySource.HumanAgentSideConfig",
            )

        class ContextFilterSettings(proto.Message):
            r"""Settings that determine how to filter recent conversation
            context when generating suggestions.

            Attributes:
                drop_handoff_messages (bool):
                    If set to true, the last message from virtual
                    agent (hand off message) and the message before
                    it (trigger message of hand off) are dropped.
                drop_virtual_agent_messages (bool):
                    If set to true, all messages from virtual
                    agent are dropped.
                drop_ivr_messages (bool):
                    If set to true, all messages from ivr stage
                    are dropped.
            """

            drop_handoff_messages: bool = proto.Field(
                proto.BOOL,
                number=1,
            )
            drop_virtual_agent_messages: bool = proto.Field(
                proto.BOOL,
                number=2,
            )
            drop_ivr_messages: bool = proto.Field(
                proto.BOOL,
                number=3,
            )

        class Sections(proto.Message):
            r"""Custom sections to return when requesting a summary of a
            conversation. This is only supported when ``baseline_model_version``
            == '2.0'.

            Supported features: CONVERSATION_SUMMARIZATION,
            CONVERSATION_SUMMARIZATION_VOICE.

            Attributes:
                section_types (MutableSequence[google.cloud.dialogflow_v2beta1.types.HumanAgentAssistantConfig.SuggestionQueryConfig.Sections.SectionType]):
                    The selected sections chosen to return when
                    requesting a summary of a conversation. A
                    duplicate selected section will be treated as a
                    single selected section. If section types are
                    not provided, the default will be {SITUATION,
                    ACTION, RESULT}.
            """

            class SectionType(proto.Enum):
                r"""Selectable sections to return when requesting a summary of a
                conversation.

                Values:
                    SECTION_TYPE_UNSPECIFIED (0):
                        Undefined section type, does not return
                        anything.
                    SITUATION (1):
                        What the customer needs help with or has
                        question about. Section name: "situation".
                    ACTION (2):
                        What the agent does to help the customer.
                        Section name: "action".
                    RESOLUTION (3):
                        Result of the customer service. A single word
                        describing the result of the conversation.
                        Section name: "resolution".
                    REASON_FOR_CANCELLATION (4):
                        Reason for cancellation if the customer requests for a
                        cancellation. "N/A" otherwise. Section name:
                        "reason_for_cancellation".
                    CUSTOMER_SATISFACTION (5):
                        "Unsatisfied" or "Satisfied" depending on the customer's
                        feelings at the end of the conversation. Section name:
                        "customer_satisfaction".
                    ENTITIES (6):
                        Key entities extracted from the conversation,
                        such as ticket number, order number, dollar
                        amount, etc. Section names are prefixed by
                        "entities/".
                """

                SECTION_TYPE_UNSPECIFIED = 0
                SITUATION = 1
                ACTION = 2
                RESOLUTION = 3
                REASON_FOR_CANCELLATION = 4
                CUSTOMER_SATISFACTION = 5
                ENTITIES = 6

            section_types: MutableSequence[
                "HumanAgentAssistantConfig.SuggestionQueryConfig.Sections.SectionType"
            ] = proto.RepeatedField(
                proto.ENUM,
                number=1,
                enum="HumanAgentAssistantConfig.SuggestionQueryConfig.Sections.SectionType",
            )

        knowledge_base_query_source: "HumanAgentAssistantConfig.SuggestionQueryConfig.KnowledgeBaseQuerySource" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="query_source",
            message="HumanAgentAssistantConfig.SuggestionQueryConfig.KnowledgeBaseQuerySource",
        )
        document_query_source: "HumanAgentAssistantConfig.SuggestionQueryConfig.DocumentQuerySource" = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="query_source",
            message="HumanAgentAssistantConfig.SuggestionQueryConfig.DocumentQuerySource",
        )
        dialogflow_query_source: "HumanAgentAssistantConfig.SuggestionQueryConfig.DialogflowQuerySource" = proto.Field(
            proto.MESSAGE,
            number=3,
            oneof="query_source",
            message="HumanAgentAssistantConfig.SuggestionQueryConfig.DialogflowQuerySource",
        )
        max_results: int = proto.Field(
            proto.INT32,
            number=4,
        )
        confidence_threshold: float = proto.Field(
            proto.FLOAT,
            number=5,
        )
        context_filter_settings: "HumanAgentAssistantConfig.SuggestionQueryConfig.ContextFilterSettings" = proto.Field(
            proto.MESSAGE,
            number=7,
            message="HumanAgentAssistantConfig.SuggestionQueryConfig.ContextFilterSettings",
        )
        sections: "HumanAgentAssistantConfig.SuggestionQueryConfig.Sections" = (
            proto.Field(
                proto.MESSAGE,
                number=8,
                message="HumanAgentAssistantConfig.SuggestionQueryConfig.Sections",
            )
        )
        context_size: int = proto.Field(
            proto.INT32,
            number=9,
        )

    class ConversationProcessConfig(proto.Message):
        r"""Config to process conversation.

        Attributes:
            recent_sentences_count (int):
                Number of recent non-small-talk sentences to
                use as context for article and FAQ suggestion
        """

        recent_sentences_count: int = proto.Field(
            proto.INT32,
            number=2,
        )

    class MessageAnalysisConfig(proto.Message):
        r"""Configuration for analyses to run on each conversation
        message.

        Attributes:
            enable_entity_extraction (bool):
                Enable entity extraction in conversation messages on `agent
                assist
                stage <https://cloud.google.com/dialogflow/priv/docs/contact-center/basics#stages>`__.
                If unspecified, defaults to false.

                Currently, this feature is not general available, please
                contact Google to get access.
            enable_sentiment_analysis (bool):
                Enable sentiment analysis in conversation messages on `agent
                assist
                stage <https://cloud.google.com/dialogflow/priv/docs/contact-center/basics#stages>`__.
                If unspecified, defaults to false. Sentiment analysis
                inspects user input and identifies the prevailing subjective
                opinion, especially to determine a user's attitude as
                positive, negative, or neutral:
                https://cloud.google.com/natural-language/docs/basics#sentiment_analysis
                For
                [Participants.StreamingAnalyzeContent][google.cloud.dialogflow.v2beta1.Participants.StreamingAnalyzeContent]
                method, result will be in
                [StreamingAnalyzeContentResponse.message.SentimentAnalysisResult][google.cloud.dialogflow.v2beta1.StreamingAnalyzeContentResponse.message].
                For
                [Participants.AnalyzeContent][google.cloud.dialogflow.v2beta1.Participants.AnalyzeContent]
                method, result will be in
                [AnalyzeContentResponse.message.SentimentAnalysisResult][google.cloud.dialogflow.v2beta1.AnalyzeContentResponse.message]
                For
                [Conversations.ListMessages][google.cloud.dialogflow.v2beta1.Conversations.ListMessages]
                method, result will be in
                [ListMessagesResponse.messages.SentimentAnalysisResult][google.cloud.dialogflow.v2beta1.ListMessagesResponse.messages]
                If Pub/Sub notification is configured, result will be in
                [ConversationEvent.new_message_payload.SentimentAnalysisResult][google.cloud.dialogflow.v2beta1.ConversationEvent.new_message_payload].
            enable_sentiment_analysis_v3 (bool):
                Optional. Enables sentiment analysis for audio input and
                conversation messages. If unspecified, defaults to false. If
                this flag is set to true, other 'enable_sentiment_analysis'
                fields will be ignored.

                Sentiment analysis inspects user input and identifies the
                prevailing subjective opinion, especially to determine a
                user's attitude as positive, negative, or neutral.
                https://cloud.google.com/natural-language/docs/basics#sentiment_analysis
                For
                [Participants.StreamingAnalyzeContent][google.cloud.dialogflow.v2beta1.Participants.StreamingAnalyzeContent]
                method, result will be in
                [StreamingAnalyzeContentResponse.message.SentimentAnalysisResult][google.cloud.dialogflow.v2beta1.StreamingAnalyzeContentResponse.message].
                For
                [Participants.AnalyzeContent][google.cloud.dialogflow.v2beta1.Participants.AnalyzeContent]
                method, result will be in
                [AnalyzeContentResponse.message.SentimentAnalysisResult][google.cloud.dialogflow.v2beta1.AnalyzeContentResponse.message]
                For
                [Conversations.ListMessages][google.cloud.dialogflow.v2beta1.Conversations.ListMessages]
                method, result will be in
                [ListMessagesResponse.messages.SentimentAnalysisResult][google.cloud.dialogflow.v2beta1.ListMessagesResponse.messages]
                If Pub/Sub notification is configured, result will be in
                [ConversationEvent.new_message_payload.SentimentAnalysisResult][google.cloud.dialogflow.v2beta1.ConversationEvent.new_message_payload].
        """

        enable_entity_extraction: bool = proto.Field(
            proto.BOOL,
            number=2,
        )
        enable_sentiment_analysis: bool = proto.Field(
            proto.BOOL,
            number=3,
        )
        enable_sentiment_analysis_v3: bool = proto.Field(
            proto.BOOL,
            number=5,
        )

    notification_config: "NotificationConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="NotificationConfig",
    )
    human_agent_suggestion_config: SuggestionConfig = proto.Field(
        proto.MESSAGE,
        number=3,
        message=SuggestionConfig,
    )
    end_user_suggestion_config: SuggestionConfig = proto.Field(
        proto.MESSAGE,
        number=4,
        message=SuggestionConfig,
    )
    message_analysis_config: MessageAnalysisConfig = proto.Field(
        proto.MESSAGE,
        number=5,
        message=MessageAnalysisConfig,
    )


class HumanAgentHandoffConfig(proto.Message):
    r"""Defines the hand off to a live agent, typically on which
    external agent service provider to connect to a conversation.

    Currently, this feature is not general available, please contact
    Google to get access.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        live_person_config (google.cloud.dialogflow_v2beta1.types.HumanAgentHandoffConfig.LivePersonConfig):
            Uses `LivePerson <https://www.liveperson.com>`__.

            This field is a member of `oneof`_ ``agent_service``.
        salesforce_live_agent_config (google.cloud.dialogflow_v2beta1.types.HumanAgentHandoffConfig.SalesforceLiveAgentConfig):
            Uses Salesforce Live Agent.

            This field is a member of `oneof`_ ``agent_service``.
    """

    class LivePersonConfig(proto.Message):
        r"""Configuration specific to
        `LivePerson <https://www.liveperson.com>`__.

        Attributes:
            account_number (str):
                Required. Account number of the LivePerson
                account to connect. This is the account number
                you input at the login page.
        """

        account_number: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class SalesforceLiveAgentConfig(proto.Message):
        r"""Configuration specific to Salesforce Live Agent.

        Attributes:
            organization_id (str):
                Required. The organization ID of the
                Salesforce account.
            deployment_id (str):
                Required. Live Agent deployment ID.
            button_id (str):
                Required. Live Agent chat button ID.
            endpoint_domain (str):
                Required. Domain of the Live Agent endpoint for this agent.
                You can find the endpoint URL in the ``Live Agent settings``
                page. For example if URL has the form
                https://d.la4-c2-phx.salesforceliveagent.com/..., you should
                fill in d.la4-c2-phx.salesforceliveagent.com.
        """

        organization_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        deployment_id: str = proto.Field(
            proto.STRING,
            number=2,
        )
        button_id: str = proto.Field(
            proto.STRING,
            number=3,
        )
        endpoint_domain: str = proto.Field(
            proto.STRING,
            number=4,
        )

    live_person_config: LivePersonConfig = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="agent_service",
        message=LivePersonConfig,
    )
    salesforce_live_agent_config: SalesforceLiveAgentConfig = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="agent_service",
        message=SalesforceLiveAgentConfig,
    )


class NotificationConfig(proto.Message):
    r"""Defines notification behavior.

    Attributes:
        topic (str):
            Name of the Pub/Sub topic to publish conversation events
            like
            [CONVERSATION_STARTED][google.cloud.dialogflow.v2beta1.ConversationEvent.Type.CONVERSATION_STARTED]
            as serialized
            [ConversationEvent][google.cloud.dialogflow.v2beta1.ConversationEvent]
            protos.

            For telephony integration to receive notification, make sure
            either this topic is in the same project as the conversation
            or you grant
            ``service-<Conversation Project Number>@gcp-sa-dialogflow.iam.gserviceaccount.com``
            the ``Dialogflow Service Agent`` role in the topic project.

            For chat integration to receive notification, make sure API
            caller has been granted the ``Dialogflow Service Agent``
            role for the topic.

            Format:
            ``projects/<Project ID>/locations/<Location ID>/topics/<Topic ID>``.
        message_format (google.cloud.dialogflow_v2beta1.types.NotificationConfig.MessageFormat):
            Format of message.
    """

    class MessageFormat(proto.Enum):
        r"""Format of cloud pub/sub message.

        Values:
            MESSAGE_FORMAT_UNSPECIFIED (0):
                If it is unspecified, PROTO will be used.
            PROTO (1):
                Pub/Sub message will be serialized proto.
            JSON (2):
                Pub/Sub message will be json.
        """

        MESSAGE_FORMAT_UNSPECIFIED = 0
        PROTO = 1
        JSON = 2

    topic: str = proto.Field(
        proto.STRING,
        number=1,
    )
    message_format: MessageFormat = proto.Field(
        proto.ENUM,
        number=2,
        enum=MessageFormat,
    )


class LoggingConfig(proto.Message):
    r"""Defines logging behavior for conversation lifecycle events.

    Attributes:
        enable_stackdriver_logging (bool):
            Whether to log conversation events like
            [CONVERSATION_STARTED][google.cloud.dialogflow.v2beta1.ConversationEvent.Type.CONVERSATION_STARTED]
            to Stackdriver in the conversation project as JSON format
            [ConversationEvent][google.cloud.dialogflow.v2beta1.ConversationEvent]
            protos.
    """

    enable_stackdriver_logging: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class SipConfig(proto.Message):
    r"""Defines the SIP configuration.

    Attributes:
        create_conversation_on_the_fly (bool):
            Asks Dialogflow Telephony to create the
            conversation provided in the SIP header on the
            fly when the call comes in.
        inactive_start (bool):
            Starts the conversation with inactive SDP
            directives
        max_audio_recording_duration (google.protobuf.duration_pb2.Duration):
            Max duration for audio recording.
            Overrides the default value of 15 min.
            Max value is 8 hours.
        allow_virtual_agent_interaction (bool):
            Allows interactions with a Dialogflow virtual
            agent even if the call is connected for SIPREC
            purposes.
        keep_conversation_running (bool):
            Keeps the conversation running even if the
            call is disconnected.
        copy_inbound_call_leg_headers (MutableSequence[str]):
            List of inbound call leg headers to be copied
            to outbound call legs created later.
        ignore_reinvite_media_direction (bool):
            Ignores any media direction in the reINVITE
            SDP offer. Reuse the previous media direction.
    """

    create_conversation_on_the_fly: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    inactive_start: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    max_audio_recording_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=4,
        message=duration_pb2.Duration,
    )
    allow_virtual_agent_interaction: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    keep_conversation_running: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    copy_inbound_call_leg_headers: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    ignore_reinvite_media_direction: bool = proto.Field(
        proto.BOOL,
        number=9,
    )


class ListConversationProfilesRequest(proto.Message):
    r"""The request message for
    [ConversationProfiles.ListConversationProfiles][google.cloud.dialogflow.v2beta1.ConversationProfiles.ListConversationProfiles].

    Attributes:
        parent (str):
            Required. The project to list all conversation profiles
            from. Format:
            ``projects/<Project ID>/locations/<Location ID>``.
        page_size (int):
            The maximum number of items to return in a
            single page. By default 100 and at most 1000.
        page_token (str):
            The next_page_token value returned from a previous list
            request.
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


class ListConversationProfilesResponse(proto.Message):
    r"""The response message for
    [ConversationProfiles.ListConversationProfiles][google.cloud.dialogflow.v2beta1.ConversationProfiles.ListConversationProfiles].

    Attributes:
        conversation_profiles (MutableSequence[google.cloud.dialogflow_v2beta1.types.ConversationProfile]):
            The list of project conversation profiles. There is a
            maximum number of items returned based on the page_size
            field in the request.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    conversation_profiles: MutableSequence["ConversationProfile"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ConversationProfile",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetConversationProfileRequest(proto.Message):
    r"""The request message for
    [ConversationProfiles.GetConversationProfile][google.cloud.dialogflow.v2beta1.ConversationProfiles.GetConversationProfile].

    Attributes:
        name (str):
            Required. The resource name of the conversation profile.
            Format:
            ``projects/<Project ID>/locations/<Location ID>/conversationProfiles/<Conversation Profile ID>``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateConversationProfileRequest(proto.Message):
    r"""The request message for
    [ConversationProfiles.CreateConversationProfile][google.cloud.dialogflow.v2beta1.ConversationProfiles.CreateConversationProfile].

    Attributes:
        parent (str):
            Required. The project to create a conversation profile for.
            Format: ``projects/<Project ID>/locations/<Location ID>``.
        conversation_profile (google.cloud.dialogflow_v2beta1.types.ConversationProfile):
            Required. The conversation profile to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    conversation_profile: "ConversationProfile" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ConversationProfile",
    )


class UpdateConversationProfileRequest(proto.Message):
    r"""The request message for
    [ConversationProfiles.UpdateConversationProfile][google.cloud.dialogflow.v2beta1.ConversationProfiles.UpdateConversationProfile].

    Attributes:
        conversation_profile (google.cloud.dialogflow_v2beta1.types.ConversationProfile):
            Required. The conversation profile to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The mask to control which fields to
            update.
    """

    conversation_profile: "ConversationProfile" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ConversationProfile",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteConversationProfileRequest(proto.Message):
    r"""The request message for
    [ConversationProfiles.DeleteConversationProfile][google.cloud.dialogflow.v2beta1.ConversationProfiles.DeleteConversationProfile].

    This operation fails if the conversation profile is still referenced
    from a phone number.

    Attributes:
        name (str):
            Required. The name of the conversation profile to delete.
            Format:
            ``projects/<Project ID>/locations/<Location ID>/conversationProfiles/<Conversation Profile ID>``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class SetSuggestionFeatureConfigRequest(proto.Message):
    r"""The request message for
    [ConversationProfiles.SetSuggestionFeature][].

    Attributes:
        conversation_profile (str):
            Required. The Conversation Profile to add or update the
            suggestion feature config. Format:
            ``projects/<Project ID>/locations/<Location ID>/conversationProfiles/<Conversation Profile ID>``.
        participant_role (google.cloud.dialogflow_v2beta1.types.Participant.Role):
            Required. The participant role to add or update the
            suggestion feature config. Only HUMAN_AGENT or END_USER can
            be used.
        suggestion_feature_config (google.cloud.dialogflow_v2beta1.types.HumanAgentAssistantConfig.SuggestionFeatureConfig):
            Required. The suggestion feature config to
            add or update.
    """

    conversation_profile: str = proto.Field(
        proto.STRING,
        number=1,
    )
    participant_role: participant.Participant.Role = proto.Field(
        proto.ENUM,
        number=2,
        enum=participant.Participant.Role,
    )
    suggestion_feature_config: "HumanAgentAssistantConfig.SuggestionFeatureConfig" = (
        proto.Field(
            proto.MESSAGE,
            number=3,
            message="HumanAgentAssistantConfig.SuggestionFeatureConfig",
        )
    )


class ClearSuggestionFeatureConfigRequest(proto.Message):
    r"""The request message for [ConversationProfiles.ClearFeature][].

    Attributes:
        conversation_profile (str):
            Required. The Conversation Profile to add or update the
            suggestion feature config. Format:
            ``projects/<Project ID>/locations/<Location ID>/conversationProfiles/<Conversation Profile ID>``.
        participant_role (google.cloud.dialogflow_v2beta1.types.Participant.Role):
            Required. The participant role to remove the suggestion
            feature config. Only HUMAN_AGENT or END_USER can be used.
        suggestion_feature_type (google.cloud.dialogflow_v2beta1.types.SuggestionFeature.Type):
            Required. The type of the suggestion feature
            to remove.
    """

    conversation_profile: str = proto.Field(
        proto.STRING,
        number=1,
    )
    participant_role: participant.Participant.Role = proto.Field(
        proto.ENUM,
        number=2,
        enum=participant.Participant.Role,
    )
    suggestion_feature_type: participant.SuggestionFeature.Type = proto.Field(
        proto.ENUM,
        number=3,
        enum=participant.SuggestionFeature.Type,
    )


class SetSuggestionFeatureConfigOperationMetadata(proto.Message):
    r"""Metadata for a [ConversationProfile.SetSuggestionFeatureConfig][]
    operation.

    Attributes:
        conversation_profile (str):
            The resource name of the conversation profile. Format:
            ``projects/<Project ID>/locations/<Location ID>/conversationProfiles/<Conversation Profile ID>``
        participant_role (google.cloud.dialogflow_v2beta1.types.Participant.Role):
            Required. The participant role to add or update the
            suggestion feature config. Only HUMAN_AGENT or END_USER can
            be used.
        suggestion_feature_type (google.cloud.dialogflow_v2beta1.types.SuggestionFeature.Type):
            Required. The type of the suggestion feature
            to add or update.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp whe the request was created. The
            time is measured on server side.
    """

    conversation_profile: str = proto.Field(
        proto.STRING,
        number=1,
    )
    participant_role: participant.Participant.Role = proto.Field(
        proto.ENUM,
        number=2,
        enum=participant.Participant.Role,
    )
    suggestion_feature_type: participant.SuggestionFeature.Type = proto.Field(
        proto.ENUM,
        number=3,
        enum=participant.SuggestionFeature.Type,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


class ClearSuggestionFeatureConfigOperationMetadata(proto.Message):
    r"""Metadata for a [ConversationProfile.ClearSuggestionFeatureConfig][]
    operation.

    Attributes:
        conversation_profile (str):
            The resource name of the conversation profile. Format:
            ``projects/<Project ID>/locations/<Location ID>/conversationProfiles/<Conversation Profile ID>``
        participant_role (google.cloud.dialogflow_v2beta1.types.Participant.Role):
            Required. The participant role to remove the suggestion
            feature config. Only HUMAN_AGENT or END_USER can be used.
        suggestion_feature_type (google.cloud.dialogflow_v2beta1.types.SuggestionFeature.Type):
            Required. The type of the suggestion feature
            to remove.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp whe the request was created. The
            time is measured on server side.
    """

    conversation_profile: str = proto.Field(
        proto.STRING,
        number=1,
    )
    participant_role: participant.Participant.Role = proto.Field(
        proto.ENUM,
        number=2,
        enum=participant.Participant.Role,
    )
    suggestion_feature_type: participant.SuggestionFeature.Type = proto.Field(
        proto.ENUM,
        number=3,
        enum=participant.SuggestionFeature.Type,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
