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
import google.type.phone_number_pb2 as phone_number_pb2  # type: ignore
import google.type.postal_address_pb2 as postal_address_pb2  # type: ignore
import proto  # type: ignore

from google.shopping.merchant_accounts_v1beta.types import (
    customerservice,
    phoneverificationstate,
)

__protobuf__ = proto.module(
    package="google.shopping.merchant.accounts.v1beta",
    manifest={
        "BusinessInfo",
        "GetBusinessInfoRequest",
        "UpdateBusinessInfoRequest",
    },
)


class BusinessInfo(proto.Message):
    r"""Collection of information related to a business.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the business info. Format:
            ``accounts/{account}/businessInfo``
        address (google.type.postal_address_pb2.PostalAddress):
            Optional. The address of the business.

            This field is a member of `oneof`_ ``_address``.
        phone (google.type.phone_number_pb2.PhoneNumber):
            Output only. The phone number of the
            business.

            This field is a member of `oneof`_ ``_phone``.
        phone_verification_state (google.shopping.merchant_accounts_v1beta.types.PhoneVerificationState):
            Output only. The phone verification state of
            the business.

            This field is a member of `oneof`_ ``_phone_verification_state``.
        customer_service (google.shopping.merchant_accounts_v1beta.types.CustomerService):
            Optional. The customer service of the
            business.

            This field is a member of `oneof`_ ``_customer_service``.
        korean_business_registration_number (str):
            Optional. The 10-digit `Korean business registration
            number <https://support.google.com/merchants/answer/9037766>`__
            separated with dashes in the format: XXX-XX-XXXXX.

            This field is a member of `oneof`_ ``_korean_business_registration_number``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    address: postal_address_pb2.PostalAddress = proto.Field(
        proto.MESSAGE,
        number=2,
        optional=True,
        message=postal_address_pb2.PostalAddress,
    )
    phone: phone_number_pb2.PhoneNumber = proto.Field(
        proto.MESSAGE,
        number=3,
        optional=True,
        message=phone_number_pb2.PhoneNumber,
    )
    phone_verification_state: phoneverificationstate.PhoneVerificationState = (
        proto.Field(
            proto.ENUM,
            number=4,
            optional=True,
            enum=phoneverificationstate.PhoneVerificationState,
        )
    )
    customer_service: customerservice.CustomerService = proto.Field(
        proto.MESSAGE,
        number=5,
        optional=True,
        message=customerservice.CustomerService,
    )
    korean_business_registration_number: str = proto.Field(
        proto.STRING,
        number=6,
        optional=True,
    )


class GetBusinessInfoRequest(proto.Message):
    r"""Request message for the ``GetBusinessInfo`` method.

    Attributes:
        name (str):
            Required. The resource name of the business info. Format:
            ``accounts/{account}/businessInfo``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateBusinessInfoRequest(proto.Message):
    r"""Request message for the ``UpdateBusinessInfo`` method.

    Attributes:
        business_info (google.shopping.merchant_accounts_v1beta.types.BusinessInfo):
            Required. The new version of the business
            info.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. List of fields being updated.
    """

    business_info: "BusinessInfo" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="BusinessInfo",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
