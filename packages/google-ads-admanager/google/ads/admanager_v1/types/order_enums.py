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
        "OrderStatusEnum",
    },
)


class OrderStatusEnum(proto.Message):
    r"""Wrapper message for
    [OrderStatus][google.ads.admanager.v1.OrderStatusEnum.OrderStatus].

    """

    class OrderStatus(proto.Enum):
        r"""The status of an Order.

        Values:
            ORDER_STATUS_UNSPECIFIED (0):
                Default value. This value is unused.
            DRAFT (2):
                Indicates that the Order has just been
                created but no approval has been requested yet.
            PENDING_APPROVAL (3):
                Indicates that a request for approval for the
                Order has been made.
            APPROVED (4):
                Indicates that the Order has been approved
                and is ready to serve.
            DISAPPROVED (5):
                Indicates that the Order has been disapproved
                and is not eligible to serve.
            PAUSED (6):
                This is a legacy state. Paused status should
                be checked on LineItems within the order.
            CANCELED (7):
                Indicates that the Order has been canceled
                and cannot serve.
            DELETED (8):
                Indicates that the Order has been deleted.
        """

        ORDER_STATUS_UNSPECIFIED = 0
        DRAFT = 2
        PENDING_APPROVAL = 3
        APPROVED = 4
        DISAPPROVED = 5
        PAUSED = 6
        CANCELED = 7
        DELETED = 8


__all__ = tuple(sorted(__protobuf__.manifest))
