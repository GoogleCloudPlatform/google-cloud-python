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

import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.agentregistry_v1.types import properties

__protobuf__ = proto.module(
    package="google.cloud.agentregistry.v1",
    manifest={
        "Agent",
    },
)


class Agent(proto.Message):
    r"""Represents an Agent.
    "A2A" below refers to the Agent-to-Agent protocol.

    Attributes:
        name (str):
            Identifier. The resource name of an Agent. Format:
            ``projects/{project}/locations/{location}/agents/{agent}``.
        agent_id (str):
            Output only. A stable, globally unique
            identifier for agents.
        location (str):
            Output only. The location where agent is
            hosted. The value is defined by the hosting
            environment (i.e. cloud provider).
        display_name (str):
            Output only. The display name of the agent,
            often obtained from the A2A Agent Card.
        description (str):
            Output only. The description of the Agent,
            often obtained from the A2A Agent Card. Empty if
            Agent Card has no description.
        version (str):
            Output only. The version of the Agent, often
            obtained from the A2A Agent Card. Empty if Agent
            Card has no version or agent is not an A2A
            Agent.
        protocols (MutableSequence[google.cloud.agentregistry_v1.types.Agent.Protocol]):
            Output only. The connection details for the
            Agent.
        skills (MutableSequence[google.cloud.agentregistry_v1.types.Agent.Skill]):
            Output only. Skills the agent possesses,
            often obtained from the A2A Agent Card.
        uid (str):
            Output only. A universally unique identifier
            for the Agent.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Update time.
        attributes (MutableMapping[str, google.protobuf.struct_pb2.Struct]):
            Output only. Attributes of the Agent. Valid values:

            - ``agentregistry.googleapis.com/system/Framework``:
              {"framework": "google-adk"} - the agent framework used to
              develop the Agent. Example values: "google-adk",
              "langchain", "custom".
            - ``agentregistry.googleapis.com/system/RuntimeIdentity``:
              {"principal": "principal://..."} - the runtime identity
              associated with the Agent.
            - ``agentregistry.googleapis.com/system/RuntimeReference``:
              {"uri": "//..."}

            - the URI of the underlying resource hosting the Agent, for
              example, the Reasoning Engine URI.
        card (google.cloud.agentregistry_v1.types.Agent.Card):
            Output only. Full Agent Card payload, when
            available.
    """

    class Protocol(proto.Message):
        r"""Represents the protocol of an Agent.

        Attributes:
            type_ (google.cloud.agentregistry_v1.types.Agent.Protocol.Type):
                Output only. The type of the protocol.
            protocol_version (str):
                Output only. The version of the protocol, for
                example, the A2A Agent Card version.
            interfaces (MutableSequence[google.cloud.agentregistry_v1.types.Interface]):
                Output only. The connection details for the
                Agent.
        """

        class Type(proto.Enum):
            r"""The type of the protocol.

            Values:
                TYPE_UNSPECIFIED (0):
                    Unspecified type.
                A2A_AGENT (1):
                    The interfaces point to an A2A Agent
                    following the A2A specification.
                CUSTOM (2):
                    Agent does not follow any standard protocol.
            """

            TYPE_UNSPECIFIED = 0
            A2A_AGENT = 1
            CUSTOM = 2

        type_: "Agent.Protocol.Type" = proto.Field(
            proto.ENUM,
            number=1,
            enum="Agent.Protocol.Type",
        )
        protocol_version: str = proto.Field(
            proto.STRING,
            number=2,
        )
        interfaces: MutableSequence[properties.Interface] = proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message=properties.Interface,
        )

    class Skill(proto.Message):
        r"""Represents the skills of an Agent.

        Attributes:
            id (str):
                Output only. A unique identifier for the
                agent's skill.
            name (str):
                Output only. A human-readable name for the
                agent's skill.
            description (str):
                Output only. A more detailed description of
                the skill.
            tags (MutableSequence[str]):
                Output only. Keywords describing the skill.
            examples (MutableSequence[str]):
                Output only. Example prompts or scenarios
                this skill can handle.
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

    class Card(proto.Message):
        r"""Full Agent Card payload, often obtained from the A2A Agent
        Card.

        Attributes:
            type_ (google.cloud.agentregistry_v1.types.Agent.Card.Type):
                Output only. The type of agent card.
            content (google.protobuf.struct_pb2.Struct):
                Output only. The content of the agent card.
        """

        class Type(proto.Enum):
            r"""Represents the type of the agent card.

            Values:
                TYPE_UNSPECIFIED (0):
                    Unspecified type.
                A2A_AGENT_CARD (1):
                    Indicates that the card is an A2A Agent Card.
            """

            TYPE_UNSPECIFIED = 0
            A2A_AGENT_CARD = 1

        type_: "Agent.Card.Type" = proto.Field(
            proto.ENUM,
            number=1,
            enum="Agent.Card.Type",
        )
        content: struct_pb2.Struct = proto.Field(
            proto.MESSAGE,
            number=2,
            message=struct_pb2.Struct,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    agent_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    location: str = proto.Field(
        proto.STRING,
        number=4,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    description: str = proto.Field(
        proto.STRING,
        number=6,
    )
    version: str = proto.Field(
        proto.STRING,
        number=7,
    )
    protocols: MutableSequence[Protocol] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message=Protocol,
    )
    skills: MutableSequence[Skill] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message=Skill,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=10,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=11,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=12,
        message=timestamp_pb2.Timestamp,
    )
    attributes: MutableMapping[str, struct_pb2.Struct] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=13,
        message=struct_pb2.Struct,
    )
    card: Card = proto.Field(
        proto.MESSAGE,
        number=14,
        message=Card,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
