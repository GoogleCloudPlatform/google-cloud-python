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
    package="google.cloud.securitycenter.v2",
    manifest={
        "Application",
    },
)


class Application(proto.Message):
    r"""Represents an application associated with a finding.

    Attributes:
        base_uri (str):
            The base URI that identifies the network location of the
            application in which the vulnerability was detected. For
            example, ``http://example.com``.
        full_uri (str):
            The full URI with payload that could be used to reproduce
            the vulnerability. For example,
            ``http://example.com?p=aMmYgI6H``.
    """

    base_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    full_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
