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
    package="google.cloud.dialogflow.cx.v3beta1",
    manifest={
        "SafetySettings",
    },
)


class SafetySettings(proto.Message):
    r"""Settings for Generative Safety.

    Attributes:
        default_banned_phrase_match_strategy (google.cloud.dialogflowcx_v3beta1.types.SafetySettings.PhraseMatchStrategy):
            Optional. Default phrase match strategy for
            banned phrases.
        banned_phrases (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.SafetySettings.Phrase]):
            Banned phrases for generated text.
        rai_settings (google.cloud.dialogflowcx_v3beta1.types.SafetySettings.RaiSettings):
            Optional. Settings for Responsible AI checks.
        default_rai_settings (google.cloud.dialogflowcx_v3beta1.types.SafetySettings.RaiSettings):
            Optional. Immutable. Default RAI settings to
            be annotated on the agent, so that users will be
            able to restore their RAI configurations to the
            default settings. Read-only field for the API
            proto only.
        prompt_security_settings (google.cloud.dialogflowcx_v3beta1.types.SafetySettings.PromptSecuritySettings):
            Optional. Settings for prompt security
            checks.
    """

    class PhraseMatchStrategy(proto.Enum):
        r"""Strategy for matching phrases.

        Values:
            PHRASE_MATCH_STRATEGY_UNSPECIFIED (0):
                Unspecified, defaults to PARTIAL_MATCH.
            PARTIAL_MATCH (1):
                Text that contains the phrase as a substring
                will be matched, e.g. "foo" will match
                "afoobar".
            WORD_MATCH (2):
                Text that contains the tokenized words of the
                phrase will be matched, e.g. "foo" will match "a
                foo bar" and "foo bar", but not "foobar".
        """

        PHRASE_MATCH_STRATEGY_UNSPECIFIED = 0
        PARTIAL_MATCH = 1
        WORD_MATCH = 2

    class Phrase(proto.Message):
        r"""Text input which can be used for prompt or banned phrases.

        Attributes:
            text (str):
                Required. Text input which can be used for
                prompt or banned phrases.
            language_code (str):
                Required. Language code of the phrase.
        """

        text: str = proto.Field(
            proto.STRING,
            number=1,
        )
        language_code: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class RaiSettings(proto.Message):
        r"""Settings for Responsible AI.

        Attributes:
            category_filters (MutableSequence[google.cloud.dialogflowcx_v3beta1.types.SafetySettings.RaiSettings.CategoryFilter]):
                Optional. RAI blocking configurations.
        """

        class SafetyFilterLevel(proto.Enum):
            r"""Sensitivity level for RAI categories.

            Values:
                SAFETY_FILTER_LEVEL_UNSPECIFIED (0):
                    Unspecified -- uses default sensitivity
                    levels.
                BLOCK_NONE (1):
                    Block no text -- effectively disables the
                    category.
                BLOCK_FEW (2):
                    Block a few suspicious texts.
                BLOCK_SOME (3):
                    Block some suspicious texts.
                BLOCK_MOST (4):
                    Block most suspicious texts.
            """

            SAFETY_FILTER_LEVEL_UNSPECIFIED = 0
            BLOCK_NONE = 1
            BLOCK_FEW = 2
            BLOCK_SOME = 3
            BLOCK_MOST = 4

        class SafetyCategory(proto.Enum):
            r"""RAI categories to configure.

            Values:
                SAFETY_CATEGORY_UNSPECIFIED (0):
                    Unspecified.
                DANGEROUS_CONTENT (1):
                    Dangerous content.
                HATE_SPEECH (2):
                    Hate speech.
                HARASSMENT (3):
                    Harassment.
                SEXUALLY_EXPLICIT_CONTENT (4):
                    Sexually explicit content.
            """

            SAFETY_CATEGORY_UNSPECIFIED = 0
            DANGEROUS_CONTENT = 1
            HATE_SPEECH = 2
            HARASSMENT = 3
            SEXUALLY_EXPLICIT_CONTENT = 4

        class CategoryFilter(proto.Message):
            r"""Configuration of the sensitivity level for blocking an RAI
            category.

            Attributes:
                category (google.cloud.dialogflowcx_v3beta1.types.SafetySettings.RaiSettings.SafetyCategory):
                    RAI category to configure.
                filter_level (google.cloud.dialogflowcx_v3beta1.types.SafetySettings.RaiSettings.SafetyFilterLevel):
                    Blocking sensitivity level to configure for
                    the RAI category.
            """

            category: "SafetySettings.RaiSettings.SafetyCategory" = proto.Field(
                proto.ENUM,
                number=1,
                enum="SafetySettings.RaiSettings.SafetyCategory",
            )
            filter_level: "SafetySettings.RaiSettings.SafetyFilterLevel" = proto.Field(
                proto.ENUM,
                number=2,
                enum="SafetySettings.RaiSettings.SafetyFilterLevel",
            )

        category_filters: MutableSequence[
            "SafetySettings.RaiSettings.CategoryFilter"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message="SafetySettings.RaiSettings.CategoryFilter",
        )

    class PromptSecuritySettings(proto.Message):
        r"""Settings for prompt security checks.

        Attributes:
            enable_prompt_security (bool):
                Optional. Enable prompt security checks.
        """

        enable_prompt_security: bool = proto.Field(
            proto.BOOL,
            number=1,
        )

    default_banned_phrase_match_strategy: PhraseMatchStrategy = proto.Field(
        proto.ENUM,
        number=4,
        enum=PhraseMatchStrategy,
    )
    banned_phrases: MutableSequence[Phrase] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=Phrase,
    )
    rai_settings: RaiSettings = proto.Field(
        proto.MESSAGE,
        number=2,
        message=RaiSettings,
    )
    default_rai_settings: RaiSettings = proto.Field(
        proto.MESSAGE,
        number=3,
        message=RaiSettings,
    )
    prompt_security_settings: PromptSecuritySettings = proto.Field(
        proto.MESSAGE,
        number=8,
        message=PromptSecuritySettings,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
