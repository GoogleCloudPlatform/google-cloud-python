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

from google.ads.admanager_v1.types import (
    ad_break_optimization_type_enum,
    ad_rule_fill_order_direction_enum,
    ad_spot_fill_type_enum,
)

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "BreakTemplate",
        "BreakTemplateMember",
    },
)


class BreakTemplate(proto.Message):
    r"""A ``BreakTemplate`` defines what kinds of ads show at which
    positions within a pod. Break templates are made up of ``AdSpot``
    objects. A break template must have a single ad spot that has
    ``flexible`` set to ``true``.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the ``BreakTemplate``.
            Format:
            ``networks/{network_code}/breakTemplates/{break_template_id}``
        custom_template (bool):
            Optional. Whether this is a custom template.
            Custom templates get created outside of the ad
            rule workflow and can be referenced in ad tags.
            Only custom templates can have names and display
            names.

            This field is a member of `oneof`_ ``_custom_template``.
        ad_tag_name (str):
            Optional. Name of the ``BreakTemplate``. The name is case
            insensitive and can be referenced in ad tags. This value is
            required if ``customTemplate`` is true, and cannot be set
            otherwise. You can use alphanumeric characters and symbols
            other than the following: ", ', =, !, +, #, ,, ~, ;, ^, (,
            ), <, >, [, ], the white space character.

            This field is a member of `oneof`_ ``_ad_tag_name``.
        display_name (str):
            Optional. Descriptive name for the
            BreakTemplate. This value is optional if
            customTemplate is true, and cannot be set
            otherwise.

            This field is a member of `oneof`_ ``_display_name``.
        break_template_members (MutableSequence[google.ads.admanager_v1.types.BreakTemplateMember]):
            Optional. The list of the ``BreakTemplateMember`` objects in
            the order in which they should appear in the ad pod. Each
            ``BreakTemplateMember`` has a reference to an ``AdSpot``,
            which defines what kinds of ads can appear at that position,
            as well as other metadata that defines how each ad spot
            should be filled.
        ad_break_optimization_type (google.ads.admanager_v1.types.AdBreakOptimizationTypeEnum.AdBreakOptimizationType):
            Optional. The optimization type of the pod. This field is
            optional and defaults to
            [AdBreakOptimizationTypeEnum.AdBreakOptimizationType.REVENUE][google.ads.admanager.v1.AdBreakOptimizationTypeEnum.AdBreakOptimizationType.REVENUE].

            This field is a member of `oneof`_ ``_ad_break_optimization_type``.
        fill_order_direction_type (google.ads.admanager_v1.types.AdRuleFillOrderDirectionEnum.AdRuleFillOrderDirection):
            Optional. The fill order direction of the pod. This value is
            required if
            [adBreakOptimizationType][google.ads.admanager.v1.BreakTemplate.ad_break_optimization_type]
            is equal to
            [AdBreakOptimizationTypeEnum.AdBreakOptimizationType.POSITION][google.ads.admanager.v1.AdBreakOptimizationTypeEnum.AdBreakOptimizationType.POSITION]
            and should otherwise be unset.

            This field is a member of `oneof`_ ``_fill_order_direction_type``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    custom_template: bool = proto.Field(
        proto.BOOL,
        number=2,
        optional=True,
    )
    ad_tag_name: str = proto.Field(
        proto.STRING,
        number=8,
        optional=True,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    break_template_members: MutableSequence["BreakTemplateMember"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=5,
            message="BreakTemplateMember",
        )
    )
    ad_break_optimization_type: ad_break_optimization_type_enum.AdBreakOptimizationTypeEnum.AdBreakOptimizationType = proto.Field(
        proto.ENUM,
        number=6,
        optional=True,
        enum=ad_break_optimization_type_enum.AdBreakOptimizationTypeEnum.AdBreakOptimizationType,
    )
    fill_order_direction_type: ad_rule_fill_order_direction_enum.AdRuleFillOrderDirectionEnum.AdRuleFillOrderDirection = proto.Field(
        proto.ENUM,
        number=7,
        optional=True,
        enum=ad_rule_fill_order_direction_enum.AdRuleFillOrderDirectionEnum.AdRuleFillOrderDirection,
    )


class BreakTemplateMember(proto.Message):
    r"""A building block of a pod template.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        ad_spot (str):
            Required. The ID of the ``AdSpot`` that has the settings
            about what kinds of ads can appear in this position of the
            ``BreakTemplate``.

            This field is a member of `oneof`_ ``_ad_spot``.
        ad_spot_fill_type (google.ads.admanager_v1.types.AdSpotFillTypeEnum.AdSpotFillType):
            Optional. The behavior for how the ``AdSpot`` should be
            filled in the context of the ``BreakTemplate``.

            This field is a member of `oneof`_ ``_ad_spot_fill_type``.
    """

    ad_spot: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    ad_spot_fill_type: ad_spot_fill_type_enum.AdSpotFillTypeEnum.AdSpotFillType = (
        proto.Field(
            proto.ENUM,
            number=2,
            optional=True,
            enum=ad_spot_fill_type_enum.AdSpotFillTypeEnum.AdSpotFillType,
        )
    )


__all__ = tuple(sorted(__protobuf__.manifest))
