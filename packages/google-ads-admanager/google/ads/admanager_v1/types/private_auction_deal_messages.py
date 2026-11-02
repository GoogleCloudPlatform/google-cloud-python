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

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.type.money_pb2 as money_pb2  # type: ignore
import proto  # type: ignore

from google.ads.admanager_v1.types import (
    deal_buyer_permission_type_enum,
    non_guaranteed_deal_priority,
    private_marketplace_enums,
    size,
)
from google.ads.admanager_v1.types import targeting as gaa_targeting

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "PrivateAuctionDeal",
    },
)


class PrivateAuctionDeal(proto.Message):
    r"""The ``PrivateAuctionDeal`` resource.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the ``PrivateAuctionDeal``.
            Format:
            ``networks/{network_code}/privateAuctionDeals/{private_auction_deal_id}``
        private_auction_deal_id (int):
            Output only. Deprecated: ``PrivateAuctionDeal`` ID.

            This field is a member of `oneof`_ ``_private_auction_deal_id``.
        private_auction_id (int):
            Immutable. The ID of the
            [PrivateAuction][google.ads.admanager.v1.PrivateAuction].

            This field is a member of `oneof`_ ``_private_auction_id``.
        private_auction_display_name (str):
            Output only. The display name of the
            [PrivateAuction][google.ads.admanager.v1.PrivateAuction].

            This field is a member of `oneof`_ ``_private_auction_display_name``.
        buyer_account_id (int):
            Immutable. The account ID of the buyer of the
            ``PrivateAuctionDeal``.

            This field is a member of `oneof`_ ``_buyer_account_id``.
        external_deal_id (int):
            Output only. The external ID of the ``PrivateAuctionDeal``.

            This field is a member of `oneof`_ ``_external_deal_id``.
        targeting (google.ads.admanager_v1.types.Targeting):
            Optional. The targeting of the ``PrivateAuctionDeal``.

            This field is a member of `oneof`_ ``_targeting``.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. Non-empty default. The start time of the
            ``PrivateAuctionDeal``. If unset, the ``startTime`` will
            default as follows: On create: To the deal's
            ``create_time``. On update: To the deal's existing
            ``start_time``, which can be null.

            This field is a member of `oneof`_ ``_start_time``.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. The end time of the ``PrivateAuctionDeal``.

            This field is a member of `oneof`_ ``_end_time``.
        floor_price (google.type.money_pb2.Money):
            Required. The floor price of the ``PrivateAuctionDeal``.

            This field is a member of `oneof`_ ``_floor_price``.
        creative_sizes (MutableSequence[google.ads.admanager_v1.types.Size]):
            Optional. The expected creative sizes of the
            ``PrivateAuctionDeal``.
        status (google.ads.admanager_v1.types.PrivateMarketplaceDealStatusEnum.PrivateMarketplaceDealStatus):
            Output only. The status of the ``PrivateAuctionDeal``.

            This field is a member of `oneof`_ ``_status``.
        auction_priority_enabled (bool):
            Optional. Whether the deal is enabled with
            priority over open auction.

            This field is a member of `oneof`_ ``_auction_priority_enabled``.
        block_override_enabled (bool):
            Optional. Whether the deal has block override
            enabled.

            This field is a member of `oneof`_ ``_block_override_enabled``.
        publisher_floor_exempt (bool):
            Optional. Whether the deal is exempt from
            publisher floor price.

            This field is a member of `oneof`_ ``_publisher_floor_exempt``.
        buyer_permission_type (google.ads.admanager_v1.types.DealBuyerPermissionTypeEnum.DealBuyerPermissionType):
            Optional. The buyer permission model defining
            how the deal would transact among all buyers
            under the same bidder.

            This field is a member of `oneof`_ ``_buyer_permission_type``.
        buyer_data (google.ads.admanager_v1.types.PrivateAuctionDeal.BuyerData):
            Optional. The buyer data required by the
            Marketplace API.

            This field is a member of `oneof`_ ``_buyer_data``.
        deal_priority (google.ads.admanager_v1.types.NonGuaranteedDealPriority):
            Optional. The priority of the deal across all
            non-guaranteed deals.

            This field is a member of `oneof`_ ``_deal_priority``.
        archived (bool):
            Output only. Whether the deal is archived.

            This field is a member of `oneof`_ ``_archived``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The instant at which the ``PrivateAuctionDeal``
            was created.

            This field is a member of `oneof`_ ``_create_time``.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The instant at which the ``PrivateAuctionDeal``
            was last updated.

            This field is a member of `oneof`_ ``_update_time``.
    """

    class BuyerData(proto.Message):
        r"""Contains buyer data. This data is required by the Marketplace
        API.

        Attributes:
            buyer_emails (MutableSequence[str]):
                Optional. The email contacts of the buyer of the
                ``PrivateAuctionDeal``.
        """

        buyer_emails: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    private_auction_deal_id: int = proto.Field(
        proto.INT64,
        number=2,
        optional=True,
    )
    private_auction_id: int = proto.Field(
        proto.INT64,
        number=3,
        optional=True,
    )
    private_auction_display_name: str = proto.Field(
        proto.STRING,
        number=20,
        optional=True,
    )
    buyer_account_id: int = proto.Field(
        proto.INT64,
        number=4,
        optional=True,
    )
    external_deal_id: int = proto.Field(
        proto.INT64,
        number=5,
        optional=True,
    )
    targeting: gaa_targeting.Targeting = proto.Field(
        proto.MESSAGE,
        number=6,
        optional=True,
        message=gaa_targeting.Targeting,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=26,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    floor_price: money_pb2.Money = proto.Field(
        proto.MESSAGE,
        number=9,
        optional=True,
        message=money_pb2.Money,
    )
    creative_sizes: MutableSequence[size.Size] = proto.RepeatedField(
        proto.MESSAGE,
        number=18,
        message=size.Size,
    )
    status: private_marketplace_enums.PrivateMarketplaceDealStatusEnum.PrivateMarketplaceDealStatus = proto.Field(
        proto.ENUM,
        number=10,
        optional=True,
        enum=private_marketplace_enums.PrivateMarketplaceDealStatusEnum.PrivateMarketplaceDealStatus,
    )
    auction_priority_enabled: bool = proto.Field(
        proto.BOOL,
        number=11,
        optional=True,
    )
    block_override_enabled: bool = proto.Field(
        proto.BOOL,
        number=12,
        optional=True,
    )
    publisher_floor_exempt: bool = proto.Field(
        proto.BOOL,
        number=24,
        optional=True,
    )
    buyer_permission_type: deal_buyer_permission_type_enum.DealBuyerPermissionTypeEnum.DealBuyerPermissionType = proto.Field(
        proto.ENUM,
        number=13,
        optional=True,
        enum=deal_buyer_permission_type_enum.DealBuyerPermissionTypeEnum.DealBuyerPermissionType,
    )
    buyer_data: BuyerData = proto.Field(
        proto.MESSAGE,
        number=14,
        optional=True,
        message=BuyerData,
    )
    deal_priority: non_guaranteed_deal_priority.NonGuaranteedDealPriority = proto.Field(
        proto.MESSAGE,
        number=22,
        optional=True,
        message=non_guaranteed_deal_priority.NonGuaranteedDealPriority,
    )
    archived: bool = proto.Field(
        proto.BOOL,
        number=23,
        optional=True,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=15,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=16,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
