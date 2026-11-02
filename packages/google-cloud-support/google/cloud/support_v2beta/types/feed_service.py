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

from google.cloud.support_v2beta.types import feed_item

__protobuf__ = proto.module(
    package="google.cloud.support.v2beta",
    manifest={
        "ShowFeedRequest",
        "ShowFeedResponse",
    },
)


class ShowFeedRequest(proto.Message):
    r"""The request message for the ShowFeed endpoint.

    Attributes:
        parent (str):
            Required. The resource name of the case for
            which feed items should be listed.
        order_by (str):
            Optional. Field to order feed items by, followed by ``asc``
            or ``desc`` postfix. The only valid field is
            ``creation_time``. This list is case-insensitive, default
            sorting order is ascending, and the redundant space
            characters are insignificant.

            Example: ``creation_time desc``
        page_size (int):
            Optional. The maximum number of feed items
            fetched with each request.
        page_token (str):
            Optional. A token identifying the page of
            results to return. If unspecified, it retrieves
            the first page.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    order_by: str = proto.Field(
        proto.STRING,
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


class ShowFeedResponse(proto.Message):
    r"""The response message for the ShowFeed endpoint.

    Attributes:
        feed_items (MutableSequence[google.cloud.support_v2beta.types.FeedItem]):
            The list of feed items associated with the
            given Case.
        next_page_token (str):
            A token to retrieve the next page of results. This should be
            set in the ``page_token`` field of subsequent
            ``ShowFeedRequests``. If unspecified, there are no more
            results to retrieve.
    """

    @property
    def raw_page(self):
        return self

    feed_items: MutableSequence[feed_item.FeedItem] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=feed_item.FeedItem,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
