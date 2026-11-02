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

from google.cloud.dialogflow_v2beta1.types import (
    agent_coaching_instruction,
    ces_app,
    ces_tool,
    toolset,
)
from google.cloud.dialogflow_v2beta1.types import tool_call as gcd_tool_call

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.v2beta1",
    manifest={
        "TriggerEvent",
        "CreateGeneratorRequest",
        "GetGeneratorRequest",
        "ListGeneratorsRequest",
        "ListGeneratorsResponse",
        "DeleteGeneratorRequest",
        "UpdateGeneratorRequest",
        "MessageEntry",
        "ConversationContext",
        "SummarizationSectionList",
        "FewShotExample",
        "InferenceParameter",
        "AgentCoachingContext",
        "SummarizationSection",
        "SummarizationContext",
        "FreeFormContext",
        "Generator",
        "FreeFormSuggestion",
        "SummarySuggestion",
        "AgentCoachingSuggestion",
        "GeneratorSuggestion",
        "SuggestionDedupingConfig",
        "RaiSettings",
    },
)


class TriggerEvent(proto.Enum):
    r"""The event that triggers the generator and LLM execution.

    Values:
        TRIGGER_EVENT_UNSPECIFIED (0):
            Default value for TriggerEvent.
        END_OF_UTTERANCE (1):
            Triggers when each chat message or voice
            utterance ends.
        MANUAL_CALL (2):
            Triggers on the conversation manually by API
            calls, such as
            Conversations.GenerateStatelessSuggestion and
            Conversations.GenerateSuggestions.
        CUSTOMER_MESSAGE (3):
            Triggers after each customer message only.
        AGENT_MESSAGE (4):
            Triggers after each agent message only.
    """

    TRIGGER_EVENT_UNSPECIFIED = 0
    END_OF_UTTERANCE = 1
    MANUAL_CALL = 2
    CUSTOMER_MESSAGE = 3
    AGENT_MESSAGE = 4


class CreateGeneratorRequest(proto.Message):
    r"""Request message of CreateGenerator.

    Attributes:
        parent (str):
            Required. The project/location to create generator for.
            Format: ``projects/<Project ID>/locations/<Location ID>``
        generator (google.cloud.dialogflow_v2beta1.types.Generator):
            Required. The generator to create.
        generator_id (str):
            Optional. The ID to use for the generator, which will become
            the final component of the generator's resource name.

            The generator ID must be compliant with the regression
            formula ``[a-zA-Z][a-zA-Z0-9_-]*`` with the characters
            length in range of [3,64]. If the field is not provided, an
            Id will be auto-generated. If the field is provided, the
            caller is responsible for

            1. the uniqueness of the ID, otherwise the request will be
               rejected.
            2. the consistency for whether to use custom ID or not under
               a project to better ensure uniqueness.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    generator: "Generator" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Generator",
    )
    generator_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GetGeneratorRequest(proto.Message):
    r"""Request message of GetGenerator.

    Attributes:
        name (str):
            Required. The generator resource name to retrieve. Format:
            ``projects/<Project ID>/locations/<Location ID>``/generators/\`
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListGeneratorsRequest(proto.Message):
    r"""Request message of ListGenerators.

    Attributes:
        parent (str):
            Required. The project/location to list generators for.
            Format: ``projects/<Project ID>/locations/<Location ID>``
        page_size (int):
            Optional. Maximum number of conversation
            models to return in a single page. Default to
            10.
        page_token (str):
            Optional. The next_page_token value returned from a previous
            list request.
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


class ListGeneratorsResponse(proto.Message):
    r"""Response of ListGenerators.

    Attributes:
        generators (MutableSequence[google.cloud.dialogflow_v2beta1.types.Generator]):
            List of generators retrieved.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    generators: MutableSequence["Generator"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Generator",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteGeneratorRequest(proto.Message):
    r"""Request of DeleteGenerator.

    Attributes:
        name (str):
            Required. The generator resource name to delete. Format:
            ``projects/<Project ID>/locations/<Location ID>/generators/<Generator ID>``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateGeneratorRequest(proto.Message):
    r"""Request of UpdateGenerator.

    Attributes:
        generator (google.cloud.dialogflow_v2beta1.types.Generator):
            Required. The generator to update.
            The name field of generator is to identify the
            generator to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    generator: "Generator" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Generator",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class MessageEntry(proto.Message):
    r"""Represents a message entry of a conversation.

    Attributes:
        role (google.cloud.dialogflow_v2beta1.types.MessageEntry.Role):
            Optional. Participant role of the message.
        text (str):
            Optional. Transcript content of the message.
        language_code (str):
            Optional. The language of the text. See `Language
            Support <https://cloud.google.com/dialogflow/docs/reference/language>`__
            for a list of the currently supported language codes.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. Create time of the message entry.
    """

    class Role(proto.Enum):
        r"""Enumeration of the roles a participant can play in a
        conversation.

        Values:
            ROLE_UNSPECIFIED (0):
                Participant role not set.
            HUMAN_AGENT (1):
                Participant is a human agent.
            AUTOMATED_AGENT (2):
                Participant is an automated agent, such as a
                Dialogflow agent.
            END_USER (3):
                Participant is an end user that has called or
                chatted with Dialogflow services.
        """

        ROLE_UNSPECIFIED = 0
        HUMAN_AGENT = 1
        AUTOMATED_AGENT = 2
        END_USER = 3

    role: Role = proto.Field(
        proto.ENUM,
        number=1,
        enum=Role,
    )
    text: str = proto.Field(
        proto.STRING,
        number=2,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=3,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


class ConversationContext(proto.Message):
    r"""Context of the conversation, including transcripts.

    Attributes:
        message_entries (MutableSequence[google.cloud.dialogflow_v2beta1.types.MessageEntry]):
            Optional. List of message transcripts in the
            conversation.
    """

    message_entries: MutableSequence["MessageEntry"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="MessageEntry",
    )


class SummarizationSectionList(proto.Message):
    r"""List of summarization sections.

    Attributes:
        summarization_sections (MutableSequence[google.cloud.dialogflow_v2beta1.types.SummarizationSection]):
            Optional. Summarization sections.
    """

    summarization_sections: MutableSequence["SummarizationSection"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="SummarizationSection",
        )
    )


class FewShotExample(proto.Message):
    r"""Providing examples in the generator (i.e. building a few-shot
    generator) helps convey the desired format of the LLM response.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        conversation_context (google.cloud.dialogflow_v2beta1.types.ConversationContext):
            Optional. Conversation transcripts.
        extra_info (MutableMapping[str, str]):
            Optional. Key is the placeholder field name
            in input, value is the value of the placeholder.
            E.g. instruction contains "@price", and ingested
            data has <"price", "10">
        summarization_section_list (google.cloud.dialogflow_v2beta1.types.SummarizationSectionList):
            Summarization sections.

            This field is a member of `oneof`_ ``instruction_list``.
        output (google.cloud.dialogflow_v2beta1.types.GeneratorSuggestion):
            Required. Example output of the model.
    """

    conversation_context: "ConversationContext" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ConversationContext",
    )
    extra_info: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    summarization_section_list: "SummarizationSectionList" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="instruction_list",
        message="SummarizationSectionList",
    )
    output: "GeneratorSuggestion" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="GeneratorSuggestion",
    )


class InferenceParameter(proto.Message):
    r"""The parameters of inference.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        max_output_tokens (int):
            Optional. Maximum number of the output tokens
            for the generator.

            This field is a member of `oneof`_ ``_max_output_tokens``.
        temperature (float):
            Optional. Controls the randomness of LLM
            predictions. Low temperature = less random. High
            temperature = more random. If unset (or 0), uses
            a default value of 0.

            This field is a member of `oneof`_ ``_temperature``.
        top_k (int):
            Optional. Top-k changes how the model selects tokens for
            output. A top-k of 1 means the selected token is the most
            probable among all tokens in the model's vocabulary (also
            called greedy decoding), while a top-k of 3 means that the
            next token is selected from among the 3 most probable tokens
            (using temperature). For each token selection step, the top
            K tokens with the highest probabilities are sampled. Then
            tokens are further filtered based on topP with the final
            token selected using temperature sampling. Specify a lower
            value for less random responses and a higher value for more
            random responses. Acceptable value is [1, 40], default to
            40.

            This field is a member of `oneof`_ ``_top_k``.
        top_p (float):
            Optional. Top-p changes how the model selects tokens for
            output. Tokens are selected from most K (see topK parameter)
            probable to least until the sum of their probabilities
            equals the top-p value. For example, if tokens A, B, and C
            have a probability of 0.3, 0.2, and 0.1 and the top-p value
            is 0.5, then the model will select either A or B as the next
            token (using temperature) and doesn't consider C. The
            default top-p value is 0.95. Specify a lower value for less
            random responses and a higher value for more random
            responses. Acceptable value is [0.0, 1.0], default to 0.95.

            This field is a member of `oneof`_ ``_top_p``.
    """

    max_output_tokens: int = proto.Field(
        proto.INT32,
        number=1,
        optional=True,
    )
    temperature: float = proto.Field(
        proto.DOUBLE,
        number=2,
        optional=True,
    )
    top_k: int = proto.Field(
        proto.INT32,
        number=3,
        optional=True,
    )
    top_p: float = proto.Field(
        proto.DOUBLE,
        number=4,
        optional=True,
    )


class AgentCoachingContext(proto.Message):
    r"""Agent Coaching context that customer can configure.

    Attributes:
        overarching_guidance (str):
            Optional. The overarching guidance for the
            agent coaching. This should be set only for v1.5
            and later versions.
        instructions (MutableSequence[google.cloud.dialogflow_v2beta1.types.AgentCoachingInstruction]):
            Optional. Customized instructions for agent
            coaching.
        version (str):
            Optional. Version of the feature. If not set, default to
            latest version. Current candidates are ["2.5"].
        output_language_code (str):
            Optional. Output language code.
    """

    overarching_guidance: str = proto.Field(
        proto.STRING,
        number=7,
    )
    instructions: MutableSequence[
        agent_coaching_instruction.AgentCoachingInstruction
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=agent_coaching_instruction.AgentCoachingInstruction,
    )
    version: str = proto.Field(
        proto.STRING,
        number=2,
    )
    output_language_code: str = proto.Field(
        proto.STRING,
        number=9,
    )


class SummarizationSection(proto.Message):
    r"""Represents the section of summarization.

    Attributes:
        key (str):
            Optional. Name of the section, for example,
            "situation".
        definition (str):
            Optional. Definition of the section, for
            example, "what the customer needs help with or
            has question about.".
        type_ (google.cloud.dialogflow_v2beta1.types.SummarizationSection.Type):
            Optional. Type of the summarization section.
    """

    class Type(proto.Enum):
        r"""Type enum of the summarization sections.

        Values:
            TYPE_UNSPECIFIED (0):
                Undefined section type, does not return
                anything.
            SITUATION (1):
                What the customer needs help with or has
                question about. Section name: "situation".
            ACTION (2):
                What the agent does to help the customer.
                Section name: "action".
            RESOLUTION (3):
                Result of the customer service. A single word
                describing the result of the conversation.
                Section name: "resolution".
            REASON_FOR_CANCELLATION (4):
                Reason for cancellation if the customer requests for a
                cancellation. "N/A" otherwise. Section name:
                "reason_for_cancellation".
            CUSTOMER_SATISFACTION (5):
                "Unsatisfied" or "Satisfied" depending on the customer's
                feelings at the end of the conversation. Section name:
                "customer_satisfaction".
            ENTITIES (6):
                Key entities extracted from the conversation,
                such as ticket number, order number, dollar
                amount, etc. Section names are prefixed by
                "entities/".
            CUSTOMER_DEFINED (7):
                Customer defined sections.
            SITUATION_CONCISE (9):
                Concise version of the situation section.
                This type is only available if type SITUATION is
                not selected.
            ACTION_CONCISE (10):
                Concise version of the action section. This
                type is only available if type ACTION is not
                selected.
        """

        TYPE_UNSPECIFIED = 0
        SITUATION = 1
        ACTION = 2
        RESOLUTION = 3
        REASON_FOR_CANCELLATION = 4
        CUSTOMER_SATISFACTION = 5
        ENTITIES = 6
        CUSTOMER_DEFINED = 7
        SITUATION_CONCISE = 9
        ACTION_CONCISE = 10

    key: str = proto.Field(
        proto.STRING,
        number=1,
    )
    definition: str = proto.Field(
        proto.STRING,
        number=2,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=3,
        enum=Type,
    )


class SummarizationContext(proto.Message):
    r"""Summarization context that customer can configure.

    Attributes:
        summarization_sections (MutableSequence[google.cloud.dialogflow_v2beta1.types.SummarizationSection]):
            Optional. List of sections. Note it contains
            both predefined section sand customer defined
            sections.
        few_shot_examples (MutableSequence[google.cloud.dialogflow_v2beta1.types.FewShotExample]):
            Optional. List of few shot examples.
        version (str):
            Optional. Version of the feature. If not set, default to
            latest version. Current candidates are ["1.0"].
        output_language_code (str):
            Optional. The target language of the
            generated summary. The language code for
            conversation will be used if this field is
            empty. Supported 2.0 and later versions.
    """

    summarization_sections: MutableSequence["SummarizationSection"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="SummarizationSection",
        )
    )
    few_shot_examples: MutableSequence["FewShotExample"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="FewShotExample",
    )
    version: str = proto.Field(
        proto.STRING,
        number=3,
    )
    output_language_code: str = proto.Field(
        proto.STRING,
        number=6,
    )


class FreeFormContext(proto.Message):
    r"""Free form generator context that customer can configure.

    Attributes:
        text (str):
            Optional. Free form text input to LLM.
    """

    text: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Generator(proto.Message):
    r"""LLM generator.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. Identifier. The resource name of the generator.
            Format:
            ``projects/<Project ID>/locations/<Location ID>/generators/<Generator ID>``
        description (str):
            Optional. Human readable description of the
            generator.
        free_form_context (google.cloud.dialogflow_v2beta1.types.FreeFormContext):
            Input of free from generator to LLM.

            This field is a member of `oneof`_ ``context``.
        agent_coaching_context (google.cloud.dialogflow_v2beta1.types.AgentCoachingContext):
            Input of Agent Coaching feature.

            This field is a member of `oneof`_ ``context``.
        summarization_context (google.cloud.dialogflow_v2beta1.types.SummarizationContext):
            Input of Summarization feature.

            This field is a member of `oneof`_ ``context``.
        inference_parameter (google.cloud.dialogflow_v2beta1.types.InferenceParameter):
            Optional. Inference parameters for this
            generator.
        trigger_event (google.cloud.dialogflow_v2beta1.types.TriggerEvent):
            Optional. The trigger event of the generator.
            It defines when the generator is triggered in a
            conversation.
        published_model (str):
            Optional. The published Large Language Model name.

            - To use the latest model version, specify the model name
              without version number. Example: ``text-bison``
            - To use a stable model version, specify the version number
              as well. Example: ``text-bison@002``.

            This field is a member of `oneof`_ ``foundation_model``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Creation time of this generator.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Update time of this generator.
        tools (MutableSequence[str]):
            Optional. Resource names of the tools that the generator can
            choose from. Format:
            ``projects/<Project ID>/locations/<Location ID>/tools/<tool ID>``.
        suggestion_deduping_config (google.cloud.dialogflow_v2beta1.types.SuggestionDedupingConfig):
            Optional. Configuration for suggestion
            deduping. This is only applicable to AI Coach
            feature.
        toolset_tools (MutableSequence[google.cloud.dialogflow_v2beta1.types.ToolsetTool]):
            Optional. List of CES toolset specs that the
            generator can choose from.
        ces_tool_specs (MutableSequence[google.cloud.dialogflow_v2beta1.types.CesToolSpec]):
            Optional. List of CES tool specs that the
            generator can choose from.
        ces_app_specs (MutableSequence[google.cloud.dialogflow_v2beta1.types.CesAppSpec]):
            Optional. Deprecated: Use ``ces_tool_specs`` instead. List
            of CES app specs that the generator can choose from.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    free_form_context: "FreeFormContext" = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="context",
        message="FreeFormContext",
    )
    agent_coaching_context: "AgentCoachingContext" = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="context",
        message="AgentCoachingContext",
    )
    summarization_context: "SummarizationContext" = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="context",
        message="SummarizationContext",
    )
    inference_parameter: "InferenceParameter" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="InferenceParameter",
    )
    trigger_event: "TriggerEvent" = proto.Field(
        proto.ENUM,
        number=5,
        enum="TriggerEvent",
    )
    published_model: str = proto.Field(
        proto.STRING,
        number=15,
        oneof="foundation_model",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    tools: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=14,
    )
    suggestion_deduping_config: "SuggestionDedupingConfig" = proto.Field(
        proto.MESSAGE,
        number=23,
        message="SuggestionDedupingConfig",
    )
    toolset_tools: MutableSequence[toolset.ToolsetTool] = proto.RepeatedField(
        proto.MESSAGE,
        number=27,
        message=toolset.ToolsetTool,
    )
    ces_tool_specs: MutableSequence[ces_tool.CesToolSpec] = proto.RepeatedField(
        proto.MESSAGE,
        number=28,
        message=ces_tool.CesToolSpec,
    )
    ces_app_specs: MutableSequence[ces_app.CesAppSpec] = proto.RepeatedField(
        proto.MESSAGE,
        number=29,
        message=ces_app.CesAppSpec,
    )


class FreeFormSuggestion(proto.Message):
    r"""Suggestion generated using free form generator.

    Attributes:
        response (str):
            Required. Free form suggestion.
    """

    response: str = proto.Field(
        proto.STRING,
        number=1,
    )


class SummarySuggestion(proto.Message):
    r"""Suggested summary of the conversation.

    Attributes:
        summary_sections (MutableSequence[google.cloud.dialogflow_v2beta1.types.SummarySuggestion.SummarySection]):
            Required. All the parts of generated summary.
    """

    class SummarySection(proto.Message):
        r"""A component of the generated summary.

        Attributes:
            section (str):
                Required. Name of the section.
            summary (str):
                Required. Summary text for the section.
        """

        section: str = proto.Field(
            proto.STRING,
            number=1,
        )
        summary: str = proto.Field(
            proto.STRING,
            number=2,
        )

    summary_sections: MutableSequence[SummarySection] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=SummarySection,
    )


class AgentCoachingSuggestion(proto.Message):
    r"""Suggestion for coaching agents.

    Attributes:
        applicable_instructions (MutableSequence[google.cloud.dialogflow_v2beta1.types.AgentCoachingInstruction]):
            Optional. Instructions applicable based on
            the current context.
        agent_action_suggestions (MutableSequence[google.cloud.dialogflow_v2beta1.types.AgentCoachingSuggestion.AgentActionSuggestion]):
            Optional. Suggested actions for the agent to
            take.
        sample_responses (MutableSequence[google.cloud.dialogflow_v2beta1.types.AgentCoachingSuggestion.SampleResponse]):
            Optional. Sample response for the Agent.
    """

    class Sources(proto.Message):
        r"""Sources for the suggestion.

        Attributes:
            instruction_indexes (MutableSequence[int]):
                Output only. Source instruction indexes for the suggestion.
                This is the index of the applicable_instructions field.
        """

        instruction_indexes: MutableSequence[int] = proto.RepeatedField(
            proto.INT32,
            number=2,
        )

    class DuplicateCheckResult(proto.Message):
        r"""Duplication check for the suggestion.

        Attributes:
            duplicate_suggestions (MutableSequence[google.cloud.dialogflow_v2beta1.types.AgentCoachingSuggestion.DuplicateCheckResult.DuplicateSuggestion]):
                Output only. The duplicate suggestions.
        """

        class DuplicateSuggestion(proto.Message):
            r"""The duplicate suggestion details. Keeping answer_record and sources
            together as they are identifiers for duplicate suggestions.

            Attributes:
                answer_record (str):
                    Output only. The answer record id of the past
                    duplicate suggestion.
                sources (google.cloud.dialogflow_v2beta1.types.AgentCoachingSuggestion.Sources):
                    Output only. Sources for the suggestion.
                suggestion_index (int):
                    Output only. The index of the duplicate
                    suggestion in the past suggestion list.
                similarity_score (float):
                    Output only. The similarity score of between
                    the past and current suggestion.
            """

            answer_record: str = proto.Field(
                proto.STRING,
                number=1,
            )
            sources: "AgentCoachingSuggestion.Sources" = proto.Field(
                proto.MESSAGE,
                number=2,
                message="AgentCoachingSuggestion.Sources",
            )
            suggestion_index: int = proto.Field(
                proto.INT32,
                number=3,
            )
            similarity_score: float = proto.Field(
                proto.FLOAT,
                number=4,
            )

        duplicate_suggestions: MutableSequence[
            "AgentCoachingSuggestion.DuplicateCheckResult.DuplicateSuggestion"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="AgentCoachingSuggestion.DuplicateCheckResult.DuplicateSuggestion",
        )

    class AgentActionSuggestion(proto.Message):
        r"""Actions suggested for the agent. This is based on applicable
        instructions.

        Attributes:
            agent_action (str):
                Optional. The suggested action for the agent.
            sources (google.cloud.dialogflow_v2beta1.types.AgentCoachingSuggestion.Sources):
                Output only. Sources for the agent action
                suggestion.
            duplicate_check_result (google.cloud.dialogflow_v2beta1.types.AgentCoachingSuggestion.DuplicateCheckResult):
                Output only. Duplicate check result for the
                agent action suggestion.
        """

        agent_action: str = proto.Field(
            proto.STRING,
            number=1,
        )
        sources: "AgentCoachingSuggestion.Sources" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="AgentCoachingSuggestion.Sources",
        )
        duplicate_check_result: "AgentCoachingSuggestion.DuplicateCheckResult" = (
            proto.Field(
                proto.MESSAGE,
                number=3,
                message="AgentCoachingSuggestion.DuplicateCheckResult",
            )
        )

    class SampleResponse(proto.Message):
        r"""Sample response that the agent can use. This could be based
        on applicable instructions and ingested data from other systems.

        Attributes:
            response_text (str):
                Optional. Sample response for Agent in text.
            sources (google.cloud.dialogflow_v2beta1.types.AgentCoachingSuggestion.Sources):
                Output only. Sources for the Sample Response.
            duplicate_check_result (google.cloud.dialogflow_v2beta1.types.AgentCoachingSuggestion.DuplicateCheckResult):
                Output only. Duplicate check result for the
                sample response.
        """

        response_text: str = proto.Field(
            proto.STRING,
            number=1,
        )
        sources: "AgentCoachingSuggestion.Sources" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="AgentCoachingSuggestion.Sources",
        )
        duplicate_check_result: "AgentCoachingSuggestion.DuplicateCheckResult" = (
            proto.Field(
                proto.MESSAGE,
                number=3,
                message="AgentCoachingSuggestion.DuplicateCheckResult",
            )
        )

    applicable_instructions: MutableSequence[
        agent_coaching_instruction.AgentCoachingInstruction
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=agent_coaching_instruction.AgentCoachingInstruction,
    )
    agent_action_suggestions: MutableSequence[AgentActionSuggestion] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message=AgentActionSuggestion,
        )
    )
    sample_responses: MutableSequence[SampleResponse] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=SampleResponse,
    )


class GeneratorSuggestion(proto.Message):
    r"""Suggestion generated using a Generator.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        free_form_suggestion (google.cloud.dialogflow_v2beta1.types.FreeFormSuggestion):
            Optional. Free form suggestion.

            This field is a member of `oneof`_ ``suggestion``.
        summary_suggestion (google.cloud.dialogflow_v2beta1.types.SummarySuggestion):
            Optional. Suggested summary.

            This field is a member of `oneof`_ ``suggestion``.
        agent_coaching_suggestion (google.cloud.dialogflow_v2beta1.types.AgentCoachingSuggestion):
            Optional. Suggestion to coach the agent.

            This field is a member of `oneof`_ ``suggestion``.
        tool_call_info (MutableSequence[google.cloud.dialogflow_v2beta1.types.GeneratorSuggestion.ToolCallInfo]):
            Optional. List of request and response for
            tool calls executed.
    """

    class ToolCallInfo(proto.Message):
        r"""Request and response for a tool call.

        Attributes:
            tool_call (google.cloud.dialogflow_v2beta1.types.ToolCall):
                Required. Request for a tool call.
            tool_call_result (google.cloud.dialogflow_v2beta1.types.ToolCallResult):
                Required. Response for a tool call.
        """

        tool_call: gcd_tool_call.ToolCall = proto.Field(
            proto.MESSAGE,
            number=1,
            message=gcd_tool_call.ToolCall,
        )
        tool_call_result: gcd_tool_call.ToolCallResult = proto.Field(
            proto.MESSAGE,
            number=2,
            message=gcd_tool_call.ToolCallResult,
        )

    free_form_suggestion: "FreeFormSuggestion" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="suggestion",
        message="FreeFormSuggestion",
    )
    summary_suggestion: "SummarySuggestion" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="suggestion",
        message="SummarySuggestion",
    )
    agent_coaching_suggestion: "AgentCoachingSuggestion" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="suggestion",
        message="AgentCoachingSuggestion",
    )
    tool_call_info: MutableSequence[ToolCallInfo] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message=ToolCallInfo,
    )


class SuggestionDedupingConfig(proto.Message):
    r"""Config for suggestion deduping. NEXT_ID: 3

    Attributes:
        enable_deduping (bool):
            Optional. Whether to enable suggestion
            deduping.
        similarity_threshold (float):
            Optional. The threshold for similarity between two
            suggestions. Acceptable value is [0.0, 1.0], default to 0.8
    """

    enable_deduping: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    similarity_threshold: float = proto.Field(
        proto.FLOAT,
        number=2,
    )


class RaiSettings(proto.Message):
    r"""Settings for Responsible AI checks.

    Attributes:
        rai_category_configs (MutableSequence[google.cloud.dialogflow_v2beta1.types.RaiSettings.RaiCategoryConfig]):
            Configuration for a set of RAI categories.
    """

    class RaiCategoryConfig(proto.Message):
        r"""Configuration for a specific RAI category.

        Attributes:
            category (google.cloud.dialogflow_v2beta1.types.RaiSettings.RaiCategoryConfig.RaiCategory):
                Optional. The RAI category.
            sensitivity_level (google.cloud.dialogflow_v2beta1.types.RaiSettings.RaiCategoryConfig.SensitivityLevel):
                Optional. The sensitivity level for this
                category.
        """

        class RaiCategory(proto.Enum):
            r"""Enum for RAI category.

            Values:
                RAI_CATEGORY_UNSPECIFIED (0):
                    Default value.
                DANGEROUS_CONTENT (1):
                    Dangerous content.
                SEXUALLY_EXPLICIT (2):
                    Sexually explicit content.
                HARASSMENT (3):
                    Harassment content.
                HATE_SPEECH (4):
                    Hate speech content.
            """

            RAI_CATEGORY_UNSPECIFIED = 0
            DANGEROUS_CONTENT = 1
            SEXUALLY_EXPLICIT = 2
            HARASSMENT = 3
            HATE_SPEECH = 4

        class SensitivityLevel(proto.Enum):
            r"""Enum for user-configurable sensitivity levels.

            Values:
                SENSITIVITY_LEVEL_UNSPECIFIED (0):
                    Default value. If unspecified, the default behavior is:

                    - DANGEROUS_CONTENT: BLOCK_FEW
                    - SEXUALLY_EXPLICIT: BLOCK_SOME
                    - HARASSMENT: BLOCK_SOME
                    - HATE_SPEECH: BLOCK_SOME
                BLOCK_MOST (1):
                    Block most potentially sensitive responses.
                BLOCK_SOME (2):
                    Block some potentially sensitive responses.
                BLOCK_FEW (3):
                    Block a few potentially sensitive responses.
                BLOCK_NONE (4):
                    No filtering for this category.
            """

            SENSITIVITY_LEVEL_UNSPECIFIED = 0
            BLOCK_MOST = 1
            BLOCK_SOME = 2
            BLOCK_FEW = 3
            BLOCK_NONE = 4

        category: "RaiSettings.RaiCategoryConfig.RaiCategory" = proto.Field(
            proto.ENUM,
            number=1,
            enum="RaiSettings.RaiCategoryConfig.RaiCategory",
        )
        sensitivity_level: "RaiSettings.RaiCategoryConfig.SensitivityLevel" = (
            proto.Field(
                proto.ENUM,
                number=2,
                enum="RaiSettings.RaiCategoryConfig.SensitivityLevel",
            )
        )

    rai_category_configs: MutableSequence[RaiCategoryConfig] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=RaiCategoryConfig,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
