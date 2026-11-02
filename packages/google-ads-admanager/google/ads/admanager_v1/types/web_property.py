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

from google.ads.admanager_v1.types import exchange_syndication_product_enum

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "WebProperty",
    },
)


class WebProperty(proto.Message):
    r"""Represents a web property.

    Attributes:
        name (str):
            Identifier. The resource name of the WebProperty. Format:
            ``networks/{network_code}/webProperties/{web_property_code}``
        web_property_code (str):
            Required. The ``WebProperty`` code.
        product_type (google.ads.admanager_v1.types.ExchangeSyndicationProductEnum.ExchangeSyndicationProduct):
            Required. The ExchangeSyndicationProduct
            associated with this WebProperty.
        web_property_id (int):
            Optional. The ``WebProperty`` ID.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    web_property_code: str = proto.Field(
        proto.STRING,
        number=2,
    )
    product_type: exchange_syndication_product_enum.ExchangeSyndicationProductEnum.ExchangeSyndicationProduct = proto.Field(
        proto.ENUM,
        number=3,
        enum=exchange_syndication_product_enum.ExchangeSyndicationProductEnum.ExchangeSyndicationProduct,
    )
    web_property_id: int = proto.Field(
        proto.INT64,
        number=4,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
