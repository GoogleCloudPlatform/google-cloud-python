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
        "LineItemCostTypeEnum",
        "LineItemTypeEnum",
        "LineItemReservationStatusEnum",
        "LineItemComputedStatusEnum",
    },
)


class LineItemCostTypeEnum(proto.Message):
    r"""Wrapper message for
    [LineItemCostType][google.ads.admanager.v1.LineItemCostTypeEnum.LineItemCostType].

    """

    class LineItemCostType(proto.Enum):
        r"""Describes the LineItem actions that are billable.

        Values:
            LINE_ITEM_COST_TYPE_UNSPECIFIED (0):
                Not specified value.
            CPA (1):
                Starting February 22, 2024 the CPA LineItemCostType will
                only be read as part of Spotlight deprecation, learn more
                at:
                https://support.google.com/admanager/answer/7519021#spotlight

                Cost per action. The line item
                [lineItemType][google.ads.admanager.v1.LineItem.line_item_type]
                must be one of:

                - [LineItemTypeEnum.LineItemType.SPONSORSHIP][google.ads.admanager.v1.LineItemTypeEnum.LineItemType.SPONSORSHIP]
                - [LineItemTypeEnum.LineItemType.STANDARD][google.ads.admanager.v1.LineItemTypeEnum.LineItemType.STANDARD]
                - [LineItemTypeEnum.LineItemType.BULK][google.ads.admanager.v1.LineItemTypeEnum.LineItemType.BULK]
                - [LineItemTypeEnum.LineItemType.NETWORK][google.ads.admanager.v1.LineItemTypeEnum.LineItemType.NETWORK]
            CPC (2):
                Cost per click. The line item
                [lineItemType][google.ads.admanager.v1.LineItem.line_item_type]
                must be one of:

                - [LineItemTypeEnum.LineItemType.SPONSORSHIP][google.ads.admanager.v1.LineItemTypeEnum.LineItemType.SPONSORSHIP]
                - [LineItemTypeEnum.LineItemType.STANDARD][google.ads.admanager.v1.LineItemTypeEnum.LineItemType.STANDARD]
                - [LineItemTypeEnum.LineItemType.BULK][google.ads.admanager.v1.LineItemTypeEnum.LineItemType.BULK]
                - [LineItemTypeEnum.LineItemType.NETWORK][google.ads.admanager.v1.LineItemTypeEnum.LineItemType.NETWORK]
                - [LineItemTypeEnum.LineItemType.PRICE_PRIORITY][google.ads.admanager.v1.LineItemTypeEnum.LineItemType.PRICE_PRIORITY]
                - [LineItemTypeEnum.LineItemType.HOUSE][google.ads.admanager.v1.LineItemTypeEnum.LineItemType.HOUSE]
            CPD (3):
                Cost per day. The line item
                [lineItemType][google.ads.admanager.v1.LineItem.line_item_type]
                must be one of:

                - [LineItemTypeEnum.LineItemType.SPONSORSHIP][google.ads.admanager.v1.LineItemTypeEnum.LineItemType.SPONSORSHIP]
                - [LineItemTypeEnum.LineItemType.NETWORK][google.ads.admanager.v1.LineItemTypeEnum.LineItemType.NETWORK]
            CPM (4):
                Cost per mille (thousand) impressions. The line item
                [lineItemType][google.ads.admanager.v1.LineItem.line_item_type]
                must be one of:

                - [LineItemTypeEnum.LineItemType.SPONSORSHIP][google.ads.admanager.v1.LineItemTypeEnum.LineItemType.SPONSORSHIP]
                - [LineItemTypeEnum.LineItemType.STANDARD][google.ads.admanager.v1.LineItemTypeEnum.LineItemType.STANDARD]
                - [LineItemTypeEnum.LineItemType.BULK][google.ads.admanager.v1.LineItemTypeEnum.LineItemType.BULK]
                - [LineItemTypeEnum.LineItemType.NETWORK][google.ads.admanager.v1.LineItemTypeEnum.LineItemType.NETWORK]
                - [LineItemTypeEnum.LineItemType.PRICE_PRIORITY][google.ads.admanager.v1.LineItemTypeEnum.LineItemType.PRICE_PRIORITY]
                - [LineItemTypeEnum.LineItemType.HOUSE][google.ads.admanager.v1.LineItemTypeEnum.LineItemType.HOUSE]
            VCPM (5):
                Cost per mille (thousand) Active View viewable impressions.
                The line item
                [lineItemType][google.ads.admanager.v1.LineItem.line_item_type]
                must be one of:

                - [LineItemTypeEnum.LineItemType.STANDARD][google.ads.admanager.v1.LineItemTypeEnum.LineItemType.STANDARD]
            CPM_IN_TARGET (6):
                Cost per millie (thousand) in-target impressions. The line
                item
                [lineItemType][google.ads.admanager.v1.LineItem.line_item_type]
                must be one of:

                - [LineItemTypeEnum.LineItemType.STANDARD][google.ads.admanager.v1.LineItemTypeEnum.LineItemType.STANDARD]
            CPF (7):
                Cost for the entire flight of the deal. The line item
                [lineItemType][google.ads.admanager.v1.LineItem.line_item_type]
                must be must be one of:

                - [LineItemTypeEnum.LineItemType.SPONSORSHIP][google.ads.admanager.v1.LineItemTypeEnum.LineItemType.SPONSORSHIP]
            CPCV (8):
                Cost per completed view. The line item
                [lineItemType][google.ads.admanager.v1.LineItem.line_item_type]
                must be one of:

                - [LineItemTypeEnum.LineItemType.STANDARD][google.ads.admanager.v1.LineItemTypeEnum.LineItemType.STANDARD].
        """

        LINE_ITEM_COST_TYPE_UNSPECIFIED = 0
        CPA = 1
        CPC = 2
        CPD = 3
        CPM = 4
        VCPM = 5
        CPM_IN_TARGET = 6
        CPF = 7
        CPCV = 8


class LineItemTypeEnum(proto.Message):
    r"""Wrapper message for
    [LineItemType][google.ads.admanager.v1.LineItemTypeEnum.LineItemType].

    """

    class LineItemType(proto.Enum):
        r"""Indicates the priority of a LineItem, determined by the way
        in which impressions are reserved to be served for it.

        Values:
            LINE_ITEM_TYPE_UNSPECIFIED (0):
                Not specified value.
            SPONSORSHIP (12):
                The type of LineItem for which a percentage
                of all the impressions that are being sold are
                reserved.
            STANDARD (13):
                The type of LineItem for which a fixed
                quantity of impressions or clicks are reserved.
            NETWORK (9):
                The type of LineItem most commonly used to
                fill a site's unsold inventory if not
                contractually obligated to deliver a requested
                number of impressions. Uses daily percentage of
                unsold impressions or clicks.
            BULK (4):
                The type of LineItem for which a fixed
                quantity of impressions or clicks will be
                delivered at a priority lower than the STANDARD
                type.
            PRICE_PRIORITY (11):
                The type of LineItem most commonly used to
                fill a site's unsold inventory if not
                contractually obligated to deliver a requested
                number of impressions. Uses fixed quantity
                percentage of unsold impressions or clicks.
            HOUSE (7):
                The type of LineItem typically used for ads
                that promote products and services chosen by the
                publisher.
            CLICK_TRACKING (6):
                The type of LineItem used for ads that track
                ads being served externally of Ad Manager.
            ADSENSE (2):
                Targets the LineItem to specific inventory
                available to AdSense buyers.
            AD_EXCHANGE (3):
                Targets the LineItem to specific inventory
                available to Authorized Buyers and the Open
                Auction.
            BUMPER (5):
                Represents a non-monetizable video LineItem
                that targets one or more bumper positions, which
                are short house video messages used by
                publishers to separate content from ad breaks.
            PREFERRED_DEAL (10):
                The type of LineItem for which there are no
                impressions reserved, and will serve for a
                second price bid.
            AUDIENCE_EXTENSION (14):
                The type of LineItem used for configuring
                audience extension campaigns.
        """

        LINE_ITEM_TYPE_UNSPECIFIED = 0
        SPONSORSHIP = 12
        STANDARD = 13
        NETWORK = 9
        BULK = 4
        PRICE_PRIORITY = 11
        HOUSE = 7
        CLICK_TRACKING = 6
        ADSENSE = 2
        AD_EXCHANGE = 3
        BUMPER = 5
        PREFERRED_DEAL = 10
        AUDIENCE_EXTENSION = 14


class LineItemReservationStatusEnum(proto.Message):
    r"""Wrapper message for
    [LineItemReservationStatus][google.ads.admanager.v1.LineItemReservationStatusEnum.LineItemReservationStatus].

    """

    class LineItemReservationStatus(proto.Enum):
        r"""Defines the different reservation statuses of a line item.

        Values:
            LINE_ITEM_RESERVATION_STATUS_UNSPECIFIED (0):
                No value specified
            RESERVED (1):
                Indicates that inventory has been reserved
                for the line item.
            UNRESERVED (2):
                Indicates that inventory has not been
                reserved for the line item.
        """

        LINE_ITEM_RESERVATION_STATUS_UNSPECIFIED = 0
        RESERVED = 1
        UNRESERVED = 2


class LineItemComputedStatusEnum(proto.Message):
    r"""Wrapper message for
    [LineItemComputedStatus][google.ads.admanager.v1.LineItemComputedStatusEnum.LineItemComputedStatus].

    """

    class LineItemComputedStatus(proto.Enum):
        r"""Describes the computed LineItem status that is derived from
        the current state of the LineItem.

        Values:
            LINE_ITEM_COMPUTED_STATUS_UNSPECIFIED (0):
                No value specified.
            CANCELED (1):
                The LineItem has been canceled and is no
                longer eligible to serve. This is a legacy
                status.
            COMPLETED (2):
                The LineItem has completed its run.
            DELIVERING (3):
                The LineItem has begun serving.
            DELIVERY_EXTENDED (4):
                The LineItem has past its endDateTime with an
                auto extension, but hasn't met its goal.
            DISAPPROVED (5):
                The LineItem has been disapproved and is not
                eligible to serve.
            DRAFT (6):
                The LineItem is still being drafted.
            INACTIVE (7):
                The LineItem is inactive. It is either caused
                by missing creatives or the network disabling
                auto-activation.
            PAUSED (8):
                The LineItem has been paused from serving.
            PAUSED_INVENTORY_RELEASED (9):
                The LineItem has been paused and its reserved
                inventory has been released. The LineItem will
                not serve.
            PENDING_APPROVAL (10):
                The LineItem has been submitted for approval.
            READY (11):
                The LineItem has been activated and is ready
                to serve.
        """

        LINE_ITEM_COMPUTED_STATUS_UNSPECIFIED = 0
        CANCELED = 1
        COMPLETED = 2
        DELIVERING = 3
        DELIVERY_EXTENDED = 4
        DISAPPROVED = 5
        DRAFT = 6
        INACTIVE = 7
        PAUSED = 8
        PAUSED_INVENTORY_RELEASED = 9
        PENDING_APPROVAL = 10
        READY = 11


__all__ = tuple(sorted(__protobuf__.manifest))
