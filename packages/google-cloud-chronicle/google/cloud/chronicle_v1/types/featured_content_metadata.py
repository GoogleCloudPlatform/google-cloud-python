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

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.chronicle.v1",
    manifest={
        "FeaturedContentMetadata",
    },
)


class FeaturedContentMetadata(proto.Message):
    r"""FeaturedContentMetadata holds metadata about the Featured
    Content.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        id (str):
            Required. Unique identifier of the featured
            content.
        display_name (str):
            Output only. The display name of the featured
            content.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp indicating when the
            item was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp indicating when the
            item was updated.
        author (str):
            Output only. Content item author full name.
        certified (bool):
            Output only. Determine if this content item
            is officially certified by Google or created by
            the community.
        description (str):
            Output only. The description of the content
            item.
        categories (MutableSequence[str]):
            Output only. Categories the content is
            associated with.
        version (str):
            Output only. Featured content version
            (Major.Minor.Patch).
        verified (bool):
            Output only. Whether the content is verified
            by Google (applicable for 3rd party content).

            This field is a member of `oneof`_ ``_verified``.
        source_type (google.cloud.chronicle_v1.types.FeaturedContentMetadata.ContentSourceType):
            Output only. The source type of the content.
    """

    class ContentSourceType(proto.Enum):
        r"""ContentSourceType specifying the content source of origin

        Values:
            CONTENT_SOURCE_TYPE_UNSPECIFIED (0):
                Unspecified content source type
            GOOGLE (1):
                Certified Google content source type
            COMMUNITY (2):
                Community content source type
            PARTNER (3):
                Partner content source type
        """

        CONTENT_SOURCE_TYPE_UNSPECIFIED = 0
        GOOGLE = 1
        COMMUNITY = 2
        PARTNER = 3

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    author: str = proto.Field(
        proto.STRING,
        number=5,
    )
    certified: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    description: str = proto.Field(
        proto.STRING,
        number=7,
    )
    categories: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    version: str = proto.Field(
        proto.STRING,
        number=9,
    )
    verified: bool = proto.Field(
        proto.BOOL,
        number=10,
        optional=True,
    )
    source_type: ContentSourceType = proto.Field(
        proto.ENUM,
        number=11,
        enum=ContentSourceType,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
