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
        "AdBreakStateEnum",
    },
)


class AdBreakStateEnum(proto.Message):
    r"""Wrapper message for
    [AdBreakState][google.ads.admanager.v1.AdBreakStateEnum.AdBreakState]

    """

    class AdBreakState(proto.Enum):
        r"""Represents the state of an ad break

        Values:
            AD_BREAK_STATE_UNSPECIFIED (0):
                Default value. This value is unused.
            DECISIONED (1):
                The ad break's decisioning has finished. You
                can delete, but not update the ad break.
            COMPLETE (2):
                The ad break has started serving to users.
                You cannot delete or update the ad break.
            SCHEDULED (3):
                The ad break is scheduled and decisioning
                will start later. You can delete or update the
                ad break.
        """

        AD_BREAK_STATE_UNSPECIFIED = 0
        DECISIONED = 1
        COMPLETE = 2
        SCHEDULED = 3


__all__ = tuple(sorted(__protobuf__.manifest))
