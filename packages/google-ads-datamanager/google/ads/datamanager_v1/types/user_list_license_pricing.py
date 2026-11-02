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
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.ads.datamanager.v1",
    manifest={
        "UserListLicensePricing",
    },
)


class UserListLicensePricing(proto.Message):
    r"""A user list license pricing.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        pricing_id (int):
            Output only. The ID of this pricing.
        cost_micros (int):
            Optional. The cost associated with the model, in micro units
            (10^-6), in the currency specified by the currency_code
            field. For example, 2000000 means $2 if ``currency_code`` is
            ``USD``.

            This field is a member of `oneof`_ ``_cost_micros``.
        currency_code (str):
            Optional. The currency in which cost and max_cost is
            specified. Must be a three-letter currency code defined in
            ISO 4217.

            This field is a member of `oneof`_ ``_currency_code``.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Start time of the pricing.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. End time of the pricing.
        pricing_active (bool):
            Output only. Whether this pricing is active.
        buyer_approval_state (google.ads.datamanager_v1.types.UserListLicensePricing.UserListPricingBuyerApprovalState):
            Output only. The buyer approval state of this
            pricing.
            This field is read-only.
        cost_type (google.ads.datamanager_v1.types.UserListLicensePricing.UserListPricingCostType):
            Immutable. The cost type of this pricing.

            Can be set only in the ``create`` operation. Can't be
            updated for an existing license.

            This field is a member of `oneof`_ ``_cost_type``.
        max_cost_micros (int):
            Optional. The maximum CPM a commerce audience can be charged
            when the MEDIA_SHARE cost type is used. The value is in
            micro units (10^-6) and in the currency specified by the
            currency_code field. For example, 2000000 means $2 if
            ``currency_code`` is ``USD``.

            This is only relevant when cost_type is MEDIA_SHARE. When
            cost_type is not MEDIA_SHARE, and this field is set, a
            MAX_COST_NOT_ALLOWED error will be returned. If not set or
            set to\ ``0``, there is no cap.

            This field is a member of `oneof`_ ``_max_cost_micros``.
    """

    class UserListPricingBuyerApprovalState(proto.Enum):
        r"""User list pricing buyer approval state.

        Values:
            USER_LIST_PRICING_BUYER_APPROVAL_STATE_UNSPECIFIED (0):
                UNSPECIFIED.
            PENDING (1):
                User list client has not yet accepted the
                pricing terms set by the user list owner.
            APPROVED (2):
                User list client has accepted the pricing
                terms set by the user list owner.
            REJECTED (3):
                User list client has rejected the pricing
                terms set by the user list owner.
        """

        USER_LIST_PRICING_BUYER_APPROVAL_STATE_UNSPECIFIED = 0
        PENDING = 1
        APPROVED = 2
        REJECTED = 3

    class UserListPricingCostType(proto.Enum):
        r"""User list pricing cost type.

        Values:
            USER_LIST_PRICING_COST_TYPE_UNSPECIFIED (0):
                Unspecified.
            CPC (1):
                Cost per click.
            CPM (2):
                Cost per mille (thousand impressions).
            MEDIA_SHARE (3):
                Media share.
        """

        USER_LIST_PRICING_COST_TYPE_UNSPECIFIED = 0
        CPC = 1
        CPM = 2
        MEDIA_SHARE = 3

    pricing_id: int = proto.Field(
        proto.INT64,
        number=1,
    )
    cost_micros: int = proto.Field(
        proto.INT64,
        number=2,
        optional=True,
    )
    currency_code: str = proto.Field(
        proto.STRING,
        number=9,
        optional=True,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    pricing_active: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    buyer_approval_state: UserListPricingBuyerApprovalState = proto.Field(
        proto.ENUM,
        number=6,
        enum=UserListPricingBuyerApprovalState,
    )
    cost_type: UserListPricingCostType = proto.Field(
        proto.ENUM,
        number=7,
        optional=True,
        enum=UserListPricingCostType,
    )
    max_cost_micros: int = proto.Field(
        proto.INT64,
        number=8,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
