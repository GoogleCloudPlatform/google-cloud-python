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

from google.ads.admanager_v1.types import time_unit_enum

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "FrequencyCap",
    },
)


class FrequencyCap(proto.Message):
    r"""Represents a Frequency Cap that can be applied to an entity.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        max_impressions (int):
            The maximum number of impressions for this
            frequency cap.

            This field is a member of `oneof`_ ``_max_impressions``.
        time_amount (int):
            The number of time units over which the
            frequency cap is effective.

            This field is a member of `oneof`_ ``_time_amount``.
        time_unit (google.ads.admanager_v1.types.TimeUnitEnum.TimeUnit):
            The units of time of this frequency cap.

            This field is a member of `oneof`_ ``_time_unit``.
    """

    max_impressions: int = proto.Field(
        proto.INT64,
        number=1,
        optional=True,
    )
    time_amount: int = proto.Field(
        proto.INT64,
        number=2,
        optional=True,
    )
    time_unit: time_unit_enum.TimeUnitEnum.TimeUnit = proto.Field(
        proto.ENUM,
        number=3,
        optional=True,
        enum=time_unit_enum.TimeUnitEnum.TimeUnit,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
