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
        "SkippableAdTypeEnum",
    },
)


class SkippableAdTypeEnum(proto.Message):
    r"""Wrapper message for
    [SkippableAdType][google.ads.admanager.v1.SkippableAdTypeEnum.SkippableAdType]

    """

    class SkippableAdType(proto.Enum):
        r"""The different types of skippable ads.

        Values:
            SKIPPABLE_AD_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            ANY (1):
                Any skippable or not skippable. This is only
                for programmatic case when the creative
                skippability is decided by the buyside.
            DISABLED (2):
                The ad is not skippable.
            ENABLED (3):
                The ad is skippable.
            INSTREAM_SELECT (4):
                The ad is an instream select ad.
        """

        SKIPPABLE_AD_TYPE_UNSPECIFIED = 0
        ANY = 1
        DISABLED = 2
        ENABLED = 3
        INSTREAM_SELECT = 4


__all__ = tuple(sorted(__protobuf__.manifest))
