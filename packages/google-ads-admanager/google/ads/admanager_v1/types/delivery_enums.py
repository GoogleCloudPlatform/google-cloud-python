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
        "LineItemDeliveryRateTypeEnum",
        "RoadblockingTypeEnum",
        "CompanionDeliveryOptionEnum",
        "CreativeRotationTypeEnum",
    },
)


class LineItemDeliveryRateTypeEnum(proto.Message):
    r"""Wrapper message for
    [LineItemDeliveryRateType][google.ads.admanager.v1.LineItemDeliveryRateTypeEnum.LineItemDeliveryRateType].

    """

    class LineItemDeliveryRateType(proto.Enum):
        r"""Possible delivery rates for a
        [LineItem][google.ads.admanager.v1.LineItem]. It dictates the manner
        in which the LineItem is served.

        Values:
            LINE_ITEM_DELIVERY_RATE_TYPE_UNSPECIFIED (0):
                No value specified.
            AS_FAST_AS_POSSIBLE (3):
                The booked impressions may delivered well
                before the end time. Other lower-priority or
                lower-value LineItems will be stopped from
                delivering until the LineItem meets the number
                of impressions or clicks it is booked for.
            EVENLY (1):
                LineItems are served as evenly as possible
                across the number of days specified in a
                LineItem's duration.
            FRONTLOADED (2):
                LineItems are served more aggressively in the
                beginning of the flight date.
        """

        LINE_ITEM_DELIVERY_RATE_TYPE_UNSPECIFIED = 0
        AS_FAST_AS_POSSIBLE = 3
        EVENLY = 1
        FRONTLOADED = 2


class RoadblockingTypeEnum(proto.Message):
    r"""Wrapper message for
    [RoadblockingType][google.ads.admanager.v1.RoadblockingTypeEnum.RoadblockingType]

    """

    class RoadblockingType(proto.Enum):
        r"""Describes the roadblocking types.

        Values:
            ROADBLOCKING_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            ALL_ROADBLOCK (1):
                All or none of the creatives from a line item
                will serve. This option will only work if served
                to a GPT tag using SRA (single request
                architecture mode).
            AS_MANY_AS_POSSIBLE (2):
                As many creatives from a line item as can fit
                on a page will serve. This could mean anywhere
                from one to all of a line item's creatives given
                the size constraints of ad slots on a page.
            CREATIVE_SET (3):
                A master/companion creative set roadblocking type. A
                [CreativePlaceholder][google.ads.admanager.v1.CreativePlaceholder]
                must be set accordingly.
            ONE_OR_MORE (4):
                Any number of creatives from a line item can
                serve together at a time.
            ONLY_ONE (5):
                Only one creative from a line item can serve
                at a time.
        """

        ROADBLOCKING_TYPE_UNSPECIFIED = 0
        ALL_ROADBLOCK = 1
        AS_MANY_AS_POSSIBLE = 2
        CREATIVE_SET = 3
        ONE_OR_MORE = 4
        ONLY_ONE = 5


class CompanionDeliveryOptionEnum(proto.Message):
    r"""Wrapper message for
    [CompanionDeliveryOption][google.ads.admanager.v1.CompanionDeliveryOptionEnum.CompanionDeliveryOption].

    """

    class CompanionDeliveryOption(proto.Enum):
        r"""Defines the different delivery types of a line item
        companion.

        Values:
            COMPANION_DELIVERY_OPTION_UNSPECIFIED (0):
                No value specified.
            OPTIONAL (1):
                Companions are not required to serve a
                [CreativeSet][google.ads.admanager.v1.CreativeSet]. The
                creative set can serve to inventory that has zero or more
                matching companions.
            AT_LEAST_ONE (2):
                At least one companion must be served in
                order for the creative set to be used.
            ALL (3):
                All companions in the set must be served in
                order for the creative set to be used. This can
                still serve to inventory that has more
                companions than can be filled.
        """

        COMPANION_DELIVERY_OPTION_UNSPECIFIED = 0
        OPTIONAL = 1
        AT_LEAST_ONE = 2
        ALL = 3


class CreativeRotationTypeEnum(proto.Message):
    r"""Wrapper message for
    [CreativeRotationType][google.ads.admanager.v1.CreativeRotationTypeEnum.CreativeRotationType].

    """

    class CreativeRotationType(proto.Enum):
        r"""The strategy to use for displaying multiple creatives that
        are associated with a line item.

        Values:
            CREATIVE_ROTATION_TYPE_UNSPECIFIED (0):
                No value specified.
            EVENLY (1):
                Creatives are displayed approximately the
                same number of times over the duration of the
                line item.
            OPTIMIZED (2):
                Creatives are served approximately
                proportionally to their performance.
            SEQUENTIAL (4):
                Creatives are served exactly in sequential
                order, aka Storyboarding. Set on the
                LineItemCreativeAssociation.
            WEIGHTED (3):
                Creatives are served approximately
                proportionally to their weights, set on the
                LineItemCreativeAssociation.
        """

        CREATIVE_ROTATION_TYPE_UNSPECIFIED = 0
        EVENLY = 1
        OPTIMIZED = 2
        SEQUENTIAL = 4
        WEIGHTED = 3


__all__ = tuple(sorted(__protobuf__.manifest))
