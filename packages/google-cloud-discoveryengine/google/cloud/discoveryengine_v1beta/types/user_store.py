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
    package="google.cloud.discoveryengine.v1beta",
    manifest={
        "UserStore",
    },
)


class UserStore(proto.Message):
    r"""Configures metadata that is used for End User entities.

    Attributes:
        name (str):
            Immutable. The full resource name of the User Store, in the
            format of
            ``projects/{project}/locations/{location}/userStores/{user_store}``.

            This field must be a UTF-8 encoded string with a length
            limit of 1024 characters.
        display_name (str):
            The display name of the User Store.
        default_license_config (str):
            Optional. The default subscription
            [LicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfig]
            for the UserStore, if
            [UserStore.enable_license_auto_register][google.cloud.discoveryengine.v1beta.UserStore.enable_license_auto_register]
            is true, new users will automatically register under the
            default subscription.

            If default
            [LicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfig]
            doesn't have remaining license seats left, new users will
            not be assigned with license and will be blocked for Vertex
            AI Search features. This is used if
            ``license_assignment_tier_rules`` is not configured.
        enable_license_auto_register (bool):
            Optional. Whether to enable license auto
            register for users in this User Store. If true,
            new users will automatically register under the
            default license config as long as the default
            license config has seats left.
        enable_expired_license_auto_update (bool):
            Optional. Whether to enable license auto
            update for users in this User Store. If true,
            users with expired licenses will automatically
            be updated to use the default license config as
            long as the default license config has seats
            left.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    default_license_config: str = proto.Field(
        proto.STRING,
        number=5,
    )
    enable_license_auto_register: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    enable_expired_license_auto_update: bool = proto.Field(
        proto.BOOL,
        number=7,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
