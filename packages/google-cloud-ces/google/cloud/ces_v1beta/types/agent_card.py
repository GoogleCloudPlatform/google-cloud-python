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
    package="google.cloud.ces.v1beta",
    manifest={
        "AgentCard",
        "AgentInterface",
        "AgentSkill",
        "RemoteAgentTool",
    },
)


class AgentCard(proto.Message):
    r"""AgentCard conveys key information about a remote agent.
    It is a trimmed version of the AgentCard defined in the A2A
    protocol
    https://a2a-protocol.org/dev/specification/#441-agentcard

    Attributes:
        name (str):
            Required. A human-readable name for the
            agent.
        description (str):
            Required. A description of the agent's domain
            of action/solution space.
        supported_interfaces (MutableSequence[google.cloud.ces_v1beta.types.AgentInterface]):
            Required. Ordered list of supported
            interfaces. The first entry is preferred.
        version (str):
            Required. The version of the agent.
        skills (MutableSequence[google.cloud.ces_v1beta.types.AgentSkill]):
            Required. Skills represent a unit of ability
            an agent can perform. This may somewhat abstract
            but represents a more focused set of actions
            that the agent is highly likely to succeed at.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    supported_interfaces: MutableSequence["AgentInterface"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="AgentInterface",
    )
    version: str = proto.Field(
        proto.STRING,
        number=5,
    )
    skills: MutableSequence["AgentSkill"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="AgentSkill",
    )


class AgentInterface(proto.Message):
    r"""Declares a combination of a target URL, transport and
    protocol version for interacting with the agent. This allows
    agents to expose the same functionality over multiple protocol
    binding mechanisms.

    Attributes:
        url (str):
            Required. The URL where this interface is
            available. Must be a valid absolute HTTPS URL in
            production. Example:

            "https://api.example.com/a2a/v1",
            "https://grpc.example.com/a2a".
        protocol_binding (str):
            Required. The protocol binding supported at this URL. This
            is an open form string, to be easily extended for other
            protocol bindings. The core ones officially supported are
            ``JSONRPC``, ``GRPC`` and ``HTTP+JSON``.
        tenant (str):
            Tenant ID to be used in the request when
            calling the agent.
        protocol_version (str):
            Required. The version of the A2A protocol
            this interface exposes. Use the latest supported
            minor version per major version. Examples:
            "0.3", "1.0".
    """

    url: str = proto.Field(
        proto.STRING,
        number=1,
    )
    protocol_binding: str = proto.Field(
        proto.STRING,
        number=2,
    )
    tenant: str = proto.Field(
        proto.STRING,
        number=3,
    )
    protocol_version: str = proto.Field(
        proto.STRING,
        number=4,
    )


class AgentSkill(proto.Message):
    r"""Represents a distinct capability or function that an agent
    can perform.

    Attributes:
        id (str):
            Required. A unique identifier for the agent's
            skill.
        name (str):
            Required. A human-readable name for the
            skill.
        description (str):
            Required. A detailed description of the
            skill.
        tags (MutableSequence[str]):
            Required. A set of keywords describing the
            skill's capabilities.
        examples (MutableSequence[str]):
            Example prompts or scenarios that this skill
            can handle.
        input_modes (MutableSequence[str]):
            The set of supported input media types for
            this skill, overriding the agent's defaults.
        output_modes (MutableSequence[str]):
            The set of supported output media types for
            this skill, overriding the agent's defaults.
    """

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    examples: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    input_modes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    output_modes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )


class RemoteAgentTool(proto.Message):
    r"""Represents a tool that allows the agent to call another
    remote agent.

    Attributes:
        name (str):
            Required. The name of the tool.
        description (str):
            Required. The description of the tool.
        agent_card (google.cloud.ces_v1beta.types.AgentCard):
            Required. The agent card of the remote agent
            that this tool invokes.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    agent_card: "AgentCard" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="AgentCard",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
