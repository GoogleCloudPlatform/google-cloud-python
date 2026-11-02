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
        "CesToolSpec",
    },
)


class CesToolSpec(proto.Message):
    r"""Spec of CES tool that the generator can choose from.

    Attributes:
        ces_tool (str):
            Optional. Format:
            ``projects/<Project ID>/locations/<Location ID>/apps/<app ID>/tools/<tool ID>``.
        confirmation_requirement (google.cloud.dialogflow_v2beta1.types.Tool.ConfirmationRequirement):
            Optional. Indicates whether the tool requires
            human confirmation.
    """

    ces_tool: str = proto.Field(
        proto.STRING,
        number=1,
    )
    confirmation_requirement: tool.Tool.ConfirmationRequirement = proto.Field(
        proto.ENUM,
        number=2,
        enum=tool.Tool.ConfirmationRequirement,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
