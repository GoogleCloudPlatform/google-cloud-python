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

__protobuf__ = proto.module(
    package="google.cloud.discoveryengine.v1beta",
    manifest={
        "Assistant",
    },
)


class Assistant(proto.Message):
    r"""Discovery Engine Assistant resource.

    Attributes:
        name (str):
            Immutable. Resource name of the assistant. Format:
            ``projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/assistants/{assistant}``

            It must be a UTF-8 encoded string with a length limit of
            1024 characters.
        display_name (str):
            Required. The assistant display name.

            It must be a UTF-8 encoded string with a length
            limit of 128 characters.
        description (str):
            Optional. Description for additional
            information. Expected to be shown on the
            configuration UI, not to the users of the
            assistant.
        generation_config (google.cloud.discoveryengine_v1beta.types.Assistant.GenerationConfig):
            Optional. Configuration for the generation of
            the assistant response.
        web_grounding_type (google.cloud.discoveryengine_v1beta.types.Assistant.WebGroundingType):
            Optional. The type of web grounding to use.
        default_web_grounding_toggle_off (bool):
            Optional. This field controls the default web grounding
            toggle for end users if ``web_grounding_type`` is set to
            ``WEB_GROUNDING_TYPE_GOOGLE_SEARCH`` or
            ``WEB_GROUNDING_TYPE_ENTERPRISE_WEB_SEARCH``. By default,
            this field is set to false. If ``web_grounding_type`` is
            ``WEB_GROUNDING_TYPE_GOOGLE_SEARCH`` or
            ``WEB_GROUNDING_TYPE_ENTERPRISE_WEB_SEARCH``, end users will
            have web grounding enabled by default on UI. If true,
            grounding toggle will be disabled by default on UI. End
            users can still enable web grounding in the UI if web
            grounding is enabled.
        enabled_tools (MutableMapping[str, google.cloud.discoveryengine_v1beta.types.Assistant.ToolList]):
            Optional. Note: not implemented yet. Use
            [enabled_actions][google.cloud.discoveryengine.v1beta.Assistant.enabled_actions]
            instead. The enabled tools on this assistant. The keys are
            connector name, for example
            "projects/{projectId}/locations/{locationId}/collections/{collectionId}/dataconnector
            The values consist of admin enabled tools towards the
            connector instance. Admin can selectively enable multiple
            tools on any of the connector instances that they created in
            the project. For example {"jira1ConnectorName": [(toolId1,
            "createTicket"), (toolId2, "transferTicket")],
            "gmail1ConnectorName": [(toolId3, "sendEmail"),..] }
        customer_policy (google.cloud.discoveryengine_v1beta.types.Assistant.CustomerPolicy):
            Optional. Customer policy for the assistant.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Represents the time when this
            Assistant was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Represents the time when this
            Assistant was most recently updated.
    """

    class WebGroundingType(proto.Enum):
        r"""The type of web grounding to use.

        Values:
            WEB_GROUNDING_TYPE_UNSPECIFIED (0):
                Default, unspecified setting. This is the
                same as disabled.
            WEB_GROUNDING_TYPE_DISABLED (1):
                Web grounding is disabled.
            WEB_GROUNDING_TYPE_GOOGLE_SEARCH (2):
                Grounding with Google Search is enabled.
            WEB_GROUNDING_TYPE_ENTERPRISE_WEB_SEARCH (3):
                Grounding with Enterprise Web Search is
                enabled.
        """

        WEB_GROUNDING_TYPE_UNSPECIFIED = 0
        WEB_GROUNDING_TYPE_DISABLED = 1
        WEB_GROUNDING_TYPE_GOOGLE_SEARCH = 2
        WEB_GROUNDING_TYPE_ENTERPRISE_WEB_SEARCH = 3

    class GenerationConfig(proto.Message):
        r"""Configuration for the generation of the assistant response.

        Attributes:
            default_model_id (str):
                Optional. The default model to use for
                assistant.
            allowed_model_ids (MutableSequence[str]):
                Optional. The list of models that are allowed
                to be used for assistant.
            system_instruction (google.cloud.discoveryengine_v1beta.types.Assistant.GenerationConfig.SystemInstruction):
                System instruction, also known as the prompt
                preamble for LLM calls. See also
                https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/system-instructions
            default_language (str):
                The default language to use for the generation of the
                assistant response. Use an ISO 639-1 language code such as
                ``en``. If not specified, the language will be automatically
                detected.
        """

        class SystemInstruction(proto.Message):
            r"""System instruction, also known as the prompt preamble for LLM
            calls.

            Attributes:
                additional_system_instruction (str):
                    Optional. Additional system instruction that
                    will be added to the default system instruction.
            """

            additional_system_instruction: str = proto.Field(
                proto.STRING,
                number=2,
            )

        default_model_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        allowed_model_ids: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )
        system_instruction: "Assistant.GenerationConfig.SystemInstruction" = (
            proto.Field(
                proto.MESSAGE,
                number=3,
                message="Assistant.GenerationConfig.SystemInstruction",
            )
        )
        default_language: str = proto.Field(
            proto.STRING,
            number=4,
        )

    class ToolInfo(proto.Message):
        r"""Information to identify a tool.

        Attributes:
            tool_name (str):
                The name of the tool as defined by
                DataConnectorService.QueryAvailableActions. Note: it's using
                ``action`` in the DataConnectorService apis, but they are
                the same as the ``tool`` here.
            tool_display_name (str):
                The display name of the tool.
        """

        tool_name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        tool_display_name: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class ToolList(proto.Message):
        r"""The enabled tools on a connector

        Attributes:
            tool_info (MutableSequence[google.cloud.discoveryengine_v1beta.types.Assistant.ToolInfo]):
                The list of tools with corresponding tool
                information.
        """

        tool_info: MutableSequence["Assistant.ToolInfo"] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="Assistant.ToolInfo",
        )

    class CustomerPolicy(proto.Message):
        r"""Customer-defined policy for the assistant.

        Attributes:
            banned_phrases (MutableSequence[google.cloud.discoveryengine_v1beta.types.Assistant.CustomerPolicy.BannedPhrase]):
                Optional. List of banned phrases.
            model_armor_config (google.cloud.discoveryengine_v1beta.types.Assistant.CustomerPolicy.ModelArmorConfig):
                Optional. Model Armor configuration to be
                used for sanitizing user prompts and assistant
                responses.
        """

        class BannedPhrase(proto.Message):
            r"""Definition of a customer-defined banned phrase. A banned
            phrase is not allowed to appear in the user query or the LLM
            response, or else the answer will be refused.

            Attributes:
                phrase (str):
                    Required. The raw string content to be
                    banned.
                match_type (google.cloud.discoveryengine_v1beta.types.Assistant.CustomerPolicy.BannedPhrase.BannedPhraseMatchType):
                    Optional. Match type for the banned phrase.
                ignore_diacritics (bool):
                    Optional. If true, diacritical marks (e.g.,
                    accents, umlauts) are ignored when matching
                    banned phrases. For example, "cafe" would match
                    "café".
            """

            class BannedPhraseMatchType(proto.Enum):
                r"""The matching method for the banned phrase.

                Values:
                    BANNED_PHRASE_MATCH_TYPE_UNSPECIFIED (0):
                        Defaults to SIMPLE_STRING_MATCH.
                    SIMPLE_STRING_MATCH (1):
                        The banned phrase matches if it is found
                        anywhere in the text as an exact substring.
                    WORD_BOUNDARY_STRING_MATCH (2):
                        Banned phrase only matches if the pattern
                        found in the text is surrounded by word
                        delimiters. The phrase itself may still contain
                        word delimiters.
                """

                BANNED_PHRASE_MATCH_TYPE_UNSPECIFIED = 0
                SIMPLE_STRING_MATCH = 1
                WORD_BOUNDARY_STRING_MATCH = 2

            phrase: str = proto.Field(
                proto.STRING,
                number=1,
            )
            match_type: "Assistant.CustomerPolicy.BannedPhrase.BannedPhraseMatchType" = proto.Field(
                proto.ENUM,
                number=2,
                enum="Assistant.CustomerPolicy.BannedPhrase.BannedPhraseMatchType",
            )
            ignore_diacritics: bool = proto.Field(
                proto.BOOL,
                number=3,
            )

        class ModelArmorConfig(proto.Message):
            r"""Configuration for customer defined Model Armor templates to
            be used for sanitizing user prompts and assistant responses.

            Attributes:
                user_prompt_template (str):
                    Optional. The resource name of the Model Armor template for
                    sanitizing user prompts. Format:
                    ``projects/{project}/locations/{location}/templates/{template_id}``

                    If not specified, no sanitization will be applied to the
                    user prompt.
                response_template (str):
                    Optional. The resource name of the Model Armor template for
                    sanitizing assistant responses. Format:
                    ``projects/{project}/locations/{location}/templates/{template_id}``

                    If not specified, no sanitization will be applied to the
                    assistant response.
                failure_mode (google.cloud.discoveryengine_v1beta.types.Assistant.CustomerPolicy.ModelArmorConfig.FailureMode):
                    Optional. Defines the failure mode for Model
                    Armor sanitization.
            """

            class FailureMode(proto.Enum):
                r"""Determines the behavior when Model Armor fails to process a
                request.

                Values:
                    FAILURE_MODE_UNSPECIFIED (0):
                        Unspecified failure mode, default behavior is
                        ``FAIL_CLOSED``.
                    FAIL_OPEN (1):
                        In case of a Model Armor processing failure,
                        the request is allowed to proceed without any
                        changes.
                    FAIL_CLOSED (2):
                        In case of a Model Armor processing failure,
                        the request is rejected.
                """

                FAILURE_MODE_UNSPECIFIED = 0
                FAIL_OPEN = 1
                FAIL_CLOSED = 2

            user_prompt_template: str = proto.Field(
                proto.STRING,
                number=1,
            )
            response_template: str = proto.Field(
                proto.STRING,
                number=2,
            )
            failure_mode: "Assistant.CustomerPolicy.ModelArmorConfig.FailureMode" = (
                proto.Field(
                    proto.ENUM,
                    number=3,
                    enum="Assistant.CustomerPolicy.ModelArmorConfig.FailureMode",
                )
            )

        banned_phrases: MutableSequence["Assistant.CustomerPolicy.BannedPhrase"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=1,
                message="Assistant.CustomerPolicy.BannedPhrase",
            )
        )
        model_armor_config: "Assistant.CustomerPolicy.ModelArmorConfig" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="Assistant.CustomerPolicy.ModelArmorConfig",
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
    generation_config: GenerationConfig = proto.Field(
        proto.MESSAGE,
        number=19,
        message=GenerationConfig,
    )
    web_grounding_type: WebGroundingType = proto.Field(
        proto.ENUM,
        number=4,
        enum=WebGroundingType,
    )
    default_web_grounding_toggle_off: bool = proto.Field(
        proto.BOOL,
        number=22,
    )
    enabled_tools: MutableMapping[str, ToolList] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=18,
        message=ToolList,
    )
    customer_policy: CustomerPolicy = proto.Field(
        proto.MESSAGE,
        number=12,
        message=CustomerPolicy,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=24,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=25,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
