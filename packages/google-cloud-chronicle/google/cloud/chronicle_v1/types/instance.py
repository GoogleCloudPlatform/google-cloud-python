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
    package="google.cloud.chronicle.v1",
    manifest={
        "Instance",
        "GetInstanceRequest",
    },
)


class Instance(proto.Message):
    r"""A Instance represents an instantiation of the Instance
    product.

    Attributes:
        name (str):
            Identifier. The resource name of this instance. Format:
            ``projects/{project}/locations/{location}/instances/{instance}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetInstanceRequest(proto.Message):
    r"""Request to get a Instance.

    Attributes:
        name (str):
            Required. The name of the instance to retrieve. Format:
            ``projects/{project_id}/locations/{location}/instances/{instance}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
