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
import proto  # type: ignore

from google.cloud.dialogflowcx_v3.types import generative_settings

__protobuf__ = proto.module(
    package="google.cloud.dialogflow.cx.v3",
    manifest={
        "Generator",
        "Phrase",
        "ListGeneratorsRequest",
        "ListGeneratorsResponse",
        "GetGeneratorRequest",
        "CreateGeneratorRequest",
        "UpdateGeneratorRequest",
        "DeleteGeneratorRequest",
    },
)


class Generator(proto.Message):
    r"""Generators contain prompt to be sent to the LLM model to
    generate text. The prompt can contain parameters which will be
    resolved before calling the model. It can optionally contain
    banned phrases to ensure the model responses are safe.

    Attributes:
        name (str):
            The unique identifier of the generator. Must be set for the
            [Generators.UpdateGenerator][google.cloud.dialogflow.cx.v3.Generators.UpdateGenerator]
            method. [Generators.CreateGenerate][] populates the name
            automatically. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/generators/<GeneratorID>``.
        display_name (str):
            Required. The human-readable name of the
            generator, unique within the agent. The prompt
            contains pre-defined parameters such as
            $conversation, $last-user-utterance, etc.
            populated by Dialogflow. It can also contain
            custom placeholders which will be resolved
            during fulfillment.
        prompt_text (google.cloud.dialogflowcx_v3.types.Phrase):
            Required. Prompt for the LLM model.
        placeholders (MutableSequence[google.cloud.dialogflowcx_v3.types.Generator.Placeholder]):
            Optional. List of custom placeholders in the
            prompt text.
        llm_model_settings (google.cloud.dialogflowcx_v3.types.LlmModelSettings):
            The LLM model settings.
        model_parameter (google.cloud.dialogflowcx_v3.types.Generator.ModelParameter):
            Parameters passed to the LLM to configure its
            behavior.
    """

    class Placeholder(proto.Message):
        r"""Represents a custom placeholder in the prompt text.

        Attributes:
            id (str):
                Unique ID used to map custom placeholder to
                parameters in fulfillment.
            name (str):
                Custom placeholder value in the prompt text.
        """

        id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        name: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class ModelParameter(proto.Message):
        r"""Parameters to be passed to the LLM. If not set, default
        values will be used.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            temperature (float):
                The temperature used for sampling. Temperature sampling
                occurs after both topP and topK have been applied. Valid
                range: [0.0, 1.0] Low temperature = less random. High
                temperature = more random.

                This field is a member of `oneof`_ ``_temperature``.
            max_decode_steps (int):
                The maximum number of tokens to generate.

                This field is a member of `oneof`_ ``_max_decode_steps``.
            top_p (float):
                If set, only the tokens comprising the top top_p probability
                mass are considered. If both top_p and top_k are set, top_p
                will be used for further refining candidates selected with
                top_k. Valid range: (0.0, 1.0]. Small topP = less random.
                Large topP = more random.

                This field is a member of `oneof`_ ``_top_p``.
            top_k (int):
                If set, the sampling process in each step is limited to the
                top_k tokens with highest probabilities. Valid range: [1,
                40] or 1000+. Small topK = less random. Large topK = more
                random.

                This field is a member of `oneof`_ ``_top_k``.
        """

        temperature: float = proto.Field(
            proto.FLOAT,
            number=1,
            optional=True,
        )
        max_decode_steps: int = proto.Field(
            proto.INT32,
            number=2,
            optional=True,
        )
        top_p: float = proto.Field(
            proto.FLOAT,
            number=3,
            optional=True,
        )
        top_k: int = proto.Field(
            proto.INT32,
            number=4,
            optional=True,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    prompt_text: "Phrase" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Phrase",
    )
    placeholders: MutableSequence[Placeholder] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message=Placeholder,
    )
    llm_model_settings: generative_settings.LlmModelSettings = proto.Field(
        proto.MESSAGE,
        number=9,
        message=generative_settings.LlmModelSettings,
    )
    model_parameter: ModelParameter = proto.Field(
        proto.MESSAGE,
        number=8,
        message=ModelParameter,
    )


class Phrase(proto.Message):
    r"""Text input which can be used for prompt or banned phrases.

    Attributes:
        text (str):
            Required. Text input which can be used for
            prompt or banned phrases.
    """

    text: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListGeneratorsRequest(proto.Message):
    r"""The request message for
    [Generators.ListGenerators][google.cloud.dialogflow.cx.v3.Generators.ListGenerators].

    Attributes:
        parent (str):
            Required. The agent to list all generators for. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>``.
        language_code (str):
            The language to list generators for.
        page_size (int):
            The maximum number of items to return in a
            single page. By default 100 and at most 1000.
        page_token (str):
            The next_page_token value returned from a previous list
            request.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListGeneratorsResponse(proto.Message):
    r"""The response message for
    [Generators.ListGenerators][google.cloud.dialogflow.cx.v3.Generators.ListGenerators].

    Attributes:
        generators (MutableSequence[google.cloud.dialogflowcx_v3.types.Generator]):
            The list of generators. There will be a maximum number of
            items returned based on the page_size field in the request.
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


class GetGeneratorRequest(proto.Message):
    r"""The request message for
    [Generators.GetGenerator][google.cloud.dialogflow.cx.v3.Generators.GetGenerator].

    Attributes:
        name (str):
            Required. The name of the generator. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/generators/<GeneratorID>``.
        language_code (str):
            The language to list generators for.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateGeneratorRequest(proto.Message):
    r"""The request message for
    [Generators.CreateGenerator][google.cloud.dialogflow.cx.v3.Generators.CreateGenerator].

    Attributes:
        parent (str):
            Required. The agent to create a generator for. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>``.
        generator (google.cloud.dialogflowcx_v3.types.Generator):
            Required. The generator to create.
        language_code (str):
            The language to create generators for the following fields:

            - ``Generator.prompt_text.text`` If not specified, the
              agent's default language is used.
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
    language_code: str = proto.Field(
        proto.STRING,
        number=3,
    )


class UpdateGeneratorRequest(proto.Message):
    r"""The request message for
    [Generators.UpdateGenerator][google.cloud.dialogflow.cx.v3.Generators.UpdateGenerator].

    Attributes:
        generator (google.cloud.dialogflowcx_v3.types.Generator):
            Required. The generator to update.
        language_code (str):
            The language to list generators for.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The mask to control which fields get updated.
            If the mask is not present, all fields will be
            updated.
    """

    generator: "Generator" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Generator",
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=2,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=3,
        message=field_mask_pb2.FieldMask,
    )


class DeleteGeneratorRequest(proto.Message):
    r"""The request message for
    [Generators.DeleteGenerator][google.cloud.dialogflow.cx.v3.Generators.DeleteGenerator].

    Attributes:
        name (str):
            Required. The name of the generator to delete. Format:
            ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/generators/<GeneratorID>``.
        force (bool):
            This field has no effect for generators not being used. For
            generators that are used by pages/flows/transition route
            groups:

            - If ``force`` is set to false, an error will be returned
              with message indicating the referenced resources.
            - If ``force`` is set to true, Dialogflow will remove the
              generator, as well as any references to the generator
              (i.e. [Generator][Fulfillment.generator]) in fulfillments.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
