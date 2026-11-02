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

from google.ads.admanager_v1.types import (
    ad_unit_enums,
    ad_unit_messages,
    target_platform_enum,
)

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "SuggestedAdUnit",
    },
)


class SuggestedAdUnit(proto.Message):
    r"""A read-only suggestion for a new ad unit based on an ad tag
    that has served 10+ times in the past week for an undefined ad
    unit.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. Resource name of the ``SuggestedAdUnit``.
            Format:
            ``networks/{network_code}/suggestedAdUnits/{suggested_ad_unit_id}``
        weekly_request_count (int):
            Output only. Number of times the ad tag has
            been served in the past week.

            This field is a member of `oneof`_ ``_weekly_request_count``.
        new_code_path (MutableSequence[str]):
            Output only. Path of suggested ad unit codes from the
            closest existing ancestor ad unit that will all be created
            as ad units when the suggestion is approved.

            Example: If a -> b -> c are existing ad units with
            parent-child relationships, and the suggested ad unit x is a
            child of c, the ``new_code_path`` is (x). If x is the
            grandchild of c, the ``new_code_path`` is (y, x) where y is
            an ad unit that would be created as the parent ad unit of x
            (and the child of c) if the suggestion is approved.
        existing_code_path (MutableSequence[google.ads.admanager_v1.types.AdUnitParent]):
            Output only. Code path of ad units leading up to and
            including the parent of the first suggested ad unit.
            Combined with the ``new_code_path`` field, this represents
            the full path for the suggested ad unit if approved.

            Example: If a -> b -> c are existing ad units with
            parent-child relationships, and the suggested ad unit x is a
            child of c, the ``existing_code_path`` is (a, b, c). If x is
            the grandchild of c, the ``existing_code_path`` is also (a,
            b, c).
        target_window (google.ads.admanager_v1.types.TargetWindowEnum.TargetWindow):
            Output only. Target window of the underlying
            ad tag which will be used in the ad unit if the
            suggestion is approved.

            This field is a member of `oneof`_ ``_target_window``.
        target_platform (google.ads.admanager_v1.types.TargetPlatformEnum.TargetPlatform):
            Output only. Target platform for the browser
            that clicked the underlying ad tag.

            This field is a member of `oneof`_ ``_target_platform``.
        ad_unit_sizes (MutableSequence[google.ads.admanager_v1.types.AdUnitSize]):
            Output only. Sizes associated with this
            suggested ad unit.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    weekly_request_count: int = proto.Field(
        proto.INT64,
        number=2,
        optional=True,
    )
    new_code_path: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    existing_code_path: MutableSequence[ad_unit_messages.AdUnitParent] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message=ad_unit_messages.AdUnitParent,
        )
    )
    target_window: ad_unit_enums.TargetWindowEnum.TargetWindow = proto.Field(
        proto.ENUM,
        number=5,
        optional=True,
        enum=ad_unit_enums.TargetWindowEnum.TargetWindow,
    )
    target_platform: target_platform_enum.TargetPlatformEnum.TargetPlatform = (
        proto.Field(
            proto.ENUM,
            number=6,
            optional=True,
            enum=target_platform_enum.TargetPlatformEnum.TargetPlatform,
        )
    )
    ad_unit_sizes: MutableSequence[ad_unit_messages.AdUnitSize] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message=ad_unit_messages.AdUnitSize,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
