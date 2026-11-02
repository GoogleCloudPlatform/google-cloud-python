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
    package="google.shopping.merchant.accounts.v1beta",
    manifest={
        "AccessRight",
    },
)


class AccessRight(proto.Enum):
    r"""The access right.

    Values:
        ACCESS_RIGHT_UNSPECIFIED (0):
            Default value. This value is unused.
        STANDARD (1):
            Standard access rights.
        ADMIN (2):
            Admin access rights.
        PERFORMANCE_REPORTING (3):
            Users with this right have access to
            performance and insights.
    """

    ACCESS_RIGHT_UNSPECIFIED = 0
    STANDARD = 1
    ADMIN = 2
    PERFORMANCE_REPORTING = 3


__all__ = tuple(sorted(__protobuf__.manifest))
