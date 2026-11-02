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

from google.cloud.support_v2.types import comment as gcs_comment

__protobuf__ = proto.module(
    package="google.cloud.support.v2",
    manifest={
        "ListCommentsRequest",
        "ListCommentsResponse",
        "CreateCommentRequest",
        "GetCommentRequest",
    },
)


class ListCommentsRequest(proto.Message):
    r"""The request message for the ListComments endpoint.

    Attributes:
        parent (str):
            Required. The name of the case for which to
            list comments.
        page_size (int):
            The maximum number of comments to fetch.
            Defaults to 10.
        page_token (str):
            A token identifying the page of results to
            return. If unspecified, the first page is
            returned.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=4,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListCommentsResponse(proto.Message):
    r"""The response message for the ListComments endpoint.

    Attributes:
        comments (MutableSequence[google.cloud.support_v2.types.Comment]):
            List of the comments associated with the
            case.
        next_page_token (str):
            A token to retrieve the next page of results. Set this in
            the ``page_token`` field of subsequent
            ``cases.comments.list`` requests. If unspecified, there are
            no more results to retrieve.
    """

    @property
    def raw_page(self):
        return self

    comments: MutableSequence[gcs_comment.Comment] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcs_comment.Comment,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateCommentRequest(proto.Message):
    r"""The request message for the CreateComment endpoint.

    Attributes:
        parent (str):
            Required. The name of the case to which the
            comment should be added.
        comment (google.cloud.support_v2.types.Comment):
            Required. The comment to be added.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    comment: gcs_comment.Comment = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcs_comment.Comment,
    )


class GetCommentRequest(proto.Message):
    r"""The request message for the GetComment endpoint.

    Attributes:
        name (str):
            Required. The name of the comment to
            retrieve.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
