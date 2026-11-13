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

from google.ads.datamanager_v1.types import destination

__protobuf__ = proto.module(
    package="google.ads.datamanager.v1",
    manifest={
        "FeatureSet",
        "CreatePartnerLinkRequest",
        "DeletePartnerLinkRequest",
        "SearchPartnerLinksRequest",
        "SearchPartnerLinksResponse",
        "PartnerLink",
        "PartnerCustomerAccount",
        "PartnerLinkMetadata",
    },
)


class FeatureSet(proto.Enum):
    r"""The set of supported features for a partner link.

    Values:
        FEATURE_SET_UNSPECIFIED (0):
            Unspecified feature set. If unspecified, the system behavior
            defaults to
            [FEATURE_SET_AUDIENCE_AND_EVENT_MANAGEMENT][google.ads.datamanager.v1.FeatureSet.FEATURE_SET_AUDIENCE_AND_EVENT_MANAGEMENT].
        FEATURE_SET_AUDIENCE_AND_EVENT_MANAGEMENT (1):
            Indicates a link used for audience and event
            management.
        FEATURE_SET_AD_EVENT_MANAGEMENT (2):
            Indicates a link used for ad event
            management.
    """

    FEATURE_SET_UNSPECIFIED = 0
    FEATURE_SET_AUDIENCE_AND_EVENT_MANAGEMENT = 1
    FEATURE_SET_AD_EVENT_MANAGEMENT = 2


class CreatePartnerLinkRequest(proto.Message):
    r"""Request to create a
    [PartnerLink][google.ads.datamanager.v1.PartnerLink] resource.
    Returns a [PartnerLink][google.ads.datamanager.v1.PartnerLink].

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of partner
            links. Format:
            accountTypes/{account_type}/accounts/{account}
        partner_link (google.ads.datamanager_v1.types.PartnerLink):
            Required. The partner link to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    partner_link: "PartnerLink" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="PartnerLink",
    )


class DeletePartnerLinkRequest(proto.Message):
    r"""Request to delete a
    [PartnerLink][google.ads.datamanager.v1.PartnerLink] resource.
    Returns a [google.protobuf.Empty][google.protobuf.Empty].

    Attributes:
        name (str):
            Required. The resource name of the partner link to delete.
            Format:
            accountTypes/{account_type}/accounts/{account}/partnerLinks/{partner_link}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class SearchPartnerLinksRequest(proto.Message):
    r"""Request to search for
    [PartnerLink][google.ads.datamanager.v1.PartnerLink] resources.
    Returns a
    [SearchPartnerLinksResponse][google.ads.datamanager.v1.SearchPartnerLinksResponse].

    Attributes:
        parent (str):
            Required. Account to search for partner links. If no
            ``filter`` is specified, all partner links where this
            account is either the ``owning_account`` or
            ``partner_account`` are returned.

            Format: ``accountTypes/{account_type}/accounts/{account}``
        page_size (int):
            The maximum number of partner links to
            return. The service may return fewer than this
            value. If unspecified, at most 50 partner links
            will be returned. The maximum value is 100;
            values above 100 will be coerced to 100.
        page_token (str):
            A page token, received from a previous
            ``SearchPartnerLinks`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``SearchPartnerLinks`` must match the call that provided the
            page token.
        filter (str):
            Optional. A `filter string <https://google.aip.dev/160>`__.
            All fields need to be on the left hand side of each
            condition (for example: ``partner_link_id = 123456789``).
            Fields must be specified using either all `camel
            case <https://en.wikipedia.org/wiki/Camel_case>`__ or all
            `snake case <https://en.wikipedia.org/wiki/Snake_case>`__.
            Don't use a combination of camel case and snake case.

            Supported operations:

            - ``AND``
            - ``=``
            - ``!=``

            Supported fields:

            - ``partner_link_id``
            - ``owning_account.account_type``
            - ``owning_account.account_id``
            - ``partner_account.account_type``
            - ``partner_account.account_id``
            - ``feature_set``

            For partner links with the
            [FEATURE_SET_AD_EVENT_MANAGEMENT][google.ads.datamanager.v1.FeatureSet.FEATURE_SET_AD_EVENT_MANAGEMENT]
            feature set, the following fields are also supported:

            - ``partner_customer_account.account_id``
            - ``partner_link_metadata.implicit_accounts.account_id``

            Example:
            ``owning_account.account_type = "GOOGLE_ADS" AND partner_account.account_id = 987654321``
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
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )


class SearchPartnerLinksResponse(proto.Message):
    r"""Response from the
    [SearchPartnerLinksRequest][google.ads.datamanager.v1.SearchPartnerLinksRequest].

    Attributes:
        partner_links (MutableSequence[google.ads.datamanager_v1.types.PartnerLink]):
            The partner links for the given account.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    partner_links: MutableSequence["PartnerLink"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="PartnerLink",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class PartnerLink(proto.Message):
    r"""A partner link between an owning account and a partner
    account.

    Attributes:
        name (str):
            Identifier. The name of the partner link. Format:
            accountTypes/{account_type}/accounts/{account}/partnerLinks/{partner_link}
        partner_link_id (str):
            Output only. The partner link ID.
        owning_account (google.ads.datamanager_v1.types.ProductAccount):
            Required. The owning account granting access
            to the partner account.
        partner_account (google.ads.datamanager_v1.types.ProductAccount):
            Required. The partner account granted access
            by the owning account.
        feature_set (google.ads.datamanager_v1.types.FeatureSet):
            Optional. Immutable. The set of features supported for the
            partner link. If not specified, the system behavior defaults
            to
            [FEATURE_SET_AUDIENCE_AND_EVENT_MANAGEMENT][google.ads.datamanager.v1.FeatureSet.FEATURE_SET_AUDIENCE_AND_EVENT_MANAGEMENT].
        partner_customer_account (google.ads.datamanager_v1.types.PartnerCustomerAccount):
            Optional. The customer account in the partner system. This
            is required for partner links with the
            [FEATURE_SET_AD_EVENT_MANAGEMENT][google.ads.datamanager.v1.FeatureSet.FEATURE_SET_AD_EVENT_MANAGEMENT]
            feature set.
        partner_link_metadata (google.ads.datamanager_v1.types.PartnerLinkMetadata):
            Optional. Metadata associated with the partner link. This is
            optional and only accepted for partner links with the
            [FEATURE_SET_AD_EVENT_MANAGEMENT][google.ads.datamanager.v1.FeatureSet.FEATURE_SET_AD_EVENT_MANAGEMENT].
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    partner_link_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    owning_account: destination.ProductAccount = proto.Field(
        proto.MESSAGE,
        number=3,
        message=destination.ProductAccount,
    )
    partner_account: destination.ProductAccount = proto.Field(
        proto.MESSAGE,
        number=4,
        message=destination.ProductAccount,
    )
    feature_set: "FeatureSet" = proto.Field(
        proto.ENUM,
        number=5,
        enum="FeatureSet",
    )
    partner_customer_account: "PartnerCustomerAccount" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="PartnerCustomerAccount",
    )
    partner_link_metadata: "PartnerLinkMetadata" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="PartnerLinkMetadata",
    )


class PartnerCustomerAccount(proto.Message):
    r"""Represents a customer account in the partner's system.

    Attributes:
        account_id (str):
            Required. The identifier of the customer
            account in the partner's ID space.
        account_name (str):
            Optional. The name of the account.
        account_type (str):
            Optional. The type of the account. Can be
            used to distinguish between advertiser accounts
            and business level accounts, for example.
    """

    account_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    account_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    account_type: str = proto.Field(
        proto.STRING,
        number=3,
    )


class PartnerLinkMetadata(proto.Message):
    r"""Represents metadata associated with a partner link.

    Attributes:
        implicit_accounts (MutableSequence[google.ads.datamanager_v1.types.PartnerCustomerAccount]):
            Optional. The list of implicit accounts.
    """

    implicit_accounts: MutableSequence["PartnerCustomerAccount"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="PartnerCustomerAccount",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
