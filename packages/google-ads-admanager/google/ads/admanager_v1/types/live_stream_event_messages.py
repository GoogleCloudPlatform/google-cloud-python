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
        "LiveStreamEvent",
    },
)


class LiveStreamEvent(proto.Message):
    r"""A ``LiveStreamEvent`` encapsulates all the information necessary to
    enable DAI (Dynamic Ad Insertion) into a live video stream. This
    includes information such as the start and expected end time of the
    ``LiveStreamEvent``, the URL of the actual content for Ad Manager to
    pull and insert ads into, as well as the metadata necessary to
    generate ad requests during the live stream.

    Attributes:
        name (str):
            Identifier. The resource name of the ``LiveStreamEvent``.
            Format:
            ``networks/{network_code}/liveStreamEvents/{live_stream_event_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
