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
    package="google.ads.datamanager.v1",
    manifest={
        "Product",
        "Destination",
        "ProductAccount",
    },
)


class Product(proto.Enum):
    r"""Deprecated. Use
    [``AccountType``][google.ads.datamanager.v1.ProductAccount.AccountType]
    instead. Represents a specific Google product.

    Values:
        PRODUCT_UNSPECIFIED (0):
            Unspecified product. Should never be used.
        GOOGLE_ADS (1):
            Google Ads.
        DISPLAY_VIDEO_PARTNER (2):
            Display & Video 360 partner.
        DISPLAY_VIDEO_ADVERTISER (3):
            Display & Video 360 advertiser.
        DATA_PARTNER (4):
            Data Partner.
    """

    _pb_options = {"deprecated": True}
    PRODUCT_UNSPECIFIED = 0
    GOOGLE_ADS = 1
    DISPLAY_VIDEO_PARTNER = 2
    DISPLAY_VIDEO_ADVERTISER = 3
    DATA_PARTNER = 4


class Destination(proto.Message):
    r"""The Google product you're sending data to. For example, a
    Google Ads account.

    Attributes:
        reference (str):
            Optional. ID for this ``Destination`` resource, unique
            within the request. Use to reference this ``Destination`` in
            the
            [IngestEventsRequest][google.ads.datamanager.v1.IngestEventsRequest]
            and
            [IngestAudienceMembersRequest][google.ads.datamanager.v1.IngestAudienceMembersRequest].
        login_account (google.ads.datamanager_v1.types.ProductAccount):
            Optional. The account used to make this API call. To add or
            remove data from the
            [``operating_account``][google.ads.datamanager.v1.Destination.operating_account],
            this ``login_account`` must have write access to the
            ``operating_account``. For example, a manager account of the
            ``operating_account``, or an account with an established
            link to the ``operating_account``.
        linked_account (google.ads.datamanager_v1.types.ProductAccount):
            Optional. An account that the calling user's
            [``login_account``][google.ads.datamanager.v1.Destination.login_account]
            has access to, through an established account link. For
            example, a data partner's ``login_account`` might have
            access to a client's ``linked_account``. The partner might
            use this field to send data from the ``linked_account`` to
            another
            [``operating_account``][google.ads.datamanager.v1.Destination.operating_account].
        operating_account (google.ads.datamanager_v1.types.ProductAccount):
            Required. The account to send the data to or
            remove the data from.
        product_destination_id (str):
            Optional. The object within the product
            account to ingest into. For example, a Google
            Ads audience ID, a Display & Video 360 audience
            ID or a Google Ads conversion action ID.

            This field is optional for Google Ad Manager
            event ingestion and User ingestion. Required for
            all other use cases.
    """

    reference: str = proto.Field(
        proto.STRING,
        number=1,
    )
    login_account: "ProductAccount" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ProductAccount",
    )
    linked_account: "ProductAccount" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ProductAccount",
    )
    operating_account: "ProductAccount" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="ProductAccount",
    )
    product_destination_id: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ProductAccount(proto.Message):
    r"""Represents a specific account.

    Attributes:
        product (google.ads.datamanager_v1.types.Product):
            Deprecated. Use
            [``account_type``][google.ads.datamanager.v1.ProductAccount.account_type]
            instead.
        account_id (str):
            Required. The ID of the account. For example,
            your Google Ads account ID.
        account_type (google.ads.datamanager_v1.types.ProductAccount.AccountType):
            Required. The type of the account. For example,
            ``GOOGLE_ADS``. Either ``account_type`` or the deprecated
            ``product`` is required. If both are set, the values must
            match.
    """

    class AccountType(proto.Enum):
        r"""Represents Google account types. Used to locate accounts and
        destinations.

        Values:
            ACCOUNT_TYPE_UNSPECIFIED (0):
                Unspecified product. Should never be used.
            GOOGLE_ADS (1):
                Google Ads.
            DISPLAY_VIDEO_PARTNER (2):
                Display & Video 360 partner.
            DISPLAY_VIDEO_ADVERTISER (3):
                Display & Video 360 advertiser.
            DATA_PARTNER (4):
                Data Partner.
            GOOGLE_ANALYTICS_PROPERTY (5):
                Google Analytics.
            GOOGLE_AD_MANAGER_AUDIENCE_LINK (6):
                Google Ad Manager audience link.
            FLOODLIGHT_CONFIG (7):
                Floodlight configuration.
            GOOGLE_AD_MANAGER (8):
                Google Ad Manager.
        """

        ACCOUNT_TYPE_UNSPECIFIED = 0
        GOOGLE_ADS = 1
        DISPLAY_VIDEO_PARTNER = 2
        DISPLAY_VIDEO_ADVERTISER = 3
        DATA_PARTNER = 4
        GOOGLE_ANALYTICS_PROPERTY = 5
        GOOGLE_AD_MANAGER_AUDIENCE_LINK = 6
        FLOODLIGHT_CONFIG = 7
        GOOGLE_AD_MANAGER = 8

    product: "Product" = proto.Field(
        proto.ENUM,
        number=1,
        enum="Product",
    )
    account_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    account_type: AccountType = proto.Field(
        proto.ENUM,
        number=3,
        enum=AccountType,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
