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

from google.cloud.dialogflowcx_v3.types import safety_settings

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.cx.v3",
    manifest={
        "GenerativeSettings",
        "LlmModelSettings",
    },
)


class GenerativeSettings(proto.Message):
    r"""Settings for Generative AI.

    Attributes:
        name (str):
            Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/generativeSettings``.
        fallback_settings (google.cloud.dialogflowcx_v3.types.GenerativeSettings.FallbackSettings):
            Settings for Generative Fallback.
        generative_safety_settings (google.cloud.dialogflowcx_v3.types.SafetySettings):
            Settings for Generative Safety.
        knowledge_connector_settings (google.cloud.dialogflowcx_v3.types.GenerativeSettings.KnowledgeConnectorSettings):
            Settings for knowledge connector.
        language_code (str):
            Language for this settings.
        llm_model_settings (google.cloud.dialogflowcx_v3.types.LlmModelSettings):
            LLM model settings.
    """

    class FallbackSettings(proto.Message):
        r"""Settings for Generative Fallback.

        Attributes:
            selected_prompt (str):
                Display name of the selected prompt.
            prompt_templates (MutableSequence[google.cloud.dialogflowcx_v3.types.GenerativeSettings.FallbackSettings.PromptTemplate]):
                Stored prompts that can be selected, for
                example default templates like "conservative" or
                "chatty", or user defined ones.
        """

        class PromptTemplate(proto.Message):
            r"""Prompt template.

            Attributes:
                display_name (str):
                    Prompt name.
                prompt_text (str):
                    Prompt text that is sent to a LLM on no-match
                    default, placeholders are filled downstream. For
                    example: "Here is a conversation $conversation,
                    a response is: ".
                frozen (bool):
                    If the flag is true, the prompt is frozen and
                    cannot be modified by users.
            """

            display_name: str = proto.Field(
                proto.STRING,
                number=1,
            )
            prompt_text: str = proto.Field(
                proto.STRING,
                number=2,
            )
            frozen: bool = proto.Field(
                proto.BOOL,
                number=3,
            )

        selected_prompt: str = proto.Field(
            proto.STRING,
            number=3,
        )
        prompt_templates: MutableSequence[
            "GenerativeSettings.FallbackSettings.PromptTemplate"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message="GenerativeSettings.FallbackSettings.PromptTemplate",
        )

    class KnowledgeConnectorSettings(proto.Message):
        r"""Settings for knowledge connector. These parameters are used for LLM
        prompt like "You are . You are a helpful and verbose
        <agent_identity> at , <business_description>. Your task is to help
        humans on <agent_scope>".

        Attributes:
            business (str):
                Name of the company, organization or other
                entity that the agent represents. Used for
                knowledge connector LLM prompt and for knowledge
                search.
            agent (str):
                Name of the virtual agent. Used for LLM
                prompt. Can be left empty.
            agent_identity (str):
                Identity of the agent, e.g. "virtual agent",
                "AI assistant".
            business_description (str):
                Company description, used for LLM prompt,
                e.g. "a family company selling freshly roasted
                coffee beans".
            agent_scope (str):
                Agent scope, e.g. "Example company website",
                "internal Example company website for
                employees", "manual of car owner".
            disable_data_store_fallback (bool):
                Whether to disable fallback to Data Store
                search results (in case the LLM couldn't pick a
                proper answer). Per default the feature is
                enabled.
        """

        business: str = proto.Field(
            proto.STRING,
            number=1,
        )
        agent: str = proto.Field(
            proto.STRING,
            number=2,
        )
        agent_identity: str = proto.Field(
            proto.STRING,
            number=3,
        )
        business_description: str = proto.Field(
            proto.STRING,
            number=4,
        )
        agent_scope: str = proto.Field(
            proto.STRING,
            number=5,
        )
        disable_data_store_fallback: bool = proto.Field(
            proto.BOOL,
            number=8,
        )

    name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    fallback_settings: FallbackSettings = proto.Field(
        proto.MESSAGE,
        number=1,
        message=FallbackSettings,
    )
    generative_safety_settings: safety_settings.SafetySettings = proto.Field(
        proto.MESSAGE,
        number=3,
        message=safety_settings.SafetySettings,
    )
    knowledge_connector_settings: KnowledgeConnectorSettings = proto.Field(
        proto.MESSAGE,
        number=7,
        message=KnowledgeConnectorSettings,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=4,
    )
    llm_model_settings: "LlmModelSettings" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="LlmModelSettings",
    )


class LlmModelSettings(proto.Message):
    r"""Settings for LLM models.

    Attributes:
        model (str):
            The selected LLM model.
        prompt_text (str):
            The custom prompt to use.
    """

    model: str = proto.Field(
        proto.STRING,
        number=1,
    )
    prompt_text: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
