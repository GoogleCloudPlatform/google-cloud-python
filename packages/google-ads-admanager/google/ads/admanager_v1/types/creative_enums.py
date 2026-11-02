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
        "CreativeLockedOrientationEnum",
        "CreativeDestinationUrlTypeEnum",
        "CreativeSslOverrideEnum",
        "CreativeSslScanResultEnum",
        "VastAdIdTypeEnum",
    },
)


class CreativeLockedOrientationEnum(proto.Message):
    r"""Wrapper message for
    [CreativeLockedOrientation][google.ads.admanager.v1.CreativeLockedOrientationEnum.CreativeLockedOrientation].

    """

    class CreativeLockedOrientation(proto.Enum):
        r"""Describes the orientation that a creative should be served
        with.

        Values:
            CREATIVE_LOCKED_ORIENTATION_UNSPECIFIED (0):
                Default value. This value is unused.
            LANDSCAPE (1):
                Landscape orientation.
            PORTRAIT (2):
                Portrait orientation.
            FREE (3):
                Free orientation.
        """

        CREATIVE_LOCKED_ORIENTATION_UNSPECIFIED = 0
        LANDSCAPE = 1
        PORTRAIT = 2
        FREE = 3


class CreativeDestinationUrlTypeEnum(proto.Message):
    r"""Wrapper message for
    [CreativeDestinationUrlType][google.ads.admanager.v1.CreativeDestinationUrlTypeEnum.CreativeDestinationUrlType]

    """

    class CreativeDestinationUrlType(proto.Enum):
        r"""The valid actions that a destination URL may perform if the
        user clicks on the ad.

        Values:
            CREATIVE_DESTINATION_URL_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            CLICK_TO_APP (1):
                Start an application.
            CLICK_TO_CALL (2):
                Make a phone call.
            CLICK_TO_WEB (3):
                Navigate to a web page. (a.k.a.
                "Click-through URL").
            NONE (4):
                Destination URL not present. Useful for video
                creatives where a landing page or a product
                isn't necessarily applicable.
        """

        CREATIVE_DESTINATION_URL_TYPE_UNSPECIFIED = 0
        CLICK_TO_APP = 1
        CLICK_TO_CALL = 2
        CLICK_TO_WEB = 3
        NONE = 4


class CreativeSslOverrideEnum(proto.Message):
    r"""Wrapper message for
    [CreativeSslOverride][google.ads.admanager.v1.CreativeSslOverrideEnum.CreativeSslOverride]

    """

    class CreativeSslOverride(proto.Enum):
        r"""Enum to store the creative SSL compatibility manual override.
        Its three states are similar to that of SslScanResult.

        Values:
            CREATIVE_SSL_OVERRIDE_UNSPECIFIED (0):
                Default value. This value is unused.
            NOT_SSL_COMPATIBLE (1):
                The creative is manually overridden to be
                SSL-incompatible.
            NO_OVERRIDE (2):
                The creative's SSL compatibility is
                determined by the scan result.
            SSL_COMPATIBLE (3):
                The creative is manually overridden to be
                SSL-compatible.
        """

        CREATIVE_SSL_OVERRIDE_UNSPECIFIED = 0
        NOT_SSL_COMPATIBLE = 1
        NO_OVERRIDE = 2
        SSL_COMPATIBLE = 3


class CreativeSslScanResultEnum(proto.Message):
    r"""Wrapper message for
    [CreativeSslScanResult][google.ads.admanager.v1.CreativeSslScanResultEnum.CreativeSslScanResult]

    """

    class CreativeSslScanResult(proto.Enum):
        r"""Enum to store the creative SSL compatibility scan result.

        Values:
            CREATIVE_SSL_SCAN_RESULT_UNSPECIFIED (0):
                Default value. This value is unused.
            SCANNED_NON_SSL (1):
                The creative was scanned and found to be
                SSL-incompatible.
            SCANNED_SSL (2):
                The creative was scanned and found to be
                SSL-compatible.
            UNSCANNED (3):
                The creative has not been scanned for SSL
                compatibility.
        """

        CREATIVE_SSL_SCAN_RESULT_UNSPECIFIED = 0
        SCANNED_NON_SSL = 1
        SCANNED_SSL = 2
        UNSCANNED = 3


class VastAdIdTypeEnum(proto.Message):
    r"""Wrapper message for
    [VastAdIdType][google.ads.admanager.v1.VastAdIdTypeEnum.VastAdIdType]

    """

    class VastAdIdType(proto.Enum):
        r"""The registry that an ad ID belongs to.

        Values:
            VAST_AD_ID_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            AD_ID (1):
                Ad ID.
            ARPP (2):
                The ad ID is registered with ARPP Pub-ID.
            CLEARCAST (3):
                The ad ID is registered with clearcast.co.uk.
            CUSV (4):
                The ad ID is registered with Auditel Spot ID.
            NONE (5):
                None.
        """

        VAST_AD_ID_TYPE_UNSPECIFIED = 0
        AD_ID = 1
        ARPP = 2
        CLEARCAST = 3
        CUSV = 4
        NONE = 5


__all__ = tuple(sorted(__protobuf__.manifest))
