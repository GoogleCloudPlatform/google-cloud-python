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
    package="google.cloud.ces.v1",
    manifest={
        "ToolsetTool",
    },
)


class ToolsetTool(proto.Message):
    r"""A tool that is created from a toolset.

    Attributes:
        toolset (str):
            Required. The resource name of the Toolset from which this
            tool is derived. Format:
            ``projects/{project}/locations/{location}/apps/{app}/toolsets/{toolset}``
        tool_id (str):
            Optional. The tool ID to filter the tools to
            retrieve the schema for.
    """

    toolset: str = proto.Field(
        proto.STRING,
        number=1,
    )
    tool_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
