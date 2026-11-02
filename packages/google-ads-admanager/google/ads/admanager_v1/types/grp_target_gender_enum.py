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
        "GrpTargetGenderEnum",
    },
)


class GrpTargetGenderEnum(proto.Message):
    r"""Wrapper message for
    [GrpTargetGender][google.ads.admanager.v1.GrpTargetGenderEnum.GrpTargetGender]

    """

    class GrpTargetGender(proto.Enum):
        r"""Represents the target gender for a GRP demographic targeted
        line item.

        Values:
            GRP_TARGET_GENDER_UNSPECIFIED (0):
                Default value. This value is unused.
            BOTH (1):
                Indicates that the GRP target gender is both
                male and female.
            FEMALE (2):
                Indicates that the GRP target gender is
                Female.
            MALE (3):
                Indicates that the GRP target gender is Male.
        """

        GRP_TARGET_GENDER_UNSPECIFIED = 0
        BOTH = 1
        FEMALE = 2
        MALE = 3


__all__ = tuple(sorted(__protobuf__.manifest))
