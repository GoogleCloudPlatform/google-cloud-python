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
    package="google.cloud.discoveryengine.v1beta",
    manifest={
        "ObservabilityConfig",
    },
)


class ObservabilityConfig(proto.Message):
    r"""Observability config for a resource.

    Attributes:
        observability_enabled (bool):
            Optional. Enables observability. If ``false``, all other
            flags are ignored.
        sensitive_logging_enabled (bool):
            Optional. Enables sensitive logging. Sensitive logging
            includes customer core content (e.g. prompts, responses). If
            ``false``, will sanitize all sensitive fields.
    """

    observability_enabled: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    sensitive_logging_enabled: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
