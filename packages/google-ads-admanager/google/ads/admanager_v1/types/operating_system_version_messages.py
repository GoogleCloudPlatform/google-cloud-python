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
        "OperatingSystemVersion",
    },
)


class OperatingSystemVersion(proto.Message):
    r"""Represents a specific version of an operating system.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the
            ``OperatingSystemVersion``. Format:
            ``networks/{network_code}/operatingSystemVersions/{operating_system_version_id}``
        major_version (int):
            Output only. The major version of the
            operating system.

            This field is a member of `oneof`_ ``_major_version``.
        minor_version (int):
            Output only. The minor version of the
            operating system.

            This field is a member of `oneof`_ ``_minor_version``.
        micro_version (int):
            Output only. The micro version of the
            operating system.

            This field is a member of `oneof`_ ``_micro_version``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    major_version: int = proto.Field(
        proto.INT32,
        number=2,
        optional=True,
    )
    minor_version: int = proto.Field(
        proto.INT32,
        number=3,
        optional=True,
    )
    micro_version: int = proto.Field(
        proto.INT32,
        number=4,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
