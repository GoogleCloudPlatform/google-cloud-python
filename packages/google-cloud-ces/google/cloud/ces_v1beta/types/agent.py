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

from google.cloud.ces_v1beta.types import agent_transfers, common

__protobuf__ = proto.module(
    package="google.cloud.ces.v1beta",
    manifest={
        "Agent",
    },
)


class Agent(proto.Message):
    r"""An agent acts as the fundamental building block that provides
    instructions to the Large Language Model (LLM) for executing
    specific tasks.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        llm_agent (google.cloud.ces_v1beta.types.Agent.LlmAgent):
            Optional. The default agent type.

            This field is a member of `oneof`_ ``agent_type``.
        remote_dialogflow_agent (google.cloud.ces_v1beta.types.Agent.RemoteDialogflowAgent):
            Optional. The remote
            `Dialogflow <https://cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents>`__
            agent to be used for the agent execution. If this field is
            set, all other agent level properties will be ignored.

            Note: If the Dialogflow agent is in a different project from
            the app, you should grant ``roles/dialogflow.client`` to the
            CES service agent
            ``service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com``.

            This field is a member of `oneof`_ ``agent_type``.
        name (str):
            Identifier. The unique identifier of the agent. Format:
            ``projects/{project}/locations/{location}/apps/{app}/agents/{agent}``
        display_name (str):
            Required. Display name of the agent.
        description (str):
            Optional. Human-readable description of the
            agent.
        model_settings (google.cloud.ces_v1beta.types.ModelSettings):
            Optional. Configurations for the LLM model.
        instruction (str):
            Optional. Instructions for the LLM model to
            guide the agent's behavior.
        tools (MutableSequence[str]):
            Optional. List of available tools for the agent. Format:
            ``projects/{project}/locations/{location}/apps/{app}/tools/{tool}``
        child_agents (MutableSequence[str]):
            Optional. List of child agents in the agent tree. Format:
            ``projects/{project}/locations/{location}/apps/{app}/agents/{agent}``
        before_agent_callbacks (MutableSequence[google.cloud.ces_v1beta.types.Callback]):
            Optional. The callbacks to execute before the
            agent is called. The provided callbacks are
            executed sequentially in the exact order they
            are given in the list. If a callback returns an
            overridden response, execution stops and any
            remaining callbacks are skipped.
        after_agent_callbacks (MutableSequence[google.cloud.ces_v1beta.types.Callback]):
            Optional. The callbacks to execute after the
            agent is called. The provided callbacks are
            executed sequentially in the exact order they
            are given in the list. If a callback returns an
            overridden response, execution stops and any
            remaining callbacks are skipped.
        before_model_callbacks (MutableSequence[google.cloud.ces_v1beta.types.Callback]):
            Optional. The callbacks to execute before the
            model is called. If there are multiple calls to
            the model, the callback will be executed
            multiple times. The provided callbacks are
            executed sequentially in the exact order they
            are given in the list. If a callback returns an
            overridden response, execution stops and any
            remaining callbacks are skipped.
        after_model_callbacks (MutableSequence[google.cloud.ces_v1beta.types.Callback]):
            Optional. The callbacks to execute after the
            model is called. If there are multiple calls to
            the model, the callback will be executed
            multiple times. The provided callbacks are
            executed sequentially in the exact order they
            are given in the list. If a callback returns an
            overridden response, execution stops and any
            remaining callbacks are skipped.
        before_tool_callbacks (MutableSequence[google.cloud.ces_v1beta.types.Callback]):
            Optional. The callbacks to execute before the
            tool is invoked. If there are multiple tool
            invocations, the callback will be executed
            multiple times. The provided callbacks are
            executed sequentially in the exact order they
            are given in the list. If a callback returns an
            overridden response, execution stops and any
            remaining callbacks are skipped.
        after_tool_callbacks (MutableSequence[google.cloud.ces_v1beta.types.Callback]):
            Optional. The callbacks to execute after the
            tool is invoked. If there are multiple tool
            invocations, the callback will be executed
            multiple times. The provided callbacks are
            executed sequentially in the exact order they
            are given in the list. If a callback returns an
            overridden response, execution stops and any
            remaining callbacks are skipped.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the agent was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the agent was
            last updated.
        guardrails (MutableSequence[str]):
            Optional. List of guardrails for the agent. Format:
            ``projects/{project}/locations/{location}/apps/{app}/guardrails/{guardrail}``
        etag (str):
            Etag used to ensure the object hasn't changed
            during a read-modify-write operation. If the
            etag is empty, the update will overwrite any
            concurrent changes.
        toolsets (MutableSequence[google.cloud.ces_v1beta.types.Agent.AgentToolset]):
            Optional. List of toolsets for the agent.
        generated_summary (str):
            Output only. If the agent is generated by the
            LLM assistant, this field contains a descriptive
            summary of the generation.
        transfer_rules (MutableSequence[google.cloud.ces_v1beta.types.TransferRule]):
            Optional. Agent transfer rules.
            If multiple rules match, the first one in the
            list will be used.
        validation_errors (MutableSequence[str]):
            Output only. Misconfigurations or errors in
            the agent that may affect agent quality.
    """

    class LlmAgent(proto.Message):
        r"""Default agent type. The agent uses instructions and callbacks
        specified in the agent to perform the task using a large
        language model.

        """

    class RemoteDialogflowAgent(proto.Message):
        r"""The agent which will transfer execution to a remote `Dialogflow
        CX <https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent>`__
        agent. The Dialogflow agent will process subsequent user queries
        until the session ends or flow ends, and the control is transferred
        back to the parent CES agent.

        Attributes:
            agent (str):
                Required. The
                `Dialogflow <https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent>`__
                agent resource name. Format:
                ``projects/{project}/locations/{location}/agents/{agent}``
            flow_id (str):
                Optional. The flow ID of the flow in the
                Dialogflow agent.
            environment_id (str):
                Optional. The environment ID of the
                Dialogflow agent to be used for the agent
                execution. If not specified, the draft
                environment will be used.
            input_variable_mapping (MutableMapping[str, str]):
                Optional. The mapping of the app variables
                names to the Dialogflow session parameters names
                to be sent to the Dialogflow agent as input.
            output_variable_mapping (MutableMapping[str, str]):
                Optional. The mapping of the Dialogflow
                session parameters names to the app variables
                names to be sent back to the CES agent after the
                Dialogflow agent execution ends.
            respect_response_interruption_settings (bool):
                Optional. Indicates whether to respect the message-level
                interruption settings configured in the Dialogflow agent.

                - If false: all response messages from the Dialogflow agent
                  follow the app-level barge-in settings.
                - If true: only response messages with
                  ```allow_playback_interruption`` <https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#text>`__
                  set to true will be interruptable, all other messages
                  follow the app-level barge-in settings.
            language_code_variable (str):
                Optional. The name of the variable that
                contains the language code to be used for the
                Dialogflow session. If unspecified, the default
                language code of the Dialogflow agent will be
                used.
        """

        agent: str = proto.Field(
            proto.STRING,
            number=1,
        )
        flow_id: str = proto.Field(
            proto.STRING,
            number=2,
        )
        environment_id: str = proto.Field(
            proto.STRING,
            number=3,
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
        respect_response_interruption_settings: bool = proto.Field(
            proto.BOOL,
            number=6,
        )
        language_code_variable: str = proto.Field(
            proto.STRING,
            number=7,
        )

    class AgentToolset(proto.Message):
        r"""A toolset with a selection of its tools.

        Attributes:
            toolset (str):
                Required. The resource name of the toolset. Format:
                ``projects/{project}/locations/{location}/apps/{app}/toolsets/{toolset}``
            tool_ids (MutableSequence[str]):
                Optional. The tools IDs to filter the
                toolset.
        """

        toolset: str = proto.Field(
            proto.STRING,
            number=1,
        )
        tool_ids: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=4,
        )

    llm_agent: LlmAgent = proto.Field(
        proto.MESSAGE,
        number=26,
        oneof="agent_type",
        message=LlmAgent,
    )
    remote_dialogflow_agent: RemoteDialogflowAgent = proto.Field(
        proto.MESSAGE,
        number=27,
        oneof="agent_type",
        message=RemoteDialogflowAgent,
    )
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
    model_settings: common.ModelSettings = proto.Field(
        proto.MESSAGE,
        number=4,
        message=common.ModelSettings,
    )
    instruction: str = proto.Field(
        proto.STRING,
        number=6,
    )
    tools: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    child_agents: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    before_agent_callbacks: MutableSequence[common.Callback] = proto.RepeatedField(
        proto.MESSAGE,
        number=18,
        message=common.Callback,
    )
    after_agent_callbacks: MutableSequence[common.Callback] = proto.RepeatedField(
        proto.MESSAGE,
        number=19,
        message=common.Callback,
    )
    before_model_callbacks: MutableSequence[common.Callback] = proto.RepeatedField(
        proto.MESSAGE,
        number=20,
        message=common.Callback,
    )
    after_model_callbacks: MutableSequence[common.Callback] = proto.RepeatedField(
        proto.MESSAGE,
        number=21,
        message=common.Callback,
    )
    before_tool_callbacks: MutableSequence[common.Callback] = proto.RepeatedField(
        proto.MESSAGE,
        number=22,
        message=common.Callback,
    )
    after_tool_callbacks: MutableSequence[common.Callback] = proto.RepeatedField(
        proto.MESSAGE,
        number=23,
        message=common.Callback,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=15,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=16,
        message=timestamp_pb2.Timestamp,
    )
    guardrails: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=17,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=24,
    )
    toolsets: MutableSequence[AgentToolset] = proto.RepeatedField(
        proto.MESSAGE,
        number=28,
        message=AgentToolset,
    )
    generated_summary: str = proto.Field(
        proto.STRING,
        number=29,
    )
    transfer_rules: MutableSequence[agent_transfers.TransferRule] = proto.RepeatedField(
        proto.MESSAGE,
        number=30,
        message=agent_transfers.TransferRule,
    )
    validation_errors: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=32,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
