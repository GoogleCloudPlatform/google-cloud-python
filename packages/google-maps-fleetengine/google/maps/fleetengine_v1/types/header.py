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
    package="maps.fleetengine.v1",
    manifest={
        "RequestHeader",
    },
)


class RequestHeader(proto.Message):
    r"""A RequestHeader contains fields common to all Fleet Engine
    RPC requests.

    Attributes:
        language_code (str):
            The BCP-47 language code, such as en-US or sr-Latn. For more
            information, see
            http://www.unicode.org/reports/tr35/#Unicode_locale_identifier.
            If none is specified, the response may be in any language,
            with a preference for English if such a name exists. Field
            value example: ``en-US``.
        region_code (str):
            Required. CLDR region code of the region where the request
            originates. Field value example: ``US``.
        sdk_version (str):
            Version of the calling SDK, if applicable. The version
            format is "major.minor.patch", example: ``1.1.2``.
        os_version (str):
            Version of the operating system on which the calling SDK is
            running. Field value examples: ``4.4.1``, ``12.1``.
        device_model (str):
            Model of the device on which the calling SDK is running.
            Field value examples: ``iPhone12,1``, ``SM-G920F``.
        sdk_type (google.maps.fleetengine_v1.types.RequestHeader.SdkType):
            The type of SDK sending the request.
        maps_sdk_version (str):
            Version of the MapSDK which the calling SDK depends on, if
            applicable. The version format is "major.minor.patch",
            example: ``5.2.1``.
        nav_sdk_version (str):
            Version of the NavSDK which the calling SDK depends on, if
            applicable. The version format is "major.minor.patch",
            example: ``2.1.0``.
        platform (google.maps.fleetengine_v1.types.RequestHeader.Platform):
            Platform of the calling SDK.
        manufacturer (str):
            Manufacturer of the Android device from the calling SDK,
            only applicable for the Android SDKs. Field value example:
            ``Samsung``.
        android_api_level (int):
            Android API level of the calling SDK, only applicable for
            the Android SDKs. Field value example: ``23``.
        trace_id (str):
            Optional ID that can be provided for logging
            purposes in order to identify the request.
    """

    class SdkType(proto.Enum):
        r"""Possible types of SDK.

        Values:
            SDK_TYPE_UNSPECIFIED (0):
                The default value. This value is used if the ``sdk_type`` is
                omitted.
            CONSUMER (1):
                The calling SDK is Consumer.
            DRIVER (2):
                The calling SDK is Driver.
            JAVASCRIPT (3):
                The calling SDK is JavaScript.
        """

        SDK_TYPE_UNSPECIFIED = 0
        CONSUMER = 1
        DRIVER = 2
        JAVASCRIPT = 3

    class Platform(proto.Enum):
        r"""The platform of the calling SDK.

        Values:
            PLATFORM_UNSPECIFIED (0):
                The default value. This value is used if the
                platform is omitted.
            ANDROID (1):
                The request is coming from Android.
            IOS (2):
                The request is coming from iOS.
            WEB (3):
                The request is coming from the web.
        """

        PLATFORM_UNSPECIFIED = 0
        ANDROID = 1
        IOS = 2
        WEB = 3

    language_code: str = proto.Field(
        proto.STRING,
        number=1,
    )
    region_code: str = proto.Field(
        proto.STRING,
        number=2,
    )
    sdk_version: str = proto.Field(
        proto.STRING,
        number=3,
    )
    os_version: str = proto.Field(
        proto.STRING,
        number=4,
    )
    device_model: str = proto.Field(
        proto.STRING,
        number=5,
    )
    sdk_type: SdkType = proto.Field(
        proto.ENUM,
        number=6,
        enum=SdkType,
    )
    maps_sdk_version: str = proto.Field(
        proto.STRING,
        number=7,
    )
    nav_sdk_version: str = proto.Field(
        proto.STRING,
        number=8,
    )
    platform: Platform = proto.Field(
        proto.ENUM,
        number=9,
        enum=Platform,
    )
    manufacturer: str = proto.Field(
        proto.STRING,
        number=10,
    )
    android_api_level: int = proto.Field(
        proto.INT32,
        number=11,
    )
    trace_id: str = proto.Field(
        proto.STRING,
        number=12,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
