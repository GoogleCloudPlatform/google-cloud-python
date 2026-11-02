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

from google.cloud.ces_v1beta.types import schema

__protobuf__ = proto.module(
    package="google.cloud.ces.v1beta",
    manifest={
        "ClientFunction",
    },
)


class ClientFunction(proto.Message):
    r"""Represents a client-side function that the agent can invoke. When
    the tool is chosen by the agent, control is handed off to the
    client. The client is responsible for executing the function and
    returning the result as a
    [ToolResponse][google.cloud.ces.v1beta.ToolResponse] to continue the
    interaction with the agent.

    Attributes:
        name (str):
            Required. The function name.
        description (str):
            Optional. The function description.
        parameters (google.cloud.ces_v1beta.types.Schema):
            Optional. The schema of the function
            parameters.
        response (google.cloud.ces_v1beta.types.Schema):
            Optional. The schema of the function
            response.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    parameters: schema.Schema = proto.Field(
        proto.MESSAGE,
        number=3,
        message=schema.Schema,
    )
    response: schema.Schema = proto.Field(
        proto.MESSAGE,
        number=4,
        message=schema.Schema,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
