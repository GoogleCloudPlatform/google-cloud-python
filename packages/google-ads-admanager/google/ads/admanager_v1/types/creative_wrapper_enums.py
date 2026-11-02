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
        "CreativeWrapperTypeEnum",
        "CreativeWrapperStatusEnum",
        "CreativeWrapperOrderingEnum",
    },
)


class CreativeWrapperTypeEnum(proto.Message):
    r"""Wrapper message for
    [CreativeWrapperType][google.ads.admanager.v1.CreativeWrapperTypeEnum.CreativeWrapperType]

    """

    class CreativeWrapperType(proto.Enum):
        r"""The type of a CreativeWrapper which is specified on the
        CreativeWrapper.

        Values:
            CREATIVE_WRAPPER_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            HTML (1):
                HTML CreativeWrappers that include
                header/footer HTML snippets.
            VIDEO_TRACKING_URL (2):
                Video Tracking URL CreativeWrappers that
                include tracking URIs.
        """

        CREATIVE_WRAPPER_TYPE_UNSPECIFIED = 0
        HTML = 1
        VIDEO_TRACKING_URL = 2


class CreativeWrapperStatusEnum(proto.Message):
    r"""Wrapper message for
    [CreativeWrapperStatus][google.ads.admanager.v1.CreativeWrapperStatusEnum.CreativeWrapperStatus]

    """

    class CreativeWrapperStatus(proto.Enum):
        r"""Indicates whether the CreativeWrapper is active. HTML
        snippets are served to Creatives only when the CreativeWrapper
        is active.

        Values:
            CREATIVE_WRAPPER_STATUS_UNSPECIFIED (0):
                Default value. This value is unused.
            ACTIVE (1):
                The CreativeWrapper will be applied to served
                creatives.
            INACTIVE (2):
                The CreativeWrapper will not be applied to
                served creatives.
        """

        CREATIVE_WRAPPER_STATUS_UNSPECIFIED = 0
        ACTIVE = 1
        INACTIVE = 2


class CreativeWrapperOrderingEnum(proto.Message):
    r"""Wrapper message for
    [CreativeWrapperOrdering][google.ads.admanager.v1.CreativeWrapperOrderingEnum.CreativeWrapperOrdering]

    """

    class CreativeWrapperOrdering(proto.Enum):
        r"""Defines the order in which the header and footer HTML snippets will
        be wrapped around the served creative. INNER snippets will be
        wrapped first, followed by NO_PREFERENCE and finally OUTER. If the
        creative needs to be wrapped with more than one snippet with the
        same CreativeWrapperOrdering, then the order is unspecified.

        Values:
            CREATIVE_WRAPPER_ORDERING_UNSPECIFIED (0):
                Default value. This value is unused.
            INNER (1):
                Wrapping occurs as early as possible.
            NO_PREFERENCE (2):
                Wrapping occurs after ``INNER`` but before ``OUTER``
            OUTER (3):
                Wrapping occurs after both ``NO_PREFERENCE`` and ``INNER``
        """

        CREATIVE_WRAPPER_ORDERING_UNSPECIFIED = 0
        INNER = 1
        NO_PREFERENCE = 2
        OUTER = 3


__all__ = tuple(sorted(__protobuf__.manifest))
