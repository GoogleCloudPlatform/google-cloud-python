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
    package="google.shopping.merchant.loyaltycustomers.v1",
    manifest={
        "AddressInfo",
        "UserIdentifier",
        "LoyaltyCustomer",
        "ManageLoyaltyCustomerMatchRequest",
        "ManageLoyaltyCustomerMatchResponse",
    },
)


class AddressInfo(proto.Message):
    r"""Represents a customer’s physical address.

    Attributes:
        given_name (str):
            Optional. The given name of the customer.
        family_name (str):
            Optional. The family name of the customer.
        city (str):
            Optional. The city of the customer.
        state (str):
            Optional. The state or province of the
            customer.
        region_code (str):
            Optional. The Unicode country/region code (CLDR) of the
            customer, such as "US" or "CH". This field is
            case-insensitive. For more information, see
            https://cldr.unicode.org/ and
            https://www.unicode.org/cldr/charts/latest/supplemental/territory_containment_un_m_49.html.
        postal_code (str):
            Optional. The postal code (zip code) of the customer.

            **Format Rules:**

            - **United States:** 5-digit zip codes (e.g., "94108").
    """

    given_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    family_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    city: str = proto.Field(
        proto.STRING,
        number=3,
    )
    state: str = proto.Field(
        proto.STRING,
        number=4,
    )
    region_code: str = proto.Field(
        proto.STRING,
        number=5,
    )
    postal_code: str = proto.Field(
        proto.STRING,
        number=6,
    )


class UserIdentifier(proto.Message):
    r"""The user identifiers associated with the customer.
    At least one of the fields within this message must be provided.

    Attributes:
        email_address (str):
            Optional. The customer’s email address.
        address (google.shopping.merchant_loyaltycustomers_v1.types.AddressInfo):
            Optional. The customer’s physical address.
        phone_number (str):
            Optional. The customer's phone number, in `E.164
            format <https://support.google.com/google-ads/answer/16355235>`__
            (e.g., "+16502530000").
    """

    email_address: str = proto.Field(
        proto.STRING,
        number=1,
    )
    address: "AddressInfo" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="AddressInfo",
    )
    phone_number: str = proto.Field(
        proto.STRING,
        number=3,
    )


class LoyaltyCustomer(proto.Message):
    r"""Represents a customer’s loyalty information. Represents loyalty
    customer data in ``ManageLoyaltyCustomerMatch`` API, but is not a
    resource that can be retrieved or listed by other methods.

    Attributes:
        user_identifier (google.shopping.merchant_loyaltycustomers_v1.types.UserIdentifier):
            Required. The identifiers for the customer.
        loyalty_tier (google.shopping.merchant_loyaltycustomers_v1.types.LoyaltyCustomer.LoyaltyTier):
            Required. The tier label of the loyalty tier
            the customer belongs to.
        point_balance (int):
            Optional. The point balance of the loyalty
            customer.
    """

    class LoyaltyTier(proto.Enum):
        r"""The tier label of the loyalty tier the customer belongs to.

        Values:
            LOYALTY_TIER_UNSPECIFIED (0):
                Loyalty tier unspecified.
            TIER1 (1):
                Loyalty tier 1.
            TIER2 (2):
                Loyalty tier 2.
            TIER3 (3):
                Loyalty tier 3.
            TIER4 (4):
                Loyalty tier 4.
            TIER5 (5):
                Loyalty tier 5.
            TIER6 (6):
                Loyalty tier 6.
            TIER7 (7):
                Loyalty tier 7.
            NON_MEMBER (8):
                Disassociates the user from any loyalty tier. Only set to
                “NON_MEMBER” when the intent is to remove the user
                association from Google organic loyalty customer match
                experience.
        """

        LOYALTY_TIER_UNSPECIFIED = 0
        TIER1 = 1
        TIER2 = 2
        TIER3 = 3
        TIER4 = 4
        TIER5 = 5
        TIER6 = 6
        TIER7 = 7
        NON_MEMBER = 8

    user_identifier: "UserIdentifier" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="UserIdentifier",
    )
    loyalty_tier: LoyaltyTier = proto.Field(
        proto.ENUM,
        number=2,
        enum=LoyaltyTier,
    )
    point_balance: int = proto.Field(
        proto.INT64,
        number=3,
    )


class ManageLoyaltyCustomerMatchRequest(proto.Message):
    r"""Request message for the ManageLoyaltyCustomerMatch method.

    Attributes:
        parent (str):
            Required. The parent account where this loyalty customer
            will be handled. Format: ``accounts/{account}``
        loyalty_customer (google.shopping.merchant_loyaltycustomers_v1.types.LoyaltyCustomer):
            Required. The loyalty customer to insert,
            update, or remove.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    loyalty_customer: "LoyaltyCustomer" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="LoyaltyCustomer",
    )


class ManageLoyaltyCustomerMatchResponse(proto.Message):
    r"""Response message for the ManageLoyaltyCustomerMatch method.

    Attributes:
        loyalty_customer (google.shopping.merchant_loyaltycustomers_v1.types.LoyaltyCustomer):
            The loyalty customer that was inserted, updated, or removed.
            If the customer's identifier cannot be matched to a Google
            account or if the user has not opted into loyalty
            personalization, this field will contain a default
            ``LoyaltyCustomer`` instance.
    """

    loyalty_customer: "LoyaltyCustomer" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="LoyaltyCustomer",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
