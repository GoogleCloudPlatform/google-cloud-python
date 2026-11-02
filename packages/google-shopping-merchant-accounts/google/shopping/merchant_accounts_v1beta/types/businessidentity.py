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
    package="google.shopping.merchant.accounts.v1beta",
    manifest={
        "BusinessIdentity",
        "GetBusinessIdentityRequest",
        "UpdateBusinessIdentityRequest",
    },
)


class BusinessIdentity(proto.Message):
    r"""Collection of information related to the `identity of a
    business <https://support.google.com/merchants/answer/12564247>`__.

    Attributes:
        name (str):
            Identifier. The resource name of the business identity.
            Format: ``accounts/{account}/businessIdentity``
        promotions_consent (google.shopping.merchant_accounts_v1beta.types.BusinessIdentity.PromotionsConsent):
            Optional. Whether the identity attributes may
            be used for promotions.
        black_owned (google.shopping.merchant_accounts_v1beta.types.BusinessIdentity.IdentityAttribute):
            Optional. Specifies whether the business identifies itself
            as being black-owned. This optional field will only be
            available for merchants with a business country set to
            ``US``. It is also not applicable for marketplaces or
            marketplace sellers.
        women_owned (google.shopping.merchant_accounts_v1beta.types.BusinessIdentity.IdentityAttribute):
            Optional. Specifies whether the business identifies itself
            as being women-owned. This optional field will only be
            available for merchants with a business country set to
            ``US``. It is also not applicable for marketplaces or
            marketplace sellers.
        veteran_owned (google.shopping.merchant_accounts_v1beta.types.BusinessIdentity.IdentityAttribute):
            Optional. Specifies whether the business identifies itself
            as being veteran-owned. This optional field will only be
            available for merchants with a business country set to
            ``US``. It is also not applicable for marketplaces or
            marketplace sellers.
        latino_owned (google.shopping.merchant_accounts_v1beta.types.BusinessIdentity.IdentityAttribute):
            Optional. Specifies whether the business identifies itself
            as being latino-owned. This optional field will only be
            available for merchants with a business country set to
            ``US``. It is also not applicable for marketplaces or
            marketplace sellers.
        small_business (google.shopping.merchant_accounts_v1beta.types.BusinessIdentity.IdentityAttribute):
            Optional. Specifies whether the business identifies itself
            as a small business. This optional field will only be
            available for merchants with a business country set to
            ``US``. It is also not applicable for marketplaces.
    """

    class PromotionsConsent(proto.Enum):
        r"""All possible settings regarding promotions related to the
        business identity.

        Values:
            PROMOTIONS_CONSENT_UNSPECIFIED (0):
                Default value indicating that no selection
                was made.
            PROMOTIONS_CONSENT_GIVEN (1):
                Indicates that the account consented to
                having their business identity used for
                promotions.
            PROMOTIONS_CONSENT_DENIED (2):
                Indicates that the account did not consent to
                having their business identity used for
                promotions.
        """

        PROMOTIONS_CONSENT_UNSPECIFIED = 0
        PROMOTIONS_CONSENT_GIVEN = 1
        PROMOTIONS_CONSENT_DENIED = 2

    class IdentityAttribute(proto.Message):
        r"""All information related to an identity attribute.

        Attributes:
            identity_declaration (google.shopping.merchant_accounts_v1beta.types.BusinessIdentity.IdentityAttribute.IdentityDeclaration):
                Required. The declaration of identity for
                this attribute.
        """

        class IdentityDeclaration(proto.Enum):
            r"""All possible settings regarding the declaration of an
            identity.

            Values:
                IDENTITY_DECLARATION_UNSPECIFIED (0):
                    Default value indicating that no selection
                    was made.
                SELF_IDENTIFIES_AS (1):
                    Indicates that the account identifies with
                    the attribute.
                DOES_NOT_SELF_IDENTIFY_AS (2):
                    Indicates that the account does not identify
                    with the attribute.
            """

            IDENTITY_DECLARATION_UNSPECIFIED = 0
            SELF_IDENTIFIES_AS = 1
            DOES_NOT_SELF_IDENTIFY_AS = 2

        identity_declaration: "BusinessIdentity.IdentityAttribute.IdentityDeclaration" = proto.Field(
            proto.ENUM,
            number=1,
            enum="BusinessIdentity.IdentityAttribute.IdentityDeclaration",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    promotions_consent: PromotionsConsent = proto.Field(
        proto.ENUM,
        number=2,
        enum=PromotionsConsent,
    )
    black_owned: IdentityAttribute = proto.Field(
        proto.MESSAGE,
        number=3,
        message=IdentityAttribute,
    )
    women_owned: IdentityAttribute = proto.Field(
        proto.MESSAGE,
        number=4,
        message=IdentityAttribute,
    )
    veteran_owned: IdentityAttribute = proto.Field(
        proto.MESSAGE,
        number=5,
        message=IdentityAttribute,
    )
    latino_owned: IdentityAttribute = proto.Field(
        proto.MESSAGE,
        number=6,
        message=IdentityAttribute,
    )
    small_business: IdentityAttribute = proto.Field(
        proto.MESSAGE,
        number=7,
        message=IdentityAttribute,
    )


class GetBusinessIdentityRequest(proto.Message):
    r"""Request message for the ``GetBusinessIdentity`` method.

    Attributes:
        name (str):
            Required. The resource name of the business identity.
            Format: ``accounts/{account}/businessIdentity``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateBusinessIdentityRequest(proto.Message):
    r"""Request message for the ``UpdateBusinessIdentity`` method.

    Attributes:
        business_identity (google.shopping.merchant_accounts_v1beta.types.BusinessIdentity):
            Required. The new version of the business
            identity.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. List of fields being updated.
    """

    business_identity: "BusinessIdentity" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="BusinessIdentity",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
