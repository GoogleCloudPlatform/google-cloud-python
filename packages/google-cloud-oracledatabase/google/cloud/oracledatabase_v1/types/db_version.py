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
    package="google.cloud.oracledatabase.v1",
    manifest={
        "DbVersion",
        "DbVersionProperties",
        "ListDbVersionsRequest",
        "ListDbVersionsResponse",
    },
)


class DbVersion(proto.Message):
    r"""A valid Oracle Database version.

    Attributes:
        name (str):
            Output only. The name of the DbVersion resource in the
            following format:
            projects/{project}/locations/{region}/dbVersions/{db_version}
        properties (google.cloud.oracledatabase_v1.types.DbVersionProperties):
            Output only. The properties of the DbVersion.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    properties: "DbVersionProperties" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DbVersionProperties",
    )


class DbVersionProperties(proto.Message):
    r"""The properties of a DbVersion.

    Attributes:
        version (str):
            Output only. A valid Oracle Database version.
        is_latest_for_major_version (bool):
            Output only. True if this version of the
            Oracle Database software is the latest version
            for a release.
        supports_pdb (bool):
            Output only. True if this version of the
            Oracle Database software supports pluggable
            databases.
        is_preview_db_version (bool):
            Output only. True if this version of the
            Oracle Database software is the preview version.
        is_upgrade_supported (bool):
            Output only. True if this version of the
            Oracle Database software is supported for
            Upgrade.
    """

    version: str = proto.Field(
        proto.STRING,
        number=1,
    )
    is_latest_for_major_version: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    supports_pdb: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    is_preview_db_version: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    is_upgrade_supported: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class ListDbVersionsRequest(proto.Message):
    r"""The request for ``DbVersions.List``.

    Attributes:
        parent (str):
            Required. The parent value for the DbVersion
            resource with the format:
            projects/{project}/locations/{location}
        page_size (int):
            Optional. The maximum number of items to
            return. If unspecified, a maximum of 50
            DbVersions will be returned. The maximum value
            is 1000; values above 1000 will be reset to
            1000.
        page_token (str):
            Optional. A token identifying the requested
            page of results to return. All fields except the
            filter should remain the same as in the request
            that provided this page token.
        filter (str):
            Optional. Filter expression that matches a subset of the
            DbVersions to show. The supported filter for dbSystem
            creation is
            ``db_system_shape = {db_system_shape} AND storage_management = {storage_management}``.
            If no filter is provided, all DbVersions will be returned.
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


class ListDbVersionsResponse(proto.Message):
    r"""The response for ``DbVersions.List``.

    Attributes:
        db_versions (MutableSequence[google.cloud.oracledatabase_v1.types.DbVersion]):
            The list of DbVersions.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
    """

    @property
    def raw_page(self):
        return self

    db_versions: MutableSequence["DbVersion"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DbVersion",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
