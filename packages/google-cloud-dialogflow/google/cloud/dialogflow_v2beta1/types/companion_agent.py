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

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.dialogflow_v2beta1.types import ces_tool, toolset

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.v2beta1",
    manifest={
        "CreateCompanionAgentRequest",
        "GetCompanionAgentRequest",
        "ListCompanionAgentsRequest",
        "ListCompanionAgentsResponse",
        "UpdateCompanionAgentRequest",
        "DeleteCompanionAgentRequest",
        "GuidanceInstruction",
        "CompanionAgent",
    },
)


class CreateCompanionAgentRequest(proto.Message):
    r"""Request of CreateCompanionAgent.

    Attributes:
        parent (str):
            Required. Resource identifier of the project creating the
            companion agent. Format:
            ``projects/{project}/locations/{location}``
        companion_agent (google.cloud.dialogflow_v2beta1.types.CompanionAgent):
            Required. The companion agent to create.
        companion_agent_id (str):
            Optional. The resource ID of the companion
            agent to create. If not provided, the server
            will auto-generate a resource ID.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    companion_agent: "CompanionAgent" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="CompanionAgent",
    )
    companion_agent_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GetCompanionAgentRequest(proto.Message):
    r"""Request message for GetCompanionAgent.

    Attributes:
        name (str):
            Required. The unique resource identifier of the
            CompanionAgent to get all information for. Format:
            ``projects/{project}/locations/{location}/companionAgents/{companion_agent}``.
            Contains the information about the project_id, location_id,
            companion_agent_id
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListCompanionAgentsRequest(proto.Message):
    r"""Request message for ListCompanionAgents.

    Attributes:
        parent (str):
            Required. The parent resource name to list the companion
            agents for. Format:
            ``projects/{project}/locations/{location}``
        page_size (int):
            Optional. Maximum number of companion agents
            to return in a single page. By default 100 and
            at most 1000.
        page_token (str):
            Optional. The page token, received from a
            previous call.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListCompanionAgentsResponse(proto.Message):
    r"""Response message for ListCompanionAgents.

    Attributes:
        companion_agents (MutableSequence[google.cloud.dialogflow_v2beta1.types.CompanionAgent]):
            The list of companion agents.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    companion_agents: MutableSequence["CompanionAgent"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="CompanionAgent",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateCompanionAgentRequest(proto.Message):
    r"""Request message for UpdateCompanionAgent.

    Attributes:
        companion_agent (google.cloud.dialogflow_v2beta1.types.CompanionAgent):
            Required. The Companion Agent to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Update mask for Companion Agent.
    """

    companion_agent: "CompanionAgent" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="CompanionAgent",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteCompanionAgentRequest(proto.Message):
    r"""Request message for DeleteCompanionAgent.

    Attributes:
        name (str):
            Required. The unique resource identifier of the
            CompanionAgent to delete. Format:
            ``projects/{project}/locations/{location}/companionAgents/{companion_agent}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GuidanceInstruction(proto.Message):
    r"""Guidance instruction for the companion agent.

    Attributes:
        display_name (str):
            Optional. Display name for the instruction.
            This name should be unique within the companion
            agent.
        display_details (str):
            Optional. The detailed description of this
            instruction.
        condition (str):
            Optional. The condition of the instruction.
            For example, "the customer wants to cancel an
            order".  If the users want the instruction to be
            triggered unconditionally, the condition can be
            empty.
        actions (MutableSequence[google.cloud.dialogflow_v2beta1.types.GuidanceInstruction.Action]):
            Optional. The action items that can be
            processed.
        trigger_event (google.cloud.dialogflow_v2beta1.types.CompanionAgent.TriggerEvent):
            Optional. Event that triggers the guidance instruction. If
            UNSPECIFIED, the instruction triggering will be the same as
            the skill's skill_triggering_event.
        disable_suggested_reply (bool):
            Optional. Whether to disable suggested reply generation for
            this instruction. When set to ``true``, guidance generated
            from this instruction will not include a suggested reply.
            Default is ``false`` (suggested reply enabled).
    """

    class Action(proto.Message):
        r"""Actions to take, including agent action and system action
        (automation).

        Attributes:
            description (str):
                Required. Description of action item. It can
                be a agent action (e.g. "Send a message to the
                customer", "greet the customer") or system
                action (e.g. "Update the ticket", "Create a
                task", "cancel the order").
        """

        description: str = proto.Field(
            proto.STRING,
            number=1,
        )

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_details: str = proto.Field(
        proto.STRING,
        number=2,
    )
    condition: str = proto.Field(
        proto.STRING,
        number=3,
    )
    actions: MutableSequence[Action] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=Action,
    )
    trigger_event: "CompanionAgent.TriggerEvent" = proto.Field(
        proto.ENUM,
        number=6,
        enum="CompanionAgent.TriggerEvent",
    )
    disable_suggested_reply: bool = proto.Field(
        proto.BOOL,
        number=7,
    )


class CompanionAgent(proto.Message):
    r"""Companion agent.

    Attributes:
        name (str):
            Identifier. The unique identifier of the companion agent.
            Format:
            ``projects/{project}/locations/{location}/companionAgents/{companion_agent}``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Creation time of this companion
            agent.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Update time of this companion
            agent.
        toolset_tools (MutableSequence[google.cloud.dialogflow_v2beta1.types.ToolsetTool]):
            Optional. List of CES toolset specs that the
            companion agent can choose from.
        ces_tool_specs (MutableSequence[google.cloud.dialogflow_v2beta1.types.CesToolSpec]):
            Optional. List of CES tool specs that the
            companion agent can choose from.
        display_name (str):
            Optional. Display name for the companion
            agent. Character limit is 63.
        description (str):
            Optional. Description for the companion
            agent.
        skill_configs (MutableSequence[google.cloud.dialogflow_v2beta1.types.CompanionAgent.SkillConfig]):
            Optional. List of skill configs for the companion agent.
            Allows at most one instance of each
            [SkillConfig][google.cloud.dialogflow.v2beta1.CompanionAgent.SkillConfig]
            type.
    """

    class TriggerEvent(proto.Enum):
        r"""Event that triggers companion agent skills and guidance
        instructions.

        Values:
            TRIGGER_EVENT_UNSPECIFIED (0):
                Default value for TriggerEvent. For skill_triggering_event,
                UNSPECIFIED defaults to CUSTOMER_MESSAGE. For instruction
                trigger_event, UNSPECIFIED defaults to the skill's
                skill_triggering_event.
            END_OF_UTTERANCE (1):
                Triggers when each chat message or voice
                utterance ends.
            CUSTOMER_MESSAGE (2):
                Triggers after each customer message.
            AGENT_MESSAGE (3):
                Triggers after each agent message.
        """

        TRIGGER_EVENT_UNSPECIFIED = 0
        END_OF_UTTERANCE = 1
        CUSTOMER_MESSAGE = 2
        AGENT_MESSAGE = 3

    class SkillConfig(proto.Message):
        r"""Skill configuration for the companion agent.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            guidance_skill_config (google.cloud.dialogflow_v2beta1.types.CompanionAgent.GuidanceSkillConfig):
                Optional. Guidance skill configuration.

                This field is a member of `oneof`_ ``config``.
            skill_triggering_event (google.cloud.dialogflow_v2beta1.types.CompanionAgent.SkillConfig.SkillTriggerEvent):
                Optional. The event that should trigger the
                skill.
        """

        class SkillTriggerEvent(proto.Enum):
            r"""The event that should trigger the skill.

            Values:
                SKILL_TRIGGER_EVENT_UNSPECIFIED (0):
                    Default value for SkillTriggerEvent.
                END_OF_UTTERANCE (1):
                    Triggers when each chat message or voice
                    utterance ends.
                CUSTOMER_MESSAGE (2):
                    Triggers after each customer message.
                AGENT_MESSAGE (3):
                    Triggers after each agent message.
            """

            SKILL_TRIGGER_EVENT_UNSPECIFIED = 0
            END_OF_UTTERANCE = 1
            CUSTOMER_MESSAGE = 2
            AGENT_MESSAGE = 3

        guidance_skill_config: "CompanionAgent.GuidanceSkillConfig" = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="config",
            message="CompanionAgent.GuidanceSkillConfig",
        )
        skill_triggering_event: "CompanionAgent.SkillConfig.SkillTriggerEvent" = (
            proto.Field(
                proto.ENUM,
                number=1,
                enum="CompanionAgent.SkillConfig.SkillTriggerEvent",
            )
        )

    class GuidanceSkillConfig(proto.Message):
        r"""Guidance skill configuration.

        Attributes:
            guidance_instructions (MutableSequence[google.cloud.dialogflow_v2beta1.types.GuidanceInstruction]):
                Optional. Customized instructions for
                guidance.
            overarching_guidance (str):
                Optional. This is specific additional
                guidance that can configured by the user.
            knowledge_source (google.cloud.dialogflow_v2beta1.types.CompanionAgent.KnowledgeSource):
                Optional. Knowledge source configuration for
                guidance.
        """

        guidance_instructions: MutableSequence["GuidanceInstruction"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message="GuidanceInstruction",
            )
        )
        overarching_guidance: str = proto.Field(
            proto.STRING,
            number=3,
        )
        knowledge_source: "CompanionAgent.KnowledgeSource" = proto.Field(
            proto.MESSAGE,
            number=5,
            message="CompanionAgent.KnowledgeSource",
        )

    class KnowledgeSource(proto.Message):
        r"""Knowledge source configuration for knowledge retrieval."""

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    toolset_tools: MutableSequence[toolset.ToolsetTool] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=toolset.ToolsetTool,
    )
    ces_tool_specs: MutableSequence[ces_tool.CesToolSpec] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message=ces_tool.CesToolSpec,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=8,
    )
    description: str = proto.Field(
        proto.STRING,
        number=9,
    )
    skill_configs: MutableSequence[SkillConfig] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message=SkillConfig,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
