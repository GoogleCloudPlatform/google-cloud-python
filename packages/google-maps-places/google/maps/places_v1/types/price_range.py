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

import google.type.money_pb2 as money_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.maps.places.v1",
    manifest={
        "PriceRange",
    },
)


class PriceRange(proto.Message):
    r"""The price range associated with a Place. ``end_price`` could be
    unset, which indicates a range without upper bound (e.g. "More than
    $100").

    Attributes:
        start_price (google.type.money_pb2.Money):
            The low end of the price range (inclusive).
            Price should be at or above this amount.
        end_price (google.type.money_pb2.Money):
            The high end of the price range (exclusive).
            Price should be lower than this amount.
    """

    start_price: money_pb2.Money = proto.Field(
        proto.MESSAGE,
        number=1,
        message=money_pb2.Money,
    )
    end_price: money_pb2.Money = proto.Field(
        proto.MESSAGE,
        number=2,
        message=money_pb2.Money,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
