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

import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import proto  # type: ignore

from google.ads.admanager_v1.types import ad_spot_targeting_type_enum, line_item_enums

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "AdSpot",
    },
)


class AdSpot(proto.Message):
    r"""An AdSpot is a targetable entity used in the creation of
    AdRule objects. A ad spot contains a variable number of ads and
    has constraints (ad duration, reservation type, etc) on the ads
    that can appear in it.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the ``AdSpot``. Format:
            ``networks/{network_code}/adSpots/{ad_spot_id}``
        canonical_display_name (str):
            Optional. Name of the AdSpot. The name is case insensitive
            and can be referenced in ad tags. This value is required if
            ``customSpot`` is true, and cannot be set otherwise. You can
            use alphanumeric characters and symbols other than the
            following: ", ', =, !, +, #, , ~, ;, ^, (, ), <, >, [, ],
            the white space character.

            This field is a member of `oneof`_ ``_canonical_display_name``.
        display_name (str):
            Optional. Descriptive name for the ``AdSpot``.This value is
            optional if ``customSpot`` is true, and cannot be set
            otherwise.

            This field is a member of `oneof`_ ``_display_name``.
        custom_spot (bool):
            Optional. Whether this ad spot is a custom
            spot. This field is optional and defaults to
            false. Custom spots can be reused and targeted
            in the targeting picker.

            This field is a member of `oneof`_ ``_custom_spot``.
        flexible (bool):
            Optional. Whether this ad spot is a flexible
            spot. This field is optional and defaults to
            false. Flexible spots are allowed to have no max
            number of ads.

            This field is a member of `oneof`_ ``_flexible``.
        max_duration (google.protobuf.duration_pb2.Duration):
            Optional. The maximum total duration for this
            AdSpot. This field is optional, defaults to 0,
            and supports precision to the nearest second.

            This field is a member of `oneof`_ ``_max_duration``.
        min_ad_duration (google.protobuf.duration_pb2.Duration):
            Optional. The minimum allowed duration for
            ads in the AdSpot. This field is optional and
            defaults to 0.

            This field is a member of `oneof`_ ``_min_ad_duration``.
        max_ad_duration (google.protobuf.duration_pb2.Duration):
            Required. The maximum allowed duration for ads in the
            ``AdSpot``. This field is required and must be greater than
            [minAdDuration][google.ads.admanager.v1.AdSpot.min_ad_duration].

            This field is a member of `oneof`_ ``_max_ad_duration``.
        max_ads (int):
            Optional. The maximum number of ads allowed
            in the AdSpot. This field is optional and
            defaults to 0. A value of 0 means that there is
            no maximum for the number of ads in the ad spot.
            No max ads is only supported for ad spots that
            have flexible set to true.

            This field is a member of `oneof`_ ``_max_ads``.
        targeting_type (google.ads.admanager_v1.types.AdSpotTargetingTypeEnum.AdSpotTargetingType):
            Optional. The AdSpot TargetingType determines
            how this ad spot can be targeted. This field is
            required.

            This field is a member of `oneof`_ ``_targeting_type``.
        backfill_blocked (bool):
            Optional. Whether backfill is blocked in this
            ad spot. This field is optional and defaults to
            false.

            This field is a member of `oneof`_ ``_backfill_blocked``.
        allowed_line_item_types (MutableSequence[google.ads.admanager_v1.types.LineItemTypeEnum.LineItemType]):
            Optional. The set of line item types that may appear in the
            ad spot. This field is optional and defaults to an empty
            set, which means that all types are allowed. Note, backfill
            reservation types are controlled by the ``backfillBlocked``
            field.
        inventory_sharing_blocked (bool):
            Optional. Whether inventory sharing is
            blocked in this ad spot. This field is optional
            and defaults to false.

            This field is a member of `oneof`_ ``_inventory_sharing_blocked``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    canonical_display_name: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    custom_spot: bool = proto.Field(
        proto.BOOL,
        number=4,
        optional=True,
    )
    flexible: bool = proto.Field(
        proto.BOOL,
        number=5,
        optional=True,
    )
    max_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=6,
        optional=True,
        message=duration_pb2.Duration,
    )
    min_ad_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=12,
        optional=True,
        message=duration_pb2.Duration,
    )
    max_ad_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=13,
        optional=True,
        message=duration_pb2.Duration,
    )
    max_ads: int = proto.Field(
        proto.INT32,
        number=7,
        optional=True,
    )
    targeting_type: ad_spot_targeting_type_enum.AdSpotTargetingTypeEnum.AdSpotTargetingType = proto.Field(
        proto.ENUM,
        number=8,
        optional=True,
        enum=ad_spot_targeting_type_enum.AdSpotTargetingTypeEnum.AdSpotTargetingType,
    )
    backfill_blocked: bool = proto.Field(
        proto.BOOL,
        number=9,
        optional=True,
    )
    allowed_line_item_types: MutableSequence[
        line_item_enums.LineItemTypeEnum.LineItemType
    ] = proto.RepeatedField(
        proto.ENUM,
        number=10,
        enum=line_item_enums.LineItemTypeEnum.LineItemType,
    )
    inventory_sharing_blocked: bool = proto.Field(
        proto.BOOL,
        number=11,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
