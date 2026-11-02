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

from google.ads.admanager_v1.types import native_style_enums
from google.ads.admanager_v1.types import size as gaa_size
from google.ads.admanager_v1.types import targeting as gaa_targeting

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "NativeStyle",
    },
)


class NativeStyle(proto.Message):
    r"""Used to define the look and feel of native ads, for both web
    and apps. Native styles determine how native creatives look for
    a segment of inventory.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the ``NativeStyle``.
            Format:
            ``networks/{network_code}/nativeStyles/{native_style_id}``
        creative_template (str):
            Required. Immutable. The creative template this native style
            is associated with. Format:
            "networks/{network_code}/creativeTemplates/{creative_template}".

            This field is a member of `oneof`_ ``_creative_template``.
        display_name (str):
            Required. The display name of the native
            style. This attribute has a maximum length of
            255 characters.

            This field is a member of `oneof`_ ``_display_name``.
        html_snippet (str):
            Optional. The HTML snippet of the native
            style with placeholders for the associated
            variables.

            This field is a member of `oneof`_ ``_html_snippet``.
        css_snippet (str):
            Optional. The CSS snippet of the native
            style, with placeholders for the associated
            variables.

            This field is a member of `oneof`_ ``_css_snippet``.
        targeting (google.ads.admanager_v1.types.Targeting):
            Optional. The targeting criteria for this
            native style.
        status (google.ads.admanager_v1.types.NativeStyleStatusEnum.NativeStyleStatus):
            Output only. The status of the native style.

            This field is a member of `oneof`_ ``_status``.
        size (google.ads.admanager_v1.types.Size):
            Required. The size of the native style.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    creative_template: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    html_snippet: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    css_snippet: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    targeting: gaa_targeting.Targeting = proto.Field(
        proto.MESSAGE,
        number=9,
        message=gaa_targeting.Targeting,
    )
    status: native_style_enums.NativeStyleStatusEnum.NativeStyleStatus = proto.Field(
        proto.ENUM,
        number=10,
        optional=True,
        enum=native_style_enums.NativeStyleStatusEnum.NativeStyleStatus,
    )
    size: gaa_size.Size = proto.Field(
        proto.MESSAGE,
        number=12,
        message=gaa_size.Size,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
