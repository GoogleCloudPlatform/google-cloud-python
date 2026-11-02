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

from google.cloud.ces_v1beta.types import common

__protobuf__ = proto.module(
    package="google.cloud.ces.v1beta",
    manifest={
        "Guardrail",
    },
)


class Guardrail(proto.Message):
    r"""Guardrail contains a list of checks and balances to keep the
    agents safe and secure.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        content_filter (google.cloud.ces_v1beta.types.Guardrail.ContentFilter):
            Optional. Guardrail that bans certain content
            from being used in the conversation.

            This field is a member of `oneof`_ ``guardrail_type``.
        llm_prompt_security (google.cloud.ces_v1beta.types.Guardrail.LlmPromptSecurity):
            Optional. Guardrail that blocks the
            conversation if the prompt is considered unsafe
            based on the LLM classification.

            This field is a member of `oneof`_ ``guardrail_type``.
        llm_policy (google.cloud.ces_v1beta.types.Guardrail.LlmPolicy):
            Optional. Guardrail that blocks the
            conversation if the LLM response is considered
            violating the policy based on the LLM
            classification.

            This field is a member of `oneof`_ ``guardrail_type``.
        model_safety (google.cloud.ces_v1beta.types.Guardrail.ModelSafety):
            Optional. Guardrail that blocks the
            conversation if the LLM response is considered
            unsafe based on the model safety settings.

            This field is a member of `oneof`_ ``guardrail_type``.
        code_callback (google.cloud.ces_v1beta.types.Guardrail.CodeCallback):
            Optional. Guardrail that potentially blocks
            the conversation based on the result of the
            callback execution.

            This field is a member of `oneof`_ ``guardrail_type``.
        name (str):
            Identifier. The unique identifier of the guardrail. Format:
            ``projects/{project}/locations/{location}/apps/{app}/guardrails/{guardrail}``
        display_name (str):
            Required. Display name of the guardrail.
        description (str):
            Optional. Description of the guardrail.
        enabled (bool):
            Optional. Whether the guardrail is enabled.
        action (google.cloud.ces_v1beta.types.TriggerAction):
            Optional. Action to take when the guardrail
            is triggered.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the guardrail was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when the guardrail was
            last updated.
        etag (str):
            Etag used to ensure the object hasn't changed
            during a read-modify-write operation. If the
            etag is empty, the update will overwrite any
            concurrent changes.
    """

    class ContentFilter(proto.Message):
        r"""Guardrail that bans certain content from being used in the
        conversation.

        Attributes:
            banned_contents (MutableSequence[str]):
                Optional. List of banned phrases. Applies to
                both user inputs and agent responses.
            banned_contents_in_user_input (MutableSequence[str]):
                Optional. List of banned phrases. Applies
                only to user inputs.
            banned_contents_in_agent_response (MutableSequence[str]):
                Optional. List of banned phrases. Applies
                only to agent responses.
            match_type (google.cloud.ces_v1beta.types.Guardrail.ContentFilter.MatchType):
                Required. Match type for the content filter.
            disregard_diacritics (bool):
                Optional. If true, diacritics are ignored
                during matching.
        """

        class MatchType(proto.Enum):
            r"""Match type for the content filter.

            Values:
                MATCH_TYPE_UNSPECIFIED (0):
                    Match type is not specified.
                SIMPLE_STRING_MATCH (1):
                    Content is matched for substrings character
                    by character.
                WORD_BOUNDARY_STRING_MATCH (2):
                    Content only matches if the pattern found in
                    the text is surrounded by word delimiters.
                    Banned phrases can also contain word delimiters.
                REGEXP_MATCH (3):
                    Content is matched using regular expression
                    syntax.
            """

            MATCH_TYPE_UNSPECIFIED = 0
            SIMPLE_STRING_MATCH = 1
            WORD_BOUNDARY_STRING_MATCH = 2
            REGEXP_MATCH = 3

        banned_contents: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        banned_contents_in_user_input: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )
        banned_contents_in_agent_response: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=3,
        )
        match_type: "Guardrail.ContentFilter.MatchType" = proto.Field(
            proto.ENUM,
            number=4,
            enum="Guardrail.ContentFilter.MatchType",
        )
        disregard_diacritics: bool = proto.Field(
            proto.BOOL,
            number=5,
        )

    class LlmPromptSecurity(proto.Message):
        r"""Guardrail that blocks the conversation if the input is
        considered unsafe based on the LLM classification.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            default_settings (google.cloud.ces_v1beta.types.Guardrail.LlmPromptSecurity.DefaultSecuritySettings):
                Optional. Use the system's predefined default security
                settings. To select this mode, include an empty
                'default_settings' message in the request. The
                'default_prompt_template' field within will be populated by
                the server in the response.

                This field is a member of `oneof`_ ``security_config``.
            custom_policy (google.cloud.ces_v1beta.types.Guardrail.LlmPolicy):
                Optional. Use a user-defined LlmPolicy to
                configure the security guardrail.

                This field is a member of `oneof`_ ``security_config``.
            fail_open (bool):
                Optional. Determines the behavior when the guardrail
                encounters an LLM error.

                - If true: the guardrail is bypassed.
                - If false (default): the guardrail triggers/blocks.

                Note: If a custom policy is provided, this field is ignored
                in favor of the policy's 'fail_open' configuration.
        """

        class DefaultSecuritySettings(proto.Message):
            r"""Configuration for default system security settings.

            Attributes:
                default_prompt_template (str):
                    Output only. The default prompt template used by the system.
                    This field is for display purposes to show the user what
                    prompt the system uses by default. It is OUTPUT_ONLY.
            """

            default_prompt_template: str = proto.Field(
                proto.STRING,
                number=1,
            )

        default_settings: "Guardrail.LlmPromptSecurity.DefaultSecuritySettings" = (
            proto.Field(
                proto.MESSAGE,
                number=1,
                oneof="security_config",
                message="Guardrail.LlmPromptSecurity.DefaultSecuritySettings",
            )
        )
        custom_policy: "Guardrail.LlmPolicy" = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="security_config",
            message="Guardrail.LlmPolicy",
        )
        fail_open: bool = proto.Field(
            proto.BOOL,
            number=3,
        )

    class LlmPolicy(proto.Message):
        r"""Guardrail that blocks the conversation if the LLM response is
        considered violating the policy based on the LLM classification.

        Attributes:
            max_conversation_messages (int):
                Optional. When checking this policy, consider
                the last 'n' messages in the conversation. When
                not set a default value of 10 will be used.
            model_settings (google.cloud.ces_v1beta.types.ModelSettings):
                Optional. Model settings.
            prompt (str):
                Required. Policy prompt.
            policy_scope (google.cloud.ces_v1beta.types.Guardrail.LlmPolicy.PolicyScope):
                Required. Defines when to apply the policy check during the
                conversation. If set to ``POLICY_SCOPE_UNSPECIFIED``, the
                policy will be applied to the user input. When applying the
                policy to the agent response, additional latency will be
                introduced before the agent can respond.
            fail_open (bool):
                Optional. If an error occurs during the
                policy check, fail open and do not trigger the
                guardrail.
            allow_short_utterance (bool):
                Optional. By default, the LLM policy check is
                bypassed for short utterances. Enabling this
                setting applies the policy check to all
                utterances, including those that would normally
                be skipped.
        """

        class PolicyScope(proto.Enum):
            r"""Defines when to apply the policy check during the
            conversation.

            Values:
                POLICY_SCOPE_UNSPECIFIED (0):
                    Policy scope is not specified.
                USER_QUERY (1):
                    Policy check is triggered on user input.
                AGENT_RESPONSE (2):
                    Policy check is triggered on agent response.
                    Applying this policy scope will introduce
                    additional latency before the agent can respond.
                USER_QUERY_AND_AGENT_RESPONSE (3):
                    Policy check is triggered on both user input
                    and agent response. Applying this policy scope
                    will introduce additional latency before the
                    agent can respond.
            """

            POLICY_SCOPE_UNSPECIFIED = 0
            USER_QUERY = 1
            AGENT_RESPONSE = 2
            USER_QUERY_AND_AGENT_RESPONSE = 3

        max_conversation_messages: int = proto.Field(
            proto.INT32,
            number=1,
        )
        model_settings: common.ModelSettings = proto.Field(
            proto.MESSAGE,
            number=2,
            message=common.ModelSettings,
        )
        prompt: str = proto.Field(
            proto.STRING,
            number=3,
        )
        policy_scope: "Guardrail.LlmPolicy.PolicyScope" = proto.Field(
            proto.ENUM,
            number=4,
            enum="Guardrail.LlmPolicy.PolicyScope",
        )
        fail_open: bool = proto.Field(
            proto.BOOL,
            number=5,
        )
        allow_short_utterance: bool = proto.Field(
            proto.BOOL,
            number=6,
        )

    class ModelSafety(proto.Message):
        r"""Model safety settings overrides. When this is set, it will
        override the default settings and trigger the guardrail if the
        response is considered unsafe.

        Attributes:
            safety_settings (MutableSequence[google.cloud.ces_v1beta.types.Guardrail.ModelSafety.SafetySetting]):
                Required. List of safety settings.
        """

        class HarmCategory(proto.Enum):
            r"""Harm category.

            Values:
                HARM_CATEGORY_UNSPECIFIED (0):
                    The harm category is unspecified.
                HARM_CATEGORY_HATE_SPEECH (1):
                    The harm category is hate speech.
                HARM_CATEGORY_DANGEROUS_CONTENT (2):
                    The harm category is dangerous content.
                HARM_CATEGORY_HARASSMENT (3):
                    The harm category is harassment.
                HARM_CATEGORY_SEXUALLY_EXPLICIT (4):
                    The harm category is sexually explicit
                    content.
            """

            HARM_CATEGORY_UNSPECIFIED = 0
            HARM_CATEGORY_HATE_SPEECH = 1
            HARM_CATEGORY_DANGEROUS_CONTENT = 2
            HARM_CATEGORY_HARASSMENT = 3
            HARM_CATEGORY_SEXUALLY_EXPLICIT = 4

        class HarmBlockThreshold(proto.Enum):
            r"""Probability based thresholds levels for blocking.

            Values:
                HARM_BLOCK_THRESHOLD_UNSPECIFIED (0):
                    Unspecified harm block threshold.
                BLOCK_LOW_AND_ABOVE (1):
                    Block low threshold and above (i.e. block
                    more).
                BLOCK_MEDIUM_AND_ABOVE (2):
                    Block medium threshold and above.
                BLOCK_ONLY_HIGH (3):
                    Block only high threshold (i.e. block less).
                BLOCK_NONE (4):
                    Block none.
                OFF (5):
                    Turn off the safety filter.
            """

            HARM_BLOCK_THRESHOLD_UNSPECIFIED = 0
            BLOCK_LOW_AND_ABOVE = 1
            BLOCK_MEDIUM_AND_ABOVE = 2
            BLOCK_ONLY_HIGH = 3
            BLOCK_NONE = 4
            OFF = 5

        class SafetySetting(proto.Message):
            r"""Safety setting.

            Attributes:
                category (google.cloud.ces_v1beta.types.Guardrail.ModelSafety.HarmCategory):
                    Required. The harm category.
                threshold (google.cloud.ces_v1beta.types.Guardrail.ModelSafety.HarmBlockThreshold):
                    Required. The harm block threshold.
            """

            category: "Guardrail.ModelSafety.HarmCategory" = proto.Field(
                proto.ENUM,
                number=1,
                enum="Guardrail.ModelSafety.HarmCategory",
            )
            threshold: "Guardrail.ModelSafety.HarmBlockThreshold" = proto.Field(
                proto.ENUM,
                number=2,
                enum="Guardrail.ModelSafety.HarmBlockThreshold",
            )

        safety_settings: MutableSequence["Guardrail.ModelSafety.SafetySetting"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=1,
                message="Guardrail.ModelSafety.SafetySetting",
            )
        )

    class CodeCallback(proto.Message):
        r"""Guardrail that blocks the conversation based on the code
        callbacks provided.

        Attributes:
            before_agent_callback (google.cloud.ces_v1beta.types.Callback):
                Optional. The callback to execute before the
                agent is called. Each callback function is
                expected to return a structure (e.g., a dict or
                object) containing at least:

                  - 'decision': Either 'OK' or 'TRIGGER'.
                  - 'reason': A string explaining the decision.
                  A 'TRIGGER' decision may halt further
                  processing.
            after_agent_callback (google.cloud.ces_v1beta.types.Callback):
                Optional. The callback to execute after the
                agent is called. Each callback function is
                expected to return a structure (e.g., a dict or
                object) containing at least:

                  - 'decision': Either 'OK' or 'TRIGGER'.
                  - 'reason': A string explaining the decision.
                  A 'TRIGGER' decision may halt further
                  processing.
            before_model_callback (google.cloud.ces_v1beta.types.Callback):
                Optional. The callback to execute before the
                model is called. If there are multiple calls to
                the model, the callback will be executed
                multiple times. Each callback function is
                expected to return a structure (e.g., a dict or
                object) containing at least:

                  - 'decision': Either 'OK' or 'TRIGGER'.
                  - 'reason': A string explaining the decision.
                  A 'TRIGGER' decision may halt further
                  processing.
            after_model_callback (google.cloud.ces_v1beta.types.Callback):
                Optional. The callback to execute after the
                model is called. If there are multiple calls to
                the model, the callback will be executed
                multiple times. Each callback function is
                expected to return a structure (e.g., a dict or
                object) containing at least:

                  - 'decision': Either 'OK' or 'TRIGGER'.
                  - 'reason': A string explaining the decision.
                  A 'TRIGGER' decision may halt further
                  processing.
        """

        before_agent_callback: common.Callback = proto.Field(
            proto.MESSAGE,
            number=1,
            message=common.Callback,
        )
        after_agent_callback: common.Callback = proto.Field(
            proto.MESSAGE,
            number=2,
            message=common.Callback,
        )
        before_model_callback: common.Callback = proto.Field(
            proto.MESSAGE,
            number=3,
            message=common.Callback,
        )
        after_model_callback: common.Callback = proto.Field(
            proto.MESSAGE,
            number=4,
            message=common.Callback,
        )

    content_filter: ContentFilter = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="guardrail_type",
        message=ContentFilter,
    )
    llm_prompt_security: LlmPromptSecurity = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="guardrail_type",
        message=LlmPromptSecurity,
    )
    llm_policy: LlmPolicy = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="guardrail_type",
        message=LlmPolicy,
    )
    model_safety: ModelSafety = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="guardrail_type",
        message=ModelSafety,
    )
    code_callback: CodeCallback = proto.Field(
        proto.MESSAGE,
        number=14,
        oneof="guardrail_type",
        message=CodeCallback,
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
    enabled: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    action: common.TriggerAction = proto.Field(
        proto.MESSAGE,
        number=5,
        message=common.TriggerAction,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=11,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
