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
    package="grafeas.v1",
    manifest={
        "Severity",
    },
)


class Severity(proto.Enum):
    r"""Note provider assigned severity/impact ranking.

    Values:
        SEVERITY_UNSPECIFIED (0):
            Unknown.
        MINIMAL (1):
            Minimal severity.
        LOW (2):
            Low severity.
        MEDIUM (3):
            Medium severity.
        HIGH (4):
            High severity.
        CRITICAL (5):
            Critical severity.
    """

    SEVERITY_UNSPECIFIED = 0
    MINIMAL = 1
    LOW = 2
    MEDIUM = 3
    HIGH = 4
    CRITICAL = 5


__all__ = tuple(sorted(__protobuf__.manifest))
