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
    package="google.ads.datamanager.v1",
    manifest={
        "UserListLicenseStatus",
    },
)


class UserListLicenseStatus(proto.Enum):
    r"""User list license status.

    Values:
        USER_LIST_LICENSE_STATUS_UNSPECIFIED (0):
            Unknown.
        USER_LIST_LICENSE_STATUS_ENABLED (1):
            Active status - user list is still being
            licensed.
        USER_LIST_LICENSE_STATUS_DISABLED (2):
            Inactive status - user list is no longer
            being licensed.
    """

    USER_LIST_LICENSE_STATUS_UNSPECIFIED = 0
    USER_LIST_LICENSE_STATUS_ENABLED = 1
    USER_LIST_LICENSE_STATUS_DISABLED = 2


__all__ = tuple(sorted(__protobuf__.manifest))
