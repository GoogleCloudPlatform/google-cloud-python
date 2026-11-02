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
        "LineItemDealInfo",
    },
)


class LineItemDealInfo(proto.Message):
    r"""Data transfer object for the exchange deal info of a line
    item.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        external_deal_id (int):
            Optional. The external deal ID shared between
            seller and buyer. This field is only present if
            the deal has been finalized.

            This field is a member of `oneof`_ ``_external_deal_id``.
    """

    external_deal_id: int = proto.Field(
        proto.INT64,
        number=2,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
