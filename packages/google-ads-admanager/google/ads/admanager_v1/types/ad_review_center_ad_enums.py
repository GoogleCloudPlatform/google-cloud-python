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
        "AdReviewCenterAdStatusEnum",
        "ManualAdReviewCenterAdStatusEnum",
        "ArcCreativeFormatEnum",
    },
)


class AdReviewCenterAdStatusEnum(proto.Message):
    r"""Wrapper message for
    [AdReviewCenterAdStatus][google.ads.admanager.v1.AdReviewCenterAdStatusEnum.AdReviewCenterAdStatus]

    """

    class AdReviewCenterAdStatus(proto.Enum):
        r"""Specifies the status of an AdReviewCenterAd.

        Values:
            AD_REVIEW_CENTER_AD_STATUS_UNSPECIFIED (0):
                Not specified value
            ALLOWED (1):
                This ad has been explicitly allowed to serve.
            BLOCKED (2):
                This ad has been explicitly blocked from
                serving.
            UNREVIEWED (3):
                This ad is allowed to serve by default and
                has not been reviewed.
        """

        AD_REVIEW_CENTER_AD_STATUS_UNSPECIFIED = 0
        ALLOWED = 1
        BLOCKED = 2
        UNREVIEWED = 3


class ManualAdReviewCenterAdStatusEnum(proto.Message):
    r"""Wrapper message for
    [ManualAdReviewCenterAdStatus][google.ads.admanager.v1.ManualAdReviewCenterAdStatusEnum.ManualAdReviewCenterAdStatus]

    """

    class ManualAdReviewCenterAdStatus(proto.Enum):
        r"""Specifies the manual review status of a AdReviewCenterAd.

        Values:
            MANUAL_AD_REVIEW_CENTER_AD_STATUS_UNSPECIFIED (0):
                Not specified value.
            ALLOWED (1):
                This ad has been explicitly allowed to serve.
            BLOCKED (2):
                This ad has been explicitly blocked from
                serving.
            ARCHIVED (3):
                This ad is implicitly blocked and has been
                reviewed.
            PENDING (4):
                This ad is implicitly blocked and has not
                been reviewed.
            SERVING (5):
                This ad is allowed to serve by default and
                has not been reviewed.
        """

        MANUAL_AD_REVIEW_CENTER_AD_STATUS_UNSPECIFIED = 0
        ALLOWED = 1
        BLOCKED = 2
        ARCHIVED = 3
        PENDING = 4
        SERVING = 5


class ArcCreativeFormatEnum(proto.Message):
    r"""Wrapper message for
    [ArcCreativeFormat][google.ads.admanager.v1.ArcCreativeFormatEnum.ArcCreativeFormat]

    Message representing the ad review center creative formats which is
    about how the creative is rendered for the end user.

    """

    class ArcCreativeFormat(proto.Enum):
        r"""Specifies the status of an ArcCreativeFormat.

        New values may be added in the future.

        Values:
            ARC_CREATIVE_FORMAT_UNSPECIFIED (0):
                Not specified value
            TEXT (1):
                Text based creatives.
            IMAGE (2):
                Image creatives.
            VIDEO (3):
                Video creatives.
            AUDIO (4):
                Audio creatives.
            APP_INSTALLS (5):
                Creatives leading to mobile app stores.
            RICH_MEDIA (6):
                Creatives leading to rich media.
        """

        ARC_CREATIVE_FORMAT_UNSPECIFIED = 0
        TEXT = 1
        IMAGE = 2
        VIDEO = 3
        AUDIO = 4
        APP_INSTALLS = 5
        RICH_MEDIA = 6


__all__ = tuple(sorted(__protobuf__.manifest))
