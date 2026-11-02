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
        "ExchangeSyndicationProductEnum",
    },
)


class ExchangeSyndicationProductEnum(proto.Message):
    r"""Wrapper message for
    [ExchangeSyndicationProduct][google.ads.admanager.v1.ExchangeSyndicationProductEnum.ExchangeSyndicationProduct]

    """

    class ExchangeSyndicationProduct(proto.Enum):
        r"""Ad Exchange syndication product.

        Values:
            EXCHANGE_SYNDICATION_PRODUCT_UNSPECIFIED (0):
                No value specified
            DISPLAY (1):
                Property serves in-browser.
            MOBILE_APP (2):
                Property serves on mobile applications
                (includes JS and SDK).
            VIDEO_AND_AUDIO (3):
                Property serves video (includes audio).
            GAMES (4):
                Property serves for games.
        """

        EXCHANGE_SYNDICATION_PRODUCT_UNSPECIFIED = 0
        DISPLAY = 1
        MOBILE_APP = 2
        VIDEO_AND_AUDIO = 3
        GAMES = 4


__all__ = tuple(sorted(__protobuf__.manifest))
