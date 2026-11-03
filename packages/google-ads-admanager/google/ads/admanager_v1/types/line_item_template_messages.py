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

from google.ads.admanager_v1.types import delivery_enums, line_item_enums

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "LineItemTemplate",
    },
)


class LineItemTemplate(proto.Message):
    r"""The LineItemTemplate resource.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the LineItemTemplate.
            Format:
            ``networks/{network_code}/lineItemTemplates/{line_item_template_id}``
        display_name (str):
            Required. Display name of the
            LineItemTemplate. This attribute has a maximum
            length of 255 characters.

            This field is a member of `oneof`_ ``_display_name``.
        default_template (bool):
            Output only. Whether or not the LineItemTemplate represents
            the default choices for creating a
            [LineItem][google.ads.admanager.v1.LineItem]. Only one
            default LineItemTemplate is allowed per
            [Network][google.ads.admanager.v1.Network].

            This field is a member of `oneof`_ ``_default_template``.
        same_advertiser_exception_enabled (bool):
            Optional. The default value for
            [same_advertiser_exception_enabled][google.ads.admanager.v1.LineItem.same_advertiser_exception_enabled]
            of a new [LineItem][google.ads.admanager.v1.LineItem].

            This field is a member of `oneof`_ ``_same_advertiser_exception_enabled``.
        line_item_display_name (str):
            Optional. The default
            [display_name][google.ads.admanager.v1.LineItem.display_name]
            of a new [LineItem][google.ads.admanager.v1.LineItem]. This
            attribute has a maximum length of 127 characters.

            This field is a member of `oneof`_ ``_line_item_display_name``.
        line_item_type (google.ads.admanager_v1.types.LineItemTypeEnum.LineItemType):
            Required. The default
            [line_item_type][google.ads.admanager.v1.LineItem.line_item_type]
            of a new [LineItem][google.ads.admanager.v1.LineItem].

            This field is a member of `oneof`_ ``_line_item_type``.
        notes (str):
            Optional. The default
            [notes][google.ads.admanager.v1.LineItem.notes] of a new
            [LineItem][google.ads.admanager.v1.LineItem]. This attribute
            has a maximum length of 65,535 characters.

            This field is a member of `oneof`_ ``_notes``.
        delivery_rate_type (google.ads.admanager_v1.types.LineItemDeliveryRateTypeEnum.LineItemDeliveryRateType):
            Required. The default
            [delivery_rate_type][google.ads.admanager.v1.LineItem.delivery_rate_type]
            of a new [LineItem][google.ads.admanager.v1.LineItem].

            This field is a member of `oneof`_ ``_delivery_rate_type``.
        roadblocking_type (google.ads.admanager_v1.types.RoadblockingTypeEnum.RoadblockingType):
            Required. The default
            [roadblocking_type][google.ads.admanager.v1.LineItem.roadblocking_type]
            of a new [LineItem][google.ads.admanager.v1.LineItem].

            This field is a member of `oneof`_ ``_roadblocking_type``.
        creative_rotation_type (google.ads.admanager_v1.types.CreativeRotationTypeEnum.CreativeRotationType):
            Required. The default
            [creative_rotation_type][google.ads.admanager.v1.LineItem.creative_rotation_type]
            of a new [LineItem][google.ads.admanager.v1.LineItem].

            This field is a member of `oneof`_ ``_creative_rotation_type``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    default_template: bool = proto.Field(
        proto.BOOL,
        number=3,
        optional=True,
    )
    same_advertiser_exception_enabled: bool = proto.Field(
        proto.BOOL,
        number=4,
        optional=True,
    )
    line_item_display_name: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    line_item_type: line_item_enums.LineItemTypeEnum.LineItemType = proto.Field(
        proto.ENUM,
        number=6,
        optional=True,
        enum=line_item_enums.LineItemTypeEnum.LineItemType,
    )
    notes: str = proto.Field(
        proto.STRING,
        number=7,
        optional=True,
    )
    delivery_rate_type: delivery_enums.LineItemDeliveryRateTypeEnum.LineItemDeliveryRateType = proto.Field(
        proto.ENUM,
        number=8,
        optional=True,
        enum=delivery_enums.LineItemDeliveryRateTypeEnum.LineItemDeliveryRateType,
    )
    roadblocking_type: delivery_enums.RoadblockingTypeEnum.RoadblockingType = (
        proto.Field(
            proto.ENUM,
            number=9,
            optional=True,
            enum=delivery_enums.RoadblockingTypeEnum.RoadblockingType,
        )
    )
    creative_rotation_type: delivery_enums.CreativeRotationTypeEnum.CreativeRotationType = proto.Field(
        proto.ENUM,
        number=10,
        optional=True,
        enum=delivery_enums.CreativeRotationTypeEnum.CreativeRotationType,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
