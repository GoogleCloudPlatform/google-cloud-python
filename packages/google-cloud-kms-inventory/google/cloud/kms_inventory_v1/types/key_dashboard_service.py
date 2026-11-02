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
from google.cloud.kms_v1.types import resources

__protobuf__ = proto.module(
    package="google.cloud.kms.inventory.v1",
    manifest={
        "ListCryptoKeysRequest",
        "ListCryptoKeysResponse",
    },
)


class ListCryptoKeysRequest(proto.Message):
    r"""Request message for
    [KeyDashboardService.ListCryptoKeys][google.cloud.kms.inventory.v1.KeyDashboardService.ListCryptoKeys].

    Attributes:
        parent (str):
            Required. The Google Cloud project for which to retrieve key
            metadata, in the format ``projects/*``
        page_size (int):
            Optional. The maximum number of keys to
            return. The service may return fewer than this
            value. If unspecified, at most 1000 keys will be
            returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            Optional. Pass this into a subsequent request
            in order to receive the next page of results.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListCryptoKeysResponse(proto.Message):
    r"""Response message for
    [KeyDashboardService.ListCryptoKeys][google.cloud.kms.inventory.v1.KeyDashboardService.ListCryptoKeys].

    Attributes:
        crypto_keys (MutableSequence[google.cloud.kms_v1.types.CryptoKey]):
            The list of [CryptoKeys][google.cloud.kms.v1.CryptoKey].
        next_page_token (str):
            The page token returned from the previous
            response if the next page is desired.
    """

    @property
    def raw_page(self):
        return self

    crypto_keys: MutableSequence[resources.CryptoKey] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.CryptoKey,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
