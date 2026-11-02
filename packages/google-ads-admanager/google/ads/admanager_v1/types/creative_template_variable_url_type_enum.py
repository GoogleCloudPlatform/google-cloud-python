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
        "CreativeTemplateVariableUrlTypeEnum",
    },
)


class CreativeTemplateVariableUrlTypeEnum(proto.Message):
    r"""Wrapper message for
    [CreativeTemplateVariableUrlType][google.ads.admanager.v1.CreativeTemplateVariableUrlTypeEnum.CreativeTemplateVariableUrlType]

    """

    class CreativeTemplateVariableUrlType(proto.Enum):
        r"""Types of URLs that a UrlCreativeTemplateVariable can
        represent.

        Values:
            CREATIVE_TEMPLATE_VARIABLE_URL_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            CLICK_TRACKER (1):
                Click tracking URL.
            DEEPLINK (2):
                Deep-link URL.
            IMPRESSION_TRACKER (3):
                Impression tracking URL.
            STANDARD_HTTP (4):
                Standard HTTP URL.
        """

        CREATIVE_TEMPLATE_VARIABLE_URL_TYPE_UNSPECIFIED = 0
        CLICK_TRACKER = 1
        DEEPLINK = 2
        IMPRESSION_TRACKER = 3
        STANDARD_HTTP = 4


__all__ = tuple(sorted(__protobuf__.manifest))
