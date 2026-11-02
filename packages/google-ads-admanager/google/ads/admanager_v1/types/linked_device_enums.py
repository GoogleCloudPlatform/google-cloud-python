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
    package="google.ads.admanager.v1",
    manifest={
        "LinkedDeviceVisibilityEnum",
    },
)


class LinkedDeviceVisibilityEnum(proto.Message):
    r"""Wrapper message for
    [LinkedDeviceVisibility][google.ads.admanager.v1.LinkedDeviceVisibilityEnum.LinkedDeviceVisibility]

    """

    class LinkedDeviceVisibility(proto.Enum):
        r"""Represents the visibility of a LinkedDevice.

        Values:
            LINKED_DEVICE_VISIBILITY_UNSPECIFIED (0):
                Default value. This value is unused.
            PRIVATE (2):
                The linked device can only be used by the
                user who owns the device linking.
            PUBLIC (3):
                The linked device can be used by anyone on
                the network.
        """

        LINKED_DEVICE_VISIBILITY_UNSPECIFIED = 0
        PRIVATE = 2
        PUBLIC = 3


__all__ = tuple(sorted(__protobuf__.manifest))
