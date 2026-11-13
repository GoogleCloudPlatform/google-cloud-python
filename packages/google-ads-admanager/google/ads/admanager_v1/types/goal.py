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

from google.ads.admanager_v1.types import goal_enums

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "Goal",
    },
)


class Goal(proto.Message):
    r"""Defines the criteria a [LineItem][google.ads.admanager.v1.LineItem]
    needs to satisfy to meet its delivery goal.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        goal_type (google.ads.admanager_v1.types.GoalTypeEnum.GoalType):
            The type of the goal for the LineItem. It
            defines the period over which the goal should be
            reached.

            This field is a member of `oneof`_ ``_goal_type``.
        unit_type (google.ads.admanager_v1.types.UnitTypeEnum.UnitType):
            The type of the goal unit for the LineItem.

            This field is a member of `oneof`_ ``_unit_type``.
        units (int):
            If this is a primary goal, it represents the number or
            percentage of impressions or clicks that will be reserved.
            If the line item is of type
            [LineItemTypeEnum.LineItemType.SPONSORSHIP][google.ads.admanager.v1.LineItemTypeEnum.LineItemType.SPONSORSHIP],
            it represents the percentage of available impressions
            reserved. If the line item is of type
            [LineItemTypeEnum.LineItemType.BULK][google.ads.admanager.v1.LineItemTypeEnum.LineItemType.BULK]
            or
            [LineItemTypeEnum.LineItemType.PRICE_PRIORITY][google.ads.admanager.v1.LineItemTypeEnum.LineItemType.PRICE_PRIORITY],
            it represents the number of remaining impressions reserved.
            If the line item is of type
            [LineItemTypeEnum.LineItemType.NETWORK][google.ads.admanager.v1.LineItemTypeEnum.LineItemType.NETWORK]
            or
            [LineItemTypeEnum.LineItemType.HOUSE][google.ads.admanager.v1.LineItemTypeEnum.LineItemType.HOUSE],
            it represents the percentage of remaining impressions
            reserved. If this is an impression cap goal, it represents
            the number of impressions or conversions that the line item
            will stop serving at if reached. For valid line item types,
            see [LineItem.impressionsCap][LineItem.impressions_cap].

            This field is a member of `oneof`_ ``_units``.
    """

    goal_type: goal_enums.GoalTypeEnum.GoalType = proto.Field(
        proto.ENUM,
        number=1,
        optional=True,
        enum=goal_enums.GoalTypeEnum.GoalType,
    )
    unit_type: goal_enums.UnitTypeEnum.UnitType = proto.Field(
        proto.ENUM,
        number=2,
        optional=True,
        enum=goal_enums.UnitTypeEnum.UnitType,
    )
    units: int = proto.Field(
        proto.INT64,
        number=3,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
