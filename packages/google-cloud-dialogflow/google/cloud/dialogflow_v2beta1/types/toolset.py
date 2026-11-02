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

from google.cloud.dialogflow_v2beta1.types import tool

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.v2beta1",
    manifest={
        "ToolsetTool",
    },
)


class ToolsetTool(proto.Message):
    r"""A tool that is created from a toolset.

    Attributes:
        toolset (str):
            Required. The name of the toolset to retrieve the schema
            for. Format:
            ``projects/{project}/locations/{location}/apps/{app}/toolsets/{toolset}``
        operation_id (str):
            Optional. The operationId field of the
            OpenAPI endpoint. The operationId must be
            present in the toolset's definition.
        confirmation_requirement (google.cloud.dialogflow_v2beta1.types.Tool.ConfirmationRequirement):
            Optional. Indicates whether the tool requires
            human confirmation.
    """

    toolset: str = proto.Field(
        proto.STRING,
        number=1,
    )
    operation_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    confirmation_requirement: tool.Tool.ConfirmationRequirement = proto.Field(
        proto.ENUM,
        number=3,
        enum=tool.Tool.ConfirmationRequirement,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
