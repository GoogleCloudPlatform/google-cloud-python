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
        "PrivateMarketplaceDealStatusEnum",
    },
)


class PrivateMarketplaceDealStatusEnum(proto.Message):
    r"""Wrapper message for
    [PrivateMarketplaceDealStatus][google.ads.admanager.v1.PrivateMarketplaceDealStatusEnum.PrivateMarketplaceDealStatus].

    """

    class PrivateMarketplaceDealStatus(proto.Enum):
        r"""Describes the status of a private marketplace deal.

        Values:
            PRIVATE_MARKETPLACE_DEAL_STATUS_UNSPECIFIED (0):
                No value specified.
            PENDING (1):
                The deal is pending.
            ACTIVE (2):
                The deal is active.
            CANCELED (3):
                The deal is canceled.
            SELLER_PAUSED (4):
                The deal is paused by the seller.
            BUYER_PAUSED (5):
                The deal is paused by the buyer.
            COMPLETED (6):
                The deal is past its end date.
        """

        PRIVATE_MARKETPLACE_DEAL_STATUS_UNSPECIFIED = 0
        PENDING = 1
        ACTIVE = 2
        CANCELED = 3
        SELLER_PAUSED = 4
        BUYER_PAUSED = 5
        COMPLETED = 6


__all__ = tuple(sorted(__protobuf__.manifest))
