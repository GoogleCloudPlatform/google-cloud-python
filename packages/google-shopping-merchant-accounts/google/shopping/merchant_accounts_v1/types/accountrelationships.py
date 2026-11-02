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
        "AccountRelationship",
        "GetAccountRelationshipRequest",
        "UpdateAccountRelationshipRequest",
        "ListAccountRelationshipsRequest",
        "ListAccountRelationshipsResponse",
    },
)


class AccountRelationship(proto.Message):
    r"""The ``AccountRelationship`` message defines a formal connection
    between a merchant's account and a service provider's account. This
    relationship enables the provider to offer specific services to the
    business, such as product management or campaign management. It
    specifies the access rights and permissions to the business's data
    relevant to those services.

    Establishing an account relationship involves linking the merchant's
    account with a provider's account. The provider could be another
    Google account (like Google Ads or Google My Business) or a
    third-party platform (such as Shopify or WooCommerce).


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the account relationship.
            Format: ``accounts/{account}/relationships/{relationship}``.
            For example, ``accounts/123456/relationships/567890``.
        provider (str):
            Immutable. The provider of the service. Either the reference
            to an account such as ``providers/123`` or a well-known
            service provider (one of ``providers/GOOGLE_ADS`` or
            ``providers/GOOGLE_BUSINESS_PROFILE``).

            This field is a member of `oneof`_ ``_provider``.
        provider_display_name (str):
            Output only. The human-readable display name
            of the provider account.
        account_id_alias (str):
            Optional. An optional alias you can assign to this account
            relationship. This alias acts as a convenient identifier for
            your own reference and management. It must be unique among
            all your account relationships with the same provider.

            For example, you might use ``account_id_alias`` to assign a
            friendly name to this relationship for easier identification
            in your systems.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    provider: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    provider_display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    account_id_alias: str = proto.Field(
        proto.STRING,
        number=4,
    )


class GetAccountRelationshipRequest(proto.Message):
    r"""Request to get an account relationship.

    Attributes:
        name (str):
            Required. The resource name of the account relationship to
            get. Format:
            ``accounts/{account}/relationships/{relationship}``. For
            example, ``accounts/123456/relationships/567890``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateAccountRelationshipRequest(proto.Message):
    r"""Request message for the ``UpdateAccountRelationship`` method.

    Attributes:
        account_relationship (google.shopping.merchant_accounts_v1.types.AccountRelationship):
            Required. The new version of the account
            relationship.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. List of fields being updated.

            The following fields are supported (in both ``snake_case``
            and ``lowerCamelCase``):

            - ``account_id_alias``
    """

    account_relationship: "AccountRelationship" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="AccountRelationship",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class ListAccountRelationshipsRequest(proto.Message):
    r"""Request to list account relationships.

    Attributes:
        parent (str):
            Required. The parent account of the account relationship to
            filter by. Format: ``accounts/{account}``
        page_token (str):
            Optional. The token returned by the previous ``list``
            request.
        page_size (int):
            Optional. The maximum number of elements to return in the
            response. Use for paging. If no ``page_size`` is specified,
            ``100`` is used as the default value. The maximum allowed
            value is ``1000``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=4,
    )


class ListAccountRelationshipsResponse(proto.Message):
    r"""Response after trying to list account relationships.

    Attributes:
        account_relationships (MutableSequence[google.shopping.merchant_accounts_v1.types.AccountRelationship]):
            The account relationships that match your
            filter.
        next_page_token (str):
            A page token. You can send the ``page_token`` to get the
            next page. Only included in the ``list`` response if there
            are more pages.
    """

    @property
    def raw_page(self):
        return self

    account_relationships: MutableSequence["AccountRelationship"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AccountRelationship",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
