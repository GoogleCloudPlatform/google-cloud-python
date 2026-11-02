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

from google.cloud.dialogflowcx_v3beta1.types import data_store_connection

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.cx.v3beta1",
    manifest={
        "OutputState",
        "RetrievalStrategy",
        "TraceBlock",
        "SpeechProcessingMetadata",
        "PlaybookTraceMetadata",
        "FlowTraceMetadata",
        "Action",
        "UserUtterance",
        "Event",
        "AgentUtterance",
        "ToolUse",
        "LlmCall",
        "PlaybookInvocation",
        "FlowInvocation",
        "PlaybookTransition",
        "FlowTransition",
        "PlaybookInput",
        "PlaybookOutput",
        "Span",
        "NamedMetric",
        "Status",
        "ExceptionDetail",
    },
)


class OutputState(proto.Enum):
    r"""Output state.

    Values:
        OUTPUT_STATE_UNSPECIFIED (0):
            Unspecified output.
        OUTPUT_STATE_OK (1):
            Succeeded.
        OUTPUT_STATE_CANCELLED (2):
            Cancelled.
        OUTPUT_STATE_FAILED (3):
            Failed.
        OUTPUT_STATE_ESCALATED (4):
            Escalated.
        OUTPUT_STATE_PENDING (5):
            Pending.
    """

    OUTPUT_STATE_UNSPECIFIED = 0
    OUTPUT_STATE_OK = 1
    OUTPUT_STATE_CANCELLED = 2
    OUTPUT_STATE_FAILED = 3
    OUTPUT_STATE_ESCALATED = 4
    OUTPUT_STATE_PENDING = 5


class RetrievalStrategy(proto.Enum):
    r"""Retrieval strategy on how the example is selected to be fed
    to the prompt.

    Values:
        RETRIEVAL_STRATEGY_UNSPECIFIED (0):
            Not specified. ``DEFAULT`` will be used.
        DEFAULT (1):
            Default retrieval strategy.
        STATIC (2):
            Static example will always be inserted to the
            prompt.
        NEVER (3):
            Example will never be inserted into the
            prompt.
    """

    RETRIEVAL_STRATEGY_UNSPECIFIED = 0
    DEFAULT = 1
    STATIC = 2
    NEVER = 3


class TraceBlock(proto.Message):
    r"""The trace block tracks a sequence of actions taken by the
    agent in a flow or a playbook.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        playbook_trace_metadata (google.cloud.dialogflowcx_v3beta1.types.PlaybookTraceMetadata):
            Metadata of the playbook trace.

            This field is a member of `oneof`_ ``trace_metadata``.
        flow_trace_metadata (google.cloud.dialogflowcx_v3beta1.types.FlowTraceMetadata):
            Metadata of the flow trace.

            This field is a member of `oneof`_ ``trace_metadata``.
        speech_processing_metadata (google.cloud.dialogflowcx_v3beta1.types.SpeechProcessingMetadata):
            Metadata of the speech-to-text and
            speech-to-text processing.

            This field is a member of `oneof`_ ``trace_metadata``.
        actions (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.Action]):
            The actions performed by the agent and the
            user during this session.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp of the start of the
            trace block.
        complete_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp of the end of the
            trace block.
        input_parameters (google.protobuf.struct_pb2.Struct):
            Optional. A list of input parameters of the
            trace block.
        output_parameters (google.protobuf.struct_pb2.Struct):
            Optional. A list of output parameters of the
            trace block.
        end_state (google.cloud.dialogflowcx_v3beta1.types.OutputState):
            Optional. Output only. The end state of the
            trace block.
    """

    playbook_trace_metadata: "PlaybookTraceMetadata" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="trace_metadata",
        message="PlaybookTraceMetadata",
    )
    flow_trace_metadata: "FlowTraceMetadata" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="trace_metadata",
        message="FlowTraceMetadata",
    )
    speech_processing_metadata: "SpeechProcessingMetadata" = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="trace_metadata",
        message="SpeechProcessingMetadata",
    )
    actions: MutableSequence["Action"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="Action",
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    complete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    input_parameters: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=9,
        message=struct_pb2.Struct,
    )
    output_parameters: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=6,
        message=struct_pb2.Struct,
    )
    end_state: "OutputState" = proto.Field(
        proto.ENUM,
        number=7,
        enum="OutputState",
    )


class SpeechProcessingMetadata(proto.Message):
    r"""Metadata of the speech-to-text and text-to-speech processing.

    Attributes:
        display_name (str):
            Output only. The display name of the speech
            processing.
    """

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class PlaybookTraceMetadata(proto.Message):
    r"""Metadata of the playbook trace.

    Attributes:
        playbook (str):
            Required. The unique identifier of the playbook. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>``.
        display_name (str):
            Output only. The display name of the
            playbook.
    """

    playbook: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class FlowTraceMetadata(proto.Message):
    r"""Metadata of the flow trace.

    Attributes:
        flow (str):
            Required. The unique identifier of the flow. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>``.
        display_name (str):
            Output only. The display name of the flow.
    """

    flow: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class Action(proto.Message):
    r"""Action performed by end user or Dialogflow agent in the
    conversation.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        user_utterance (google.cloud.dialogflowcx_v3beta1.types.UserUtterance):
            Optional. Agent obtained a message from the
            customer.

            This field is a member of `oneof`_ ``action``.
        event (google.cloud.dialogflowcx_v3beta1.types.Event):
            Optional. The agent received an event from
            the customer or a system event is emitted.

            This field is a member of `oneof`_ ``action``.
        agent_utterance (google.cloud.dialogflowcx_v3beta1.types.AgentUtterance):
            Optional. Action performed by the agent as a
            message.

            This field is a member of `oneof`_ ``action``.
        tool_use (google.cloud.dialogflowcx_v3beta1.types.ToolUse):
            Optional. Action performed on behalf of the
            agent by calling a plugin tool.

            This field is a member of `oneof`_ ``action``.
        llm_call (google.cloud.dialogflowcx_v3beta1.types.LlmCall):
            Optional. Output only. LLM call performed by
            the agent.

            This field is a member of `oneof`_ ``action``.
        intent_match (google.cloud.dialogflowcx_v3beta1.types.Action.IntentMatch):
            Optional. Output only. Intent Match in flows.

            This field is a member of `oneof`_ ``action``.
        flow_state_update (google.cloud.dialogflowcx_v3beta1.types.Action.FlowStateUpdate):
            Optional. Output only. The state machine
            update in flows.

            This field is a member of `oneof`_ ``action``.
        playbook_invocation (google.cloud.dialogflowcx_v3beta1.types.PlaybookInvocation):
            Optional. Action performed on behalf of the
            agent by invoking a child playbook.

            This field is a member of `oneof`_ ``action``.
        flow_invocation (google.cloud.dialogflowcx_v3beta1.types.FlowInvocation):
            Optional. Action performed on behalf of the
            agent by invoking a CX flow.

            This field is a member of `oneof`_ ``action``.
        playbook_transition (google.cloud.dialogflowcx_v3beta1.types.PlaybookTransition):
            Optional. Action performed on behalf of the
            agent by transitioning to a target playbook.

            This field is a member of `oneof`_ ``action``.
        flow_transition (google.cloud.dialogflowcx_v3beta1.types.FlowTransition):
            Optional. Action performed on behalf of the
            agent by transitioning to a target CX flow.

            This field is a member of `oneof`_ ``action``.
        tts (google.cloud.dialogflowcx_v3beta1.types.Action.TTS):
            Optional. Text-to-speech action performed by
            the agent.

            This field is a member of `oneof`_ ``action``.
        stt (google.cloud.dialogflowcx_v3beta1.types.Action.STT):
            Optional. Speech-to-text action performed by
            the agent.

            This field is a member of `oneof`_ ``action``.
        display_name (str):
            Output only. The display name of the action.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp of the start of the
            agent action.
        complete_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp of the completion of
            the agent action.
        sub_execution_steps (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.Span]):
            Optional. The detailed tracing information
            for sub execution steps of the action.
        status (google.cloud.dialogflowcx_v3beta1.types.Status):
            Optional. Output only. The status of the
            action.
    """

    class IntentMatch(proto.Message):
        r"""Stores metadata of the intent match action.

        Attributes:
            matched_intents (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.Action.IntentMatch.MatchedIntent]):
                The matched intent.
        """

        class MatchedIntent(proto.Message):
            r"""Stores the matched intent, which is the result of the intent
            match action.

            Attributes:
                intent_id (str):
                    The ID of the matched intent.
                display_name (str):
                    The display name of the matched intent.
                score (float):
                    The score of the matched intent.
                generative_fallback (google.protobuf.struct_pb2.Struct):
                    The generative fallback response of the
                    matched intent.
            """

            intent_id: str = proto.Field(
                proto.STRING,
                number=1,
            )
            display_name: str = proto.Field(
                proto.STRING,
                number=2,
            )
            score: float = proto.Field(
                proto.FLOAT,
                number=3,
            )
            generative_fallback: struct_pb2.Struct = proto.Field(
                proto.MESSAGE,
                number=4,
                message=struct_pb2.Struct,
            )

        matched_intents: MutableSequence["Action.IntentMatch.MatchedIntent"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=1,
                message="Action.IntentMatch.MatchedIntent",
            )
        )

    class FlowStateUpdate(proto.Message):
        r"""Stores metadata of the state update action, such as a state
        machine execution in flows.

        Attributes:
            event_type (str):
                The type of the event that triggered the
                state update.
            page_state (google.cloud.dialogflowcx_v3beta1.types.Action.FlowStateUpdate.PageState):
                The updated page and flow state.
            updated_parameters (google.protobuf.struct_pb2.Struct):
                The updated parameters.
            destination (str):
                The destination of the transition. Format:
                ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/pages/<PageID>``
                or
                ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookId>``.
            function_call (google.cloud.dialogflowcx_v3beta1.types.Action.FlowStateUpdate.FunctionCall):
                The function call to execute.
        """

        class PageState(proto.Message):
            r"""Stores the state of a page and its flow.

            Attributes:
                page (str):
                    The ID of the page. Format:
                    ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/pages/<PageID>``.
                display_name (str):
                    The display name of the page.
                status (str):
                    The status of the page.
            """

            page: str = proto.Field(
                proto.STRING,
                number=1,
            )
            display_name: str = proto.Field(
                proto.STRING,
                number=2,
            )
            status: str = proto.Field(
                proto.STRING,
                number=3,
            )

        class FunctionCall(proto.Message):
            r"""Stores the metadata of a function call to execute.

            Attributes:
                name (str):
                    The name of the function call.
            """

            name: str = proto.Field(
                proto.STRING,
                number=1,
            )

        event_type: str = proto.Field(
            proto.STRING,
            number=1,
        )
        page_state: "Action.FlowStateUpdate.PageState" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="Action.FlowStateUpdate.PageState",
        )
        updated_parameters: struct_pb2.Struct = proto.Field(
            proto.MESSAGE,
            number=3,
            message=struct_pb2.Struct,
        )
        destination: str = proto.Field(
            proto.STRING,
            number=4,
        )
        function_call: "Action.FlowStateUpdate.FunctionCall" = proto.Field(
            proto.MESSAGE,
            number=5,
            message="Action.FlowStateUpdate.FunctionCall",
        )

    class TTS(proto.Message):
        r"""Stores metadata of the Text-to-Speech action."""

    class STT(proto.Message):
        r"""Stores metadata of the Speech-to-Text action."""

    user_utterance: "UserUtterance" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="action",
        message="UserUtterance",
    )
    event: "Event" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="action",
        message="Event",
    )
    agent_utterance: "AgentUtterance" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="action",
        message="AgentUtterance",
    )
    tool_use: "ToolUse" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="action",
        message="ToolUse",
    )
    llm_call: "LlmCall" = proto.Field(
        proto.MESSAGE,
        number=14,
        oneof="action",
        message="LlmCall",
    )
    intent_match: IntentMatch = proto.Field(
        proto.MESSAGE,
        number=17,
        oneof="action",
        message=IntentMatch,
    )
    flow_state_update: FlowStateUpdate = proto.Field(
        proto.MESSAGE,
        number=18,
        oneof="action",
        message=FlowStateUpdate,
    )
    playbook_invocation: "PlaybookInvocation" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="action",
        message="PlaybookInvocation",
    )
    flow_invocation: "FlowInvocation" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="action",
        message="FlowInvocation",
    )
    playbook_transition: "PlaybookTransition" = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="action",
        message="PlaybookTransition",
    )
    flow_transition: "FlowTransition" = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="action",
        message="FlowTransition",
    )
    tts: TTS = proto.Field(
        proto.MESSAGE,
        number=19,
        oneof="action",
        message=TTS,
    )
    stt: STT = proto.Field(
        proto.MESSAGE,
        number=20,
        oneof="action",
        message=STT,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=15,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    complete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    sub_execution_steps: MutableSequence["Span"] = proto.RepeatedField(
        proto.MESSAGE,
        number=11,
        message="Span",
    )
    status: "Status" = proto.Field(
        proto.MESSAGE,
        number=16,
        message="Status",
    )


class UserUtterance(proto.Message):
    r"""UserUtterance represents one message sent by the customer.

    Attributes:
        text (str):
            Required. Message content in text.
        audio_tokens (MutableSequence[int]):
            Optional. Tokens of the audio input.
        audio (bytes):
            Optional. Audio input.
    """

    text: str = proto.Field(
        proto.STRING,
        number=1,
    )
    audio_tokens: MutableSequence[int] = proto.RepeatedField(
        proto.INT32,
        number=2,
    )
    audio: bytes = proto.Field(
        proto.BYTES,
        number=3,
    )


class Event(proto.Message):
    r"""Event represents the event sent by the customer.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        event (str):
            Required. Name of the event.
        text (str):
            Optional. Unstructured text payload of the
            event.

            This field is a member of `oneof`_ ``payload``.
    """

    event: str = proto.Field(
        proto.STRING,
        number=1,
    )
    text: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="payload",
    )


class AgentUtterance(proto.Message):
    r"""AgentUtterance represents one message sent by the agent.

    Attributes:
        text (str):
            Required. Message content in text.
        require_generation (bool):
            Optional. True if the agent utterance needs to be generated
            by the LLM. Only used in webhook response to differentiate
            from empty text. Revisit whether we need this field or mark
            ``text`` as optional when we expose webhook interface to
            customer.
    """

    text: str = proto.Field(
        proto.STRING,
        number=1,
    )
    require_generation: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class ToolUse(proto.Message):
    r"""Stores metadata of the invocation of an action supported by a
    tool.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        tool (str):
            Required. The
            [tool][google.cloud.dialogflow.cx.v3beta1.Tool] that should
            be used. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/tools/<ToolID>``.
        display_name (str):
            Output only. The display name of the tool.
        action (str):
            Optional. Name of the action to be called
            during the tool use.
        input_action_parameters (google.protobuf.struct_pb2.Struct):
            Optional. A list of input parameters for the
            action.
        output_action_parameters (google.protobuf.struct_pb2.Struct):
            Optional. A list of output parameters
            generated by the action.
        data_store_tool_trace (google.cloud.dialogflowcx_v3beta1.types.ToolUse.DataStoreToolTrace):
            Optional. Data store tool trace.

            This field is a member of `oneof`_ ``ToolTrace``.
        webhook_tool_trace (google.cloud.dialogflowcx_v3beta1.types.ToolUse.WebhookToolTrace):
            Optional. Webhook tool trace.

            This field is a member of `oneof`_ ``ToolTrace``.
    """

    class DataStoreToolTrace(proto.Message):
        r"""The tracing information for the data store tool.

        Attributes:
            data_store_connection_signals (google.cloud.dialogflowcx_v3beta1.types.DataStoreConnectionSignals):
                Optional. Data store connection feature
                output signals.
        """

        data_store_connection_signals: data_store_connection.DataStoreConnectionSignals = proto.Field(
            proto.MESSAGE,
            number=1,
            message=data_store_connection.DataStoreConnectionSignals,
        )

    class WebhookToolTrace(proto.Message):
        r"""The tracing information for the webhook tool.

        Attributes:
            webhook_tag (str):
                Optional. The tag of the webhook.
            webhook_uri (str):
                Optional. The url of the webhook.
        """

        webhook_tag: str = proto.Field(
            proto.STRING,
            number=1,
        )
        webhook_uri: str = proto.Field(
            proto.STRING,
            number=2,
        )

    tool: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=8,
    )
    action: str = proto.Field(
        proto.STRING,
        number=2,
    )
    input_action_parameters: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=5,
        message=struct_pb2.Struct,
    )
    output_action_parameters: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=6,
        message=struct_pb2.Struct,
    )
    data_store_tool_trace: DataStoreToolTrace = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="ToolTrace",
        message=DataStoreToolTrace,
    )
    webhook_tool_trace: WebhookToolTrace = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="ToolTrace",
        message=WebhookToolTrace,
    )


class LlmCall(proto.Message):
    r"""Stores metadata of the call of an LLM.

    Attributes:
        retrieved_examples (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.LlmCall.RetrievedExample]):
            A list of relevant examples used for the LLM
            prompt.
        token_count (google.cloud.dialogflowcx_v3beta1.types.LlmCall.TokenCount):
            The token counts of the LLM call.
        model (str):
            The model of the LLM call.
        temperature (float):
            The temperature of the LLM call.
    """

    class RetrievedExample(proto.Message):
        r"""Relevant example used for the LLM prompt.

        Attributes:
            example_id (str):
                The id of the example.
            example_display_name (str):
                The display name of the example.
            retrieval_strategy (google.cloud.dialogflowcx_v3beta1.types.RetrievalStrategy):
                Retrieval strategy of the example.
            matched_retrieval_label (str):
                Optional. The matched retrieval label of this
                LLM call.
        """

        example_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        example_display_name: str = proto.Field(
            proto.STRING,
            number=2,
        )
        retrieval_strategy: "RetrievalStrategy" = proto.Field(
            proto.ENUM,
            number=3,
            enum="RetrievalStrategy",
        )
        matched_retrieval_label: str = proto.Field(
            proto.STRING,
            number=14,
        )

    class TokenCount(proto.Message):
        r"""Stores token counts of the LLM call.

        Attributes:
            total_input_token_count (int):
                The total number of tokens used for the input
                to the LLM call.
            conversation_context_token_count (int):
                The number of tokens used for the
                conversation history in the prompt.
            example_token_count (int):
                The number of tokens used for the retrieved
                examples in the prompt.
            total_output_token_count (int):
                The total number of tokens used for the
                output of the LLM call.
        """

        total_input_token_count: int = proto.Field(
            proto.INT64,
            number=1,
        )
        conversation_context_token_count: int = proto.Field(
            proto.INT64,
            number=3,
        )
        example_token_count: int = proto.Field(
            proto.INT64,
            number=4,
        )
        total_output_token_count: int = proto.Field(
            proto.INT64,
            number=5,
        )

    retrieved_examples: MutableSequence[RetrievedExample] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=RetrievedExample,
    )
    token_count: TokenCount = proto.Field(
        proto.MESSAGE,
        number=2,
        message=TokenCount,
    )
    model: str = proto.Field(
        proto.STRING,
        number=3,
    )
    temperature: float = proto.Field(
        proto.FLOAT,
        number=4,
    )


class PlaybookInvocation(proto.Message):
    r"""Stores metadata of the invocation of a child playbook.
    Playbook invocation actions enter the child playbook.

    Attributes:
        playbook (str):
            Required. The unique identifier of the playbook. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>``.
        display_name (str):
            Output only. The display name of the
            playbook.
        playbook_input (google.cloud.dialogflowcx_v3beta1.types.PlaybookInput):
            Optional. Input of the child playbook
            invocation.
        playbook_output (google.cloud.dialogflowcx_v3beta1.types.PlaybookOutput):
            Optional. Output of the child playbook
            invocation.
        playbook_state (google.cloud.dialogflowcx_v3beta1.types.OutputState):
            Required. Playbook invocation's output state.
    """

    playbook: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    playbook_input: "PlaybookInput" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="PlaybookInput",
    )
    playbook_output: "PlaybookOutput" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="PlaybookOutput",
    )
    playbook_state: "OutputState" = proto.Field(
        proto.ENUM,
        number=4,
        enum="OutputState",
    )


class FlowInvocation(proto.Message):
    r"""Stores metadata of the invocation of a child CX flow. Flow
    invocation actions enter the child flow.

    Attributes:
        flow (str):
            Required. The unique identifier of the flow. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<Agentflows/<FlowID>``.
        display_name (str):
            Output only. The display name of the flow.
        input_action_parameters (google.protobuf.struct_pb2.Struct):
            Optional. A list of input parameters for the
            flow.
        output_action_parameters (google.protobuf.struct_pb2.Struct):
            Optional. A list of output parameters
            generated by the flow invocation.
        flow_state (google.cloud.dialogflowcx_v3beta1.types.OutputState):
            Required. Flow invocation's output state.
    """

    flow: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=7,
    )
    input_action_parameters: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=5,
        message=struct_pb2.Struct,
    )
    output_action_parameters: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=6,
        message=struct_pb2.Struct,
    )
    flow_state: "OutputState" = proto.Field(
        proto.ENUM,
        number=4,
        enum="OutputState",
    )


class PlaybookTransition(proto.Message):
    r"""Stores metadata of the transition to another target playbook.
    Playbook transition actions exit the caller playbook and enter
    the target playbook.

    Attributes:
        playbook (str):
            Required. The unique identifier of the playbook. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>``.
        display_name (str):
            Output only. The display name of the
            playbook.
        input_action_parameters (google.protobuf.struct_pb2.Struct):
            A list of input parameters for the action.
    """

    playbook: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    input_action_parameters: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=2,
        message=struct_pb2.Struct,
    )


class FlowTransition(proto.Message):
    r"""Stores metadata of the transition to a target CX flow. Flow
    transition actions exit the caller playbook and enter the child
    flow.

    Attributes:
        flow (str):
            Required. The unique identifier of the flow. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<Agentflows/<FlowID>``.
        display_name (str):
            Output only. The display name of the flow.
        input_action_parameters (google.protobuf.struct_pb2.Struct):
            A list of input parameters for the action.
    """

    flow: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    input_action_parameters: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=2,
        message=struct_pb2.Struct,
    )


class PlaybookInput(proto.Message):
    r"""Input of the playbook.

    Attributes:
        preceding_conversation_summary (str):
            Optional. Summary string of the preceding
            conversation for the child playbook invocation.
        action_parameters (google.protobuf.struct_pb2.Struct):
            Optional. A list of input parameters for the
            action.
    """

    preceding_conversation_summary: str = proto.Field(
        proto.STRING,
        number=1,
    )
    action_parameters: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=3,
        message=struct_pb2.Struct,
    )


class PlaybookOutput(proto.Message):
    r"""Output of the playbook.

    Attributes:
        execution_summary (str):
            Optional. Summary string of the execution
            result of the child playbook.
        state (google.cloud.dialogflowcx_v3beta1.types.PlaybookOutput.State):
            End state of the playbook.
        action_parameters (google.protobuf.struct_pb2.Struct):
            Optional. A Struct object of output
            parameters for the action.
    """

    class State(proto.Enum):
        r"""Playbook output state.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified state.
            OK (1):
                Playbook succeeded.
            CANCELLED (2):
                Playbook cancelled.
            FAILED (3):
                Playbook failed.
            ESCALATED (4):
                Playbook failed due to escalation.
        """

        _pb_options = {"deprecated": True}
        STATE_UNSPECIFIED = 0
        OK = 1
        CANCELLED = 2
        FAILED = 3
        ESCALATED = 4

    execution_summary: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=2,
        enum=State,
    )
    action_parameters: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=4,
        message=struct_pb2.Struct,
    )


class Span(proto.Message):
    r"""A span represents a sub execution step of an action.

    Attributes:
        name (str):
            The name of the span.
        tags (MutableSequence[str]):
            The metadata tags of the span such as span
            type.
        metrics (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.NamedMetric]):
            The unordered collection of metrics in this
            span.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp of the start of the span.
        complete_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp of the completion of the span.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    metrics: MutableSequence["NamedMetric"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="NamedMetric",
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    complete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )


class NamedMetric(proto.Message):
    r"""A named metric is a metric with name, value and unit.

    Attributes:
        name (str):
            The name of the metric.
        value (google.protobuf.struct_pb2.Value):
            The value of the metric.
        unit (str):
            The unit in which this metric is reported. Follows `The
            Unified Code for Units of
            Measure <https://unitsofmeasure.org/ucum.html>`__ standard.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    value: struct_pb2.Value = proto.Field(
        proto.MESSAGE,
        number=2,
        message=struct_pb2.Value,
    )
    unit: str = proto.Field(
        proto.STRING,
        number=3,
    )


class Status(proto.Message):
    r"""The status of the action.

    Attributes:
        exception (google.cloud.dialogflowcx_v3beta1.types.ExceptionDetail):
            Optional. The exception thrown during the
            execution of the action.
    """

    exception: "ExceptionDetail" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ExceptionDetail",
    )


class ExceptionDetail(proto.Message):
    r"""Exception thrown during the execution of an action.

    Attributes:
        error_message (str):
            Optional. The error message.
    """

    error_message: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
