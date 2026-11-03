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

from google.cloud.ces_v1beta.types import auth

__protobuf__ = proto.module(
    package="google.cloud.ces.v1beta",
    manifest={
        "AgentCard",
        "AgentInterface",
        "AgentSkill",
        "RemoteA2aConfig",
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


class RemoteA2aConfig(proto.Message):
    r"""Shared configuration for connecting to a remote
    `A2A <https://github.com/a2aproject/A2A>`__ agent.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        agent_card (google.cloud.ces_v1beta.types.AgentCard):
            Optional. The full agent card defined inline.

            This field is a member of `oneof`_ ``agent_spec``.
        agent_registry (str):
            Optional. Reference to the agent in the Agent Registry.
            Format:
            ``projects/{project}/locations/{location}/agents/{agent}``

            This field is a member of `oneof`_ ``agent_spec``.
        api_authentication (google.cloud.ces_v1beta.types.ApiAuthentication):
            Optional. Authentication configuration for
            calling the remote agent. Optional if the
            registry reference already handles
            authentication.
        input_variable_mapping (MutableMapping[str, str]):
            Optional. Mapping of input variable names of
            remote agent to GECX variable names.
        output_variable_mapping (MutableMapping[str, str]):
            Optional. Mapping of output variable names of
            remote agent to GECX variable names.
        streaming_enabled (bool):
            Optional. Whether streaming is enabled for
            the remote agent.
        context_id (str):
            Optional. If not empty, interactions with the remote A2A
            agent will use this context ID. This context_id field can
            refer to a session variable like
            ``$context.variables.order_agent_session_id``.
    """

    agent_card: "AgentCard" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="agent_spec",
        message="AgentCard",
    )
    agent_registry: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="agent_spec",
    )
    api_authentication: auth.ApiAuthentication = proto.Field(
        proto.MESSAGE,
        number=3,
        message=auth.ApiAuthentication,
    )
    input_variable_mapping: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    output_variable_mapping: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    streaming_enabled: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    context_id: str = proto.Field(
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
        api_authentication (google.cloud.ces_v1beta.types.ApiAuthentication):
            Optional. Authentication configuration for
            calling the remote agent.
        stateful_agent (bool):
            Optional. When enabled, the interaction between the CXAS app
            and the remote agent will share the same context. If the
            remote agent returns a context_id, it will be persisted for
            the entirety of the session for this remote agent tool.
        input_variable_mapping (MutableMapping[str, str]):
            Optional. Mapping of input variable names of
            remote agent to GECX variable names.
        output_variable_mapping (MutableMapping[str, str]):
            Optional. Mapping of output variable names of
            remote agent to GECX variable names.
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
    api_authentication: auth.ApiAuthentication = proto.Field(
        proto.MESSAGE,
        number=4,
        message=auth.ApiAuthentication,
    )
    stateful_agent: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    input_variable_mapping: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    output_variable_mapping: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
