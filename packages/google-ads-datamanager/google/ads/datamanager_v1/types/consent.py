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
    package="google.ads.datamanager.v1",
    manifest={
        "ConsentStatus",
        "Consent",
    },
)


class ConsentStatus(proto.Enum):
    r"""Represents if the user granted, denied, or hasn't specified
    consent.

    Values:
        CONSENT_STATUS_UNSPECIFIED (0):
            Not specified.
        CONSENT_GRANTED (1):
            Granted.
        CONSENT_DENIED (2):
            Denied.
    """

    CONSENT_STATUS_UNSPECIFIED = 0
    CONSENT_GRANTED = 1
    CONSENT_DENIED = 2


class Consent(proto.Message):
    r"""`Digital Markets Act
    (DMA) <//digital-markets-act.ec.europa.eu/index_en>`__ consent
    settings for the user.

    Attributes:
        ad_user_data (google.ads.datamanager_v1.types.ConsentStatus):
            Optional. Represents if the user consents to
            ad user data.
        ad_personalization (google.ads.datamanager_v1.types.ConsentStatus):
            Optional. Represents if the user consents to
            ad personalization.
    """

    ad_user_data: "ConsentStatus" = proto.Field(
        proto.ENUM,
        number=1,
        enum="ConsentStatus",
    )
    ad_personalization: "ConsentStatus" = proto.Field(
        proto.ENUM,
        number=2,
        enum="ConsentStatus",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
