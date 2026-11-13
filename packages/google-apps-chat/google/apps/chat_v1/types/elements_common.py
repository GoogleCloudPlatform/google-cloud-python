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
    package="google.chat.v1",
    manifest={
        "ElementsImage",
    },
)


class ElementsImage(proto.Message):
    r"""An object encapsulating different ways of representing an image.
    Currently supported representations:

    - An image fetched from a URI.

    Additional representations might be supported in the future.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        image_uri (str):
            Required. The URI of the image. Must be a
            publicly accessible URI so that Chat can fetch
            and display it.

            This field is a member of `oneof`_ ``image``.
    """

    image_uri: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="image",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
