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

from google.ads.admanager_v1.types import targeting as gaa_targeting
from google.ads.admanager_v1.types import targeting_preset_enums

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "TargetingPreset",
    },
)


class TargetingPreset(proto.Message):
    r"""User-defined preset targeting criteria.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the ``TargetingPreset``.
            Format:
            ``networks/{network_code}/targetingPresets/{targeting_preset_id}``
        display_name (str):
            Required. The name of the TargetingPreset.
            This attribute has a maximum length of 255
            characters.

            This field is a member of `oneof`_ ``_display_name``.
        targeting (google.ads.admanager_v1.types.Targeting):
            Required. Contains the targeting criteria for
            the TargetingPreset. If not provided, empty
            targeting will be used as a default.

            This field is a member of `oneof`_ ``_targeting``.
        status (google.ads.admanager_v1.types.TargetingPresetStatusEnum.TargetingPresetStatus):
            Output only. The status of the
            TargetingPreset.

            This field is a member of `oneof`_ ``_status``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    targeting: gaa_targeting.Targeting = proto.Field(
        proto.MESSAGE,
        number=4,
        optional=True,
        message=gaa_targeting.Targeting,
    )
    status: targeting_preset_enums.TargetingPresetStatusEnum.TargetingPresetStatus = (
        proto.Field(
            proto.ENUM,
            number=5,
            optional=True,
            enum=targeting_preset_enums.TargetingPresetStatusEnum.TargetingPresetStatus,
        )
    )


__all__ = tuple(sorted(__protobuf__.manifest))
