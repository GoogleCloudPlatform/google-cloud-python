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
        "EncryptedUserId",
    },
)


class EncryptedUserId(proto.Message):
    r"""A user identifier issued to be used for attribution. All
    fields are required if this is used.

    Attributes:
        encrypted_id (str):
            Required. The alphanumeric encrypted id.
        entity_type (google.ads.datamanager_v1.types.EncryptedUserId.EncryptionEntityType):
            Required. The encryption entity type. This
            should match the encryption configuration for ad
            serving or Data Transfer.
        entity_id (int):
            Required. The encryption entity ID. This
            should match the encryption configuration for ad
            serving or Data Transfer.
        source (google.ads.datamanager_v1.types.EncryptedUserId.EncryptionSource):
            Required. Describes whether the encrypted
            cookie was received from ad serving (the %m
            macro) or from Data Transfer.
    """

    class EncryptionEntityType(proto.Enum):
        r"""The encryption entity type.

        Values:
            ENCRYPTION_ENTITY_TYPE_UNSPECIFIED (0):
                Unspecified encryption entity type.
            CAMPAIGN_MANAGER_ACCOUNT (1):
                Campaign Manager 360 account.
            CAMPAIGN_MANAGER_ADVERTISER (2):
                Campaign Manager 360 advertiser.
            DISPLAY_VIDEO_PARTNER (3):
                Display & Video 360 partner.
            DISPLAY_VIDEO_ADVERTISER (4):
                Display & Video 360 advertiser.
            GOOGLE_ADS_CUSTOMER (5):
                Google Ads customer.
            GOOGLE_AD_MANAGER_NETWORK_CODE (6):
                Google Ad Manager network code.
        """

        ENCRYPTION_ENTITY_TYPE_UNSPECIFIED = 0
        CAMPAIGN_MANAGER_ACCOUNT = 1
        CAMPAIGN_MANAGER_ADVERTISER = 2
        DISPLAY_VIDEO_PARTNER = 3
        DISPLAY_VIDEO_ADVERTISER = 4
        GOOGLE_ADS_CUSTOMER = 5
        GOOGLE_AD_MANAGER_NETWORK_CODE = 6

    class EncryptionSource(proto.Enum):
        r"""The encryption source.

        Values:
            ENCRYPTION_SOURCE_UNSPECIFIED (0):
                Unspecified encryption source.
            AD_SERVING (1):
                Ad serving encryption source.
            DATA_TRANSFER (2):
                Data transfer encryption source.
        """

        ENCRYPTION_SOURCE_UNSPECIFIED = 0
        AD_SERVING = 1
        DATA_TRANSFER = 2

    encrypted_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    entity_type: EncryptionEntityType = proto.Field(
        proto.ENUM,
        number=2,
        enum=EncryptionEntityType,
    )
    entity_id: int = proto.Field(
        proto.INT64,
        number=3,
    )
    source: EncryptionSource = proto.Field(
        proto.ENUM,
        number=4,
        enum=EncryptionSource,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
