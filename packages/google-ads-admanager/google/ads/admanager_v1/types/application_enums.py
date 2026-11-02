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
        "ApplicationStoreEnum",
        "ApplicationApprovalStatusEnum",
        "ApplicationPlatformEnum",
        "WebviewClaimingStatusEnum",
    },
)


class ApplicationStoreEnum(proto.Message):
    r"""Wrapper message for
    [ApplicationStore][google.ads.admanager.v1.ApplicationStoreEnum.ApplicationStore].

    """

    class ApplicationStore(proto.Enum):
        r"""The application store that distributes applications.

        Values:
            APPLICATION_STORE_UNSPECIFIED (0):
                Not specified value.
            APPLE_APP_STORE (1):
                Apple App Store (iTunes).
            GOOGLE_PLAY_STORE (2):
                Google Play (ex. Google Market).
            AMAZON_APP_STORE (14):
                Amazon App Store.
            OPPO_APP_STORE (15):
                Oppo App Market.
            SAMSUNG_APP_STORE (16):
                Samsung Galaxy Store.
            VIVO_APP_STORE (17):
                Vivo App Store.
            XIAOMI_APP_STORE (18):
                Mi GetApps.
            AMAZON_FIRETV_STORE (7):
                Application store for Amazon Fire TV apps.
            LG_TV_STORE (19):
                Application store for LG TV apps.
            PLAYSTATION_STORE (8):
                Application store for Playstation apps.
            ROKU_STORE (6):
                Application store for Roku apps.
            SAMSUNG_TV_STORE (11):
                Application store for Samsung TV apps.
            XBOX_STORE (10):
                Application store for Xbox apps.
        """

        APPLICATION_STORE_UNSPECIFIED = 0
        APPLE_APP_STORE = 1
        GOOGLE_PLAY_STORE = 2
        AMAZON_APP_STORE = 14
        OPPO_APP_STORE = 15
        SAMSUNG_APP_STORE = 16
        VIVO_APP_STORE = 17
        XIAOMI_APP_STORE = 18
        AMAZON_FIRETV_STORE = 7
        LG_TV_STORE = 19
        PLAYSTATION_STORE = 8
        ROKU_STORE = 6
        SAMSUNG_TV_STORE = 11
        XBOX_STORE = 10


class ApplicationApprovalStatusEnum(proto.Message):
    r"""Wrapper message for
    [ApplicationApprovalStatus][google.ads.admanager.v1.ApplicationApprovalStatusEnum.ApplicationApprovalStatus]

    """

    class ApplicationApprovalStatus(proto.Enum):
        r"""The approval status of the application.

        Values:
            APPLICATION_APPROVAL_STATUS_UNSPECIFIED (0):
                Default value. This value is unused.
            APPEALING (1):
                The application is disapproved but has a
                pending review status, signaling an appeal.
            APPROVED (2):
                The application can serve ads.
            DISAPPROVED (3):
                The application failed approval checks and it
                cannot serve any ads.
            DRAFT (4):
                The application is not yet ready for review.
            UNCHECKED (5):
                The application has not yet been reviewed.
        """

        APPLICATION_APPROVAL_STATUS_UNSPECIFIED = 0
        APPEALING = 1
        APPROVED = 2
        DISAPPROVED = 3
        DRAFT = 4
        UNCHECKED = 5


class ApplicationPlatformEnum(proto.Message):
    r"""Wrapper message for
    [ApplicationPlatform][google.ads.admanager.v1.ApplicationPlatformEnum.ApplicationPlatform]

    """

    class ApplicationPlatform(proto.Enum):
        r"""A platform a Application can run on.

        Values:
            APPLICATION_PLATFORM_UNSPECIFIED (0):
                Default value. This value is unused.
            UNSUPPORTED (14):
                Platform for apps with platforms we don't
                support yet or don't have a representation for.
            AMAZON_TV (6):
                Platform for Amazon Fire TV compatible apps.
            ANDROID (1):
                Platform for Android compatible apps.
            IOS (2):
                Platform for IOS compatible apps.
            LG_TV (12):
                Platform for LG TV compatible apps.
            PLAYSTATION (7):
                Platform for Playstation compatible apps.
            ROKU (5):
                Platform for Roku compatible apps.
            SAMSUNG_TV (10):
                Platform for Samsung TV compatible apps.
            XBOX (9):
                Platform for Xbox compatible apps.
        """

        APPLICATION_PLATFORM_UNSPECIFIED = 0
        UNSUPPORTED = 14
        AMAZON_TV = 6
        ANDROID = 1
        IOS = 2
        LG_TV = 12
        PLAYSTATION = 7
        ROKU = 5
        SAMSUNG_TV = 10
        XBOX = 9


class WebviewClaimingStatusEnum(proto.Message):
    r"""Wrapper message for
    [WebviewClaimingStatus][google.ads.admanager.v1.WebviewClaimingStatusEnum.WebviewClaimingStatus]

    """

    class WebviewClaimingStatus(proto.Enum):
        r"""The webview claiming status of a Application.

        Values:
            WEBVIEW_CLAIMING_STATUS_UNSPECIFIED (0):
                Default value. This value is unused.
            SOFT_CLAIMED (1):
                The application is soft claimed (claimed for
                targeting, but not ownership).
            SOFT_CLAIMING_REVERTED (2):
                The application had its soft claiming status
                reverted (usually by a user action).
        """

        WEBVIEW_CLAIMING_STATUS_UNSPECIFIED = 0
        SOFT_CLAIMED = 1
        SOFT_CLAIMING_REVERTED = 2


__all__ = tuple(sorted(__protobuf__.manifest))
