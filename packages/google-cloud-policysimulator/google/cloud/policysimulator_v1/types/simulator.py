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

import google.iam.v1.policy_pb2 as policy_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.rpc.status_pb2 as status_pb2  # type: ignore
import google.type.date_pb2 as date_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.policysimulator_v1.types import explanations

__protobuf__ = proto.module(
    package="google.cloud.policysimulator.v1",
    manifest={
        "Replay",
        "ReplayResult",
        "CreateReplayRequest",
        "ReplayOperationMetadata",
        "GetReplayRequest",
        "ListReplayResultsRequest",
        "ListReplayResultsResponse",
        "ReplayConfig",
        "ReplayDiff",
        "AccessStateDiff",
        "ExplainedAccess",
    },
)


class Replay(proto.Message):
    r"""A resource describing a ``Replay``, or simulation.

    Attributes:
        name (str):
            Output only. The resource name of the ``Replay``, which has
            the following format:

            ``{projects|folders|organizations}/{resource-id}/locations/global/replays/{replay-id}``,
            where ``{resource-id}`` is the ID of the project, folder, or
            organization that owns the Replay.

            Example:
            ``projects/my-example-project/locations/global/replays/506a5f7f-38ce-4d7d-8e03-479ce1833c36``
        state (google.cloud.policysimulator_v1.types.Replay.State):
            Output only. The current state of the ``Replay``.
        config (google.cloud.policysimulator_v1.types.ReplayConfig):
            Required. The configuration used for the ``Replay``.
        results_summary (google.cloud.policysimulator_v1.types.Replay.ResultsSummary):
            Output only. Summary statistics about the
            replayed log entries.
    """

    class State(proto.Enum):
        r"""The current state of the
        [Replay][google.cloud.policysimulator.v1.Replay].

        Values:
            STATE_UNSPECIFIED (0):
                Default value. This value is unused.
            PENDING (1):
                The ``Replay`` has not started yet.
            RUNNING (2):
                The ``Replay`` is currently running.
            SUCCEEDED (3):
                The ``Replay`` has successfully completed.
            FAILED (4):
                The ``Replay`` has finished with an error.
        """

        STATE_UNSPECIFIED = 0
        PENDING = 1
        RUNNING = 2
        SUCCEEDED = 3
        FAILED = 4

    class ResultsSummary(proto.Message):
        r"""Summary statistics about the replayed log entries.

        Attributes:
            log_count (int):
                The total number of log entries replayed.
            unchanged_count (int):
                The number of replayed log entries with no
                difference between baseline and simulated
                policies.
            difference_count (int):
                The number of replayed log entries with a
                difference between baseline and simulated
                policies.
            error_count (int):
                The number of log entries that could not be
                replayed.
            oldest_date (google.type.date_pb2.Date):
                The date of the oldest log entry replayed.
            newest_date (google.type.date_pb2.Date):
                The date of the newest log entry replayed.
        """

        log_count: int = proto.Field(
            proto.INT32,
            number=1,
        )
        unchanged_count: int = proto.Field(
            proto.INT32,
            number=2,
        )
        difference_count: int = proto.Field(
            proto.INT32,
            number=3,
        )
        error_count: int = proto.Field(
            proto.INT32,
            number=4,
        )
        oldest_date: date_pb2.Date = proto.Field(
            proto.MESSAGE,
            number=5,
            message=date_pb2.Date,
        )
        newest_date: date_pb2.Date = proto.Field(
            proto.MESSAGE,
            number=6,
            message=date_pb2.Date,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=2,
        enum=State,
    )
    config: "ReplayConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ReplayConfig",
    )
    results_summary: ResultsSummary = proto.Field(
        proto.MESSAGE,
        number=5,
        message=ResultsSummary,
    )


class ReplayResult(proto.Message):
    r"""The result of replaying a single access tuple against a
    simulated state.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        diff (google.cloud.policysimulator_v1.types.ReplayDiff):
            The difference between the principal's access
            under the current (baseline) policies and the
            principal's access under the proposed
            (simulated) policies.

            This field is only included for access tuples
            that were successfully replayed and had
            different results under the current policies and
            the proposed policies.

            This field is a member of `oneof`_ ``result``.
        error (google.rpc.status_pb2.Status):
            The error that caused the access tuple replay
            to fail.
            This field is only included for access tuples
            that were not replayed successfully.

            This field is a member of `oneof`_ ``result``.
        name (str):
            The resource name of the ``ReplayResult``, in the following
            format:

            ``{projects|folders|organizations}/{resource-id}/locations/global/replays/{replay-id}/results/{replay-result-id}``,
            where ``{resource-id}`` is the ID of the project, folder, or
            organization that owns the
            [Replay][google.cloud.policysimulator.v1.Replay].

            Example:
            ``projects/my-example-project/locations/global/replays/506a5f7f-38ce-4d7d-8e03-479ce1833c36/results/1234``
        parent (str):
            The [Replay][google.cloud.policysimulator.v1.Replay] that
            the access tuple was included in.
        access_tuple (google.cloud.policysimulator_v1.types.AccessTuple):
            The access tuple that was replayed. This
            field includes information about the principal,
            resource, and permission that were involved in
            the access attempt.
        last_seen_date (google.type.date_pb2.Date):
            The latest date this access tuple was seen in
            the logs.
    """

    diff: "ReplayDiff" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="result",
        message="ReplayDiff",
    )
    error: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="result",
        message=status_pb2.Status,
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    parent: str = proto.Field(
        proto.STRING,
        number=2,
    )
    access_tuple: explanations.AccessTuple = proto.Field(
        proto.MESSAGE,
        number=3,
        message=explanations.AccessTuple,
    )
    last_seen_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=4,
        message=date_pb2.Date,
    )


class CreateReplayRequest(proto.Message):
    r"""Request message for
    [Simulator.CreateReplay][google.cloud.policysimulator.v1.Simulator.CreateReplay].

    Attributes:
        parent (str):
            Required. The parent resource where this
            [Replay][google.cloud.policysimulator.v1.Replay] will be
            created. This resource must be a project, folder, or
            organization with a location.

            Example: ``projects/my-example-project/locations/global``
        replay (google.cloud.policysimulator_v1.types.Replay):
            Required. The
            [Replay][google.cloud.policysimulator.v1.Replay] to create.
            Set ``Replay.ReplayConfig`` to configure the replay.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    replay: "Replay" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Replay",
    )


class ReplayOperationMetadata(proto.Message):
    r"""Metadata about a Replay operation.

    Attributes:
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Time when the request was received.
    """

    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )


class GetReplayRequest(proto.Message):
    r"""Request message for
    [Simulator.GetReplay][google.cloud.policysimulator.v1.Simulator.GetReplay].

    Attributes:
        name (str):
            Required. The name of the
            [Replay][google.cloud.policysimulator.v1.Replay] to
            retrieve, in the following format:

            ``{projects|folders|organizations}/{resource-id}/locations/global/replays/{replay-id}``,
            where ``{resource-id}`` is the ID of the project, folder, or
            organization that owns the ``Replay``.

            Example:
            ``projects/my-example-project/locations/global/replays/506a5f7f-38ce-4d7d-8e03-479ce1833c36``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListReplayResultsRequest(proto.Message):
    r"""Request message for
    [Simulator.ListReplayResults][google.cloud.policysimulator.v1.Simulator.ListReplayResults].

    Attributes:
        parent (str):
            Required. The
            [Replay][google.cloud.policysimulator.v1.Replay] whose
            results are listed, in the following format:

            ``{projects|folders|organizations}/{resource-id}/locations/global/replays/{replay-id}``

            Example:
            ``projects/my-project/locations/global/replays/506a5f7f-38ce-4d7d-8e03-479ce1833c36``
        page_size (int):
            The maximum number of
            [ReplayResult][google.cloud.policysimulator.v1.ReplayResult]
            objects to return. Defaults to 5000.

            The maximum value is 5000; values above 5000 are rounded
            down to 5000.
        page_token (str):
            A page token, received from a previous
            [Simulator.ListReplayResults][google.cloud.policysimulator.v1.Simulator.ListReplayResults]
            call. Provide this token to retrieve the next page of
            results.

            When paginating, all other parameters provided to
            [Simulator.ListReplayResults[] must match the call that
            provided the page token.
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


class ListReplayResultsResponse(proto.Message):
    r"""Response message for
    [Simulator.ListReplayResults][google.cloud.policysimulator.v1.Simulator.ListReplayResults].

    Attributes:
        replay_results (MutableSequence[google.cloud.policysimulator_v1.types.ReplayResult]):
            The results of running a
            [Replay][google.cloud.policysimulator.v1.Replay].
        next_page_token (str):
            A token that you can use to retrieve the next page of
            [ReplayResult][google.cloud.policysimulator.v1.ReplayResult]
            objects. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    replay_results: MutableSequence["ReplayResult"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ReplayResult",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ReplayConfig(proto.Message):
    r"""The configuration used for a
    [Replay][google.cloud.policysimulator.v1.Replay].

    Attributes:
        policy_overlay (MutableMapping[str, google.iam.v1.policy_pb2.Policy]):
            A mapping of the resources that you want to simulate
            policies for and the policies that you want to simulate.

            Keys are the full resource names for the resources. For
            example,
            ``//cloudresourcemanager.googleapis.com/projects/my-project``.
            For examples of full resource names for Google Cloud
            services, see
            https://cloud.google.com/iam/help/troubleshooter/full-resource-names.

            Values are [Policy][google.iam.v1.Policy] objects
            representing the policies that you want to simulate.

            Replays automatically take into account any IAM policies
            inherited through the resource hierarchy, and any policies
            set on descendant resources. You do not need to include
            these policies in the policy overlay.
        log_source (google.cloud.policysimulator_v1.types.ReplayConfig.LogSource):
            The logs to use as input for the
            [Replay][google.cloud.policysimulator.v1.Replay].
    """

    class LogSource(proto.Enum):
        r"""The source of the logs to use for a
        [Replay][google.cloud.policysimulator.v1.Replay].

        Values:
            LOG_SOURCE_UNSPECIFIED (0):
                An unspecified log source. If the log source is unspecified,
                the [Replay][google.cloud.policysimulator.v1.Replay]
                defaults to using ``RECENT_ACCESSES``.
            RECENT_ACCESSES (1):
                All access logs from the last 90 days. These
                logs may not include logs from the most recent 7
                days.
        """

        LOG_SOURCE_UNSPECIFIED = 0
        RECENT_ACCESSES = 1

    policy_overlay: MutableMapping[str, policy_pb2.Policy] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=1,
        message=policy_pb2.Policy,
    )
    log_source: LogSource = proto.Field(
        proto.ENUM,
        number=2,
        enum=LogSource,
    )


class ReplayDiff(proto.Message):
    r"""The difference between the results of evaluating an access
    tuple under the current (baseline) policies and under the
    proposed (simulated) policies. This difference explains how a
    principal's access could change if the proposed policies were
    applied.

    Attributes:
        access_diff (google.cloud.policysimulator_v1.types.AccessStateDiff):
            A summary and comparison of the principal's access under the
            current (baseline) policies and the proposed (simulated)
            policies for a single access tuple.

            The evaluation of the principal's access is reported in the
            [AccessState][google.cloud.policysimulator.v1.AccessState]
            field.
    """

    access_diff: "AccessStateDiff" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="AccessStateDiff",
    )


class AccessStateDiff(proto.Message):
    r"""A summary and comparison of the principal's access under the
    current (baseline) policies and the proposed (simulated)
    policies for a single access tuple.

    Attributes:
        baseline (google.cloud.policysimulator_v1.types.ExplainedAccess):
            The results of evaluating the access tuple under the current
            (baseline) policies.

            If the
            [AccessState][google.cloud.policysimulator.v1.AccessState]
            couldn't be fully evaluated, this field explains why.
        simulated (google.cloud.policysimulator_v1.types.ExplainedAccess):
            The results of evaluating the access tuple
            under the proposed (simulated) policies.

            If the AccessState couldn't be fully evaluated,
            this field explains why.
        access_change (google.cloud.policysimulator_v1.types.AccessStateDiff.AccessChangeType):
            How the principal's access, specified in the
            AccessState field, changed between the current
            (baseline) policies and proposed (simulated)
            policies.
    """

    class AccessChangeType(proto.Enum):
        r"""How the principal's access, specified in the AccessState
        field, changed between the current (baseline) policies and
        proposed (simulated) policies.

        Values:
            ACCESS_CHANGE_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            NO_CHANGE (1):
                The principal's access did not change.
                This includes the case where both baseline and
                simulated are UNKNOWN, but the unknown
                information is equivalent.
            UNKNOWN_CHANGE (2):
                The principal's access under both the current policies and
                the proposed policies is ``UNKNOWN``, but the unknown
                information differs between them.
            ACCESS_REVOKED (3):
                The principal had access under the current policies
                (``GRANTED``), but will no longer have access after the
                proposed changes (``NOT_GRANTED``).
            ACCESS_GAINED (4):
                The principal did not have access under the current policies
                (``NOT_GRANTED``), but will have access after the proposed
                changes (``GRANTED``).
            ACCESS_MAYBE_REVOKED (5):
                This result can occur for the following reasons:

                - The principal had access under the current policies
                  (``GRANTED``), but their access after the proposed changes
                  is ``UNKNOWN``.

                - The principal's access under the current policies is
                  ``UNKNOWN``, but they will not have access after the
                  proposed changes (``NOT_GRANTED``).
            ACCESS_MAYBE_GAINED (6):
                This result can occur for the following reasons:

                - The principal did not have access under the current
                  policies (``NOT_GRANTED``), but their access after the
                  proposed changes is ``UNKNOWN``.

                - The principal's access under the current policies is
                  ``UNKNOWN``, but they will have access after the proposed
                  changes (``GRANTED``).
        """

        ACCESS_CHANGE_TYPE_UNSPECIFIED = 0
        NO_CHANGE = 1
        UNKNOWN_CHANGE = 2
        ACCESS_REVOKED = 3
        ACCESS_GAINED = 4
        ACCESS_MAYBE_REVOKED = 5
        ACCESS_MAYBE_GAINED = 6

    baseline: "ExplainedAccess" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ExplainedAccess",
    )
    simulated: "ExplainedAccess" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ExplainedAccess",
    )
    access_change: AccessChangeType = proto.Field(
        proto.ENUM,
        number=3,
        enum=AccessChangeType,
    )


class ExplainedAccess(proto.Message):
    r"""Details about how a set of policies, listed in
    [ExplainedPolicy][google.cloud.policysimulator.v1.ExplainedPolicy],
    resulted in a certain
    [AccessState][google.cloud.policysimulator.v1.AccessState] when
    replaying an access tuple.

    Attributes:
        access_state (google.cloud.policysimulator_v1.types.AccessState):
            Whether the principal in the access tuple has
            permission to access the resource in the access
            tuple under the given policies.
        policies (MutableSequence[google.cloud.policysimulator_v1.types.ExplainedPolicy]):
            If the
            [AccessState][google.cloud.policysimulator.v1.AccessState]
            is ``UNKNOWN``, this field contains the policies that led to
            that result.

            If the ``AccessState`` is ``GRANTED`` or ``NOT_GRANTED``,
            this field is omitted.
        errors (MutableSequence[google.rpc.status_pb2.Status]):
            If the
            [AccessState][google.cloud.policysimulator.v1.AccessState]
            is ``UNKNOWN``, this field contains a list of errors
            explaining why the result is ``UNKNOWN``.

            If the ``AccessState`` is ``GRANTED`` or ``NOT_GRANTED``,
            this field is omitted.
    """

    access_state: explanations.AccessState = proto.Field(
        proto.ENUM,
        number=1,
        enum=explanations.AccessState,
    )
    policies: MutableSequence[explanations.ExplainedPolicy] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=explanations.ExplainedPolicy,
    )
    errors: MutableSequence[status_pb2.Status] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=status_pb2.Status,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
