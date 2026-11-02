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
from google.shopping.type.types import types

__protobuf__ = proto.module(
    package="google.shopping.merchant.accounts.v1beta",
    manifest={
        "GetCheckoutSettingsRequest",
        "CreateCheckoutSettingsRequest",
        "UpdateCheckoutSettingsRequest",
        "DeleteCheckoutSettingsRequest",
        "CheckoutSettings",
        "UriSettings",
    },
)


class GetCheckoutSettingsRequest(proto.Message):
    r"""Request message for ``GetCheckoutSettings`` method.

    Attributes:
        name (str):
            Required. The name/identifier of the merchant account.
            Format:
            ``accounts/{account}/programs/{program}/checkoutSettings``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateCheckoutSettingsRequest(proto.Message):
    r"""Request message for the ``CreateCheckoutSettings`` method.

    Attributes:
        parent (str):
            Required. The merchant account for which the
            ``CheckoutSettings`` will be created.
        checkout_settings (google.shopping.merchant_accounts_v1beta.types.CheckoutSettings):
            Required. The ``CheckoutSettings`` object to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    checkout_settings: "CheckoutSettings" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="CheckoutSettings",
    )


class UpdateCheckoutSettingsRequest(proto.Message):
    r"""Request message for the ``UpdateCheckoutSettings`` method.

    Attributes:
        checkout_settings (google.shopping.merchant_accounts_v1beta.types.CheckoutSettings):
            Required. The updated version of the ``CheckoutSettings``.
            The ``name`` field is used to identify the
            ``CheckoutSettings``. Format:
            ``accounts/{account}/programs/{program}/checkoutSettings``
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. List of fields being updated. The following fields
            are supported (in both ``snake_case`` and
            ``lowerCamelCase``):

            - ``eligible_destinations``
            - ``uri_settings``
    """

    checkout_settings: "CheckoutSettings" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="CheckoutSettings",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteCheckoutSettingsRequest(proto.Message):
    r"""Request message for the ``DeleteCheckoutSettings`` method.

    Attributes:
        name (str):
            Required. The name/identifier of the merchant account.
            Format:
            ``accounts/{account}/programs/{program}/checkoutSettings``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CheckoutSettings(proto.Message):
    r"""`CheckoutSettings <https://support.google.com/merchants/answer/13945960>`__
    for a specific merchant.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the program configuration
            settings. Format:
            ``accounts/{account}/programs/{program}/checkoutSettings``
        uri_settings (google.shopping.merchant_accounts_v1beta.types.UriSettings):
            URI settings for cart or checkout URL.

            This field is a member of `oneof`_ ``_uri_settings``.
        eligible_destinations (MutableSequence[google.shopping.type.types.Destination.DestinationEnum]):
            Optional. The destinations to which the checkout program
            applies, valid destination values are ``SHOPPING_ADS``,
            ``FREE_LISTINGS``
        enrollment_state (google.shopping.merchant_accounts_v1beta.types.CheckoutSettings.CheckoutEnrollmentState):
            Output only. Reflects the merchant enrollment state in
            ``Checkout`` program.

            This field is a member of `oneof`_ ``_enrollment_state``.
        review_state (google.shopping.merchant_accounts_v1beta.types.CheckoutSettings.CheckoutReviewState):
            Output only. Reflects the merchant review state in
            ``Checkout`` program. This is set based on the data quality
            reviews of the URL provided by the merchant. A merchant with
            enrollment state as ``ENROLLED`` can be in the following
            review states: ``IN_REVIEW``, ``APPROVED`` or
            ``DISAPPROVED``. A merchant must be in an
            ``enrollment_state`` of ``ENROLLED`` before a review can
            begin for the merchant.For more details, check the help
            center doc.

            This field is a member of `oneof`_ ``_review_state``.
        effective_uri_settings (google.shopping.merchant_accounts_v1beta.types.UriSettings):
            Output only. The effective value of ``uri_settings`` for a
            given merchant. If account level settings are present then
            this value will be a copy of url settings. Otherwise, it
            will have the value of the parent account (for only
            marketplace sellers).
        effective_enrollment_state (google.shopping.merchant_accounts_v1beta.types.CheckoutSettings.CheckoutEnrollmentState):
            Output only. The effective value of enrollment_state for a
            given merchant ID. If account level settings are present
            then this value will be a copy of the account level
            settings. Otherwise, it will have the value of the parent
            account (for only marketplace sellers).

            This field is a member of `oneof`_ ``_effective_enrollment_state``.
        effective_review_state (google.shopping.merchant_accounts_v1beta.types.CheckoutSettings.CheckoutReviewState):
            Output only. The effective value of ``review_state`` for a
            given merchant ID. If account level settings are present
            then this value will be a copy of the account level
            settings. Otherwise, it will have the value of the parent
            account (for only marketplace sellers).

            This field is a member of `oneof`_ ``_effective_review_state``.
    """

    class CheckoutEnrollmentState(proto.Enum):
        r"""Enum indicating the enrollment state of merchant in ``Checkout``
        program.

        Values:
            CHECKOUT_ENROLLMENT_STATE_UNSPECIFIED (0):
                Default enrollment state when enrollment
                state is not specified.
            INACTIVE (1):
                Merchant has not enrolled into the program.
            ENROLLED (2):
                Merchant has enrolled into the program by
                providing either an account level URL or
                checkout URLs as part of their feed.
            OPTED_OUT (3):
                Merchant has previously enrolled but opted
                out of the program.
        """

        CHECKOUT_ENROLLMENT_STATE_UNSPECIFIED = 0
        INACTIVE = 1
        ENROLLED = 2
        OPTED_OUT = 3

    class CheckoutReviewState(proto.Enum):
        r"""Enum indicating the review state of merchant in ``Checkout``
        program.

        Values:
            CHECKOUT_REVIEW_STATE_UNSPECIFIED (0):
                Default review state when review state is not
                specified.
            IN_REVIEW (1):
                Merchant provided URLs are being reviewed for
                data quality issues.
            APPROVED (2):
                Merchant account has been approved. Indicates
                the data quality checks have passed.
            DISAPPROVED (3):
                Merchant account has been disapproved due to
                data quality issues.
        """

        CHECKOUT_REVIEW_STATE_UNSPECIFIED = 0
        IN_REVIEW = 1
        APPROVED = 2
        DISAPPROVED = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uri_settings: "UriSettings" = proto.Field(
        proto.MESSAGE,
        number=2,
        optional=True,
        message="UriSettings",
    )
    eligible_destinations: MutableSequence[types.Destination.DestinationEnum] = (
        proto.RepeatedField(
            proto.ENUM,
            number=8,
            enum=types.Destination.DestinationEnum,
        )
    )
    enrollment_state: CheckoutEnrollmentState = proto.Field(
        proto.ENUM,
        number=3,
        optional=True,
        enum=CheckoutEnrollmentState,
    )
    review_state: CheckoutReviewState = proto.Field(
        proto.ENUM,
        number=4,
        optional=True,
        enum=CheckoutReviewState,
    )
    effective_uri_settings: "UriSettings" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="UriSettings",
    )
    effective_enrollment_state: CheckoutEnrollmentState = proto.Field(
        proto.ENUM,
        number=6,
        optional=True,
        enum=CheckoutEnrollmentState,
    )
    effective_review_state: CheckoutReviewState = proto.Field(
        proto.ENUM,
        number=7,
        optional=True,
        enum=CheckoutReviewState,
    )


class UriSettings(proto.Message):
    r"""URL settings for cart or checkout URL.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        checkout_uri_template (str):
            Checkout URL template. When the placeholders are expanded
            will redirect the buyer to the merchant checkout page with
            the item in the cart. For more details, check the `help
            center
            doc <https://support.google.com/merchants/answer/13945960#method1&zippy=%2Cproduct-level-url-formatting%2Caccount-level-url-formatting>`__

            This field is a member of `oneof`_ ``uri_template``.
        cart_uri_template (str):
            Cart URL template. When the placeholders are expanded will
            redirect the buyer to the cart page on the merchant website
            with the selected item in cart. For more details, check the
            `help center
            doc <https://support.google.com/merchants/answer/13945960#method1&zippy=%2Cproduct-level-url-formatting%2Caccount-level-url-formatting>`__

            This field is a member of `oneof`_ ``uri_template``.
    """

    checkout_uri_template: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="uri_template",
    )
    cart_uri_template: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="uri_template",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
