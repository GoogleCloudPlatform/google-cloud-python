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

from google.cloud.productregistry_v1.types import lifecycle_state as gcp_lifecycle_state

__protobuf__ = proto.module(
    package="google.cloud.productregistry.v1",
    manifest={
        "LogicalProductVariant",
    },
)


class LogicalProductVariant(proto.Message):
    r"""Represents a distinct offering derived from a primary product
    that retains core functionalities but offers specialized
    features for a specific market segment.

    Attributes:
        name (str):
            Identifier. The resource name of the LogicalProductVariant.
            Format: logicalProducts/{logical_product}/variants/{variant}
        title (str):
            Display name of the LogicalProductVariant.
        lifecycle_state (google.cloud.productregistry_v1.types.LifecycleState):
            Output only. Current Lifecycle state of the
            logical product variant.
        replaced (bool):
            Output only. Indicates whether the logical product variant
            has been replaced. If ``false``, the variant is active. If
            ``true``, the variant has been replaced by another type, and
            the ``replacement`` field contains the resource name of that
            replacement.
        replacement (str):
            Output only. The resource name of the Logical Entity that
            the logical product variant is replaced by. This field is
            only populated when this logical product variant is replaced
            by some other type. Eg: logicalProducts/{logical_product},
            productSuites/{product_suite}, etc.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    title: str = proto.Field(
        proto.STRING,
        number=2,
    )
    lifecycle_state: gcp_lifecycle_state.LifecycleState = proto.Field(
        proto.ENUM,
        number=3,
        enum=gcp_lifecycle_state.LifecycleState,
    )
    replaced: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    replacement: str = proto.Field(
        proto.STRING,
        number=5,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
