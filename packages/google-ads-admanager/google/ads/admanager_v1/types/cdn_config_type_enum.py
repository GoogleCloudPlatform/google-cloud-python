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
        "CdnConfigTypeEnum",
    },
)


class CdnConfigTypeEnum(proto.Message):
    r"""Wrapper message for
    [CdnConfigType][google.ads.admanager.v1.CdnConfigTypeEnum.CdnConfigType]

    """

    class CdnConfigType(proto.Enum):
        r"""Indicates the type of CDN configuration for CdnConfiguration.

        Values:
            CDN_CONFIG_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            AD_MEDIA_DELIVERY (1):
                A configuration that specifies a
                publisher-provided CDN for delivering ad media.
            LIVE_STREAM_SOURCE_CONTENT (2):
                A configuration that specifies where and how
                ``LiveStreamEvent`` content should be ingested and
                delivered.
            MIDROLL (3):
                A configuration that specifies where and how
                split content should be uploaded and delivered.
            VOD_SOURCE_CONTENT (4):
                A configuration that specifies where and how
                video on demand content should be ingested and
                delivered.
        """

        CDN_CONFIG_TYPE_UNSPECIFIED = 0
        AD_MEDIA_DELIVERY = 1
        LIVE_STREAM_SOURCE_CONTENT = 2
        MIDROLL = 3
        VOD_SOURCE_CONTENT = 4


__all__ = tuple(sorted(__protobuf__.manifest))
