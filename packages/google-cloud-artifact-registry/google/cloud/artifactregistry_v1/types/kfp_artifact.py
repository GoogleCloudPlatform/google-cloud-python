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
    package="google.devtools.artifactregistry.v1",
    manifest={
        "KfpArtifact",
    },
)


class KfpArtifact(proto.Message):
    r"""A detailed representation of a KFP artifact.

    Attributes:
        name (str):
            Output only. Resource name of the KFP
            artifact. Since users don't directly interact
            with this resource, the name will be derived
            from the associated version. For example, when
            version = ".../versions/sha256:abcdef...", the
            name will be
            ".../kfpArtifacts/sha256:abcdef...".
        version (str):
            The version associated with the KFP artifact.
            Must follow the Semantic Versioning standard.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    version: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
