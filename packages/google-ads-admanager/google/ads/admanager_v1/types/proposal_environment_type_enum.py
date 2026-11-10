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
        "ProposalEnvironmentTypeEnum",
    },
)


class ProposalEnvironmentTypeEnum(proto.Message):
    r"""Wrapper message for
    [ProposalEnvironmentType][google.ads.admanager.v1.ProposalEnvironmentTypeEnum.ProposalEnvironmentType]

    """

    class ProposalEnvironmentType(proto.Enum):
        r"""Identifies the format of inventory or "channel" in which ads
        serve.

        Values:
            PROPOSAL_ENVIRONMENT_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            DISPLAY (1):
                Ads serve in a browser.
            DISPLAY_OUTSTREAM_VIDEO (2):
                Out-stream video ads serve in a browser.
                Examples include in-feed and in-banner video
                ads.
            GAMES (3):
                In-stream video ads serve in a game.
            MOBILE (4):
                Ads serve in a mobile app.
            MOBILE_OUTSTREAM_VIDEO (5):
                Out-stream video ads serve in a mobile app.
            VIDEO (6):
                In-stream video ads serve in a video.
        """

        PROPOSAL_ENVIRONMENT_TYPE_UNSPECIFIED = 0
        DISPLAY = 1
        DISPLAY_OUTSTREAM_VIDEO = 2
        GAMES = 3
        MOBILE = 4
        MOBILE_OUTSTREAM_VIDEO = 5
        VIDEO = 6


__all__ = tuple(sorted(__protobuf__.manifest))
