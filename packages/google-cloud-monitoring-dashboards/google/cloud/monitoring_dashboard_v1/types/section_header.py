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
    package="google.monitoring.dashboard.v1",
    manifest={
        "SectionHeader",
    },
)


class SectionHeader(proto.Message):
    r"""A widget that defines a new section header. Sections populate
    a table of contents and allow easier navigation of long-form
    content.

    Attributes:
        subtitle (str):
            The subtitle of the section
        divider_below (bool):
            Whether to insert a divider below the section
            in the table of contents
    """

    subtitle: str = proto.Field(
        proto.STRING,
        number=1,
    )
    divider_below: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
