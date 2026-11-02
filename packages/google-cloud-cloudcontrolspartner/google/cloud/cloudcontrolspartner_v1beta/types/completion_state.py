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
    package="google.cloud.cloudcontrolspartner.v1beta",
    manifest={
        "CompletionState",
    },
)


class CompletionState(proto.Enum):
    r"""Enum for possible completion states.

    Values:
        COMPLETION_STATE_UNSPECIFIED (0):
            Unspecified completion state.
        PENDING (1):
            Task started (has start date) but not yet
            completed.
        SUCCEEDED (2):
            Succeeded state.
        FAILED (3):
            Failed state.
        NOT_APPLICABLE (4):
            Not applicable state.
    """

    COMPLETION_STATE_UNSPECIFIED = 0
    PENDING = 1
    SUCCEEDED = 2
    FAILED = 3
    NOT_APPLICABLE = 4


__all__ = tuple(sorted(__protobuf__.manifest))
