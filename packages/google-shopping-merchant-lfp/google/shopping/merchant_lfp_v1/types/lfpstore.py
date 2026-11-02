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
        "LfpStore",
        "GetLfpStoreRequest",
        "InsertLfpStoreRequest",
        "DeleteLfpStoreRequest",
        "ListLfpStoresRequest",
        "ListLfpStoresResponse",
    },
)


class LfpStore(proto.Message):
    r"""A store for the merchant. This will be used to match to a
    store under the Google Business Profile of the target merchant.
    If a matching store can't be found, the inventories or sales
    submitted with the store code will not be used.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. Identifier. The name of the ``LfpStore``
            resource. Format:
            ``accounts/{account}/lfpStores/{target_merchant}~{store_code}``
        target_account (int):
            Required. The Merchant Center id of the
            merchant to submit the store for.
        store_code (str):
            Required. Immutable. A store identifier that
            is unique for the target merchant.
        store_address (str):
            Required. The street address of the store.
            Example: 1600 Amphitheatre Pkwy, Mountain View,
            CA 94043, USA.
        store_name (str):
            Optional. The merchant or store name.

            This field is a member of `oneof`_ ``_store_name``.
        phone_number (str):
            Optional. The store phone number in
            `E.164 <https://en.wikipedia.org/wiki/E.164>`__ format.
            Example: ``+15556767888``

            This field is a member of `oneof`_ ``_phone_number``.
        website_uri (str):
            Optional. The website URL for the store or
            merchant.

            This field is a member of `oneof`_ ``_website_uri``.
        gcid_category (MutableSequence[str]):
            Optional. `Google My Business category
            id <https://gcid-explorer.corp.google.com/static/gcid.html>`__.
        place_id (str):
            Optional. The `Google Place
            Id <https://developers.google.com/maps/documentation/places/web-service/place-id#id-overview>`__
            of the store location.

            This field is a member of `oneof`_ ``_place_id``.
        matching_state (google.shopping.merchant_lfp_v1.types.LfpStore.StoreMatchingState):
            Optional. Output only. The state of matching to a Google
            Business Profile. See
            [matchingStateHint][google.shopping.merchant.lfp.v1.LfpStore.matching_state_hint]
            for further details if no match is found.
        matching_state_hint (str):
            Optional. Output only. The hint of why the matching has
            failed. This is only set when
            [matchingState][google.shopping.merchant.lfp.v1.LfpStore.matching_state]=\ ``STORE_MATCHING_STATE_FAILED``.

            Possible values are:

            - "``linked-store-not-found``": There aren't any Google
              Business Profile stores available for matching.
            - "``store-match-not-found``": The provided ``LfpStore``
              couldn't be matched to any of the connected Google
              Business Profile stores. Merchant Center account is
              connected correctly and stores are available on Google
              Business Profile, but the ``LfpStore`` location address
              does not match with Google Business Profile stores'
              addresses. Update the ``LfpStore`` address or Google
              Business Profile store address to match correctly.
            - "``store-match-unverified``": The provided ``LfpStore``
              couldn't be matched to any of the connected Google
              Business Profile stores, as the matched Google Business
              Profile store is unverified. Go through the Google
              Business Profile verification process to match correctly.

            This field is a member of `oneof`_ ``_matching_state_hint``.
    """

    class StoreMatchingState(proto.Enum):
        r"""The state of matching ``LfpStore`` to a Google Business Profile.

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

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    target_account: int = proto.Field(
        proto.INT64,
        number=2,
    )
    store_code: str = proto.Field(
        proto.STRING,
        number=3,
    )
    store_address: str = proto.Field(
        proto.STRING,
        number=4,
    )
    store_name: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    phone_number: str = proto.Field(
        proto.STRING,
        number=6,
        optional=True,
    )
    website_uri: str = proto.Field(
        proto.STRING,
        number=7,
        optional=True,
    )
    gcid_category: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    place_id: str = proto.Field(
        proto.STRING,
        number=9,
        optional=True,
    )
    matching_state: StoreMatchingState = proto.Field(
        proto.ENUM,
        number=10,
        enum=StoreMatchingState,
    )
    matching_state_hint: str = proto.Field(
        proto.STRING,
        number=11,
        optional=True,
    )


class GetLfpStoreRequest(proto.Message):
    r"""Request message for the ``GetLfpStore`` method.

    Attributes:
        name (str):
            Required. The name of the store to retrieve. Format:
            ``accounts/{account}/lfpStores/{target_merchant}~{store_code}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class InsertLfpStoreRequest(proto.Message):
    r"""Request message for the InsertLfpStore method.

    Attributes:
        parent (str):
            Required. The LFP provider account Format:
            ``accounts/{account}``
        lfp_store (google.shopping.merchant_lfp_v1.types.LfpStore):
            Required. The store to insert.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    lfp_store: "LfpStore" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="LfpStore",
    )


class DeleteLfpStoreRequest(proto.Message):
    r"""Request message for the DeleteLfpStore method.

    Attributes:
        name (str):
            Required. The name of the store to delete for the target
            merchant account. Format:
            ``accounts/{account}/lfpStores/{target_merchant}~{store_code}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListLfpStoresRequest(proto.Message):
    r"""Request message for the ListLfpStores method.

    Attributes:
        parent (str):
            Required. The LFP partner. Format: ``accounts/{account}``
        target_account (int):
            Required. The Merchant Center id of the
            merchant to list stores for.
        page_size (int):
            Optional. The maximum number of ``LfpStore`` resources for
            the given account to return. The service returns fewer than
            this value if the number of stores for the given account is
            less than the ``pageSize``. The default value is 250. The
            maximum value is 1000; If a value higher than the maximum is
            specified, then the ``pageSize`` will default to the
            maximum.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListLfpStoresRequest`` call. Provide the page token to
            retrieve the subsequent page. When paginating, all other
            parameters provided to ``ListLfpStoresRequest`` must match
            the call that provided the page token. The token returned as
            [nextPageToken][google.shopping.merchant.lfp.v1.ListLfpStoresResponse.next_page_token]
            in the response to the previous request.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    target_account: int = proto.Field(
        proto.INT64,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListLfpStoresResponse(proto.Message):
    r"""Response message for the ListLfpStores method.

    Attributes:
        lfp_stores (MutableSequence[google.shopping.merchant_lfp_v1.types.LfpStore]):
            The stores from the specified merchant.
        next_page_token (str):
            A token, which can be sent as ``pageToken`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    lfp_stores: MutableSequence["LfpStore"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="LfpStore",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
