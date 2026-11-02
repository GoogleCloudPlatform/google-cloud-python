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
        "AdUnitStatusEnum",
        "SmartSizeModeEnum",
        "TargetWindowEnum",
        "RefreshRateTypeEnum",
    },
)


class AdUnitStatusEnum(proto.Message):
    r"""Wrapper message for
    [AdUnitStatus][google.ads.admanager.v1.AdUnitStatusEnum.AdUnitStatus]

    """

    class AdUnitStatus(proto.Enum):
        r"""The status of an AdUnit.

        Values:
            AD_UNIT_STATUS_UNSPECIFIED (0):
                Default value. This value is unused.
            ACTIVE (1):
                The ad unit is active, available for
                targeting, and serving.
            INACTIVE (2):
                The ad unit will be visible in the UI, but
                ignored by serving.
            ARCHIVED (3):
                The ad unit will be hidden in the UI and
                ignored by serving.
        """

        AD_UNIT_STATUS_UNSPECIFIED = 0
        ACTIVE = 1
        INACTIVE = 2
        ARCHIVED = 3


class SmartSizeModeEnum(proto.Message):
    r"""Wrapper message for
    [SmartSizeMode][google.ads.admanager.v1.SmartSizeModeEnum.SmartSizeMode].

    """

    class SmartSizeMode(proto.Enum):
        r"""The smart size mode for this ad unit. This attribute is
        optional and defaults to SmartSizeMode.NONE for fixed sizes.

        Values:
            SMART_SIZE_MODE_UNSPECIFIED (0):
                Default value. This value is unused.
            NONE (1):
                Fixed size mode (default).
            SMART_BANNER (2):
                The height is fixed for the request, the
                width is a range.
            DYNAMIC_SIZE (3):
                Height and width are ranges.
        """

        SMART_SIZE_MODE_UNSPECIFIED = 0
        NONE = 1
        SMART_BANNER = 2
        DYNAMIC_SIZE = 3


class TargetWindowEnum(proto.Message):
    r"""Wrapper message for
    [TargetWindow][google.ads.admanager.v1.TargetWindowEnum.TargetWindow].

    """

    class TargetWindow(proto.Enum):
        r"""Corresponds to an HTML link's target attribute.
        See http://www.w3.org/TR/html401/present/frames.html#adef-target

        Values:
            TARGET_WINDOW_UNSPECIFIED (0):
                Default value. This value is unused.
            TOP (1):
                Specifies that the link should open in the
                full body of the page.
            BLANK (2):
                Specifies that the link should open in a new
                window.
        """

        TARGET_WINDOW_UNSPECIFIED = 0
        TOP = 1
        BLANK = 2


class RefreshRateTypeEnum(proto.Message):
    r"""Wrapper message for
    [RefreshRateType][google.ads.admanager.v1.RefreshRateTypeEnum.RefreshRateType]

    """

    class RefreshRateType(proto.Enum):
        r"""Represents the refresh rate control type for an ad unit.
        New values may be added in the future.

        Values:
            REFRESH_RATE_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            DISABLED (1):
                Indicates refresh is disabled.
            OPTIMIZED (2):
                Represents the Google optimized refresh rate.
            FIXED_INTERVAL (3):
                Represents a fixed interval refresh rate.
        """

        REFRESH_RATE_TYPE_UNSPECIFIED = 0
        DISABLED = 1
        OPTIMIZED = 2
        FIXED_INTERVAL = 3


__all__ = tuple(sorted(__protobuf__.manifest))
