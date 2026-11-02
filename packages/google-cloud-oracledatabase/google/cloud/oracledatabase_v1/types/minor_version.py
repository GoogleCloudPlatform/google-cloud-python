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
        "MinorVersion",
        "ListMinorVersionsRequest",
        "ListMinorVersionsResponse",
    },
)


class MinorVersion(proto.Message):
    r"""MinorVersion represents a minor version of a GI.
    https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/GiMinorVersionSummary/

    Attributes:
        name (str):
            Identifier. The name of the MinorVersion resource with the
            format:
            projects/{project}/locations/{region}/giVersions/{gi_version}/minorVersions/{minor_version}
        grid_image_id (str):
            Optional. The ID of the Grid Image.
        version (str):
            Optional. The valid Oracle grid
            infrastructure software version.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    grid_image_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    version: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListMinorVersionsRequest(proto.Message):
    r"""The request for ``MinorVersion.List``.

    Attributes:
        parent (str):
            Required. The parent value for the MinorVersion resource
            with the format:
            projects/{project}/locations/{location}/giVersions/{gi_version}
        page_size (int):
            Optional. The maximum number of items to
            return. If unspecified, a maximum of 50 System
            Versions will be returned. The maximum value is
            1000; values above 1000 will be reset to 1000.
        page_token (str):
            Optional. A token identifying the requested
            page of results to return. All fields except the
            filter should remain the same as in the request
            that provided this page token.
        filter (str):
            Optional. An expression for filtering the results of the
            request. Only the ``shape_family`` and
            ``gcp_oracle_zone_id`` fields are supported in the following
            format:
            ``shape_family="{shape_family}" AND gcp_oracle_zone_id="{gcp_oracle_zone_id}"``.
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


class ListMinorVersionsResponse(proto.Message):
    r"""The response for ``MinorVersion.List``.

    Attributes:
        minor_versions (MutableSequence[google.cloud.oracledatabase_v1.types.MinorVersion]):
            The list of MinorVersions.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
    """

    @property
    def raw_page(self):
        return self

    minor_versions: MutableSequence["MinorVersion"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="MinorVersion",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
