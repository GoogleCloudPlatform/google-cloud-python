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
    package="google.devtools.artifactregistry.v1beta2",
    manifest={
        "Hash",
        "File",
        "ListFilesRequest",
        "ListFilesResponse",
        "GetFileRequest",
    },
)


class Hash(proto.Message):
    r"""A hash of file content.

    Attributes:
        type_ (google.cloud.artifactregistry_v1beta2.types.Hash.HashType):
            The algorithm used to compute the hash value.
        value (bytes):
            The hash value.
    """

    class HashType(proto.Enum):
        r"""The algorithm used to compute the hash.

        Values:
            HASH_TYPE_UNSPECIFIED (0):
                Unspecified.
            SHA256 (1):
                SHA256 hash.
            MD5 (2):
                MD5 hash.
        """

        HASH_TYPE_UNSPECIFIED = 0
        SHA256 = 1
        MD5 = 2

    type_: HashType = proto.Field(
        proto.ENUM,
        number=1,
        enum=HashType,
    )
    value: bytes = proto.Field(
        proto.BYTES,
        number=2,
    )


class File(proto.Message):
    r"""Files store content that is potentially associated with
    Packages or Versions.

    Attributes:
        name (str):
            The name of the file, for example:

            "projects/p1/locations/us-central1/repositories/repo1/files/a%2Fb%2Fc.txt".
            If the file ID part contains slashes, they are
            escaped.
        size_bytes (int):
            The size of the File in bytes.
        hashes (MutableSequence[google.cloud.artifactregistry_v1beta2.types.Hash]):
            The hashes of the file content.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the File was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the File was last updated.
        owner (str):
            The name of the Package or Version that owns
            this file, if any.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    size_bytes: int = proto.Field(
        proto.INT64,
        number=3,
    )
    hashes: MutableSequence["Hash"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="Hash",
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
    owner: str = proto.Field(
        proto.STRING,
        number=7,
    )


class ListFilesRequest(proto.Message):
    r"""The request to list files.

    Attributes:
        parent (str):
            The name of the repository whose files will
            be listed. For example:
            "projects/p1/locations/us-central1/repositories/repo1
        filter (str):
            An expression for filtering the results of the request.
            Filter rules are case insensitive. The fields eligible for
            filtering are:

            - ``name``
            - ``owner``

            An example of using a filter:

            - ``name="projects/p1/locations/us-central1/repositories/repo1/files/a/b/*"``
              --> Files with an ID starting with "a/b/".
            - ``owner="projects/p1/locations/us-central1/repositories/repo1/packages/pkg1/versions/1.0"``
              --> Files owned by the version ``1.0`` in package
              ``pkg1``.
        page_size (int):
            The maximum number of files to return.
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


class ListFilesResponse(proto.Message):
    r"""The response from listing files.

    Attributes:
        files (MutableSequence[google.cloud.artifactregistry_v1beta2.types.File]):
            The files returned.
        next_page_token (str):
            The token to retrieve the next page of files,
            or empty if there are no more files to return.
    """

    @property
    def raw_page(self):
        return self

    files: MutableSequence["File"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="File",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetFileRequest(proto.Message):
    r"""The request to retrieve a file.

    Attributes:
        name (str):
            The name of the file to retrieve.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
