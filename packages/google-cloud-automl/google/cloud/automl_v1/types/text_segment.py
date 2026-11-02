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
    package="google.cloud.automl.v1",
    manifest={
        "TextSegment",
    },
)


class TextSegment(proto.Message):
    r"""A contiguous part of a text (string), assuming it has an
    UTF-8 NFC encoding.

    Attributes:
        content (str):
            Output only. The content of the TextSegment.
        start_offset (int):
            Required. Zero-based character index of the
            first character of the text segment (counting
            characters from the beginning of the text).
        end_offset (int):
            Required. Zero-based character index of the first character
            past the end of the text segment (counting character from
            the beginning of the text). The character at the end_offset
            is NOT included in the text segment.
    """

    content: str = proto.Field(
        proto.STRING,
        number=3,
    )
    start_offset: int = proto.Field(
        proto.INT64,
        number=1,
    )
    end_offset: int = proto.Field(
        proto.INT64,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
