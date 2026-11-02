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

from google.ads.admanager_v1.types import size_type_enum

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "Size",
    },
)


class Size(proto.Message):
    r"""Represents the dimensions of an AdUnit, LineItem, or
    Creative.

    Attributes:
        width (int):
            Required. The width of the Creative,
            [AdUnit][google.ads.admanager.v1.AdUnit], or LineItem.
        height (int):
            Required. The height of the Creative,
            [AdUnit][google.ads.admanager.v1.AdUnit], or LineItem.
        size_type (google.ads.admanager_v1.types.SizeTypeEnum.SizeType):
            Required. The SizeType of the Creative,
            [AdUnit][google.ads.admanager.v1.AdUnit], or LineItem.
    """

    width: int = proto.Field(
        proto.INT32,
        number=1,
    )
    height: int = proto.Field(
        proto.INT32,
        number=2,
    )
    size_type: size_type_enum.SizeTypeEnum.SizeType = proto.Field(
        proto.ENUM,
        number=3,
        enum=size_type_enum.SizeTypeEnum.SizeType,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
