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

from google.cloud.automl_v1.types import data_items

__protobuf__ = proto.module(
    package="google.cloud.automl.v1",
    manifest={
        "TranslationDatasetMetadata",
        "TranslationEvaluationMetrics",
        "TranslationModelMetadata",
        "TranslationAnnotation",
    },
)


class TranslationDatasetMetadata(proto.Message):
    r"""Dataset metadata that is specific to translation.

    Attributes:
        source_language_code (str):
            Required. The BCP-47 language code of the
            source language.
        target_language_code (str):
            Required. The BCP-47 language code of the
            target language.
    """

    source_language_code: str = proto.Field(
        proto.STRING,
        number=1,
    )
    target_language_code: str = proto.Field(
        proto.STRING,
        number=2,
    )


class TranslationEvaluationMetrics(proto.Message):
    r"""Evaluation metrics for the dataset.

    Attributes:
        bleu_score (float):
            Output only. BLEU score.
        base_bleu_score (float):
            Output only. BLEU score for base model.
    """

    bleu_score: float = proto.Field(
        proto.DOUBLE,
        number=1,
    )
    base_bleu_score: float = proto.Field(
        proto.DOUBLE,
        number=2,
    )


class TranslationModelMetadata(proto.Message):
    r"""Model metadata that is specific to translation.

    Attributes:
        base_model (str):
            The resource name of the model to use as a baseline to train
            the custom model. If unset, we use the default base model
            provided by Google Translate. Format:
            ``projects/{project_id}/locations/{location_id}/models/{model_id}``
        source_language_code (str):
            Output only. Inferred from the dataset.
            The source language (The BCP-47 language code)
            that is used for training.
        target_language_code (str):
            Output only. The target language (The BCP-47
            language code) that is used for training.
    """

    base_model: str = proto.Field(
        proto.STRING,
        number=1,
    )
    source_language_code: str = proto.Field(
        proto.STRING,
        number=2,
    )
    target_language_code: str = proto.Field(
        proto.STRING,
        number=3,
    )


class TranslationAnnotation(proto.Message):
    r"""Annotation details specific to translation.

    Attributes:
        translated_content (google.cloud.automl_v1.types.TextSnippet):
            Output only . The translated content.
    """

    translated_content: data_items.TextSnippet = proto.Field(
        proto.MESSAGE,
        number=1,
        message=data_items.TextSnippet,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
