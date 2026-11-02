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
    package="google.cloud.video.stitcher.v1",
    manifest={
        "FetchOptions",
    },
)


class FetchOptions(proto.Message):
    r"""Options on how fetches should be made.

    Attributes:
        headers (MutableMapping[str, str]):
            Custom headers to pass into fetch request.
            Headers must have a maximum of 3 key value
            pairs. Each key value pair must have a maximum
            of 256 characters per key and 256 characters per
            value.
    """

    headers: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
