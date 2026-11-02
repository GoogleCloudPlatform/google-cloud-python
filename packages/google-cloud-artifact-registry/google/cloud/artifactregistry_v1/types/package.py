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
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.devtools.artifactregistry.v1",
    manifest={
        "Package",
        "ListPackagesRequest",
        "ListPackagesResponse",
        "GetPackageRequest",
        "DeletePackageRequest",
        "UpdatePackageRequest",
    },
)


class Package(proto.Message):
    r"""Packages are named collections of versions.

    Attributes:
        name (str):
            The name of the package, for example:
            ``projects/p1/locations/us-central1/repositories/repo1/packages/pkg1``.
            If the package ID part contains slashes, the slashes are
            escaped.
        display_name (str):
            The display name of the package.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the package was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the package was last updated.
            This includes publishing a new version of the
            package.
        annotations (MutableMapping[str, str]):
            Optional. Client specified annotations.
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
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )


class ListPackagesRequest(proto.Message):
    r"""The request to list packages.

    Attributes:
        parent (str):
            Required. The name of the parent resource
            whose packages will be listed.
        page_size (int):
            The maximum number of packages to return.
            Maximum page size is 1,000.
        page_token (str):
            The next_page_token value returned from a previous list
            request, if any.
        filter (str):
            Optional. An expression for filtering the results of the
            request. Filter rules are case insensitive. The fields
            eligible for filtering are:

            - ``name``
            - ``annotations``

            Examples of using a filter:

            To filter the results of your request to packages with the
            name ``my-package`` in project ``my-project`` in the
            ``us-central`` region, in repository ``my-repo``, append the
            following filter expression to your request:

            - ``name="projects/my-project/locations/us-central1/repositories/my-repo/packages/my-package"``

            You can also use wildcards to match any number of characters
            before or after the value:

            - ``name="projects/my-project/locations/us-central1/repositories/my-repo/packages/my-*"``
            - ``name="projects/my-project/locations/us-central1/repositories/my-repo/packages/*package"``
            - ``name="projects/my-project/locations/us-central1/repositories/my-repo/packages/*pack*"``

            To filter the results of your request to packages with the
            annotation key-value pair [``external_link``:
            ``external_link_value``], append the following filter
            expression to your request":

            - ``"annotations.external_link:external_link_value"``

            To filter the results just for a specific annotation key
            ``external_link``, append the following filter expression to
            your request:

            - ``"annotations.external_link"``

            If the annotation key or value contains special characters,
            you can escape them by surrounding the value with backticks.
            For example, to filter the results of your request to
            packages with the annotation key-value pair
            [``external.link``:``https://example.com/my-package``],
            append the following filter expression to your request:

            - :literal:`"annotations.`external.link\`:\`https://example.com/my-package\`"`

            You can also filter with annotations with a wildcard to
            match any number of characters before or after the value:

            - :literal:`"annotations.*_link:\`*example.com*\`"`
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
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListPackagesResponse(proto.Message):
    r"""The response from listing packages.

    Attributes:
        packages (MutableSequence[google.cloud.artifactregistry_v1.types.Package]):
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
            Required. The name of the package to
            retrieve.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeletePackageRequest(proto.Message):
    r"""The request to delete a package.

    Attributes:
        name (str):
            Required. The name of the package to delete.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdatePackageRequest(proto.Message):
    r"""The request to update a package.

    Attributes:
        package (google.cloud.artifactregistry_v1.types.Package):
            The package that replaces the resource on the
            server.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The update mask applies to the resource. For the
            ``FieldMask`` definition, see
            https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask
    """

    package: "Package" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Package",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
