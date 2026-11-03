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
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.dialogflow_v2beta1.types import generator, participant

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.v2beta1",
    manifest={
        "AnswerRecord",
        "AgentAssistantRecord",
        "AnswerFeedback",
        "AgentAssistantFeedback",
        "GetAnswerRecordRequest",
        "ListAnswerRecordsRequest",
        "ListAnswerRecordsResponse",
        "UpdateAnswerRecordRequest",
    },
)


class AnswerRecord(proto.Message):
    r"""Answer records are records to manage answer history and feedbacks
    for Dialogflow.

    Currently, answer record includes:

    - human agent assistant article suggestion
    - human agent assistant faq article

    It doesn't include:

    - ``DetectIntent`` intent matching
    - ``DetectIntent`` knowledge

    Answer records are not related to the conversation history in the
    Dialogflow Console. A Record is generated even when the end-user
    disables conversation history in the console. Records are created
    when there's a human agent assistant suggestion generated.

    A typical workflow for customers provide feedback to an answer is:

    1. For human agent assistant, customers get suggestion via
       ListSuggestions API. Together with the answers,
       [AnswerRecord.name][google.cloud.dialogflow.v2beta1.AnswerRecord.name]
       are returned to the customers.
    2. The customer uses the
       [AnswerRecord.name][google.cloud.dialogflow.v2beta1.AnswerRecord.name]
       to call the [UpdateAnswerRecord][] method to send feedback about
       a specific answer that they believe is wrong.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            The unique identifier of this answer record. Required for
            [AnswerRecords.UpdateAnswerRecord][google.cloud.dialogflow.v2beta1.AnswerRecords.UpdateAnswerRecord]
            method. Format:
            ``projects/<Project ID>/locations/<Location ID>/answerRecords/<Answer Record ID>``.
        answer_feedback (google.cloud.dialogflow_v2beta1.types.AnswerFeedback):
            Optional. The AnswerFeedback for this record. You can set
            this with
            [AnswerRecords.UpdateAnswerRecord][google.cloud.dialogflow.v2beta1.AnswerRecords.UpdateAnswerRecord]
            in order to give us feedback about this answer.
        agent_assistant_record (google.cloud.dialogflow_v2beta1.types.AgentAssistantRecord):
            Output only. The record for human agent
            assistant.

            This field is a member of `oneof`_ ``record``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    answer_feedback: "AnswerFeedback" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="AnswerFeedback",
    )
    agent_assistant_record: "AgentAssistantRecord" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="record",
        message="AgentAssistantRecord",
    )


class AgentAssistantRecord(proto.Message):
    r"""Represents a record of a human agent assistant answer.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        article_suggestion_answer (google.cloud.dialogflow_v2beta1.types.ArticleAnswer):
            Output only. The article suggestion answer.

            This field is a member of `oneof`_ ``answer``.
        faq_answer (google.cloud.dialogflow_v2beta1.types.FaqAnswer):
            Output only. The FAQ answer.

            This field is a member of `oneof`_ ``answer``.
        dialogflow_assist_answer (google.cloud.dialogflow_v2beta1.types.DialogflowAssistAnswer):
            Output only. The Dialogflow assist answer.

            This field is a member of `oneof`_ ``answer``.
        generator_suggestion (google.cloud.dialogflow_v2beta1.types.GeneratorSuggestion):
            Output only. The generator suggestion.

            This field is a member of `oneof`_ ``answer``.
        companion_suggestion (google.cloud.dialogflow_v2beta1.types.CompanionSuggestion):
            Output only. The companion suggestion.

            This field is a member of `oneof`_ ``answer``.
        reactive_companion_suggestion (google.cloud.dialogflow_v2beta1.types.StreamingReactiveCompanionSuggestionsResponse.ReactiveModeResponse):
            Output only. The reactive companion
            suggestion.

            This field is a member of `oneof`_ ``answer``.
    """

    article_suggestion_answer: participant.ArticleAnswer = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="answer",
        message=participant.ArticleAnswer,
    )
    faq_answer: participant.FaqAnswer = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="answer",
        message=participant.FaqAnswer,
    )
    dialogflow_assist_answer: participant.DialogflowAssistAnswer = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="answer",
        message=participant.DialogflowAssistAnswer,
    )
    generator_suggestion: generator.GeneratorSuggestion = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="answer",
        message=generator.GeneratorSuggestion,
    )
    companion_suggestion: participant.CompanionSuggestion = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="answer",
        message=participant.CompanionSuggestion,
    )
    reactive_companion_suggestion: participant.StreamingReactiveCompanionSuggestionsResponse.ReactiveModeResponse = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="answer",
        message=participant.StreamingReactiveCompanionSuggestionsResponse.ReactiveModeResponse,
    )


class AnswerFeedback(proto.Message):
    r"""Represents feedback the customer has about the quality &
    correctness of a certain answer in a conversation.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        correctness_level (google.cloud.dialogflow_v2beta1.types.AnswerFeedback.CorrectnessLevel):
            The correctness level of the specific answer.
        agent_assistant_detail_feedback (google.cloud.dialogflow_v2beta1.types.AgentAssistantFeedback):
            Optional. Detail feedback of agent assistant
            suggestions.

            This field is a member of `oneof`_ ``detail_feedback``.
        clicked (bool):
            Indicates whether the answer/item was clicked
            by the human agent or not. Default to false.
            For knowledge search, the answer record is
            considered to be clicked if the answer was
            copied or any URI was clicked.
        click_time (google.protobuf.timestamp_pb2.Timestamp):
            Time when the answer/item was clicked.
        displayed (bool):
            Indicates whether the answer/item was
            displayed to the human agent in the agent
            desktop UI. Default to false.
        display_time (google.protobuf.timestamp_pb2.Timestamp):
            Time when the answer/item was displayed.
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
    agent_assistant_detail_feedback: "AgentAssistantFeedback" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="detail_feedback",
        message="AgentAssistantFeedback",
    )
    clicked: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    click_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    displayed: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    display_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )


class AgentAssistantFeedback(proto.Message):
    r"""Detail feedback of Agent Assistant result.

    Attributes:
        answer_relevance (google.cloud.dialogflow_v2beta1.types.AgentAssistantFeedback.AnswerRelevance):
            Optional. Whether or not the suggested answer is relevant.

            For example:

            - Query: "Can I change my mailing address?"
            - Suggested document says: "Items must be returned/exchanged
              within 60 days of the purchase date."
            - [answer_relevance][google.cloud.dialogflow.v2beta1.AgentAssistantFeedback.answer_relevance]:
              [AnswerRelevance.IRRELEVANT][google.cloud.dialogflow.v2beta1.AgentAssistantFeedback.AnswerRelevance.IRRELEVANT]
        document_correctness (google.cloud.dialogflow_v2beta1.types.AgentAssistantFeedback.DocumentCorrectness):
            Optional. Whether or not the information in the document is
            correct.

            For example:

            - Query: "Can I return the package in 2 days once received?"
            - Suggested document says: "Items must be returned/exchanged
              within 60 days of the purchase date."
            - Ground truth: "No return or exchange is allowed."
            - [document_correctness][google.cloud.dialogflow.v2beta1.AgentAssistantFeedback.document_correctness]:
              [INCORRECT][google.cloud.dialogflow.v2beta1.AgentAssistantFeedback.DocumentCorrectness.INCORRECT]
        document_efficiency (google.cloud.dialogflow_v2beta1.types.AgentAssistantFeedback.DocumentEfficiency):
            Optional. Whether or not the suggested document is
            efficient. For example, if the document is poorly written,
            hard to understand, hard to use or too long to find useful
            information,
            [document_efficiency][google.cloud.dialogflow.v2beta1.AgentAssistantFeedback.document_efficiency]
            is
            [DocumentEfficiency.INEFFICIENT][google.cloud.dialogflow.v2beta1.AgentAssistantFeedback.DocumentEfficiency.INEFFICIENT].
        summarization_feedback (google.cloud.dialogflow_v2beta1.types.AgentAssistantFeedback.SummarizationFeedback):
            Feedback for conversation summarization.
        knowledge_search_feedback (google.cloud.dialogflow_v2beta1.types.AgentAssistantFeedback.KnowledgeSearchFeedback):
            Optional. Feedback for knowledge search.
        knowledge_assist_feedback (google.cloud.dialogflow_v2beta1.types.AgentAssistantFeedback.KnowledgeAssistFeedback):
            Optional. Feedback for knowledge assist.
        companion_feedback (google.cloud.dialogflow_v2beta1.types.AgentAssistantFeedback.CompanionFeedback):
            Optional. Feedback for companion agent.
    """

    class AnswerRelevance(proto.Enum):
        r"""Relevance of an answer.

        Values:
            ANSWER_RELEVANCE_UNSPECIFIED (0):
                Answer relevance unspecified.
            IRRELEVANT (1):
                Answer is irrelevant to query.
            RELEVANT (2):
                Answer is relevant to query.
        """

        ANSWER_RELEVANCE_UNSPECIFIED = 0
        IRRELEVANT = 1
        RELEVANT = 2

    class DocumentCorrectness(proto.Enum):
        r"""Correctness of document.

        Values:
            DOCUMENT_CORRECTNESS_UNSPECIFIED (0):
                Document correctness unspecified.
            INCORRECT (1):
                Information in document is incorrect.
            CORRECT (2):
                Information in document is correct.
        """

        DOCUMENT_CORRECTNESS_UNSPECIFIED = 0
        INCORRECT = 1
        CORRECT = 2

    class DocumentEfficiency(proto.Enum):
        r"""Efficiency of document.

        Values:
            DOCUMENT_EFFICIENCY_UNSPECIFIED (0):
                Document efficiency unspecified.
            INEFFICIENT (1):
                Document is inefficient.
            EFFICIENT (2):
                Document is efficient.
        """

        DOCUMENT_EFFICIENCY_UNSPECIFIED = 0
        INEFFICIENT = 1
        EFFICIENT = 2

    class SummarizationFeedback(proto.Message):
        r"""Feedback for conversation summarization.

        Attributes:
            start_timestamp (google.protobuf.timestamp_pb2.Timestamp):
                Timestamp when composing of the summary
                starts.
            submit_timestamp (google.protobuf.timestamp_pb2.Timestamp):
                Timestamp when the summary was submitted.
            summary_text (str):
                Text of actual submitted summary.
            text_sections (MutableMapping[str, str]):
                Optional. Actual text sections of submitted
                summary.
        """

        start_timestamp: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=1,
            message=timestamp_pb2.Timestamp,
        )
        submit_timestamp: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=2,
            message=timestamp_pb2.Timestamp,
        )
        summary_text: str = proto.Field(
            proto.STRING,
            number=3,
        )
        text_sections: MutableMapping[str, str] = proto.MapField(
            proto.STRING,
            proto.STRING,
            number=4,
        )

    class KnowledgeSearchFeedback(proto.Message):
        r"""Feedback for knowledge search.

        Attributes:
            answer_copied (bool):
                Whether the answer was copied by the human agent or not. If
                the value is set to be true,
                [AnswerFeedback.clicked][google.cloud.dialogflow.v2beta1.AnswerFeedback.clicked]
                will be updated to be true.
            clicked_uris (MutableSequence[str]):
                The URIs clicked by the human agent. The value is appended
                for each UpdateAnswerRecordRequest. If the value is not
                empty,
                [AnswerFeedback.clicked][google.cloud.dialogflow.v2beta1.AnswerFeedback.clicked]
                will be updated to be true.
        """

        answer_copied: bool = proto.Field(
            proto.BOOL,
            number=1,
        )
        clicked_uris: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )

    class KnowledgeAssistFeedback(proto.Message):
        r"""Feedback for knowledge assist.

        Attributes:
            answer_copied (bool):
                Whether the suggested answer was copied by the human agent.
                If the value is set to be true,
                [AnswerFeedback.clicked][google.cloud.dialogflow.v2beta1.AnswerFeedback.clicked]
                will be updated to be true.
            clicked_uris (MutableSequence[str]):
                The URIs clicked by the human agent. The value is appended
                for each
                [UpdateAnswerRecordRequest][google.cloud.dialogflow.v2beta1.UpdateAnswerRecordRequest].
                If the value is not empty,
                [AnswerFeedback.clicked][google.cloud.dialogflow.v2beta1.AnswerFeedback.clicked]
                will be updated to be true.
        """

        answer_copied: bool = proto.Field(
            proto.BOOL,
            number=1,
        )
        clicked_uris: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )

    class CompanionFeedback(proto.Message):
        r"""Feedback for companion agent."""

    answer_relevance: AnswerRelevance = proto.Field(
        proto.ENUM,
        number=1,
        enum=AnswerRelevance,
    )
    document_correctness: DocumentCorrectness = proto.Field(
        proto.ENUM,
        number=2,
        enum=DocumentCorrectness,
    )
    document_efficiency: DocumentEfficiency = proto.Field(
        proto.ENUM,
        number=3,
        enum=DocumentEfficiency,
    )
    summarization_feedback: SummarizationFeedback = proto.Field(
        proto.MESSAGE,
        number=4,
        message=SummarizationFeedback,
    )
    knowledge_search_feedback: KnowledgeSearchFeedback = proto.Field(
        proto.MESSAGE,
        number=5,
        message=KnowledgeSearchFeedback,
    )
    knowledge_assist_feedback: KnowledgeAssistFeedback = proto.Field(
        proto.MESSAGE,
        number=6,
        message=KnowledgeAssistFeedback,
    )
    companion_feedback: CompanionFeedback = proto.Field(
        proto.MESSAGE,
        number=8,
        message=CompanionFeedback,
    )


class GetAnswerRecordRequest(proto.Message):
    r"""Request message for
    [AnswerRecords.GetAnswerRecord][google.cloud.dialogflow.v2beta1.AnswerRecords.GetAnswerRecord].

    Attributes:
        name (str):
            Required. The name of the answer record to retrieve. Format:
            ``projects/<Project ID>/locations/<Location ID>/answerRecords/<Answer Record Id>``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListAnswerRecordsRequest(proto.Message):
    r"""Request message for
    [AnswerRecords.ListAnswerRecords][google.cloud.dialogflow.v2beta1.AnswerRecords.ListAnswerRecords].

    Attributes:
        parent (str):
            Required. The project to list all answer records for in
            reverse chronological order. Format:
            ``projects/<Project ID>/locations/<Location ID>``.
        filter (str):
            Optional. Filters to restrict results to specific answer
            records. The expression has the following syntax:

            [AND ] ...

            The following fields and operators are supported:

            - conversation_id with equals(=) operator

            Examples:

            - "conversation_id=bar" matches answer records in the
              projects/foo/locations/global/conversations/bar
              conversation (assuming the parent is
              projects/foo/locations/global).

            For more information about filtering, see `API
            Filtering <https://aip.dev/160>`__.
        page_size (int):
            Optional. The maximum number of records to
            return in a single page. The server may return
            fewer records than this. If unspecified, we use
            10. The maximum is 100.
        page_token (str):
            Optional. The
            [ListAnswerRecordsResponse.next_page_token][google.cloud.dialogflow.v2beta1.ListAnswerRecordsResponse.next_page_token]
            value returned from a previous list request used to continue
            listing on the next page.
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


class ListAnswerRecordsResponse(proto.Message):
    r"""Response message for
    [AnswerRecords.ListAnswerRecords][google.cloud.dialogflow.v2beta1.AnswerRecords.ListAnswerRecords].

    Attributes:
        answer_records (MutableSequence[google.cloud.dialogflow_v2beta1.types.AnswerRecord]):
            The list of answer records.
        next_page_token (str):
            A token to retrieve next page of results. Or empty if there
            are no more results. Pass this value in the
            [ListAnswerRecordsRequest.page_token][google.cloud.dialogflow.v2beta1.ListAnswerRecordsRequest.page_token]
            field in the subsequent call to ``ListAnswerRecords`` method
            to retrieve the next page of results.
    """

    @property
    def raw_page(self):
        return self

    answer_records: MutableSequence["AnswerRecord"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AnswerRecord",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateAnswerRecordRequest(proto.Message):
    r"""Request message for
    [AnswerRecords.UpdateAnswerRecord][google.cloud.dialogflow.v2beta1.AnswerRecords.UpdateAnswerRecord].

    Attributes:
        answer_record (google.cloud.dialogflow_v2beta1.types.AnswerRecord):
            Required. Answer record to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The mask to control which fields
            get updated.
    """

    answer_record: "AnswerRecord" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="AnswerRecord",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
