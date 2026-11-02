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

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.cx.v3beta1",
    manifest={
        "Experiment",
        "VersionVariants",
        "RolloutConfig",
        "RolloutState",
        "VariantsHistory",
        "ListExperimentsRequest",
        "ListExperimentsResponse",
        "GetExperimentRequest",
        "CreateExperimentRequest",
        "UpdateExperimentRequest",
        "DeleteExperimentRequest",
        "StartExperimentRequest",
        "StopExperimentRequest",
    },
)


class Experiment(proto.Message):
    r"""Represents an experiment in an environment.

    Attributes:
        name (str):
            The name of the experiment.
            Format:

            projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>/experiments/<ExperimentID>.
        display_name (str):
            Required. The human-readable name of the
            experiment (unique in an environment). Limit of
            64 characters.
        description (str):
            The human-readable description of the
            experiment.
        state (google.cloud.dialogflowcx_v3beta1.types.Experiment.State):
            The current state of the experiment.
            Transition triggered by
            Experiments.StartExperiment: DRAFT->RUNNING.
            Transition triggered by
            Experiments.CancelExperiment: DRAFT->DONE or
            RUNNING->DONE.
        definition (google.cloud.dialogflowcx_v3beta1.types.Experiment.Definition):
            The definition of the experiment.
        rollout_config (google.cloud.dialogflowcx_v3beta1.types.RolloutConfig):
            The configuration for auto rollout. If set,
            there should be exactly two variants in the
            experiment (control variant being the default
            version of the flow), the traffic allocation for
            the non-control variant will gradually increase
            to 100% when conditions are met, and eventually
            replace the control variant to become the
            default version of the flow.
        rollout_state (google.cloud.dialogflowcx_v3beta1.types.RolloutState):
            State of the auto rollout process.
        rollout_failure_reason (str):
            The reason why rollout has failed. Should only be set when
            state is ROLLOUT_FAILED.
        result (google.cloud.dialogflowcx_v3beta1.types.Experiment.Result):
            Inference result of the experiment.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Creation time of this experiment.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Start time of this experiment.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            End time of this experiment.
        last_update_time (google.protobuf.timestamp_pb2.Timestamp):
            Last update time of this experiment.
        experiment_length (google.protobuf.duration_pb2.Duration):
            Maximum number of days to run the experiment.
            If auto-rollout is not enabled, default value
            and maximum will be 30 days. If auto-rollout is
            enabled, default value and maximum will be 6
            days.
        variants_history (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.VariantsHistory]):
            The history of updates to the experiment
            variants.
    """

    class State(proto.Enum):
        r"""The state of the experiment.

        Values:
            STATE_UNSPECIFIED (0):
                State unspecified.
            DRAFT (1):
                The experiment is created but not started
                yet.
            RUNNING (2):
                The experiment is running.
            DONE (3):
                The experiment is done.
            ROLLOUT_FAILED (4):
                The experiment with auto-rollout enabled has
                failed.
        """

        STATE_UNSPECIFIED = 0
        DRAFT = 1
        RUNNING = 2
        DONE = 3
        ROLLOUT_FAILED = 4

    class Definition(proto.Message):
        r"""Definition of the experiment.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            condition (str):
                The condition defines which subset of sessions are selected
                for this experiment. If not specified, all sessions are
                eligible. E.g. "query_input.language_code=en" See the
                `conditions
                reference <https://cloud.google.com/dialogflow/cx/docs/reference/condition>`__.
            version_variants (google.cloud.dialogflowcx_v3beta1.types.VersionVariants):
                The flow versions as the variants of this
                experiment.

                This field is a member of `oneof`_ ``variants``.
        """

        condition: str = proto.Field(
            proto.STRING,
            number=1,
        )
        version_variants: "VersionVariants" = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="variants",
            message="VersionVariants",
        )

    class Result(proto.Message):
        r"""The inference result which includes an objective metric to
        optimize and the confidence interval.

        Attributes:
            version_metrics (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.Experiment.Result.VersionMetrics]):
                Version variants and metrics.
            last_update_time (google.protobuf.timestamp_pb2.Timestamp):
                The last time the experiment's stats data was
                updated. Will have default value if stats have
                never been computed for this experiment.
        """

        class MetricType(proto.Enum):
            r"""Types of ratio-based metric for Dialogflow experiment.

            Values:
                METRIC_UNSPECIFIED (0):
                    Metric unspecified.
                CONTAINED_SESSION_NO_CALLBACK_RATE (1):
                    Percentage of contained sessions without user
                    calling back in 24 hours.
                LIVE_AGENT_HANDOFF_RATE (2):
                    Percentage of sessions that were handed to a
                    human agent.
                CALLBACK_SESSION_RATE (3):
                    Percentage of sessions with the same user
                    calling back.
                ABANDONED_SESSION_RATE (4):
                    Percentage of sessions where user hung up.
                SESSION_END_RATE (5):
                    Percentage of sessions reached Dialogflow 'END_PAGE' or
                    'END_SESSION'.
            """

            METRIC_UNSPECIFIED = 0
            CONTAINED_SESSION_NO_CALLBACK_RATE = 1
            LIVE_AGENT_HANDOFF_RATE = 2
            CALLBACK_SESSION_RATE = 3
            ABANDONED_SESSION_RATE = 4
            SESSION_END_RATE = 5

        class CountType(proto.Enum):
            r"""types of count-based metric for Dialogflow experiment.

            Values:
                COUNT_TYPE_UNSPECIFIED (0):
                    Count type unspecified.
                TOTAL_NO_MATCH_COUNT (1):
                    Total number of occurrences of a 'NO_MATCH'.
                TOTAL_TURN_COUNT (2):
                    Total number of turn counts.
                AVERAGE_TURN_COUNT (3):
                    Average turn count in a session.
            """

            COUNT_TYPE_UNSPECIFIED = 0
            TOTAL_NO_MATCH_COUNT = 1
            TOTAL_TURN_COUNT = 2
            AVERAGE_TURN_COUNT = 3

        class ConfidenceInterval(proto.Message):
            r"""A confidence interval is a range of possible values for the
            experiment objective you are trying to measure.

            Attributes:
                confidence_level (float):
                    The confidence level used to construct the
                    interval, i.e. there is X% chance that the true
                    value is within this interval.
                ratio (float):
                    The percent change between an experiment
                    metric's value and the value for its control.
                lower_bound (float):
                    Lower bound of the interval.
                upper_bound (float):
                    Upper bound of the interval.
            """

            confidence_level: float = proto.Field(
                proto.DOUBLE,
                number=1,
            )
            ratio: float = proto.Field(
                proto.DOUBLE,
                number=2,
            )
            lower_bound: float = proto.Field(
                proto.DOUBLE,
                number=3,
            )
            upper_bound: float = proto.Field(
                proto.DOUBLE,
                number=4,
            )

        class Metric(proto.Message):
            r"""Metric and corresponding confidence intervals.

            This message has `oneof`_ fields (mutually exclusive fields).
            For each oneof, at most one member field can be set at the same time.
            Setting any member of the oneof automatically clears all other
            members.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                type_ (google.cloud.dialogflowcx_v3beta1.types.Experiment.Result.MetricType):
                    Ratio-based metric type. Only one of type or count_type is
                    specified in each Metric.
                count_type (google.cloud.dialogflowcx_v3beta1.types.Experiment.Result.CountType):
                    Count-based metric type. Only one of type or count_type is
                    specified in each Metric.
                ratio (float):
                    Ratio value of a metric.

                    This field is a member of `oneof`_ ``value``.
                count (float):
                    Count value of a metric.

                    This field is a member of `oneof`_ ``value``.
                confidence_interval (google.cloud.dialogflowcx_v3beta1.types.Experiment.Result.ConfidenceInterval):
                    The probability that the treatment is better
                    than all other treatments in the experiment
            """

            type_: "Experiment.Result.MetricType" = proto.Field(
                proto.ENUM,
                number=1,
                enum="Experiment.Result.MetricType",
            )
            count_type: "Experiment.Result.CountType" = proto.Field(
                proto.ENUM,
                number=5,
                enum="Experiment.Result.CountType",
            )
            ratio: float = proto.Field(
                proto.DOUBLE,
                number=2,
                oneof="value",
            )
            count: float = proto.Field(
                proto.DOUBLE,
                number=4,
                oneof="value",
            )
            confidence_interval: "Experiment.Result.ConfidenceInterval" = proto.Field(
                proto.MESSAGE,
                number=3,
                message="Experiment.Result.ConfidenceInterval",
            )

        class VersionMetrics(proto.Message):
            r"""Version variant and associated metrics.

            Attributes:
                version (str):
                    The name of the flow
                    [Version][google.cloud.dialogflow.cx.v3beta1.Version].
                    Format:
                    ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/versions/<VersionID>``.
                metrics (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.Experiment.Result.Metric]):
                    The metrics and corresponding confidence
                    intervals in the inference result.
                session_count (int):
                    Number of sessions that were allocated to
                    this version.
            """

            version: str = proto.Field(
                proto.STRING,
                number=1,
            )
            metrics: MutableSequence["Experiment.Result.Metric"] = proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message="Experiment.Result.Metric",
            )
            session_count: int = proto.Field(
                proto.INT32,
                number=3,
            )

        version_metrics: MutableSequence["Experiment.Result.VersionMetrics"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=1,
                message="Experiment.Result.VersionMetrics",
            )
        )
        last_update_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=2,
            message=timestamp_pb2.Timestamp,
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
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )
    definition: Definition = proto.Field(
        proto.MESSAGE,
        number=5,
        message=Definition,
    )
    rollout_config: "RolloutConfig" = proto.Field(
        proto.MESSAGE,
        number=14,
        message="RolloutConfig",
    )
    rollout_state: "RolloutState" = proto.Field(
        proto.MESSAGE,
        number=15,
        message="RolloutState",
    )
    rollout_failure_reason: str = proto.Field(
        proto.STRING,
        number=16,
    )
    result: Result = proto.Field(
        proto.MESSAGE,
        number=6,
        message=Result,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    last_update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    experiment_length: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=11,
        message=duration_pb2.Duration,
    )
    variants_history: MutableSequence["VariantsHistory"] = proto.RepeatedField(
        proto.MESSAGE,
        number=12,
        message="VariantsHistory",
    )


class VersionVariants(proto.Message):
    r"""A list of flow version variants.

    Attributes:
        variants (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.VersionVariants.Variant]):
            A list of flow version variants.
    """

    class Variant(proto.Message):
        r"""A single flow version with specified traffic allocation.

        Attributes:
            version (str):
                The name of the flow version. Format:
                ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/versions/<VersionID>``.
            traffic_allocation (float):
                Percentage of the traffic which should be
                routed to this version of flow. Traffic
                allocation for a single flow must sum up to 1.0.
            is_control_group (bool):
                Whether the variant is for the control group.
        """

        version: str = proto.Field(
            proto.STRING,
            number=1,
        )
        traffic_allocation: float = proto.Field(
            proto.FLOAT,
            number=2,
        )
        is_control_group: bool = proto.Field(
            proto.BOOL,
            number=3,
        )

    variants: MutableSequence[Variant] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=Variant,
    )


class RolloutConfig(proto.Message):
    r"""The configuration for auto rollout.

    Attributes:
        rollout_steps (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.RolloutConfig.RolloutStep]):
            Steps to roll out a flow version. Steps
            should be sorted by percentage in ascending
            order.
        rollout_condition (str):
            The conditions that are used to evaluate the success of a
            rollout step. If not specified, all rollout steps will
            proceed to the next one unless failure conditions are met.
            E.g. "containment_rate > 60% AND callback_rate < 20%". See
            the `conditions
            reference <https://cloud.google.com/dialogflow/cx/docs/reference/condition>`__.
        failure_condition (str):
            The conditions that are used to evaluate the failure of a
            rollout step. If not specified, no rollout steps will fail.
            E.g. "containment_rate < 10% OR average_turn_count < 3". See
            the `conditions
            reference <https://cloud.google.com/dialogflow/cx/docs/reference/condition>`__.
    """

    class RolloutStep(proto.Message):
        r"""A single rollout step with specified traffic allocation.

        Attributes:
            display_name (str):
                The name of the rollout step;
            traffic_percent (int):
                The percentage of traffic allocated to the flow version of
                this rollout step. (0%, 100%].
            min_duration (google.protobuf.duration_pb2.Duration):
                The minimum time that this step should last.
                Should be longer than 1 hour. If not set, the
                default minimum duration for each step will be 1
                hour.
        """

        display_name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        traffic_percent: int = proto.Field(
            proto.INT32,
            number=2,
        )
        min_duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=3,
            message=duration_pb2.Duration,
        )

    rollout_steps: MutableSequence[RolloutStep] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=RolloutStep,
    )
    rollout_condition: str = proto.Field(
        proto.STRING,
        number=2,
    )
    failure_condition: str = proto.Field(
        proto.STRING,
        number=3,
    )


class RolloutState(proto.Message):
    r"""State of the auto-rollout process.

    Attributes:
        step (str):
            Display name of the current auto rollout
            step.
        step_index (int):
            Index of the current step in the auto rollout
            steps list.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Start time of the current step.
    """

    step: str = proto.Field(
        proto.STRING,
        number=1,
    )
    step_index: int = proto.Field(
        proto.INT32,
        number=3,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


class VariantsHistory(proto.Message):
    r"""The history of variants update.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        version_variants (google.cloud.dialogflowcx_v3beta1.types.VersionVariants):
            The flow versions as the variants.

            This field is a member of `oneof`_ ``variants``.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Update time of the variants.
    """

    version_variants: "VersionVariants" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="variants",
        message="VersionVariants",
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


class ListExperimentsRequest(proto.Message):
    r"""The request message for
    [Experiments.ListExperiments][google.cloud.dialogflow.cx.v3beta1.Experiments.ListExperiments].

    Attributes:
        parent (str):
            Required. The
            [Environment][google.cloud.dialogflow.cx.v3beta1.Environment]
            to list all environments for. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>``.
        page_size (int):
            The maximum number of items to return in a
            single page. By default 20 and at most 100.
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


class ListExperimentsResponse(proto.Message):
    r"""The response message for
    [Experiments.ListExperiments][google.cloud.dialogflow.cx.v3beta1.Experiments.ListExperiments].

    Attributes:
        experiments (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.Experiment]):
            The list of experiments. There will be a maximum number of
            items returned based on the page_size field in the request.
            The list may in some cases be empty or contain fewer entries
            than page_size even if this isn't the last page.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    experiments: MutableSequence["Experiment"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Experiment",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetExperimentRequest(proto.Message):
    r"""The request message for
    [Experiments.GetExperiment][google.cloud.dialogflow.cx.v3beta1.Experiments.GetExperiment].

    Attributes:
        name (str):
            Required. The name of the
            [Environment][google.cloud.dialogflow.cx.v3beta1.Environment].
            Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>/experiments/<ExperimentID>``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateExperimentRequest(proto.Message):
    r"""The request message for
    [Experiments.CreateExperiment][google.cloud.dialogflow.cx.v3beta1.Experiments.CreateExperiment].

    Attributes:
        parent (str):
            Required. The
            [Agent][google.cloud.dialogflow.cx.v3beta1.Agent] to create
            an
            [Environment][google.cloud.dialogflow.cx.v3beta1.Environment]
            for. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>``.
        experiment (google.cloud.dialogflowcx_v3beta1.types.Experiment):
            Required. The experiment to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    experiment: "Experiment" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Experiment",
    )


class UpdateExperimentRequest(proto.Message):
    r"""The request message for
    [Experiments.UpdateExperiment][google.cloud.dialogflow.cx.v3beta1.Experiments.UpdateExperiment].

    Attributes:
        experiment (google.cloud.dialogflowcx_v3beta1.types.Experiment):
            Required. The experiment to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The mask to control which fields
            get updated.
    """

    experiment: "Experiment" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Experiment",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteExperimentRequest(proto.Message):
    r"""The request message for
    [Experiments.DeleteExperiment][google.cloud.dialogflow.cx.v3beta1.Experiments.DeleteExperiment].

    Attributes:
        name (str):
            Required. The name of the
            [Environment][google.cloud.dialogflow.cx.v3beta1.Environment]
            to delete. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>/experiments/<ExperimentID>``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class StartExperimentRequest(proto.Message):
    r"""The request message for
    [Experiments.StartExperiment][google.cloud.dialogflow.cx.v3beta1.Experiments.StartExperiment].

    Attributes:
        name (str):
            Required. Resource name of the experiment to start. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>/experiments/<ExperimentID>``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class StopExperimentRequest(proto.Message):
    r"""The request message for
    [Experiments.StopExperiment][google.cloud.dialogflow.cx.v3beta1.Experiments.StopExperiment].

    Attributes:
        name (str):
            Required. Resource name of the experiment to stop. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>/experiments/<ExperimentID>``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
