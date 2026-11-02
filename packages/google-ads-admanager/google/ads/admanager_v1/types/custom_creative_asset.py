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

from google.ads.admanager_v1.types import creative_asset

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "CustomCreativeAsset",
    },
)


class CustomCreativeAsset(proto.Message):
    r"""A ``CustomCreativeAsset`` is an association between a
    ``CustomCreative`` and an asset. Any assets that are associated with
    a creative can be inserted into its HTML snippet.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        macro_name (str):
            Optional. The name by which the associated
            asset will be referenced. For example, if the
            value is "foo", then the asset can be inserted
            into an HTML snippet using the macro:
            "%%FILE:foo%%".

            This field is a member of `oneof`_ ``_macro_name``.
        asset (google.ads.admanager_v1.types.CreativeAsset):
            Required. The asset. To view the asset, use
            ``CreativeAsset.asset_url``.
    """

    macro_name: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    asset: creative_asset.CreativeAsset = proto.Field(
        proto.MESSAGE,
        number=6,
        message=creative_asset.CreativeAsset,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
