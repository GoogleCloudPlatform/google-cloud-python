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

import google.type.money_pb2 as money_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.ads.datamanager.v1",
    manifest={
        "PartnerMatchReportEntry",
        "PartnerMatchAdvertiserAccount",
        "PartnerMatchCampaign",
        "PartnerMatchAdGroup",
        "PartnerMatchUserList",
        "PartnerMatchLineItem",
    },
)


class PartnerMatchReportEntry(proto.Message):
    r"""A row/entry in a Partner Match report.

    Attributes:
        advertiser_account (google.ads.datamanager_v1.types.PartnerMatchAdvertiserAccount):
            The advertiser account details.
        campaign (google.ads.datamanager_v1.types.PartnerMatchCampaign):
            The campaign details.  Only returned for
            Google Ads advertisers.
        ad_group (google.ads.datamanager_v1.types.PartnerMatchAdGroup):
            The ad group details.
        user_list (google.ads.datamanager_v1.types.PartnerMatchUserList):
            The user list details.
        impression_count (int):
            The number of impressions for this entry.
        media_cost (google.type.money_pb2.Money):
            The media cost associated for this entry.
        line_item (google.ads.datamanager_v1.types.PartnerMatchLineItem):
            The line item details.  Only returned for
            DV360 advertisers.
        data_fees (google.type.money_pb2.Money):
            The data fees for this entry. Only returned
            for DV360 advertisers
    """

    advertiser_account: "PartnerMatchAdvertiserAccount" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="PartnerMatchAdvertiserAccount",
    )
    campaign: "PartnerMatchCampaign" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="PartnerMatchCampaign",
    )
    ad_group: "PartnerMatchAdGroup" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="PartnerMatchAdGroup",
    )
    user_list: "PartnerMatchUserList" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="PartnerMatchUserList",
    )
    impression_count: int = proto.Field(
        proto.INT64,
        number=5,
    )
    media_cost: money_pb2.Money = proto.Field(
        proto.MESSAGE,
        number=6,
        message=money_pb2.Money,
    )
    line_item: "PartnerMatchLineItem" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="PartnerMatchLineItem",
    )
    data_fees: money_pb2.Money = proto.Field(
        proto.MESSAGE,
        number=8,
        message=money_pb2.Money,
    )


class PartnerMatchAdvertiserAccount(proto.Message):
    r"""The advertiser account details.

    Attributes:
        account_type (str):
            The type of account (e.g. GOOGLE_ADS,
            DISPLAY_VIDEO_ADVERTISER).
        account_id (str):
            The Customer ID of the account.
        display_name (str):
            The descriptive name of the account.
    """

    account_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    account_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )


class PartnerMatchCampaign(proto.Message):
    r"""The campaign details.

    Attributes:
        campaign_id (int):
            The ID of the campaign.
        display_name (str):
            The descriptive name of the campaign.
    """

    campaign_id: int = proto.Field(
        proto.INT64,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class PartnerMatchAdGroup(proto.Message):
    r"""The ad group details.

    Attributes:
        ad_group_id (int):
            The ID of the ad group.
        display_name (str):
            The descriptive name of the ad group.
    """

    ad_group_id: int = proto.Field(
        proto.INT64,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class PartnerMatchUserList(proto.Message):
    r"""The user list details.

    Attributes:
        user_list_id (int):
            The ID of the user list.
        display_name (str):
            The descriptive name of the user list.
    """

    user_list_id: int = proto.Field(
        proto.INT64,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class PartnerMatchLineItem(proto.Message):
    r"""The line item details.

    Attributes:
        line_item_id (int):
            The ID of the line item.
        display_name (str):
            The descriptive name of the line item.
    """

    line_item_id: int = proto.Field(
        proto.INT64,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
