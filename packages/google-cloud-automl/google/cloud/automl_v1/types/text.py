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

from google.cloud.automl_v1.types import classification

__protobuf__ = proto.module(
    package="google.cloud.automl.v1",
    manifest={
        "TextClassificationDatasetMetadata",
        "TextClassificationModelMetadata",
        "TextExtractionDatasetMetadata",
        "TextExtractionModelMetadata",
        "TextSentimentDatasetMetadata",
        "TextSentimentModelMetadata",
    },
)


class TextClassificationDatasetMetadata(proto.Message):
    r"""Dataset metadata for classification.

    Attributes:
        classification_type (google.cloud.automl_v1.types.ClassificationType):
            Required. Type of the classification problem.
    """

    classification_type: classification.ClassificationType = proto.Field(
        proto.ENUM,
        number=1,
        enum=classification.ClassificationType,
    )


class TextClassificationModelMetadata(proto.Message):
    r"""Model metadata that is specific to text classification.

    Attributes:
        classification_type (google.cloud.automl_v1.types.ClassificationType):
            Output only. Classification type of the
            dataset used to train this model.
    """

    classification_type: classification.ClassificationType = proto.Field(
        proto.ENUM,
        number=3,
        enum=classification.ClassificationType,
    )


class TextExtractionDatasetMetadata(proto.Message):
    r"""Dataset metadata that is specific to text extraction"""


class TextExtractionModelMetadata(proto.Message):
    r"""Model metadata that is specific to text extraction."""


class TextSentimentDatasetMetadata(proto.Message):
    r"""Dataset metadata for text sentiment.

    Attributes:
        sentiment_max (int):
            Required. A sentiment is expressed as an integer ordinal,
            where higher value means a more positive sentiment. The
            range of sentiments that will be used is between 0 and
            sentiment_max (inclusive on both ends), and all the values
            in the range must be represented in the dataset before a
            model can be created. sentiment_max value must be between 1
            and 10 (inclusive).
    """

    sentiment_max: int = proto.Field(
        proto.INT32,
        number=1,
    )


class TextSentimentModelMetadata(proto.Message):
    r"""Model metadata that is specific to text sentiment."""


__all__ = tuple(sorted(__protobuf__.manifest))
