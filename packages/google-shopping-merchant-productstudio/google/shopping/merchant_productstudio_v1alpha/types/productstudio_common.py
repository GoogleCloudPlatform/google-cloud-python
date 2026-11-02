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
    package="google.shopping.merchant.productstudio.v1alpha",
    manifest={
        "InputImage",
    },
)


class InputImage(proto.Message):
    r"""Represents an input image.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        image_uri (str):
            Public uri of the image.

            This field is a member of `oneof`_ ``image``.
        image_bytes (bytes):
            Raw image bytes.

            This field is a member of `oneof`_ ``image``.
    """

    image_uri: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="image",
    )
    image_bytes: bytes = proto.Field(
        proto.BYTES,
        number=2,
        oneof="image",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
