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
        "OmnichannelSetting",
        "ReviewState",
        "InStock",
        "Pickup",
        "LfpLink",
        "OnDisplayToOrder",
        "About",
        "InventoryVerification",
        "GetOmnichannelSettingRequest",
        "ListOmnichannelSettingsRequest",
        "ListOmnichannelSettingsResponse",
        "CreateOmnichannelSettingRequest",
        "UpdateOmnichannelSettingRequest",
        "RequestInventoryVerificationRequest",
        "RequestInventoryVerificationResponse",
    },
)


class OmnichannelSetting(proto.Message):
    r"""Collection of information related to the omnichannel settings
    of a merchant.

    Attributes:
        name (str):
            Identifier. The resource name of the omnichannel setting.
            Format:
            ``accounts/{account}/omnichannelSettings/{omnichannel_setting}``
        region_code (str):
            Required. Immutable. Region code defined by
            `CLDR <https://cldr.unicode.org/>`__. Must be provided in
            the Create method, and is immutable.
        lsf_type (google.shopping.merchant_accounts_v1.types.OmnichannelSetting.LsfType):
            Required. The Local Store Front type for this
            country.
        in_stock (google.shopping.merchant_accounts_v1.types.InStock):
            Optional. The InStock URI and state for this
            country.
        pickup (google.shopping.merchant_accounts_v1.types.Pickup):
            Optional. The Pickup URI and state for this
            country.
        lfp_link (google.shopping.merchant_accounts_v1.types.LfpLink):
            Output only. The established link to a LFP
            provider.
        odo (google.shopping.merchant_accounts_v1.types.OnDisplayToOrder):
            Optional. The On Display to Order (ODO)
            policy URI and state for this country.
        about (google.shopping.merchant_accounts_v1.types.About):
            Optional. The about page URI and state for
            this country.
        inventory_verification (google.shopping.merchant_accounts_v1.types.InventoryVerification):
            Optional. The inventory verification contact
            and state for this country.
    """

    class LsfType(proto.Enum):
        r"""The product page experience type, which is also called the Local
        Store Front (LSF) type. Check the `HC
        article <https://support.google.com/merchants/answer/7178526>`__ for
        more details.

        Values:
            LSF_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            GHLSF (1):
                Google-Hosted Local Store Front. Check the `HC
                article <https://support.google.com/merchants/answer/14869424>`__
                for more details.
            MHLSF_BASIC (2):
                Merchant-Hosted Local Store Front Basic. Check the `HC
                article <https://support.google.com/merchants/answer/14615867>`__
                for more details.
            MHLSF_FULL (3):
                Merchant-Hosted Local Store Front Full. Check the `HC
                article <https://support.google.com/merchants/answer/14617076>`__
                for more details.
        """

        LSF_TYPE_UNSPECIFIED = 0
        GHLSF = 1
        MHLSF_BASIC = 2
        MHLSF_FULL = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    region_code: str = proto.Field(
        proto.STRING,
        number=2,
    )
    lsf_type: LsfType = proto.Field(
        proto.ENUM,
        number=12,
        enum=LsfType,
    )
    in_stock: "InStock" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="InStock",
    )
    pickup: "Pickup" = proto.Field(
        proto.MESSAGE,
        number=14,
        message="Pickup",
    )
    lfp_link: "LfpLink" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="LfpLink",
    )
    odo: "OnDisplayToOrder" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="OnDisplayToOrder",
    )
    about: "About" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="About",
    )
    inventory_verification: "InventoryVerification" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="InventoryVerification",
    )


class ReviewState(proto.Message):
    r"""The state of a omnichannel setting related review process."""

    class State(proto.Enum):
        r"""The state of the review process.

        Values:
            STATE_UNSPECIFIED (0):
                Default value. This value is unused.
            ACTIVE (1):
                The review process has concluded
                successfully. The reviewed item is active.
            FAILED (2):
                The review process failed.
            RUNNING (3):
                The review process is running.
            ACTION_REQUIRED (4):
                The review process is waiting for the
                merchant to take action.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        FAILED = 2
        RUNNING = 3
        ACTION_REQUIRED = 4


class InStock(proto.Message):
    r"""Collection of information related to InStock.

    Attributes:
        uri (str):
            Optional. Product landing page URI. It is only used for the
            review of MHLSF in-stock serving. This URI domain should
            match with the business's homepage. Required to be empty if
            the lsf_type is GHLSF, and required when the lsf_type is
            MHLSF_FULL or MHLSF_BASIC.
        state (google.shopping.merchant_accounts_v1.types.ReviewState.State):
            Output only. The state of the in-stock
            serving.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: "ReviewState.State" = proto.Field(
        proto.ENUM,
        number=2,
        enum="ReviewState.State",
    )


class Pickup(proto.Message):
    r"""Collection of information related to Pickup.

    Attributes:
        uri (str):
            Required. Pickup product page URI. It is only
            used for the review of pickup serving. This URI
            domain should match with the business's
            homepage.
        state (google.shopping.merchant_accounts_v1.types.ReviewState.State):
            Output only. The state of the pickup serving.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: "ReviewState.State" = proto.Field(
        proto.ENUM,
        number=2,
        enum="ReviewState.State",
    )


class LfpLink(proto.Message):
    r"""Collection of information related to the LFP link.

    Attributes:
        lfp_provider (str):
            Required. The resource name of the LFP provider. Format:
            ``lfpProviders/{lfp_provider}``
        external_account_id (str):
            Required. The account ID by which this
            merchant is known to the LFP provider.
        state (google.shopping.merchant_accounts_v1.types.ReviewState.State):
            Output only. The state of the LFP link.
    """

    lfp_provider: str = proto.Field(
        proto.STRING,
        number=1,
    )
    external_account_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    state: "ReviewState.State" = proto.Field(
        proto.ENUM,
        number=3,
        enum="ReviewState.State",
    )


class OnDisplayToOrder(proto.Message):
    r"""Collection of information related to the on display to order
    (`ODO <https://support.google.com/merchants/answer/14615056?ref_topic=15145747&sjid=6892280366904591178-NC>`__).

    Attributes:
        uri (str):
            Required. The on display to order (ODO)
            policy URI.
        state (google.shopping.merchant_accounts_v1.types.ReviewState.State):
            Output only. The state of the URI.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: "ReviewState.State" = proto.Field(
        proto.ENUM,
        number=2,
        enum="ReviewState.State",
    )


class About(proto.Message):
    r"""Collection of information related to the about page
    (`impressum <https://support.google.com/merchants/answer/14675634?ref_topic=15145634&sjid=6892280366904591178-NC>`__).

    Attributes:
        uri (str):
            Required. The about page URI.
        state (google.shopping.merchant_accounts_v1.types.ReviewState.State):
            Output only. The state of the URI.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: "ReviewState.State" = proto.Field(
        proto.ENUM,
        number=2,
        enum="ReviewState.State",
    )


class InventoryVerification(proto.Message):
    r"""Collection of information related to `inventory
    verification <https://support.google.com/merchants/answer/14684499?ref_topic=15145634&sjid=6892280366904591178-NC>`__.

    Attributes:
        state (google.shopping.merchant_accounts_v1.types.InventoryVerification.State):
            Output only. The state of the inventory
            verification process.
        contact (str):
            Required. The name of the contact for the
            inventory verification process.
        contact_email (str):
            Required. The email address of the contact
            for the inventory verification process.
        contact_state (google.shopping.merchant_accounts_v1.types.ReviewState.State):
            Output only. The state of the contact
            verification.
    """

    class State(proto.Enum):
        r"""The state of the `inventory
        verification <https://support.google.com/merchants/answer/14684499?ref_topic=15145634&sjid=6892280366904591178-NC>`__
        process.

        Values:
            STATE_UNSPECIFIED (0):
                Default value. This value is unused.
            ACTION_REQUIRED (1):
                When the merchant needs to initiate the
                inventory verification process. The next state
                is INACTIVE.
            INACTIVE (5):
                When the merchant is ready to request
                inventory verification.
            RUNNING (2):
                The inventory verification process is
                running. If the merchant is rejected, the next
                state is INACTIVE.
            SUCCEEDED (3):
                The inventory verification process succeeded.
            SUSPENDED (4):
                When merchant fails the inventory
                verification process and all attempts are
                exhausted.
        """

        STATE_UNSPECIFIED = 0
        ACTION_REQUIRED = 1
        INACTIVE = 5
        RUNNING = 2
        SUCCEEDED = 3
        SUSPENDED = 4

    state: State = proto.Field(
        proto.ENUM,
        number=1,
        enum=State,
    )
    contact: str = proto.Field(
        proto.STRING,
        number=2,
    )
    contact_email: str = proto.Field(
        proto.STRING,
        number=3,
    )
    contact_state: "ReviewState.State" = proto.Field(
        proto.ENUM,
        number=4,
        enum="ReviewState.State",
    )


class GetOmnichannelSettingRequest(proto.Message):
    r"""Request message for the GetOmnichannelSettings method.

    Attributes:
        name (str):
            Required. The name of the omnichannel setting to retrieve.
            Format:
            ``accounts/{account}/omnichannelSettings/{omnichannel_setting}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListOmnichannelSettingsRequest(proto.Message):
    r"""Request message for the ListOmnichannelSettings method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            omnichannel settings. Format: ``accounts/{account}``
        page_size (int):
            Optional. The maximum number of omnichannel
            settings to return. The service may return fewer
            than this value. If unspecified, at most 50
            omnichannel settings will be returned. The
            maximum value is 1000; values above 1000 will be
            coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListOmnichannelSettings`` call. Provide this to retrieve
            the subsequent page.

            When paginating, all other parameters provided to
            ``ListOmnichannelSettings`` must match the call that
            provided the page token.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListOmnichannelSettingsResponse(proto.Message):
    r"""Response message for the ListOmnichannelSettings method.

    Attributes:
        omnichannel_settings (MutableSequence[google.shopping.merchant_accounts_v1.types.OmnichannelSetting]):
            The omnichannel settings from the specified
            merchant.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    omnichannel_settings: MutableSequence["OmnichannelSetting"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="OmnichannelSetting",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateOmnichannelSettingRequest(proto.Message):
    r"""Request message for the CreateOmnichannelSetting method.

    Attributes:
        parent (str):
            Required. The parent resource where this omnichannel setting
            will be created. Format: ``accounts/{account}``
        omnichannel_setting (google.shopping.merchant_accounts_v1.types.OmnichannelSetting):
            Required. The omnichannel setting to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    omnichannel_setting: "OmnichannelSetting" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="OmnichannelSetting",
    )


class UpdateOmnichannelSettingRequest(proto.Message):
    r"""Request message for the UpdateOmnichannelSetting method.

    Attributes:
        omnichannel_setting (google.shopping.merchant_accounts_v1.types.OmnichannelSetting):
            Required. The omnichannel setting to update.

            The omnichannel setting's ``name`` field is used to identify
            the omnichannel setting to be updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to be updated.

            The following fields are supported in snake_case only:

            - ``lsf_type``
            - ``in_stock``
            - ``pickup``
            - ``odo``
            - ``about``
            - ``inventory_verification``

            Full replacement with wildcard ``*``\ is supported, while
            empty/implied update mask is not.
    """

    omnichannel_setting: "OmnichannelSetting" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="OmnichannelSetting",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class RequestInventoryVerificationRequest(proto.Message):
    r"""Request message for the RequestInventoryVerification method.

    Attributes:
        name (str):
            Required. The name of the omnichannel setting to request
            inventory verification. Format:
            ``accounts/{account}/omnichannelSettings/{omnichannel_setting}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class RequestInventoryVerificationResponse(proto.Message):
    r"""Response message for the RequestInventoryVerification method.

    Attributes:
        omnichannel_setting (google.shopping.merchant_accounts_v1.types.OmnichannelSetting):
            The omnichannel setting that was updated.
    """

    omnichannel_setting: "OmnichannelSetting" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="OmnichannelSetting",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
