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

from google.ads.admanager_v1.types import discount_type_enum

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "LineItemDiscount",
    },
)


class LineItemDiscount(proto.Message):
    r"""Discount information for a
    [LineItem][google.ads.admanager.v1.LineItem].


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        discount_type (google.ads.admanager_v1.types.DiscountTypeEnum.DiscountType):
            Optional. The type of discount being applied to a
            [LineItem][google.ads.admanager.v1.LineItem], either
            percentage based or absolute. This attribute is optional and
            defaults to
            [PERCENTAGE][google.ads.admanager.v1.DiscountTypeEnum.DiscountType.PERCENTAGE].

            This field is a member of `oneof`_ ``_discount_type``.
        discount (float):
            Optional. The number here is either a percentage or an
            absolute value depending on the
            [DiscountType][google.ads.admanager.v1.DiscountTypeEnum.DiscountType].
            If the
            [DiscountType][google.ads.admanager.v1.DiscountTypeEnum.DiscountType]
            is
            [PERCENTAGE][google.ads.admanager.v1.DiscountTypeEnum.DiscountType.PERCENTAGE],
            then only non-fractional values are supported.

            This field is a member of `oneof`_ ``_discount``.
    """

    discount_type: discount_type_enum.DiscountTypeEnum.DiscountType = proto.Field(
        proto.ENUM,
        number=1,
        optional=True,
        enum=discount_type_enum.DiscountTypeEnum.DiscountType,
    )
    discount: float = proto.Field(
        proto.DOUBLE,
        number=2,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
