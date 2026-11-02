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

from google.ads.admanager_v1.types import team_enums

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "Team",
    },
)


class Team(proto.Message):
    r"""A Team defines a grouping of users and what entities they
    have access to.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the ``Team``. Format:
            ``networks/{network_code}/teams/{team_id}``
        display_name (str):
            Required. The name of the Team. This value
            has a maximum length of 127 characters.

            This field is a member of `oneof`_ ``_display_name``.
        description (str):
            Optional. The description of the Team. This
            value has a maximum length of 255 characters.

            This field is a member of `oneof`_ ``_description``.
        status (google.ads.admanager_v1.types.TeamStatusEnum.TeamStatus):
            Output only. The status of the Team. This
            value determines the visibility of the team in
            the UI.

            This field is a member of `oneof`_ ``_status``.
        all_companies_access (bool):
            Optional. Whether or not users on this team
            have access to all companies. If this value is
            true, then an error will be thrown if an attempt
            is made to associate this team with a Company.

            This field is a member of `oneof`_ ``_all_companies_access``.
        all_inventory_access (bool):
            Optional. Whether or not users on this team
            have access to all inventory. If this value is
            true, then an error will be thrown if an attempt
            is made to associate this team with an AdUnit.

            This field is a member of `oneof`_ ``_all_inventory_access``.
        access_type (google.ads.admanager_v1.types.TeamAccessTypeEnum.TeamAccessType):
            Optional. The default access to orders for
            users on this team.

            This field is a member of `oneof`_ ``_access_type``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    status: team_enums.TeamStatusEnum.TeamStatus = proto.Field(
        proto.ENUM,
        number=5,
        optional=True,
        enum=team_enums.TeamStatusEnum.TeamStatus,
    )
    all_companies_access: bool = proto.Field(
        proto.BOOL,
        number=6,
        optional=True,
    )
    all_inventory_access: bool = proto.Field(
        proto.BOOL,
        number=7,
        optional=True,
    )
    access_type: team_enums.TeamAccessTypeEnum.TeamAccessType = proto.Field(
        proto.ENUM,
        number=8,
        optional=True,
        enum=team_enums.TeamAccessTypeEnum.TeamAccessType,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
