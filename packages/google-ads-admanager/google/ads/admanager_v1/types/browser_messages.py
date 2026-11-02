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
    package="google.ads.admanager.v1",
    manifest={
        "Browser",
    },
)


class Browser(proto.Message):
    r"""Represents a browser, including its version.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the ``Browser``. Format:
            ``networks/{network_code}/browsers/{browser}``
        display_name (str):
            Output only. The display name of the browser,
            including version info.

            This field is a member of `oneof`_ ``_display_name``.
        major_version (str):
            Output only. The major version of the
            browser.

            This field is a member of `oneof`_ ``_major_version``.
        minor_version (str):
            Output only. The minor version of the
            browser.

            This field is a member of `oneof`_ ``_minor_version``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    major_version: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    minor_version: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
