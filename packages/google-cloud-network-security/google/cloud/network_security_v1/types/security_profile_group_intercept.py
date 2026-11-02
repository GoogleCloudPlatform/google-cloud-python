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
    package="google.cloud.networksecurity.v1",
    manifest={
        "CustomInterceptProfile",
    },
)


class CustomInterceptProfile(proto.Message):
    r"""CustomInterceptProfile defines in-band integration behavior
    (intercept). It is used by firewall rules with an
    APPLY_SECURITY_PROFILE_GROUP action.

    Attributes:
        intercept_endpoint_group (str):
            Required. The target InterceptEndpointGroup.
            When a firewall rule with this security profile
            attached matches a packet, the packet will be
            intercepted to the location-local target in this
            group.
    """

    intercept_endpoint_group: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
