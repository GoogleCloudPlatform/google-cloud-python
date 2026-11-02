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
        "ReachPartnerEnum",
    },
)


class ReachPartnerEnum(proto.Message):
    r"""Wrapper message for
    [ReachPartner][google.ads.admanager.v1.ReachPartnerEnum.ReachPartner]

    """

    class ReachPartner(proto.Enum):
        r"""Possible options for third-party reach integration.

        Values:
            REACH_PARTNER_UNSPECIFIED (0):
                Default value. This value is unused.
            AUDIENCE_PROJECT (1):
                Indicates third-party reach integration
                partner Audience Project
            COMSCORE (2):
                Indicates third-party reach integration
                partner Comscore.
            GEMIUS (3):
                Indicates third-party reach integration
                partner Gemius.
            ISPOT_TV (5):
                Indicates third-party reach integration
                partner iSpot.TV
            KANTAR_MILLWARD_BROWN (6):
                Indicates third-party reach integration
                partner Kantar.
            NIELSEN (7):
                Indicates third-party reach integration
                partner Nielsen.
            NONE (8):
                Indicates there's no third-party reach
                integration partner.
            VIDEO_AMP (9):
                Indicates third-party reach integration
                partner VideoAmp
            VIDEO_RESEARCH (10):
                Indicates third-party reach integration
                partner Video Research.
        """

        REACH_PARTNER_UNSPECIFIED = 0
        AUDIENCE_PROJECT = 1
        COMSCORE = 2
        GEMIUS = 3
        ISPOT_TV = 5
        KANTAR_MILLWARD_BROWN = 6
        NIELSEN = 7
        NONE = 8
        VIDEO_AMP = 9
        VIDEO_RESEARCH = 10


__all__ = tuple(sorted(__protobuf__.manifest))
