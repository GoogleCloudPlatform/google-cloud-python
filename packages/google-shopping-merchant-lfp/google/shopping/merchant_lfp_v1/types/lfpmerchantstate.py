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
    package="google.shopping.merchant.lfp.v1",
    manifest={
        "LfpMerchantState",
        "GetLfpMerchantStateRequest",
    },
)


class LfpMerchantState(proto.Message):
    r"""The LFP state of a merchant.

    Attributes:
        name (str):
            Identifier. The name of the ``LfpMerchantState`` resource.
            Format:
            ``accounts/{account}/lfpMerchantStates/{target_merchant}``.
            For example, ``accounts/123456/lfpMerchantStates/567890``.
        linked_gbps (int):
            Number of `GBPs <https://www.google.com/business/>`__ this
            merchant has access to.
        store_states (MutableSequence[google.shopping.merchant_lfp_v1.types.LfpMerchantState.LfpStoreState]):
            Output only. The state per store from the
            specified merchant. The field will be absent if
            the merchant has no stores submitted through
            LFP.
        inventory_stats (google.shopping.merchant_lfp_v1.types.LfpMerchantState.InventoryStats):
            The inventory statistics for the merchant.
            The field will be absent if the merchant has no
            inventory submitted through LFP.
        country_settings (MutableSequence[google.shopping.merchant_lfp_v1.types.LfpMerchantState.CountrySettings]):
            Country-specific settings for the merchant.
    """

    class LfpStoreState(proto.Message):
        r"""The state of a specific merchant's store.

        Attributes:
            store_code (str):
                Required. Immutable. The identifier of this
                store.
            matching_state (google.shopping.merchant_lfp_v1.types.LfpMerchantState.LfpStoreState.StoreMatchingState):
                Output only. The store matching state.
            matching_state_hint (str):
                The hint of why the matching has failed (only set if
                matching_state is FAILED).
        """

        class StoreMatchingState(proto.Enum):
            r"""The state of matching ``LfpStore`` to a Google Business Profile
            listing.

            Values:
                STORE_MATCHING_STATE_UNSPECIFIED (0):
                    Store matching state unspecified.
                STORE_MATCHING_STATE_MATCHED (1):
                    The ``LfpStore`` is successfully matched with a Google
                    Business Profile store.
                STORE_MATCHING_STATE_FAILED (2):
                    The ``LfpStore`` is not matched with a Google Business
                    Profile store.
            """

            STORE_MATCHING_STATE_UNSPECIFIED = 0
            STORE_MATCHING_STATE_MATCHED = 1
            STORE_MATCHING_STATE_FAILED = 2

        store_code: str = proto.Field(
            proto.STRING,
            number=1,
        )
        matching_state: "LfpMerchantState.LfpStoreState.StoreMatchingState" = (
            proto.Field(
                proto.ENUM,
                number=2,
                enum="LfpMerchantState.LfpStoreState.StoreMatchingState",
            )
        )
        matching_state_hint: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class InventoryStats(proto.Message):
        r"""The inventory statistics for a merchant.

        Attributes:
            submitted_entries (int):
                Number of entries (understanding entry as a
                pair of product and store) that were built based
                on provided inventories/sales and submitted to
                Google.
            submitted_in_stock_entries (int):
                Number of submitted in stock entries.
            unsubmitted_entries (int):
                Number of entries that were built based on
                provided inventories/sales and couldn't be
                submitted to Google due to errors like missing
                product.
            submitted_products (int):
                Number of products from provided
                inventories/sales that were created from matches
                to existing online products provided by the
                merchant or to the Google catalog.
        """

        submitted_entries: int = proto.Field(
            proto.INT64,
            number=1,
        )
        submitted_in_stock_entries: int = proto.Field(
            proto.INT64,
            number=2,
        )
        unsubmitted_entries: int = proto.Field(
            proto.INT64,
            number=3,
        )
        submitted_products: int = proto.Field(
            proto.INT64,
            number=4,
        )

    class CountrySettings(proto.Message):
        r"""Country-specific settings for the merchant.

        Attributes:
            region_code (str):
                Required. The `CLDR territory
                code <https://github.com/unicode-org/cldr/blob/latest/common/main/en.xml>`__
                for the country for which these settings are defined.
            free_local_listings_enabled (bool):
                True if this merchant has enabled free local
                listings in MC.
            local_inventory_ads_enabled (bool):
                True if this merchant has enabled local
                inventory ads in MC.
            inventory_verification_state (google.shopping.merchant_lfp_v1.types.LfpMerchantState.CountrySettings.VerificationState):
                Output only. The verification state of this
                merchant's inventory check.
            product_page_type (google.shopping.merchant_lfp_v1.types.LfpMerchantState.CountrySettings.ProductPageType):
                Output only. The product page type selected
                by this merchant.
            instock_serving_verification_state (google.shopping.merchant_lfp_v1.types.LfpMerchantState.CountrySettings.VerificationState):
                Output only. The verification state of this
                merchant's instock serving feature.
            pickup_serving_verification_state (google.shopping.merchant_lfp_v1.types.LfpMerchantState.CountrySettings.VerificationState):
                Output only. The verification state of this
                merchant's pickup serving feature.
        """

        class VerificationState(proto.Enum):
            r"""The possible verification states for different merchant
            programs.

            Values:
                VERIFICATION_STATE_UNSPECIFIED (0):
                    Verification state unspecified.
                VERIFICATION_STATE_NOT_APPROVED (1):
                    Verification state not approved.
                VERIFICATION_STATE_IN_PROGRESS (2):
                    Verification state in progress.
                VERIFICATION_STATE_APPROVED (3):
                    Verification state approved.
            """

            VERIFICATION_STATE_UNSPECIFIED = 0
            VERIFICATION_STATE_NOT_APPROVED = 1
            VERIFICATION_STATE_IN_PROGRESS = 2
            VERIFICATION_STATE_APPROVED = 3

        class ProductPageType(proto.Enum):
            r"""The possible `product page
            types <https://support.google.com/merchants/topic/15148370>`__ for a
            merchant.

            Values:
                PRODUCT_PAGE_TYPE_UNSPECIFIED (0):
                    Product page type unspecified.
                GOOGLE_HOSTED (1):
                    Google hosted product page.
                MERCHANT_HOSTED (2):
                    Merchant hosted product page.
                MERCHANT_HOSTED_STORE_SPECIFIC (3):
                    Merchant hosted store specific product page.
            """

            PRODUCT_PAGE_TYPE_UNSPECIFIED = 0
            GOOGLE_HOSTED = 1
            MERCHANT_HOSTED = 2
            MERCHANT_HOSTED_STORE_SPECIFIC = 3

        region_code: str = proto.Field(
            proto.STRING,
            number=1,
        )
        free_local_listings_enabled: bool = proto.Field(
            proto.BOOL,
            number=2,
        )
        local_inventory_ads_enabled: bool = proto.Field(
            proto.BOOL,
            number=3,
        )
        inventory_verification_state: "LfpMerchantState.CountrySettings.VerificationState" = proto.Field(
            proto.ENUM,
            number=4,
            enum="LfpMerchantState.CountrySettings.VerificationState",
        )
        product_page_type: "LfpMerchantState.CountrySettings.ProductPageType" = (
            proto.Field(
                proto.ENUM,
                number=5,
                enum="LfpMerchantState.CountrySettings.ProductPageType",
            )
        )
        instock_serving_verification_state: "LfpMerchantState.CountrySettings.VerificationState" = proto.Field(
            proto.ENUM,
            number=6,
            enum="LfpMerchantState.CountrySettings.VerificationState",
        )
        pickup_serving_verification_state: "LfpMerchantState.CountrySettings.VerificationState" = proto.Field(
            proto.ENUM,
            number=7,
            enum="LfpMerchantState.CountrySettings.VerificationState",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    linked_gbps: int = proto.Field(
        proto.INT64,
        number=2,
    )
    store_states: MutableSequence[LfpStoreState] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=LfpStoreState,
    )
    inventory_stats: InventoryStats = proto.Field(
        proto.MESSAGE,
        number=4,
        message=InventoryStats,
    )
    country_settings: MutableSequence[CountrySettings] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message=CountrySettings,
    )


class GetLfpMerchantStateRequest(proto.Message):
    r"""Request message for the GetLfpMerchantState method.

    Attributes:
        name (str):
            Required. The name of the state to retrieve. Format:
            ``accounts/{account}/lfpMerchantStates/{target_merchant}``.
            For example, ``accounts/123456/lfpMerchantStates/567890``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
