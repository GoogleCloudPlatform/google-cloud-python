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
        "DealBuyerPermissionTypeEnum",
    },
)


class DealBuyerPermissionTypeEnum(proto.Message):
    r"""Wrapper message for
    [DealBuyerPermissionType][google.ads.admanager.v1.DealBuyerPermissionTypeEnum.DealBuyerPermissionType].

    """

    class DealBuyerPermissionType(proto.Enum):
        r"""Defines how a deal would transact among all buyers under the
        same bidder.

        Values:
            DEAL_BUYER_PERMISSION_TYPE_UNSPECIFIED (0):
                No value specified.
            NEGOTIATOR_ONLY (1):
                The deal only transacts with the buyer
                specified.
            BIDDER (2):
                The deal transacts with all buyers under the
                same bidder.
        """

        DEAL_BUYER_PERMISSION_TYPE_UNSPECIFIED = 0
        NEGOTIATOR_ONLY = 1
        BIDDER = 2


__all__ = tuple(sorted(__protobuf__.manifest))
