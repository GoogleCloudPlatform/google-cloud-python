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

from google.ads.admanager_v1.types import applied_label
from google.ads.admanager_v1.types import size as gaa_size

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "CreativePlaceholder",
        "CreativePlaceholderCompanion",
    },
)


class CreativePlaceholder(proto.Message):
    r"""Describes a slot that a creative is expected to fill. This is
    used in forecasting and to validate that the correct creatives
    are associated with the line item.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        size (google.ads.admanager_v1.types.Size):
            Required. The size that the creative is
            expected to have.
        companions (MutableSequence[google.ads.admanager_v1.types.CreativePlaceholderCompanion]):
            Optional. The companions that the creative is expected to
            have. This attribute can only be set if the line item it
            belongs to has an
            [EnvironmentType][google.ads.admanager.v1.EnvironmentTypeEnum.EnvironmentType]
            of
            [VIDEO_PLAYER][google.ads.admanager.v1.EnvironmentTypeEnum.EnvironmentType.VIDEO_PLAYER]
            or
            [roadblockingType][google.ads.admanager.v1.LineItem.roadblocking_type]
            of
            [CREATIVE_SET][google.ads.admanager.v1.RoadblockingTypeEnum.RoadblockingType.CREATIVE_SET].
        expected_creative_count (int):
            Optional. Non-empty default. Expected number
            of creatives that will be uploaded corresponding
            to this creative placeholder.  This estimate is
            used to improve the accuracy of forecasting; for
            example, if label frequency capping limits the
            number of times a creative may be served. By
            default, the expected creative count is set to
            1.

            This field is a member of `oneof`_ ``_expected_creative_count``.
        applied_labels (MutableSequence[google.ads.admanager_v1.types.AppliedLabel]):
            Optional. Set of labels applied directly to
            this CreativePlaceholder.
        amp_only (bool):
            Optional. Non-empty default. Indicates if the
            expected creative of this placeholder has an AMP
            only variant. This is used to improve the
            accuracy of forecasting and has no effect on
            serving. By default, the value is false.

            This field is a member of `oneof`_ ``_amp_only``.
        creative_targeting_display_name (str):
            Optional. The display name of the creative
            targeting that this CreativePlaceholder
            represents.

            This field is a member of `oneof`_ ``_creative_targeting_display_name``.
    """

    size: gaa_size.Size = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gaa_size.Size,
    )
    companions: MutableSequence["CreativePlaceholderCompanion"] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message="CreativePlaceholderCompanion",
    )
    expected_creative_count: int = proto.Field(
        proto.INT32,
        number=3,
        optional=True,
    )
    applied_labels: MutableSequence[applied_label.AppliedLabel] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=applied_label.AppliedLabel,
    )
    amp_only: bool = proto.Field(
        proto.BOOL,
        number=5,
        optional=True,
    )
    creative_targeting_display_name: str = proto.Field(
        proto.STRING,
        number=6,
        optional=True,
    )


class CreativePlaceholderCompanion(proto.Message):
    r"""An individual companion to a
    [CreativePlaceholder][google.ads.admanager.v1.CreativePlaceholder].


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        size (google.ads.admanager_v1.types.Size):
            Required. The size of the companion to a
            [CreativePlaceholder][google.ads.admanager.v1.CreativePlaceholder].

            This field is a member of `oneof`_ ``_size``.
    """

    size: gaa_size.Size = proto.Field(
        proto.MESSAGE,
        number=1,
        optional=True,
        message=gaa_size.Size,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
