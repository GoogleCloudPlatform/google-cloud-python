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
    package="google.cloud.channel.v1",
    manifest={
        "MediaType",
        "Product",
        "Sku",
        "MarketingInfo",
        "Media",
    },
)


class MediaType(proto.Enum):
    r"""Type of media used.

    Values:
        MEDIA_TYPE_UNSPECIFIED (0):
            Not used.
        MEDIA_TYPE_IMAGE (1):
            Type of image.
    """

    MEDIA_TYPE_UNSPECIFIED = 0
    MEDIA_TYPE_IMAGE = 1


class Product(proto.Message):
    r"""A Product is the entity a customer uses when placing an
    order. For example, Google Workspace, Google Voice, etc.

    Attributes:
        name (str):
            Resource Name of the Product. Format: products/{product_id}
        marketing_info (google.cloud.channel_v1.types.MarketingInfo):
            Marketing information for the product.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    marketing_info: "MarketingInfo" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="MarketingInfo",
    )


class Sku(proto.Message):
    r"""Represents a product's purchasable Stock Keeping Unit (SKU).
    SKUs represent the different variations of the product. For
    example, Google Workspace Business Standard and Google Workspace
    Business Plus are Google Workspace product SKUs.

    Attributes:
        name (str):
            Resource Name of the SKU. Format:
            products/{product_id}/skus/{sku_id}
        marketing_info (google.cloud.channel_v1.types.MarketingInfo):
            Marketing information for the SKU.
        product (google.cloud.channel_v1.types.Product):
            Product the SKU is associated with.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    marketing_info: "MarketingInfo" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="MarketingInfo",
    )
    product: "Product" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Product",
    )


class MarketingInfo(proto.Message):
    r"""Represents the marketing information for a Product, SKU or
    Offer.

    Attributes:
        display_name (str):
            Human readable name.
        description (str):
            Human readable description. Description can
            contain HTML.
        default_logo (google.cloud.channel_v1.types.Media):
            Default logo.
    """

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    default_logo: "Media" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Media",
    )


class Media(proto.Message):
    r"""Represents media information.

    Attributes:
        title (str):
            Title of the media.
        content (str):
            URL of the media.
        type_ (google.cloud.channel_v1.types.MediaType):
            Type of the media.
    """

    title: str = proto.Field(
        proto.STRING,
        number=1,
    )
    content: str = proto.Field(
        proto.STRING,
        number=2,
    )
    type_: "MediaType" = proto.Field(
        proto.ENUM,
        number=3,
        enum="MediaType",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
