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

from google.ads.admanager_v1.types import linked_device_enums

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "LinkedDevice",
    },
)


class LinkedDevice(proto.Message):
    r"""A test mobile device that is linked to the network. Can be
    used to preview a creative within a mobile application.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the ``LinkedDevice``.
            Format:
            ``networks/{network_code}/linkedDevices/{linked_device_id}``
        display_name (str):
            Required. The display name of the
            LinkedDevice.

            This field is a member of `oneof`_ ``_display_name``.
        owner (str):
            Output only. The user who owns this device linking. Format:
            ``networks/{network_code}/users/{user}``

            This field is a member of `oneof`_ ``_owner``.
        visibility (google.ads.admanager_v1.types.LinkedDeviceVisibilityEnum.LinkedDeviceVisibility):
            Optional. The visibility of the device.

            This field is a member of `oneof`_ ``_visibility``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    owner: str = proto.Field(
        proto.STRING,
        number=7,
        optional=True,
    )
    visibility: linked_device_enums.LinkedDeviceVisibilityEnum.LinkedDeviceVisibility = proto.Field(
        proto.ENUM,
        number=9,
        optional=True,
        enum=linked_device_enums.LinkedDeviceVisibilityEnum.LinkedDeviceVisibility,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
