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
    package="google.ads.admanager.v1",
    manifest={
        "LineItemStats",
    },
)


class LineItemStats(proto.Message):
    r"""Contains trafficking statistics for LineItem.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        impressions_delivered (int):
            Output only. The number of impressions
            delivered.

            This field is a member of `oneof`_ ``_impressions_delivered``.
        clicks_delivered (int):
            Output only. The number of clicks delivered

            This field is a member of `oneof`_ ``_clicks_delivered``.
        video_completions_delivered (int):
            Output only. The number of video completions
            delivered.

            This field is a member of `oneof`_ ``_video_completions_delivered``.
        video_starts_delivered (int):
            Output only. The number of video starts
            delivered.

            This field is a member of `oneof`_ ``_video_starts_delivered``.
        viewable_impressions_delivered (int):
            Output only. The number of viewable
            impressions delivered.

            This field is a member of `oneof`_ ``_viewable_impressions_delivered``.
        delivery_data (MutableSequence[int]):
            Output only. Clicks or impressions delivered
            for each of the last 7 days. Values are in
            chronological order (oldest to newest).
    """

    impressions_delivered: int = proto.Field(
        proto.INT64,
        number=1,
        optional=True,
    )
    clicks_delivered: int = proto.Field(
        proto.INT64,
        number=2,
        optional=True,
    )
    video_completions_delivered: int = proto.Field(
        proto.INT64,
        number=3,
        optional=True,
    )
    video_starts_delivered: int = proto.Field(
        proto.INT64,
        number=4,
        optional=True,
    )
    viewable_impressions_delivered: int = proto.Field(
        proto.INT64,
        number=5,
        optional=True,
    )
    delivery_data: MutableSequence[int] = proto.RepeatedField(
        proto.INT64,
        number=8,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
