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
        "ConversionEventEnum",
    },
)


class ConversionEventEnum(proto.Message):
    r"""Wrapper message for
    [ConversionEvent][google.ads.admanager.v1.ConversionEventEnum.ConversionEvent]

    """

    class ConversionEvent(proto.Enum):
        r"""All possible tracking event types. Not all events are
        supported by every kind of creative.

        Values:
            CONVERSION_EVENT_UNSPECIFIED (0):
                Default value. This value is unused.
            ACCEPT_INVITATION (1):
                Corresponds to the ``acceptInvitation`` tracking event.
            CLICK_TRACKING (2):
                Corresponds to the ``Linear.VideoClicks.ClickTracking``
                node.
            CLOSE (3):
                Corresponds to the ``close`` tracking event.
            COLLAPSE (4):
                Corresponds to the ``collapse`` tracking event.
            COMPLETE (5):
                Corresponds to the ``complete`` tracking event.
            CREATIVE_VIEW (6):
                Corresponds to the ``creativeView`` tracking event.
            CUSTOM_CLICK (7):
                Corresponds to the ``Linear.VideoClicks.CustomClick`` node.
            ENGAGED_VIEW (8):
                An event that is fired after 30 seconds of
                viewing the video or when the video finished (if
                the video duration is less than 30 seconds).
                This event does not correspond to any VAST
                element and is implemented using an extension.
            EXPAND (9):
                Corresponds to the ``expand`` tracking event.
            FIRST_QUARTILE (10):
                Corresponds to the ``firstQuartile`` tracking event.
            FULLSCREEN (11):
                Corresponds to the ``fullscreen`` tracking event.
            FULLY_VIEWABLE_AUDIBLE_HALF_DURATION_IMPRESSION (12):
                Corresponds to the
                ``fullyViewableAudibleHalfDurationImpression`` tracking
                event.
            MEASURABLE_IMPRESSION (13):
                Corresponds to the ``measurableImpression`` tracking event.
            MIDPOINT (14):
                Corresponds to the ``midpoint`` tracking event.
            MUTE (15):
                Corresponds to the ``mute`` tracking event.
            PAUSE (16):
                Corresponds to the ``pause`` tracking event.
            RESUME (17):
                Corresponds to the ``resume`` tracking event.
            REWIND (18):
                Corresponds to the ``rewind`` tracking event.
            SKIPPED (19):
                An event that is fired when a video was
                skipped. This event does not correspond to any
                VAST element and is implemented using an
                extension.
            SKIP_SHOWN (20):
                An event that is fired when a video skip
                button is shown, usually after 5 seconds of
                viewing the video. This event does not
                correspond to any VAST element and is
                implemented using an extension.
            START (21):
                Corresponds to the ``start`` tracking event.
            SURVEY (22):
                Corresponds to the ``InLine.Survey`` node.
            THIRD_QUARTILE (23):
                Corresponds to the ``thirdQuartile`` tracking event.
            UNMUTE (24):
                Corresponds to the ``unmute`` tracking event.
            VIDEO_ABANDON (25):
                Corresponds to the ``abandon`` tracking event.
            VIEWABLE_IMPRESSION (26):
                Corresponds to the ``viewableImpression`` tracking event.
        """

        CONVERSION_EVENT_UNSPECIFIED = 0
        ACCEPT_INVITATION = 1
        CLICK_TRACKING = 2
        CLOSE = 3
        COLLAPSE = 4
        COMPLETE = 5
        CREATIVE_VIEW = 6
        CUSTOM_CLICK = 7
        ENGAGED_VIEW = 8
        EXPAND = 9
        FIRST_QUARTILE = 10
        FULLSCREEN = 11
        FULLY_VIEWABLE_AUDIBLE_HALF_DURATION_IMPRESSION = 12
        MEASURABLE_IMPRESSION = 13
        MIDPOINT = 14
        MUTE = 15
        PAUSE = 16
        RESUME = 17
        REWIND = 18
        SKIPPED = 19
        SKIP_SHOWN = 20
        START = 21
        SURVEY = 22
        THIRD_QUARTILE = 23
        UNMUTE = 24
        VIDEO_ABANDON = 25
        VIEWABLE_IMPRESSION = 26


__all__ = tuple(sorted(__protobuf__.manifest))
