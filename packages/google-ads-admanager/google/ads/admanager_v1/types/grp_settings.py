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
    grp_provider_enum,
    grp_target_gender_enum,
    nielsen_ctv_pacing_enum,
    pacing_device_categorization_enum,
)

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "GrpSettings",
    },
)


class GrpSettings(proto.Message):
    r"""GrpSettings contains information for a line item that will
    have a target demographic when serving. This information will be
    used to set up tracking and enable reporting on the demographic
    information.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        min_target_age (int):
            Optional. Specifies the minimum target age (in years) of the
            LineItem. This field is only applicable if
            [provider][google.ads.admanager.v1.GrpSettings.provider] is
            not null.

            This field is a member of `oneof`_ ``_min_target_age``.
        max_target_age (int):
            Optional. Specifies the maximum target age (in years) of the
            LineItem. This field is only applicable if
            [provider][google.ads.admanager.v1.GrpSettings.provider] is
            not null.

            This field is a member of `oneof`_ ``_max_target_age``.
        target_gender (google.ads.admanager_v1.types.GrpTargetGenderEnum.GrpTargetGender):
            Optional. Specifies the target gender of the LineItem. This
            field is only applicable if
            [provider][google.ads.admanager.v1.GrpSettings.provider] is
            not null.

            This field is a member of `oneof`_ ``_target_gender``.
        provider (google.ads.admanager_v1.types.GrpProviderEnum.GrpProvider):
            Optional. Specifies the GRP provider of the
            LineItem.

            This field is a member of `oneof`_ ``_provider``.
        in_target_ratio_estimate_milli_percent (int):
            Optional. Estimate for the in-target ratio given the line
            item's audience targeting. This field is only applicable if
            [provider][google.ads.admanager.v1.GrpSettings.provider] is
            Nielsen,
            [Goal.unitType][google.ads.admanager.v1.Goal.unit_type] is
            in-target impressions, and
            [LineItemCostTypeEnum.LineItemCostType][google.ads.admanager.v1.LineItemCostTypeEnum.LineItemCostType]
            is in-target CPM. This field determines the in-target ratio
            to use for pacing Nielsen line items before Nielsen
            reporting data is available. Represented as a milli percent,
            so 55.7% becomes 55700.

            This field is a member of `oneof`_ ``_in_target_ratio_estimate_milli_percent``.
        nielsen_ctv_pacing_type (google.ads.admanager_v1.types.NielsenCtvPacingEnum.NielsenCtvPacing):
            Optional. Specifies which pacing computation
            to apply in pacing to impressions from connected
            devices.

            This field is a member of `oneof`_ ``_nielsen_ctv_pacing_type``.
        pacing_device_categorization_type (google.ads.admanager_v1.types.PacingDeviceCategorizationEnum.PacingDeviceCategorization):
            Optional. Specifies whether to use Google or
            Nielsen device breakdown in Nielsen Line Item
            auto pacing.

            This field is a member of `oneof`_ ``_pacing_device_categorization_type``.
        apply_true_coview (bool):
            Optional. Specifies whether to apply true coviewing in
            Nielsen Line Item auto pacing. This field can only be true
            if
            [nielsenCtvPacingType][google.ads.admanager.v1.GrpSettings.nielsen_ctv_pacing_type]
            is not NONE.

            This field is a member of `oneof`_ ``_apply_true_coview``.
    """

    min_target_age: int = proto.Field(
        proto.INT64,
        number=1,
        optional=True,
    )
    max_target_age: int = proto.Field(
        proto.INT64,
        number=2,
        optional=True,
    )
    target_gender: grp_target_gender_enum.GrpTargetGenderEnum.GrpTargetGender = (
        proto.Field(
            proto.ENUM,
            number=3,
            optional=True,
            enum=grp_target_gender_enum.GrpTargetGenderEnum.GrpTargetGender,
        )
    )
    provider: grp_provider_enum.GrpProviderEnum.GrpProvider = proto.Field(
        proto.ENUM,
        number=4,
        optional=True,
        enum=grp_provider_enum.GrpProviderEnum.GrpProvider,
    )
    in_target_ratio_estimate_milli_percent: int = proto.Field(
        proto.INT64,
        number=6,
        optional=True,
    )
    nielsen_ctv_pacing_type: nielsen_ctv_pacing_enum.NielsenCtvPacingEnum.NielsenCtvPacing = proto.Field(
        proto.ENUM,
        number=8,
        optional=True,
        enum=nielsen_ctv_pacing_enum.NielsenCtvPacingEnum.NielsenCtvPacing,
    )
    pacing_device_categorization_type: pacing_device_categorization_enum.PacingDeviceCategorizationEnum.PacingDeviceCategorization = proto.Field(
        proto.ENUM,
        number=9,
        optional=True,
        enum=pacing_device_categorization_enum.PacingDeviceCategorizationEnum.PacingDeviceCategorization,
    )
    apply_true_coview: bool = proto.Field(
        proto.BOOL,
        number=10,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
