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
    package="google.cloud.retail.v2beta",
    manifest={
        "GenerativeQuestionsFeatureConfig",
        "GenerativeQuestionConfig",
    },
)


class GenerativeQuestionsFeatureConfig(proto.Message):
    r"""Configuration for overall generative question feature state.

    Attributes:
        catalog (str):
            Required. Resource name of the affected
            catalog. Format:
            projects/{project}/locations/{location}/catalogs/{catalog}
        feature_enabled (bool):
            Optional. Determines whether questions will
            be used at serving time. Note: This feature
            cannot be enabled until initial data
            requirements are satisfied.
        minimum_products (int):
            Optional. Minimum number of products in the
            response to trigger follow-up questions. Value
            must be 0 or positive.
    """

    catalog: str = proto.Field(
        proto.STRING,
        number=1,
    )
    feature_enabled: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    minimum_products: int = proto.Field(
        proto.INT32,
        number=3,
    )


class GenerativeQuestionConfig(proto.Message):
    r"""Configuration for a single generated question.

    Attributes:
        catalog (str):
            Required. Resource name of the catalog.
            Format:
            projects/{project}/locations/{location}/catalogs/{catalog}
        facet (str):
            Required. The facet to which the question is
            associated.
        generated_question (str):
            Output only. The LLM generated question.
        final_question (str):
            Optional. The question that will be used at serving time.
            Question can have a max length of 300 bytes. When not
            populated, generated_question should be used.
        example_values (MutableSequence[str]):
            Output only. Values that can be used to
            answer the question.
        frequency (float):
            Output only. The ratio of how often a
            question was asked.
        allowed_in_conversation (bool):
            Optional. Whether the question is asked at
            serving time.
    """

    catalog: str = proto.Field(
        proto.STRING,
        number=1,
    )
    facet: str = proto.Field(
        proto.STRING,
        number=2,
    )
    generated_question: str = proto.Field(
        proto.STRING,
        number=3,
    )
    final_question: str = proto.Field(
        proto.STRING,
        number=4,
    )
    example_values: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    frequency: float = proto.Field(
        proto.FLOAT,
        number=6,
    )
    allowed_in_conversation: bool = proto.Field(
        proto.BOOL,
        number=7,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
