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
        "CustomMirroringProfile",
    },
)


class CustomMirroringProfile(proto.Message):
    r"""CustomMirroringProfile defines out-of-band integration
    behavior (mirroring). It is used by mirroring rules with a
    MIRROR action.

    Attributes:
        mirroring_endpoint_group (str):
            Required. Immutable. The target
            MirroringEndpointGroup. When a mirroring rule
            with this security profile attached matches a
            packet, a replica will be mirrored to the
            location-local target in this group.
    """

    mirroring_endpoint_group: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
