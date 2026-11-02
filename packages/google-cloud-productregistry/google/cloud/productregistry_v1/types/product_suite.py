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
        "ProductSuite",
    },
)


class ProductSuite(proto.Message):
    r"""Represents a unified grouping of products sharing a common
    brand and market positioning.

    Attributes:
        name (str):
            Identifier. The resource name of the ProductSuite. Format:
            productSuites/{product_suite}
        title (str):
            Title of the ProductSuite.
        logical_products (MutableSequence[str]):
            Output only. LogicalProducts under this suite. Format:
            logicalProducts/{logical_product}
        replaced (bool):
            Output only. Indicates whether the product suite has been
            replaced. If ``false``, the product suite is active. If
            ``true``, the product suite has been replaced by another
            type, and the ``replacement`` field contains the resource
            name of that replacement.
        replacement (str):
            Output only. The resource name of the Logical Entity that
            the product suite is replaced by. This field is only
            populated when this product suite is replaced by some other
            type. Eg: logicalProducts/{logical_product},
            logicalProducts/{logical_product}/variants/{variant}, etc.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    title: str = proto.Field(
        proto.STRING,
        number=2,
    )
    logical_products: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
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
