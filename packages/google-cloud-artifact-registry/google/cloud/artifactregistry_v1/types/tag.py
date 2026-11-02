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
    package="google.devtools.artifactregistry.v1",
    manifest={
        "Tag",
        "ListTagsRequest",
        "ListTagsResponse",
        "GetTagRequest",
        "CreateTagRequest",
        "UpdateTagRequest",
        "DeleteTagRequest",
    },
)


class Tag(proto.Message):
    r"""Tags point to a version and represent an alternative name
    that can be used to access the version.

    Attributes:
        name (str):
            The name of the tag, for example:
            "projects/p1/locations/us-central1/repositories/repo1/packages/pkg1/tags/tag1".
            If the package part contains slashes, the slashes are
            escaped. The tag part can only have characters in
            [a-zA-Z0-9-.\_~:@], anything else must be URL encoded.
        version (str):
            The name of the version the tag refers to, for example:
            ``projects/p1/locations/us-central1/repositories/repo1/packages/pkg1/versions/sha256:5243811``
            If the package or version ID parts contain slashes, the
            slashes are escaped.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    version: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListTagsRequest(proto.Message):
    r"""The request to list tags.

    Attributes:
        parent (str):
            The name of the parent package whose tags will be listed.
            For example:
            ``projects/p1/locations/us-central1/repositories/repo1/packages/pkg1``.
        filter (str):
            An expression for filtering the results of the request.
            Filter rules are case insensitive. The fields eligible for
            filtering are:

            - ``name``
            - ``version``

            Examples of using a filter:

            To filter the results of your request to tags with the name
            ``my-tag`` in package ``my-package`` in repository
            ``my-repo`` in project "``y-project`` in the us-central
            region, append the following filter expression to your
            request:

            - ``name="projects/my-project/locations/us-central1/repositories/my-repo/packages/my-package/tags/my-tag"``

            You can also use wildcards to match any number of characters
            before or after the value:

            - ``name="projects/my-project/locations/us-central1/repositories/my-repo/packages/my-package/tags/my*"``
            - ``name="projects/my-project/locations/us-central1/repositories/my-repo/packages/my-package/tags/*tag"``
            - ``name="projects/my-project/locations/us-central1/repositories/my-repo/packages/my-package/tags/*tag*"``

            To filter the results of your request to tags applied to the
            version ``1.0`` in package ``my-package``, append the
            following filter expression to your request:

            - ``version="projects/my-project/locations/us-central1/repositories/my-repo/packages/my-package/versions/1.0"``
        page_size (int):
            The maximum number of tags to return. Maximum
            page size is 1,000.
        page_token (str):
            The next_page_token value returned from a previous list
            request, if any.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListTagsResponse(proto.Message):
    r"""The response from listing tags.

    Attributes:
        tags (MutableSequence[google.cloud.artifactregistry_v1.types.Tag]):
            The tags returned.
        next_page_token (str):
            The token to retrieve the next page of tags,
            or empty if there are no more tags to return.
    """

    @property
    def raw_page(self):
        return self

    tags: MutableSequence["Tag"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Tag",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetTagRequest(proto.Message):
    r"""The request to retrieve a tag.

    Attributes:
        name (str):
            The name of the tag to retrieve.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateTagRequest(proto.Message):
    r"""The request to create a new tag.

    Attributes:
        parent (str):
            The name of the parent resource where the tag
            will be created.
        tag_id (str):
            The tag id to use for this repository.
        tag (google.cloud.artifactregistry_v1.types.Tag):
            The tag to be created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    tag_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    tag: "Tag" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Tag",
    )


class UpdateTagRequest(proto.Message):
    r"""The request to create or update a tag.

    Attributes:
        tag (google.cloud.artifactregistry_v1.types.Tag):
            The tag that replaces the resource on the
            server.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The update mask applies to the resource. For the
            ``FieldMask`` definition, see
            https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask
    """

    tag: "Tag" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Tag",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteTagRequest(proto.Message):
    r"""The request to delete a tag.

    Attributes:
        name (str):
            The name of the tag to delete.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
