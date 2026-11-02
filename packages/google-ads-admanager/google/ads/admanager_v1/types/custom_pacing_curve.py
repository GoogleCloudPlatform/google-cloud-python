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
import proto  # type: ignore

from google.ads.admanager_v1.types import custom_pacing_goal_unit_enum

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "CustomPacingCurve",
        "CustomPacingGoal",
    },
)


class CustomPacingCurve(proto.Message):
    r"""A curve consisting of CustomPacingGoal objects that is used
    to pace line item delivery.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        custom_pacing_goal_unit (google.ads.admanager_v1.types.CustomPacingGoalUnitEnum.CustomPacingGoalUnit):
            Required. The unit of the
            [CustomPacingGoal.amount][google.ads.admanager.v1.CustomPacingGoal.amount]
            values.

            This field is a member of `oneof`_ ``_custom_pacing_goal_unit``.
        custom_pacing_goals (MutableSequence[google.ads.admanager_v1.types.CustomPacingGoal]):
            Required. The list of goals that make up the
            custom pacing curve.
    """

    custom_pacing_goal_unit: custom_pacing_goal_unit_enum.CustomPacingGoalUnitEnum.CustomPacingGoalUnit = proto.Field(
        proto.ENUM,
        number=1,
        optional=True,
        enum=custom_pacing_goal_unit_enum.CustomPacingGoalUnitEnum.CustomPacingGoalUnit,
    )
    custom_pacing_goals: MutableSequence["CustomPacingGoal"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="CustomPacingGoal",
    )


class CustomPacingGoal(proto.Message):
    r"""An interval of a CustomPacingCurve. A custom pacing goal
    contains a start time and an amount. The goal will apply until
    either the next custom pacing goal's getStartTime or the line
    item's end time if it is the last goal.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. The start date and time of the goal. This field is
            required unless
            [useLineItemStartTime][google.ads.admanager.v1.CustomPacingGoal.use_line_item_start_time]
            is true.

            This field is a member of `oneof`_ ``_start_time``.
        use_line_item_start_time (bool):
            Optional. Input only. Whether the
            [LineItem.startTime][google.ads.admanager.v1.LineItem.start_time]
            should be used for the start date and time of this goal.
            This field is not persisted and if it is set to true, the
            [startTime][google.ads.admanager.v1.CustomPacingGoal.start_time]
            field will be populated by the line item's start time.

            This field is a member of `oneof`_ ``_use_line_item_start_time``.
        amount (int):
            Optional. The amount associated with the
            goal. This field is required.

            This field is a member of `oneof`_ ``_amount``.
    """

    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    use_line_item_start_time: bool = proto.Field(
        proto.BOOL,
        number=2,
        optional=True,
    )
    amount: int = proto.Field(
        proto.INT64,
        number=3,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
