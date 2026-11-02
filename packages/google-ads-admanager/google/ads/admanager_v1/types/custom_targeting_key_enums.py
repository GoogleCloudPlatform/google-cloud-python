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
        "CustomTargetingKeyStatusEnum",
        "CustomTargetingKeyTypeEnum",
        "CustomTargetingKeyReportableTypeEnum",
    },
)


class CustomTargetingKeyStatusEnum(proto.Message):
    r"""Wrapper message for
    [CustomTargetingKeyStatus][google.ads.admanager.v1.CustomTargetingKeyStatusEnum.CustomTargetingKeyStatus]

    """

    class CustomTargetingKeyStatus(proto.Enum):
        r"""Status of the custom targeting key.

        Values:
            CUSTOM_TARGETING_KEY_STATUS_UNSPECIFIED (0):
                Not specified value.
            ACTIVE (1):
                Custom targeting key is active.
            INACTIVE (2):
                Custom targeting key is inactive.
        """

        CUSTOM_TARGETING_KEY_STATUS_UNSPECIFIED = 0
        ACTIVE = 1
        INACTIVE = 2


class CustomTargetingKeyTypeEnum(proto.Message):
    r"""Wrapper message for
    [CustomTargetingKeyType][google.ads.admanager.v1.CustomTargetingKeyTypeEnum.CustomTargetingKeyType]

    """

    class CustomTargetingKeyType(proto.Enum):
        r"""Type of the custom targeting key.

        Values:
            CUSTOM_TARGETING_KEY_TYPE_UNSPECIFIED (0):
                Not specified value.
            PREDEFINED (1):
                Key with a fixed set of values.
            FREEFORM (2):
                Key without a fixed set of values
        """

        CUSTOM_TARGETING_KEY_TYPE_UNSPECIFIED = 0
        PREDEFINED = 1
        FREEFORM = 2


class CustomTargetingKeyReportableTypeEnum(proto.Message):
    r"""Wrapper message for
    [CustomTargetingKeyReportableType][google.ads.admanager.v1.CustomTargetingKeyReportableTypeEnum.CustomTargetingKeyReportableType]

    """

    class CustomTargetingKeyReportableType(proto.Enum):
        r"""Reportable type of the custom targeting key.

        Values:
            CUSTOM_TARGETING_KEY_REPORTABLE_TYPE_UNSPECIFIED (0):
                Not specified value.
            OFF (1):
                Not available for reporting in the Ad Manager
                query tool.
            ON (2):
                Available for reporting in the Ad Manager
                query tool.
            CUSTOM_DIMENSION (3):
                Custom dimension available for reporting in
                the AdManager query tool.
        """

        CUSTOM_TARGETING_KEY_REPORTABLE_TYPE_UNSPECIFIED = 0
        OFF = 1
        ON = 2
        CUSTOM_DIMENSION = 3


__all__ = tuple(sorted(__protobuf__.manifest))
