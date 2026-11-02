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
    package="google.devicesandservices.health.v4",
    manifest={
        "MedicalDeviceInfo",
    },
)


class MedicalDeviceInfo(proto.Message):
    r"""Software as Medical Device (SaMD) metadata.
    Used to construct the Unique Device Identifier (UDI).

    Attributes:
        algorithm_version (str):
            Output only. The algorithm version used by
            the feature.
        service_version (str):
            Output only. The service version used by the
            feature.
        firmware_version (str):
            Output only. The firmware version running on
            the compatible device used to collect the data.
        feature_version (str):
            Output only. The version of the feature/app
            running on the device.
        device_model (str):
            Output only. The model name or device type of
            the compatible device used to collect the data.
    """

    algorithm_version: str = proto.Field(
        proto.STRING,
        number=1,
    )
    service_version: str = proto.Field(
        proto.STRING,
        number=2,
    )
    firmware_version: str = proto.Field(
        proto.STRING,
        number=3,
    )
    feature_version: str = proto.Field(
        proto.STRING,
        number=4,
    )
    device_model: str = proto.Field(
        proto.STRING,
        number=5,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
