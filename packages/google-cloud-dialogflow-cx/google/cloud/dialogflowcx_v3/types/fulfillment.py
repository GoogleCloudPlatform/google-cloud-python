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
import proto  # type: ignore

from google.cloud.dialogflowcx_v3.types import (
    advanced_settings as gcdc_advanced_settings,
)
from google.cloud.dialogflowcx_v3.types import response_message

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.cx.v3",
    manifest={
        "Fulfillment",
    },
)


class Fulfillment(proto.Message):
    r"""A fulfillment can do one or more of the following actions at the
    same time:

    - Generate rich message responses.
    - Set parameter values.
    - Call the webhook.

    Fulfillments can be called at various stages in the
    [Page][google.cloud.dialogflow.cx.v3.Page] or
    [Form][google.cloud.dialogflow.cx.v3.Form] lifecycle. For example,
    when a
    [DetectIntentRequest][google.cloud.dialogflow.cx.v3.DetectIntentRequest]
    drives a session to enter a new page, the page's entry fulfillment
    can add a static response to the
    [QueryResult][google.cloud.dialogflow.cx.v3.QueryResult] in the
    returning
    [DetectIntentResponse][google.cloud.dialogflow.cx.v3.DetectIntentResponse],
    call the webhook (for example, to load user data from a database),
    or both.

    Attributes:
        messages (MutableSequence[google.cloud.dialogflowcx_v3.types.ResponseMessage]):
            The list of rich message responses to present
            to the user.
        webhook (str):
            The webhook to call. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/webhooks/<WebhookID>``.
        return_partial_responses (bool):
            Whether Dialogflow should return currently
            queued fulfillment response messages in
            streaming APIs. If a webhook is specified, it
            happens before Dialogflow invokes webhook.
            Warning:

            1) This flag only affects streaming API.
            Responses are still queued and returned once in
            non-streaming API.
            2) The flag can be enabled in any fulfillment
            but only the first 3 partial responses will be
            returned. You may only want to apply it to
            fulfillments that have slow webhooks.
        tag (str):
            The value of this field will be populated in the
            [WebhookRequest][google.cloud.dialogflow.cx.v3.WebhookRequest]
            ``fulfillmentInfo.tag`` field by Dialogflow when the
            associated webhook is called. The tag is typically used by
            the webhook service to identify which fulfillment is being
            called, but it could be used for other purposes. This field
            is required if ``webhook`` is specified.
        code_block_function (str):
            Optional. The name of the code block function
            to execute, if this is a code block fulfillment.
            The code block itself is implied by the
            fulfillment's parent, e.g. a playbook.
        set_parameter_actions (MutableSequence[google.cloud.dialogflowcx_v3.types.Fulfillment.SetParameterAction]):
            Set parameter values before executing the
            webhook.
        conditional_cases (MutableSequence[google.cloud.dialogflowcx_v3.types.Fulfillment.ConditionalCases]):
            Conditional cases for this fulfillment.
        advanced_settings (google.cloud.dialogflowcx_v3.types.AdvancedSettings):
            Hierarchical advanced settings for this
            fulfillment. The settings exposed at the lower
            level overrides the settings exposed at the
            higher level.
        enable_generative_fallback (bool):
            If the flag is true, the agent will utilize LLM to generate
            a text response. If LLM generation fails, the defined
            [responses][google.cloud.dialogflow.cx.v3.Fulfillment.messages]
            in the fulfillment will be respected. This flag is only
            useful for fulfillments associated with no-match event
            handlers.
        generators (MutableSequence[google.cloud.dialogflowcx_v3.types.Fulfillment.GeneratorSettings]):
            A list of Generators to be called during this
            fulfillment.
    """

    class SetParameterAction(proto.Message):
        r"""Setting a parameter value.

        Attributes:
            parameter (str):
                Display name of the parameter.
            value (google.protobuf.struct_pb2.Value):
                The new value of the parameter. A null value
                clears the parameter.
        """

        parameter: str = proto.Field(
            proto.STRING,
            number=1,
        )
        value: struct_pb2.Value = proto.Field(
            proto.MESSAGE,
            number=2,
            message=struct_pb2.Value,
        )

    class ConditionalCases(proto.Message):
        r"""A list of cascading if-else conditions. Cases are mutually
        exclusive. The first one with a matching condition is selected,
        all the rest ignored.

        Attributes:
            cases (MutableSequence[google.cloud.dialogflowcx_v3.types.Fulfillment.ConditionalCases.Case]):
                A list of cascading if-else conditions.
        """

        class Case(proto.Message):
            r"""Each case has a Boolean condition. When it is evaluated to be
            True, the corresponding messages will be selected and evaluated
            recursively.

            Attributes:
                condition (str):
                    The condition to activate and select this case. Empty means
                    the condition is always true. The condition is evaluated
                    against [form parameters][Form.parameters] or [session
                    parameters][SessionInfo.parameters].

                    See the `conditions
                    reference <https://cloud.google.com/dialogflow/cx/docs/reference/condition>`__.
                case_content (MutableSequence[google.cloud.dialogflowcx_v3.types.Fulfillment.ConditionalCases.Case.CaseContent]):
                    A list of case content.
            """

            class CaseContent(proto.Message):
                r"""The list of messages or conditional cases to activate for
                this case.

                This message has `oneof`_ fields (mutually exclusive fields).
                For each oneof, at most one member field can be set at the same time.
                Setting any member of the oneof automatically clears all other
                members.

                .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

                Attributes:
                    message (google.cloud.dialogflowcx_v3.types.ResponseMessage):
                        Returned message.

                        This field is a member of `oneof`_ ``cases_or_message``.
                    additional_cases (google.cloud.dialogflowcx_v3.types.Fulfillment.ConditionalCases):
                        Additional cases to be evaluated.

                        This field is a member of `oneof`_ ``cases_or_message``.
                """

                message: response_message.ResponseMessage = proto.Field(
                    proto.MESSAGE,
                    number=1,
                    oneof="cases_or_message",
                    message=response_message.ResponseMessage,
                )
                additional_cases: "Fulfillment.ConditionalCases" = proto.Field(
                    proto.MESSAGE,
                    number=2,
                    oneof="cases_or_message",
                    message="Fulfillment.ConditionalCases",
                )

            condition: str = proto.Field(
                proto.STRING,
                number=1,
            )
            case_content: MutableSequence[
                "Fulfillment.ConditionalCases.Case.CaseContent"
            ] = proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message="Fulfillment.ConditionalCases.Case.CaseContent",
            )

        cases: MutableSequence["Fulfillment.ConditionalCases.Case"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=1,
                message="Fulfillment.ConditionalCases.Case",
            )
        )

    class GeneratorSettings(proto.Message):
        r"""Generator settings used by the LLM to generate a text
        response.

        Attributes:
            generator (str):
                Required. The generator to call. Format:
                ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/generators/<GeneratorID>``.
            input_parameters (MutableMapping[str, str]):
                Map from [placeholder parameter][Generator.Parameter.id] in
                the [Generator][google.cloud.dialogflow.cx.v3.Generator] to
                corresponding session parameters. By default, Dialogflow
                uses the session parameter with the same name to fill in the
                generator template. e.g. If there is a placeholder parameter
                ``city`` in the Generator, Dialogflow default to fill in the
                ``$city`` with ``$session.params.city``. However, you may
                choose to fill ``$city`` with
                ``$session.params.desination-city``.

                - Map key: [parameter ID][Genrator.Parameter.id]
                - Map value: session parameter name
            output_parameter (str):
                Required. Output parameter which should
                contain the generator response.
        """

        generator: str = proto.Field(
            proto.STRING,
            number=1,
        )
        input_parameters: MutableMapping[str, str] = proto.MapField(
            proto.STRING,
            proto.STRING,
            number=2,
        )
        output_parameter: str = proto.Field(
            proto.STRING,
            number=3,
        )

    messages: MutableSequence[response_message.ResponseMessage] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=response_message.ResponseMessage,
    )
    webhook: str = proto.Field(
        proto.STRING,
        number=2,
    )
    return_partial_responses: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    tag: str = proto.Field(
        proto.STRING,
        number=3,
    )
    code_block_function: str = proto.Field(
        proto.STRING,
        number=17,
    )
    set_parameter_actions: MutableSequence[SetParameterAction] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=SetParameterAction,
    )
    conditional_cases: MutableSequence[ConditionalCases] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message=ConditionalCases,
    )
    advanced_settings: gcdc_advanced_settings.AdvancedSettings = proto.Field(
        proto.MESSAGE,
        number=7,
        message=gcdc_advanced_settings.AdvancedSettings,
    )
    enable_generative_fallback: bool = proto.Field(
        proto.BOOL,
        number=12,
    )
    generators: MutableSequence[GeneratorSettings] = proto.RepeatedField(
        proto.MESSAGE,
        number=13,
        message=GeneratorSettings,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
