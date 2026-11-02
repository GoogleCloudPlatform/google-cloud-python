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

from google.ads.admanager_v1.types import rich_media_studio_child_asset_type_enum

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "RichMediaStudioChildAssetProperty",
    },
)


class RichMediaStudioChildAssetProperty(proto.Message):
    r"""Represents a child asset in RichMediaStudioCreative.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        display_name (str):
            Output only. The name of the asset as known
            by Rich Media Studio.

            This field is a member of `oneof`_ ``_display_name``.
        type_ (google.ads.admanager_v1.types.RichMediaStudioChildAssetTypeEnum.RichMediaStudioChildAssetType):
            Output only. Required file type of the asset.

            This field is a member of `oneof`_ ``_type``.
        total_file_size (int):
            Output only. The total size of the asset in
            bytes.

            This field is a member of `oneof`_ ``_total_file_size``.
        width (int):
            Output only. Width of the widget in pixels.

            This field is a member of `oneof`_ ``_width``.
        height (int):
            Output only. Height of the widget in pixels.

            This field is a member of `oneof`_ ``_height``.
        url (str):
            Output only. The URL of the asset.

            This field is a member of `oneof`_ ``_url``.
    """

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    type_: rich_media_studio_child_asset_type_enum.RichMediaStudioChildAssetTypeEnum.RichMediaStudioChildAssetType = proto.Field(
        proto.ENUM,
        number=2,
        optional=True,
        enum=rich_media_studio_child_asset_type_enum.RichMediaStudioChildAssetTypeEnum.RichMediaStudioChildAssetType,
    )
    total_file_size: int = proto.Field(
        proto.INT64,
        number=3,
        optional=True,
    )
    width: int = proto.Field(
        proto.INT32,
        number=4,
        optional=True,
    )
    height: int = proto.Field(
        proto.INT32,
        number=5,
        optional=True,
    )
    url: str = proto.Field(
        proto.STRING,
        number=6,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
