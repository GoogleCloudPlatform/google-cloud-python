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

from google.ads.admanager_v1.types import deal_priority_tier_enum

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "NonGuaranteedDealPriority",
    },
)


class NonGuaranteedDealPriority(proto.Message):
    r"""Represents the priority settings to apply to non-guaranteed
    deals, independently of their types.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        priority_tier (google.ads.admanager_v1.types.DealPriorityTierEnum.DealPriorityTier):
            Required. Enables publishers to favor certain
            deals, even if their default priorities are
            lower. For example, allowing a PA deal to beat a
            PD deal.

            This field is a member of `oneof`_ ``_priority_tier``.
    """

    priority_tier: deal_priority_tier_enum.DealPriorityTierEnum.DealPriorityTier = (
        proto.Field(
            proto.ENUM,
            number=1,
            optional=True,
            enum=deal_priority_tier_enum.DealPriorityTierEnum.DealPriorityTier,
        )
    )


__all__ = tuple(sorted(__protobuf__.manifest))
