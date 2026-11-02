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
import google.rpc.status_pb2 as status_pb2  # type: ignore
import google.type.interval_pb2 as interval_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.contact_center_insights_v1.types import resources

__protobuf__ = proto.module(
    package="google.cloud.contactcenterinsights.v1",
    manifest={
        "ConversationView",
        "CalculateStatsRequest",
        "CalculateStatsResponse",
        "CreateAnalysisOperationMetadata",
        "CreateConversationRequest",
        "UploadConversationRequest",
        "UploadConversationMetadata",
        "ListConversationsRequest",
        "ListConversationsResponse",
        "GetConversationRequest",
        "UpdateConversationRequest",
        "DeleteConversationRequest",
        "IngestConversationsRequest",
        "IngestConversationsMetadata",
        "IngestConversationsResponse",
        "CreateAnalysisRequest",
        "ListAnalysesRequest",
        "ListAnalysesResponse",
        "GetAnalysisRequest",
        "DeleteAnalysisRequest",
        "BulkAnalyzeConversationsRequest",
        "BulkAnalyzeConversationsMetadata",
        "BulkAnalyzeConversationsResponse",
        "BulkDeleteConversationsRequest",
        "BulkDeleteConversationsMetadata",
        "BulkDeleteConversationsResponse",
        "ExportInsightsDataRequest",
        "ExportInsightsDataMetadata",
        "ExportInsightsDataResponse",
        "CreateIssueModelRequest",
        "CreateIssueModelMetadata",
        "UpdateIssueModelRequest",
        "ListIssueModelsRequest",
        "ListIssueModelsResponse",
        "GetIssueModelRequest",
        "DeleteIssueModelRequest",
        "DeleteIssueModelMetadata",
        "DeployIssueModelRequest",
        "DeployIssueModelResponse",
        "DeployIssueModelMetadata",
        "UndeployIssueModelRequest",
        "UndeployIssueModelResponse",
        "UndeployIssueModelMetadata",
        "ExportIssueModelRequest",
        "ExportIssueModelResponse",
        "ExportIssueModelMetadata",
        "ImportIssueModelRequest",
        "ImportIssueModelResponse",
        "ImportIssueModelMetadata",
        "GetIssueRequest",
        "ListIssuesRequest",
        "ListIssuesResponse",
        "UpdateIssueRequest",
        "DeleteIssueRequest",
        "CalculateIssueModelStatsRequest",
        "CalculateIssueModelStatsResponse",
        "CreatePhraseMatcherRequest",
        "ListPhraseMatchersRequest",
        "ListPhraseMatchersResponse",
        "GetPhraseMatcherRequest",
        "DeletePhraseMatcherRequest",
        "UpdatePhraseMatcherRequest",
        "GetSettingsRequest",
        "UpdateSettingsRequest",
        "CreateAnalysisRuleRequest",
        "GetAnalysisRuleRequest",
        "UpdateAnalysisRuleRequest",
        "DeleteAnalysisRuleRequest",
        "ListAnalysisRulesRequest",
        "ListAnalysisRulesResponse",
        "GetEncryptionSpecRequest",
        "InitializeEncryptionSpecRequest",
        "InitializeEncryptionSpecResponse",
        "InitializeEncryptionSpecMetadata",
        "CreateViewRequest",
        "GetViewRequest",
        "ListViewsRequest",
        "ListViewsResponse",
        "UpdateViewRequest",
        "DeleteViewRequest",
        "Dimension",
        "QueryMetricsRequest",
        "QueryMetricsResponse",
        "QueryMetricsMetadata",
        "CreateQaQuestionRequest",
        "GetQaQuestionRequest",
        "ListQaQuestionsRequest",
        "ListQaQuestionsResponse",
        "UpdateQaQuestionRequest",
        "DeleteQaQuestionRequest",
        "CreateQaScorecardRequest",
        "GetQaScorecardRequest",
        "UpdateQaScorecardRequest",
        "DeleteQaScorecardRequest",
        "CreateQaScorecardRevisionRequest",
        "GetQaScorecardRevisionRequest",
        "TuneQaScorecardRevisionRequest",
        "TuneQaScorecardRevisionResponse",
        "TuneQaScorecardRevisionMetadata",
        "DeployQaScorecardRevisionRequest",
        "UndeployQaScorecardRevisionRequest",
        "DeleteQaScorecardRevisionRequest",
        "ListQaScorecardsRequest",
        "ListQaScorecardsResponse",
        "ListQaScorecardRevisionsRequest",
        "ListQaScorecardRevisionsResponse",
        "CreateFeedbackLabelRequest",
        "ListFeedbackLabelsRequest",
        "ListFeedbackLabelsResponse",
        "GetFeedbackLabelRequest",
        "UpdateFeedbackLabelRequest",
        "DeleteFeedbackLabelRequest",
        "ListAllFeedbackLabelsRequest",
        "ListAllFeedbackLabelsResponse",
        "BulkUploadFeedbackLabelsRequest",
        "BulkUploadFeedbackLabelsResponse",
        "BulkUploadFeedbackLabelsMetadata",
        "BulkDownloadFeedbackLabelsRequest",
        "BulkDownloadFeedbackLabelsResponse",
        "BulkDownloadFeedbackLabelsMetadata",
    },
)


class ConversationView(proto.Enum):
    r"""Represents the options for viewing a conversation.

    Values:
        CONVERSATION_VIEW_UNSPECIFIED (0):
            The conversation view is not specified.

            - Defaults to ``FULL`` in ``GetConversationRequest``.
            - Defaults to ``BASIC`` in ``ListConversationsRequest``.
        FULL (2):
            Populates all fields in the conversation.
        BASIC (1):
            Populates all fields in the conversation
            except the transcript.
    """

    CONVERSATION_VIEW_UNSPECIFIED = 0
    FULL = 2
    BASIC = 1


class CalculateStatsRequest(proto.Message):
    r"""The request for calculating conversation statistics.

    Attributes:
        location (str):
            Required. The location of the conversations.
        filter (str):
            A filter to reduce results to a specific
            subset. This field is useful for getting
            statistics about conversations with specific
            properties.
    """

    location: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CalculateStatsResponse(proto.Message):
    r"""The response for calculating conversation statistics.

    Attributes:
        average_duration (google.protobuf.duration_pb2.Duration):
            The average duration of all conversations.
            The average is calculated using only
            conversations that have a time duration.
        average_turn_count (int):
            The average number of turns per conversation.
        conversation_count (int):
            The total number of conversations.
        smart_highlighter_matches (MutableMapping[str, int]):
            A map associating each smart highlighter
            display name with its respective number of
            matches in the set of conversations.
        custom_highlighter_matches (MutableMapping[str, int]):
            A map associating each custom highlighter
            resource name with its respective number of
            matches in the set of conversations.
        issue_matches (MutableMapping[str, int]):
            A map associating each issue resource name with its
            respective number of matches in the set of conversations.
            Key has the format:
            ``projects/<Project-ID>/locations/<Location-ID>/issueModels/<Issue-Model-ID>/issues/<Issue-ID>``
            Deprecated, use ``issue_matches_stats`` field instead.
        issue_matches_stats (MutableMapping[str, google.cloud.contact_center_insights_v1.types.IssueModelLabelStats.IssueStats]):
            A map associating each issue resource name with its
            respective number of matches in the set of conversations.
            Key has the format:
            ``projects/<Project-ID>/locations/<Location-ID>/issueModels/<Issue-Model-ID>/issues/<Issue-ID>``
        conversation_count_time_series (google.cloud.contact_center_insights_v1.types.CalculateStatsResponse.TimeSeries):
            A time series representing the count of
            conversations created over time that match that
            requested filter criteria.
    """

    class TimeSeries(proto.Message):
        r"""A time series representing conversations over time.

        Attributes:
            interval_duration (google.protobuf.duration_pb2.Duration):
                The duration of each interval.
            points (MutableSequence[google.cloud.contact_center_insights_v1.types.CalculateStatsResponse.TimeSeries.Interval]):
                An ordered list of intervals from earliest to
                latest, where each interval represents the
                number of conversations that transpired during
                the time window.
        """

        class Interval(proto.Message):
            r"""A single interval in a time series.

            Attributes:
                start_time (google.protobuf.timestamp_pb2.Timestamp):
                    The start time of this interval.
                conversation_count (int):
                    The number of conversations created in this
                    interval.
            """

            start_time: timestamp_pb2.Timestamp = proto.Field(
                proto.MESSAGE,
                number=1,
                message=timestamp_pb2.Timestamp,
            )
            conversation_count: int = proto.Field(
                proto.INT32,
                number=2,
            )

        interval_duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=1,
            message=duration_pb2.Duration,
        )
        points: MutableSequence["CalculateStatsResponse.TimeSeries.Interval"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message="CalculateStatsResponse.TimeSeries.Interval",
            )
        )

    average_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=1,
        message=duration_pb2.Duration,
    )
    average_turn_count: int = proto.Field(
        proto.INT32,
        number=2,
    )
    conversation_count: int = proto.Field(
        proto.INT32,
        number=3,
    )
    smart_highlighter_matches: MutableMapping[str, int] = proto.MapField(
        proto.STRING,
        proto.INT32,
        number=4,
    )
    custom_highlighter_matches: MutableMapping[str, int] = proto.MapField(
        proto.STRING,
        proto.INT32,
        number=5,
    )
    issue_matches: MutableMapping[str, int] = proto.MapField(
        proto.STRING,
        proto.INT32,
        number=6,
    )
    issue_matches_stats: MutableMapping[
        str, resources.IssueModelLabelStats.IssueStats
    ] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=8,
        message=resources.IssueModelLabelStats.IssueStats,
    )
    conversation_count_time_series: TimeSeries = proto.Field(
        proto.MESSAGE,
        number=7,
        message=TimeSeries,
    )


class CreateAnalysisOperationMetadata(proto.Message):
    r"""Metadata for a create analysis operation.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation finished
            running.
        conversation (str):
            Output only. The Conversation that this
            Analysis Operation belongs to.
        annotator_selector (google.cloud.contact_center_insights_v1.types.AnnotatorSelector):
            Output only. The annotator selector used for
            the analysis (if any).
    """

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    conversation: str = proto.Field(
        proto.STRING,
        number=3,
    )
    annotator_selector: resources.AnnotatorSelector = proto.Field(
        proto.MESSAGE,
        number=4,
        message=resources.AnnotatorSelector,
    )


class CreateConversationRequest(proto.Message):
    r"""Request to create a conversation.

    Attributes:
        parent (str):
            Required. The parent resource of the
            conversation.
        conversation (google.cloud.contact_center_insights_v1.types.Conversation):
            Required. The conversation resource to
            create.
        conversation_id (str):
            A unique ID for the new conversation. This ID will become
            the final component of the conversation's resource name. If
            no ID is specified, a server-generated ID will be used.

            This value should be 4-64 characters and must match the
            regular expression ``^[a-z0-9-]{4,64}$``. Valid characters
            are ``[a-z][0-9]-``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    conversation: resources.Conversation = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.Conversation,
    )
    conversation_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class UploadConversationRequest(proto.Message):
    r"""Request to upload a conversation.

    Attributes:
        parent (str):
            Required. The parent resource of the
            conversation.
        conversation (google.cloud.contact_center_insights_v1.types.Conversation):
            Required. The conversation resource to
            create.
        conversation_id (str):
            Optional. A unique ID for the new conversation. This ID will
            become the final component of the conversation's resource
            name. If no ID is specified, a server-generated ID will be
            used.

            This value should be 4-64 characters and must match the
            regular expression ``^[a-z0-9-]{4,64}$``. Valid characters
            are ``[a-z][0-9]-``
        redaction_config (google.cloud.contact_center_insights_v1.types.RedactionConfig):
            Optional. DLP settings for transcript
            redaction. Will default to the config specified
            in Settings.
        speech_config (google.cloud.contact_center_insights_v1.types.SpeechConfig):
            Optional. Speech-to-Text configuration. Will
            default to the config specified in Settings.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    conversation: resources.Conversation = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.Conversation,
    )
    conversation_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    redaction_config: resources.RedactionConfig = proto.Field(
        proto.MESSAGE,
        number=4,
        message=resources.RedactionConfig,
    )
    speech_config: resources.SpeechConfig = proto.Field(
        proto.MESSAGE,
        number=11,
        message=resources.SpeechConfig,
    )


class UploadConversationMetadata(proto.Message):
    r"""The metadata for an ``UploadConversation`` operation.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation finished
            running.
        request (google.cloud.contact_center_insights_v1.types.UploadConversationRequest):
            Output only. The original request.
        analysis_operation (str):
            Output only. The operation name for a
            successfully created analysis operation, if any.
        applied_redaction_config (google.cloud.contact_center_insights_v1.types.RedactionConfig):
            Output only. The redaction config applied to
            the uploaded conversation.
    """

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    request: "UploadConversationRequest" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="UploadConversationRequest",
    )
    analysis_operation: str = proto.Field(
        proto.STRING,
        number=4,
    )
    applied_redaction_config: resources.RedactionConfig = proto.Field(
        proto.MESSAGE,
        number=5,
        message=resources.RedactionConfig,
    )


class ListConversationsRequest(proto.Message):
    r"""Request to list conversations.

    Attributes:
        parent (str):
            Required. The parent resource of the
            conversation.
        page_size (int):
            The maximum number of conversations to return
            in the response. A valid page size ranges from 0
            to 100,000 inclusive. If the page size is zero
            or unspecified, a default page size of 100 will
            be chosen. Note that a call might return fewer
            results than the requested page size.
        page_token (str):
            The value returned by the last
            ``ListConversationsResponse``. This value indicates that
            this is a continuation of a prior ``ListConversations`` call
            and that the system should return the next page of data.
        filter (str):
            A filter to reduce results to a specific
            subset. Useful for querying conversations with
            specific properties.
        order_by (str):
            Optional. The attribute by which to order conversations in
            the response. If empty, conversations will be ordered by
            descending creation time. Supported values are one of the
            following:

            - create_time
            - customer_satisfaction_rating
            - duration
            - latest_analysis
            - start_time
            - turn_count

            The default sort order is ascending. To specify order,
            append ``asc`` or ``desc`` (``create_time desc``). For more
            details, see `Google AIPs
            Ordering <https://google.aip.dev/132#ordering>`__.
        view (google.cloud.contact_center_insights_v1.types.ConversationView):
            The level of details of the conversation. Default is
            ``BASIC``.
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
    order_by: str = proto.Field(
        proto.STRING,
        number=7,
    )
    view: "ConversationView" = proto.Field(
        proto.ENUM,
        number=5,
        enum="ConversationView",
    )


class ListConversationsResponse(proto.Message):
    r"""The response of listing conversations.

    Attributes:
        conversations (MutableSequence[google.cloud.contact_center_insights_v1.types.Conversation]):
            The conversations that match the request.
        next_page_token (str):
            A token which can be sent as ``page_token`` to retrieve the
            next page. If this field is set, it means there is another
            page available. If it is not set, it means no other pages
            are available.
    """

    @property
    def raw_page(self):
        return self

    conversations: MutableSequence[resources.Conversation] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Conversation,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetConversationRequest(proto.Message):
    r"""The request to get a conversation.

    Attributes:
        name (str):
            Required. The name of the conversation to
            get.
        view (google.cloud.contact_center_insights_v1.types.ConversationView):
            The level of details of the conversation. Default is
            ``FULL``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: "ConversationView" = proto.Field(
        proto.ENUM,
        number=2,
        enum="ConversationView",
    )


class UpdateConversationRequest(proto.Message):
    r"""The request to update a conversation.

    Attributes:
        conversation (google.cloud.contact_center_insights_v1.types.Conversation):
            Required. The new values for the
            conversation.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields to be updated. All possible fields can be
            updated by passing ``*``, or a subset of the following
            updateable fields can be provided:

            - ``agent_id``
            - ``language_code``
            - ``labels``
            - ``metadata``
            - ``quality_metadata``
            - ``call_metadata``
            - ``start_time``
            - ``expire_time`` or ``ttl``
            - ``data_source.gcs_source.audio_uri`` or
              ``data_source.dialogflow_source.audio_uri``
    """

    conversation: resources.Conversation = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.Conversation,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteConversationRequest(proto.Message):
    r"""The request to delete a conversation.

    Attributes:
        name (str):
            Required. The name of the conversation to
            delete.
        force (bool):
            If set to true, all of this conversation's
            analyses will also be deleted. Otherwise, the
            request will only succeed if the conversation
            has no analyses.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class IngestConversationsRequest(proto.Message):
    r"""The request to ingest conversations.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_source (google.cloud.contact_center_insights_v1.types.IngestConversationsRequest.GcsSource):
            A cloud storage bucket source. Note that any
            previously ingested objects from the source will
            be skipped to avoid duplication.

            This field is a member of `oneof`_ ``source``.
        transcript_object_config (google.cloud.contact_center_insights_v1.types.IngestConversationsRequest.TranscriptObjectConfig):
            Configuration for when ``source`` contains conversation
            transcripts.

            This field is a member of `oneof`_ ``object_config``.
        parent (str):
            Required. The parent resource for new
            conversations.
        conversation_config (google.cloud.contact_center_insights_v1.types.IngestConversationsRequest.ConversationConfig):
            Configuration that applies to all
            conversations.
        redaction_config (google.cloud.contact_center_insights_v1.types.RedactionConfig):
            Optional. DLP settings for transcript
            redaction. Optional, will default to the config
            specified in Settings.
        speech_config (google.cloud.contact_center_insights_v1.types.SpeechConfig):
            Optional. Default Speech-to-Text
            configuration. Optional, will default to the
            config specified in Settings.
        sample_size (int):
            Optional. If set, this fields indicates the
            number of objects to ingest from the Cloud
            Storage bucket. If empty, the entire bucket will
            be ingested. Unless they are first deleted,
            conversations produced through sampling won't be
            ingested by subsequent ingest requests.

            This field is a member of `oneof`_ ``_sample_size``.
    """

    class GcsSource(proto.Message):
        r"""Configuration for Cloud Storage bucket sources.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            bucket_uri (str):
                Required. The Cloud Storage bucket containing
                source objects.
            bucket_object_type (google.cloud.contact_center_insights_v1.types.IngestConversationsRequest.GcsSource.BucketObjectType):
                Optional. Specifies the type of the objects in
                ``bucket_uri``.
            metadata_bucket_uri (str):
                Optional. The Cloud Storage path to the conversation
                metadata. Note that: [1] Metadata files are expected to be
                in JSON format. [2] Metadata and source files (transcripts
                or audio) must be in separate buckets. [3] A source file and
                its corresponding metadata file must share the same name to
                be properly ingested, E.g.
                ``gs://bucket/audio/conversation1.mp3`` and
                ``gs://bucket/metadata/conversation1.json``.

                This field is a member of `oneof`_ ``_metadata_bucket_uri``.
            custom_metadata_keys (MutableSequence[str]):
                Optional. Custom keys to extract as conversation labels from
                metadata files in ``metadata_bucket_uri``. Keys not included
                in this field will be ignored. Note that there is a limit of
                100 labels per conversation.
        """

        class BucketObjectType(proto.Enum):
            r"""

            Values:
                BUCKET_OBJECT_TYPE_UNSPECIFIED (0):
                    The object type is unspecified and will default to
                    ``TRANSCRIPT``.
                TRANSCRIPT (1):
                    The object is a transcript.
                AUDIO (2):
                    The object is an audio file.
            """

            BUCKET_OBJECT_TYPE_UNSPECIFIED = 0
            TRANSCRIPT = 1
            AUDIO = 2

        bucket_uri: str = proto.Field(
            proto.STRING,
            number=1,
        )
        bucket_object_type: "IngestConversationsRequest.GcsSource.BucketObjectType" = (
            proto.Field(
                proto.ENUM,
                number=2,
                enum="IngestConversationsRequest.GcsSource.BucketObjectType",
            )
        )
        metadata_bucket_uri: str = proto.Field(
            proto.STRING,
            number=3,
            optional=True,
        )
        custom_metadata_keys: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=12,
        )

    class TranscriptObjectConfig(proto.Message):
        r"""Configuration for processing transcript objects.

        Attributes:
            medium (google.cloud.contact_center_insights_v1.types.Conversation.Medium):
                Required. The medium transcript objects
                represent.
        """

        medium: resources.Conversation.Medium = proto.Field(
            proto.ENUM,
            number=1,
            enum=resources.Conversation.Medium,
        )

    class ConversationConfig(proto.Message):
        r"""Configuration that applies to all conversations.

        Attributes:
            agent_id (str):
                Optional. An opaque, user-specified string representing a
                human agent who handled all conversations in the import.
                Note that this will be overridden if per-conversation
                metadata is provided through the ``metadata_bucket_uri``.
            agent_channel (int):
                Optional. Indicates which of the channels, 1
                or 2, contains the agent. Note that this must be
                set for conversations to be properly displayed
                and analyzed.
            customer_channel (int):
                Optional. Indicates which of the channels, 1
                or 2, contains the agent. Note that this must be
                set for conversations to be properly displayed
                and analyzed.
        """

        agent_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        agent_channel: int = proto.Field(
            proto.INT32,
            number=2,
        )
        customer_channel: int = proto.Field(
            proto.INT32,
            number=3,
        )

    gcs_source: GcsSource = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="source",
        message=GcsSource,
    )
    transcript_object_config: TranscriptObjectConfig = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="object_config",
        message=TranscriptObjectConfig,
    )
    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    conversation_config: ConversationConfig = proto.Field(
        proto.MESSAGE,
        number=4,
        message=ConversationConfig,
    )
    redaction_config: resources.RedactionConfig = proto.Field(
        proto.MESSAGE,
        number=5,
        message=resources.RedactionConfig,
    )
    speech_config: resources.SpeechConfig = proto.Field(
        proto.MESSAGE,
        number=6,
        message=resources.SpeechConfig,
    )
    sample_size: int = proto.Field(
        proto.INT32,
        number=7,
        optional=True,
    )


class IngestConversationsMetadata(proto.Message):
    r"""The metadata for an IngestConversations operation.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation finished
            running.
        request (google.cloud.contact_center_insights_v1.types.IngestConversationsRequest):
            Output only. The original request for ingest.
        partial_errors (MutableSequence[google.rpc.status_pb2.Status]):
            Output only. Partial errors during ingest
            operation that might cause the operation output
            to be incomplete.
        ingest_conversations_stats (google.cloud.contact_center_insights_v1.types.IngestConversationsMetadata.IngestConversationsStats):
            Output only. Statistics for
            IngestConversations operation.
    """

    class IngestConversationsStats(proto.Message):
        r"""Statistics for IngestConversations operation.

        Attributes:
            processed_object_count (int):
                Output only. The number of objects processed
                during the ingest operation.
            duplicates_skipped_count (int):
                Output only. The number of objects skipped
                because another conversation with the same
                transcript uri had already been ingested.
            successful_ingest_count (int):
                Output only. The number of new conversations
                added during this ingest operation.
            failed_ingest_count (int):
                Output only. The number of objects which were unable to be
                ingested due to errors. The errors are populated in the
                partial_errors field.
        """

        processed_object_count: int = proto.Field(
            proto.INT32,
            number=1,
        )
        duplicates_skipped_count: int = proto.Field(
            proto.INT32,
            number=2,
        )
        successful_ingest_count: int = proto.Field(
            proto.INT32,
            number=3,
        )
        failed_ingest_count: int = proto.Field(
            proto.INT32,
            number=4,
        )

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    request: "IngestConversationsRequest" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="IngestConversationsRequest",
    )
    partial_errors: MutableSequence[status_pb2.Status] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=status_pb2.Status,
    )
    ingest_conversations_stats: IngestConversationsStats = proto.Field(
        proto.MESSAGE,
        number=5,
        message=IngestConversationsStats,
    )


class IngestConversationsResponse(proto.Message):
    r"""The response to an IngestConversations operation."""


class CreateAnalysisRequest(proto.Message):
    r"""The request to create an analysis.

    Attributes:
        parent (str):
            Required. The parent resource of the
            analysis.
        analysis (google.cloud.contact_center_insights_v1.types.Analysis):
            Required. The analysis to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    analysis: resources.Analysis = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.Analysis,
    )


class ListAnalysesRequest(proto.Message):
    r"""The request to list analyses.

    Attributes:
        parent (str):
            Required. The parent resource of the
            analyses.
        page_size (int):
            The maximum number of analyses to return in the response. If
            this value is zero, the service will select a default size.
            A call might return fewer objects than requested. A
            non-empty ``next_page_token`` in the response indicates that
            more data is available.
        page_token (str):
            The value returned by the last ``ListAnalysesResponse``;
            indicates that this is a continuation of a prior
            ``ListAnalyses`` call and the system should return the next
            page of data.
        filter (str):
            A filter to reduce results to a specific
            subset. Useful for querying conversations with
            specific properties.
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


class ListAnalysesResponse(proto.Message):
    r"""The response to list analyses.

    Attributes:
        analyses (MutableSequence[google.cloud.contact_center_insights_v1.types.Analysis]):
            The analyses that match the request.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    analyses: MutableSequence[resources.Analysis] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Analysis,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetAnalysisRequest(proto.Message):
    r"""The request to get an analysis.

    Attributes:
        name (str):
            Required. The name of the analysis to get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteAnalysisRequest(proto.Message):
    r"""The request to delete an analysis.

    Attributes:
        name (str):
            Required. The name of the analysis to delete.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class BulkAnalyzeConversationsRequest(proto.Message):
    r"""The request to analyze conversations in bulk.

    Attributes:
        parent (str):
            Required. The parent resource to create
            analyses in.
        filter (str):
            Required. Filter used to select the subset of
            conversations to analyze.
        analysis_percentage (float):
            Required. Percentage of selected conversation to analyze,
            between [0, 100].
        annotator_selector (google.cloud.contact_center_insights_v1.types.AnnotatorSelector):
            To select the annotators to run and the
            phrase matchers to use (if any). If not
            specified, all annotators will be run.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    analysis_percentage: float = proto.Field(
        proto.FLOAT,
        number=3,
    )
    annotator_selector: resources.AnnotatorSelector = proto.Field(
        proto.MESSAGE,
        number=8,
        message=resources.AnnotatorSelector,
    )


class BulkAnalyzeConversationsMetadata(proto.Message):
    r"""The metadata for a bulk analyze conversations operation.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the operation was created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the operation finished running.
        request (google.cloud.contact_center_insights_v1.types.BulkAnalyzeConversationsRequest):
            The original request for bulk analyze.
        completed_analyses_count (int):
            The number of requested analyses that have
            completed successfully so far.
        failed_analyses_count (int):
            The number of requested analyses that have
            failed so far.
        total_requested_analyses_count (int):
            Total number of analyses requested. Computed by the number
            of conversations returned by ``filter`` multiplied by
            ``analysis_percentage`` in the request.
        partial_errors (MutableSequence[google.rpc.status_pb2.Status]):
            Output only. Partial errors during bulk
            analyze operation that might cause the operation
            output to be incomplete.
    """

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    request: "BulkAnalyzeConversationsRequest" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="BulkAnalyzeConversationsRequest",
    )
    completed_analyses_count: int = proto.Field(
        proto.INT32,
        number=4,
    )
    failed_analyses_count: int = proto.Field(
        proto.INT32,
        number=5,
    )
    total_requested_analyses_count: int = proto.Field(
        proto.INT32,
        number=6,
    )
    partial_errors: MutableSequence[status_pb2.Status] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message=status_pb2.Status,
    )


class BulkAnalyzeConversationsResponse(proto.Message):
    r"""The response for a bulk analyze conversations operation.

    Attributes:
        successful_analysis_count (int):
            Count of successful analyses.
        failed_analysis_count (int):
            Count of failed analyses.
    """

    successful_analysis_count: int = proto.Field(
        proto.INT32,
        number=1,
    )
    failed_analysis_count: int = proto.Field(
        proto.INT32,
        number=2,
    )


class BulkDeleteConversationsRequest(proto.Message):
    r"""The request to delete conversations in bulk.

    Attributes:
        parent (str):
            Required. The parent resource to delete
            conversations from. Format:

            projects/{project}/locations/{location}
        filter (str):
            Filter used to select the subset of
            conversations to delete.
        max_delete_count (int):
            Maximum number of conversations to delete.
        force (bool):
            If set to true, all of this conversation's
            analyses will also be deleted. Otherwise, the
            request will only succeed if the conversation
            has no analyses.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    max_delete_count: int = proto.Field(
        proto.INT32,
        number=3,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class BulkDeleteConversationsMetadata(proto.Message):
    r"""The metadata for a bulk delete conversations operation.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the operation was created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the operation finished running.
        request (google.cloud.contact_center_insights_v1.types.BulkDeleteConversationsRequest):
            The original request for bulk delete.
        partial_errors (MutableSequence[google.rpc.status_pb2.Status]):
            Partial errors during bulk delete
            conversations operation that might cause the
            operation output to be incomplete.
    """

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    request: "BulkDeleteConversationsRequest" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="BulkDeleteConversationsRequest",
    )
    partial_errors: MutableSequence[status_pb2.Status] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=status_pb2.Status,
    )


class BulkDeleteConversationsResponse(proto.Message):
    r"""The response for a bulk delete conversations operation."""


class ExportInsightsDataRequest(proto.Message):
    r"""The request to export insights.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        big_query_destination (google.cloud.contact_center_insights_v1.types.ExportInsightsDataRequest.BigQueryDestination):
            Specified if sink is a BigQuery table.

            This field is a member of `oneof`_ ``destination``.
        parent (str):
            Required. The parent resource to export data
            from.
        filter (str):
            A filter to reduce results to a specific
            subset. Useful for exporting conversations with
            specific properties.
        kms_key (str):
            A fully qualified KMS key name for BigQuery
            tables protected by CMEK. Format:

            projects/{project}/locations/{location}/keyRings/{keyring}/cryptoKeys/{key}/cryptoKeyVersions/{version}
        write_disposition (google.cloud.contact_center_insights_v1.types.ExportInsightsDataRequest.WriteDisposition):
            Options for what to do if the destination
            table already exists.
    """

    class WriteDisposition(proto.Enum):
        r"""Specifies the action that occurs if the destination table
        already exists.

        Values:
            WRITE_DISPOSITION_UNSPECIFIED (0):
                Write disposition is not specified. Defaults to
                WRITE_TRUNCATE.
            WRITE_TRUNCATE (1):
                If the table already exists, BigQuery will
                overwrite the table data and use the schema from
                the load.
            WRITE_APPEND (2):
                If the table already exists, BigQuery will
                append data to the table.
        """

        WRITE_DISPOSITION_UNSPECIFIED = 0
        WRITE_TRUNCATE = 1
        WRITE_APPEND = 2

    class BigQueryDestination(proto.Message):
        r"""A BigQuery Table Reference.

        Attributes:
            project_id (str):
                A project ID or number. If specified, then
                export will attempt to write data to this
                project instead of the resource project.
                Otherwise, the resource project will be used.
            dataset (str):
                Required. The name of the BigQuery dataset that the snapshot
                result should be exported to. If this dataset does not
                exist, the export call returns an INVALID_ARGUMENT error.
            table (str):
                The BigQuery table name to which the insights data should be
                written. If this table does not exist, the export call
                returns an INVALID_ARGUMENT error.
        """

        project_id: str = proto.Field(
            proto.STRING,
            number=3,
        )
        dataset: str = proto.Field(
            proto.STRING,
            number=1,
        )
        table: str = proto.Field(
            proto.STRING,
            number=2,
        )

    big_query_destination: BigQueryDestination = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="destination",
        message=BigQueryDestination,
    )
    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=3,
    )
    kms_key: str = proto.Field(
        proto.STRING,
        number=4,
    )
    write_disposition: WriteDisposition = proto.Field(
        proto.ENUM,
        number=5,
        enum=WriteDisposition,
    )


class ExportInsightsDataMetadata(proto.Message):
    r"""Metadata for an export insights operation.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation finished
            running.
        request (google.cloud.contact_center_insights_v1.types.ExportInsightsDataRequest):
            The original request for export.
        partial_errors (MutableSequence[google.rpc.status_pb2.Status]):
            Partial errors during export operation that
            might cause the operation output to be
            incomplete.
    """

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    request: "ExportInsightsDataRequest" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ExportInsightsDataRequest",
    )
    partial_errors: MutableSequence[status_pb2.Status] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=status_pb2.Status,
    )


class ExportInsightsDataResponse(proto.Message):
    r"""Response for an export insights operation."""


class CreateIssueModelRequest(proto.Message):
    r"""The request to create an issue model.

    Attributes:
        parent (str):
            Required. The parent resource of the issue
            model.
        issue_model (google.cloud.contact_center_insights_v1.types.IssueModel):
            Required. The issue model to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    issue_model: resources.IssueModel = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.IssueModel,
    )


class CreateIssueModelMetadata(proto.Message):
    r"""Metadata for creating an issue model.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation finished
            running.
        request (google.cloud.contact_center_insights_v1.types.CreateIssueModelRequest):
            The original request for creation.
    """

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    request: "CreateIssueModelRequest" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="CreateIssueModelRequest",
    )


class UpdateIssueModelRequest(proto.Message):
    r"""The request to update an issue model.

    Attributes:
        issue_model (google.cloud.contact_center_insights_v1.types.IssueModel):
            Required. The new values for the issue model.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields to be updated.
    """

    issue_model: resources.IssueModel = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.IssueModel,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class ListIssueModelsRequest(proto.Message):
    r"""Request to list issue models.

    Attributes:
        parent (str):
            Required. The parent resource of the issue
            model.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListIssueModelsResponse(proto.Message):
    r"""The response of listing issue models.

    Attributes:
        issue_models (MutableSequence[google.cloud.contact_center_insights_v1.types.IssueModel]):
            The issue models that match the request.
    """

    issue_models: MutableSequence[resources.IssueModel] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.IssueModel,
    )


class GetIssueModelRequest(proto.Message):
    r"""The request to get an issue model.

    Attributes:
        name (str):
            Required. The name of the issue model to get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteIssueModelRequest(proto.Message):
    r"""The request to delete an issue model.

    Attributes:
        name (str):
            Required. The name of the issue model to
            delete.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteIssueModelMetadata(proto.Message):
    r"""Metadata for deleting an issue model.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation finished
            running.
        request (google.cloud.contact_center_insights_v1.types.DeleteIssueModelRequest):
            The original request for deletion.
    """

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    request: "DeleteIssueModelRequest" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="DeleteIssueModelRequest",
    )


class DeployIssueModelRequest(proto.Message):
    r"""The request to deploy an issue model.

    Attributes:
        name (str):
            Required. The issue model to deploy.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeployIssueModelResponse(proto.Message):
    r"""The response to deploy an issue model."""


class DeployIssueModelMetadata(proto.Message):
    r"""Metadata for deploying an issue model.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation finished
            running.
        request (google.cloud.contact_center_insights_v1.types.DeployIssueModelRequest):
            The original request for deployment.
    """

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    request: "DeployIssueModelRequest" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="DeployIssueModelRequest",
    )


class UndeployIssueModelRequest(proto.Message):
    r"""The request to undeploy an issue model.

    Attributes:
        name (str):
            Required. The issue model to undeploy.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UndeployIssueModelResponse(proto.Message):
    r"""The response to undeploy an issue model."""


class UndeployIssueModelMetadata(proto.Message):
    r"""Metadata for undeploying an issue model.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation finished
            running.
        request (google.cloud.contact_center_insights_v1.types.UndeployIssueModelRequest):
            The original request for undeployment.
    """

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    request: "UndeployIssueModelRequest" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="UndeployIssueModelRequest",
    )


class ExportIssueModelRequest(proto.Message):
    r"""Request to export an issue model.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_destination (google.cloud.contact_center_insights_v1.types.ExportIssueModelRequest.GcsDestination):
            Google Cloud Storage URI to export the issue
            model to.

            This field is a member of `oneof`_ ``Destination``.
        name (str):
            Required. The issue model to export.
    """

    class GcsDestination(proto.Message):
        r"""Google Cloud Storage Object URI to save the issue model to.

        Attributes:
            object_uri (str):
                Required. Format: ``gs://<bucket-name>/<object-name>``
        """

        object_uri: str = proto.Field(
            proto.STRING,
            number=1,
        )

    gcs_destination: GcsDestination = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="Destination",
        message=GcsDestination,
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ExportIssueModelResponse(proto.Message):
    r"""Response from export issue model"""


class ExportIssueModelMetadata(proto.Message):
    r"""Metadata used for export issue model.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the operation was created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the operation finished running.
        request (google.cloud.contact_center_insights_v1.types.ExportIssueModelRequest):
            The original export request.
    """

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    request: "ExportIssueModelRequest" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ExportIssueModelRequest",
    )


class ImportIssueModelRequest(proto.Message):
    r"""Request to import an issue model.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_source (google.cloud.contact_center_insights_v1.types.ImportIssueModelRequest.GcsSource):
            Google Cloud Storage source message.

            This field is a member of `oneof`_ ``Source``.
        parent (str):
            Required. The parent resource of the issue
            model.
        create_new_model (bool):
            Optional. If set to true, will create an
            issue model from the imported file with randomly
            generated IDs for the issue model and
            corresponding issues. Otherwise, replaces an
            existing model with the same ID as the file.
    """

    class GcsSource(proto.Message):
        r"""Google Cloud Storage Object URI to get the issue model file
        from.

        Attributes:
            object_uri (str):
                Required. Format: ``gs://<bucket-name>/<object-name>``
        """

        object_uri: str = proto.Field(
            proto.STRING,
            number=1,
        )

    gcs_source: GcsSource = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="Source",
        message=GcsSource,
    )
    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_new_model: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class ImportIssueModelResponse(proto.Message):
    r"""Response from import issue model"""


class ImportIssueModelMetadata(proto.Message):
    r"""Metadata used for import issue model.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the operation was created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the operation finished running.
        request (google.cloud.contact_center_insights_v1.types.ImportIssueModelRequest):
            The original import request.
    """

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    request: "ImportIssueModelRequest" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ImportIssueModelRequest",
    )


class GetIssueRequest(proto.Message):
    r"""The request to get an issue.

    Attributes:
        name (str):
            Required. The name of the issue to get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListIssuesRequest(proto.Message):
    r"""Request to list issues.

    Attributes:
        parent (str):
            Required. The parent resource of the issue.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListIssuesResponse(proto.Message):
    r"""The response of listing issues.

    Attributes:
        issues (MutableSequence[google.cloud.contact_center_insights_v1.types.Issue]):
            The issues that match the request.
    """

    issues: MutableSequence[resources.Issue] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Issue,
    )


class UpdateIssueRequest(proto.Message):
    r"""The request to update an issue.

    Attributes:
        issue (google.cloud.contact_center_insights_v1.types.Issue):
            Required. The new values for the issue.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields to be updated.
    """

    issue: resources.Issue = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.Issue,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteIssueRequest(proto.Message):
    r"""The request to delete an issue.

    Attributes:
        name (str):
            Required. The name of the issue to delete.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CalculateIssueModelStatsRequest(proto.Message):
    r"""Request to get statistics of an issue model.

    Attributes:
        issue_model (str):
            Required. The resource name of the issue
            model to query against.
    """

    issue_model: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CalculateIssueModelStatsResponse(proto.Message):
    r"""Response of querying an issue model's statistics.

    Attributes:
        current_stats (google.cloud.contact_center_insights_v1.types.IssueModelLabelStats):
            The latest label statistics for the queried
            issue model. Includes results on both training
            data and data labeled after deployment.
    """

    current_stats: resources.IssueModelLabelStats = proto.Field(
        proto.MESSAGE,
        number=4,
        message=resources.IssueModelLabelStats,
    )


class CreatePhraseMatcherRequest(proto.Message):
    r"""Request to create a phrase matcher.

    Attributes:
        parent (str):
            Required. The parent resource of the phrase matcher.
            Required. The location to create a phrase matcher for.
            Format: ``projects/<Project ID>/locations/<Location ID>`` or
            ``projects/<Project Number>/locations/<Location ID>``
        phrase_matcher (google.cloud.contact_center_insights_v1.types.PhraseMatcher):
            Required. The phrase matcher resource to
            create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    phrase_matcher: resources.PhraseMatcher = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.PhraseMatcher,
    )


class ListPhraseMatchersRequest(proto.Message):
    r"""Request to list phrase matchers.

    Attributes:
        parent (str):
            Required. The parent resource of the phrase
            matcher.
        page_size (int):
            The maximum number of phrase matchers to return in the
            response. If this value is zero, the service will select a
            default size. A call might return fewer objects than
            requested. A non-empty ``next_page_token`` in the response
            indicates that more data is available.
        page_token (str):
            The value returned by the last
            ``ListPhraseMatchersResponse``. This value indicates that
            this is a continuation of a prior ``ListPhraseMatchers``
            call and that the system should return the next page of
            data.
        filter (str):
            A filter to reduce results to a specific
            subset. Useful for querying phrase matchers with
            specific properties.
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


class ListPhraseMatchersResponse(proto.Message):
    r"""The response of listing phrase matchers.

    Attributes:
        phrase_matchers (MutableSequence[google.cloud.contact_center_insights_v1.types.PhraseMatcher]):
            The phrase matchers that match the request.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    phrase_matchers: MutableSequence[resources.PhraseMatcher] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.PhraseMatcher,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetPhraseMatcherRequest(proto.Message):
    r"""The request to get a a phrase matcher.

    Attributes:
        name (str):
            Required. The name of the phrase matcher to
            get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeletePhraseMatcherRequest(proto.Message):
    r"""The request to delete a phrase matcher.

    Attributes:
        name (str):
            Required. The name of the phrase matcher to
            delete.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdatePhraseMatcherRequest(proto.Message):
    r"""The request to update a phrase matcher.

    Attributes:
        phrase_matcher (google.cloud.contact_center_insights_v1.types.PhraseMatcher):
            Required. The new values for the phrase
            matcher.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields to be updated.
    """

    phrase_matcher: resources.PhraseMatcher = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.PhraseMatcher,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class GetSettingsRequest(proto.Message):
    r"""The request to get project-level settings.

    Attributes:
        name (str):
            Required. The name of the settings resource
            to get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateSettingsRequest(proto.Message):
    r"""The request to update project-level settings.

    Attributes:
        settings (google.cloud.contact_center_insights_v1.types.Settings):
            Required. The new settings values.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to be updated.
    """

    settings: resources.Settings = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.Settings,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class CreateAnalysisRuleRequest(proto.Message):
    r"""The request to create a analysis rule. analysis_rule_id will be
    generated by the server.

    Attributes:
        parent (str):
            Required. The parent resource of the analysis rule.
            Required. The location to create a analysis rule for.
            Format: ``projects/<Project ID>/locations/<Location ID>`` or
            ``projects/<Project Number>/locations/<Location ID>``
        analysis_rule (google.cloud.contact_center_insights_v1.types.AnalysisRule):
            Required. The analysis rule resource to
            create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    analysis_rule: resources.AnalysisRule = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.AnalysisRule,
    )


class GetAnalysisRuleRequest(proto.Message):
    r"""The request for getting a analysis rule.

    Attributes:
        name (str):
            Required. The name of the AnalysisRule to
            get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateAnalysisRuleRequest(proto.Message):
    r"""The request to update a analysis rule.

    Attributes:
        analysis_rule (google.cloud.contact_center_insights_v1.types.AnalysisRule):
            Required. The new analysis rule.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to be updated. If the
            update_mask is not provided, the update will be applied to
            all fields.
    """

    analysis_rule: resources.AnalysisRule = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.AnalysisRule,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteAnalysisRuleRequest(proto.Message):
    r"""The request to delete a analysis rule.

    Attributes:
        name (str):
            Required. The name of the analysis rule to
            delete.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListAnalysisRulesRequest(proto.Message):
    r"""The request to list analysis rules.

    Attributes:
        parent (str):
            Required. The parent resource of the analysis
            rules.
        page_size (int):
            Optional. The maximum number of analysis rule to return in
            the response. If this value is zero, the service will select
            a default size. A call may return fewer objects than
            requested. A non-empty ``next_page_token`` in the response
            indicates that more data is available.
        page_token (str):
            Optional. The value returned by the last
            ``ListAnalysisRulesResponse``; indicates that this is a
            continuation of a prior ``ListAnalysisRules`` call and the
            system should return the next page of data.
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


class ListAnalysisRulesResponse(proto.Message):
    r"""The response of listing views.

    Attributes:
        analysis_rules (MutableSequence[google.cloud.contact_center_insights_v1.types.AnalysisRule]):
            The analysis_rule that match the request.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    analysis_rules: MutableSequence[resources.AnalysisRule] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.AnalysisRule,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetEncryptionSpecRequest(proto.Message):
    r"""The request to get location-level encryption specification.

    Attributes:
        name (str):
            Required. The name of the encryption spec
            resource to get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class InitializeEncryptionSpecRequest(proto.Message):
    r"""The request to initialize a location-level encryption
    specification.

    Attributes:
        encryption_spec (google.cloud.contact_center_insights_v1.types.EncryptionSpec):
            Required. The encryption spec used for CMEK encryption. It
            is required that the kms key is in the same region as the
            endpoint. The same key will be used for all provisioned
            resources, if encryption is available. If the
            ``kms_key_name`` field is left empty, no encryption will be
            enforced.
    """

    encryption_spec: resources.EncryptionSpec = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.EncryptionSpec,
    )


class InitializeEncryptionSpecResponse(proto.Message):
    r"""The response to initialize a location-level encryption
    specification.

    """


class InitializeEncryptionSpecMetadata(proto.Message):
    r"""Metadata for initializing a location-level encryption
    specification.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation finished
            running.
        request (google.cloud.contact_center_insights_v1.types.InitializeEncryptionSpecRequest):
            Output only. The original request for
            initialization.
        partial_errors (MutableSequence[google.rpc.status_pb2.Status]):
            Partial errors during initializing operation
            that might cause the operation output to be
            incomplete.
    """

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    request: "InitializeEncryptionSpecRequest" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="InitializeEncryptionSpecRequest",
    )
    partial_errors: MutableSequence[status_pb2.Status] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=status_pb2.Status,
    )


class CreateViewRequest(proto.Message):
    r"""The request to create a view.

    Attributes:
        parent (str):
            Required. The parent resource of the view. Required. The
            location to create a view for. Format:
            ``projects/<Project ID>/locations/<Location ID>`` or
            ``projects/<Project Number>/locations/<Location ID>``
        view (google.cloud.contact_center_insights_v1.types.View):
            Required. The view resource to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: resources.View = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.View,
    )


class GetViewRequest(proto.Message):
    r"""The request to get a view.

    Attributes:
        name (str):
            Required. The name of the view to get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListViewsRequest(proto.Message):
    r"""The request to list views.

    Attributes:
        parent (str):
            Required. The parent resource of the views.
        page_size (int):
            The maximum number of views to return in the response. If
            this value is zero, the service will select a default size.
            A call may return fewer objects than requested. A non-empty
            ``next_page_token`` in the response indicates that more data
            is available.
        page_token (str):
            The value returned by the last ``ListViewsResponse``;
            indicates that this is a continuation of a prior
            ``ListViews`` call and the system should return the next
            page of data.
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


class ListViewsResponse(proto.Message):
    r"""The response of listing views.

    Attributes:
        views (MutableSequence[google.cloud.contact_center_insights_v1.types.View]):
            The views that match the request.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    views: MutableSequence[resources.View] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.View,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateViewRequest(proto.Message):
    r"""The request to update a view.

    Attributes:
        view (google.cloud.contact_center_insights_v1.types.View):
            Required. The new view.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields to be updated.
    """

    view: resources.View = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.View,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteViewRequest(proto.Message):
    r"""The request to delete a view.

    Attributes:
        name (str):
            Required. The name of the view to delete.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Dimension(proto.Message):
    r"""A dimension determines the grouping key for the query. In SQL
    terms, these would be part of both the "SELECT" and "GROUP BY"
    clauses.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        issue_dimension_metadata (google.cloud.contact_center_insights_v1.types.Dimension.IssueDimensionMetadata):
            Output only. Metadata about the issue
            dimension.

            This field is a member of `oneof`_ ``dimension_metadata``.
        agent_dimension_metadata (google.cloud.contact_center_insights_v1.types.Dimension.AgentDimensionMetadata):
            Output only. Metadata about the agent
            dimension.

            This field is a member of `oneof`_ ``dimension_metadata``.
        qa_question_dimension_metadata (google.cloud.contact_center_insights_v1.types.Dimension.QaQuestionDimensionMetadata):
            Output only. Metadata about the QA question
            dimension.

            This field is a member of `oneof`_ ``dimension_metadata``.
        qa_question_answer_dimension_metadata (google.cloud.contact_center_insights_v1.types.Dimension.QaQuestionAnswerDimensionMetadata):
            Output only. Metadata about the QA
            question-answer dimension.

            This field is a member of `oneof`_ ``dimension_metadata``.
        dimension_key (google.cloud.contact_center_insights_v1.types.Dimension.DimensionKey):
            The key of the dimension.
    """

    class DimensionKey(proto.Enum):
        r"""The key of the dimension.

        Values:
            DIMENSION_KEY_UNSPECIFIED (0):
                The key of the dimension is unspecified.
            ISSUE (1):
                The dimension is keyed by issues.
            AGENT (2):
                The dimension is keyed by agents.
            AGENT_TEAM (3):
                The dimension is keyed by agent teams.
            QA_QUESTION_ID (4):
                The dimension is keyed by QaQuestionIds.
                Note that: We only group by the QuestionId and
                not the revision-id of the scorecard this
                question is a part of. This allows for showing
                stats for the same question across different
                scorecard revisions.
            QA_QUESTION_ANSWER_VALUE (5):
                The dimension is keyed by
                QaQuestionIds-Answer value pairs. Note that: We
                only group by the QuestionId and not the
                revision-id of the scorecard this question is a
                part of. This allows for showing distribution of
                answers per question across different scorecard
                revisions.
            CONVERSATION_PROFILE_ID (6):
                The dimension is keyed by the conversation
                profile ID.
        """

        DIMENSION_KEY_UNSPECIFIED = 0
        ISSUE = 1
        AGENT = 2
        AGENT_TEAM = 3
        QA_QUESTION_ID = 4
        QA_QUESTION_ANSWER_VALUE = 5
        CONVERSATION_PROFILE_ID = 6

    class IssueDimensionMetadata(proto.Message):
        r"""Metadata about the issue dimension.

        Attributes:
            issue_id (str):
                The issue ID.
            issue_display_name (str):
                The issue display name.
            issue_model_id (str):
                The parent issue model ID.
        """

        issue_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        issue_display_name: str = proto.Field(
            proto.STRING,
            number=2,
        )
        issue_model_id: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class AgentDimensionMetadata(proto.Message):
        r"""Metadata about the agent dimension.

        Attributes:
            agent_id (str):
                Optional. A user-specified string
                representing the agent.
            agent_display_name (str):
                Optional. The agent's name
            agent_team (str):
                Optional. A user-specified string
                representing the agent's team.
        """

        agent_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        agent_display_name: str = proto.Field(
            proto.STRING,
            number=2,
        )
        agent_team: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class QaQuestionDimensionMetadata(proto.Message):
        r"""Metadata about the QA question dimension.

        Attributes:
            qa_scorecard_id (str):
                Optional. The QA scorecard ID.
            qa_question_id (str):
                Optional. The QA question ID.
            question_body (str):
                Optional. The full body of the question.
        """

        qa_scorecard_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        qa_question_id: str = proto.Field(
            proto.STRING,
            number=2,
        )
        question_body: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class QaQuestionAnswerDimensionMetadata(proto.Message):
        r"""Metadata about the QA question-answer dimension.
        This is useful for showing the answer distribution for questions
        for a given scorecard.

        Attributes:
            qa_scorecard_id (str):
                Optional. The QA scorecard ID.
            qa_question_id (str):
                Optional. The QA question ID.
            question_body (str):
                Optional. The full body of the question.
            answer_value (str):
                Optional. The full body of the question.
        """

        qa_scorecard_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        qa_question_id: str = proto.Field(
            proto.STRING,
            number=2,
        )
        question_body: str = proto.Field(
            proto.STRING,
            number=3,
        )
        answer_value: str = proto.Field(
            proto.STRING,
            number=4,
        )

    issue_dimension_metadata: IssueDimensionMetadata = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="dimension_metadata",
        message=IssueDimensionMetadata,
    )
    agent_dimension_metadata: AgentDimensionMetadata = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="dimension_metadata",
        message=AgentDimensionMetadata,
    )
    qa_question_dimension_metadata: QaQuestionDimensionMetadata = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="dimension_metadata",
        message=QaQuestionDimensionMetadata,
    )
    qa_question_answer_dimension_metadata: QaQuestionAnswerDimensionMetadata = (
        proto.Field(
            proto.MESSAGE,
            number=5,
            oneof="dimension_metadata",
            message=QaQuestionAnswerDimensionMetadata,
        )
    )
    dimension_key: DimensionKey = proto.Field(
        proto.ENUM,
        number=1,
        enum=DimensionKey,
    )


class QueryMetricsRequest(proto.Message):
    r"""The request for querying metrics.

    Attributes:
        location (str):
            Required. The location of the data.
            "projects/{project}/locations/{location}".
        filter (str):
            Required. Filter to select a subset of conversations to
            compute the metrics. Must specify a window of the
            conversation create time to compute the metrics. The
            returned metrics will be from the range [DATE(starting
            create time), DATE(ending create time)).
        time_granularity (google.cloud.contact_center_insights_v1.types.QueryMetricsRequest.TimeGranularity):
            The time granularity of each data point in
            the time series. Defaults to NONE if this field
            is unspecified.
        dimensions (MutableSequence[google.cloud.contact_center_insights_v1.types.Dimension]):
            The dimensions that determine the grouping
            key for the query. Defaults to no dimension if
            this field is unspecified. If a dimension is
            specified, its key must also be specified. Each
            dimension's key must be unique.

            If a time granularity is also specified, metric
            values in the dimension will be bucketed by this
            granularity.

            Up to one dimension is supported for now.
        measure_mask (google.protobuf.field_mask_pb2.FieldMask):
            Measures to return. Defaults to all measures if this field
            is unspecified. A valid mask should traverse from the
            ``measure`` field from the response. For example, a path
            from a measure mask to get the conversation count is
            "conversation_measure.count".
    """

    class TimeGranularity(proto.Enum):
        r"""A time granularity divides the time line into discrete time
        periods. This is useful for defining buckets over which
        filtering and aggregation should be performed.

        Values:
            TIME_GRANULARITY_UNSPECIFIED (0):
                The time granularity is unspecified and will
                default to NONE.
            NONE (1):
                No time granularity. The response won't
                contain a time series. This is the default value
                if no time granularity is specified.
            DAILY (2):
                Data points in the time series will aggregate at a daily
                granularity. 1 day means [midnight to midnight).
            HOURLY (3):
                Data points in the time series will aggregate at a daily
                granularity. 1 HOUR means [01:00 to 02:00).
            PER_MINUTE (4):
                Data points in the time series will aggregate at a daily
                granularity. PER_MINUTE means [01:00 to 01:01).
            PER_5_MINUTES (5):
                Data points in the time series will aggregate at a 1 minute
                granularity. PER_5_MINUTES means [01:00 to 01:05).
            MONTHLY (6):
                Data points in the time series will aggregate at a monthly
                granularity. 1 MONTH means [01st of the month to 1st of the
                next month).
        """

        TIME_GRANULARITY_UNSPECIFIED = 0
        NONE = 1
        DAILY = 2
        HOURLY = 3
        PER_MINUTE = 4
        PER_5_MINUTES = 5
        MONTHLY = 6

    location: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    time_granularity: TimeGranularity = proto.Field(
        proto.ENUM,
        number=3,
        enum=TimeGranularity,
    )
    dimensions: MutableSequence["Dimension"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="Dimension",
    )
    measure_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=5,
        message=field_mask_pb2.FieldMask,
    )


class QueryMetricsResponse(proto.Message):
    r"""The response for querying metrics.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        location (str):
            Required. The location of the data.
            "projects/{project}/locations/{location}".
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            The metrics last update time.
        slices (MutableSequence[google.cloud.contact_center_insights_v1.types.QueryMetricsResponse.Slice]):
            A slice contains a total and (if the request
            specified a time granularity) a time series of
            metric values. Each slice contains a unique
            combination of the cardinality of dimensions
            from the request.
        macro_average_slice (google.cloud.contact_center_insights_v1.types.QueryMetricsResponse.Slice):
            The macro average slice contains aggregated averages across
            the selected dimension. i.e. if group_by agent is specified
            this field will contain the average across all agents. This
            field is only populated if the request specifies a
            Dimension.

            This field is a member of `oneof`_ ``_macro_average_slice``.
    """

    class Slice(proto.Message):
        r"""A slice contains a total and (if the request specified a time
        granularity) a time series of metric values. Each slice contains a
        unique combination of the cardinality of dimensions from the
        request.

        For example, if the request specifies a single ISSUE dimension and
        it has a cardinality of 2 (i.e. the data used to compute the metrics
        has 2 issues in total), the response will have 2 slices:

        - Slice 1 -> dimensions=[Issue 1]
        - Slice 2 -> dimensions=[Issue 2]

        Attributes:
            dimensions (MutableSequence[google.cloud.contact_center_insights_v1.types.Dimension]):
                A unique combination of dimensions that this
                slice represents.
            total (google.cloud.contact_center_insights_v1.types.QueryMetricsResponse.Slice.DataPoint):
                The total metric value. The interval of this data point is
                [starting create time, ending create time) from the request.
            time_series (google.cloud.contact_center_insights_v1.types.QueryMetricsResponse.Slice.TimeSeries):
                A time series of metric values. This is only
                populated if the request specifies a time
                granularity other than NONE.
        """

        class DataPoint(proto.Message):
            r"""A data point contains the metric values mapped to an
            interval.


            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                conversation_measure (google.cloud.contact_center_insights_v1.types.QueryMetricsResponse.Slice.DataPoint.ConversationMeasure):
                    The measure related to conversations.

                    This field is a member of `oneof`_ ``measure``.
                interval (google.type.interval_pb2.Interval):
                    The interval that this data point represents.

                    - If this is the total data point, the interval is [starting
                      create time, ending create time) from the request.
                    - If this a data point from the time series, the interval is
                      [time, time + time granularity from the request).
            """

            class ConversationMeasure(proto.Message):
                r"""The measure related to conversations.

                .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

                Attributes:
                    conversation_count (int):
                        The conversation count.

                        This field is a member of `oneof`_ ``_conversation_count``.
                    average_silence_percentage (float):
                        The average silence percentage.

                        This field is a member of `oneof`_ ``_average_silence_percentage``.
                    average_duration (google.protobuf.duration_pb2.Duration):
                        The average duration.

                        This field is a member of `oneof`_ ``_average_duration``.
                    average_turn_count (float):
                        The average turn count.

                        This field is a member of `oneof`_ ``_average_turn_count``.
                    average_agent_sentiment_score (float):
                        The average agent's sentiment score.

                        This field is a member of `oneof`_ ``_average_agent_sentiment_score``.
                    average_client_sentiment_score (float):
                        The average client's sentiment score.

                        This field is a member of `oneof`_ ``_average_client_sentiment_score``.
                    average_customer_satisfaction_rating (float):
                        The average customer satisfaction rating.

                        This field is a member of `oneof`_ ``_average_customer_satisfaction_rating``.
                    average_qa_normalized_score (float):
                        Average QA normalized score.
                        Will exclude 0's in average calculation.

                        This field is a member of `oneof`_ ``_average_qa_normalized_score``.
                    qa_tag_scores (MutableSequence[google.cloud.contact_center_insights_v1.types.QueryMetricsResponse.Slice.DataPoint.ConversationMeasure.QaTagScore]):
                        Average QA normalized score for all the tags.
                    average_qa_question_normalized_score (float):
                        Average QA normalized score averaged for questions averaged
                        across all revisions of the parent scorecard. Will be only
                        populated if the request specifies a dimension of
                        QA_QUESTION_ID.

                        This field is a member of `oneof`_ ``_average_qa_question_normalized_score``.
                """

                class QaTagScore(proto.Message):
                    r"""Average QA normalized score for the tag.

                    Attributes:
                        tag (str):
                            Tag name.
                        average_tag_normalized_score (float):
                            Average tag normalized score per tag.
                    """

                    tag: str = proto.Field(
                        proto.STRING,
                        number=1,
                    )
                    average_tag_normalized_score: float = proto.Field(
                        proto.DOUBLE,
                        number=2,
                    )

                conversation_count: int = proto.Field(
                    proto.INT32,
                    number=1,
                    optional=True,
                )
                average_silence_percentage: float = proto.Field(
                    proto.FLOAT,
                    number=2,
                    optional=True,
                )
                average_duration: duration_pb2.Duration = proto.Field(
                    proto.MESSAGE,
                    number=3,
                    optional=True,
                    message=duration_pb2.Duration,
                )
                average_turn_count: float = proto.Field(
                    proto.FLOAT,
                    number=4,
                    optional=True,
                )
                average_agent_sentiment_score: float = proto.Field(
                    proto.FLOAT,
                    number=5,
                    optional=True,
                )
                average_client_sentiment_score: float = proto.Field(
                    proto.FLOAT,
                    number=6,
                    optional=True,
                )
                average_customer_satisfaction_rating: float = proto.Field(
                    proto.DOUBLE,
                    number=8,
                    optional=True,
                )
                average_qa_normalized_score: float = proto.Field(
                    proto.DOUBLE,
                    number=7,
                    optional=True,
                )
                qa_tag_scores: MutableSequence[
                    "QueryMetricsResponse.Slice.DataPoint.ConversationMeasure.QaTagScore"
                ] = proto.RepeatedField(
                    proto.MESSAGE,
                    number=9,
                    message="QueryMetricsResponse.Slice.DataPoint.ConversationMeasure.QaTagScore",
                )
                average_qa_question_normalized_score: float = proto.Field(
                    proto.DOUBLE,
                    number=10,
                    optional=True,
                )

            conversation_measure: "QueryMetricsResponse.Slice.DataPoint.ConversationMeasure" = proto.Field(
                proto.MESSAGE,
                number=2,
                oneof="measure",
                message="QueryMetricsResponse.Slice.DataPoint.ConversationMeasure",
            )
            interval: interval_pb2.Interval = proto.Field(
                proto.MESSAGE,
                number=1,
                message=interval_pb2.Interval,
            )

        class TimeSeries(proto.Message):
            r"""A time series of metric values.

            Attributes:
                data_points (MutableSequence[google.cloud.contact_center_insights_v1.types.QueryMetricsResponse.Slice.DataPoint]):
                    The data points that make up the time series
                    .
            """

            data_points: MutableSequence["QueryMetricsResponse.Slice.DataPoint"] = (
                proto.RepeatedField(
                    proto.MESSAGE,
                    number=4,
                    message="QueryMetricsResponse.Slice.DataPoint",
                )
            )

        dimensions: MutableSequence["Dimension"] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="Dimension",
        )
        total: "QueryMetricsResponse.Slice.DataPoint" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="QueryMetricsResponse.Slice.DataPoint",
        )
        time_series: "QueryMetricsResponse.Slice.TimeSeries" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="QueryMetricsResponse.Slice.TimeSeries",
        )

    location: str = proto.Field(
        proto.STRING,
        number=1,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    slices: MutableSequence[Slice] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=Slice,
    )
    macro_average_slice: Slice = proto.Field(
        proto.MESSAGE,
        number=4,
        optional=True,
        message=Slice,
    )


class QueryMetricsMetadata(proto.Message):
    r"""The metadata from querying metrics."""


class CreateQaQuestionRequest(proto.Message):
    r"""The request for creating a QaQuestion.

    Attributes:
        parent (str):
            Required. The parent resource of the
            QaQuestion.
        qa_question (google.cloud.contact_center_insights_v1.types.QaQuestion):
            Required. The QaQuestion to create.
        qa_question_id (str):
            Optional. A unique ID for the new question. This ID will
            become the final component of the question's resource name.
            If no ID is specified, a server-generated ID will be used.

            This value should be 4-64 characters and must match the
            regular expression ``^[a-z0-9-]{4,64}$``. Valid characters
            are ``[a-z][0-9]-``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    qa_question: resources.QaQuestion = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.QaQuestion,
    )
    qa_question_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GetQaQuestionRequest(proto.Message):
    r"""The request for a QaQuestion.

    Attributes:
        name (str):
            Required. The name of the QaQuestion to get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListQaQuestionsRequest(proto.Message):
    r"""Request to list QaQuestions.

    Attributes:
        parent (str):
            Required. The parent resource of the
            questions.
        page_size (int):
            Optional. The maximum number of questions to return in the
            response. If the value is zero, the service will select a
            default size. A call might return fewer objects than
            requested. A non-empty ``next_page_token`` in the response
            indicates that more data is available.
        page_token (str):
            Optional. The value returned by the last
            ``ListQaQuestionsResponse``. This value indicates that this
            is a continuation of a prior ``ListQaQuestions`` call and
            that the system should return the next page of data.
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


class ListQaQuestionsResponse(proto.Message):
    r"""The response from a ListQaQuestions request.

    Attributes:
        qa_questions (MutableSequence[google.cloud.contact_center_insights_v1.types.QaQuestion]):
            The QaQuestions under the parent.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    qa_questions: MutableSequence[resources.QaQuestion] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.QaQuestion,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateQaQuestionRequest(proto.Message):
    r"""The request for updating a QaQuestion.

    Attributes:
        qa_question (google.cloud.contact_center_insights_v1.types.QaQuestion):
            Required. The QaQuestion to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to be updated. All possible
            fields can be updated by passing ``*``, or a subset of the
            following updateable fields can be provided:

            - ``abbreviation``
            - ``answer_choices``
            - ``answer_instructions``
            - ``order``
            - ``question_body``
            - ``tags``
    """

    qa_question: resources.QaQuestion = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.QaQuestion,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteQaQuestionRequest(proto.Message):
    r"""The request for deleting a QaQuestion.

    Attributes:
        name (str):
            Required. The name of the QaQuestion to
            delete.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateQaScorecardRequest(proto.Message):
    r"""The request for creating a QaScorecard.

    Attributes:
        parent (str):
            Required. The parent resource of the
            QaScorecard.
        qa_scorecard (google.cloud.contact_center_insights_v1.types.QaScorecard):
            Required. The QaScorecard to create.
        qa_scorecard_id (str):
            Optional. A unique ID for the new QaScorecard. This ID will
            become the final component of the QaScorecard's resource
            name. If no ID is specified, a server-generated ID will be
            used.

            This value should be 4-64 characters and must match the
            regular expression ``^[a-z0-9-]{4,64}$``. Valid characters
            are ``[a-z][0-9]-``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    qa_scorecard: resources.QaScorecard = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.QaScorecard,
    )
    qa_scorecard_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GetQaScorecardRequest(proto.Message):
    r"""The request for a QaScorecard. By default, returns the latest
    revision.

    Attributes:
        name (str):
            Required. The name of the QaScorecard to get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateQaScorecardRequest(proto.Message):
    r"""The request for updating a QaScorecard.

    Attributes:
        qa_scorecard (google.cloud.contact_center_insights_v1.types.QaScorecard):
            Required. The QaScorecard to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to be updated. All possible
            fields can be updated by passing ``*``, or a subset of the
            following updateable fields can be provided:

            - ``description``
            - ``display_name``
    """

    qa_scorecard: resources.QaScorecard = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.QaScorecard,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteQaScorecardRequest(proto.Message):
    r"""The request for deleting a QaScorecard.

    Attributes:
        name (str):
            Required. The name of the QaScorecard to
            delete.
        force (bool):
            Optional. If set to true, all of this
            QaScorecard's child resources will also be
            deleted. Otherwise, the request will only
            succeed if it has none.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class CreateQaScorecardRevisionRequest(proto.Message):
    r"""The request for creating a QaScorecardRevision.

    Attributes:
        parent (str):
            Required. The parent resource of the
            QaScorecardRevision.
        qa_scorecard_revision (google.cloud.contact_center_insights_v1.types.QaScorecardRevision):
            Required. The QaScorecardRevision to create.
        qa_scorecard_revision_id (str):
            Optional. A unique ID for the new QaScorecardRevision. This
            ID will become the final component of the
            QaScorecardRevision's resource name. If no ID is specified,
            a server-generated ID will be used.

            This value should be 4-64 characters and must match the
            regular expression ``^[a-z0-9-]{4,64}$``. Valid characters
            are ``[a-z][0-9]-``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    qa_scorecard_revision: resources.QaScorecardRevision = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.QaScorecardRevision,
    )
    qa_scorecard_revision_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GetQaScorecardRevisionRequest(proto.Message):
    r"""The request for a QaScorecardRevision.

    Attributes:
        name (str):
            Required. The name of the QaScorecardRevision
            to get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class TuneQaScorecardRevisionRequest(proto.Message):
    r"""Request for TuneQaScorecardRevision endpoint.

    Attributes:
        parent (str):
            Required. The parent resource for new fine
            tuning job instance.
        filter (str):
            Required. Filter for selecting the feedback
            labels that needs to be used for training.
            This filter can be used to limit the feedback
            labels used for tuning to a feedback labels
            created or updated for a specific time-window
            etc.
        validate_only (bool):
            Optional. Run in validate only mode, no fine
            tuning will actually run. Data quality
            validations like training data distributions
            will run. Even when set to false, the data
            quality validations will still run but once the
            validations complete we will proceed with the
            fine tune, if applicable.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class TuneQaScorecardRevisionResponse(proto.Message):
    r"""Response for TuneQaScorecardRevision endpoint."""


class TuneQaScorecardRevisionMetadata(proto.Message):
    r"""Metadata for TuneQaScorecardRevision endpoint.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation finished
            running.
        request (google.cloud.contact_center_insights_v1.types.TuneQaScorecardRevisionRequest):
            Output only. The original request.
        qa_question_dataset_validation_results (MutableSequence[google.cloud.contact_center_insights_v1.types.TuneQaScorecardRevisionMetadata.QaQuestionDatasetValidationResult]):
            Output only. The results of data validation
            per question in the request.
        qa_question_dataset_tuning_metrics (MutableSequence[google.cloud.contact_center_insights_v1.types.TuneQaScorecardRevisionMetadata.QaQuestionDatasetTuningMetrics]):
            Output only. The metrics for each QaQuestion
            in the TuneScorecardRevision request.
        tuning_completion_ratio (float):
            Output only. The percentage of the tuning job
            that has completed. Always between 0 and 1 where
            0 indicates the job has not started i.e. 0% and
            1 indicates the job has completed i.e. 100%.
    """

    class QaQuestionDatasetValidationResult(proto.Message):
        r"""Contains validation results for a question in the tuning
        request.

        Attributes:
            question (str):
                Output only. The resource path of the
                question whose dataset was evaluated for tuning.
            dataset_validation_warnings (MutableSequence[google.cloud.contact_center_insights_v1.types.DatasetValidationWarning]):
                A list of any applicable data validation
                warnings about the question's feedback labels.
            valid_feedback_labels_count (int):
                The number of valid feedback labels in the
                question's dataset.
        """

        question: str = proto.Field(
            proto.STRING,
            number=1,
        )
        dataset_validation_warnings: MutableSequence[
            resources.DatasetValidationWarning
        ] = proto.RepeatedField(
            proto.ENUM,
            number=2,
            enum=resources.DatasetValidationWarning,
        )
        valid_feedback_labels_count: int = proto.Field(
            proto.INT32,
            number=3,
        )

    class QaQuestionDatasetTuningMetrics(proto.Message):
        r"""Contains performance metrics for each QaQuestion in the
        TuneScorecardRevision request.

        Attributes:
            question (str):
                Output only. The resource path of the
                question whose dataset was evaluated for tuning.
            metrics (google.cloud.contact_center_insights_v1.types.TuneQaScorecardRevisionMetadata.QaQuestionDatasetTuningMetrics.Metrics):
                Output only. The metrics for the question's
                dataset.
        """

        class Metrics(proto.Message):
            r"""Performance metrics for the question's dataset calculated
            over the tuned model.

            Attributes:
                accuracy (float):
                    Accuracy of the question's dataset.
            """

            accuracy: float = proto.Field(
                proto.DOUBLE,
                number=1,
            )

        question: str = proto.Field(
            proto.STRING,
            number=1,
        )
        metrics: "TuneQaScorecardRevisionMetadata.QaQuestionDatasetTuningMetrics.Metrics" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="TuneQaScorecardRevisionMetadata.QaQuestionDatasetTuningMetrics.Metrics",
        )

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    request: "TuneQaScorecardRevisionRequest" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="TuneQaScorecardRevisionRequest",
    )
    qa_question_dataset_validation_results: MutableSequence[
        QaQuestionDatasetValidationResult
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=QaQuestionDatasetValidationResult,
    )
    qa_question_dataset_tuning_metrics: MutableSequence[
        QaQuestionDatasetTuningMetrics
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message=QaQuestionDatasetTuningMetrics,
    )
    tuning_completion_ratio: float = proto.Field(
        proto.DOUBLE,
        number=6,
    )


class DeployQaScorecardRevisionRequest(proto.Message):
    r"""The request to deploy a QaScorecardRevision

    Attributes:
        name (str):
            Required. The name of the QaScorecardRevision
            to deploy.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UndeployQaScorecardRevisionRequest(proto.Message):
    r"""The request to undeploy a QaScorecardRevision

    Attributes:
        name (str):
            Required. The name of the QaScorecardRevision
            to undeploy.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteQaScorecardRevisionRequest(proto.Message):
    r"""The request to delete a QaScorecardRevision.

    Attributes:
        name (str):
            Required. The name of the QaScorecardRevision
            to delete.
        force (bool):
            Optional. If set to true, all of this
            QaScorecardRevision's child resources will also
            be deleted. Otherwise, the request will only
            succeed if it has none.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class ListQaScorecardsRequest(proto.Message):
    r"""Request to list QaScorecards.

    Attributes:
        parent (str):
            Required. The parent resource of the
            scorecards.
        page_size (int):
            Optional. The maximum number of scorecards to return in the
            response. If the value is zero, the service will select a
            default size. A call might return fewer objects than
            requested. A non-empty ``next_page_token`` in the response
            indicates that more data is available.
        page_token (str):
            Optional. The value returned by the last
            ``ListQaScorecardsResponse``. This value indicates that this
            is a continuation of a prior ``ListQaScorecards`` call and
            that the system should return the next page of data.
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


class ListQaScorecardsResponse(proto.Message):
    r"""The response from a ListQaScorecards request.

    Attributes:
        qa_scorecards (MutableSequence[google.cloud.contact_center_insights_v1.types.QaScorecard]):
            The QaScorecards under the parent.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    qa_scorecards: MutableSequence[resources.QaScorecard] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.QaScorecard,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListQaScorecardRevisionsRequest(proto.Message):
    r"""Request to list QaScorecardRevisions

    Attributes:
        parent (str):
            Required. The parent resource of the
            scorecard revisions. To list all revisions of
            all scorecards, substitute the QaScorecard ID
            with a '-' character.
        page_size (int):
            Optional. The maximum number of scorecard revisions to
            return in the response. If the value is zero, the service
            will select a default size. A call might return fewer
            objects than requested. A non-empty ``next_page_token`` in
            the response indicates that more data is available.
        page_token (str):
            Optional. The value returned by the last
            ``ListQaScorecardRevisionsResponse``. This value indicates
            that this is a continuation of a prior
            ``ListQaScorecardRevisions`` call and that the system should
            return the next page of data.
        filter (str):
            Optional. A filter to reduce results to a
            specific subset. Useful for querying scorecard
            revisions with specific properties.
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


class ListQaScorecardRevisionsResponse(proto.Message):
    r"""The response from a ListQaScorecardRevisions request.

    Attributes:
        qa_scorecard_revisions (MutableSequence[google.cloud.contact_center_insights_v1.types.QaScorecardRevision]):
            The QaScorecards under the parent.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    qa_scorecard_revisions: MutableSequence[resources.QaScorecardRevision] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=resources.QaScorecardRevision,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateFeedbackLabelRequest(proto.Message):
    r"""The request for creating a feedback label.

    Attributes:
        parent (str):
            Required. The parent resource of the feedback
            label.
        feedback_label_id (str):
            Optional. The ID of the feedback label to
            create. If one is not specified it will be
            generated by the server.
        feedback_label (google.cloud.contact_center_insights_v1.types.FeedbackLabel):
            Required. The feedback label to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    feedback_label_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    feedback_label: resources.FeedbackLabel = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.FeedbackLabel,
    )


class ListFeedbackLabelsRequest(proto.Message):
    r"""The request for listing feedback labels.

    Attributes:
        parent (str):
            Required. The parent resource of the feedback
            labels.
        filter (str):
            Optional. A filter to reduce results to a specific subset.
            Supports disjunctions (OR) and conjunctions (AND).
            Automatically sorts by conversation ID. To sort by all
            feedback labels in a project see ListAllFeedbackLabels.

            Supported fields:

            - ``issue_model_id``
            - ``qa_question_id``
            - ``qa_scorecard_id``
            - ``min_create_time``
            - ``max_create_time``
            - ``min_update_time``
            - ``max_update_time``
            - ``feedback_label_type``: QUALITY_AI, TOPIC_MODELING
        page_size (int):
            Optional. The maximum number of feedback
            labels to return in the response. A valid page
            size ranges from 0 to 100,000 inclusive. If the
            page size is zero or unspecified, a default page
            size of 100 will be chosen. Note that a call
            might return fewer results than the requested
            page size.
        page_token (str):
            Optional. The value returned by the last
            ``ListFeedbackLabelsResponse``. This value indicates that
            this is a continuation of a prior ``ListFeedbackLabels``
            call and that the system should return the next page of
            data.
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


class ListFeedbackLabelsResponse(proto.Message):
    r"""The response for listing feedback labels.

    Attributes:
        feedback_labels (MutableSequence[google.cloud.contact_center_insights_v1.types.FeedbackLabel]):
            The feedback labels that match the request.
        next_page_token (str):
            The next page token.
    """

    @property
    def raw_page(self):
        return self

    feedback_labels: MutableSequence[resources.FeedbackLabel] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.FeedbackLabel,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetFeedbackLabelRequest(proto.Message):
    r"""The request for getting a feedback label.

    Attributes:
        name (str):
            Required. The name of the feedback label to
            get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateFeedbackLabelRequest(proto.Message):
    r"""The request for updating a feedback label.

    Attributes:
        feedback_label (google.cloud.contact_center_insights_v1.types.FeedbackLabel):
            Required. The feedback label to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to be updated.
    """

    feedback_label: resources.FeedbackLabel = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.FeedbackLabel,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteFeedbackLabelRequest(proto.Message):
    r"""The request for deleting a feedback label.

    Attributes:
        name (str):
            Required. The name of the feedback label to
            delete.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListAllFeedbackLabelsRequest(proto.Message):
    r"""The request for listing all feedback labels.

    Attributes:
        parent (str):
            Required. The parent resource of all feedback
            labels per project.
        page_size (int):
            Optional. The maximum number of feedback
            labels to return in the response. A valid page
            size ranges from 0 to 100,000 inclusive. If the
            page size is zero or unspecified, a default page
            size of 100 will be chosen. Note that a call
            might return fewer results than the requested
            page size.
        page_token (str):
            Optional. The value returned by the last
            ``ListAllFeedbackLabelsResponse``. This value indicates that
            this is a continuation of a prior ``ListAllFeedbackLabels``
            call and that the system should return the next page of
            data.
        filter (str):
            Optional. A filter to reduce results to a specific subset in
            the entire project. Supports disjunctions (OR) and
            conjunctions (AND).

            Supported fields:

            - ``issue_model_id``
            - ``qa_question_id``
            - ``min_create_time``
            - ``max_create_time``
            - ``min_update_time``
            - ``max_update_time``
            - ``feedback_label_type``: QUALITY_AI, TOPIC_MODELING
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


class ListAllFeedbackLabelsResponse(proto.Message):
    r"""The response for listing all feedback labels.

    Attributes:
        feedback_labels (MutableSequence[google.cloud.contact_center_insights_v1.types.FeedbackLabel]):
            The feedback labels that match the request.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    feedback_labels: MutableSequence[resources.FeedbackLabel] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.FeedbackLabel,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class BulkUploadFeedbackLabelsRequest(proto.Message):
    r"""The request for bulk uploading feedback labels.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_source (google.cloud.contact_center_insights_v1.types.BulkUploadFeedbackLabelsRequest.GcsSource):
            A cloud storage bucket source.

            This field is a member of `oneof`_ ``source``.
        parent (str):
            Required. The parent resource for new
            feedback labels.
        validate_only (bool):
            Optional. If set, upload will not happen and
            the labels will be validated. If not set, then
            default behavior will be to upload the labels
            after validation is complete.
    """

    class GcsSource(proto.Message):
        r"""Google Cloud Storage Object details to get the feedback label
        file from.

        Attributes:
            format_ (google.cloud.contact_center_insights_v1.types.BulkUploadFeedbackLabelsRequest.GcsSource.Format):
                Required. File format which will be ingested.
            object_uri (str):
                Required. The Google Cloud Storage URI of the file to
                import. Format: ``gs://bucket_name/object_name``
        """

        class Format(proto.Enum):
            r"""All permissible file formats.

            Values:
                FORMAT_UNSPECIFIED (0):
                    Unspecified format.
                CSV (1):
                    CSV format.
                JSON (2):
                    JSON format.
            """

            FORMAT_UNSPECIFIED = 0
            CSV = 1
            JSON = 2

        format_: "BulkUploadFeedbackLabelsRequest.GcsSource.Format" = proto.Field(
            proto.ENUM,
            number=1,
            enum="BulkUploadFeedbackLabelsRequest.GcsSource.Format",
        )
        object_uri: str = proto.Field(
            proto.STRING,
            number=2,
        )

    gcs_source: GcsSource = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="source",
        message=GcsSource,
    )
    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class BulkUploadFeedbackLabelsResponse(proto.Message):
    r"""Response for the Bulk Upload Feedback Labels API."""


class BulkUploadFeedbackLabelsMetadata(proto.Message):
    r"""Metadata for the Bulk Upload Feedback Labels API.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation finished
            running.
        request (google.cloud.contact_center_insights_v1.types.BulkUploadFeedbackLabelsRequest):
            Output only. The original request for ingest.
        partial_errors (MutableSequence[google.rpc.status_pb2.Status]):
            Partial errors during ingest operation that
            might cause the operation output to be
            incomplete.
        upload_stats (google.cloud.contact_center_insights_v1.types.BulkUploadFeedbackLabelsMetadata.UploadStats):
            Output only. Statistics for
            BulkUploadFeedbackLabels operation.
    """

    class UploadStats(proto.Message):
        r"""Statistics for BulkUploadFeedbackLabels operation.

        Attributes:
            processed_object_count (int):
                The number of objects processed during the
                upload operation.
            failed_validation_count (int):
                The number of objects skipped because of
                failed validation
            successful_upload_count (int):
                The number of new feedback labels added
                during this ingest operation.
        """

        processed_object_count: int = proto.Field(
            proto.INT32,
            number=1,
        )
        failed_validation_count: int = proto.Field(
            proto.INT32,
            number=2,
        )
        successful_upload_count: int = proto.Field(
            proto.INT32,
            number=3,
        )

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    request: "BulkUploadFeedbackLabelsRequest" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="BulkUploadFeedbackLabelsRequest",
    )
    partial_errors: MutableSequence[status_pb2.Status] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=status_pb2.Status,
    )
    upload_stats: UploadStats = proto.Field(
        proto.MESSAGE,
        number=5,
        message=UploadStats,
    )


class BulkDownloadFeedbackLabelsRequest(proto.Message):
    r"""Request for the BulkDownloadFeedbackLabel endpoint.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_destination (google.cloud.contact_center_insights_v1.types.BulkDownloadFeedbackLabelsRequest.GcsDestination):
            A cloud storage bucket destination.

            This field is a member of `oneof`_ ``destination``.
        parent (str):
            Required. The parent resource for new
            feedback labels.
        filter (str):
            Optional. A filter to reduce results to a specific subset.
            Supports disjunctions (OR) and conjunctions (AND).

            Supported fields:

            - ``issue_model_id``
            - ``qa_question_id``
            - ``qa_scorecard_id``
            - ``min_create_time``
            - ``max_create_time``
            - ``min_update_time``
            - ``max_update_time``
            - ``feedback_label_type``: QUALITY_AI, TOPIC_MODELING
        max_download_count (int):
            Optional. Limits the maximum number of feedback labels that
            will be downloaded. The first ``N`` feedback labels will be
            downloaded.
        feedback_label_type (google.cloud.contact_center_insights_v1.types.BulkDownloadFeedbackLabelsRequest.FeedbackLabelType):
            Optional. The type of feedback labels that
            will be downloaded.
        conversation_filter (str):
            Optional. Filter parent conversations to download feedback
            labels for. When specified, the feedback labels will be
            downloaded for the conversations that match the filter. If
            ``template_qa_scorecard_id`` is set, all the conversations
            that match the filter will be paired with the questions
            under the scorecard for labeling.
        template_qa_scorecard_id (MutableSequence[str]):
            Optional. If set, a template for labeling conversations and
            scorecard questions will be created from the
            conversation_filter and the questions under the
            scorecard(s). The feedback label ``filter`` will be ignored.
    """

    class FeedbackLabelType(proto.Enum):
        r"""Possible feedback label types that will be downloaded.

        Values:
            FEEDBACK_LABEL_TYPE_UNSPECIFIED (0):
                Unspecified format
            QUALITY_AI (1):
                Downloaded file will contain all Quality AI
                labels from the latest scorecard revision.
            TOPIC_MODELING (2):
                Downloaded file will contain only Topic
                Modeling labels.
        """

        FEEDBACK_LABEL_TYPE_UNSPECIFIED = 0
        QUALITY_AI = 1
        TOPIC_MODELING = 2

    class GcsDestination(proto.Message):
        r"""Google Cloud Storage Object details to write the feedback
        labels to.

        Attributes:
            format_ (google.cloud.contact_center_insights_v1.types.BulkDownloadFeedbackLabelsRequest.GcsDestination.Format):
                Required. File format in which the labels
                will be exported.
            object_uri (str):
                Required. The Google Cloud Storage URI to write the feedback
                labels to. The file name will be used as a prefix for the
                files written to the bucket if the output needs to be split
                across multiple files, otherwise it will be used as is. The
                file extension will be appended to the file name based on
                the format selected. E.g.
                ``gs://bucket_name/object_uri_prefix``
            add_whitespace (bool):
                Optional. Add whitespace to the JSON file.
                Makes easier to read, but increases file size.
                Only applicable for JSON format.
            always_print_empty_fields (bool):
                Optional. Always print fields with no
                presence. This is useful for printing fields
                that are not set, like implicit 0 value or empty
                lists/maps. Only applicable for JSON format.
            records_per_file_count (int):
                Optional. The number of records per file.
                Applicable for either format.
        """

        class Format(proto.Enum):
            r"""All permissible file formats. See ``records_per_file_count`` to
            override the default number of records per file.

            Values:
                FORMAT_UNSPECIFIED (0):
                    Unspecified format.
                CSV (1):
                    CSV format.
                    1,000 labels are stored per CSV file by default.
                JSON (2):
                    JSON format.
                    1 label stored per JSON file by default.
            """

            FORMAT_UNSPECIFIED = 0
            CSV = 1
            JSON = 2

        format_: "BulkDownloadFeedbackLabelsRequest.GcsDestination.Format" = (
            proto.Field(
                proto.ENUM,
                number=1,
                enum="BulkDownloadFeedbackLabelsRequest.GcsDestination.Format",
            )
        )
        object_uri: str = proto.Field(
            proto.STRING,
            number=2,
        )
        add_whitespace: bool = proto.Field(
            proto.BOOL,
            number=3,
        )
        always_print_empty_fields: bool = proto.Field(
            proto.BOOL,
            number=4,
        )
        records_per_file_count: int = proto.Field(
            proto.INT64,
            number=5,
        )

    gcs_destination: GcsDestination = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="destination",
        message=GcsDestination,
    )
    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    max_download_count: int = proto.Field(
        proto.INT32,
        number=4,
    )
    feedback_label_type: FeedbackLabelType = proto.Field(
        proto.ENUM,
        number=5,
        enum=FeedbackLabelType,
    )
    conversation_filter: str = proto.Field(
        proto.STRING,
        number=6,
    )
    template_qa_scorecard_id: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )


class BulkDownloadFeedbackLabelsResponse(proto.Message):
    r"""Response for the BulkDownloadFeedbackLabel endpoint."""


class BulkDownloadFeedbackLabelsMetadata(proto.Message):
    r"""Metadata for the BulkDownloadFeedbackLabel endpoint.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation finished
            running.
        request (google.cloud.contact_center_insights_v1.types.BulkDownloadFeedbackLabelsRequest):
            Output only. The original request for
            download.
        partial_errors (MutableSequence[google.rpc.status_pb2.Status]):
            Partial errors during ingest operation that
            might cause the operation output to be
            incomplete.
        download_stats (google.cloud.contact_center_insights_v1.types.BulkDownloadFeedbackLabelsMetadata.DownloadStats):
            Output only. Statistics for
            BulkDownloadFeedbackLabels operation.
    """

    class DownloadStats(proto.Message):
        r"""Statistics for BulkDownloadFeedbackLabels operation.

        Attributes:
            processed_object_count (int):
                The number of objects processed during the
                download operation.
            successful_download_count (int):
                The number of new feedback labels downloaded
                during this operation. Different from
                "processed" because some labels might not be
                downloaded because an error.
            total_files_written (int):
                Total number of files written to the provided
                Cloud Storage bucket.
            file_names (MutableSequence[str]):
                Output only. Full name of the files written
                to Cloud storage.
        """

        processed_object_count: int = proto.Field(
            proto.INT32,
            number=1,
        )
        successful_download_count: int = proto.Field(
            proto.INT32,
            number=2,
        )
        total_files_written: int = proto.Field(
            proto.INT32,
            number=3,
        )
        file_names: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=4,
        )

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    request: "BulkDownloadFeedbackLabelsRequest" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="BulkDownloadFeedbackLabelsRequest",
    )
    partial_errors: MutableSequence[status_pb2.Status] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=status_pb2.Status,
    )
    download_stats: DownloadStats = proto.Field(
        proto.MESSAGE,
        number=5,
        message=DownloadStats,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
