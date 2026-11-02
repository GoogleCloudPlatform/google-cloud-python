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
        "HistoryState",
    },
)


class HistoryState(proto.Enum):
    r"""The history state for messages and spaces. Specifies how long
    messages and conversation threads are kept after creation.

    Values:
        HISTORY_STATE_UNSPECIFIED (0):
            Default value. Do not use.
        HISTORY_OFF (1):
            History off. `Messages and threads are kept for 24
            hours <https://support.google.com/chat/answer/7664687>`__.
        HISTORY_ON (2):
            History on. The organization's `Vault retention
            rules <https://support.google.com/vault/answer/7657597>`__
            specify for how long messages and threads are kept.
    """

    HISTORY_STATE_UNSPECIFIED = 0
    HISTORY_OFF = 1
    HISTORY_ON = 2


__all__ = tuple(sorted(__protobuf__.manifest))
