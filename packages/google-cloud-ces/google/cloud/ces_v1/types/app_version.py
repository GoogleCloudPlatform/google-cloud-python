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

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.ces_v1.types import agent, example, guardrail, tool, toolset
from google.cloud.ces_v1.types import app as gcc_app

__protobuf__ = proto.module(
    package="google.cloud.ces.v1",
    manifest={
        "AppSnapshot",
        "AppVersion",
    },
)


class AppSnapshot(proto.Message):
    r"""A snapshot of the app.

    Attributes:
        app (google.cloud.ces_v1.types.App):
            Optional. The basic settings for the app.
        agents (MutableSequence[google.cloud.ces_v1.types.Agent]):
            Optional. List of agents in the app.
        tools (MutableSequence[google.cloud.ces_v1.types.Tool]):
            Optional. List of tools in the app.
        examples (MutableSequence[google.cloud.ces_v1.types.Example]):
            Optional. List of examples in the app.
        guardrails (MutableSequence[google.cloud.ces_v1.types.Guardrail]):
            Optional. List of guardrails in the app.
        toolsets (MutableSequence[google.cloud.ces_v1.types.Toolset]):
            Optional. List of toolsets in the app.
    """

    app: gcc_app.App = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcc_app.App,
    )
    agents: MutableSequence[agent.Agent] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=agent.Agent,
    )
    tools: MutableSequence[tool.Tool] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=tool.Tool,
    )
    examples: MutableSequence[example.Example] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=example.Example,
    )
    guardrails: MutableSequence[guardrail.Guardrail] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message=guardrail.Guardrail,
    )
    toolsets: MutableSequence[toolset.Toolset] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message=toolset.Toolset,
    )


class AppVersion(proto.Message):
    r"""In Customer Engagement Suite (CES), an app version is a
    snapshot of the app at a specific point in time. It is immutable
    and cannot be modified once created.

    Attributes:
        name (str):
            Identifier. The unique identifier of the app version.
            Format:
            ``projects/{project}/locations/{location}/apps/{app}/versions/{version}``
        display_name (str):
            Optional. The display name of the app
            version.
        description (str):
            Optional. The description of the app version.
        creator (str):
            Output only. Email of the user who created
            the app version.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the app version
            was created.
        snapshot (google.cloud.ces_v1.types.AppSnapshot):
            Output only. The snapshot of the app when the
            version is created.
        etag (str):
            Output only. Etag used to ensure the object
            hasn't changed during a read-modify-write
            operation. If the etag is empty, the update will
            overwrite any concurrent changes.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    creator: str = proto.Field(
        proto.STRING,
        number=4,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    snapshot: "AppSnapshot" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="AppSnapshot",
    )
    etag: str = proto.Field(
        proto.STRING,
        number=7,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
