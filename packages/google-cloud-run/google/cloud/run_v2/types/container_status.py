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
    package="google.cloud.run.v2",
    manifest={
        "ContainerStatus",
    },
)


class ContainerStatus(proto.Message):
    r"""ContainerStatus holds the information of container name and
    image digest value.

    Attributes:
        name (str):
            The name of the container, if specified.
        image_digest (str):
            ImageDigest holds the resolved digest for the
            image specified and resolved during the creation
            of Revision. This field holds the digest value
            regardless of whether a tag or digest was
            originally specified in the Container object.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    image_digest: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
