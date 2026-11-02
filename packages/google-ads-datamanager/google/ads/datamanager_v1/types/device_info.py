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
    package="google.ads.datamanager.v1",
    manifest={
        "DeviceInfo",
    },
)


class DeviceInfo(proto.Message):
    r"""Information about the device being used (if any) when the
    event happened.

    Attributes:
        user_agent (str):
            Optional. The user-agent string of the device
            for the given context.
        ip_address (str):
            Optional. The IP address of the device for the given
            context. Required when used in an
            [AdEvent][google.ads.datamanager.v1.AdEvent] for geo checks.
        category (str):
            Optional. The category of device. For
            example, “desktop”, “tablet”, “mobile”, “smart
            TV”.
        language_code (str):
            Optional. The language the device uses in ISO
            639-1 format.
        screen_height (int):
            Optional. The height of the screen in pixels.
        screen_width (int):
            Optional. The width of the screen in pixels.
        operating_system (str):
            Optional. The operating system or platform of
            the device.
        operating_system_version (str):
            Optional. The version of the operating system
            or platform.
        model (str):
            Optional. The model of the device.
        brand (str):
            Optional. The brand of the device.
        browser (str):
            Optional. The brand or type of the browser.
        browser_version (str):
            Optional. The version of the browser.
    """

    user_agent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ip_address: str = proto.Field(
        proto.STRING,
        number=2,
    )
    category: str = proto.Field(
        proto.STRING,
        number=3,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=4,
    )
    screen_height: int = proto.Field(
        proto.INT32,
        number=5,
    )
    screen_width: int = proto.Field(
        proto.INT32,
        number=6,
    )
    operating_system: str = proto.Field(
        proto.STRING,
        number=7,
    )
    operating_system_version: str = proto.Field(
        proto.STRING,
        number=8,
    )
    model: str = proto.Field(
        proto.STRING,
        number=9,
    )
    brand: str = proto.Field(
        proto.STRING,
        number=10,
    )
    browser: str = proto.Field(
        proto.STRING,
        number=11,
    )
    browser_version: str = proto.Field(
        proto.STRING,
        number=12,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
