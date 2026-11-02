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
    package="google.shopping.merchant.accounts.v1",
    manifest={
        "AccessRight",
    },
)


class AccessRight(proto.Enum):
    r"""The access right defines the level of permission a
    user has within a Merchant Center account.

    Values:
        ACCESS_RIGHT_UNSPECIFIED (0):
            Default value. This value is unused.
        STANDARD (1):
            Standard access rights.
        READ_ONLY (4):
            Has access to the same read-only methods as
            STANDARD, but no access to any mutating methods.
        ADMIN (2):
            Admin access rights.
        PERFORMANCE_REPORTING (3):
            Users with this right have access to
            performance and insights.
        API_DEVELOPER (5):
            Users with this right have access to Merchant
            API and its notifications. This role is only
            accessible to accounts that have a developer
            registration.
    """

    ACCESS_RIGHT_UNSPECIFIED = 0
    STANDARD = 1
    READ_ONLY = 4
    ADMIN = 2
    PERFORMANCE_REPORTING = 3
    API_DEVELOPER = 5


__all__ = tuple(sorted(__protobuf__.manifest))
