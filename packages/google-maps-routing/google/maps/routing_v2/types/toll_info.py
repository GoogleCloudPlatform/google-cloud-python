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
    package="google.maps.routing.v2",
    manifest={
        "TollInfo",
    },
)


class TollInfo(proto.Message):
    r"""Encapsulates toll information on a
    [``Route``][google.maps.routing.v2.Route] or on a
    [``RouteLeg``][google.maps.routing.v2.RouteLeg].

    Attributes:
        estimated_price (MutableSequence[google.type.money_pb2.Money]):
            The monetary amount of tolls for the corresponding
            [``Route``][google.maps.routing.v2.Route] or
            [``RouteLeg``][google.maps.routing.v2.RouteLeg]. This list
            contains a money amount for each currency that is expected
            to be charged by the toll stations. Typically this list will
            contain only one item for routes with tolls in one currency.
            For international trips, this list may contain multiple
            items to reflect tolls in different currencies.
    """

    estimated_price: MutableSequence[money_pb2.Money] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=money_pb2.Money,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
