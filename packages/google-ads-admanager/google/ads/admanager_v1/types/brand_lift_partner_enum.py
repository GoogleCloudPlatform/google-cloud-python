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
        "BrandLiftPartnerEnum",
    },
)


class BrandLiftPartnerEnum(proto.Message):
    r"""Wrapper message for
    [BrandLiftPartner][google.ads.admanager.v1.BrandLiftPartnerEnum.BrandLiftPartner]

    """

    class BrandLiftPartner(proto.Enum):
        r"""Possible options for brand lift.

        Values:
            BRAND_LIFT_PARTNER_UNSPECIFIED (0):
                Default value. This value is unused.
            DYNATA (1):
                Indicates brand lift partner Dynata.
            INTAGE (3):
                Indicates brand lift partner Intage.
            KANTAR_MILLWARD_BROWN (4):
                Indicates brand lift partner Kantar.
            MACROMILL (5):
                Indicates brand lift partner Macromill.
            NONE (7):
                Indicates there's no brand lift partner.
        """

        BRAND_LIFT_PARTNER_UNSPECIFIED = 0
        DYNATA = 1
        INTAGE = 3
        KANTAR_MILLWARD_BROWN = 4
        MACROMILL = 5
        NONE = 7


__all__ = tuple(sorted(__protobuf__.manifest))
