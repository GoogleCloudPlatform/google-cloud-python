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
        "YieldIntegrationTypeEnum",
        "YieldPartnerSettingStatusEnum",
        "YieldPlatformEnum",
        "YieldEntityStatusEnum",
    },
)


class YieldIntegrationTypeEnum(proto.Message):
    r"""Wrapper message for
    [YieldIntegrationType][google.ads.admanager.v1.YieldIntegrationTypeEnum.YieldIntegrationType]

    """

    class YieldIntegrationType(proto.Enum):
        r"""Represents the possible types of adapters a buyer can have.

        Values:
            YIELD_INTEGRATION_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            CUSTOM_EVENT_MEDIATION (1):
                Custom event mediation integration type
            OPEN_BIDDING (2):
                Open bidding integration type
            SDK_MEDIATION (3):
                SDK mediation integration type
            THIRD_PARTY_SDK_BIDDING (4):
                Third party SDK bidding integration type
        """

        YIELD_INTEGRATION_TYPE_UNSPECIFIED = 0
        CUSTOM_EVENT_MEDIATION = 1
        OPEN_BIDDING = 2
        SDK_MEDIATION = 3
        THIRD_PARTY_SDK_BIDDING = 4


class YieldPartnerSettingStatusEnum(proto.Message):
    r"""Wrapper message for
    [YieldPartnerSettingStatus][google.ads.admanager.v1.YieldPartnerSettingStatusEnum.YieldPartnerSettingStatus]

    """

    class YieldPartnerSettingStatus(proto.Enum):
        r"""Status of a partner setting, representing a partner
        capability.

        Values:
            YIELD_PARTNER_SETTING_STATUS_UNSPECIFIED (0):
                Default value. This value is unused.
            ACTIVE (1):
                Active setting
            DEPRECATED (2):
                Deprecated setting
        """

        YIELD_PARTNER_SETTING_STATUS_UNSPECIFIED = 0
        ACTIVE = 1
        DEPRECATED = 2


class YieldPlatformEnum(proto.Message):
    r"""Wrapper message for
    [YieldPlatform][google.ads.admanager.v1.YieldPlatformEnum.YieldPlatform]

    """

    class YieldPlatform(proto.Enum):
        r"""Represents possible platforms for a mediation ad source.

        Values:
            YIELD_PLATFORM_UNSPECIFIED (0):
                Default value. This value is unused.
            ANDROID (1):
                Android platform.
            IOS (2):
                iOS platform.
        """

        YIELD_PLATFORM_UNSPECIFIED = 0
        ANDROID = 1
        IOS = 2


class YieldEntityStatusEnum(proto.Message):
    r"""Wrapper message for
    [YieldEntityStatus][google.ads.admanager.v1.YieldEntityStatusEnum.YieldEntityStatus]

    """

    class YieldEntityStatus(proto.Enum):
        r"""Status of the yield group or ad source.

        Values:
            YIELD_ENTITY_STATUS_UNSPECIFIED (0):
                Default value. This value is unused.
            ACTIVE (1):
                Indicates that the associated object is
                currently eligible to serve.
            EXPERIMENTING (2):
                Indicates that the associated object is under
                experiment (only applicable to yield groups).
            INACTIVE (3):
                Indicates that the associated object is not
                currently eligible to serve.
            ARCHIVED (4):
                Indicates that the associated object is
                archived (deleted).
        """

        YIELD_ENTITY_STATUS_UNSPECIFIED = 0
        ACTIVE = 1
        EXPERIMENTING = 2
        INACTIVE = 3
        ARCHIVED = 4


__all__ = tuple(sorted(__protobuf__.manifest))
