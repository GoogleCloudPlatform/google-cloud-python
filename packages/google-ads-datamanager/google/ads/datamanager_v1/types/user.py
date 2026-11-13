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

from google.ads.datamanager_v1.types import audience
from google.ads.datamanager_v1.types import user_data as gad_user_data

__protobuf__ = proto.module(
    package="google.ads.datamanager.v1",
    manifest={
        "User",
    },
)


class User(proto.Message):
    r"""Represents a single user, containing identifiers like PII and
    mobile device IDs that all refer to the same user.

    Attributes:
        user_data (google.ads.datamanager_v1.types.UserData):
            Required. Multiple pieces of user-provided
            data, used as the means of identifying the user.
        mobile_data (google.ads.datamanager_v1.types.MobileData):
            Required. Multiple mobile device ID strings
            to represent a single user.
    """

    user_data: gad_user_data.UserData = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gad_user_data.UserData,
    )
    mobile_data: audience.MobileData = proto.Field(
        proto.MESSAGE,
        number=2,
        message=audience.MobileData,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
