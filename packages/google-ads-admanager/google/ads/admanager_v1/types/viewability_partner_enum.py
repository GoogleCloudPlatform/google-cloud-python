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
        "ViewabilityPartnerEnum",
    },
)


class ViewabilityPartnerEnum(proto.Message):
    r"""Wrapper message for
    [ViewabilityPartner][google.ads.admanager.v1.ViewabilityPartnerEnum.ViewabilityPartner]

    """

    class ViewabilityPartner(proto.Enum):
        r"""Possible options for viewabitility.
        The enum may receive new values in the future.

        Values:
            VIEWABILITY_PARTNER_UNSPECIFIED (0):
                Default value. This value is unused.
            COMSCORE (1):
                Indicates viewability partner Comscore.
            DOUBLE_VERIFY (2):
                Indicates viewability partner Double Verify.
            INTEGRAL_AD_SCIENCE (4):
                Indicates viewability partner Integral Ad
                Science.
            MOAT (5):
                Indicates viewability partner Oracle Moat.
            NONE (6):
                Indicates there's no viewability partner.
            TELEMETRY (7):
                Indicates viewability partner Telemetry.
        """

        VIEWABILITY_PARTNER_UNSPECIFIED = 0
        COMSCORE = 1
        DOUBLE_VERIFY = 2
        INTEGRAL_AD_SCIENCE = 4
        MOAT = 5
        NONE = 6
        TELEMETRY = 7


__all__ = tuple(sorted(__protobuf__.manifest))
