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
    package="google.cloud.sql.v1beta4",
    manifest={
        "SqlTiersListRequest",
        "TiersListResponse",
        "Tier",
    },
)


class SqlTiersListRequest(proto.Message):
    r"""

    Attributes:
        project (str):
            Project ID of the project for which to list
            tiers.
    """

    project: str = proto.Field(
        proto.STRING,
        number=1,
    )


class TiersListResponse(proto.Message):
    r"""Tiers list response.

    Attributes:
        kind (str):
            This is always ``sql#tiersList``.
        items (MutableSequence[google.cloud.sqladmin_v1beta4.types.Tier]):
            List of tiers.
    """

    kind: str = proto.Field(
        proto.STRING,
        number=1,
    )
    items: MutableSequence["Tier"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="Tier",
    )


class Tier(proto.Message):
    r"""A Google Cloud SQL service tier resource.

    Attributes:
        tier (str):
            An identifier for the machine type, for example,
            ``db-custom-1-3840``. For related information, see
            `Pricing </sql/pricing>`__.
        RAM (int):
            The maximum RAM usage of this tier in bytes.
        kind (str):
            This is always ``sql#tier``.
        Disk_Quota (int):
            The maximum disk size of this tier in bytes.
        region (MutableSequence[str]):
            The applicable regions for this tier.
    """

    tier: str = proto.Field(
        proto.STRING,
        number=1,
    )
    RAM: int = proto.Field(
        proto.INT64,
        number=2,
    )
    kind: str = proto.Field(
        proto.STRING,
        number=3,
    )
    Disk_Quota: int = proto.Field(
        proto.INT64,
        number=4,
    )
    region: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
