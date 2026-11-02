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
        "ExclusionScopeEnum",
    },
)


class ExclusionScopeEnum(proto.Message):
    r"""Wrapper message for
    [ExclusionScope][google.ads.admanager.v1.ExclusionScopeEnum.ExclusionScope].

    """

    class ExclusionScope(proto.Enum):
        r"""The scope to which the exclusion label applies.

        Values:
            EXCLUSION_SCOPE_UNSPECIFIED (0):
                No value specified.
            PAGE (1):
                The exclusion label applies to the entire
                page.
            STREAM (2):
                The exclusion label applies to the entire
                stream of content.
            POD (3):
                The exclusion label applies to the entire pod
                (or group).
        """

        EXCLUSION_SCOPE_UNSPECIFIED = 0
        PAGE = 1
        STREAM = 2
        POD = 3


__all__ = tuple(sorted(__protobuf__.manifest))
