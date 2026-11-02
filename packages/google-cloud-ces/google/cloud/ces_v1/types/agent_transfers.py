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
    package="google.cloud.ces.v1",
    manifest={
        "ExpressionCondition",
        "PythonCodeCondition",
        "TransferRule",
    },
)


class ExpressionCondition(proto.Message):
    r"""Expression condition based on session state.

    Attributes:
        expression (str):
            Required. The string representation of
            cloud.api.Expression condition.
    """

    expression: str = proto.Field(
        proto.STRING,
        number=1,
    )


class PythonCodeCondition(proto.Message):
    r"""Python code block to evaluate the condition.

    Attributes:
        python_code (str):
            Required. The python code to execute.
    """

    python_code: str = proto.Field(
        proto.STRING,
        number=1,
    )


class TransferRule(proto.Message):
    r"""Rule for transferring to a specific agent.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        deterministic_transfer (google.cloud.ces_v1.types.TransferRule.DeterministicTransfer):
            Optional. A rule that immediately transfers
            to the target agent when the condition is met.

            This field is a member of `oneof`_ ``rule_type``.
        disable_planner_transfer (google.cloud.ces_v1.types.TransferRule.DisablePlannerTransfer):
            Optional. Rule that prevents the planner from
            transferring to the target agent.

            This field is a member of `oneof`_ ``rule_type``.
        child_agent (str):
            Required. The resource name of the child agent the rule
            applies to. Format:
            ``projects/{project}/locations/{location}/apps/{app}/agents/{agent}``
        direction (google.cloud.ces_v1.types.TransferRule.Direction):
            Required. The direction of the transfer.
    """

    class Direction(proto.Enum):
        r"""The direction of the transfer.

        Values:
            DIRECTION_UNSPECIFIED (0):
                Unspecified direction.
            PARENT_TO_CHILD (1):
                Transfer from the parent agent to the child
                agent.
            CHILD_TO_PARENT (2):
                Transfer from the child agent to the parent
                agent.
        """

        DIRECTION_UNSPECIFIED = 0
        PARENT_TO_CHILD = 1
        CHILD_TO_PARENT = 2

    class DeterministicTransfer(proto.Message):
        r"""Deterministic transfer rule. When the condition evaluates to
        true, the transfer occurs.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            expression_condition (google.cloud.ces_v1.types.ExpressionCondition):
                Optional. A rule that evaluates a session
                state condition. If the condition evaluates to
                true, the transfer occurs.

                This field is a member of `oneof`_ ``condition_type``.
            python_code_condition (google.cloud.ces_v1.types.PythonCodeCondition):
                Optional. A rule that uses Python code block
                to evaluate the conditions. If the condition
                evaluates to true, the transfer occurs.

                This field is a member of `oneof`_ ``condition_type``.
        """

        expression_condition: "ExpressionCondition" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="condition_type",
            message="ExpressionCondition",
        )
        python_code_condition: "PythonCodeCondition" = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="condition_type",
            message="PythonCodeCondition",
        )

    class DisablePlannerTransfer(proto.Message):
        r"""A rule that prevents the planner from transferring to the
        target agent.

        Attributes:
            expression_condition (google.cloud.ces_v1.types.ExpressionCondition):
                Required. If the condition evaluates to true,
                planner will not be allowed to transfer to the
                target agent.
        """

        expression_condition: "ExpressionCondition" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="ExpressionCondition",
        )

    deterministic_transfer: DeterministicTransfer = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="rule_type",
        message=DeterministicTransfer,
    )
    disable_planner_transfer: DisablePlannerTransfer = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="rule_type",
        message=DisablePlannerTransfer,
    )
    child_agent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    direction: Direction = proto.Field(
        proto.ENUM,
        number=2,
        enum=Direction,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
