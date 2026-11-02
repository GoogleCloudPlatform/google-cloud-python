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

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.dialogflow_v2beta1.types import generator

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.v2beta1",
    manifest={
        "CreateGeneratorEvaluationRequest",
        "GetGeneratorEvaluationRequest",
        "ListGeneratorEvaluationsRequest",
        "ListGeneratorEvaluationsResponse",
        "DeleteGeneratorEvaluationRequest",
        "GeneratorEvaluation",
        "SummarizationEvaluationMetrics",
        "GeneratorEvaluationConfig",
        "EvaluationStatus",
    },
)


class CreateGeneratorEvaluationRequest(proto.Message):
    r"""Request of CreateGeneratorEvaluation.

    Attributes:
        parent (str):
            Required. The generator resource name. Format:
            ``projects/<Project ID>/locations/<Location ID>/generators/<Generator ID>``
        generator_evaluation (google.cloud.dialogflow_v2beta1.types.GeneratorEvaluation):
            Required. The generator evaluation to be
            created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    generator_evaluation: "GeneratorEvaluation" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="GeneratorEvaluation",
    )


class GetGeneratorEvaluationRequest(proto.Message):
    r"""Request of GetGeneratorEvaluation.

    Attributes:
        name (str):
            Required. The generator evaluation resource name. Format:
            ``projects/<Project ID>/locations/<Location ID>/generators/<Generator ID>/evaluations/<Evaluation ID>``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListGeneratorEvaluationsRequest(proto.Message):
    r"""Request of ListGeneratorEvaluations.

    Attributes:
        parent (str):
            Required. The generator resource name. Format:
            ``projects/<Project ID>/locations/<Location ID>/generators/<Generator ID>``
            Wildcard value ``-`` is supported on generator_id to list
            evaluations across all generators under same project.
        page_size (int):
            Optional. Maximum number of evaluations to
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


class ListGeneratorEvaluationsResponse(proto.Message):
    r"""Response of ListGeneratorEvaluations.

    Attributes:
        generator_evaluations (MutableSequence[google.cloud.dialogflow_v2beta1.types.GeneratorEvaluation]):
            The list of evaluations to return.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    generator_evaluations: MutableSequence["GeneratorEvaluation"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="GeneratorEvaluation",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteGeneratorEvaluationRequest(proto.Message):
    r"""Request of DeleteGeneratorEvaluation.

    Attributes:
        name (str):
            Required. The generator evaluation resource name. Format:
            ``projects/<Project ID>/locations/<Location ID>/generators/<Generator ID>/ evaluations/<Evaluation ID>``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GeneratorEvaluation(proto.Message):
    r"""Represents evaluation result of a generator.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. Identifier. The resource name of the
            evaluation. Format:
            ``projects/<Project ID>/locations/<Location ID>/generators/<Generator ID>/ evaluations/<Evaluation ID>``
        display_name (str):
            Optional. The display name of the generator
            evaluation. At most 64 bytes long.
        generator_evaluation_config (google.cloud.dialogflow_v2beta1.types.GeneratorEvaluationConfig):
            Required. The configuration of the evaluation
            task.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Creation time of this generator
            evaluation.
        complete_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Completion time of this
            generator evaluation.
        initial_generator (google.cloud.dialogflow_v2beta1.types.Generator):
            Required. The initial generator that was used
            when creating this evaluation. This is a copy of
            the generator read from storage when creating
            the evaluation.
        summarization_metrics (google.cloud.dialogflow_v2beta1.types.SummarizationEvaluationMetrics):
            Output only. Only available when the
            summarization generator is provided.

            This field is a member of `oneof`_ ``metrics``.
        evaluation_status (google.cloud.dialogflow_v2beta1.types.EvaluationStatus):
            Output only. The result status of the
            evaluation pipeline. Provides the status
            information including if the evaluation is still
            in progress, completed or failed with certain
            error and user actionable message.
        satisfies_pzs (bool):
            Output only. A read only boolean field
            reflecting Zone Separation status of the model.
            The field is an aggregated value of ZS status of
            its underlying dependencies. See more details in
            go/zicy-resource-placement#resource-status

            This field is a member of `oneof`_ ``_satisfies_pzs``.
        satisfies_pzi (bool):
            Output only. A read only boolean field
            reflecting Zone Isolation status of the model.
            The field is an aggregated value of ZI status of
            its underlying dependencies. See more details in
            go/zicy-resource-placement#resource-status

            This field is a member of `oneof`_ ``_satisfies_pzi``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    generator_evaluation_config: "GeneratorEvaluationConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="GeneratorEvaluationConfig",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    complete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    initial_generator: generator.Generator = proto.Field(
        proto.MESSAGE,
        number=5,
        message=generator.Generator,
    )
    summarization_metrics: "SummarizationEvaluationMetrics" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="metrics",
        message="SummarizationEvaluationMetrics",
    )
    evaluation_status: "EvaluationStatus" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="EvaluationStatus",
    )
    satisfies_pzs: bool = proto.Field(
        proto.BOOL,
        number=11,
        optional=True,
    )
    satisfies_pzi: bool = proto.Field(
        proto.BOOL,
        number=12,
        optional=True,
    )


class SummarizationEvaluationMetrics(proto.Message):
    r"""Evaluation metrics for summarization generator.

    Attributes:
        summarization_evaluation_results (MutableSequence[google.cloud.dialogflow_v2beta1.types.SummarizationEvaluationMetrics.SummarizationEvaluationResult]):
            Output only. A list of evaluation results per
            conversation(&summary), metric and section.
        summarization_evaluation_merged_results_uri (str):
            Output only. User bucket uri for merged
            evaluation score and aggregation score csv.
        overall_metrics (MutableSequence[google.cloud.dialogflow_v2beta1.types.SummarizationEvaluationMetrics.OverallScoresByMetric]):
            Output only. A list of aggregated(average)
            scores per metric section.
        overall_section_tokens (MutableSequence[google.cloud.dialogflow_v2beta1.types.SummarizationEvaluationMetrics.SectionToken]):
            Output only. Overall token per section. This
            is an aggregated(sum) result of input token of
            summary acorss all conversations that are
            selected for summarization evaluation.
        conversation_details (MutableSequence[google.cloud.dialogflow_v2beta1.types.SummarizationEvaluationMetrics.ConversationDetail]):
            Output only. List of conversation details.
    """

    class AccuracyDecomposition(proto.Message):
        r"""Decomposition details for accuracy.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            point (str):
                Output only. The breakdown point of the
                summary.
            accuracy_reasoning (str):
                Output only. The accuracy reasoning of the
                breakdown point.
            is_accurate (bool):
                Output only. Whether the breakdown point is
                accurate or not.

                This field is a member of `oneof`_ ``_is_accurate``.
        """

        point: str = proto.Field(
            proto.STRING,
            number=1,
        )
        accuracy_reasoning: str = proto.Field(
            proto.STRING,
            number=2,
        )
        is_accurate: bool = proto.Field(
            proto.BOOL,
            number=3,
            optional=True,
        )

    class AdherenceDecomposition(proto.Message):
        r"""Decomposition details for adherence.

        Attributes:
            point (str):
                Output only. The breakdown point of the given
                instructions.
            adherence_reasoning (str):
                Output only. The adherence reasoning of the
                breakdown point.
            is_adherent (bool):
                Output only. Whether the breakdown point is
                adherent or not.
        """

        point: str = proto.Field(
            proto.STRING,
            number=1,
        )
        adherence_reasoning: str = proto.Field(
            proto.STRING,
            number=2,
        )
        is_adherent: bool = proto.Field(
            proto.BOOL,
            number=3,
        )

    class AdherenceRubric(proto.Message):
        r"""Rubric result of the adherence evaluation. A rubric is ued to
        determine if the summary adheres to all aspects of the given
        instructions.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            question (str):
                Output only. The question generated from
                instruction that used to evaluate summary.
            reasoning (str):
                Output only. The reasoning of the rubric
                question is addressed or not.
            is_addressed (bool):
                Output only. A boolean that indicates whether
                the rubric question is addressed or not.

                This field is a member of `oneof`_ ``_is_addressed``.
        """

        question: str = proto.Field(
            proto.STRING,
            number=1,
        )
        reasoning: str = proto.Field(
            proto.STRING,
            number=2,
        )
        is_addressed: bool = proto.Field(
            proto.BOOL,
            number=3,
            optional=True,
        )

    class CompletenessRubric(proto.Message):
        r"""Rubric details of the completeness evaluation result.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            question (str):
                Output only. The question generated from
                instruction that used to evaluate summary.
            is_addressed (bool):
                Output only. A boolean that indicates whether
                the rubric question is addressed or not.

                This field is a member of `oneof`_ ``_is_addressed``.
        """

        question: str = proto.Field(
            proto.STRING,
            number=1,
        )
        is_addressed: bool = proto.Field(
            proto.BOOL,
            number=2,
            optional=True,
        )

    class Decomposition(proto.Message):
        r"""Decomposition details

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            accuracy_decomposition (google.cloud.dialogflow_v2beta1.types.SummarizationEvaluationMetrics.AccuracyDecomposition):
                only available for accuracy metric.

                This field is a member of `oneof`_ ``decomposition``.
            adherence_decomposition (google.cloud.dialogflow_v2beta1.types.SummarizationEvaluationMetrics.AdherenceDecomposition):
                only available for adherence metric.

                This field is a member of `oneof`_ ``decomposition``.
        """

        accuracy_decomposition: "SummarizationEvaluationMetrics.AccuracyDecomposition" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="decomposition",
            message="SummarizationEvaluationMetrics.AccuracyDecomposition",
        )
        adherence_decomposition: "SummarizationEvaluationMetrics.AdherenceDecomposition" = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="decomposition",
            message="SummarizationEvaluationMetrics.AdherenceDecomposition",
        )

    class EvaluationResult(proto.Message):
        r"""Evaluation result that contains one of accuracy, adherence or
        completeness evaluation result.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            accuracy_decomposition (google.cloud.dialogflow_v2beta1.types.SummarizationEvaluationMetrics.AccuracyDecomposition):
                Only available for accuracy metric.

                This field is a member of `oneof`_ ``result``.
            adherence_rubric (google.cloud.dialogflow_v2beta1.types.SummarizationEvaluationMetrics.AdherenceRubric):
                Only available for adherence metric.

                This field is a member of `oneof`_ ``result``.
            completeness_rubric (google.cloud.dialogflow_v2beta1.types.SummarizationEvaluationMetrics.CompletenessRubric):
                Only available for completeness metric.

                This field is a member of `oneof`_ ``result``.
        """

        accuracy_decomposition: "SummarizationEvaluationMetrics.AccuracyDecomposition" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="result",
            message="SummarizationEvaluationMetrics.AccuracyDecomposition",
        )
        adherence_rubric: "SummarizationEvaluationMetrics.AdherenceRubric" = (
            proto.Field(
                proto.MESSAGE,
                number=2,
                oneof="result",
                message="SummarizationEvaluationMetrics.AdherenceRubric",
            )
        )
        completeness_rubric: "SummarizationEvaluationMetrics.CompletenessRubric" = (
            proto.Field(
                proto.MESSAGE,
                number=3,
                oneof="result",
                message="SummarizationEvaluationMetrics.CompletenessRubric",
            )
        )

    class SummarizationEvaluationResult(proto.Message):
        r"""Evaluation result per conversation(&summary), metric and
        section.

        Attributes:
            session_id (str):
                Output only. conversation session id
            metric (str):
                Output only. metric name, e.g. accuracy,
                completeness, adherence, etc.
            section (str):
                Output only. section/task name, e.g. action,
                situation, etc
            score (float):
                Output only. score calculated from
                decompositions
            section_summary (str):
                Output only. Summary of this section
            decompositions (MutableSequence[google.cloud.dialogflow_v2beta1.types.SummarizationEvaluationMetrics.Decomposition]):
                Output only. List of decompostion details
            evaluation_results (MutableSequence[google.cloud.dialogflow_v2beta1.types.SummarizationEvaluationMetrics.EvaluationResult]):
                Output only. List of evaluation results.
        """

        session_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        metric: str = proto.Field(
            proto.STRING,
            number=2,
        )
        section: str = proto.Field(
            proto.STRING,
            number=3,
        )
        score: float = proto.Field(
            proto.FLOAT,
            number=4,
        )
        section_summary: str = proto.Field(
            proto.STRING,
            number=6,
        )
        decompositions: MutableSequence[
            "SummarizationEvaluationMetrics.Decomposition"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=7,
            message="SummarizationEvaluationMetrics.Decomposition",
        )
        evaluation_results: MutableSequence[
            "SummarizationEvaluationMetrics.EvaluationResult"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=8,
            message="SummarizationEvaluationMetrics.EvaluationResult",
        )

    class OverallScoresByMetric(proto.Message):
        r"""Overall performance per metric. This is the aggregated score
        for each metric across all conversations that are selected for
        summarization evaluation.

        Attributes:
            metric (str):
                Output only. Metric name. e.g. accuracy,
                adherence, completeness.
        """

        metric: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class SectionToken(proto.Message):
        r"""A pair of section name and input token count of the input
        summary section.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            section (str):
                Output only. The name of the summary
                instruction.
            token_count (int):
                Output only. Token count.

                This field is a member of `oneof`_ ``_token_count``.
        """

        section: str = proto.Field(
            proto.STRING,
            number=1,
        )
        token_count: int = proto.Field(
            proto.INT64,
            number=2,
            optional=True,
        )

    class ConversationDetail(proto.Message):
        r"""Aggregated evaluation result on conversation level. This
        contains evaluation results of all the metrics and sections.

        Attributes:
            message_entries (MutableSequence[google.cloud.dialogflow_v2beta1.types.MessageEntry]):
                Output only. Conversation transcript that
                used for summarization evaluation as a
                reference.
            summary_sections (MutableSequence[google.cloud.dialogflow_v2beta1.types.SummarySuggestion.SummarySection]):
                Output only. Summary sections that used for
                summarization evaluation as a reference.
            metric_details (MutableSequence[google.cloud.dialogflow_v2beta1.types.SummarizationEvaluationMetrics.ConversationDetail.MetricDetail]):
                Output only. List of metric details.
            section_tokens (MutableSequence[google.cloud.dialogflow_v2beta1.types.SummarizationEvaluationMetrics.SectionToken]):
                Output only. Conversation level token count
                per section. This is an aggregated(sum) result
                of input token of summary acorss all metrics for
                a single conversation.
        """

        class MetricDetail(proto.Message):
            r"""Aggregated result on metric level. This contains the
            evaluation results of all the sections.


            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                metric (str):
                    Output only. Metrics name. e.g. accuracy,
                    adherence, completeness.
                score (float):
                    Output only. Aggregated(average) score on
                    this metric across all sections.

                    This field is a member of `oneof`_ ``_score``.
                section_details (MutableSequence[google.cloud.dialogflow_v2beta1.types.SummarizationEvaluationMetrics.ConversationDetail.MetricDetail.SectionDetail]):
                    Output only. List of section details.
            """

            class SectionDetail(proto.Message):
                r"""Section level result.

                .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

                Attributes:
                    section (str):
                        Output only. The name of the summary
                        instruction.
                    score (float):
                        Output only. Aggregated(average) score on
                        this section across all evaluation results.
                        Either decompositions or rubrics.

                        This field is a member of `oneof`_ ``_score``.
                    section_summary (str):
                        Output only. Summary for this section
                    evaluation_results (MutableSequence[google.cloud.dialogflow_v2beta1.types.SummarizationEvaluationMetrics.EvaluationResult]):
                        Output only. List of evaluation result. The
                        list only contains one kind of the evaluation
                        result.
                """

                section: str = proto.Field(
                    proto.STRING,
                    number=1,
                )
                score: float = proto.Field(
                    proto.FLOAT,
                    number=2,
                    optional=True,
                )
                section_summary: str = proto.Field(
                    proto.STRING,
                    number=4,
                )
                evaluation_results: MutableSequence[
                    "SummarizationEvaluationMetrics.EvaluationResult"
                ] = proto.RepeatedField(
                    proto.MESSAGE,
                    number=5,
                    message="SummarizationEvaluationMetrics.EvaluationResult",
                )

            metric: str = proto.Field(
                proto.STRING,
                number=1,
            )
            score: float = proto.Field(
                proto.FLOAT,
                number=2,
                optional=True,
            )
            section_details: MutableSequence[
                "SummarizationEvaluationMetrics.ConversationDetail.MetricDetail.SectionDetail"
            ] = proto.RepeatedField(
                proto.MESSAGE,
                number=4,
                message="SummarizationEvaluationMetrics.ConversationDetail.MetricDetail.SectionDetail",
            )

        message_entries: MutableSequence[generator.MessageEntry] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=generator.MessageEntry,
        )
        summary_sections: MutableSequence[
            generator.SummarySuggestion.SummarySection
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message=generator.SummarySuggestion.SummarySection,
        )
        metric_details: MutableSequence[
            "SummarizationEvaluationMetrics.ConversationDetail.MetricDetail"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="SummarizationEvaluationMetrics.ConversationDetail.MetricDetail",
        )
        section_tokens: MutableSequence[
            "SummarizationEvaluationMetrics.SectionToken"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message="SummarizationEvaluationMetrics.SectionToken",
        )

    summarization_evaluation_results: MutableSequence[SummarizationEvaluationResult] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message=SummarizationEvaluationResult,
        )
    )
    summarization_evaluation_merged_results_uri: str = proto.Field(
        proto.STRING,
        number=5,
    )
    overall_metrics: MutableSequence[OverallScoresByMetric] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message=OverallScoresByMetric,
    )
    overall_section_tokens: MutableSequence[SectionToken] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message=SectionToken,
    )
    conversation_details: MutableSequence[ConversationDetail] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message=ConversationDetail,
    )


class GeneratorEvaluationConfig(proto.Message):
    r"""Generator evaluation input config.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        input_data_config (google.cloud.dialogflow_v2beta1.types.GeneratorEvaluationConfig.InputDataConfig):
            Required. The config/source of input data.
        output_gcs_bucket_path (str):
            Required. The output Cloud Storage bucket path to store eval
            files, e.g. per_summary_accuracy_score report. This path is
            provided by customer and files stored in it are visible to
            customer, no internal data should be stored in this path.
        summarization_config (google.cloud.dialogflow_v2beta1.types.GeneratorEvaluationConfig.SummarizationConfig):
            Evaluation configs for summarization
            generator.

            This field is a member of `oneof`_ ``evaluation_feature_config``.
    """

    class InputDataSourceType(proto.Enum):
        r"""Enumeration of input data source type.

        Values:
            INPUT_DATA_SOURCE_TYPE_UNSPECIFIED (0):
                Unspecified InputDataSourceType. Should not
                be used.
            AGENT_ASSIST_CONVERSATIONS (1):
                Fetch data from Agent Assist storage. If this source type is
                chosen, input_data_config.start_time and
                input_data_config.end_timestamp must be provided.
            INSIGHTS_CONVERSATIONS (2):
                Fetch data from Insights storage. If this source type is
                chosen, input_data_config.start_time and
                input_data_config.end_timestamp must be provided.
        """

        INPUT_DATA_SOURCE_TYPE_UNSPECIFIED = 0
        AGENT_ASSIST_CONVERSATIONS = 1
        INSIGHTS_CONVERSATIONS = 2

    class AgentAssistInputDataConfig(proto.Message):
        r"""The distinctive configs for Agent Assist conversations as the
        conversation source.

        Attributes:
            start_time (google.protobuf.timestamp_pb2.Timestamp):
                Required. The start of the time range for
                conversations to be evaluated. Only
                conversations created at or after this timestamp
                will be sampled.
            end_time (google.protobuf.timestamp_pb2.Timestamp):
                Required. The end of the time range for
                conversations to be evaluated. Only
                conversations ended at or before this timestamp
                will be sampled.
        """

        start_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=1,
            message=timestamp_pb2.Timestamp,
        )
        end_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=2,
            message=timestamp_pb2.Timestamp,
        )

    class DatasetInputDataConfig(proto.Message):
        r"""The distinctive configs for dataset as the conversation
        source.

        Attributes:
            dataset (str):
                Required. The identifier of the dataset to be evaluated.
                Format:
                ``projects/<ProjectId>/locations/<LocationID>/datasets/<DatasetID>``.
        """

        dataset: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class InputDataConfig(proto.Message):
        r"""Input data config details

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            input_data_source_type (google.cloud.dialogflow_v2beta1.types.GeneratorEvaluationConfig.InputDataSourceType):
                Required. The source type of input data.
            start_time (google.protobuf.timestamp_pb2.Timestamp):
                Optional. The start timestamp to fetch
                conversation data.
            end_time (google.protobuf.timestamp_pb2.Timestamp):
                Optional. The end timestamp to fetch
                conversation data.
            sample_size (int):
                Optional. Desired number of
                conversation-summary pairs to be evaluated.
            is_summary_generation_allowed (bool):
                Optional. Whether the summary generation is
                allowed when the pre-existing qualified
                summaries are insufficient to cover the sample
                size.
            summary_generation_option (google.cloud.dialogflow_v2beta1.types.GeneratorEvaluationConfig.InputDataConfig.SummaryGenerationOption):
                Optional. Option to control whether summaries
                are generated during evaluation.
            agent_assist_input_data_config (google.cloud.dialogflow_v2beta1.types.GeneratorEvaluationConfig.AgentAssistInputDataConfig):
                The distinctive configs for Agent Assist
                conversations as the conversation source.

                This field is a member of `oneof`_ ``source_specific_config``.
            dataset_input_data_config (google.cloud.dialogflow_v2beta1.types.GeneratorEvaluationConfig.DatasetInputDataConfig):
                The distinctive configs for dataset as the
                conversation source.

                This field is a member of `oneof`_ ``source_specific_config``.
        """

        class SummaryGenerationOption(proto.Enum):
            r"""Summary generation options.

            Values:
                SUMMARY_GENERATION_OPTION_UNSPECIFIED (0):
                    Default option will not be used
                ALWAYS_GENERATE (1):
                    Always Generate summary for all
                    conversations.
                GENERATE_IF_MISSING (2):
                    Gnerate only missing summaries.
                DO_NOT_GENERATE (3):
                    Do not generate new summaries. Only use
                    existing summaries found.
            """

            SUMMARY_GENERATION_OPTION_UNSPECIFIED = 0
            ALWAYS_GENERATE = 1
            GENERATE_IF_MISSING = 2
            DO_NOT_GENERATE = 3

        input_data_source_type: "GeneratorEvaluationConfig.InputDataSourceType" = (
            proto.Field(
                proto.ENUM,
                number=1,
                enum="GeneratorEvaluationConfig.InputDataSourceType",
            )
        )
        start_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=2,
            message=timestamp_pb2.Timestamp,
        )
        end_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=3,
            message=timestamp_pb2.Timestamp,
        )
        sample_size: int = proto.Field(
            proto.INT32,
            number=4,
        )
        is_summary_generation_allowed: bool = proto.Field(
            proto.BOOL,
            number=5,
        )
        summary_generation_option: "GeneratorEvaluationConfig.InputDataConfig.SummaryGenerationOption" = proto.Field(
            proto.ENUM,
            number=8,
            enum="GeneratorEvaluationConfig.InputDataConfig.SummaryGenerationOption",
        )
        agent_assist_input_data_config: "GeneratorEvaluationConfig.AgentAssistInputDataConfig" = proto.Field(
            proto.MESSAGE,
            number=6,
            oneof="source_specific_config",
            message="GeneratorEvaluationConfig.AgentAssistInputDataConfig",
        )
        dataset_input_data_config: "GeneratorEvaluationConfig.DatasetInputDataConfig" = proto.Field(
            proto.MESSAGE,
            number=7,
            oneof="source_specific_config",
            message="GeneratorEvaluationConfig.DatasetInputDataConfig",
        )

    class SummarizationConfig(proto.Message):
        r"""Evaluation configs for summarization generator.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            enable_accuracy_evaluation (bool):
                Optional. Enable accuracy evaluation.
            accuracy_evaluation_version (str):
                Optional. Version for summarization accuracy.
                This will determine the prompt and model used at
                backend.
            enable_completeness_evaluation (bool):
                Optional. Enable completeness evaluation.
            completeness_evaluation_version (str):
                Optional. Version for summarization
                completeness. This will determine the prompt and
                model used at backend.
            evaluator_version (str):
                Optional. Version for summarization
                evaluation.

                This field is a member of `oneof`_ ``_evaluator_version``.
        """

        enable_accuracy_evaluation: bool = proto.Field(
            proto.BOOL,
            number=1,
        )
        accuracy_evaluation_version: str = proto.Field(
            proto.STRING,
            number=2,
        )
        enable_completeness_evaluation: bool = proto.Field(
            proto.BOOL,
            number=3,
        )
        completeness_evaluation_version: str = proto.Field(
            proto.STRING,
            number=4,
        )
        evaluator_version: str = proto.Field(
            proto.STRING,
            number=5,
            optional=True,
        )

    input_data_config: InputDataConfig = proto.Field(
        proto.MESSAGE,
        number=1,
        message=InputDataConfig,
    )
    output_gcs_bucket_path: str = proto.Field(
        proto.STRING,
        number=2,
    )
    summarization_config: SummarizationConfig = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="evaluation_feature_config",
        message=SummarizationConfig,
    )


class EvaluationStatus(proto.Message):
    r"""A common evalaution pipeline status.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        done (bool):
            Output only. If the value is ``false``, it means the
            evaluation is still in progress. If ``true``, the operation
            is completed, and either ``error`` or ``response`` is
            available.

            This field is a member of `oneof`_ ``_done``.
        pipeline_status (google.rpc.status_pb2.Status):
            Output only. The error result of the
            evaluation in case of failure in evaluation
            pipeline.
    """

    done: bool = proto.Field(
        proto.BOOL,
        number=1,
        optional=True,
    )
    pipeline_status: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=2,
        message=status_pb2.Status,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
