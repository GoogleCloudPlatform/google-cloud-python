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

import google.type.date_pb2 as date_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.orchestration.airflow.service.v1beta1",
    manifest={
        "ListImageVersionsRequest",
        "ListImageVersionsResponse",
        "ImageVersion",
    },
)


class ListImageVersionsRequest(proto.Message):
    r"""List ImageVersions in a project and location.

    Attributes:
        parent (str):
            List ImageVersions in the given project and
            location, in the form:
            "projects/{projectId}/locations/{locationId}".
        page_size (int):
            The maximum number of image_versions to return.
        page_token (str):
            The next_page_token value returned from a previous List
            request, if any.
        include_past_releases (bool):
            Whether or not image versions from old
            releases should be included.
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
    include_past_releases: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class ListImageVersionsResponse(proto.Message):
    r"""The ImageVersions in a project and location.

    Attributes:
        image_versions (MutableSequence[google.cloud.orchestration.airflow.service_v1beta1.types.ImageVersion]):
            The list of supported ImageVersions in a
            location.
        next_page_token (str):
            The page token used to query for the next
            page if one exists.
    """

    @property
    def raw_page(self):
        return self

    image_versions: MutableSequence["ImageVersion"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ImageVersion",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ImageVersion(proto.Message):
    r"""Image Version information

    Attributes:
        image_version_id (str):
            The string identifier of the ImageVersion, in
            the form: "composer-x.y.z-airflow-a.b.c".
        is_default (bool):
            Whether this is the default ImageVersion used
            by Composer during environment creation if no
            input ImageVersion is specified.
        supported_python_versions (MutableSequence[str]):
            supported python versions
        release_date (google.type.date_pb2.Date):
            The date of the version release.
        creation_disabled (bool):
            Whether it is impossible to create an
            environment with the image version.
        upgrade_disabled (bool):
            Whether it is impossible to upgrade an
            environment running with the image version.
    """

    image_version_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    is_default: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    supported_python_versions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    release_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=4,
        message=date_pb2.Date,
    )
    creation_disabled: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    upgrade_disabled: bool = proto.Field(
        proto.BOOL,
        number=6,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
