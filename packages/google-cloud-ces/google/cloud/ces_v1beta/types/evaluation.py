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
import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.ces_v1beta.types import app as gcc_app
from google.cloud.ces_v1beta.types import (
    common,
    evaluation_metrics_config,
    example,
    fakes,
    golden_run,
    session_service,
)
from google.cloud.ces_v1beta.types import toolset_tool as gcc_toolset_tool

__protobuf__ = proto.module(
    package="google.cloud.ces.v1beta",
    manifest={
        "AggregatedMetrics",
        "Evaluation",
        "EvaluationDataset",
        "EvaluationResult",
        "EvaluationRun",
        "LatencyReport",
        "EvaluationExpectation",
        "EvaluationConfig",
        "EvaluationErrorInfo",
        "RunEvaluationRequest",
        "ScheduledEvaluationRun",
        "PersonaRunConfig",
        "OptimizationConfig",
    },
)


class AggregatedMetrics(proto.Message):
    r"""Aggregated metrics for an evaluation or evaluation dataset.

    Attributes:
        metrics_by_app_version (MutableSequence[google.cloud.ces_v1beta.types.AggregatedMetrics.MetricsByAppVersion]):
            Output only. Aggregated metrics, grouped by
            app version ID.
    """

    class ToolMetrics(proto.Message):
        r"""Metrics for a single tool.

        Attributes:
            tool (str):
                Output only. The name of the tool.
            pass_count (int):
                Output only. The number of times the tool
                passed.
            fail_count (int):
                Output only. The number of times the tool
                failed.
        """

        tool: str = proto.Field(
            proto.STRING,
            number=1,
        )
        pass_count: int = proto.Field(
            proto.INT32,
            number=2,
        )
        fail_count: int = proto.Field(
            proto.INT32,
            number=3,
        )

    class TurnLatencyMetrics(proto.Message):
        r"""Metrics for turn latency.

        Attributes:
            average_latency (google.protobuf.duration_pb2.Duration):
                Output only. The average latency of the
                turns.
        """

        average_latency: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=1,
            message=duration_pb2.Duration,
        )

    class ToolCallLatencyMetrics(proto.Message):
        r"""Metrics for tool call latency.

        Attributes:
            tool (str):
                Output only. The name of the tool.
            average_latency (google.protobuf.duration_pb2.Duration):
                Output only. The average latency of the tool
                calls.
        """

        tool: str = proto.Field(
            proto.STRING,
            number=1,
        )
        average_latency: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=2,
            message=duration_pb2.Duration,
        )

    class SemanticSimilarityMetrics(proto.Message):
        r"""Metrics for semantic similarity results.

        Attributes:
            score (float):
                Output only. The average semantic similarity
                score (0-4).
        """

        score: float = proto.Field(
            proto.FLOAT,
            number=1,
        )

    class HallucinationMetrics(proto.Message):
        r"""Metrics for hallucination results.

        Attributes:
            score (float):
                Output only. The average hallucination score
                (0 to 1).
        """

        score: float = proto.Field(
            proto.FLOAT,
            number=1,
        )

    class MetricsByAppVersion(proto.Message):
        r"""Metrics aggregated per app version.

        Attributes:
            app_version_id (str):
                Output only. The app version ID.
            tool_metrics (MutableSequence[google.cloud.ces_v1beta.types.AggregatedMetrics.ToolMetrics]):
                Output only. Metrics for each tool within
                this app version.
            semantic_similarity_metrics (MutableSequence[google.cloud.ces_v1beta.types.AggregatedMetrics.SemanticSimilarityMetrics]):
                Output only. Metrics for semantic similarity
                within this app version.
            hallucination_metrics (MutableSequence[google.cloud.ces_v1beta.types.AggregatedMetrics.HallucinationMetrics]):
                Output only. Metrics for hallucination within
                this app version.
            tool_call_latency_metrics (MutableSequence[google.cloud.ces_v1beta.types.AggregatedMetrics.ToolCallLatencyMetrics]):
                Output only. Metrics for tool call latency
                within this app version.
            turn_latency_metrics (MutableSequence[google.cloud.ces_v1beta.types.AggregatedMetrics.TurnLatencyMetrics]):
                Output only. Metrics for turn latency within
                this app version.
            pass_count (int):
                Output only. The number of times the
                evaluation passed.
            fail_count (int):
                Output only. The number of times the
                evaluation failed.
            metrics_by_turn (MutableSequence[google.cloud.ces_v1beta.types.AggregatedMetrics.MetricsByTurn]):
                Output only. Metrics aggregated per turn
                within this app version.
        """

        app_version_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        tool_metrics: MutableSequence["AggregatedMetrics.ToolMetrics"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message="AggregatedMetrics.ToolMetrics",
            )
        )
        semantic_similarity_metrics: MutableSequence[
            "AggregatedMetrics.SemanticSimilarityMetrics"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message="AggregatedMetrics.SemanticSimilarityMetrics",
        )
        hallucination_metrics: MutableSequence[
            "AggregatedMetrics.HallucinationMetrics"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=5,
            message="AggregatedMetrics.HallucinationMetrics",
        )
        tool_call_latency_metrics: MutableSequence[
            "AggregatedMetrics.ToolCallLatencyMetrics"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=6,
            message="AggregatedMetrics.ToolCallLatencyMetrics",
        )
        turn_latency_metrics: MutableSequence[
            "AggregatedMetrics.TurnLatencyMetrics"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=7,
            message="AggregatedMetrics.TurnLatencyMetrics",
        )
        pass_count: int = proto.Field(
            proto.INT32,
            number=8,
        )
        fail_count: int = proto.Field(
            proto.INT32,
            number=9,
        )
        metrics_by_turn: MutableSequence["AggregatedMetrics.MetricsByTurn"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=4,
                message="AggregatedMetrics.MetricsByTurn",
            )
        )

    class MetricsByTurn(proto.Message):
        r"""Metrics aggregated per turn.

        Attributes:
            turn_index (int):
                Output only. The turn index (0-based).
            tool_metrics (MutableSequence[google.cloud.ces_v1beta.types.AggregatedMetrics.ToolMetrics]):
                Output only. Metrics for each tool within
                this turn.
            semantic_similarity_metrics (MutableSequence[google.cloud.ces_v1beta.types.AggregatedMetrics.SemanticSimilarityMetrics]):
                Output only. Metrics for semantic similarity
                within this turn.
            hallucination_metrics (MutableSequence[google.cloud.ces_v1beta.types.AggregatedMetrics.HallucinationMetrics]):
                Output only. Metrics for hallucination within
                this turn.
            tool_call_latency_metrics (MutableSequence[google.cloud.ces_v1beta.types.AggregatedMetrics.ToolCallLatencyMetrics]):
                Output only. Metrics for tool call latency
                within this turn.
            turn_latency_metrics (MutableSequence[google.cloud.ces_v1beta.types.AggregatedMetrics.TurnLatencyMetrics]):
                Output only. Metrics for turn latency within
                this turn.
        """

        turn_index: int = proto.Field(
            proto.INT32,
            number=1,
        )
        tool_metrics: MutableSequence["AggregatedMetrics.ToolMetrics"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message="AggregatedMetrics.ToolMetrics",
            )
        )
        semantic_similarity_metrics: MutableSequence[
            "AggregatedMetrics.SemanticSimilarityMetrics"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message="AggregatedMetrics.SemanticSimilarityMetrics",
        )
        hallucination_metrics: MutableSequence[
            "AggregatedMetrics.HallucinationMetrics"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message="AggregatedMetrics.HallucinationMetrics",
        )
        tool_call_latency_metrics: MutableSequence[
            "AggregatedMetrics.ToolCallLatencyMetrics"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=5,
            message="AggregatedMetrics.ToolCallLatencyMetrics",
        )
        turn_latency_metrics: MutableSequence[
            "AggregatedMetrics.TurnLatencyMetrics"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=6,
            message="AggregatedMetrics.TurnLatencyMetrics",
        )

    metrics_by_app_version: MutableSequence[MetricsByAppVersion] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=MetricsByAppVersion,
    )


class Evaluation(proto.Message):
    r"""An evaluation represents all of the information needed to
    simulate and evaluate an agent.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        golden (google.cloud.ces_v1beta.types.Evaluation.Golden):
            Optional. The golden steps to be evaluated.

            This field is a member of `oneof`_ ``inputs``.
        scenario (google.cloud.ces_v1beta.types.Evaluation.Scenario):
            Optional. The config for a scenario.

            This field is a member of `oneof`_ ``inputs``.
        name (str):
            Identifier. The unique identifier of this evaluation.
            Format:
            ``projects/{project}/locations/{location}/apps/{app}/evaluations/{evaluation}``
        display_name (str):
            Required. User-defined display name of the
            evaluation. Unique within an App.
        description (str):
            Optional. User-defined description of the
            evaluation.
        tags (MutableSequence[str]):
            Optional. User defined tags to categorize the
            evaluation.
        evaluation_datasets (MutableSequence[str]):
            Output only. List of evaluation datasets the evaluation
            belongs to. Format:
            ``projects/{project}/locations/{location}/apps/{app}/evaluationDatasets/{evaluationDataset}``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the evaluation
            was created.
        created_by (str):
            Output only. The user who created the
            evaluation.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the evaluation
            was last updated.
        last_updated_by (str):
            Output only. The user who last updated the
            evaluation.
        evaluation_runs (MutableSequence[str]):
            Output only. The EvaluationRuns that this
            Evaluation is associated with.
        etag (str):
            Output only. Etag used to ensure the object
            hasn't changed during a read-modify-write
            operation. If the etag is empty, the update will
            overwrite any concurrent changes.
        aggregated_metrics (google.cloud.ces_v1beta.types.AggregatedMetrics):
            Output only. The aggregated metrics for this
            evaluation across all runs.
        last_completed_result (google.cloud.ces_v1beta.types.EvaluationResult):
            Output only. The latest evaluation result for
            this evaluation.
        invalid (bool):
            Output only. Whether the evaluation is
            invalid. This can happen if an evaluation is
            referencing a tool, toolset, or agent that has
            since been deleted.
        last_ten_results (MutableSequence[google.cloud.ces_v1beta.types.EvaluationResult]):
            Output only. The last 10 evaluation results for this
            evaluation. This is only populated if
            include_last_ten_results is set to true in the
            ListEvaluationsRequest or GetEvaluationRequest.
        evaluation_metrics_threshold_override (google.cloud.ces_v1beta.types.EvaluationMetricsThresholds):
            Optional. Overrides metrics thresholds for
            this specific evaluation.
        evaluation_metrics_config_override (google.cloud.ces_v1beta.types.EvaluationMetricsConfig):
            Optional. Overrides metrics config for this
            specific evaluation.
    """

    class GoldenExpectation(proto.Message):
        r"""Represents a single, checkable requirement.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            tool_call (google.cloud.ces_v1beta.types.ToolCall):
                Optional. Check that a specific tool was
                called with the parameters.

                This field is a member of `oneof`_ ``condition``.
            tool_response (google.cloud.ces_v1beta.types.ToolResponse):
                Optional. Check that a specific tool had the
                expected response.

                This field is a member of `oneof`_ ``condition``.
            agent_response (google.cloud.ces_v1beta.types.Message):
                Optional. Check that the agent responded with
                the correct response. The role "agent" is
                implied.

                This field is a member of `oneof`_ ``condition``.
            agent_transfer (google.cloud.ces_v1beta.types.AgentTransfer):
                Optional. Check that the agent transferred
                the conversation to a different agent.

                This field is a member of `oneof`_ ``condition``.
            updated_variables (google.protobuf.struct_pb2.Struct):
                Optional. Check that the agent updated the
                session variables to the expected values. Used
                to also capture agent variable updates for
                golden evals.

                This field is a member of `oneof`_ ``condition``.
            mock_tool_response (google.cloud.ces_v1beta.types.ToolResponse):
                Optional. The tool response to mock, with the
                parameters of interest specified. Any parameters
                not specified will be hallucinated by the LLM.

                This field is a member of `oneof`_ ``condition``.
            no_tool_calls (bool):
                Optional. Check that no tools were called
                during this turn.

                This field is a member of `oneof`_ ``condition``.
            note (str):
                Optional. A note for this requirement, useful in reporting
                when specific checks fail. E.g.,
                "Check_Payment_Tool_Called".
            skip_evaluation (bool):
                Optional. If set to true, this specific
                expectation will not be evaluated.
            expectation_level_metrics_thresholds_override (google.cloud.ces_v1beta.types.EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.ExpectationLevelMetricsThresholds):
                Optional. Overrides metrics at the step
                level.
            agent_response_semantic_similarity_metrics_config_override (google.cloud.ces_v1beta.types.EvaluationMetricsConfig.SemanticSimilarityMetricsConfig):
                Optional. Overrides for agent_response semantic similarity
                metrics.
            agent_response_hallucination_metrics_config_override (google.cloud.ces_v1beta.types.EvaluationMetricsConfig.HallucinationMetricsConfig):
                Optional. Overrides for agent_response hallucination
                metrics.
            comparison_type (google.cloud.ces_v1beta.types.EvaluationMetricsConfig.ComparisonType):
                Optional. The comparison type to use for the
                expectation check.
        """

        tool_call: example.ToolCall = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="condition",
            message=example.ToolCall,
        )
        tool_response: example.ToolResponse = proto.Field(
            proto.MESSAGE,
            number=3,
            oneof="condition",
            message=example.ToolResponse,
        )
        agent_response: example.Message = proto.Field(
            proto.MESSAGE,
            number=4,
            oneof="condition",
            message=example.Message,
        )
        agent_transfer: example.AgentTransfer = proto.Field(
            proto.MESSAGE,
            number=5,
            oneof="condition",
            message=example.AgentTransfer,
        )
        updated_variables: struct_pb2.Struct = proto.Field(
            proto.MESSAGE,
            number=6,
            oneof="condition",
            message=struct_pb2.Struct,
        )
        mock_tool_response: example.ToolResponse = proto.Field(
            proto.MESSAGE,
            number=7,
            oneof="condition",
            message=example.ToolResponse,
        )
        no_tool_calls: bool = proto.Field(
            proto.BOOL,
            number=13,
            oneof="condition",
        )
        note: str = proto.Field(
            proto.STRING,
            number=1,
        )
        skip_evaluation: bool = proto.Field(
            proto.BOOL,
            number=8,
        )
        expectation_level_metrics_thresholds_override: gcc_app.EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.ExpectationLevelMetricsThresholds = proto.Field(
            proto.MESSAGE,
            number=9,
            message=gcc_app.EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.ExpectationLevelMetricsThresholds,
        )
        agent_response_semantic_similarity_metrics_config_override: evaluation_metrics_config.EvaluationMetricsConfig.SemanticSimilarityMetricsConfig = proto.Field(
            proto.MESSAGE,
            number=10,
            message=evaluation_metrics_config.EvaluationMetricsConfig.SemanticSimilarityMetricsConfig,
        )
        agent_response_hallucination_metrics_config_override: evaluation_metrics_config.EvaluationMetricsConfig.HallucinationMetricsConfig = proto.Field(
            proto.MESSAGE,
            number=11,
            message=evaluation_metrics_config.EvaluationMetricsConfig.HallucinationMetricsConfig,
        )
        comparison_type: evaluation_metrics_config.EvaluationMetricsConfig.ComparisonType = proto.Field(
            proto.ENUM,
            number=12,
            enum=evaluation_metrics_config.EvaluationMetricsConfig.ComparisonType,
        )

    class Step(proto.Message):
        r"""A step defines a singular action to happen during the
        evaluation.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            user_input (google.cloud.ces_v1beta.types.SessionInput):
                Optional. User input for the conversation.

                This field is a member of `oneof`_ ``step``.
            agent_transfer (google.cloud.ces_v1beta.types.AgentTransfer):
                Optional. Transfer the conversation to a
                different agent.

                This field is a member of `oneof`_ ``step``.
            expectation (google.cloud.ces_v1beta.types.Evaluation.GoldenExpectation):
                Optional. Executes an expectation on the
                current turn.

                This field is a member of `oneof`_ ``step``.
        """

        user_input: session_service.SessionInput = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="step",
            message=session_service.SessionInput,
        )
        agent_transfer: example.AgentTransfer = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="step",
            message=example.AgentTransfer,
        )
        expectation: "Evaluation.GoldenExpectation" = proto.Field(
            proto.MESSAGE,
            number=3,
            oneof="step",
            message="Evaluation.GoldenExpectation",
        )

    class GoldenTurn(proto.Message):
        r"""A golden turn defines a single turn in a golden conversation.

        Attributes:
            steps (MutableSequence[google.cloud.ces_v1beta.types.Evaluation.Step]):
                Required. The steps required to replay a
                golden conversation.
            root_span (google.cloud.ces_v1beta.types.Span):
                Optional. The root span of the golden turn
                for processing and maintaining audio
                information. The uri for the audio must contain
                audio saved in 16Khz sample rate.
            turn_level_metrics_thresholds_override (google.cloud.ces_v1beta.types.EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds):
                Optional. Overrides for turn-level metric
                thresholds.
            hallucination_metric_behavior_override (google.cloud.ces_v1beta.types.EvaluationMetricsThresholds.HallucinationMetricBehavior):
                Optional. Override for turn-level
                hallucination metric behavior.
        """

        steps: MutableSequence["Evaluation.Step"] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="Evaluation.Step",
        )
        root_span: common.Span = proto.Field(
            proto.MESSAGE,
            number=2,
            message=common.Span,
        )
        turn_level_metrics_thresholds_override: gcc_app.EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds = proto.Field(
            proto.MESSAGE,
            number=3,
            message=gcc_app.EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds,
        )
        hallucination_metric_behavior_override: gcc_app.EvaluationMetricsThresholds.HallucinationMetricBehavior = proto.Field(
            proto.ENUM,
            number=4,
            enum=gcc_app.EvaluationMetricsThresholds.HallucinationMetricBehavior,
        )

    class Golden(proto.Message):
        r"""The steps required to replay a golden conversation.

        Attributes:
            turns (MutableSequence[google.cloud.ces_v1beta.types.Evaluation.GoldenTurn]):
                Required. The golden turns required to replay
                a golden conversation. The maximum number of
                allowed turns is 100.
            evaluation_expectations (MutableSequence[str]):
                Optional. The evaluation expectations to evaluate the
                replayed conversation against. Format:
                ``projects/{project}/locations/{location}/apps/{app}/evaluationExpectations/{evaluationExpectation}``
        """

        turns: MutableSequence["Evaluation.GoldenTurn"] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="Evaluation.GoldenTurn",
        )
        evaluation_expectations: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=3,
        )

    class ScenarioExpectation(proto.Message):
        r"""The expectation to evaluate the conversation produced by the
        simulation.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            tool_expectation (google.cloud.ces_v1beta.types.Evaluation.ScenarioExpectation.ToolExpectation):
                Optional. The tool call and response pair to
                be evaluated.

                This field is a member of `oneof`_ ``expectation``.
            agent_response (google.cloud.ces_v1beta.types.Message):
                Optional. The agent response to be evaluated.

                This field is a member of `oneof`_ ``expectation``.
        """

        class ToolExpectation(proto.Message):
            r"""The tool call and response pair to be evaluated.

            Attributes:
                expected_tool_call (google.cloud.ces_v1beta.types.ToolCall):
                    Required. The expected tool call, with the
                    parameters of interest specified. Any parameters
                    not specified will be hallucinated by the LLM.
                mock_tool_response (google.cloud.ces_v1beta.types.ToolResponse):
                    Required. The tool response to mock, with the
                    parameters of interest specified. Any parameters
                    not specified will be hallucinated by the LLM.
            """

            expected_tool_call: example.ToolCall = proto.Field(
                proto.MESSAGE,
                number=1,
                message=example.ToolCall,
            )
            mock_tool_response: example.ToolResponse = proto.Field(
                proto.MESSAGE,
                number=2,
                message=example.ToolResponse,
            )

        tool_expectation: "Evaluation.ScenarioExpectation.ToolExpectation" = (
            proto.Field(
                proto.MESSAGE,
                number=1,
                oneof="expectation",
                message="Evaluation.ScenarioExpectation.ToolExpectation",
            )
        )
        agent_response: example.Message = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="expectation",
            message=example.Message,
        )

    class Scenario(proto.Message):
        r"""The config for a scenario

        Attributes:
            task (str):
                Required. The task to be targeted by the
                scenario.
            user_facts (MutableSequence[google.cloud.ces_v1beta.types.Evaluation.Scenario.UserFact]):
                Optional. The user facts to be used by the
                scenario.
            max_turns (int):
                Optional. The maximum number of turns to
                simulate. The maximum allowed value is 100. The
                default value is 100.
            rubrics (MutableSequence[str]):
                Required. The rubrics to score the scenario
                against.
            scenario_expectations (MutableSequence[google.cloud.ces_v1beta.types.Evaluation.ScenarioExpectation]):
                Required. The ScenarioExpectations to
                evaluate the conversation produced by the user
                simulation.
            variable_overrides (google.protobuf.struct_pb2.Struct):
                Optional. Variables / Session Parameters as
                context for the session, keyed by variable
                names. Members of this struct will override any
                default values set by the system.

                Note, these are different from user facts, which
                are facts known to the user. Variables are
                parameters known to the agent: i.e. MDN (phone
                number) passed by the telephony system.
            task_completion_behavior (google.cloud.ces_v1beta.types.Evaluation.Scenario.TaskCompletionBehavior):
                Optional. Deprecated. Use user_goal_behavior instead.
            user_goal_behavior (google.cloud.ces_v1beta.types.Evaluation.Scenario.UserGoalBehavior):
                Optional. The expected behavior of the user
                goal.
            evaluation_expectations (MutableSequence[str]):
                Optional. The evaluation expectations to evaluate the
                conversation produced by the simulation against. Format:
                ``projects/{project}/locations/{location}/apps/{app}/evaluationExpectations/{evaluationExpectation}``
            scenario_execution_mode (google.cloud.ces_v1beta.types.EvaluationSettings.ScenarioExecutionMode):
                Optional. The execution mode for scenario
                evaluations.
        """

        class TaskCompletionBehavior(proto.Enum):
            r"""The expected behavior of the user task. This is used to
            determine whether the scenario is successful.

            Values:
                TASK_COMPLETION_BEHAVIOR_UNSPECIFIED (0):
                    Behavior unspecified. Will default to TASK_SATISFIED.
                TASK_SATISFIED (1):
                    The user task should be completed
                    successfully.
                TASK_REJECTED (2):
                    The user task should be rejected.
            """

            TASK_COMPLETION_BEHAVIOR_UNSPECIFIED = 0
            TASK_SATISFIED = 1
            TASK_REJECTED = 2

        class UserGoalBehavior(proto.Enum):
            r"""The expected behavior of the user goal. This is used to
            determine whether the scenario is successful.

            Values:
                USER_GOAL_BEHAVIOR_UNSPECIFIED (0):
                    Behavior unspecified. Will default to USER_GOAL_SATISFIED.
                USER_GOAL_SATISFIED (1):
                    The user goal should be completed
                    successfully.
                USER_GOAL_REJECTED (2):
                    The user goal should be rejected.
                USER_GOAL_IGNORED (3):
                    Ignore the user goal status.
            """

            USER_GOAL_BEHAVIOR_UNSPECIFIED = 0
            USER_GOAL_SATISFIED = 1
            USER_GOAL_REJECTED = 2
            USER_GOAL_IGNORED = 3

        class UserFact(proto.Message):
            r"""Facts about the user as a key value pair.

            Attributes:
                name (str):
                    Required. The name of the user fact.
                value (str):
                    Required. The value of the user fact.
            """

            name: str = proto.Field(
                proto.STRING,
                number=1,
            )
            value: str = proto.Field(
                proto.STRING,
                number=2,
            )

        task: str = proto.Field(
            proto.STRING,
            number=1,
        )
        user_facts: MutableSequence["Evaluation.Scenario.UserFact"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=4,
                message="Evaluation.Scenario.UserFact",
            )
        )
        max_turns: int = proto.Field(
            proto.INT32,
            number=5,
        )
        rubrics: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )
        scenario_expectations: MutableSequence["Evaluation.ScenarioExpectation"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=3,
                message="Evaluation.ScenarioExpectation",
            )
        )
        variable_overrides: struct_pb2.Struct = proto.Field(
            proto.MESSAGE,
            number=6,
            message=struct_pb2.Struct,
        )
        task_completion_behavior: "Evaluation.Scenario.TaskCompletionBehavior" = (
            proto.Field(
                proto.ENUM,
                number=7,
                enum="Evaluation.Scenario.TaskCompletionBehavior",
            )
        )
        user_goal_behavior: "Evaluation.Scenario.UserGoalBehavior" = proto.Field(
            proto.ENUM,
            number=8,
            enum="Evaluation.Scenario.UserGoalBehavior",
        )
        evaluation_expectations: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=10,
        )
        scenario_execution_mode: gcc_app.EvaluationSettings.ScenarioExecutionMode = (
            proto.Field(
                proto.ENUM,
                number=12,
                enum=gcc_app.EvaluationSettings.ScenarioExecutionMode,
            )
        )

    golden: Golden = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="inputs",
        message=Golden,
    )
    scenario: Scenario = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="inputs",
        message=Scenario,
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    evaluation_datasets: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    created_by: str = proto.Field(
        proto.STRING,
        number=13,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    last_updated_by: str = proto.Field(
        proto.STRING,
        number=14,
    )
    evaluation_runs: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=15,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=10,
    )
    aggregated_metrics: "AggregatedMetrics" = proto.Field(
        proto.MESSAGE,
        number=16,
        message="AggregatedMetrics",
    )
    last_completed_result: "EvaluationResult" = proto.Field(
        proto.MESSAGE,
        number=17,
        message="EvaluationResult",
    )
    invalid: bool = proto.Field(
        proto.BOOL,
        number=18,
    )
    last_ten_results: MutableSequence["EvaluationResult"] = proto.RepeatedField(
        proto.MESSAGE,
        number=19,
        message="EvaluationResult",
    )
    evaluation_metrics_threshold_override: gcc_app.EvaluationMetricsThresholds = (
        proto.Field(
            proto.MESSAGE,
            number=20,
            message=gcc_app.EvaluationMetricsThresholds,
        )
    )
    evaluation_metrics_config_override: evaluation_metrics_config.EvaluationMetricsConfig = proto.Field(
        proto.MESSAGE,
        number=21,
        message=evaluation_metrics_config.EvaluationMetricsConfig,
    )


class EvaluationDataset(proto.Message):
    r"""An evaluation dataset represents a set of evaluations that
    are grouped together basaed on shared tags.

    Attributes:
        name (str):
            Identifier. The unique identifier of this evaluation
            dataset. Format:
            ``projects/{project}/locations/{location}/apps/{app}/evaluationDatasets/{evaluationDataset}``
        display_name (str):
            Required. User-defined display name of the
            evaluation dataset. Unique within an App.
        evaluations (MutableSequence[str]):
            Optional. Evaluations that are included in
            this dataset.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the evaluation
            dataset was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the evaluation
            dataset was last updated.
        etag (str):
            Output only. Etag used to ensure the object
            hasn't changed during a read-modify-write
            operation. If the etag is empty, the update will
            overwrite any concurrent changes.
        created_by (str):
            Output only. The user who created the
            evaluation dataset.
        last_updated_by (str):
            Output only. The user who last updated the
            evaluation dataset.
        aggregated_metrics (google.cloud.ces_v1beta.types.AggregatedMetrics):
            Output only. The aggregated metrics for this
            evaluation dataset across all runs.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    evaluations: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=6,
    )
    created_by: str = proto.Field(
        proto.STRING,
        number=7,
    )
    last_updated_by: str = proto.Field(
        proto.STRING,
        number=8,
    )
    aggregated_metrics: "AggregatedMetrics" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="AggregatedMetrics",
    )


class EvaluationResult(proto.Message):
    r"""An evaluation result represents the output of running an
    Evaluation.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        golden_result (google.cloud.ces_v1beta.types.EvaluationResult.GoldenResult):
            Output only. The outcome of a golden
            evaluation.

            This field is a member of `oneof`_ ``result``.
        scenario_result (google.cloud.ces_v1beta.types.EvaluationResult.ScenarioResult):
            Output only. The outcome of a scenario
            evaluation.

            This field is a member of `oneof`_ ``result``.
        name (str):
            Identifier. The unique identifier of the evaluation result.
            Format:
            ``projects/{project}/locations/{location}/apps/{app}/evaluations/{evaluation}/results/{result}``
        display_name (str):
            Required. Display name of the Evaluation
            Result. Unique within an Evaluation. By default,
            it has the following format:

            "<evaluation-display-name> result
            - <timestamp>".
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the evaluation
            result was created.
        evaluation_status (google.cloud.ces_v1beta.types.EvaluationResult.Outcome):
            Output only. The outcome of the evaluation. Only populated
            if execution_state is COMPLETE.
        evaluation_run (str):
            Output only. The evaluation run that produced this result.
            Format:
            ``projects/{project}/locations/{location}/apps/{app}/evaluationRuns/{evaluationRun}``
        persona (google.cloud.ces_v1beta.types.EvaluationPersona):
            Output only. The persona used to generate the
            conversation for the evaluation result.
        error_info (google.cloud.ces_v1beta.types.EvaluationErrorInfo):
            Output only. Error information for the
            evaluation result.
        error (google.rpc.status_pb2.Status):
            Output only. Deprecated: Use ``error_info`` instead. Errors
            encountered during execution.
        initiated_by (str):
            Output only. The user who initiated the
            evaluation run that resulted in this result.
        app_version (str):
            Output only. The app version used to generate the
            conversation that resulted in this result. Format:
            ``projects/{project}/locations/{location}/apps/{app}/versions/{version}``
        app_version_display_name (str):
            Output only. The display name of the ``app_version`` that
            the evaluation ran against.
        changelog (str):
            Output only. The changelog of the app version
            that the evaluation ran against. This is
            populated if user runs evaluation on
            latest/draft.
        changelog_create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The create time of the changelog
            of the app version that the evaluation ran
            against. This is populated if user runs
            evaluation on latest/draft.
        execution_state (google.cloud.ces_v1beta.types.EvaluationResult.ExecutionState):
            Output only. The state of the evaluation
            result execution.
        evaluation_metrics_thresholds (google.cloud.ces_v1beta.types.EvaluationMetricsThresholds):
            Output only. The evaluation thresholds for
            the result.
        config (google.cloud.ces_v1beta.types.EvaluationConfig):
            Output only. The configuration used in the
            evaluation run that resulted in this result.
        golden_run_method (google.cloud.ces_v1beta.types.GoldenRunMethod):
            Output only. The method used to run the
            golden evaluation.
    """

    class Outcome(proto.Enum):
        r"""The outcome of the evaluation or expectation.

        Values:
            OUTCOME_UNSPECIFIED (0):
                Evaluation outcome is not specified.
            PASS (1):
                Evaluation/Expectation passed. In the case of
                an evaluation, this means that all expectations
                were met.
            FAIL (2):
                Evaluation/Expectation failed. In the case of
                an evaluation, this means that at least one
                expectation was not met.
            SKIPPED (3):
                Evaluation/Expectation was skipped.
        """

        OUTCOME_UNSPECIFIED = 0
        PASS = 1
        FAIL = 2
        SKIPPED = 3

    class ExecutionState(proto.Enum):
        r"""The state of the evaluation result execution.

        Values:
            EXECUTION_STATE_UNSPECIFIED (0):
                Evaluation result execution state is not
                specified.
            QUEUED (5):
                Evaluation result execution is queued.
            RUNNING (1):
                Evaluation result execution is running.
            COMPLETED (2):
                Evaluation result execution has completed.
            ERROR (3):
                Evaluation result execution failed due to an
                internal error.
            CANCELLED (4):
                Evaluation result execution was cancelled.
        """

        EXECUTION_STATE_UNSPECIFIED = 0
        QUEUED = 5
        RUNNING = 1
        COMPLETED = 2
        ERROR = 3
        CANCELLED = 4

    class GoldenExpectationOutcome(proto.Message):
        r"""Specifies the expectation and the result of that expectation.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            observed_tool_call (google.cloud.ces_v1beta.types.ToolCall):
                Output only. The result of the tool call
                expectation.

                This field is a member of `oneof`_ ``result``.
            observed_tool_response (google.cloud.ces_v1beta.types.ToolResponse):
                Output only. The result of the tool response
                expectation.

                This field is a member of `oneof`_ ``result``.
            observed_agent_response (google.cloud.ces_v1beta.types.Message):
                Output only. The result of the agent response
                expectation.

                This field is a member of `oneof`_ ``result``.
            observed_agent_transfer (google.cloud.ces_v1beta.types.AgentTransfer):
                Output only. The result of the agent transfer
                expectation.

                This field is a member of `oneof`_ ``result``.
            observed_payload (google.protobuf.struct_pb2.Struct):
                Output only. An observed custom payload.
                There are no expectations for custom payloads.
                This is only used for metrics calculation. The
                outcome is always SKIPPED.

                This field is a member of `oneof`_ ``result``.
            expectation (google.cloud.ces_v1beta.types.Evaluation.GoldenExpectation):
                Output only. The expectation that was
                evaluated.
            outcome (google.cloud.ces_v1beta.types.EvaluationResult.Outcome):
                Output only. The outcome of the expectation.
            semantic_similarity_result (google.cloud.ces_v1beta.types.EvaluationResult.SemanticSimilarityResult):
                Output only. The result of the semantic
                similarity check.
            tool_invocation_result (google.cloud.ces_v1beta.types.EvaluationResult.GoldenExpectationOutcome.ToolInvocationResult):
                Output only. The result of the tool
                invocation check.
        """

        class ToolInvocationResult(proto.Message):
            r"""The result of the tool invocation check.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                parameter_correctness_score (float):
                    Output only. The tool invocation parameter
                    correctness score. This indicates the percent of
                    parameters from the expected tool call that were
                    also present in the actual tool call.

                    This field is a member of `oneof`_ ``_parameter_correctness_score``.
                outcome (google.cloud.ces_v1beta.types.EvaluationResult.Outcome):
                    Output only. The outcome of the tool invocation check. This
                    is determined by comparing the parameter_correctness_score
                    to the threshold. If the score is equal to or above the
                    threshold, the outcome will be PASS. Otherwise, the outcome
                    will be FAIL.
                explanation (str):
                    Output only. A free text explanation for the
                    tool invocation result.
            """

            parameter_correctness_score: float = proto.Field(
                proto.FLOAT,
                number=1,
                optional=True,
            )
            outcome: "EvaluationResult.Outcome" = proto.Field(
                proto.ENUM,
                number=2,
                enum="EvaluationResult.Outcome",
            )
            explanation: str = proto.Field(
                proto.STRING,
                number=3,
            )

        observed_tool_call: example.ToolCall = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="result",
            message=example.ToolCall,
        )
        observed_tool_response: example.ToolResponse = proto.Field(
            proto.MESSAGE,
            number=3,
            oneof="result",
            message=example.ToolResponse,
        )
        observed_agent_response: example.Message = proto.Field(
            proto.MESSAGE,
            number=4,
            oneof="result",
            message=example.Message,
        )
        observed_agent_transfer: example.AgentTransfer = proto.Field(
            proto.MESSAGE,
            number=5,
            oneof="result",
            message=example.AgentTransfer,
        )
        observed_payload: struct_pb2.Struct = proto.Field(
            proto.MESSAGE,
            number=9,
            oneof="result",
            message=struct_pb2.Struct,
        )
        expectation: "Evaluation.GoldenExpectation" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="Evaluation.GoldenExpectation",
        )
        outcome: "EvaluationResult.Outcome" = proto.Field(
            proto.ENUM,
            number=6,
            enum="EvaluationResult.Outcome",
        )
        semantic_similarity_result: "EvaluationResult.SemanticSimilarityResult" = (
            proto.Field(
                proto.MESSAGE,
                number=7,
                message="EvaluationResult.SemanticSimilarityResult",
            )
        )
        tool_invocation_result: "EvaluationResult.GoldenExpectationOutcome.ToolInvocationResult" = proto.Field(
            proto.MESSAGE,
            number=8,
            message="EvaluationResult.GoldenExpectationOutcome.ToolInvocationResult",
        )

    class EvaluationExpectationResult(proto.Message):
        r"""The result of a single evaluation expectation.

        Attributes:
            evaluation_expectation (str):
                Output only. The evaluation expectation. Format:
                ``projects/{project}/locations/{location}/apps/{app}/evaluationExpectations/{evaluation_expectation}``
            prompt (str):
                Output only. The prompt that was used for the
                evaluation.
            outcome (google.cloud.ces_v1beta.types.EvaluationResult.Outcome):
                Output only. The outcome of the evaluation
                expectation.
            explanation (str):
                Output only. The explanation for the result.
        """

        evaluation_expectation: str = proto.Field(
            proto.STRING,
            number=1,
        )
        prompt: str = proto.Field(
            proto.STRING,
            number=2,
        )
        outcome: "EvaluationResult.Outcome" = proto.Field(
            proto.ENUM,
            number=3,
            enum="EvaluationResult.Outcome",
        )
        explanation: str = proto.Field(
            proto.STRING,
            number=4,
        )

    class GoldenResult(proto.Message):
        r"""The result of a golden evaluation.

        Attributes:
            turn_replay_results (MutableSequence[google.cloud.ces_v1beta.types.EvaluationResult.GoldenResult.TurnReplayResult]):
                Output only. The result of running each turn
                of the golden conversation.
            evaluation_expectation_results (MutableSequence[google.cloud.ces_v1beta.types.EvaluationResult.EvaluationExpectationResult]):
                Output only. The results of the evaluation
                expectations.
        """

        class TurnReplayResult(proto.Message):
            r"""The result of running a single turn of the golden
            conversation.


            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                conversation (str):
                    Output only. The conversation that was
                    generated for this turn.
                expectation_outcome (MutableSequence[google.cloud.ces_v1beta.types.EvaluationResult.GoldenExpectationOutcome]):
                    Output only. The outcome of each expectation.
                hallucination_result (google.cloud.ces_v1beta.types.EvaluationResult.HallucinationResult):
                    Output only. The result of the hallucination
                    check.
                tool_invocation_score (float):
                    Output only. Deprecated. Use
                    OverallToolInvocationResult instead.
                tool_ordered_invocation_score (float):
                    Output only. The overall tool ordered
                    invocation score for this turn. This indicates
                    the overall percent of tools from the expected
                    turn that were actually invoked in the expected
                    order.

                    This field is a member of `oneof`_ ``_tool_ordered_invocation_score``.
                turn_latency (google.protobuf.duration_pb2.Duration):
                    Output only. Duration of the turn.
                tool_call_latencies (MutableSequence[google.cloud.ces_v1beta.types.EvaluationResult.ToolCallLatency]):
                    Output only. The latency of each tool call in
                    the turn.
                semantic_similarity_result (google.cloud.ces_v1beta.types.EvaluationResult.SemanticSimilarityResult):
                    Output only. The result of the semantic
                    similarity check.
                overall_tool_invocation_result (google.cloud.ces_v1beta.types.EvaluationResult.OverallToolInvocationResult):
                    Output only. The result of the overall tool
                    invocation check.
                error_info (google.cloud.ces_v1beta.types.EvaluationErrorInfo):
                    Output only. Information about the error that
                    occurred during this turn.
                span_latencies (MutableSequence[google.cloud.ces_v1beta.types.EvaluationResult.SpanLatency]):
                    Output only. The latency of spans in the
                    turn.
            """

            conversation: str = proto.Field(
                proto.STRING,
                number=1,
            )
            expectation_outcome: MutableSequence[
                "EvaluationResult.GoldenExpectationOutcome"
            ] = proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message="EvaluationResult.GoldenExpectationOutcome",
            )
            hallucination_result: "EvaluationResult.HallucinationResult" = proto.Field(
                proto.MESSAGE,
                number=3,
                message="EvaluationResult.HallucinationResult",
            )
            tool_invocation_score: float = proto.Field(
                proto.FLOAT,
                number=4,
            )
            tool_ordered_invocation_score: float = proto.Field(
                proto.FLOAT,
                number=5,
                optional=True,
            )
            turn_latency: duration_pb2.Duration = proto.Field(
                proto.MESSAGE,
                number=6,
                message=duration_pb2.Duration,
            )
            tool_call_latencies: MutableSequence["EvaluationResult.ToolCallLatency"] = (
                proto.RepeatedField(
                    proto.MESSAGE,
                    number=7,
                    message="EvaluationResult.ToolCallLatency",
                )
            )
            semantic_similarity_result: "EvaluationResult.SemanticSimilarityResult" = (
                proto.Field(
                    proto.MESSAGE,
                    number=8,
                    message="EvaluationResult.SemanticSimilarityResult",
                )
            )
            overall_tool_invocation_result: "EvaluationResult.OverallToolInvocationResult" = proto.Field(
                proto.MESSAGE,
                number=9,
                message="EvaluationResult.OverallToolInvocationResult",
            )
            error_info: "EvaluationErrorInfo" = proto.Field(
                proto.MESSAGE,
                number=10,
                message="EvaluationErrorInfo",
            )
            span_latencies: MutableSequence["EvaluationResult.SpanLatency"] = (
                proto.RepeatedField(
                    proto.MESSAGE,
                    number=11,
                    message="EvaluationResult.SpanLatency",
                )
            )

        turn_replay_results: MutableSequence[
            "EvaluationResult.GoldenResult.TurnReplayResult"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="EvaluationResult.GoldenResult.TurnReplayResult",
        )
        evaluation_expectation_results: MutableSequence[
            "EvaluationResult.EvaluationExpectationResult"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="EvaluationResult.EvaluationExpectationResult",
        )

    class ScenarioRubricOutcome(proto.Message):
        r"""The outcome of the evaluation against the rubric.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            rubric (str):
                Output only. The rubric that was used to
                evaluate the conversation.
            score (float):
                Output only. The score of the conversation
                against the rubric.

                This field is a member of `oneof`_ ``_score``.
            score_explanation (str):
                Output only. The rater's response to the
                rubric.
        """

        rubric: str = proto.Field(
            proto.STRING,
            number=1,
        )
        score: float = proto.Field(
            proto.FLOAT,
            number=2,
            optional=True,
        )
        score_explanation: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class ScenarioExpectationOutcome(proto.Message):
        r"""The outcome of a scenario expectation.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            observed_tool_call (google.cloud.ces_v1beta.types.EvaluationResult.ScenarioExpectationOutcome.ObservedToolCall):
                Output only. The observed tool call.

                This field is a member of `oneof`_ ``result``.
            observed_agent_response (google.cloud.ces_v1beta.types.Message):
                Output only. The observed agent response.

                This field is a member of `oneof`_ ``result``.
            expectation (google.cloud.ces_v1beta.types.Evaluation.ScenarioExpectation):
                Output only. The expectation that was
                evaluated.
            outcome (google.cloud.ces_v1beta.types.EvaluationResult.Outcome):
                Output only. The outcome of the
                ScenarioExpectation.
        """

        class ObservedToolCall(proto.Message):
            r"""The observed tool call and response.

            Attributes:
                tool_call (google.cloud.ces_v1beta.types.ToolCall):
                    Output only. The observed tool call.
                tool_response (google.cloud.ces_v1beta.types.ToolResponse):
                    Output only. The observed tool response.
            """

            tool_call: example.ToolCall = proto.Field(
                proto.MESSAGE,
                number=1,
                message=example.ToolCall,
            )
            tool_response: example.ToolResponse = proto.Field(
                proto.MESSAGE,
                number=2,
                message=example.ToolResponse,
            )

        observed_tool_call: "EvaluationResult.ScenarioExpectationOutcome.ObservedToolCall" = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="result",
            message="EvaluationResult.ScenarioExpectationOutcome.ObservedToolCall",
        )
        observed_agent_response: example.Message = proto.Field(
            proto.MESSAGE,
            number=3,
            oneof="result",
            message=example.Message,
        )
        expectation: "Evaluation.ScenarioExpectation" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="Evaluation.ScenarioExpectation",
        )
        outcome: "EvaluationResult.Outcome" = proto.Field(
            proto.ENUM,
            number=4,
            enum="EvaluationResult.Outcome",
        )

    class ScenarioResult(proto.Message):
        r"""The outcome of a scenario evaluation.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            conversation (str):
                Output only. The conversation that was
                generated in the scenario.
            task (str):
                Output only. The task that was used when
                running the scenario for this result.
            user_facts (MutableSequence[google.cloud.ces_v1beta.types.Evaluation.Scenario.UserFact]):
                Output only. The user facts that were used by
                the scenario for this result.
            expectation_outcomes (MutableSequence[google.cloud.ces_v1beta.types.EvaluationResult.ScenarioExpectationOutcome]):
                Output only. The outcome of each expectation.
            rubric_outcomes (MutableSequence[google.cloud.ces_v1beta.types.EvaluationResult.ScenarioRubricOutcome]):
                Output only. The outcome of the rubric.
            hallucination_result (MutableSequence[google.cloud.ces_v1beta.types.EvaluationResult.HallucinationResult]):
                Output only. The result of the hallucination
                check. There will be one hallucination result
                for each turn in the conversation.
            task_completion_result (google.cloud.ces_v1beta.types.EvaluationResult.TaskCompletionResult):
                Output only. The result of the task
                completion check.
            tool_call_latencies (MutableSequence[google.cloud.ces_v1beta.types.EvaluationResult.ToolCallLatency]):
                Output only. The latency of each tool call
                execution in the conversation.
            user_goal_satisfaction_result (google.cloud.ces_v1beta.types.EvaluationResult.UserGoalSatisfactionResult):
                Output only. The result of the user goal
                satisfaction check.
            all_expectations_satisfied (bool):
                Output only. Whether all expectations were
                satisfied for this turn.

                This field is a member of `oneof`_ ``_all_expectations_satisfied``.
            task_completed (bool):
                Output only. Whether the task was completed
                for this turn. This is a composite of all
                expectations satisfied, no hallucinations, and
                user goal satisfaction.

                This field is a member of `oneof`_ ``_task_completed``.
            span_latencies (MutableSequence[google.cloud.ces_v1beta.types.EvaluationResult.SpanLatency]):
                Output only. The latency of spans in the
                conversation.
            evaluation_expectation_results (MutableSequence[google.cloud.ces_v1beta.types.EvaluationResult.EvaluationExpectationResult]):
                Output only. The results of the evaluation
                expectations.
        """

        conversation: str = proto.Field(
            proto.STRING,
            number=1,
        )
        task: str = proto.Field(
            proto.STRING,
            number=10,
        )
        user_facts: MutableSequence["Evaluation.Scenario.UserFact"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=11,
                message="Evaluation.Scenario.UserFact",
            )
        )
        expectation_outcomes: MutableSequence[
            "EvaluationResult.ScenarioExpectationOutcome"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="EvaluationResult.ScenarioExpectationOutcome",
        )
        rubric_outcomes: MutableSequence["EvaluationResult.ScenarioRubricOutcome"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=3,
                message="EvaluationResult.ScenarioRubricOutcome",
            )
        )
        hallucination_result: MutableSequence[
            "EvaluationResult.HallucinationResult"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message="EvaluationResult.HallucinationResult",
        )
        task_completion_result: "EvaluationResult.TaskCompletionResult" = proto.Field(
            proto.MESSAGE,
            number=5,
            message="EvaluationResult.TaskCompletionResult",
        )
        tool_call_latencies: MutableSequence["EvaluationResult.ToolCallLatency"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=6,
                message="EvaluationResult.ToolCallLatency",
            )
        )
        user_goal_satisfaction_result: "EvaluationResult.UserGoalSatisfactionResult" = (
            proto.Field(
                proto.MESSAGE,
                number=7,
                message="EvaluationResult.UserGoalSatisfactionResult",
            )
        )
        all_expectations_satisfied: bool = proto.Field(
            proto.BOOL,
            number=8,
            optional=True,
        )
        task_completed: bool = proto.Field(
            proto.BOOL,
            number=9,
            optional=True,
        )
        span_latencies: MutableSequence["EvaluationResult.SpanLatency"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=12,
                message="EvaluationResult.SpanLatency",
            )
        )
        evaluation_expectation_results: MutableSequence[
            "EvaluationResult.EvaluationExpectationResult"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=13,
            message="EvaluationResult.EvaluationExpectationResult",
        )

    class SpanLatency(proto.Message):
        r"""The latency of a span execution.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            resource (str):
                Output only. The resource name of the
                guardrail or tool spans.

                This field is a member of `oneof`_ ``identifier``.
            toolset (google.cloud.ces_v1beta.types.ToolsetTool):
                Output only. The toolset tool identifier.

                This field is a member of `oneof`_ ``identifier``.
            model (str):
                Output only. The name of the LLM span.

                This field is a member of `oneof`_ ``identifier``.
            callback (str):
                Output only. The name of the user callback
                span.

                This field is a member of `oneof`_ ``identifier``.
            type_ (google.cloud.ces_v1beta.types.EvaluationResult.SpanLatency.Type):
                Output only. The type of span.
            display_name (str):
                Output only. The display name of the span.
                Applicable to tool and guardrail spans.
            start_time (google.protobuf.timestamp_pb2.Timestamp):
                Output only. The start time of span.
            end_time (google.protobuf.timestamp_pb2.Timestamp):
                Output only. The end time of span.
            execution_latency (google.protobuf.duration_pb2.Duration):
                Output only. The latency of span.
        """

        class Type(proto.Enum):
            r"""The type of span.
            Additional values may be added in the future.

            Values:
                TYPE_UNSPECIFIED (0):
                    Default value. This value is unused.
                TOOL (1):
                    Tool call span.
                USER_CALLBACK (2):
                    User callback span.
                GUARDRAIL (3):
                    Guardrail span.
                LLM (4):
                    LLM span.
            """

            TYPE_UNSPECIFIED = 0
            TOOL = 1
            USER_CALLBACK = 2
            GUARDRAIL = 3
            LLM = 4

        resource: str = proto.Field(
            proto.STRING,
            number=2,
            oneof="identifier",
        )
        toolset: gcc_toolset_tool.ToolsetTool = proto.Field(
            proto.MESSAGE,
            number=3,
            oneof="identifier",
            message=gcc_toolset_tool.ToolsetTool,
        )
        model: str = proto.Field(
            proto.STRING,
            number=4,
            oneof="identifier",
        )
        callback: str = proto.Field(
            proto.STRING,
            number=5,
            oneof="identifier",
        )
        type_: "EvaluationResult.SpanLatency.Type" = proto.Field(
            proto.ENUM,
            number=1,
            enum="EvaluationResult.SpanLatency.Type",
        )
        display_name: str = proto.Field(
            proto.STRING,
            number=9,
        )
        start_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=6,
            message=timestamp_pb2.Timestamp,
        )
        end_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=7,
            message=timestamp_pb2.Timestamp,
        )
        execution_latency: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=8,
            message=duration_pb2.Duration,
        )

    class ToolCallLatency(proto.Message):
        r"""The latency of a tool call execution.

        Attributes:
            tool (str):
                Output only. The name of the tool that got executed. Format:
                ``projects/{project}/locations/{location}/apps/{app}/tools/{tool}``.
            display_name (str):
                Output only. The display name of the tool.
            start_time (google.protobuf.timestamp_pb2.Timestamp):
                Output only. The start time of the tool call
                execution.
            end_time (google.protobuf.timestamp_pb2.Timestamp):
                Output only. The end time of the tool call
                execution.
            execution_latency (google.protobuf.duration_pb2.Duration):
                Output only. The latency of the tool call
                execution.
        """

        tool: str = proto.Field(
            proto.STRING,
            number=1,
        )
        display_name: str = proto.Field(
            proto.STRING,
            number=2,
        )
        start_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=3,
            message=timestamp_pb2.Timestamp,
        )
        end_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=4,
            message=timestamp_pb2.Timestamp,
        )
        execution_latency: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=5,
            message=duration_pb2.Duration,
        )

    class HallucinationResult(proto.Message):
        r"""The result of the hallucination check for a single turn.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            score (int):
                Output only. The hallucination score. Can be
                -1, 0, 1.

                This field is a member of `oneof`_ ``_score``.
            label (str):
                Output only. The label associated with each
                score. Score 1: Justified
                Score 0: Not Justified
                Score -1: No Claim To Assess
            explanation (str):
                Output only. The explanation for the
                hallucination score.
        """

        score: int = proto.Field(
            proto.INT32,
            number=1,
            optional=True,
        )
        label: str = proto.Field(
            proto.STRING,
            number=2,
        )
        explanation: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class UserGoalSatisfactionResult(proto.Message):
        r"""The result of a user goal satisfaction check for a
        conversation.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            score (int):
                Output only. The user task satisfaction
                score. Can be -1, 0, 1.

                This field is a member of `oneof`_ ``_score``.
            label (str):
                Output only. The label associated with each
                score. Score 1: User Task Satisfied
                Score 0: User Task Not Satisfied
                Score -1: User Task Unspecified
            explanation (str):
                Output only. The explanation for the user
                task satisfaction score.
        """

        score: int = proto.Field(
            proto.INT32,
            number=1,
            optional=True,
        )
        label: str = proto.Field(
            proto.STRING,
            number=2,
        )
        explanation: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class SemanticSimilarityResult(proto.Message):
        r"""The result of the semantic similarity check.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            score (int):
                Output only. The semantic similarity score.
                Can be 0, 1, 2, 3, or 4.

                This field is a member of `oneof`_ ``_score``.
            label (str):
                Output only. The label associated with each
                score. Score 4: Fully Consistent
                Score 3: Mostly Consistent
                Score 2: Partially Consistent (Minor Omissions)
                Score 1: Largely Inconsistent (Major Omissions)
                Score 0: Completely Inconsistent / Contradictory
            explanation (str):
                Output only. The explanation for the semantic
                similarity score.
            outcome (google.cloud.ces_v1beta.types.EvaluationResult.Outcome):
                Output only. The outcome of the semantic similarity check.
                This is determined by comparing the score to the
                semantic_similarity_success_threshold. If the score is equal
                to or above the threshold, the outcome will be PASS.
                Otherwise, the outcome will be FAIL.
        """

        score: int = proto.Field(
            proto.INT32,
            number=1,
            optional=True,
        )
        label: str = proto.Field(
            proto.STRING,
            number=2,
        )
        explanation: str = proto.Field(
            proto.STRING,
            number=3,
        )
        outcome: "EvaluationResult.Outcome" = proto.Field(
            proto.ENUM,
            number=4,
            enum="EvaluationResult.Outcome",
        )

    class OverallToolInvocationResult(proto.Message):
        r"""The result of the overall tool invocation check.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            tool_invocation_score (float):
                The overall tool invocation score for this
                turn. This indicates the overall percent of
                tools from the expected turn that were actually
                invoked.

                This field is a member of `oneof`_ ``_tool_invocation_score``.
            outcome (google.cloud.ces_v1beta.types.EvaluationResult.Outcome):
                Output only. The outcome of the tool invocation check. This
                is determined by comparing the tool_invocation_score to the
                overall_tool_invocation_correctness_threshold. If the score
                is equal to or above the threshold, the outcome will be
                PASS. Otherwise, the outcome will be FAIL.
        """

        tool_invocation_score: float = proto.Field(
            proto.FLOAT,
            number=1,
            optional=True,
        )
        outcome: "EvaluationResult.Outcome" = proto.Field(
            proto.ENUM,
            number=2,
            enum="EvaluationResult.Outcome",
        )

    class TaskCompletionResult(proto.Message):
        r"""The result of the task completion check for the conversation.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            score (int):
                Output only. The task completion score. Can
                be -1, 0, 1

                This field is a member of `oneof`_ ``_score``.
            label (str):
                Output only. The label associated with each
                score. Score 1: Task Completed
                Score 0: Task Not Completed
                Score -1: User Goal Undefined
            explanation (str):
                Output only. The explanation for the task
                completion score.
        """

        score: int = proto.Field(
            proto.INT32,
            number=1,
            optional=True,
        )
        label: str = proto.Field(
            proto.STRING,
            number=2,
        )
        explanation: str = proto.Field(
            proto.STRING,
            number=3,
        )

    golden_result: GoldenResult = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="result",
        message=GoldenResult,
    )
    scenario_result: ScenarioResult = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="result",
        message=ScenarioResult,
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
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    evaluation_status: Outcome = proto.Field(
        proto.ENUM,
        number=4,
        enum=Outcome,
    )
    evaluation_run: str = proto.Field(
        proto.STRING,
        number=6,
    )
    persona: gcc_app.EvaluationPersona = proto.Field(
        proto.MESSAGE,
        number=17,
        message=gcc_app.EvaluationPersona,
    )
    error_info: "EvaluationErrorInfo" = proto.Field(
        proto.MESSAGE,
        number=15,
        message="EvaluationErrorInfo",
    )
    error: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=14,
        message=status_pb2.Status,
    )
    initiated_by: str = proto.Field(
        proto.STRING,
        number=9,
    )
    app_version: str = proto.Field(
        proto.STRING,
        number=10,
    )
    app_version_display_name: str = proto.Field(
        proto.STRING,
        number=13,
    )
    changelog: str = proto.Field(
        proto.STRING,
        number=21,
    )
    changelog_create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=22,
        message=timestamp_pb2.Timestamp,
    )
    execution_state: ExecutionState = proto.Field(
        proto.ENUM,
        number=11,
        enum=ExecutionState,
    )
    evaluation_metrics_thresholds: gcc_app.EvaluationMetricsThresholds = proto.Field(
        proto.MESSAGE,
        number=12,
        message=gcc_app.EvaluationMetricsThresholds,
    )
    config: "EvaluationConfig" = proto.Field(
        proto.MESSAGE,
        number=18,
        message="EvaluationConfig",
    )
    golden_run_method: golden_run.GoldenRunMethod = proto.Field(
        proto.ENUM,
        number=19,
        enum=golden_run.GoldenRunMethod,
    )


class EvaluationRun(proto.Message):
    r"""An evaluation run represents an all the evaluation results
    from an evaluation execution.

    Attributes:
        name (str):
            Identifier. The unique identifier of the evaluation run.
            Format:
            ``projects/{project}/locations/{location}/apps/{app}/evaluationRuns/{evaluationRun}``
        display_name (str):
            Optional. User-defined display name of the
            evaluation run. default:
            "<evaluation-dataset-display-name> run -
            <timestamp>".
        evaluation_results (MutableSequence[str]):
            Output only. The evaluation results that are part of this
            run. Format:
            ``projects/{project}/locations/{location}/apps/{app}/evaluations/{evaluation}/results/{result}``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the evaluation
            run was created.
        initiated_by (str):
            Output only. The user who initiated the
            evaluation run.
        app_version (str):
            Output only. The app version to evaluate. Format:
            ``projects/{project}/locations/{location}/apps/{app}/versions/{version}``
        app_version_display_name (str):
            Output only. The display name of the ``app_version`` that
            the evaluation ran against.
        changelog (str):
            Output only. The changelog of the app version
            that the evaluation ran against. This is
            populated if user runs evaluation on
            latest/draft.
        changelog_create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The create time of the changelog
            of the app version that the evaluation ran
            against. This is populated if user runs
            evaluation on latest/draft.
        evaluations (MutableSequence[str]):
            Output only. The evaluations that are part of this run. The
            list may contain evaluations of either type. This field is
            mutually exclusive with ``evaluation_dataset``. Format:
            ``projects/{project}/locations/{location}/apps/{app}/evaluations/{evaluation}``
        evaluation_dataset (str):
            Output only. The evaluation dataset that this run is
            associated with. This field is mutually exclusive with
            ``evaluations``. Format:
            ``projects/{project}/locations/{location}/apps/{app}/evaluationDatasets/{evaluationDataset}``
        evaluation_type (google.cloud.ces_v1beta.types.EvaluationRun.EvaluationType):
            Output only. The type of the evaluations in
            this run.
        state (google.cloud.ces_v1beta.types.EvaluationRun.EvaluationRunState):
            Output only. The state of the evaluation run.
        progress (google.cloud.ces_v1beta.types.EvaluationRun.Progress):
            Output only. The progress of the evaluation
            run.
        config (google.cloud.ces_v1beta.types.EvaluationConfig):
            Output only. The configuration used in the
            run.
        error (google.rpc.status_pb2.Status):
            Output only. Deprecated: Use error_info instead. Errors
            encountered during execution.
        error_info (google.cloud.ces_v1beta.types.EvaluationErrorInfo):
            Output only. Error information for the
            evaluation run.
        evaluation_run_summaries (MutableMapping[str, google.cloud.ces_v1beta.types.EvaluationRun.EvaluationRunSummary]):
            Output only. Map of evaluation name to
            EvaluationRunSummary.
        latency_report (google.cloud.ces_v1beta.types.LatencyReport):
            Output only. Latency report for the
            evaluation run.
        run_count (int):
            Output only. The number of times the
            evaluations inside the run were run.
        persona_run_configs (MutableSequence[google.cloud.ces_v1beta.types.PersonaRunConfig]):
            Output only. The configuration to use for the
            run per persona.
        optimization_config (google.cloud.ces_v1beta.types.OptimizationConfig):
            Optional. Configuration for running the
            optimization step after the evaluation run. If
            not set, the optimization step will not be run.
        scheduled_evaluation_run (str):
            Output only. The scheduled evaluation run resource name that
            created this evaluation run. This field is only set if the
            evaluation run was created by a scheduled evaluation run.
            Format:
            ``projects/{project}/locations/{location}/apps/{app}/scheduledEvaluationRuns/{scheduled_evaluation_run}``
        golden_run_method (google.cloud.ces_v1beta.types.GoldenRunMethod):
            Output only. The method used to run the
            evaluation.
        operation (str):
            Output only. The operation that created this evaluation run.
            Format:
            ``projects/{project}/locations/{location}/operations/{operation}``
    """

    class EvaluationType(proto.Enum):
        r"""The type of the evaluations in this run.
        Additional values may be added in the future.

        Values:
            EVALUATION_TYPE_UNSPECIFIED (0):
                Evaluation type is not specified.
            GOLDEN (1):
                Golden evaluation.
            SCENARIO (2):
                Scenario evaluation.
            MIXED (3):
                Indicates the run includes a mix of golden
                and scenario evaluations.
        """

        EVALUATION_TYPE_UNSPECIFIED = 0
        GOLDEN = 1
        SCENARIO = 2
        MIXED = 3

    class EvaluationRunState(proto.Enum):
        r"""The state of the evaluation run.

        Values:
            EVALUATION_RUN_STATE_UNSPECIFIED (0):
                Evaluation run state is not specified.
            QUEUED (5):
                Indicates the evaluation run is queued.
            RUNNING (1):
                Evaluation run is running.
            COMPLETED (2):
                Evaluation run has completed.
            ERROR (3):
                The evaluation run has an error.
            CANCELLED (4):
                Evaluation run was cancelled.
        """

        EVALUATION_RUN_STATE_UNSPECIFIED = 0
        QUEUED = 5
        RUNNING = 1
        COMPLETED = 2
        ERROR = 3
        CANCELLED = 4

    class Progress(proto.Message):
        r"""The progress of the evaluation run.

        Attributes:
            total_count (int):
                Output only. Total number of evaluation
                results in this run.
            failed_count (int):
                Output only. Number of completed evaluation results with an
                outcome of FAIL. (EvaluationResult.execution_state is
                COMPLETED and EvaluationResult.evaluation_status is FAIL).
            error_count (int):
                Output only. Number of evaluation results that failed to
                execute. (EvaluationResult.execution_state is ERROR).
            completed_count (int):
                Output only. Number of evaluation results that finished
                successfully. (EvaluationResult.execution_state is
                COMPLETED).
            passed_count (int):
                Output only. Number of completed evaluation results with an
                outcome of PASS. (EvaluationResult.execution_state is
                COMPLETED and EvaluationResult.evaluation_status is PASS).
            cancelled_count (int):
                Output only. Number of evaluation results that were
                cancelled. (EvaluationResult.execution_state is CANCELLED).
        """

        total_count: int = proto.Field(
            proto.INT32,
            number=1,
        )
        failed_count: int = proto.Field(
            proto.INT32,
            number=2,
        )
        error_count: int = proto.Field(
            proto.INT32,
            number=3,
        )
        completed_count: int = proto.Field(
            proto.INT32,
            number=4,
        )
        passed_count: int = proto.Field(
            proto.INT32,
            number=5,
        )
        cancelled_count: int = proto.Field(
            proto.INT32,
            number=6,
        )

    class EvaluationRunSummary(proto.Message):
        r"""Contains the summary of passed and failed result counts for a
        specific evaluation in an evaluation run.

        Attributes:
            passed_count (int):
                Output only. Number of passed results for the
                associated Evaluation in this run.
            failed_count (int):
                Output only. Number of failed results for the
                associated Evaluation in this run.
            error_count (int):
                Output only. Number of error results for the
                associated Evaluation in this run.
        """

        passed_count: int = proto.Field(
            proto.INT32,
            number=1,
        )
        failed_count: int = proto.Field(
            proto.INT32,
            number=2,
        )
        error_count: int = proto.Field(
            proto.INT32,
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
    evaluation_results: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    initiated_by: str = proto.Field(
        proto.STRING,
        number=5,
    )
    app_version: str = proto.Field(
        proto.STRING,
        number=6,
    )
    app_version_display_name: str = proto.Field(
        proto.STRING,
        number=13,
    )
    changelog: str = proto.Field(
        proto.STRING,
        number=22,
    )
    changelog_create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=23,
        message=timestamp_pb2.Timestamp,
    )
    evaluations: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    evaluation_dataset: str = proto.Field(
        proto.STRING,
        number=8,
    )
    evaluation_type: EvaluationType = proto.Field(
        proto.ENUM,
        number=9,
        enum=EvaluationType,
    )
    state: EvaluationRunState = proto.Field(
        proto.ENUM,
        number=10,
        enum=EvaluationRunState,
    )
    progress: Progress = proto.Field(
        proto.MESSAGE,
        number=11,
        message=Progress,
    )
    config: "EvaluationConfig" = proto.Field(
        proto.MESSAGE,
        number=12,
        message="EvaluationConfig",
    )
    error: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=14,
        message=status_pb2.Status,
    )
    error_info: "EvaluationErrorInfo" = proto.Field(
        proto.MESSAGE,
        number=17,
        message="EvaluationErrorInfo",
    )
    evaluation_run_summaries: MutableMapping[str, EvaluationRunSummary] = (
        proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=15,
            message=EvaluationRunSummary,
        )
    )
    latency_report: "LatencyReport" = proto.Field(
        proto.MESSAGE,
        number=25,
        message="LatencyReport",
    )
    run_count: int = proto.Field(
        proto.INT32,
        number=16,
    )
    persona_run_configs: MutableSequence["PersonaRunConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=18,
        message="PersonaRunConfig",
    )
    optimization_config: "OptimizationConfig" = proto.Field(
        proto.MESSAGE,
        number=19,
        message="OptimizationConfig",
    )
    scheduled_evaluation_run: str = proto.Field(
        proto.STRING,
        number=20,
    )
    golden_run_method: golden_run.GoldenRunMethod = proto.Field(
        proto.ENUM,
        number=21,
        enum=golden_run.GoldenRunMethod,
    )
    operation: str = proto.Field(
        proto.STRING,
        number=26,
    )


class LatencyReport(proto.Message):
    r"""Latency report for the evaluation run.

    Attributes:
        tool_latencies (MutableSequence[google.cloud.ces_v1beta.types.LatencyReport.ToolLatency]):
            Output only. Unordered list. Latency metrics
            for each tool.
        callback_latencies (MutableSequence[google.cloud.ces_v1beta.types.LatencyReport.CallbackLatency]):
            Output only. Unordered list. Latency metrics
            for each callback.
        guardrail_latencies (MutableSequence[google.cloud.ces_v1beta.types.LatencyReport.GuardrailLatency]):
            Output only. Unordered list. Latency metrics
            for each guardrail.
        llm_call_latencies (MutableSequence[google.cloud.ces_v1beta.types.LatencyReport.LlmCallLatency]):
            Output only. Unordered list. Latency metrics
            for each LLM call.
        session_count (int):
            Output only. The total number of sessions
            considered in the latency report.
    """

    class LatencyMetrics(proto.Message):
        r"""Latency metrics for a component.

        Attributes:
            p50_latency (google.protobuf.duration_pb2.Duration):
                Output only. The 50th percentile latency.
            p90_latency (google.protobuf.duration_pb2.Duration):
                Output only. The 90th percentile latency.
            p99_latency (google.protobuf.duration_pb2.Duration):
                Output only. The 99th percentile latency.
            call_count (int):
                Output only. The number of times the resource
                was called.
        """

        p50_latency: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=1,
            message=duration_pb2.Duration,
        )
        p90_latency: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=2,
            message=duration_pb2.Duration,
        )
        p99_latency: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=3,
            message=duration_pb2.Duration,
        )
        call_count: int = proto.Field(
            proto.INT32,
            number=4,
        )

    class ToolLatency(proto.Message):
        r"""Latency metrics for a single tool.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            tool (str):
                Output only. Format:
                ``projects/{project}/locations/{location}/apps/{app}/tools/{tool}``.

                This field is a member of `oneof`_ ``tool_identifier``.
            toolset_tool (google.cloud.ces_v1beta.types.ToolsetTool):
                Output only. The toolset tool identifier.

                This field is a member of `oneof`_ ``tool_identifier``.
            tool_display_name (str):
                Output only. The display name of the tool.
            latency_metrics (google.cloud.ces_v1beta.types.LatencyReport.LatencyMetrics):
                Output only. The latency metrics for the
                tool.
        """

        tool: str = proto.Field(
            proto.STRING,
            number=1,
            oneof="tool_identifier",
        )
        toolset_tool: gcc_toolset_tool.ToolsetTool = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="tool_identifier",
            message=gcc_toolset_tool.ToolsetTool,
        )
        tool_display_name: str = proto.Field(
            proto.STRING,
            number=3,
        )
        latency_metrics: "LatencyReport.LatencyMetrics" = proto.Field(
            proto.MESSAGE,
            number=4,
            message="LatencyReport.LatencyMetrics",
        )

    class CallbackLatency(proto.Message):
        r"""Latency metrics for a single callback.

        Attributes:
            stage (str):
                Output only. The stage of the callback.
            latency_metrics (google.cloud.ces_v1beta.types.LatencyReport.LatencyMetrics):
                Output only. The latency metrics for the
                callback.
        """

        stage: str = proto.Field(
            proto.STRING,
            number=1,
        )
        latency_metrics: "LatencyReport.LatencyMetrics" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="LatencyReport.LatencyMetrics",
        )

    class GuardrailLatency(proto.Message):
        r"""Latency metrics for a single guardrail.

        Attributes:
            guardrail (str):
                Output only. The name of the guardrail. Format:
                ``projects/{project}/locations/{location}/apps/{app}/guardrails/{guardrail}``.
            guardrail_display_name (str):
                Output only. The display name of the
                guardrail.
            latency_metrics (google.cloud.ces_v1beta.types.LatencyReport.LatencyMetrics):
                Output only. The latency metrics for the
                guardrail.
        """

        guardrail: str = proto.Field(
            proto.STRING,
            number=1,
        )
        guardrail_display_name: str = proto.Field(
            proto.STRING,
            number=2,
        )
        latency_metrics: "LatencyReport.LatencyMetrics" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="LatencyReport.LatencyMetrics",
        )

    class LlmCallLatency(proto.Message):
        r"""Latency metrics for a single LLM call.

        Attributes:
            model (str):
                Output only. The name of the model.
            latency_metrics (google.cloud.ces_v1beta.types.LatencyReport.LatencyMetrics):
                Output only. The latency metrics for the LLM
                call.
        """

        model: str = proto.Field(
            proto.STRING,
            number=1,
        )
        latency_metrics: "LatencyReport.LatencyMetrics" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="LatencyReport.LatencyMetrics",
        )

    tool_latencies: MutableSequence[ToolLatency] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=ToolLatency,
    )
    callback_latencies: MutableSequence[CallbackLatency] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=CallbackLatency,
    )
    guardrail_latencies: MutableSequence[GuardrailLatency] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=GuardrailLatency,
    )
    llm_call_latencies: MutableSequence[LlmCallLatency] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=LlmCallLatency,
    )
    session_count: int = proto.Field(
        proto.INT32,
        number=5,
    )


class EvaluationExpectation(proto.Message):
    r"""An evaluation expectation represents a specific criteria to
    evaluate against.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        llm_criteria (google.cloud.ces_v1beta.types.EvaluationExpectation.LlmCriteria):
            Optional. Evaluation criteria based on an LLM
            prompt.

            This field is a member of `oneof`_ ``criteria``.
        name (str):
            Identifier. The unique identifier of this evaluation
            expectation. Format:
            ``projects/{project}/locations/{location}/apps/{app}/evaluationExpectations/{evaluation_expectation}``
        display_name (str):
            Required. User-defined display name. Must be
            unique within the app.
        tags (MutableSequence[str]):
            Optional. User-defined tags for expectations.
            Can be used to filter expectations.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the evaluation
            expectation was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the evaluation
            expectation was last updated.
        etag (str):
            Output only. Etag used to ensure the object
            hasn't changed during a read-modify-write
            operation. If the etag is empty, the update will
            overwrite any concurrent changes.
    """

    class LlmCriteria(proto.Message):
        r"""Configuration for LLM-based evaluation criteria.

        Attributes:
            prompt (str):
                Required. The prompt/instructions provided to
                the LLM judge.
        """

        prompt: str = proto.Field(
            proto.STRING,
            number=1,
        )

    llm_criteria: LlmCriteria = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="criteria",
        message=LlmCriteria,
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=6,
    )


class EvaluationConfig(proto.Message):
    r"""EvaluationConfig configures settings for running the
    evaluation.

    Attributes:
        input_audio_config (google.cloud.ces_v1beta.types.InputAudioConfig):
            Optional. Configuration for processing the
            input audio.
        output_audio_config (google.cloud.ces_v1beta.types.OutputAudioConfig):
            Optional. Configuration for generating the
            output audio.
        evaluation_channel (google.cloud.ces_v1beta.types.EvaluationConfig.EvaluationChannel):
            Optional. The channel to evaluate.
        tool_call_behaviour (google.cloud.ces_v1beta.types.EvaluationToolCallBehaviour):
            Optional. Specifies whether the evaluation
            should use real tool calls or fake tools.
    """

    class EvaluationChannel(proto.Enum):
        r"""The channel to evaluate.

        Values:
            EVALUATION_CHANNEL_UNSPECIFIED (0):
                Unspecified evaluation channel.
            TEXT (1):
                Text-only evaluation channel.
            AUDIO (2):
                Audio evaluation channel.
        """

        EVALUATION_CHANNEL_UNSPECIFIED = 0
        TEXT = 1
        AUDIO = 2

    input_audio_config: session_service.InputAudioConfig = proto.Field(
        proto.MESSAGE,
        number=1,
        message=session_service.InputAudioConfig,
    )
    output_audio_config: session_service.OutputAudioConfig = proto.Field(
        proto.MESSAGE,
        number=2,
        message=session_service.OutputAudioConfig,
    )
    evaluation_channel: EvaluationChannel = proto.Field(
        proto.ENUM,
        number=3,
        enum=EvaluationChannel,
    )
    tool_call_behaviour: fakes.EvaluationToolCallBehaviour = proto.Field(
        proto.ENUM,
        number=4,
        enum=fakes.EvaluationToolCallBehaviour,
    )


class EvaluationErrorInfo(proto.Message):
    r"""Information about an error encountered during an evaluation
    execution.

    Attributes:
        error_type (google.cloud.ces_v1beta.types.EvaluationErrorInfo.ErrorType):
            Output only. The type of error.
        error_message (str):
            Output only. The error message.
        session_id (str):
            Output only. The session ID for the
            conversation that caused the error.
        user_facing_error_message (str):
            Output only. The user facing error message.
    """

    class ErrorType(proto.Enum):
        r"""The type of error

        Values:
            ERROR_TYPE_UNSPECIFIED (0):
                Unspecified error type.
            RUNTIME_FAILURE (1):
                Failure during runtime execution.
            CONVERSATION_RETRIEVAL_FAILURE (2):
                Failure to retrieve conversation from CES
                Runtime.
            METRIC_CALCULATION_FAILURE (3):
                Failure to calculate a metric / outcome.
            EVALUATION_UPDATE_FAILURE (4):
                Failure to update the evaluation.
            QUOTA_EXHAUSTED (5):
                Ran out of quota.
            USER_SIMULATION_FAILURE (6):
                Failure during user simulation.
        """

        ERROR_TYPE_UNSPECIFIED = 0
        RUNTIME_FAILURE = 1
        CONVERSATION_RETRIEVAL_FAILURE = 2
        METRIC_CALCULATION_FAILURE = 3
        EVALUATION_UPDATE_FAILURE = 4
        QUOTA_EXHAUSTED = 5
        USER_SIMULATION_FAILURE = 6

    error_type: ErrorType = proto.Field(
        proto.ENUM,
        number=1,
        enum=ErrorType,
    )
    error_message: str = proto.Field(
        proto.STRING,
        number=2,
    )
    session_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    user_facing_error_message: str = proto.Field(
        proto.STRING,
        number=4,
    )


class RunEvaluationRequest(proto.Message):
    r"""Request message for
    [EvaluationService.RunEvaluation][google.cloud.ces.v1beta.EvaluationService.RunEvaluation].


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        app (str):
            Required. The app to evaluate. Format:
            ``projects/{project}/locations/{location}/apps/{app}``
        evaluations (MutableSequence[str]):
            Optional. List of evaluations to run. Format:
            ``projects/{project}/locations/{location}/apps/{app}/evaluations/{evaluation}``
        evaluation_dataset (str):
            Optional. An evaluation dataset to run. Format:
            ``projects/{project}/locations/{location}/apps/{app}/evaluationDatasets/{evaluationDataset}``
        display_name (str):
            Optional. The display name of the evaluation
            run.
        app_version (str):
            Optional. The app version to evaluate. Format:
            ``projects/{project}/locations/{location}/apps/{app}/versions/{version}``
        config (google.cloud.ces_v1beta.types.EvaluationConfig):
            Optional. The configuration to use for the
            run.
        run_count (int):
            Optional. The number of times to run the
            evaluation. If not set, the default value is 1
            per golden, and 5 per scenario.

            This field is a member of `oneof`_ ``_run_count``.
        persona_run_configs (MutableSequence[google.cloud.ces_v1beta.types.PersonaRunConfig]):
            Optional. The configuration to use for the
            run per persona.
        optimization_config (google.cloud.ces_v1beta.types.OptimizationConfig):
            Optional. Configuration for running the
            optimization step after the evaluation run. If
            not set, the optimization step will not be run.
        scheduled_evaluation_run (str):
            Optional. The resource name of the
            ``ScheduledEvaluationRun`` that is triggering this
            evaluation run.

            If this field is set, the ``scheduled_evaluation_run`` field
            on the created ``EvaluationRun`` resource will be populated
            from this value. Format:
            ``projects/{project}/locations/{location}/apps/{app}/scheduledEvaluationRuns/{scheduled_evaluation_run}``
        golden_run_method (google.cloud.ces_v1beta.types.GoldenRunMethod):
            Optional. The method to run the evaluation if
            it is a golden evaluation. If not set, default
            to STABLE.
        generate_latency_report (bool):
            Optional. Whether to generate a latency
            report for the evaluation run.
        evaluation_run_caching_settings (google.cloud.ces_v1beta.types.EvaluationRunCachingSettings):
            Optional. The caching settings to use for the
            evaluation run.
    """

    app: str = proto.Field(
        proto.STRING,
        number=1,
    )
    evaluations: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    evaluation_dataset: str = proto.Field(
        proto.STRING,
        number=3,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    app_version: str = proto.Field(
        proto.STRING,
        number=6,
    )
    config: "EvaluationConfig" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="EvaluationConfig",
    )
    run_count: int = proto.Field(
        proto.INT32,
        number=9,
        optional=True,
    )
    persona_run_configs: MutableSequence["PersonaRunConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message="PersonaRunConfig",
    )
    optimization_config: "OptimizationConfig" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="OptimizationConfig",
    )
    scheduled_evaluation_run: str = proto.Field(
        proto.STRING,
        number=12,
    )
    golden_run_method: golden_run.GoldenRunMethod = proto.Field(
        proto.ENUM,
        number=13,
        enum=golden_run.GoldenRunMethod,
    )
    generate_latency_report: bool = proto.Field(
        proto.BOOL,
        number=14,
    )
    evaluation_run_caching_settings: common.EvaluationRunCachingSettings = proto.Field(
        proto.MESSAGE,
        number=15,
        message=common.EvaluationRunCachingSettings,
    )


class ScheduledEvaluationRun(proto.Message):
    r"""Represents a scheduled evaluation run configuration.

    Attributes:
        name (str):
            Identifier. The unique identifier of the
            scheduled evaluation run config. Format:

            projects/{projectId}/locations/{locationId}/apps/{appId}/scheduledEvaluationRuns/{scheduledEvaluationRunId}
        display_name (str):
            Required. User-defined display name of the
            scheduled evaluation run config.
        request (google.cloud.ces_v1beta.types.RunEvaluationRequest):
            Required. The RunEvaluationRequest to
            schedule
        description (str):
            Optional. User-defined description of the
            scheduled evaluation run.
        scheduling_config (google.cloud.ces_v1beta.types.ScheduledEvaluationRun.SchedulingConfig):
            Required. Configuration for the timing and
            frequency with which to execute the evaluations.
        active (bool):
            Optional. Whether this config is active
        last_completed_run (str):
            Output only. The last successful EvaluationRun of this
            scheduled execution. Format:
            ``projects/{project}/locations/{location}/apps/{app}/evaluationRuns/{evaluationRun}``
        total_executions (int):
            Output only. The total number of times this
            run has been executed
        next_scheduled_execution_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The next time this is scheduled
            to execute
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the scheduled
            evaluation run was created.
        created_by (str):
            Output only. The user who created the
            scheduled evaluation run.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the evaluation
            was last updated.
        last_updated_by (str):
            Output only. The user who last updated the
            evaluation.
        etag (str):
            Output only. Etag used to ensure the object
            hasn't changed during a read-modify-write
            operation. If the etag is empty, the update will
            overwrite any concurrent changes.
    """

    class SchedulingConfig(proto.Message):
        r"""Eval scheduling configuration details

        Attributes:
            frequency (google.cloud.ces_v1beta.types.ScheduledEvaluationRun.SchedulingConfig.Frequency):
                Required. The frequency with which to run the
                eval
            start_time (google.protobuf.timestamp_pb2.Timestamp):
                Required. Timestamp when the eval should
                start.
            days_of_week (MutableSequence[int]):
                Optional. The days of the week to run the
                eval. Applicable only for Weekly and Biweekly
                frequencies. 1 is Monday, 2 is Tuesday, ..., 7
                is Sunday.
        """

        class Frequency(proto.Enum):
            r"""The frequencies evals can be run at

            Values:
                FREQUENCY_UNSPECIFIED (0):
                    The frequency is unspecified.
                NONE (1):
                    Indicates a one-time scheduled run that
                    should not repeat
                DAILY (2):
                    Run the evaluation daily.
                WEEKLY (3):
                    Run the evaluation weekly.
                BIWEEKLY (4):
                    Run the evaluation biweekly.
            """

            FREQUENCY_UNSPECIFIED = 0
            NONE = 1
            DAILY = 2
            WEEKLY = 3
            BIWEEKLY = 4

        frequency: "ScheduledEvaluationRun.SchedulingConfig.Frequency" = proto.Field(
            proto.ENUM,
            number=1,
            enum="ScheduledEvaluationRun.SchedulingConfig.Frequency",
        )
        start_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=2,
            message=timestamp_pb2.Timestamp,
        )
        days_of_week: MutableSequence[int] = proto.RepeatedField(
            proto.INT32,
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
    request: "RunEvaluationRequest" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="RunEvaluationRequest",
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
    )
    scheduling_config: SchedulingConfig = proto.Field(
        proto.MESSAGE,
        number=5,
        message=SchedulingConfig,
    )
    active: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    last_completed_run: str = proto.Field(
        proto.STRING,
        number=7,
    )
    total_executions: int = proto.Field(
        proto.INT32,
        number=8,
    )
    next_scheduled_execution_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    created_by: str = proto.Field(
        proto.STRING,
        number=11,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=12,
        message=timestamp_pb2.Timestamp,
    )
    last_updated_by: str = proto.Field(
        proto.STRING,
        number=13,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=14,
    )


class PersonaRunConfig(proto.Message):
    r"""Configuration for running an evaluation for a specific
    persona.

    Attributes:
        persona (str):
            Optional. The persona to use for the evaluation. Format:
            ``projects/{project}/locations/{location}/apps/{app}/evaluationPersonas/{evaluationPersona}``
        task_count (int):
            Optional. The number of tasks to run for the
            persona.
    """

    persona: str = proto.Field(
        proto.STRING,
        number=1,
    )
    task_count: int = proto.Field(
        proto.INT32,
        number=2,
    )


class OptimizationConfig(proto.Message):
    r"""Configuration for running the optimization step after the
    evaluation run.

    Attributes:
        generate_loss_report (bool):
            Optional. Whether to generate a loss report.
        assistant_session (str):
            Output only. The assistant session to use for the
            optimization based on this evaluation run. Format:
            ``projects/{project}/locations/{location}/apps/{app}/assistantSessions/{assistantSession}``
        report_summary (str):
            Output only. The summary of the loss report.
        should_suggest_fix (bool):
            Output only. Whether to suggest a fix for the
            losses.
        status (google.cloud.ces_v1beta.types.OptimizationConfig.OptimizationStatus):
            Output only. The status of the optimization
            run.
        error_message (str):
            Output only. The error message if the
            optimization run failed.
        loss_report (google.protobuf.struct_pb2.Struct):
            Output only. The generated loss report.
    """

    class OptimizationStatus(proto.Enum):
        r"""The status of the optimization run.

        Values:
            OPTIMIZATION_STATUS_UNSPECIFIED (0):
                Optimization status is not specified.
            RUNNING (1):
                Optimization is running.
            COMPLETED (2):
                Optimization has completed.
            ERROR (3):
                Optimization failed due to an internal error.
        """

        OPTIMIZATION_STATUS_UNSPECIFIED = 0
        RUNNING = 1
        COMPLETED = 2
        ERROR = 3

    generate_loss_report: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    assistant_session: str = proto.Field(
        proto.STRING,
        number=2,
    )
    report_summary: str = proto.Field(
        proto.STRING,
        number=3,
    )
    should_suggest_fix: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    status: OptimizationStatus = proto.Field(
        proto.ENUM,
        number=4,
        enum=OptimizationStatus,
    )
    error_message: str = proto.Field(
        proto.STRING,
        number=6,
    )
    loss_report: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=7,
        message=struct_pb2.Struct,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
