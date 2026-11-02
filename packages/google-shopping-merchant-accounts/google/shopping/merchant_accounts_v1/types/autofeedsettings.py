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

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.shopping.merchant.accounts.v1",
    manifest={
        "AutofeedSettings",
        "GetAutofeedSettingsRequest",
        "UpdateAutofeedSettingsRequest",
    },
)


class AutofeedSettings(proto.Message):
    r"""Collection of information related to the
    `autofeed <https://support.google.com/merchants/answer/7538732>`__
    settings.

    Attributes:
        name (str):
            Identifier. The resource name of the autofeed settings.
            Format: ``accounts/{account}/autofeedSettings``.
        enable_products (bool):
            Required. Enables or disables product crawling through the
            autofeed for the given account. Autofeed accounts must meet
            `certain
            conditions <https://support.google.com/merchants/answer/7538732#Configure_automated_feeds_Standard_Experience>`__,
            which can be checked through the ``eligible`` field. The
            account must **not** be a marketplace. When the autofeed is
            enabled for the first time, the products usually appear
            instantly. When re-enabling, it might take up to 24 hours
            for products to appear.
        eligible (bool):
            Output only. Determines whether the business
            is eligible for being enrolled into an autofeed.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    enable_products: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    eligible: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class GetAutofeedSettingsRequest(proto.Message):
    r"""Request message for the ``GetAutofeedSettings`` method.

    Attributes:
        name (str):
            Required. The resource name of the autofeed settings.
            Format: ``accounts/{account}/autofeedSettings``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateAutofeedSettingsRequest(proto.Message):
    r"""Request message for the ``UpdateAutofeedSettings`` method.

    Attributes:
        autofeed_settings (google.shopping.merchant_accounts_v1.types.AutofeedSettings):
            Required. The new version of the autofeed
            setting.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. List of fields being updated.
    """

    autofeed_settings: "AutofeedSettings" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="AutofeedSettings",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
