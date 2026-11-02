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
    package="google.firestore.admin.v1",
    manifest={
        "RealtimeUpdatesMode",
    },
)


class RealtimeUpdatesMode(proto.Enum):
    r"""The Realtime Updates mode.

    Values:
        REALTIME_UPDATES_MODE_UNSPECIFIED (0):
            The Realtime Updates feature is not
            specified.
        REALTIME_UPDATES_MODE_ENABLED (1):
            The Realtime Updates feature is enabled by
            default.
            This could potentially degrade write performance
            for the database.
        REALTIME_UPDATES_MODE_DISABLED (2):
            The Realtime Updates feature is disabled by
            default.
    """

    REALTIME_UPDATES_MODE_UNSPECIFIED = 0
    REALTIME_UPDATES_MODE_ENABLED = 1
    REALTIME_UPDATES_MODE_DISABLED = 2


__all__ = tuple(sorted(__protobuf__.manifest))
