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
    package="google.cloud.productregistry.v1",
    manifest={
        "LifecycleState",
    },
)


class LifecycleState(proto.Enum):
    r"""Enum representing the lifecycle state of the underlying
    entity.

    Values:
        LIFECYCLE_STATE_UNSPECIFIED (0):
            The default value. This value is used if the
            lifecycle state is not set.
        LIFECYCLE_STATE_PUBLIC_PREVIEW (1):
            The entity is in Public Preview. It is
            available to all customers, but may not be
            feature-complete or have full support
            guarantees.
        LIFECYCLE_STATE_PRIVATE_GA (2):
            The entity is in Private General
            Availability. It is fully supported and stable,
            but only available to a select group of
            customers.
        LIFECYCLE_STATE_GA (3):
            The entity is Generally Available. It is
            fully supported, stable, and available to all
            customers.
        LIFECYCLE_STATE_DEPRECATED (4):
            The entity is deprecated. It is no longer
            recommended for use and may be removed in a
            future version.
    """

    LIFECYCLE_STATE_UNSPECIFIED = 0
    LIFECYCLE_STATE_PUBLIC_PREVIEW = 1
    LIFECYCLE_STATE_PRIVATE_GA = 2
    LIFECYCLE_STATE_GA = 3
    LIFECYCLE_STATE_DEPRECATED = 4


__all__ = tuple(sorted(__protobuf__.manifest))
