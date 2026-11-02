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

from google.ads.admanager_v1.types import targeting as gaa_targeting

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "CreativeTargeting",
    },
)


class CreativeTargeting(proto.Message):
    r"""Represents the creative targeting criteria for a LineItem.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        creative_targeting_display_name (str):
            Required. The name of this creative
            targeting. This attribute is required.

            This field is a member of `oneof`_ ``_creative_targeting_display_name``.
        targeting (google.ads.admanager_v1.types.Targeting):
            Required. The Targeting criteria of this
            creative targeting. This attribute is required.

            This field is a member of `oneof`_ ``_targeting``.
    """

    creative_targeting_display_name: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    targeting: gaa_targeting.Targeting = proto.Field(
        proto.MESSAGE,
        number=2,
        optional=True,
        message=gaa_targeting.Targeting,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
