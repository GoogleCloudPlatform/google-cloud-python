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
        "DeliveryIndicator",
    },
)


class DeliveryIndicator(proto.Message):
    r"""Indicates the delivery performance of the LineItem.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        expected_delivery_percentage (float):
            Output only. The expected delivery percentage
            of the LineItem.

            This field is a member of `oneof`_ ``_expected_delivery_percentage``.
        actual_delivery_percentage (float):
            Output only. The actual delivery percentage
            of the LineItem.

            This field is a member of `oneof`_ ``_actual_delivery_percentage``.
    """

    expected_delivery_percentage: float = proto.Field(
        proto.DOUBLE,
        number=1,
        optional=True,
    )
    actual_delivery_percentage: float = proto.Field(
        proto.DOUBLE,
        number=2,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
