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
        "Package",
        "ListPackagesRequest",
        "ListPackagesResponse",
        "GetPackageRequest",
        "DeletePackageRequest",
    },
)


class Package(proto.Message):
    r"""Packages are named collections of versions.

    Attributes:
        name (str):
            The name of the package, for example:

            "projects/p1/locations/us-central1/repositories/repo1/packages/pkg1".
        display_name (str):
            The display name of the package.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the package was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the package was last updated.
            This includes publishing a new version of the
            package.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
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


class ListPackagesRequest(proto.Message):
    r"""The request to list packages.

    Attributes:
        parent (str):
            The name of the parent resource whose
            packages will be listed.
        page_size (int):
            The maximum number of packages to return.
            Maximum page size is 10,000.
        page_token (str):
            The next_page_token value returned from a previous list
            request, if any.
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


class ListPackagesResponse(proto.Message):
    r"""The response from listing packages.

    Attributes:
        packages (MutableSequence[google.cloud.artifactregistry_v1beta2.types.Package]):
            The packages returned.
        next_page_token (str):
            The token to retrieve the next page of
            packages, or empty if there are no more packages
            to return.
    """

    @property
    def raw_page(self):
        return self

    packages: MutableSequence["Package"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Package",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetPackageRequest(proto.Message):
    r"""The request to retrieve a package.

    Attributes:
        name (str):
            The name of the package to retrieve.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeletePackageRequest(proto.Message):
    r"""The request to delete a package.

    Attributes:
        name (str):
            The name of the package to delete.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
