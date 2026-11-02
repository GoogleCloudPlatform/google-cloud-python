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
        "DiscountTypeEnum",
    },
)


class DiscountTypeEnum(proto.Message):
    r"""Wrapper message for
    [DiscountType][google.ads.admanager.v1.DiscountTypeEnum.DiscountType].

    """

    class DiscountType(proto.Enum):
        r"""Describes the possible discount types on the cost of booking
        a line item.

        Values:
            DISCOUNT_TYPE_UNSPECIFIED (0):
                No value specified
            ABSOLUTE_VALUE (1):
                An absolute value will be discounted from the
                line item's cost.
            PERCENTAGE (2):
                A percentage of the cost will be discounted
                for booking the line item.
        """

        DISCOUNT_TYPE_UNSPECIFIED = 0
        ABSOLUTE_VALUE = 1
        PERCENTAGE = 2


__all__ = tuple(sorted(__protobuf__.manifest))
