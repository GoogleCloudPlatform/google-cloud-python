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

import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.artifactregistry_v1beta2.types import tag

__protobuf__ = proto.module(
    package="google.devtools.artifactregistry.v1beta2",
    manifest={
        "VersionView",
        "Version",
        "ListVersionsRequest",
        "ListVersionsResponse",
        "GetVersionRequest",
        "DeleteVersionRequest",
    },
)


class VersionView(proto.Enum):
    r"""The view, which determines what version information is
    returned in a response.

    Values:
        VERSION_VIEW_UNSPECIFIED (0):
            The default / unset value.
            The API will default to the BASIC view.
        BASIC (1):
            Includes basic information about the version,
            but not any related tags.
        FULL (2):
            Include everything.
    """

    VERSION_VIEW_UNSPECIFIED = 0
    BASIC = 1
    FULL = 2


class Version(proto.Message):
    r"""The body of a version resource. A version resource represents
    a collection of components, such as files and other data. This
    may correspond to a version in many package management schemes.

    Attributes:
        name (str):
            The name of the version, for example:

            "projects/p1/locations/us-central1/repositories/repo1/packages/pkg1/versions/art1".
            If the package or version ID parts contain
            slashes, the slashes are escaped.
        description (str):
            Optional. Description of the version, as
            specified in its metadata.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the version was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the version was last updated.
        related_tags (MutableSequence[google.cloud.artifactregistry_v1beta2.types.Tag]):
            Output only. A list of related tags. Will
            contain up to 100 tags that reference this
            version.
        metadata (google.protobuf.struct_pb2.Struct):
            Output only. Repository-specific Metadata stored against
            this version. The fields returned are defined by the
            underlying repository-specific resource. Currently, the only
            resource in use is
            [DockerImage][google.devtools.artifactregistry.v1.DockerImage]
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    related_tags: MutableSequence[tag.Tag] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message=tag.Tag,
    )
    metadata: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=8,
        message=struct_pb2.Struct,
    )


class ListVersionsRequest(proto.Message):
    r"""The request to list versions.

    Attributes:
        parent (str):
            The name of the parent resource whose
            versions will be listed.
        page_size (int):
            The maximum number of versions to return.
            Maximum page size is 1,000.
        page_token (str):
            The next_page_token value returned from a previous list
            request, if any.
        view (google.cloud.artifactregistry_v1beta2.types.VersionView):
            The view that should be returned in the
            response.
        order_by (str):
            Optional. The field to order the results by.
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
    view: "VersionView" = proto.Field(
        proto.ENUM,
        number=4,
        enum="VersionView",
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListVersionsResponse(proto.Message):
    r"""The response from listing versions.

    Attributes:
        versions (MutableSequence[google.cloud.artifactregistry_v1beta2.types.Version]):
            The versions returned.
        next_page_token (str):
            The token to retrieve the next page of
            versions, or empty if there are no more versions
            to return.
    """

    @property
    def raw_page(self):
        return self

    versions: MutableSequence["Version"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Version",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetVersionRequest(proto.Message):
    r"""The request to retrieve a version.

    Attributes:
        name (str):
            The name of the version to retrieve.
        view (google.cloud.artifactregistry_v1beta2.types.VersionView):
            The view that should be returned in the
            response.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: "VersionView" = proto.Field(
        proto.ENUM,
        number=2,
        enum="VersionView",
    )


class DeleteVersionRequest(proto.Message):
    r"""The request to delete a version.

    Attributes:
        name (str):
            The name of the version to delete.
        force (bool):
            By default, a version that is tagged may not
            be deleted. If force=true, the version and any
            tags pointing to the version are deleted.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
