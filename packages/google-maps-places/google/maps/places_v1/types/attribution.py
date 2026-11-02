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
    package="google.maps.places.v1",
    manifest={
        "AuthorAttribution",
    },
)


class AuthorAttribution(proto.Message):
    r"""Information about the author of the UGC data. Used in
    [Photo][google.maps.places.v1.Photo], and
    [Review][google.maps.places.v1.Review].

    Attributes:
        display_name (str):
            Name of the author of the
            [Photo][google.maps.places.v1.Photo] or
            [Review][google.maps.places.v1.Review].
        uri (str):
            URI of the author of the
            [Photo][google.maps.places.v1.Photo] or
            [Review][google.maps.places.v1.Review].
        photo_uri (str):
            Profile photo URI of the author of the
            [Photo][google.maps.places.v1.Photo] or
            [Review][google.maps.places.v1.Review].
    """

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    photo_uri: str = proto.Field(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
