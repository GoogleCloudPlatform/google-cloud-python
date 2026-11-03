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

__protobuf__ = proto.module(
    package="google.cloud.contactcenterinsights.v1",
    manifest={
        "DatasetValidationWarning",
        "Conversation",
        "Analysis",
        "ConversationDataSource",
        "GcsSource",
        "DialogflowSource",
        "AnalysisResult",
        "IssueModelResult",
        "FeedbackLabel",
        "ConversationLevelSentiment",
        "ConversationLevelSilence",
        "IssueAssignment",
        "CallAnnotation",
        "AnnotationBoundary",
        "Entity",
        "Intent",
        "PhraseMatchData",
        "DialogflowIntent",
        "InterruptionData",
        "SilenceData",
        "HoldData",
        "EntityMentionData",
        "IntentMatchData",
        "SentimentData",
        "IssueMatchData",
        "IssueModel",
        "Issue",
        "IssueModelLabelStats",
        "PhraseMatcher",
        "PhraseMatchRuleGroup",
        "PhraseMatchRule",
        "PhraseMatchRuleConfig",
        "ExactMatchConfig",
        "Settings",
        "AnalysisRule",
        "EncryptionSpec",
        "RedactionConfig",
        "SpeechConfig",
        "RuntimeAnnotation",
        "AnswerFeedback",
        "ArticleSuggestionData",
        "FaqAnswerData",
        "SmartReplyData",
        "SmartComposeSuggestionData",
        "DialogflowInteractionData",
        "ConversationSummarizationSuggestionData",
        "ConversationParticipant",
        "View",
        "AnnotatorSelector",
        "QaQuestion",
        "QaScorecard",
        "QaScorecardRevision",
        "QaAnswer",
        "QaScorecardResult",
    },
)


class DatasetValidationWarning(proto.Enum):
    r"""Enum for the different types of issues a tuning dataset can
    have. These warnings are currentlyraised when trying to validate
    a dataset for tuning a scorecard.

    Values:
        DATASET_VALIDATION_WARNING_UNSPECIFIED (0):
            Unspecified data validation warning.
        TOO_MANY_INVALID_FEEDBACK_LABELS (1):
            A non-trivial percentage of the feedback
            labels are invalid.
        INSUFFICIENT_FEEDBACK_LABELS (2):
            The quantity of valid feedback labels
            provided is less than the recommended minimum.
        INSUFFICIENT_FEEDBACK_LABELS_PER_ANSWER (3):
            One or more of the answers have less than the
            recommended minimum of feedback labels.
        ALL_FEEDBACK_LABELS_HAVE_THE_SAME_ANSWER (4):
            All the labels in the dataset come from a
            single answer choice.
    """

    DATASET_VALIDATION_WARNING_UNSPECIFIED = 0
    TOO_MANY_INVALID_FEEDBACK_LABELS = 1
    INSUFFICIENT_FEEDBACK_LABELS = 2
    INSUFFICIENT_FEEDBACK_LABELS_PER_ANSWER = 3
    ALL_FEEDBACK_LABELS_HAVE_THE_SAME_ANSWER = 4


class Conversation(proto.Message):
    r"""The conversation resource.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        call_metadata (google.cloud.contact_center_insights_v1.types.Conversation.CallMetadata):
            Call-specific metadata.

            This field is a member of `oneof`_ ``metadata``.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            The time at which this conversation should
            expire. After this time, the conversation data
            and any associated analyses will be deleted.

            This field is a member of `oneof`_ ``expiration``.
        ttl (google.protobuf.duration_pb2.Duration):
            Input only. The TTL for this resource. If
            specified, then this TTL will be used to
            calculate the expire time.

            This field is a member of `oneof`_ ``expiration``.
        name (str):
            Immutable. The resource name of the
            conversation. Format:

            projects/{project}/locations/{location}/conversations/{conversation}
        data_source (google.cloud.contact_center_insights_v1.types.ConversationDataSource):
            The source of the audio and transcription for
            the conversation.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the
            conversation was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The most recent time at which
            the conversation was updated.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            The time at which the conversation started.
        language_code (str):
            A user-specified language code for the
            conversation.
        agent_id (str):
            An opaque, user-specified string representing
            the human agent who handled the conversation.
        labels (MutableMapping[str, str]):
            A map for the user to specify any custom
            fields. A maximum of 100 labels per conversation
            is allowed, with a maximum of 256 characters per
            entry.
        quality_metadata (google.cloud.contact_center_insights_v1.types.Conversation.QualityMetadata):
            Conversation metadata related to quality
            management.
        metadata_json (str):
            Input only. JSON metadata encoded as a
            string. This field is primarily used by Insights
            integrations with various telphony systems and
            must be in one of Insight's supported formats.
        transcript (google.cloud.contact_center_insights_v1.types.Conversation.Transcript):
            Output only. The conversation transcript.
        medium (google.cloud.contact_center_insights_v1.types.Conversation.Medium):
            Immutable. The conversation medium, if unspecified will
            default to PHONE_CALL.
        duration (google.protobuf.duration_pb2.Duration):
            Output only. The duration of the
            conversation.
        turn_count (int):
            Output only. The number of turns in the
            conversation.
        latest_analysis (google.cloud.contact_center_insights_v1.types.Analysis):
            Output only. The conversation's latest
            analysis, if one exists.
        latest_summary (google.cloud.contact_center_insights_v1.types.ConversationSummarizationSuggestionData):
            Output only. Latest summary of the
            conversation.
        runtime_annotations (MutableSequence[google.cloud.contact_center_insights_v1.types.RuntimeAnnotation]):
            Output only. The annotations that were
            generated during the customer and agent
            interaction.
        dialogflow_intents (MutableMapping[str, google.cloud.contact_center_insights_v1.types.DialogflowIntent]):
            Output only. All the matched Dialogflow
            intents in the call. The key corresponds to a
            Dialogflow intent, format:

            projects/{project}/agent/{agent}/intents/{intent}
        obfuscated_user_id (str):
            Obfuscated user ID which the customer sent to
            us.
    """

    class Medium(proto.Enum):
        r"""Possible media for the conversation.

        Values:
            MEDIUM_UNSPECIFIED (0):
                Default value, if unspecified will default to PHONE_CALL.
            PHONE_CALL (1):
                The format for conversations that took place
                over the phone.
            CHAT (2):
                The format for conversations that took place
                over chat.
        """

        MEDIUM_UNSPECIFIED = 0
        PHONE_CALL = 1
        CHAT = 2

    class CallMetadata(proto.Message):
        r"""Call-specific metadata.

        Attributes:
            customer_channel (int):
                The audio channel that contains the customer.
            agent_channel (int):
                The audio channel that contains the agent.
        """

        customer_channel: int = proto.Field(
            proto.INT32,
            number=1,
        )
        agent_channel: int = proto.Field(
            proto.INT32,
            number=2,
        )

    class QualityMetadata(proto.Message):
        r"""Conversation metadata related to quality management.

        Attributes:
            customer_satisfaction_rating (int):
                An arbitrary integer value indicating the
                customer's satisfaction rating.
            wait_duration (google.protobuf.duration_pb2.Duration):
                The amount of time the customer waited to
                connect with an agent.
            menu_path (str):
                An arbitrary string value specifying the menu
                path the customer took.
            agent_info (MutableSequence[google.cloud.contact_center_insights_v1.types.Conversation.QualityMetadata.AgentInfo]):
                Information about agents involved in the
                call.
        """

        class AgentInfo(proto.Message):
            r"""Information about an agent involved in the conversation.

            Attributes:
                agent_id (str):
                    A user-specified string representing the
                    agent.
                display_name (str):
                    The agent's name.
                team (str):
                    A user-specified string representing the agent's team.
                    Deprecated in favor of the ``teams`` field.
                teams (MutableSequence[str]):
                    User-specified strings representing the
                    agent's teams.
                disposition_code (str):
                    A user-provided string indicating the outcome
                    of the agent's segment of the call.
                agent_type (google.cloud.contact_center_insights_v1.types.ConversationParticipant.Role):
                    The agent type, e.g. HUMAN_AGENT.
                location (str):
                    The agent's location.
                deployment_id (str):
                    The agent's deployment ID. Only applicable to
                    automated agents.
                deployment_display_name (str):
                    The agent's deployment display name. Only
                    applicable to automated agents.
                version_id (str):
                    The agent's version ID. Only applicable to
                    automated agents.
                version_display_name (str):
                    The agent's version display name. Only
                    applicable to automated agents.
                entry_subagent_display_name (str):
                    The entry subagent's display name.
                entry_subagent_id (str):
                    The entry subagent's ID.
            """

            agent_id: str = proto.Field(
                proto.STRING,
                number=1,
            )
            display_name: str = proto.Field(
                proto.STRING,
                number=2,
            )
            team: str = proto.Field(
                proto.STRING,
                number=3,
            )
            teams: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=6,
            )
            disposition_code: str = proto.Field(
                proto.STRING,
                number=4,
            )
            agent_type: "ConversationParticipant.Role" = proto.Field(
                proto.ENUM,
                number=5,
                enum="ConversationParticipant.Role",
            )
            location: str = proto.Field(
                proto.STRING,
                number=7,
            )
            deployment_id: str = proto.Field(
                proto.STRING,
                number=8,
            )
            deployment_display_name: str = proto.Field(
                proto.STRING,
                number=9,
            )
            version_id: str = proto.Field(
                proto.STRING,
                number=10,
            )
            version_display_name: str = proto.Field(
                proto.STRING,
                number=11,
            )
            entry_subagent_display_name: str = proto.Field(
                proto.STRING,
                number=12,
            )
            entry_subagent_id: str = proto.Field(
                proto.STRING,
                number=13,
            )

        customer_satisfaction_rating: int = proto.Field(
            proto.INT32,
            number=1,
        )
        wait_duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=2,
            message=duration_pb2.Duration,
        )
        menu_path: str = proto.Field(
            proto.STRING,
            number=3,
        )
        agent_info: MutableSequence["Conversation.QualityMetadata.AgentInfo"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=4,
                message="Conversation.QualityMetadata.AgentInfo",
            )
        )

    class Transcript(proto.Message):
        r"""A message representing the transcript of a conversation.

        Attributes:
            transcript_segments (MutableSequence[google.cloud.contact_center_insights_v1.types.Conversation.Transcript.TranscriptSegment]):
                A list of sequential transcript segments that
                comprise the conversation.
        """

        class TranscriptSegment(proto.Message):
            r"""A segment of a full transcript.

            Attributes:
                message_time (google.protobuf.timestamp_pb2.Timestamp):
                    The time that the message occurred, if
                    provided.
                text (str):
                    The text of this segment.
                confidence (float):
                    A confidence estimate between 0.0 and 1.0 of
                    the fidelity of this segment. A default value of
                    0.0 indicates that the value is unset.
                words (MutableSequence[google.cloud.contact_center_insights_v1.types.Conversation.Transcript.TranscriptSegment.WordInfo]):
                    A list of the word-specific information for
                    each word in the segment.
                language_code (str):
                    The language code of this segment as a
                    `BCP-47 <https://www.rfc-editor.org/rfc/bcp/bcp47.txt>`__
                    language tag. Example: "en-US".
                channel_tag (int):
                    For conversations derived from multi-channel
                    audio, this is the channel number corresponding
                    to the audio from that channel. For
                    audioChannelCount = N, its output values can
                    range from '1' to 'N'. A channel tag of 0
                    indicates that the audio is mono.
                segment_participant (google.cloud.contact_center_insights_v1.types.ConversationParticipant):
                    The participant of this segment.
                dialogflow_segment_metadata (google.cloud.contact_center_insights_v1.types.Conversation.Transcript.TranscriptSegment.DialogflowSegmentMetadata):
                    CCAI metadata relating to the current
                    transcript segment.
                sentiment (google.cloud.contact_center_insights_v1.types.SentimentData):
                    The sentiment for this transcript segment.
            """

            class WordInfo(proto.Message):
                r"""Word-level info for words in a transcript.

                Attributes:
                    start_offset (google.protobuf.duration_pb2.Duration):
                        Time offset of the start of this word
                        relative to the beginning of the total
                        conversation.
                    end_offset (google.protobuf.duration_pb2.Duration):
                        Time offset of the end of this word relative
                        to the beginning of the total conversation.
                    word (str):
                        The word itself. Includes punctuation marks
                        that surround the word.
                    confidence (float):
                        A confidence estimate between 0.0 and 1.0 of
                        the fidelity of this word. A default value of
                        0.0 indicates that the value is unset.
                """

                start_offset: duration_pb2.Duration = proto.Field(
                    proto.MESSAGE,
                    number=1,
                    message=duration_pb2.Duration,
                )
                end_offset: duration_pb2.Duration = proto.Field(
                    proto.MESSAGE,
                    number=2,
                    message=duration_pb2.Duration,
                )
                word: str = proto.Field(
                    proto.STRING,
                    number=3,
                )
                confidence: float = proto.Field(
                    proto.FLOAT,
                    number=4,
                )

            class DialogflowSegmentMetadata(proto.Message):
                r"""Metadata from Dialogflow relating to the current transcript
                segment.

                Attributes:
                    smart_reply_allowlist_covered (bool):
                        Whether the transcript segment was covered
                        under the configured smart reply allowlist in
                        Agent Assist.
                """

                smart_reply_allowlist_covered: bool = proto.Field(
                    proto.BOOL,
                    number=1,
                )

            message_time: timestamp_pb2.Timestamp = proto.Field(
                proto.MESSAGE,
                number=6,
                message=timestamp_pb2.Timestamp,
            )
            text: str = proto.Field(
                proto.STRING,
                number=1,
            )
            confidence: float = proto.Field(
                proto.FLOAT,
                number=2,
            )
            words: MutableSequence[
                "Conversation.Transcript.TranscriptSegment.WordInfo"
            ] = proto.RepeatedField(
                proto.MESSAGE,
                number=3,
                message="Conversation.Transcript.TranscriptSegment.WordInfo",
            )
            language_code: str = proto.Field(
                proto.STRING,
                number=4,
            )
            channel_tag: int = proto.Field(
                proto.INT32,
                number=5,
            )
            segment_participant: "ConversationParticipant" = proto.Field(
                proto.MESSAGE,
                number=9,
                message="ConversationParticipant",
            )
            dialogflow_segment_metadata: "Conversation.Transcript.TranscriptSegment.DialogflowSegmentMetadata" = proto.Field(
                proto.MESSAGE,
                number=10,
                message="Conversation.Transcript.TranscriptSegment.DialogflowSegmentMetadata",
            )
            sentiment: "SentimentData" = proto.Field(
                proto.MESSAGE,
                number=11,
                message="SentimentData",
            )

        transcript_segments: MutableSequence[
            "Conversation.Transcript.TranscriptSegment"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="Conversation.Transcript.TranscriptSegment",
        )

    call_metadata: CallMetadata = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="metadata",
        message=CallMetadata,
    )
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=15,
        oneof="expiration",
        message=timestamp_pb2.Timestamp,
    )
    ttl: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=16,
        oneof="expiration",
        message=duration_pb2.Duration,
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_source: "ConversationDataSource" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ConversationDataSource",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=17,
        message=timestamp_pb2.Timestamp,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=14,
    )
    agent_id: str = proto.Field(
        proto.STRING,
        number=5,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    quality_metadata: QualityMetadata = proto.Field(
        proto.MESSAGE,
        number=24,
        message=QualityMetadata,
    )
    metadata_json: str = proto.Field(
        proto.STRING,
        number=25,
    )
    transcript: Transcript = proto.Field(
        proto.MESSAGE,
        number=8,
        message=Transcript,
    )
    medium: Medium = proto.Field(
        proto.ENUM,
        number=9,
        enum=Medium,
    )
    duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=10,
        message=duration_pb2.Duration,
    )
    turn_count: int = proto.Field(
        proto.INT32,
        number=11,
    )
    latest_analysis: "Analysis" = proto.Field(
        proto.MESSAGE,
        number=12,
        message="Analysis",
    )
    latest_summary: "ConversationSummarizationSuggestionData" = proto.Field(
        proto.MESSAGE,
        number=20,
        message="ConversationSummarizationSuggestionData",
    )
    runtime_annotations: MutableSequence["RuntimeAnnotation"] = proto.RepeatedField(
        proto.MESSAGE,
        number=13,
        message="RuntimeAnnotation",
    )
    dialogflow_intents: MutableMapping[str, "DialogflowIntent"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=18,
        message="DialogflowIntent",
    )
    obfuscated_user_id: str = proto.Field(
        proto.STRING,
        number=21,
    )


class Analysis(proto.Message):
    r"""The analysis resource.

    Attributes:
        name (str):
            Immutable. The resource name of the analysis.
            Format:

            projects/{project}/locations/{location}/conversations/{conversation}/analyses/{analysis}
        request_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the analysis
            was requested.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the analysis
            was created, which occurs when the long-running
            operation completes.
        analysis_result (google.cloud.contact_center_insights_v1.types.AnalysisResult):
            Output only. The result of the analysis,
            which is populated when the analysis finishes.
        annotator_selector (google.cloud.contact_center_insights_v1.types.AnnotatorSelector):
            To select the annotators to run and the
            phrase matchers to use (if any). If not
            specified, all annotators will be run.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    analysis_result: "AnalysisResult" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="AnalysisResult",
    )
    annotator_selector: "AnnotatorSelector" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="AnnotatorSelector",
    )


class ConversationDataSource(proto.Message):
    r"""The conversation source, which is a combination of transcript
    and audio.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_source (google.cloud.contact_center_insights_v1.types.GcsSource):
            A Cloud Storage location specification for
            the audio and transcript.

            This field is a member of `oneof`_ ``source``.
        dialogflow_source (google.cloud.contact_center_insights_v1.types.DialogflowSource):
            The source when the conversation comes from
            Dialogflow.

            This field is a member of `oneof`_ ``source``.
    """

    gcs_source: "GcsSource" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="source",
        message="GcsSource",
    )
    dialogflow_source: "DialogflowSource" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="source",
        message="DialogflowSource",
    )


class GcsSource(proto.Message):
    r"""A Cloud Storage source of conversation data.

    Attributes:
        audio_uri (str):
            Cloud Storage URI that points to a file that
            contains the conversation audio.
        transcript_uri (str):
            Immutable. Cloud Storage URI that points to a
            file that contains the conversation transcript.
    """

    audio_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    transcript_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DialogflowSource(proto.Message):
    r"""A Dialogflow source of conversation data.

    Attributes:
        dialogflow_conversation (str):
            Output only. The name of the Dialogflow
            conversation that this conversation resource is
            derived from. Format:

            projects/{project}/locations/{location}/conversations/{conversation}
        audio_uri (str):
            Cloud Storage URI that points to a file that
            contains the conversation audio.
    """

    dialogflow_conversation: str = proto.Field(
        proto.STRING,
        number=1,
    )
    audio_uri: str = proto.Field(
        proto.STRING,
        number=3,
    )


class AnalysisResult(proto.Message):
    r"""The result of an analysis.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        call_analysis_metadata (google.cloud.contact_center_insights_v1.types.AnalysisResult.CallAnalysisMetadata):
            Call-specific metadata created by the
            analysis.

            This field is a member of `oneof`_ ``metadata``.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            The time at which the analysis ended.
    """

    class CallAnalysisMetadata(proto.Message):
        r"""Call-specific metadata created during analysis.

        Attributes:
            annotations (MutableSequence[google.cloud.contact_center_insights_v1.types.CallAnnotation]):
                A list of call annotations that apply to this
                call.
            entities (MutableMapping[str, google.cloud.contact_center_insights_v1.types.Entity]):
                All the entities in the call.
            sentiments (MutableSequence[google.cloud.contact_center_insights_v1.types.ConversationLevelSentiment]):
                Overall conversation-level sentiment for each
                channel of the call.
            silence (google.cloud.contact_center_insights_v1.types.ConversationLevelSilence):
                Overall conversation-level silence during the
                call.
            intents (MutableMapping[str, google.cloud.contact_center_insights_v1.types.Intent]):
                All the matched intents in the call.
            phrase_matchers (MutableMapping[str, google.cloud.contact_center_insights_v1.types.PhraseMatchData]):
                All the matched phrase matchers in the call.
            issue_model_result (google.cloud.contact_center_insights_v1.types.IssueModelResult):
                Overall conversation-level issue modeling
                result.
            qa_scorecard_results (MutableSequence[google.cloud.contact_center_insights_v1.types.QaScorecardResult]):
                Results of scoring QaScorecards.
        """

        annotations: MutableSequence["CallAnnotation"] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="CallAnnotation",
        )
        entities: MutableMapping[str, "Entity"] = proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=3,
            message="Entity",
        )
        sentiments: MutableSequence["ConversationLevelSentiment"] = proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message="ConversationLevelSentiment",
        )
        silence: "ConversationLevelSilence" = proto.Field(
            proto.MESSAGE,
            number=11,
            message="ConversationLevelSilence",
        )
        intents: MutableMapping[str, "Intent"] = proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=6,
            message="Intent",
        )
        phrase_matchers: MutableMapping[str, "PhraseMatchData"] = proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=7,
            message="PhraseMatchData",
        )
        issue_model_result: "IssueModelResult" = proto.Field(
            proto.MESSAGE,
            number=8,
            message="IssueModelResult",
        )
        qa_scorecard_results: MutableSequence["QaScorecardResult"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=10,
                message="QaScorecardResult",
            )
        )

    call_analysis_metadata: CallAnalysisMetadata = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="metadata",
        message=CallAnalysisMetadata,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )


class IssueModelResult(proto.Message):
    r"""Issue Modeling result on a conversation.

    Attributes:
        issue_model (str):
            Issue model that generates the result. Format:
            projects/{project}/locations/{location}/issueModels/{issue_model}
        issues (MutableSequence[google.cloud.contact_center_insights_v1.types.IssueAssignment]):
            All the matched issues.
    """

    issue_model: str = proto.Field(
        proto.STRING,
        number=1,
    )
    issues: MutableSequence["IssueAssignment"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="IssueAssignment",
    )


class FeedbackLabel(proto.Message):
    r"""Represents a conversation, resource, and label provided by
    the user.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        label (str):
            String label.

            This field is a member of `oneof`_ ``label_type``.
        qa_answer_label (google.cloud.contact_center_insights_v1.types.QaAnswer.AnswerValue):
            QaAnswer label.

            This field is a member of `oneof`_ ``label_type``.
        name (str):
            Immutable. Resource name of the FeedbackLabel. Format:
            projects/{project}/locations/{location}/conversations/{conversation}/feedbackLabels/{feedback_label}
        labeled_resource (str):
            Resource name of the resource to be labeled.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create time of the label.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Update time of the label.
    """

    label: str = proto.Field(
        proto.STRING,
        number=4,
        oneof="label_type",
    )
    qa_answer_label: "QaAnswer.AnswerValue" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="label_type",
        message="QaAnswer.AnswerValue",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    labeled_resource: str = proto.Field(
        proto.STRING,
        number=3,
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


class ConversationLevelSentiment(proto.Message):
    r"""One channel of conversation-level sentiment data.

    Attributes:
        channel_tag (int):
            The channel of the audio that the data
            applies to.
        sentiment_data (google.cloud.contact_center_insights_v1.types.SentimentData):
            Data specifying sentiment.
    """

    channel_tag: int = proto.Field(
        proto.INT32,
        number=1,
    )
    sentiment_data: "SentimentData" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="SentimentData",
    )


class ConversationLevelSilence(proto.Message):
    r"""Conversation-level silence data.

    Attributes:
        silence_duration (google.protobuf.duration_pb2.Duration):
            Amount of time calculated to be in silence.
        silence_percentage (float):
            Percentage of the total conversation spent in
            silence.
    """

    silence_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=1,
        message=duration_pb2.Duration,
    )
    silence_percentage: float = proto.Field(
        proto.FLOAT,
        number=2,
    )


class IssueAssignment(proto.Message):
    r"""Information about the issue.

    Attributes:
        issue (str):
            Resource name of the assigned issue.
        score (float):
            Score indicating the likelihood of the issue assignment.
            currently bounded on [0,1].
        display_name (str):
            Immutable. Display name of the assigned
            issue. This field is set at time of analyis and
            immutable since then.
    """

    issue: str = proto.Field(
        proto.STRING,
        number=1,
    )
    score: float = proto.Field(
        proto.DOUBLE,
        number=2,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )


class CallAnnotation(proto.Message):
    r"""A piece of metadata that applies to a window of a call.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        interruption_data (google.cloud.contact_center_insights_v1.types.InterruptionData):
            Data specifying an interruption.

            This field is a member of `oneof`_ ``data``.
        sentiment_data (google.cloud.contact_center_insights_v1.types.SentimentData):
            Data specifying sentiment.

            This field is a member of `oneof`_ ``data``.
        silence_data (google.cloud.contact_center_insights_v1.types.SilenceData):
            Data specifying silence.

            This field is a member of `oneof`_ ``data``.
        hold_data (google.cloud.contact_center_insights_v1.types.HoldData):
            Data specifying a hold.

            This field is a member of `oneof`_ ``data``.
        entity_mention_data (google.cloud.contact_center_insights_v1.types.EntityMentionData):
            Data specifying an entity mention.

            This field is a member of `oneof`_ ``data``.
        intent_match_data (google.cloud.contact_center_insights_v1.types.IntentMatchData):
            Data specifying an intent match.

            This field is a member of `oneof`_ ``data``.
        phrase_match_data (google.cloud.contact_center_insights_v1.types.PhraseMatchData):
            Data specifying a phrase match.

            This field is a member of `oneof`_ ``data``.
        issue_match_data (google.cloud.contact_center_insights_v1.types.IssueMatchData):
            Data specifying an issue match.

            This field is a member of `oneof`_ ``data``.
        channel_tag (int):
            The channel of the audio where the annotation
            occurs. For single-channel audio, this field is
            not populated.
        annotation_start_boundary (google.cloud.contact_center_insights_v1.types.AnnotationBoundary):
            The boundary in the conversation where the
            annotation starts, inclusive.
        annotation_end_boundary (google.cloud.contact_center_insights_v1.types.AnnotationBoundary):
            The boundary in the conversation where the
            annotation ends, inclusive.
    """

    interruption_data: "InterruptionData" = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="data",
        message="InterruptionData",
    )
    sentiment_data: "SentimentData" = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="data",
        message="SentimentData",
    )
    silence_data: "SilenceData" = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="data",
        message="SilenceData",
    )
    hold_data: "HoldData" = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="data",
        message="HoldData",
    )
    entity_mention_data: "EntityMentionData" = proto.Field(
        proto.MESSAGE,
        number=15,
        oneof="data",
        message="EntityMentionData",
    )
    intent_match_data: "IntentMatchData" = proto.Field(
        proto.MESSAGE,
        number=16,
        oneof="data",
        message="IntentMatchData",
    )
    phrase_match_data: "PhraseMatchData" = proto.Field(
        proto.MESSAGE,
        number=17,
        oneof="data",
        message="PhraseMatchData",
    )
    issue_match_data: "IssueMatchData" = proto.Field(
        proto.MESSAGE,
        number=18,
        oneof="data",
        message="IssueMatchData",
    )
    channel_tag: int = proto.Field(
        proto.INT32,
        number=1,
    )
    annotation_start_boundary: "AnnotationBoundary" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="AnnotationBoundary",
    )
    annotation_end_boundary: "AnnotationBoundary" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="AnnotationBoundary",
    )


class AnnotationBoundary(proto.Message):
    r"""A point in a conversation that marks the start or the end of
    an annotation.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        word_index (int):
            The word index of this boundary with respect
            to the first word in the transcript piece. This
            index starts at zero.

            This field is a member of `oneof`_ ``detailed_boundary``.
        transcript_index (int):
            The index in the sequence of transcribed
            pieces of the conversation where the boundary is
            located. This index starts at zero.
    """

    word_index: int = proto.Field(
        proto.INT32,
        number=3,
        oneof="detailed_boundary",
    )
    transcript_index: int = proto.Field(
        proto.INT32,
        number=1,
    )


class Entity(proto.Message):
    r"""The data for an entity annotation.
    Represents a phrase in the conversation that is a known entity,
    such as a person, an organization, or location.

    Attributes:
        display_name (str):
            The representative name for the entity.
        type_ (google.cloud.contact_center_insights_v1.types.Entity.Type):
            The entity type.
        metadata (MutableMapping[str, str]):
            Metadata associated with the entity.

            For most entity types, the metadata is a Wikipedia URL
            (``wikipedia_url``) and Knowledge Graph MID (``mid``), if
            they are available. For the metadata associated with other
            entity types, see the Type table below.
        salience (float):
            The salience score associated with the entity in the [0,
            1.0] range.

            The salience score for an entity provides information about
            the importance or centrality of that entity to the entire
            document text. Scores closer to 0 are less salient, while
            scores closer to 1.0 are highly salient.
        sentiment (google.cloud.contact_center_insights_v1.types.SentimentData):
            The aggregate sentiment expressed for this
            entity in the conversation.
    """

    class Type(proto.Enum):
        r"""The type of the entity. For most entity types, the associated
        metadata is a Wikipedia URL (``wikipedia_url``) and Knowledge Graph
        MID (``mid``). The table below lists the associated fields for
        entities that have different metadata.

        Values:
            TYPE_UNSPECIFIED (0):
                Unspecified.
            PERSON (1):
                Person.
            LOCATION (2):
                Location.
            ORGANIZATION (3):
                Organization.
            EVENT (4):
                Event.
            WORK_OF_ART (5):
                Artwork.
            CONSUMER_GOOD (6):
                Consumer product.
            OTHER (7):
                Other types of entities.
            PHONE_NUMBER (9):
                Phone number.

                The metadata lists the phone number (formatted according to
                local convention), plus whichever additional elements appear
                in the text:

                - ``number`` - The actual number, broken down into sections
                  according to local convention.
                - ``national_prefix`` - Country code, if detected.
                - ``area_code`` - Region or area code, if detected.
                - ``extension`` - Phone extension (to be dialed after
                  connection), if detected.
            ADDRESS (10):
                Address.

                The metadata identifies the street number and locality plus
                whichever additional elements appear in the text:

                - ``street_number`` - Street number.
                - ``locality`` - City or town.
                - ``street_name`` - Street/route name, if detected.
                - ``postal_code`` - Postal code, if detected.
                - ``country`` - Country, if detected.
                - ``broad_region`` - Administrative area, such as the state,
                  if detected.
                - ``narrow_region`` - Smaller administrative area, such as
                  county, if detected.
                - ``sublocality`` - Used in Asian addresses to demark a
                  district within a city, if detected.
            DATE (11):
                Date.

                The metadata identifies the components of the date:

                - ``year`` - Four digit year, if detected.
                - ``month`` - Two digit month number, if detected.
                - ``day`` - Two digit day number, if detected.
            NUMBER (12):
                Number.

                The metadata is the number itself.
            PRICE (13):
                Price.

                The metadata identifies the ``value`` and ``currency``.
        """

        TYPE_UNSPECIFIED = 0
        PERSON = 1
        LOCATION = 2
        ORGANIZATION = 3
        EVENT = 4
        WORK_OF_ART = 5
        CONSUMER_GOOD = 6
        OTHER = 7
        PHONE_NUMBER = 9
        ADDRESS = 10
        DATE = 11
        NUMBER = 12
        PRICE = 13

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=2,
        enum=Type,
    )
    metadata: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )
    salience: float = proto.Field(
        proto.FLOAT,
        number=4,
    )
    sentiment: "SentimentData" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="SentimentData",
    )


class Intent(proto.Message):
    r"""The data for an intent. Represents a detected intent in the
    conversation, for example MAKES_PROMISE.

    Attributes:
        id (str):
            The unique identifier of the intent.
        display_name (str):
            The human-readable name of the intent.
    """

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class PhraseMatchData(proto.Message):
    r"""The data for a matched phrase matcher.
    Represents information identifying a phrase matcher for a given
    match.

    Attributes:
        phrase_matcher (str):
            The unique identifier (the resource name) of
            the phrase matcher.
        display_name (str):
            The human-readable name of the phrase
            matcher.
    """

    phrase_matcher: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DialogflowIntent(proto.Message):
    r"""The data for a Dialogflow intent. Represents a detected intent in
    the conversation, e.g. MAKES_PROMISE.

    Attributes:
        display_name (str):
            The human-readable name of the intent.
    """

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class InterruptionData(proto.Message):
    r"""The data for an interruption annotation."""


class SilenceData(proto.Message):
    r"""The data for a silence annotation."""


class HoldData(proto.Message):
    r"""The data for a hold annotation."""


class EntityMentionData(proto.Message):
    r"""The data for an entity mention annotation. This represents a mention
    of an ``Entity`` in the conversation.

    Attributes:
        entity_unique_id (str):
            The key of this entity in conversation entities. Can be used
            to retrieve the exact ``Entity`` this mention is attached
            to.
        type_ (google.cloud.contact_center_insights_v1.types.EntityMentionData.MentionType):
            The type of the entity mention.
        sentiment (google.cloud.contact_center_insights_v1.types.SentimentData):
            Sentiment expressed for this mention of the
            entity.
    """

    class MentionType(proto.Enum):
        r"""The supported types of mentions.

        Values:
            MENTION_TYPE_UNSPECIFIED (0):
                Unspecified.
            PROPER (1):
                Proper noun.
            COMMON (2):
                Common noun (or noun compound).
        """

        MENTION_TYPE_UNSPECIFIED = 0
        PROPER = 1
        COMMON = 2

    entity_unique_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: MentionType = proto.Field(
        proto.ENUM,
        number=2,
        enum=MentionType,
    )
    sentiment: "SentimentData" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="SentimentData",
    )


class IntentMatchData(proto.Message):
    r"""The data for an intent match.
    Represents an intent match for a text segment in the
    conversation. A text segment can be part of a sentence, a
    complete sentence, or an utterance with multiple sentences.

    Attributes:
        intent_unique_id (str):
            The id of the matched intent.
            Can be used to retrieve the corresponding intent
            information.
    """

    intent_unique_id: str = proto.Field(
        proto.STRING,
        number=1,
    )


class SentimentData(proto.Message):
    r"""The data for a sentiment annotation.

    Attributes:
        magnitude (float):
            A non-negative number from 0 to infinity
            which represents the abolute magnitude of
            sentiment regardless of score.
        score (float):
            The sentiment score between -1.0 (negative)
            and 1.0 (positive).
    """

    magnitude: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    score: float = proto.Field(
        proto.FLOAT,
        number=2,
    )


class IssueMatchData(proto.Message):
    r"""The data for an issue match annotation.

    Attributes:
        issue_assignment (google.cloud.contact_center_insights_v1.types.IssueAssignment):
            Information about the issue's assignment.
    """

    issue_assignment: "IssueAssignment" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="IssueAssignment",
    )


class IssueModel(proto.Message):
    r"""The issue model resource.

    Attributes:
        name (str):
            Immutable. The resource name of the issue model. Format:
            projects/{project}/locations/{location}/issueModels/{issue_model}
        display_name (str):
            The representative name for the issue model.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which this issue
            model was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The most recent time at which
            the issue model was updated.
        issue_count (int):
            Output only. Number of issues in this issue
            model.
        state (google.cloud.contact_center_insights_v1.types.IssueModel.State):
            Output only. State of the model.
        input_data_config (google.cloud.contact_center_insights_v1.types.IssueModel.InputDataConfig):
            Configs for the input data that used to
            create the issue model.
        training_stats (google.cloud.contact_center_insights_v1.types.IssueModelLabelStats):
            Output only. Immutable. The issue model's
            label statistics on its training data.
        model_type (google.cloud.contact_center_insights_v1.types.IssueModel.ModelType):
            Type of the model.
        language_code (str):
            Language of the model.
    """

    class State(proto.Enum):
        r"""State of the model.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified.
            UNDEPLOYED (1):
                Model is not deployed but is ready to deploy.
            DEPLOYING (2):
                Model is being deployed.
            DEPLOYED (3):
                Model is deployed and is ready to be used. A
                model can only be used in analysis if it's in
                this state.
            UNDEPLOYING (4):
                Model is being undeployed.
            DELETING (5):
                Model is being deleted.
        """

        STATE_UNSPECIFIED = 0
        UNDEPLOYED = 1
        DEPLOYING = 2
        DEPLOYED = 3
        UNDEPLOYING = 4
        DELETING = 5

    class ModelType(proto.Enum):
        r"""Type of the model.

        Values:
            MODEL_TYPE_UNSPECIFIED (0):
                Unspecified model type.
            TYPE_V1 (1):
                Type V1.
            TYPE_V2 (2):
                Type V2.
        """

        MODEL_TYPE_UNSPECIFIED = 0
        TYPE_V1 = 1
        TYPE_V2 = 2

    class InputDataConfig(proto.Message):
        r"""Configs for the input data used to create the issue model.

        Attributes:
            medium (google.cloud.contact_center_insights_v1.types.Conversation.Medium):
                Medium of conversations used in training data. This field is
                being deprecated. To specify the medium to be used in
                training a new issue model, set the ``medium`` field on
                ``filter``.
            training_conversations_count (int):
                Output only. Number of conversations used in
                training. Output only.
            filter (str):
                A filter to reduce the conversations used for
                training the model to a specific subset.
        """

        medium: "Conversation.Medium" = proto.Field(
            proto.ENUM,
            number=1,
            enum="Conversation.Medium",
        )
        training_conversations_count: int = proto.Field(
            proto.INT64,
            number=2,
        )
        filter: str = proto.Field(
            proto.STRING,
            number=3,
        )

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
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    issue_count: int = proto.Field(
        proto.INT64,
        number=8,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=5,
        enum=State,
    )
    input_data_config: InputDataConfig = proto.Field(
        proto.MESSAGE,
        number=6,
        message=InputDataConfig,
    )
    training_stats: "IssueModelLabelStats" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="IssueModelLabelStats",
    )
    model_type: ModelType = proto.Field(
        proto.ENUM,
        number=9,
        enum=ModelType,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=10,
    )


class Issue(proto.Message):
    r"""The issue resource.

    Attributes:
        name (str):
            Immutable. The resource name of the issue. Format:
            projects/{project}/locations/{location}/issueModels/{issue_model}/issues/{issue}
        display_name (str):
            The representative name for the issue.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which this issue was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The most recent time that this
            issue was updated.
        sample_utterances (MutableSequence[str]):
            Output only. Resource names of the sample
            representative utterances that match to this
            issue.
        display_description (str):
            Representative description of the issue.
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
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    sample_utterances: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    display_description: str = proto.Field(
        proto.STRING,
        number=14,
    )


class IssueModelLabelStats(proto.Message):
    r"""Aggregated statistics about an issue model.

    Attributes:
        analyzed_conversations_count (int):
            Number of conversations the issue model has
            analyzed at this point in time.
        unclassified_conversations_count (int):
            Number of analyzed conversations for which no
            issue was applicable at this point in time.
        issue_stats (MutableMapping[str, google.cloud.contact_center_insights_v1.types.IssueModelLabelStats.IssueStats]):
            Statistics on each issue. Key is the issue's
            resource name.
    """

    class IssueStats(proto.Message):
        r"""Aggregated statistics about an issue.

        Attributes:
            issue (str):
                Issue resource. Format:
                projects/{project}/locations/{location}/issueModels/{issue_model}/issues/{issue}
            labeled_conversations_count (int):
                Number of conversations attached to the issue
                at this point in time.
            display_name (str):
                Display name of the issue.
        """

        issue: str = proto.Field(
            proto.STRING,
            number=1,
        )
        labeled_conversations_count: int = proto.Field(
            proto.INT64,
            number=2,
        )
        display_name: str = proto.Field(
            proto.STRING,
            number=3,
        )

    analyzed_conversations_count: int = proto.Field(
        proto.INT64,
        number=1,
    )
    unclassified_conversations_count: int = proto.Field(
        proto.INT64,
        number=2,
    )
    issue_stats: MutableMapping[str, IssueStats] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=3,
        message=IssueStats,
    )


class PhraseMatcher(proto.Message):
    r"""The phrase matcher resource.

    Attributes:
        name (str):
            The resource name of the phrase matcher. Format:
            projects/{project}/locations/{location}/phraseMatchers/{phrase_matcher}
        revision_id (str):
            Output only. Immutable. The revision ID of
            the phrase matcher. A new revision is committed
            whenever the matcher is changed, except when it
            is activated or deactivated. A server generated
            random ID will be used. Example:
            locations/global/phraseMatchers/my-first-matcher@1234567
        version_tag (str):
            The customized version tag to use for the phrase matcher. If
            not specified, it will default to ``revision_id``.
        revision_create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp of when the
            revision was created. It is also the create time
            when a new matcher is added.
        display_name (str):
            The human-readable name of the phrase
            matcher.
        type_ (google.cloud.contact_center_insights_v1.types.PhraseMatcher.PhraseMatcherType):
            Required. The type of this phrase matcher.
        active (bool):
            Applies the phrase matcher only when it is
            active.
        phrase_match_rule_groups (MutableSequence[google.cloud.contact_center_insights_v1.types.PhraseMatchRuleGroup]):
            A list of phase match rule groups that are
            included in this matcher.
        activation_update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The most recent time at which
            the activation status was updated.
        role_match (google.cloud.contact_center_insights_v1.types.ConversationParticipant.Role):
            The role whose utterances the phrase matcher should be
            matched against. If the role is ROLE_UNSPECIFIED it will be
            matched against any utterances in the transcript.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The most recent time at which
            the phrase matcher was updated.
    """

    class PhraseMatcherType(proto.Enum):
        r"""Specifies how to combine each phrase match rule group to
        determine whether there is a match.

        Values:
            PHRASE_MATCHER_TYPE_UNSPECIFIED (0):
                Unspecified.
            ALL_OF (1):
                Must meet all phrase match rule groups or
                there is no match.
            ANY_OF (2):
                If any of the phrase match rule groups are
                met, there is a match.
        """

        PHRASE_MATCHER_TYPE_UNSPECIFIED = 0
        ALL_OF = 1
        ANY_OF = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    revision_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    version_tag: str = proto.Field(
        proto.STRING,
        number=3,
    )
    revision_create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    type_: PhraseMatcherType = proto.Field(
        proto.ENUM,
        number=6,
        enum=PhraseMatcherType,
    )
    active: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    phrase_match_rule_groups: MutableSequence["PhraseMatchRuleGroup"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=8,
            message="PhraseMatchRuleGroup",
        )
    )
    activation_update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    role_match: "ConversationParticipant.Role" = proto.Field(
        proto.ENUM,
        number=10,
        enum="ConversationParticipant.Role",
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=11,
        message=timestamp_pb2.Timestamp,
    )


class PhraseMatchRuleGroup(proto.Message):
    r"""A message representing a rule in the phrase matcher.

    Attributes:
        type_ (google.cloud.contact_center_insights_v1.types.PhraseMatchRuleGroup.PhraseMatchRuleGroupType):
            Required. The type of this phrase match rule
            group.
        phrase_match_rules (MutableSequence[google.cloud.contact_center_insights_v1.types.PhraseMatchRule]):
            A list of phrase match rules that are
            included in this group.
    """

    class PhraseMatchRuleGroupType(proto.Enum):
        r"""Specifies how to combine each phrase match rule for whether
        there is a match.

        Values:
            PHRASE_MATCH_RULE_GROUP_TYPE_UNSPECIFIED (0):
                Unspecified.
            ALL_OF (1):
                Must meet all phrase match rules or there is
                no match.
            ANY_OF (2):
                If any of the phrase match rules are met,
                there is a match.
        """

        PHRASE_MATCH_RULE_GROUP_TYPE_UNSPECIFIED = 0
        ALL_OF = 1
        ANY_OF = 2

    type_: PhraseMatchRuleGroupType = proto.Field(
        proto.ENUM,
        number=1,
        enum=PhraseMatchRuleGroupType,
    )
    phrase_match_rules: MutableSequence["PhraseMatchRule"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="PhraseMatchRule",
    )


class PhraseMatchRule(proto.Message):
    r"""The data for a phrase match rule.

    Attributes:
        query (str):
            Required. The phrase to be matched.
        negated (bool):
            Specifies whether the phrase must be missing
            from the transcript segment or present in the
            transcript segment.
        config (google.cloud.contact_center_insights_v1.types.PhraseMatchRuleConfig):
            Provides additional information about the
            rule that specifies how to apply the rule.
    """

    query: str = proto.Field(
        proto.STRING,
        number=1,
    )
    negated: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    config: "PhraseMatchRuleConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="PhraseMatchRuleConfig",
    )


class PhraseMatchRuleConfig(proto.Message):
    r"""Configuration information of a phrase match rule.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        exact_match_config (google.cloud.contact_center_insights_v1.types.ExactMatchConfig):
            The configuration for the exact match rule.

            This field is a member of `oneof`_ ``config``.
    """

    exact_match_config: "ExactMatchConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="config",
        message="ExactMatchConfig",
    )


class ExactMatchConfig(proto.Message):
    r"""Exact match configuration.

    Attributes:
        case_sensitive (bool):
            Whether to consider case sensitivity when
            performing an exact match.
    """

    case_sensitive: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class Settings(proto.Message):
    r"""The CCAI Insights project wide settings. Use these settings to
    configure the behavior of Insights. View these settings with
    ```getsettings`` <https://cloud.google.com/contact-center/insights/docs/reference/rest/v1/projects.locations/getSettings>`__
    and change the settings with
    ```updateSettings`` <https://cloud.google.com/contact-center/insights/docs/reference/rest/v1/projects.locations/updateSettings>`__.

    Attributes:
        name (str):
            Immutable. The resource name of the settings
            resource. Format:

            projects/{project}/locations/{location}/settings
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the settings
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the settings
            were last updated.
        language_code (str):
            A language code to be applied to each
            transcript segment unless the segment already
            specifies a language code. Language code
            defaults to "en-US" if it is neither specified
            on the segment nor here.
        conversation_ttl (google.protobuf.duration_pb2.Duration):
            The default TTL for newly-created
            conversations. If a conversation has a specified
            expiration, that value will be used instead.
            Changing this value will not change the
            expiration of existing conversations.
            Conversations with no expire time persist until
            they are deleted.
        pubsub_notification_settings (MutableMapping[str, str]):
            A map that maps a notification trigger to a Pub/Sub topic.
            Each time a specified trigger occurs, Insights will notify
            the corresponding Pub/Sub topic.

            Keys are notification triggers. Supported keys are:

            - "all-triggers": Notify each time any of the supported
              triggers occurs.
            - "create-analysis": Notify each time an analysis is
              created.
            - "create-conversation": Notify each time a conversation is
              created.
            - "export-insights-data": Notify each time an export is
              complete.
            - "ingest-conversations": Notify each time an
              IngestConversations LRO is complete.
            - "update-conversation": Notify each time a conversation is
              updated via UpdateConversation.
            - "upload-conversation": Notify when an UploadConversation
              LRO is complete.

            Values are Pub/Sub topics. The format of each Pub/Sub topic
            is: projects/{project}/topics/{topic}
        analysis_config (google.cloud.contact_center_insights_v1.types.Settings.AnalysisConfig):
            Default analysis settings.
        redaction_config (google.cloud.contact_center_insights_v1.types.RedactionConfig):
            Default DLP redaction resources to be applied while
            ingesting conversations. This applies to conversations
            ingested from the ``UploadConversation`` and
            ``IngestConversations`` endpoints, including conversations
            coming from CCAI Platform.
        speech_config (google.cloud.contact_center_insights_v1.types.SpeechConfig):
            Optional. Default Speech-to-Text resources to use while
            ingesting audio files. Optional, CCAI Insights will create a
            default if not provided. This applies to conversations
            ingested from the ``UploadConversation`` and
            ``IngestConversations`` endpoints, including conversations
            coming from CCAI Platform.
    """

    class AnalysisConfig(proto.Message):
        r"""Default configuration when creating Analyses in Insights.

        Attributes:
            runtime_integration_analysis_percentage (float):
                Percentage of conversations created using Dialogflow runtime
                integration to analyze automatically, between [0, 100].
            upload_conversation_analysis_percentage (float):
                Percentage of conversations created using the
                UploadConversation endpoint to analyze automatically,
                between [0, 100].
            annotator_selector (google.cloud.contact_center_insights_v1.types.AnnotatorSelector):
                To select the annotators to run and the
                phrase matchers to use (if any). If not
                specified, all annotators will be run.
        """

        runtime_integration_analysis_percentage: float = proto.Field(
            proto.DOUBLE,
            number=1,
        )
        upload_conversation_analysis_percentage: float = proto.Field(
            proto.DOUBLE,
            number=6,
        )
        annotator_selector: "AnnotatorSelector" = proto.Field(
            proto.MESSAGE,
            number=5,
            message="AnnotatorSelector",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=4,
    )
    conversation_ttl: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=5,
        message=duration_pb2.Duration,
    )
    pubsub_notification_settings: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    analysis_config: AnalysisConfig = proto.Field(
        proto.MESSAGE,
        number=7,
        message=AnalysisConfig,
    )
    redaction_config: "RedactionConfig" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="RedactionConfig",
    )
    speech_config: "SpeechConfig" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="SpeechConfig",
    )


class AnalysisRule(proto.Message):
    r"""The CCAI Insights project wide analysis rule. This rule will
    be applied to all conversations that match the filter defined in
    the rule. For a conversation matches the filter, the annotators
    specified in the rule will be run. If a conversation matches
    multiple rules, a union of all the annotators will be run. One
    project can have multiple analysis rules.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the analysis rule. Format:
            projects/{project}/locations/{location}/analysisRules/{analysis_rule}
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which this analysis
            rule was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The most recent time at which
            this analysis rule was updated.
        display_name (str):
            Display Name of the analysis rule.

            This field is a member of `oneof`_ ``_display_name``.
        conversation_filter (str):
            Filter for the conversations that should
            apply this analysis rule. An empty filter means
            this analysis rule applies to all conversations.
        annotator_selector (google.cloud.contact_center_insights_v1.types.AnnotatorSelector):
            Selector of annotators to run and the phrase matchers to use
            for conversations that matches the conversation_filter. If
            not specified, NO annotators will be run.
        analysis_percentage (float):
            Percentage of conversations that we should apply this
            analysis setting automatically, between [0, 1]. For example,
            0.1 means 10%. Conversations are sampled in a determenestic
            way. The original runtime_percentage & upload percentage
            will be replaced by defining filters on the conversation.
        active (bool):
            If true, apply this rule to conversations.
            Otherwise, this rule is inactive and saved as a
            draft.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    conversation_filter: str = proto.Field(
        proto.STRING,
        number=5,
    )
    annotator_selector: "AnnotatorSelector" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="AnnotatorSelector",
    )
    analysis_percentage: float = proto.Field(
        proto.DOUBLE,
        number=7,
    )
    active: bool = proto.Field(
        proto.BOOL,
        number=8,
    )


class EncryptionSpec(proto.Message):
    r"""A customer-managed encryption key specification that can be applied
    to all created resources (e.g. ``Conversation``).

    Attributes:
        name (str):
            Immutable. The resource name of the
            encryption key specification resource. Format:

            projects/{project}/locations/{location}/encryptionSpec
        kms_key (str):
            Required. The name of customer-managed encryption key that
            is used to secure a resource and its sub-resources. If
            empty, the resource is secured by our default encryption
            key. Only the key in the same location as this resource is
            allowed to be used for encryption. Format:
            ``projects/{project}/locations/{location}/keyRings/{keyRing}/cryptoKeys/{key}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    kms_key: str = proto.Field(
        proto.STRING,
        number=2,
    )


class RedactionConfig(proto.Message):
    r"""DLP resources used for redaction while ingesting conversations. DLP
    settings are applied to conversations ingested from the
    ``UploadConversation`` and ``IngestConversations`` endpoints,
    including conversation coming from CCAI Platform. They are not
    applied to conversations ingested from the ``CreateConversation``
    endpoint or the Dialogflow / Agent Assist runtime integrations. When
    using Dialogflow / Agent Assist runtime integrations, redaction
    should be performed in Dialogflow / Agent Assist.

    Attributes:
        deidentify_template (str):
            The fully-qualified DLP deidentify template resource name.
            Format:
            ``projects/{project}/deidentifyTemplates/{template}``
        inspect_template (str):
            The fully-qualified DLP inspect template resource name.
            Format:
            ``projects/{project}/locations/{location}/inspectTemplates/{template}``
    """

    deidentify_template: str = proto.Field(
        proto.STRING,
        number=1,
    )
    inspect_template: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SpeechConfig(proto.Message):
    r"""Speech-to-Text configuration. Speech-to-Text settings are applied to
    conversations ingested from the ``UploadConversation`` and
    ``IngestConversations`` endpoints, including conversation coming
    from CCAI Platform. They are not applied to conversations ingested
    from the ``CreateConversation`` endpoint.

    Attributes:
        speech_recognizer (str):
            The fully-qualified Speech Recognizer resource name. Format:
            ``projects/{project_id}/locations/{location}/recognizer/{recognizer}``
    """

    speech_recognizer: str = proto.Field(
        proto.STRING,
        number=1,
    )


class RuntimeAnnotation(proto.Message):
    r"""An annotation that was generated during the customer and
    agent interaction.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        article_suggestion (google.cloud.contact_center_insights_v1.types.ArticleSuggestionData):
            Agent Assist Article Suggestion data.

            This field is a member of `oneof`_ ``data``.
        faq_answer (google.cloud.contact_center_insights_v1.types.FaqAnswerData):
            Agent Assist FAQ answer data.

            This field is a member of `oneof`_ ``data``.
        smart_reply (google.cloud.contact_center_insights_v1.types.SmartReplyData):
            Agent Assist Smart Reply data.

            This field is a member of `oneof`_ ``data``.
        smart_compose_suggestion (google.cloud.contact_center_insights_v1.types.SmartComposeSuggestionData):
            Agent Assist Smart Compose suggestion data.

            This field is a member of `oneof`_ ``data``.
        dialogflow_interaction (google.cloud.contact_center_insights_v1.types.DialogflowInteractionData):
            Dialogflow interaction data.

            This field is a member of `oneof`_ ``data``.
        conversation_summarization_suggestion (google.cloud.contact_center_insights_v1.types.ConversationSummarizationSuggestionData):
            Conversation summarization suggestion data.

            This field is a member of `oneof`_ ``data``.
        annotation_id (str):
            The unique identifier of the annotation. Format:
            projects/{project}/locations/{location}/conversationDatasets/{dataset}/conversationDataItems/{data_item}/conversationAnnotations/{annotation}
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The time at which this annotation was
            created.
        start_boundary (google.cloud.contact_center_insights_v1.types.AnnotationBoundary):
            The boundary in the conversation where the
            annotation starts, inclusive.
        end_boundary (google.cloud.contact_center_insights_v1.types.AnnotationBoundary):
            The boundary in the conversation where the
            annotation ends, inclusive.
        answer_feedback (google.cloud.contact_center_insights_v1.types.AnswerFeedback):
            The feedback that the customer has about the answer in
            ``data``.
        user_input (google.cloud.contact_center_insights_v1.types.RuntimeAnnotation.UserInput):
            Explicit input used for generating the answer
    """

    class UserInput(proto.Message):
        r"""Explicit input used for generating the answer

        Attributes:
            query (str):
                Query text. Article Search uses this to store
                the input query used to generate the search
                results.
            generator_name (str):
                The resource name of associated generator. Format:
                ``projects/<Project ID>/locations/<Location ID>/generators/<Generator ID>``
            query_source (google.cloud.contact_center_insights_v1.types.RuntimeAnnotation.UserInput.QuerySource):
                Query source for the answer.
        """

        class QuerySource(proto.Enum):
            r"""The source of the query.

            Values:
                QUERY_SOURCE_UNSPECIFIED (0):
                    Unknown query source.
                AGENT_QUERY (1):
                    The query is from agents.
                SUGGESTED_QUERY (2):
                    The query is a query from previous
                    suggestions, e.g. from a preceding
                    SuggestKnowledgeAssist response.
            """

            QUERY_SOURCE_UNSPECIFIED = 0
            AGENT_QUERY = 1
            SUGGESTED_QUERY = 2

        query: str = proto.Field(
            proto.STRING,
            number=1,
        )
        generator_name: str = proto.Field(
            proto.STRING,
            number=2,
        )
        query_source: "RuntimeAnnotation.UserInput.QuerySource" = proto.Field(
            proto.ENUM,
            number=3,
            enum="RuntimeAnnotation.UserInput.QuerySource",
        )

    article_suggestion: "ArticleSuggestionData" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="data",
        message="ArticleSuggestionData",
    )
    faq_answer: "FaqAnswerData" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="data",
        message="FaqAnswerData",
    )
    smart_reply: "SmartReplyData" = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="data",
        message="SmartReplyData",
    )
    smart_compose_suggestion: "SmartComposeSuggestionData" = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="data",
        message="SmartComposeSuggestionData",
    )
    dialogflow_interaction: "DialogflowInteractionData" = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="data",
        message="DialogflowInteractionData",
    )
    conversation_summarization_suggestion: "ConversationSummarizationSuggestionData" = (
        proto.Field(
            proto.MESSAGE,
            number=12,
            oneof="data",
            message="ConversationSummarizationSuggestionData",
        )
    )
    annotation_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    start_boundary: "AnnotationBoundary" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="AnnotationBoundary",
    )
    end_boundary: "AnnotationBoundary" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="AnnotationBoundary",
    )
    answer_feedback: "AnswerFeedback" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="AnswerFeedback",
    )
    user_input: UserInput = proto.Field(
        proto.MESSAGE,
        number=16,
        message=UserInput,
    )


class AnswerFeedback(proto.Message):
    r"""The feedback that the customer has about a certain answer in
    the conversation.

    Attributes:
        correctness_level (google.cloud.contact_center_insights_v1.types.AnswerFeedback.CorrectnessLevel):
            The correctness level of an answer.
        clicked (bool):
            Indicates whether an answer or item was
            clicked by the human agent.
        displayed (bool):
            Indicates whether an answer or item was
            displayed to the human agent in the agent
            desktop UI.
    """

    class CorrectnessLevel(proto.Enum):
        r"""The correctness level of an answer.

        Values:
            CORRECTNESS_LEVEL_UNSPECIFIED (0):
                Correctness level unspecified.
            NOT_CORRECT (1):
                Answer is totally wrong.
            PARTIALLY_CORRECT (2):
                Answer is partially correct.
            FULLY_CORRECT (3):
                Answer is fully correct.
        """

        CORRECTNESS_LEVEL_UNSPECIFIED = 0
        NOT_CORRECT = 1
        PARTIALLY_CORRECT = 2
        FULLY_CORRECT = 3

    correctness_level: CorrectnessLevel = proto.Field(
        proto.ENUM,
        number=1,
        enum=CorrectnessLevel,
    )
    clicked: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    displayed: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class ArticleSuggestionData(proto.Message):
    r"""Agent Assist Article Suggestion data.

    Attributes:
        title (str):
            Article title.
        uri (str):
            Article URI.
        confidence_score (float):
            The system's confidence score that this
            article is a good match for this conversation,
            ranging from 0.0 (completely uncertain) to 1.0
            (completely certain).
        metadata (MutableMapping[str, str]):
            Map that contains metadata about the Article
            Suggestion and the document that it originates
            from.
        query_record (str):
            The name of the answer record. Format:
            projects/{project}/locations/{location}/answerRecords/{answer_record}
        source (str):
            The knowledge document that this answer was extracted from.
            Format:
            projects/{project}/knowledgeBases/{knowledge_base}/documents/{document}
    """

    title: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    confidence_score: float = proto.Field(
        proto.FLOAT,
        number=3,
    )
    metadata: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    query_record: str = proto.Field(
        proto.STRING,
        number=5,
    )
    source: str = proto.Field(
        proto.STRING,
        number=6,
    )


class FaqAnswerData(proto.Message):
    r"""Agent Assist frequently-asked-question answer data.

    Attributes:
        answer (str):
            The piece of text from the ``source`` knowledge base
            document.
        confidence_score (float):
            The system's confidence score that this
            answer is a good match for this conversation,
            ranging from 0.0 (completely uncertain) to 1.0
            (completely certain).
        question (str):
            The corresponding FAQ question.
        metadata (MutableMapping[str, str]):
            Map that contains metadata about the FAQ
            answer and the document that it originates from.
        query_record (str):
            The name of the answer record. Format:
            projects/{project}/locations/{location}/answerRecords/{answer_record}
        source (str):
            The knowledge document that this answer was extracted from.
            Format:
            projects/{project}/knowledgeBases/{knowledge_base}/documents/{document}.
    """

    answer: str = proto.Field(
        proto.STRING,
        number=1,
    )
    confidence_score: float = proto.Field(
        proto.FLOAT,
        number=2,
    )
    question: str = proto.Field(
        proto.STRING,
        number=3,
    )
    metadata: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    query_record: str = proto.Field(
        proto.STRING,
        number=5,
    )
    source: str = proto.Field(
        proto.STRING,
        number=6,
    )


class SmartReplyData(proto.Message):
    r"""Agent Assist Smart Reply data.

    Attributes:
        reply (str):
            The content of the reply.
        confidence_score (float):
            The system's confidence score that this reply
            is a good match for this conversation, ranging
            from 0.0 (completely uncertain) to 1.0
            (completely certain).
        metadata (MutableMapping[str, str]):
            Map that contains metadata about the Smart
            Reply and the document from which it originates.
        query_record (str):
            The name of the answer record. Format:
            projects/{project}/locations/{location}/answerRecords/{answer_record}
    """

    reply: str = proto.Field(
        proto.STRING,
        number=1,
    )
    confidence_score: float = proto.Field(
        proto.DOUBLE,
        number=2,
    )
    metadata: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )
    query_record: str = proto.Field(
        proto.STRING,
        number=4,
    )


class SmartComposeSuggestionData(proto.Message):
    r"""Agent Assist Smart Compose suggestion data.

    Attributes:
        suggestion (str):
            The content of the suggestion.
        confidence_score (float):
            The system's confidence score that this
            suggestion is a good match for this
            conversation, ranging from 0.0 (completely
            uncertain) to 1.0 (completely certain).
        metadata (MutableMapping[str, str]):
            Map that contains metadata about the Smart
            Compose suggestion and the document from which
            it originates.
        query_record (str):
            The name of the answer record. Format:
            projects/{project}/locations/{location}/answerRecords/{answer_record}
    """

    suggestion: str = proto.Field(
        proto.STRING,
        number=1,
    )
    confidence_score: float = proto.Field(
        proto.DOUBLE,
        number=2,
    )
    metadata: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )
    query_record: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DialogflowInteractionData(proto.Message):
    r"""Dialogflow interaction data.

    Attributes:
        dialogflow_intent_id (str):
            The Dialogflow intent resource path. Format:
            projects/{project}/agent/{agent}/intents/{intent}
        confidence (float):
            The confidence of the match ranging from 0.0
            (completely uncertain) to 1.0 (completely
            certain).
    """

    dialogflow_intent_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    confidence: float = proto.Field(
        proto.FLOAT,
        number=2,
    )


class ConversationSummarizationSuggestionData(proto.Message):
    r"""Conversation summarization suggestion data.

    Attributes:
        text (str):
            The summarization content that is
            concatenated into one string.
        text_sections (MutableMapping[str, str]):
            The summarization content that is divided
            into sections. The key is the section's name and
            the value is the section's content. There is no
            specific format for the key or value.
        confidence (float):
            The confidence score of the summarization.
        metadata (MutableMapping[str, str]):
            A map that contains metadata about the
            summarization and the document from which it
            originates.
        answer_record (str):
            The name of the answer record. Format:
            projects/{project}/locations/{location}/answerRecords/{answer_record}
        conversation_model (str):
            The name of the model that generates this summary. Format:
            projects/{project}/locations/{location}/conversationModels/{conversation_model}
    """

    text: str = proto.Field(
        proto.STRING,
        number=1,
    )
    text_sections: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    confidence: float = proto.Field(
        proto.FLOAT,
        number=2,
    )
    metadata: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )
    answer_record: str = proto.Field(
        proto.STRING,
        number=4,
    )
    conversation_model: str = proto.Field(
        proto.STRING,
        number=6,
    )


class ConversationParticipant(proto.Message):
    r"""The call participant speaking for a given utterance.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        dialogflow_participant_name (str):
            The name of the participant provided by
            Dialogflow. Format:
            projects/{project}/locations/{location}/conversations/{conversation}/participants/{participant}

            This field is a member of `oneof`_ ``participant``.
        user_id (str):
            A user-specified ID representing the
            participant.

            This field is a member of `oneof`_ ``participant``.
        dialogflow_participant (str):
            Deprecated. Use ``dialogflow_participant_name`` instead. The
            name of the Dialogflow participant. Format:
            projects/{project}/locations/{location}/conversations/{conversation}/participants/{participant}
        obfuscated_external_user_id (str):
            Obfuscated user ID from Dialogflow.
        role (google.cloud.contact_center_insights_v1.types.ConversationParticipant.Role):
            The role of the participant.
    """

    class Role(proto.Enum):
        r"""The role of the participant.

        Values:
            ROLE_UNSPECIFIED (0):
                Participant's role is not set.
            HUMAN_AGENT (1):
                Participant is a human agent.
            AUTOMATED_AGENT (2):
                Participant is an automated agent.
            END_USER (3):
                Participant is an end user who conversed with
                the contact center.
            ANY_AGENT (4):
                Participant is either a human or automated
                agent.
        """

        ROLE_UNSPECIFIED = 0
        HUMAN_AGENT = 1
        AUTOMATED_AGENT = 2
        END_USER = 3
        ANY_AGENT = 4

    dialogflow_participant_name: str = proto.Field(
        proto.STRING,
        number=5,
        oneof="participant",
    )
    user_id: str = proto.Field(
        proto.STRING,
        number=6,
        oneof="participant",
    )
    dialogflow_participant: str = proto.Field(
        proto.STRING,
        number=1,
    )
    obfuscated_external_user_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    role: Role = proto.Field(
        proto.ENUM,
        number=2,
        enum=Role,
    )


class View(proto.Message):
    r"""The View resource.

    Attributes:
        name (str):
            Immutable. The resource name of the view.
            Format:

            projects/{project}/locations/{location}/views/{view}
        display_name (str):
            The human-readable display name of the view.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which this view was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The most recent time at which
            the view was updated.
        value (str):
            String with specific view properties, must be
            non-empty.
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
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    value: str = proto.Field(
        proto.STRING,
        number=5,
    )


class AnnotatorSelector(proto.Message):
    r"""Selector of all available annotators and phrase matchers to
    run.

    Attributes:
        run_interruption_annotator (bool):
            Whether to run the interruption annotator.
        run_silence_annotator (bool):
            Whether to run the silence annotator.
        run_phrase_matcher_annotator (bool):
            Whether to run the active phrase matcher
            annotator(s).
        phrase_matchers (MutableSequence[str]):
            The list of phrase matchers to run. If not provided, all
            active phrase matchers will be used. If inactive phrase
            matchers are provided, they will not be used. Phrase
            matchers will be run only if run_phrase_matcher_annotator is
            set to true. Format:
            projects/{project}/locations/{location}/phraseMatchers/{phrase_matcher}
        run_sentiment_annotator (bool):
            Whether to run the sentiment annotator.
        run_entity_annotator (bool):
            Whether to run the entity annotator.
        run_intent_annotator (bool):
            Whether to run the intent annotator.
        run_issue_model_annotator (bool):
            Whether to run the issue model annotator. A
            model should have already been deployed for this
            to take effect.
        issue_models (MutableSequence[str]):
            The issue model to run. If not provided, the most recently
            deployed topic model will be used. The provided issue model
            will only be used for inference if the issue model is
            deployed and if run_issue_model_annotator is set to true. If
            more than one issue model is provided, only the first
            provided issue model will be used for inference.
        run_summarization_annotator (bool):
            Whether to run the summarization annotator.
        summarization_config (google.cloud.contact_center_insights_v1.types.AnnotatorSelector.SummarizationConfig):
            Configuration for the summarization
            annotator.
        run_qa_annotator (bool):
            Whether to run the QA annotator.
        qa_config (google.cloud.contact_center_insights_v1.types.AnnotatorSelector.QaConfig):
            Configuration for the QA annotator.
    """

    class SummarizationConfig(proto.Message):
        r"""Configuration for summarization.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            conversation_profile (str):
                Resource name of the Dialogflow conversation profile.
                Format:
                projects/{project}/locations/{location}/conversationProfiles/{conversation_profile}

                This field is a member of `oneof`_ ``model_source``.
            summarization_model (google.cloud.contact_center_insights_v1.types.AnnotatorSelector.SummarizationConfig.SummarizationModel):
                Default summarization model to be used.

                This field is a member of `oneof`_ ``model_source``.
        """

        class SummarizationModel(proto.Enum):
            r"""Summarization model to use, if ``conversation_profile`` is not used.

            Values:
                SUMMARIZATION_MODEL_UNSPECIFIED (0):
                    Unspecified summarization model.
                BASELINE_MODEL (1):
                    The CCAI baseline model.
                BASELINE_MODEL_V2_0 (2):
                    The CCAI baseline model, V2.0.
            """

            SUMMARIZATION_MODEL_UNSPECIFIED = 0
            BASELINE_MODEL = 1
            BASELINE_MODEL_V2_0 = 2

        conversation_profile: str = proto.Field(
            proto.STRING,
            number=1,
            oneof="model_source",
        )
        summarization_model: "AnnotatorSelector.SummarizationConfig.SummarizationModel" = proto.Field(
            proto.ENUM,
            number=2,
            oneof="model_source",
            enum="AnnotatorSelector.SummarizationConfig.SummarizationModel",
        )

    class QaConfig(proto.Message):
        r"""Configuration for the QA feature.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            scorecard_list (google.cloud.contact_center_insights_v1.types.AnnotatorSelector.QaConfig.ScorecardList):
                A manual list of scorecards to score.

                This field is a member of `oneof`_ ``scorecard_source``.
        """

        class ScorecardList(proto.Message):
            r"""Container for a list of scorecards.

            Attributes:
                qa_scorecard_revisions (MutableSequence[str]):
                    List of QaScorecardRevisions.
            """

            qa_scorecard_revisions: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=1,
            )

        scorecard_list: "AnnotatorSelector.QaConfig.ScorecardList" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="scorecard_source",
            message="AnnotatorSelector.QaConfig.ScorecardList",
        )

    run_interruption_annotator: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    run_silence_annotator: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    run_phrase_matcher_annotator: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    phrase_matchers: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    run_sentiment_annotator: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    run_entity_annotator: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    run_intent_annotator: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    run_issue_model_annotator: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    issue_models: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=10,
    )
    run_summarization_annotator: bool = proto.Field(
        proto.BOOL,
        number=9,
    )
    summarization_config: SummarizationConfig = proto.Field(
        proto.MESSAGE,
        number=11,
        message=SummarizationConfig,
    )
    run_qa_annotator: bool = proto.Field(
        proto.BOOL,
        number=12,
    )
    qa_config: QaConfig = proto.Field(
        proto.MESSAGE,
        number=13,
        message=QaConfig,
    )


class QaQuestion(proto.Message):
    r"""A single question to be scored by the Insights QA feature.

    Attributes:
        name (str):
            Identifier. The resource name of the question. Format:
            projects/{project}/locations/{location}/qaScorecards/{qa_scorecard}/revisions/{revision}/qaQuestions/{qa_question}
        abbreviation (str):
            Short, descriptive string, used in the UI
            where it's not practical to display the full
            question body. E.g., "Greeting".
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which this question
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The most recent time at which
            the question was updated.
        question_body (str):
            Question text. E.g., "Did the agent greet the
            customer?".
        answer_instructions (str):
            Instructions describing how to determine the
            answer.
        answer_choices (MutableSequence[google.cloud.contact_center_insights_v1.types.QaQuestion.AnswerChoice]):
            A list of valid answers to the question,
            which the LLM must choose from.
        tags (MutableSequence[str]):
            User-defined list of arbitrary tags for the
            question. Used for grouping/organization and for
            weighting the score of each question.
        order (int):
            Defines the order of the question within its
            parent scorecard revision.
        metrics (google.cloud.contact_center_insights_v1.types.QaQuestion.Metrics):
            Metrics of the underlying tuned LLM over a
            holdout/test set while fine tuning the
            underlying LLM for the given question. This
            field will only be populated if and only if the
            question is part of a scorecard revision that
            has been tuned.
        tuning_metadata (google.cloud.contact_center_insights_v1.types.QaQuestion.TuningMetadata):
            Metadata about the tuning operation for the
            question.This field will only be populated if
            and only if the question is part of a scorecard
            revision that has been tuned.
    """

    class AnswerChoice(proto.Message):
        r"""Message representing a possible answer to the question.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            str_value (str):
                String value.

                This field is a member of `oneof`_ ``value``.
            num_value (float):
                Numerical value.

                This field is a member of `oneof`_ ``value``.
            bool_value (bool):
                Boolean value.

                This field is a member of `oneof`_ ``value``.
            na_value (bool):
                A value of "Not Applicable (N/A)". If provided, this field
                may only be set to ``true``. If a question receives this
                answer, it will be excluded from any score calculations.

                This field is a member of `oneof`_ ``value``.
            key (str):
                A short string used as an identifier.
            score (float):
                Numerical score of the answer, used for generating the
                overall score of a QaScorecardResult. If the answer uses
                na_value, this field is unused.

                This field is a member of `oneof`_ ``_score``.
        """

        str_value: str = proto.Field(
            proto.STRING,
            number=2,
            oneof="value",
        )
        num_value: float = proto.Field(
            proto.DOUBLE,
            number=3,
            oneof="value",
        )
        bool_value: bool = proto.Field(
            proto.BOOL,
            number=4,
            oneof="value",
        )
        na_value: bool = proto.Field(
            proto.BOOL,
            number=5,
            oneof="value",
        )
        key: str = proto.Field(
            proto.STRING,
            number=1,
        )
        score: float = proto.Field(
            proto.DOUBLE,
            number=6,
            optional=True,
        )

    class Metrics(proto.Message):
        r"""A wrapper representing metrics calculated against a test-set
        on a LLM that was fine tuned for this question.

        Attributes:
            accuracy (float):
                Output only. Accuracy of the model. Measures
                the percentage of correct answers the model gave
                on the test set.
        """

        accuracy: float = proto.Field(
            proto.DOUBLE,
            number=1,
        )

    class TuningMetadata(proto.Message):
        r"""Metadata about the tuning operation for the question. Will
        only be set if a scorecard containing this question has been
        tuned.

        Attributes:
            total_valid_label_count (int):
                Total number of valid labels provided for the
                question at the time of tuining.
            dataset_validation_warnings (MutableSequence[google.cloud.contact_center_insights_v1.types.DatasetValidationWarning]):
                A list of any applicable data validation
                warnings about the question's feedback labels.
            tuning_error (str):
                Error status of the tuning operation for the
                question. Will only be set if the tuning
                operation failed.
        """

        total_valid_label_count: int = proto.Field(
            proto.INT64,
            number=1,
        )
        dataset_validation_warnings: MutableSequence["DatasetValidationWarning"] = (
            proto.RepeatedField(
                proto.ENUM,
                number=2,
                enum="DatasetValidationWarning",
            )
        )
        tuning_error: str = proto.Field(
            proto.STRING,
            number=3,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    abbreviation: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    question_body: str = proto.Field(
        proto.STRING,
        number=5,
    )
    answer_instructions: str = proto.Field(
        proto.STRING,
        number=9,
    )
    answer_choices: MutableSequence[AnswerChoice] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message=AnswerChoice,
    )
    tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    order: int = proto.Field(
        proto.INT32,
        number=8,
    )
    metrics: Metrics = proto.Field(
        proto.MESSAGE,
        number=10,
        message=Metrics,
    )
    tuning_metadata: TuningMetadata = proto.Field(
        proto.MESSAGE,
        number=11,
        message=TuningMetadata,
    )


class QaScorecard(proto.Message):
    r"""A QaScorecard represents a collection of questions to be
    scored during analysis.

    Attributes:
        name (str):
            Identifier. The scorecard name. Format:
            projects/{project}/locations/{location}/qaScorecards/{qa_scorecard}
        display_name (str):
            The user-specified display name of the
            scorecard.
        description (str):
            A text description explaining the intent of
            the scorecard.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which this scorecard
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The most recent time at which
            the scorecard was updated.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=7,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


class QaScorecardRevision(proto.Message):
    r"""A revision of a QaScorecard.

    Modifying published scorecard fields would invalidate existing
    scorecard results — the questions may have changed, or the score
    weighting will make existing scores impossible to understand. So
    changes must create a new revision, rather than modifying the
    existing resource.

    Attributes:
        name (str):
            Identifier. The name of the scorecard revision. Format:
            projects/{project}/locations/{location}/qaScorecards/{qa_scorecard}/revisions/{revision}
        snapshot (google.cloud.contact_center_insights_v1.types.QaScorecard):
            The snapshot of the scorecard at the time of
            this revision's creation.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp that the revision
            was created.
        alternate_ids (MutableSequence[str]):
            Output only. Alternative IDs for this revision of the
            scorecard, e.g., ``latest``.
        state (google.cloud.contact_center_insights_v1.types.QaScorecardRevision.State):
            Output only. State of the scorecard revision,
            indicating whether it's ready to be used in
            analysis.
    """

    class State(proto.Enum):
        r"""Enum representing the set of states a scorecard revision may
        be in.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified.
            EDITABLE (12):
                The scorecard revision can be edited.
            TRAINING (2):
                Scorecard model training is in progress.
            TRAINING_FAILED (9):
                Scorecard revision model training failed.
            READY (11):
                The revision can be used in analysis.
            DELETING (7):
                Scorecard is being deleted.
            TRAINING_CANCELLED (14):
                Scorecard model training was explicitly
                cancelled by the user.
        """

        STATE_UNSPECIFIED = 0
        EDITABLE = 12
        TRAINING = 2
        TRAINING_FAILED = 9
        READY = 11
        DELETING = 7
        TRAINING_CANCELLED = 14

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    snapshot: "QaScorecard" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="QaScorecard",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    alternate_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=5,
        enum=State,
    )


class QaAnswer(proto.Message):
    r"""An answer to a QaQuestion.

    Attributes:
        qa_question (str):
            The QaQuestion answered by this answer.
        conversation (str):
            The conversation the answer applies to.
        question_body (str):
            Question text. E.g., "Did the agent greet the
            customer?".
        answer_value (google.cloud.contact_center_insights_v1.types.QaAnswer.AnswerValue):
            The main answer value, incorporating any
            manual edits if they exist.
        tags (MutableSequence[str]):
            User-defined list of arbitrary tags. Matches
            the value from
            QaScorecard.ScorecardQuestion.tags. Used for
            grouping/organization and for weighting the
            score of each answer.
        answer_sources (MutableSequence[google.cloud.contact_center_insights_v1.types.QaAnswer.AnswerSource]):
            List of all individual answers given to the
            question.
    """

    class AnswerValue(proto.Message):
        r"""Message for holding the value of a
        [QaAnswer][google.cloud.contactcenterinsights.v1.QaAnswer].
        [QaQuestion.AnswerChoice][google.cloud.contactcenterinsights.v1.QaQuestion.AnswerChoice]
        defines the possible answer values for a question.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            str_value (str):
                String value.

                This field is a member of `oneof`_ ``value``.
            num_value (float):
                Numerical value.

                This field is a member of `oneof`_ ``value``.
            bool_value (bool):
                Boolean value.

                This field is a member of `oneof`_ ``value``.
            na_value (bool):
                A value of "Not Applicable (N/A)". Should only ever be
                ``true``.

                This field is a member of `oneof`_ ``value``.
            key (str):
                A short string used as an identifier. Matches
                the value used in QaQuestion.AnswerChoice.key.
            score (float):
                Output only. Numerical score of the answer.

                This field is a member of `oneof`_ ``_score``.
            potential_score (float):
                Output only. The maximum potential score of
                the question.

                This field is a member of `oneof`_ ``_potential_score``.
            normalized_score (float):
                Output only. Normalized score of the questions. Calculated
                as score / potential_score.

                This field is a member of `oneof`_ ``_normalized_score``.
        """

        str_value: str = proto.Field(
            proto.STRING,
            number=2,
            oneof="value",
        )
        num_value: float = proto.Field(
            proto.DOUBLE,
            number=3,
            oneof="value",
        )
        bool_value: bool = proto.Field(
            proto.BOOL,
            number=4,
            oneof="value",
        )
        na_value: bool = proto.Field(
            proto.BOOL,
            number=5,
            oneof="value",
        )
        key: str = proto.Field(
            proto.STRING,
            number=1,
        )
        score: float = proto.Field(
            proto.DOUBLE,
            number=6,
            optional=True,
        )
        potential_score: float = proto.Field(
            proto.DOUBLE,
            number=7,
            optional=True,
        )
        normalized_score: float = proto.Field(
            proto.DOUBLE,
            number=8,
            optional=True,
        )

    class AnswerSource(proto.Message):
        r"""A question may have multiple answers from varying sources,
        one of which becomes the "main" answer above. AnswerSource
        represents each individual answer.

        Attributes:
            source_type (google.cloud.contact_center_insights_v1.types.QaAnswer.AnswerSource.SourceType):
                What created the answer.
            answer_value (google.cloud.contact_center_insights_v1.types.QaAnswer.AnswerValue):
                The answer value from this source.
        """

        class SourceType(proto.Enum):
            r"""What created the answer.

            Values:
                SOURCE_TYPE_UNSPECIFIED (0):
                    Source type is unspecified.
                SYSTEM_GENERATED (1):
                    Answer was system-generated; created during
                    an Insights analysis.
                MANUAL_EDIT (2):
                    Answer was created by a human via manual
                    edit.
            """

            SOURCE_TYPE_UNSPECIFIED = 0
            SYSTEM_GENERATED = 1
            MANUAL_EDIT = 2

        source_type: "QaAnswer.AnswerSource.SourceType" = proto.Field(
            proto.ENUM,
            number=1,
            enum="QaAnswer.AnswerSource.SourceType",
        )
        answer_value: "QaAnswer.AnswerValue" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="QaAnswer.AnswerValue",
        )

    qa_question: str = proto.Field(
        proto.STRING,
        number=7,
    )
    conversation: str = proto.Field(
        proto.STRING,
        number=2,
    )
    question_body: str = proto.Field(
        proto.STRING,
        number=6,
    )
    answer_value: AnswerValue = proto.Field(
        proto.MESSAGE,
        number=3,
        message=AnswerValue,
    )
    tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    answer_sources: MutableSequence[AnswerSource] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message=AnswerSource,
    )


class QaScorecardResult(proto.Message):
    r"""The results of scoring a single conversation against a
    QaScorecard. Contains a collection of QaAnswers and aggregate
    score.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The name of the scorecard result. Format:
            projects/{project}/locations/{location}/qaScorecardResults/{qa_scorecard_result}
        qa_scorecard_revision (str):
            The QaScorecardRevision scored by this
            result.
        conversation (str):
            The conversation scored by this result.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp that the revision
            was created.
        agent_id (str):
            ID of the agent that handled the
            conversation.
        qa_answers (MutableSequence[google.cloud.contact_center_insights_v1.types.QaAnswer]):
            Set of QaAnswers represented in the result.
        score (float):
            The overall numerical score of the result,
            incorporating any manual edits if they exist.

            This field is a member of `oneof`_ ``_score``.
        potential_score (float):
            The maximum potential overall score of the scorecard. Any
            questions answered using ``na_value`` are excluded from this
            calculation.

            This field is a member of `oneof`_ ``_potential_score``.
        normalized_score (float):
            The normalized score, which is the score
            divided by the potential score. Any manual edits
            are included if they exist.

            This field is a member of `oneof`_ ``_normalized_score``.
        qa_tag_results (MutableSequence[google.cloud.contact_center_insights_v1.types.QaScorecardResult.QaTagResult]):
            Collection of tags and their scores.
        score_sources (MutableSequence[google.cloud.contact_center_insights_v1.types.QaScorecardResult.ScoreSource]):
            List of all individual score sets.
    """

    class QaTagResult(proto.Message):
        r"""Tags and their corresponding results.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            tag (str):
                The tag the score applies to.
            score (float):
                The score the tag applies to.

                This field is a member of `oneof`_ ``_score``.
            potential_score (float):
                The potential score the tag applies to.

                This field is a member of `oneof`_ ``_potential_score``.
            normalized_score (float):
                The normalized score the tag applies to.

                This field is a member of `oneof`_ ``_normalized_score``.
        """

        tag: str = proto.Field(
            proto.STRING,
            number=1,
        )
        score: float = proto.Field(
            proto.DOUBLE,
            number=2,
            optional=True,
        )
        potential_score: float = proto.Field(
            proto.DOUBLE,
            number=3,
            optional=True,
        )
        normalized_score: float = proto.Field(
            proto.DOUBLE,
            number=4,
            optional=True,
        )

    class ScoreSource(proto.Message):
        r"""A scorecard result may have multiple sets of scores from
        varying sources, one of which becomes the "main" answer above. A
        ScoreSource represents each individual set of scores.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            source_type (google.cloud.contact_center_insights_v1.types.QaScorecardResult.ScoreSource.SourceType):
                What created the score.
            score (float):
                The overall numerical score of the result.

                This field is a member of `oneof`_ ``_score``.
            potential_score (float):
                The maximum potential overall score of the scorecard. Any
                questions answered using ``na_value`` are excluded from this
                calculation.

                This field is a member of `oneof`_ ``_potential_score``.
            normalized_score (float):
                The normalized score, which is the score
                divided by the potential score.

                This field is a member of `oneof`_ ``_normalized_score``.
            qa_tag_results (MutableSequence[google.cloud.contact_center_insights_v1.types.QaScorecardResult.QaTagResult]):
                Collection of tags and their scores.
        """

        class SourceType(proto.Enum):
            r"""What created the score.

            Values:
                SOURCE_TYPE_UNSPECIFIED (0):
                    Source type is unspecified.
                SYSTEM_GENERATED_ONLY (1):
                    Score is derived only from system-generated
                    answers.
                INCLUDES_MANUAL_EDITS (2):
                    Score is derived from both system-generated
                    answers, and includes any manual edits if they
                    exist.
            """

            SOURCE_TYPE_UNSPECIFIED = 0
            SYSTEM_GENERATED_ONLY = 1
            INCLUDES_MANUAL_EDITS = 2

        source_type: "QaScorecardResult.ScoreSource.SourceType" = proto.Field(
            proto.ENUM,
            number=1,
            enum="QaScorecardResult.ScoreSource.SourceType",
        )
        score: float = proto.Field(
            proto.DOUBLE,
            number=2,
            optional=True,
        )
        potential_score: float = proto.Field(
            proto.DOUBLE,
            number=3,
            optional=True,
        )
        normalized_score: float = proto.Field(
            proto.DOUBLE,
            number=4,
            optional=True,
        )
        qa_tag_results: MutableSequence["QaScorecardResult.QaTagResult"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=5,
                message="QaScorecardResult.QaTagResult",
            )
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    qa_scorecard_revision: str = proto.Field(
        proto.STRING,
        number=2,
    )
    conversation: str = proto.Field(
        proto.STRING,
        number=3,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    agent_id: str = proto.Field(
        proto.STRING,
        number=5,
    )
    qa_answers: MutableSequence["QaAnswer"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="QaAnswer",
    )
    score: float = proto.Field(
        proto.DOUBLE,
        number=7,
        optional=True,
    )
    potential_score: float = proto.Field(
        proto.DOUBLE,
        number=8,
        optional=True,
    )
    normalized_score: float = proto.Field(
        proto.DOUBLE,
        number=9,
        optional=True,
    )
    qa_tag_results: MutableSequence[QaTagResult] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message=QaTagResult,
    )
    score_sources: MutableSequence[ScoreSource] = proto.RepeatedField(
        proto.MESSAGE,
        number=11,
        message=ScoreSource,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
