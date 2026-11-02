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

import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.ces.v1beta",
    manifest={
        "EvaluationMetricsConfig",
    },
)


class EvaluationMetricsConfig(proto.Message):
    r"""Configures the metrics for an evaluation.

    Attributes:
        golden_metrics_config (google.cloud.ces_v1beta.types.EvaluationMetricsConfig.GoldenMetricsConfig):
            Optional. Configuration for the golden
            metrics for the evaluation.
        scenario_metrics_config (google.cloud.ces_v1beta.types.EvaluationMetricsConfig.ScenarioMetricsConfig):
            Optional. Configuration for the scenario
            metrics for the evaluation.
    """

    class ComparisonType(proto.Enum):
        r"""Supported comparison types for checking the agent's response.

        Values:
            COMPARISON_TYPE_UNSPECIFIED (0):
                Unspecified comparison type. Behavior defaults to
                SEMANTIC_SIMILARITY for agent responses and tool calls.
            EQUALS (1):
                Exact string match.
            CONTAINS (2):
                Substring match (checks if the expected
                string is contained in the actual response).
            SEMANTIC_SIMILARITY (3):
                Semantic similarity match (evaluates meaning
                similarity using an LLM).
        """

        COMPARISON_TYPE_UNSPECIFIED = 0
        EQUALS = 1
        CONTAINS = 2
        SEMANTIC_SIMILARITY = 3

    class SemanticSimilarityMetricsConfig(proto.Message):
        r"""Configuration for similarity metrics for the evaluation. To disable
        the metric, set the message but do not set the
        ``enable_semantic_similarity_metrics`` field to true (or explicitly
        set it to false). To unset the configuration and fallback to the
        default behavior, omit the message entirely.

        Attributes:
            enable_semantic_similarity_metrics (bool):
                Optional. Whether to calculate semantic
                similarity metrics for the evaluation.
        """

        enable_semantic_similarity_metrics: bool = proto.Field(
            proto.BOOL,
            number=1,
        )

    class ToolCorrectnessMetricsConfig(proto.Message):
        r"""Configuration for correctness metrics for the evaluation. To disable
        the metric, set the message but do not set the
        ``enable_tool_correctness_metrics`` field to true (or explicitly set
        it to false). To unset the configuration and fallback to the default
        behavior, omit the message entirely.

        Attributes:
            enable_tool_correctness_metrics (bool):
                Optional. Whether to calculate tool
                correctness metrics for the evaluation.
        """

        enable_tool_correctness_metrics: bool = proto.Field(
            proto.BOOL,
            number=1,
        )

    class HallucinationMetricsConfig(proto.Message):
        r"""Configuration for the hallucination metrics for the evaluation. To
        disable the metric, set the message but do not set the
        ``enable_hallucination_metrics`` field to true (or explicitly set it
        to false). To unset the configuration and fallback to the default
        behavior, omit the message entirely.

        Attributes:
            enable_hallucination_metrics (bool):
                Optional. Whether to calculate hallucination
                metrics for the evaluation.
        """

        enable_hallucination_metrics: bool = proto.Field(
            proto.BOOL,
            number=1,
        )

    class UserGoalMetMetricsConfig(proto.Message):
        r"""Configuration for the user goal met metrics for the evaluation. To
        disable the metric, set the message but do not set the
        ``enable_user_goal_met_metrics`` field to true (or explicitly set it
        to false). To unset the configuration and fallback to the default
        behavior, omit the message entirely.

        Attributes:
            enable_user_goal_met_metrics (bool):
                Optional. Whether to calculate the user goal
                met metrics for the evaluation.
        """

        enable_user_goal_met_metrics: bool = proto.Field(
            proto.BOOL,
            number=1,
        )

    class ExpectationsMetMetricsConfig(proto.Message):
        r"""Configuration for the expectation level metrics for the evaluation.
        To disable the metric, set the message but do not set the
        ``enable_expectations_met_metrics`` field to true (or explicitly set
        it to false). To unset the configuration and fallback to the default
        behavior, omit the message entirely.

        Attributes:
            enable_expectations_met_metrics (bool):
                Optional. Whether to calculate the
                expectation level metrics for the evaluation.
        """

        enable_expectations_met_metrics: bool = proto.Field(
            proto.BOOL,
            number=1,
        )

    class GoldenMetricsConfig(proto.Message):
        r"""Configuration for the golden metrics for the evaluation.

        Attributes:
            semantic_similarity_metrics_config (google.cloud.ces_v1beta.types.EvaluationMetricsConfig.SemanticSimilarityMetricsConfig):
                Optional. Global configuration for semantic
                similarity metrics.
            tool_correctness_metrics_config (google.cloud.ces_v1beta.types.EvaluationMetricsConfig.ToolCorrectnessMetricsConfig):
                Optional. Configuration for turn level tool
                correctness metrics.
            step_tool_correctness_metrics_config (google.cloud.ces_v1beta.types.EvaluationMetricsConfig.ToolCorrectnessMetricsConfig):
                Optional. Configuration for step level tool
                correctness metrics.
        """

        semantic_similarity_metrics_config: "EvaluationMetricsConfig.SemanticSimilarityMetricsConfig" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="EvaluationMetricsConfig.SemanticSimilarityMetricsConfig",
        )
        tool_correctness_metrics_config: "EvaluationMetricsConfig.ToolCorrectnessMetricsConfig" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="EvaluationMetricsConfig.ToolCorrectnessMetricsConfig",
        )
        step_tool_correctness_metrics_config: "EvaluationMetricsConfig.ToolCorrectnessMetricsConfig" = proto.Field(
            proto.MESSAGE,
            number=6,
            message="EvaluationMetricsConfig.ToolCorrectnessMetricsConfig",
        )

    class ScenarioMetricsConfig(proto.Message):
        r"""Configuration for the scenario metrics for the evaluation.

        Attributes:
            user_goal_met_metrics_config (google.cloud.ces_v1beta.types.EvaluationMetricsConfig.UserGoalMetMetricsConfig):
                Optional. Configuration for user goal met
                metrics.
            expectations_met_metrics_config (google.cloud.ces_v1beta.types.EvaluationMetricsConfig.ExpectationsMetMetricsConfig):
                Optional. Configuration for expectation level
                metrics.
        """

        user_goal_met_metrics_config: "EvaluationMetricsConfig.UserGoalMetMetricsConfig" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="EvaluationMetricsConfig.UserGoalMetMetricsConfig",
        )
        expectations_met_metrics_config: "EvaluationMetricsConfig.ExpectationsMetMetricsConfig" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="EvaluationMetricsConfig.ExpectationsMetMetricsConfig",
        )

    golden_metrics_config: GoldenMetricsConfig = proto.Field(
        proto.MESSAGE,
        number=1,
        message=GoldenMetricsConfig,
    )
    scenario_metrics_config: ScenarioMetricsConfig = proto.Field(
        proto.MESSAGE,
        number=2,
        message=ScenarioMetricsConfig,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
