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
        "UserListGlobalLicenseType",
    },
)


class UserListGlobalLicenseType(proto.Enum):
    r"""User list global license types.

    Values:
        USER_LIST_GLOBAL_LICENSE_TYPE_UNSPECIFIED (0):
            UNSPECIFIED.
        USER_LIST_GLOBAL_LICENSE_TYPE_RESELLER (1):
            Reseller license.
        USER_LIST_GLOBAL_LICENSE_TYPE_DATA_MART_SELL_SIDE (2):
            DataMart Sell Side license.
        USER_LIST_GLOBAL_LICENSE_TYPE_DATA_MART_BUY_SIDE (3):
            DataMart Buy Side license.
    """

    USER_LIST_GLOBAL_LICENSE_TYPE_UNSPECIFIED = 0
    USER_LIST_GLOBAL_LICENSE_TYPE_RESELLER = 1
    USER_LIST_GLOBAL_LICENSE_TYPE_DATA_MART_SELL_SIDE = 2
    USER_LIST_GLOBAL_LICENSE_TYPE_DATA_MART_BUY_SIDE = 3


__all__ = tuple(sorted(__protobuf__.manifest))
